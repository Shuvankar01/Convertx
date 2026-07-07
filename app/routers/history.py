"""History HTMX endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Request
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.routers._templating import render
from app.services.history_service import HistoryService

router = APIRouter(prefix="/history", tags=["history"])


@router.delete("/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    HistoryService(db).delete(entry_id)
    return Response(status_code=200)


@router.delete("")
def clear_all(request: Request, db: Session = Depends(get_db)):
    HistoryService(db).clear()
    return render(request, "partials/history_empty.html")
