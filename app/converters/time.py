"""Time converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class TimeConverter(FactorConverter):
    category = Category.TIME
    base_unit = "second"
    units = {
        "millisecond": UnitInfo("millisecond", "Millisecond", "ms"),
        "second": UnitInfo("second", "Second", "s"),
        "minute": UnitInfo("minute", "Minute", "min"),
        "hour": UnitInfo("hour", "Hour", "h"),
        "day": UnitInfo("day", "Day", "d"),
        "week": UnitInfo("week", "Week", "wk"),
        "month": UnitInfo("month", "Month (30.44 d)", "mo"),
        "year": UnitInfo("year", "Year (365.25 d)", "yr"),
    }
    factors = {
        "millisecond": 0.001,
        "second": 1.0,
        "minute": 60.0,
        "hour": 3600.0,
        "day": 86400.0,
        "week": 604800.0,
        "month": 2_629_746.0,  # average Gregorian month in seconds
        "year": 31_557_600.0,  # Julian year (365.25 d)
    }
