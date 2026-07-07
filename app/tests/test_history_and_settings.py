"""History + favorites + settings service tests."""
from __future__ import annotations

from app.db.session import SessionLocal
from app.services.favorite_service import FavoriteService
from app.services.history_service import HistoryService
from app.services.settings_service import SettingsService


def test_history_record_and_recent():
    db = SessionLocal()
    try:
        svc = HistoryService(db)
        svc.clear()
        svc.record(
            category="length",
            input_value=1.0,
            from_unit="kilometer",
            to_unit="mile",
            result_value=0.6214,
            precision="4",
        )
        recent = svc.recent()
        assert len(recent) == 1
        assert recent[0].from_unit == "kilometer"
    finally:
        db.close()


def test_favorite_toggle():
    db = SessionLocal()
    try:
        svc = FavoriteService(db)
        assert svc.toggle("length", "meter", "foot") is True
        assert svc.is_favorite("length", "meter", "foot") is True
        assert svc.toggle("length", "meter", "foot") is False
        assert svc.is_favorite("length", "meter", "foot") is False
    finally:
        db.close()


def test_settings_defaults_and_update():
    db = SessionLocal()
    try:
        svc = SettingsService(db)
        initial = svc.get()
        assert initial.precision in {"2", "4", "6", "auto"}
        updated = svc.update(precision="6", theme="dark")
        assert updated.precision == "6"
        assert updated.theme == "dark"
    finally:
        db.close()
