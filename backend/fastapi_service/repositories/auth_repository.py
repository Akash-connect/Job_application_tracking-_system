"""Repository helpers for user account persistence."""

from accounts.models import User


class AuthRepository:
    """Encapsulate user persistence details."""

    @staticmethod
    def get_by_username(username: str) -> User | None:
        return User.objects.filter(username=username).first()

    @staticmethod
    def create_user(username: str, email: str, password_hash: str, title: str | None = None) -> User:
        return User.objects.create(username=username, email=email, password=password_hash, title=title or "")

