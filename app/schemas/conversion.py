"""Conversion request/response schemas."""
from __future__ import annotations

from pydantic import BaseModel, Field

from app.core.enums import Category


class ConversionRequest(BaseModel):
    category: Category
    value: float
    from_unit: str
    to_unit: str
    precision: str = Field(default="4")


class ComparisonEntry(BaseModel):
    unit: str
    value: float
    formatted: str


class ConversionResult(BaseModel):
    category: Category
    value: float
    from_unit: str
    to_unit: str
    result: float
    formatted: str
    precision: str
    formula: str | None = None
    comparisons: list[ComparisonEntry] = []
