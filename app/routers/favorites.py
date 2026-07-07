"""Favorites HTMX endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.routers._templating import render
from app.services.favorite_service import FavoriteService

router = APIRouter(prefix="/favorites", tags=["favorites"])


@router.post("/toggle")
def toggle(
    request: Request,
    category: str = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...),
    db: Session = Depends(get_db),
):
    now_fav = FavoriteService(db).toggle(category, from_unit, to_unit)
    return render(
        request,
        "partials/favorite_button.html",
        is_favorite=now_fav,
        category=category,
        from_unit=from_unit,
        to_unit=to_unit,
    )


@router.delete("/{fav_id}")
def delete(fav_id: int, db: Session = Depends(get_db)):
    FavoriteService(db).delete(fav_id)
    return Response(status_code=200)
