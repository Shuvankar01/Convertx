"""Static presets and dashboard copy."""
from __future__ import annotations

from dataclasses import dataclass

from app.core.enums import Category


@dataclass(frozen=True)
class Preset:
    category: Category
    from_unit: str
    to_unit: str
    value: float = 1.0

    @property
    def label(self) -> str:
        return f"{self.from_unit} → {self.to_unit}"


QUICK_PRESETS: list[Preset] = [
    Preset(Category.LENGTH, "kilometer", "mile"),
    Preset(Category.LENGTH, "mile", "kilometer"),
    Preset(Category.LENGTH, "meter", "foot"),
    Preset(Category.LENGTH, "inch", "centimeter"),
    Preset(Category.WEIGHT, "kilogram", "pound"),
    Preset(Category.WEIGHT, "pound", "kilogram"),
    Preset(Category.TEMPERATURE, "Celsius", "Fahrenheit"),
    Preset(Category.TEMPERATURE, "Fahrenheit", "Celsius"),
    Preset(Category.VOLUME, "liter", "gallon"),
    Preset(Category.DATA_STORAGE, "GB", "MB"),
]
