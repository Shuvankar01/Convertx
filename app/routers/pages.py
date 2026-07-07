"""Top-level page routes (dashboard, converter, history, favorites, settings, about)."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.converters.registry import all_categories, get_converter, units_for
from app.core.enums import Category
from app.db.session import get_db
from app.dependencies import app_settings
from app.routers._templating import render
from app.services.favorite_service import FavoriteService
from app.services.history_service import HistoryService

router = APIRouter()


@router.get("/")
def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    settings=Depends(app_settings),
):
    history = HistoryService(db).recent(limit=6)
    favorites = FavoriteService(db).list()[:6]
    return render(
        request,
        "pages/dashboard.html",
        settings=settings,
        history=history,
        favorites=favorites,
        categories=all_categories(),
    )


@router.get("/converter")
def converter_page(
    request: Request,
    category: str | None = None,
    from_unit: str | None = None,
    to_unit: str | None = None,
    value: str | None = None,
    settings=Depends(app_settings),
    db: Session = Depends(get_db),
):
    cat = _resolve_category(category, settings.default_category)
    converter = get_converter(cat)
    units = units_for(cat)
    unit_keys = [u["key"] for u in units]
    fu = from_unit if from_unit in unit_keys else unit_keys[0]
    tu = to_unit if to_unit in unit_keys else (unit_keys[1] if len(unit_keys) > 1 else unit_keys[0])

    favorite_service = FavoriteService(db)
    is_fav = favorite_service.is_favorite(cat.value, fu, tu)

    return render(
        request,
        "pages/converter.html",
        settings=settings,
        category=cat,
        converter=converter,
        units=units,
        from_unit=fu,
        to_unit=tu,
        value=value or "1",
        precision=settings.precision,
        is_favorite=is_fav,
    )


@router.get("/history")
def history_page(
    request: Request,
    db: Session = Depends(get_db),
    settings=Depends(app_settings),
):
    entries = HistoryService(db).recent(limit=200)
    return render(
        request,
        "pages/history.html",
        settings=settings,
        entries=entries,
    )


@router.get("/favorites")
def favorites_page(
    request: Request,
    db: Session = Depends(get_db),
    settings=Depends(app_settings),
):
    favorites = FavoriteService(db).list()
    return render(
        request,
        "pages/favorites.html",
        settings=settings,
        favorites=favorites,
    )


@router.get("/settings")
def settings_page(request: Request, settings=Depends(app_settings)):
    return render(
        request,
        "pages/settings.html",
        settings=settings,
        categories=all_categories(),
    )


@router.get("/supported-units")
def supported_units_page(request: Request, settings=Depends(app_settings)):
    catalog = []
    for cat in all_categories():
        catalog.append(
            {
                "category": cat,
                "units": units_for(cat),
            }
        )
    return render(
        request,
        "pages/supported_units.html",
        settings=settings,
        catalog=catalog,
    )


@router.get("/about")
def about_page(request: Request, settings=Depends(app_settings)):
    return render(request, "pages/about.html", settings=settings)


def _resolve_category(requested: str | None, fallback: str) -> Category:
    for value in (requested, fallback, "length"):
        if not value:
            continue
        try:
            return Category(value)
        except ValueError:
            continue
    return Category.LENGTH
