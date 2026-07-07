"""Favorite conversion pair model."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class FavoriteConversion(Base):
    __tablename__ = "favorite_conversions"
    __table_args__ = (
        UniqueConstraint("category", "from_unit", "to_unit", name="uq_favorite_pair"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String(64), index=True)
    from_unit: Mapped[str] = mapped_column(String(64))
    to_unit: Mapped[str] = mapped_column(String(64))
    label: Mapped[str | None] = mapped_column(String(128), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
