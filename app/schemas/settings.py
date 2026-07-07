"""Settings schemas."""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class SettingsUpdate(BaseModel):
    theme: str | None = None
    precision: str | None = None
    default_category: str | None = None
    remember_last_conversion: bool | None = None
    show_comparison_panel: bool | None = None
    save_history: bool | None = None


class SettingsRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    theme: str
    precision: str
    default_category: str
    remember_last_conversion: bool
    show_comparison_panel: bool
    save_history: bool
