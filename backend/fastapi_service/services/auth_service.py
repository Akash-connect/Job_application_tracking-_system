"""Business logic for registration, login, and current-user lookup."""

from fastapi import HTTPException, status
from jose import JWTError, jwt

from accounts.models import User

from ..core.config import settings
from ..core.security import create_access_token, get_password_hash, verify_password
from ..repositories.auth_repository import AuthRepository


class AuthService:
    """Coordinate auth workflows around Django's user model."""

    def register(self, username: str, email: str, password: str, title: str | None) -> tuple[User, str]:
        if AuthRepository.get_by_username(username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
        password_hash = get_password_hash(password)
        user = AuthRepository.create_user(username=username, email=email, password_hash=password_hash, title=title)
        token = create_access_token(subject=str(user.id))
        return user, token

    def login(self, username: str, password: str) -> tuple[User, str]:
        user = AuthRepository.get_by_username(username)
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
        token = create_access_token(subject=str(user.id))
        return user, token

    def current_user(self, token: str) -> User:
        try:
            payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
            subject = payload.get("sub")
            if not subject:
                raise ValueError("Missing sub")
        except (JWTError, ValueError) as exc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc

        user = User.objects.filter(id=int(subject)).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user

