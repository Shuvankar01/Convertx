"""History schemas."""
from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class HistoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category: str
    input_value: float
    from_unit: str
    to_unit: str
    result_value: float
    precision: str
    created_at: datetime
