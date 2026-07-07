"""Converter registry — the single source of truth for supported categories."""
from __future__ import annotations

from app.converters.angle import AngleConverter
from app.converters.area import AreaConverter
from app.converters.base import BaseConverter
from app.converters.data_storage import DataStorageConverter
from app.converters.digital_transfer_rate import DigitalTransferRateConverter
from app.converters.energy import EnergyConverter
from app.converters.frequency import FrequencyConverter
from app.converters.fuel_economy import FuelEconomyConverter
from app.converters.length import LengthConverter
from app.converters.power import PowerConverter
from app.converters.pressure import PressureConverter
from app.converters.speed import SpeedConverter
from app.converters.temperature import TemperatureConverter
from app.converters.time import TimeConverter
from app.converters.volume import VolumeConverter
from app.converters.weight import WeightConverter
from app.core.enums import Category
from app.core.exceptions import UnknownCategoryError

_REGISTRY: dict[Category, BaseConverter] = {
    Category.LENGTH: LengthConverter(),
    Category.WEIGHT: WeightConverter(),
    Category.TEMPERATURE: TemperatureConverter(),
    Category.AREA: AreaConverter(),
    Category.VOLUME: VolumeConverter(),
    Category.TIME: TimeConverter(),
    Category.SPEED: SpeedConverter(),
    Category.DATA_STORAGE: DataStorageConverter(),
    Category.PRESSURE: PressureConverter(),
    Category.ENERGY: EnergyConverter(),
    Category.POWER: PowerConverter(),
    Category.ANGLE: AngleConverter(),
    Category.FREQUENCY: FrequencyConverter(),
    Category.FUEL_ECONOMY: FuelEconomyConverter(),
    Category.DIGITAL_TRANSFER_RATE: DigitalTransferRateConverter(),
}


def get_converter(category: Category | str) -> BaseConverter:
    if isinstance(category, str):
        try:
            category = Category(category)
        except ValueError as exc:
            raise UnknownCategoryError(f"Unknown category '{category}'") from exc
    converter = _REGISTRY.get(category)
    if converter is None:
        raise UnknownCategoryError(f"Unknown category '{category}'")
    return converter


def all_categories() -> list[Category]:
    return list(_REGISTRY.keys())


def units_for(category: Category | str) -> list[dict[str, str]]:
    conv = get_converter(category)
    return [
        {"key": u.key, "label": u.label, "symbol": u.symbol}
        for u in conv.units.values()
    ]
