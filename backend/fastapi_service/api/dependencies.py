"""Reusable FastAPI dependencies."""

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from ..services.auth_service import AuthService

auth_scheme = HTTPBearer(auto_error=True)


def get_auth_service() -> AuthService:
    """Provide the auth service instance."""
    return AuthService()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
    auth_service: AuthService = Depends(get_auth_service),
):
    """Resolve the authenticated user from the bearer token."""
    return auth_service.current_user(credentials.credentials)

