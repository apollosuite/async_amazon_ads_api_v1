"""Auto-generated models for Locations from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import StrictModel


class ListLocationsRequestBodyV1(StrictModel):
    """Resulting locations will match all specified filters"""

    filters: list[LocationFilterV1] | None = Field(default=None)


class LocationFilterV1(StrictModel):
    field: Literal["category", "locationId", "name"] | None = Field(
        default=None,
        description="Field to filter by. Supported enums are 'locationId', 'name', and 'category'. The 'name' filter is a fuzzy search. If 'category' is specified, the values must match either 'CITY', 'STATE', 'DMA', 'COUNTRY', or 'POSTAL_CODE'.",
    )
    values: list[str] | None = Field(default=None)


__all__ = ["ListLocationsRequestBodyV1", "LocationFilterV1"]
