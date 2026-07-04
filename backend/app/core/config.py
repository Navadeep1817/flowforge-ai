"""
Application configuration.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    APP_NAME: str = "FlowForge AI"
    APP_VERSION: str = "0.2.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    DATABASE_URL: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/flowforge"
    )

    REDIS_URL: str = "redis://localhost:6379/0"

    JWT_SECRET: str = "change-me"

    GROQ_API_KEY: str = ""


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings() 