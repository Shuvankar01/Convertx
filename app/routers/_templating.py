"""Shared template environment and helpers."""
from __future__ import annotations

from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.config import get_settings
from app.converters.registry import all_categories, units_for
from app.core.constants import QUICK_PRESETS
from app.core.enums import Category
from app.core.utils import format_number

_settings = get_settings()
templates = Jinja2Templates(directory=str(_settings.templates_dir))

# Safe globals / helpers only
templates.env.globals["APP_NAME"] = _settings.app_name
templates.env.globals["TAGLINE"] = _settings.tagline
templates.env.globals["ALL_CATEGORIES"] = all_categories
templates.env.globals["UNITS_FOR"] = units_for
templates.env.globals["Category"] = Category
templates.env.filters["fmt"] = format_number


def render(request: Request, template: str, **context):
    context.setdefault("request", request)
    context.setdefault("current_path", request.url.path)
    context.setdefault("QUICK_PRESETS", QUICK_PRESETS)
    return templates.TemplateResponse(request=request, name=template, context=context)