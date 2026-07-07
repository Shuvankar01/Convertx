"""Shared FastAPI dependencies."""
from __future__ import annotations

from fastapi import Depends, Request
from sqlalchemy.orm import Session

from app.config import Settings, get_settings
from app.db.session import get_db
from app.services.settings_service import SettingsService


def app_settings(db: Session = Depends(get_db)):
    return SettingsService(db).get()


def is_htmx(request: Request) -> bool:
    return request.headers.get("HX-Request", "").lower() == "true"


__all__ = ["Settings", "get_settings", "get_db", "app_settings", "is_htmx"]
