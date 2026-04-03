"""Typed settings for the FastAPI service."""

from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(Path(__file__).resolve().parents[3] / ".env")


class Settings(BaseSettings):
    """Runtime configuration for the API service."""

    app_name: str = "JATS API"
    api_prefix: str = "/api/v1"
    host: str = "0.0.0.0"
    port: int = 8001
    jwt_secret_key: str = "insecure-jwt-secret"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 120

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
    )


settings = Settings()

