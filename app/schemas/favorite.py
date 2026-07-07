"""Favorite schemas."""
from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class FavoriteCreate(BaseModel):
    category: str
    from_unit: str
    to_unit: str
    label: str | None = None


class FavoriteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category: str
    from_unit: str
    to_unit: str
    label: str | None
    created_at: datetime
