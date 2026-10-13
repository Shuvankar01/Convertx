"""Application configuration via pydantic-settings."""
from __future__ import annotations

import tempfile
from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent
DB_FILENAME = "convertx.db"


def _is_writable_dir(directory: Path) -> bool:
    """Return True only if a file can actually be created in ``directory``."""
    probe = directory / ".convertx-write-probe"
    try:
        probe.touch()
    except OSError:
        return False
    finally:
        probe.unlink(missing_ok=True)
    return True


def default_database_url() -> str:
    """Resolve the default SQLite URL.

    Locally the database file lives next to the repository root, exactly as
    before. Some serverless runtimes (Vercel Functions, for example) mount the
    project directory read-only, which makes ``init_db()`` fail on startup, so
    fall back to the system temp directory there.

    That fallback storage is *ephemeral*: it is discarded whenever the instance
    is replaced or redeployed. Set ``CONVERTX_DATABASE_URL`` to a durable
    datastore when that matters — see the README section "Deployment — Vercel".
    """
    local_path = BASE_DIR.parent / DB_FILENAME
    if _is_writable_dir(local_path.parent):
        return f"sqlite:///{local_path}"
    return f"sqlite:///{Path(tempfile.gettempdir()) / DB_FILENAME}"


class Settings(BaseSettings):
    """Runtime configuration. Override via env vars prefixed with ``CONVERTX_``."""

    app_name: str = "ConvertX"
    tagline: str = "Smart Unit Converter for Everyday, Academic, and Technical Use"
    debug: bool = True

    database_url: str = Field(
        default_factory=default_database_url,
        description=(
            "SQLAlchemy database URL. Defaults to a local SQLite file; falls "
            "back to a writable temp directory on read-only filesystems."
        ),
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
