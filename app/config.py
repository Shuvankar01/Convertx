"""Application configuration via pydantic-settings."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """Runtime configuration. Override via env vars prefixed with ``CONVERTX_``."""

    app_name: str = "ConvertX"
    tagline: str = "Smart Unit Converter for Everyday, Academic, and Technical Use"
    debug: bool = True

    database_url: str = Field(
        default=f"sqlite:///{BASE_DIR.parent / 'convertx.db'}",
        description="SQLAlchemy database URL. Swap in a Postgres URL in production.",
    )

    templates_dir: Path = BASE_DIR / "templates"
    static_dir: Path = BASE_DIR / "static"

    default_precision: int = 4
    max_history_items: int = 200

    model_config = SettingsConfigDict(
        env_prefix="CONVERTX_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Cached settings singleton."""
    return Settings()
