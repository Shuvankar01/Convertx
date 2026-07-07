"""Conversion history model."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ConversionHistory(Base):
    __tablename__ = "conversion_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String(64), index=True)
    input_value: Mapped[float] = mapped_column(Float)
    from_unit: Mapped[str] = mapped_column(String(64))
    to_unit: Mapped[str] = mapped_column(String(64))
    result_value: Mapped[float] = mapped_column(Float)
    precision: Mapped[str] = mapped_column(String(16), default="4")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
