"""Settings HTMX endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Form, Request
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.routers._templating import render
from app.services.history_service import HistoryService
from app.services.settings_service import SettingsService

router = APIRouter(prefix="/settings", tags=["settings"])


@router.post("")
def update_settings(
    request: Request,
    theme: str = Form("system"),
    precision: str = Form("4"),
    default_category: str = Form("length"),
    remember_last_conversion: str | None = Form(None),
    show_comparison_panel: str | None = Form(None),
    save_history: str | None = Form(None),
    db: Session = Depends(get_db),
):
    updated = SettingsService(db).update(
        theme=theme,
        precision=precision,
        default_category=default_category,
        remember_last_conversion=bool(remember_last_conversion),
        show_comparison_panel=bool(show_comparison_panel),
        save_history=bool(save_history),
    )
    return render(request, "partials/settings_saved.html", settings=updated)


@router.post("/clear-data")
def clear_data(request: Request, db: Session = Depends(get_db)):
    HistoryService(db).clear()
    return render(request, "partials/settings_saved.html", settings=SettingsService(db).get(), cleared=True)
