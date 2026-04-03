"""Authentication endpoints."""

from fastapi import APIRouter, Depends, status

from ..schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse
from ..services.auth_service import AuthService
from .dependencies import get_auth_service, get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, service: AuthService = Depends(get_auth_service)):
    """Register a new user and return a JWT."""
    _, token = service.register(
        username=payload.username,
        email=payload.email,
        password=payload.password,
        title=payload.title,
    )
    return TokenResponse(access_token=token)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, service: AuthService = Depends(get_auth_service)):
    """Authenticate a user and return a JWT."""
    _, token = service.login(username=payload.username, password=payload.password)
    return TokenResponse(access_token=token)


@router.get("/me", response_model=UserResponse)
def me(current_user=Depends(get_current_user)):
    """Return the authenticated user profile."""
    return current_user

