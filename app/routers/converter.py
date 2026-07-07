"""Converter HTMX endpoints (result card, unit refresh, favorite toggle)."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Form, Request
from sqlalchemy.orm import Session

from app.converters.registry import get_converter, units_for
from app.core.enums import Category
from app.core.exceptions import ConvertXError
from app.core.utils import safe_float
from app.db.session import get_db
from app.dependencies import app_settings
from app.routers._templating import render
from app.services.conversion_service import ConversionService
from app.services.favorite_service import FavoriteService
from app.services.history_service import HistoryService

router = APIRouter(prefix="/converter", tags=["converter"])


@router.post("/convert")
def convert(
    request: Request,
    category: str = Form(...),
    value: str = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...),
    precision: str = Form("4"),
    db: Session = Depends(get_db),
    settings=Depends(app_settings),
):
    try:
        parsed = safe_float(value)
        cat = Category(category)
        result = ConversionService().convert(
            cat, parsed, from_unit, to_unit, precision=precision
        )
    except (ConvertXError, ValueError) as exc:
        return render(
            request,
            "partials/result_error.html",
            message=str(exc),
        )

    if settings.save_history:
        HistoryService(db).record(
            category=cat.value,
            input_value=parsed,
            from_unit=from_unit,
            to_unit=to_unit,
            result_value=result.result,
            precision=precision,
        )

    is_fav = FavoriteService(db).is_favorite(cat.value, from_unit, to_unit)
    return render(
        request,
        "partials/result_card.html",
        result=result,
        converter=get_converter(cat),
        is_favorite=is_fav,
        show_comparison=settings.show_comparison_panel,
    )


@router.get("/units")
def units_partial(request: Request, category: str):
    """HTMX endpoint: refresh from/to selects when the category changes."""
    try:
        cat = Category(category)
    except ValueError:
        cat = Category.LENGTH
    units = units_for(cat)
    return render(
        request,
        "partials/unit_selects.html",
        units=units,
        from_unit=units[0]["key"],
        to_unit=units[1]["key"] if len(units) > 1 else units[0]["key"],
        category=cat,
    )
