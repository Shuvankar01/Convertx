"""Conversion service — orchestrates converter engine + formatting."""
from __future__ import annotations

from app.converters.registry import get_converter
from app.core.enums import Category
from app.core.utils import format_number
from app.schemas.conversion import ComparisonEntry, ConversionResult

# For each category, prefer these units in the multi-unit comparison panel.
COMPARISON_UNITS: dict[Category, list[str]] = {
    Category.LENGTH: ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "mile"],
    Category.WEIGHT: ["milligram", "gram", "kilogram", "ounce", "pound"],
    Category.TEMPERATURE: ["Celsius", "Fahrenheit", "Kelvin"],
    Category.AREA: ["square_meter", "square_foot", "square_yard", "acre", "hectare"],
    Category.VOLUME: ["milliliter", "liter", "cup", "pint", "gallon"],
    Category.TIME: ["second", "minute", "hour", "day", "week"],
    Category.SPEED: ["meter_per_second", "kilometer_per_hour", "mile_per_hour", "knot"],
    Category.DATA_STORAGE: ["byte", "KB", "MB", "GB", "TB"],
    Category.PRESSURE: ["pascal", "kilopascal", "bar", "psi", "atmosphere"],
    Category.ENERGY: ["joule", "kilojoule", "calorie", "kilocalorie", "kilowatt_hour"],
    Category.POWER: ["watt", "kilowatt", "horsepower"],
    Category.ANGLE: ["degree", "radian"],
    Category.FREQUENCY: ["hertz", "kilohertz", "megahertz", "gigahertz"],
    Category.FUEL_ECONOMY: ["km_per_l", "mpg_us", "mpg_uk", "l_per_100km"],
    Category.DIGITAL_TRANSFER_RATE: ["bps", "Kbps", "Mbps", "Gbps"],
}


class ConversionService:
    def convert(
        self,
        category: Category | str,
        value: float,
        from_unit: str,
        to_unit: str,
        precision: str = "4",
        include_comparisons: bool = True,
    ) -> ConversionResult:
        cat = Category(category) if isinstance(category, str) else category
        converter = get_converter(cat)
        result = converter.convert(value, from_unit, to_unit)
        formatted = format_number(result, precision)
        formula = converter.formula(from_unit, to_unit)

        comparisons: list[ComparisonEntry] = []
        if include_comparisons:
            comparisons = self._comparisons(cat, value, from_unit, precision)

        return ConversionResult(
            category=cat,
            value=value,
            from_unit=from_unit,
            to_unit=to_unit,
            result=result,
            formatted=formatted,
            precision=str(precision),
            formula=formula,
            comparisons=comparisons,
        )

    def _comparisons(
        self, category: Category, value: float, from_unit: str, precision: str
    ) -> list[ComparisonEntry]:
        converter = get_converter(category)
        candidate_units = COMPARISON_UNITS.get(category, list(converter.units.keys()))
        entries: list[ComparisonEntry] = []
        for unit in candidate_units:
            if unit == from_unit or unit not in converter.units:
                continue
            try:
                val = converter.convert(value, from_unit, unit)
            except Exception:  # noqa: BLE001
                continue
            entries.append(
                ComparisonEntry(
                    unit=unit,
                    value=val,
                    formatted=format_number(val, precision),
                )
            )
        return entries
