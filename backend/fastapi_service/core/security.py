"""Authentication helpers for password hashing and JWT handling."""

from datetime import datetime, timedelta, timezone

from django.contrib.auth.hashers import check_password, make_password
from jose import jwt

from .config import settings


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a Django-compatible hash."""
    return check_password(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a plain password using Django's password hasher."""
    return make_password(password)


def create_access_token(subject: str) -> str:
    """Create a signed JWT for the provided subject."""
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {"sub": subject, "exp": expires}
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
