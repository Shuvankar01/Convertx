"""Data access for app settings singleton."""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models.settings import AppSettings


class SettingsRepository:
    SINGLETON_ID = 1

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_or_create(self) -> AppSettings:
        obj = self.db.get(AppSettings, self.SINGLETON_ID)
        if obj is None:
            obj = AppSettings(id=self.SINGLETON_ID)
            self.db.add(obj)
            self.db.commit()
            self.db.refresh(obj)
        return obj

    def update(self, **fields) -> AppSettings:
        obj = self.get_or_create()
        for key, value in fields.items():
            if value is None:
                continue
            if hasattr(obj, key):
                setattr(obj, key, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj
