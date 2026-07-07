"""Domain exceptions."""
from __future__ import annotations


class ConvertXError(Exception):
    """Base exception for ConvertX."""


class UnknownCategoryError(ConvertXError):
    """Raised when a category is not registered."""


class UnknownUnitError(ConvertXError):
    """Raised when a unit is not valid for the given category."""


class InvalidValueError(ConvertXError):
    """Raised when an input value cannot be converted."""
