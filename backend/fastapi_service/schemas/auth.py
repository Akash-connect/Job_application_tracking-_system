"""Pydantic schemas for authentication flows."""

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class RegisterRequest(BaseModel):
    """Payload for creating a new user."""

    username: str = Field(min_length=3, max_length=150)
    email: EmailStr
    password: str = Field(min_length=8)
    title: str | None = Field(default=None, max_length=120)


class LoginRequest(BaseModel):
    """Payload for signing in."""

    username: str
    password: str


class TokenResponse(BaseModel):
    """JWT token response."""

    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    """Public representation of a user."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    title: str | None
    theme_preference: str

