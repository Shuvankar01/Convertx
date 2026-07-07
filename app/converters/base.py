"""Base classes for converters."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.core.enums import Category
from app.core.exceptions import UnknownUnitError


@dataclass(frozen=True)
class UnitInfo:
    key: str
    label: str
    symbol: str


class BaseConverter(ABC):
    """Abstract converter for a single category."""

    category: Category
    units: dict[str, UnitInfo]

    @abstractmethod
    def convert(self, value: float, from_unit: str, to_unit: str) -> float: ...

    @abstractmethod
    def formula(self, from_unit: str, to_unit: str) -> str: ...

    def unit_keys(self) -> list[str]:
        return list(self.units.keys())

    def ensure_unit(self, unit: str) -> None:
        if unit not in self.units:
            raise UnknownUnitError(
                f"'{unit}' is not a valid unit for {self.category.label}"
            )

    def label_for(self, unit: str) -> str:
        return self.units[unit].label if unit in self.units else unit

    def symbol_for(self, unit: str) -> str:
        return self.units[unit].symbol if unit in self.units else unit


class FactorConverter(BaseConverter):
    """Converter that normalizes through a base unit using multiplicative factors.

    Subclasses set ``base_unit`` and ``factors`` mapping unit -> value_in_base.
    """

    base_unit: str
    factors: dict[str, float]

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        self.ensure_unit(from_unit)
        self.ensure_unit(to_unit)
        base_value = value * self.factors[from_unit]
        return base_value / self.factors[to_unit]

    def formula(self, from_unit: str, to_unit: str) -> str:
        self.ensure_unit(from_unit)
        self.ensure_unit(to_unit)
        if from_unit == to_unit:
            return "Same unit — value is unchanged."
        ratio = self.factors[from_unit] / self.factors[to_unit]
        from_sym = self.symbol_for(from_unit)
        to_sym = self.symbol_for(to_unit)
        return f"1 {from_sym} = {ratio:.10g} {to_sym}"
