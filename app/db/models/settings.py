"""App-wide settings singleton."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class AppSettings(Base):
    __tablename__ = "app_settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, default=1)
    theme: Mapped[str] = mapped_column(String(16), default="system")
    precision: Mapped[str] = mapped_column(String(16), default="4")
    default_category: Mapped[str] = mapped_column(String(64), default="length")
    remember_last_conversion: Mapped[bool] = mapped_column(Boolean, default=True)
    show_comparison_panel: Mapped[bool] = mapped_column(Boolean, default=True)
    save_history: Mapped[bool] = mapped_column(Boolean, default=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
