"""Data storage converter (decimal, SI convention: 1 KB = 1000 B)."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class DataStorageConverter(FactorConverter):
    category = Category.DATA_STORAGE
    base_unit = "byte"
    units = {
        "bit": UnitInfo("bit", "Bit", "b"),
        "byte": UnitInfo("byte", "Byte", "B"),
        "KB": UnitInfo("KB", "Kilobyte", "KB"),
        "MB": UnitInfo("MB", "Megabyte", "MB"),
        "GB": UnitInfo("GB", "Gigabyte", "GB"),
        "TB": UnitInfo("TB", "Terabyte", "TB"),
        "PB": UnitInfo("PB", "Petabyte", "PB"),
    }
    factors = {
        "bit": 1.0 / 8.0,
        "byte": 1.0,
        "KB": 1_000.0,
        "MB": 1_000_000.0,
        "GB": 1_000_000_000.0,
        "TB": 1_000_000_000_000.0,
        "PB": 1_000_000_000_000_000.0,
    }
