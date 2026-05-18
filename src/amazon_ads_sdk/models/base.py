"""Shared base types for auto-generated models."""

from __future__ import annotations

from enum import StrEnum


class SafeStrEnum(StrEnum):
    """StrEnum that gracefully handles unknown values.

    When the API returns a new enum value not yet defined in the SDK,
    this class falls back to creating a synthetic member instead of
    raising a ``ValidationError``.

    Example:
        >>> class Color(SafeStrEnum):
        ...     red = "red"
        ...     blue = "blue"
        >>> Color("red")
        <Color.red: 'red'>
        >>> Color("unknown")
        <Color.unknown: 'unknown'>
    """

    @classmethod
    def _missing_(cls, value: object) -> SafeStrEnum | None:
        if isinstance(value, str):
            pseudo = str.__new__(cls, value)
            pseudo._name_ = value
            pseudo._value_ = value
            return pseudo
        return None
