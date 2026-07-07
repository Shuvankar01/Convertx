"""Settings service."""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models.settings import AppSettings
from app.repositories.settings_repository import SettingsRepository


class SettingsService:
    def __init__(self, db: Session) -> None:
        self.repo = SettingsRepository(db)

    def get(self) -> AppSettings:
        return self.repo.get_or_create()

    def update(self, **fields) -> AppSettings:
        return self.repo.update(**fields)
