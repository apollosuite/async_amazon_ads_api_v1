"""Auto-generated models for GeoLocations from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
)

type DSPDistanceUnit = Literal["KILOMETERS", "MILES"]
"""
Supported values:
- `KILOMETERS`: Distance in kilometers
- `MILES`: Distance in miles
"""


class DSPCreateGeoLocationCoordinates(StrictModel):
    """Coordinates for a point of interest"""

    latitude: float = Field(description="Latitude coordinate. Example 47.6157")
    longitude: float = Field(description="Longitude coordinate. Example 122.339")


class DSPCreateGeoLocationRequest(StrictModel):
    geoLocations: list[DSPGeoLocationCreate] = Field(min_length=1, max_length=100)


class DSPCreateGeoLocationUnionRadiusLocation(StrictModel):
    radiusLocation: DSPCreateRadiusLocation


class DSPCreateGeoLocationUnionSmartLocation(StrictModel):
    smartLocation: DSPCreateSmartLocation


type DSPCreateGeoLocationUnion = DSPCreateGeoLocationUnionRadiusLocation | DSPCreateGeoLocationUnionSmartLocation


class DSPCreateRadiusLocation(StrictModel):
    """Configuration for a radius-based location. A minimum radius of 0.37 miles (2000 ft, 0.6km) is required."""

    coordinates: DSPCreateGeoLocationCoordinates | None = Field(default=None)
    pointOfInterestAddress: str | None = Field(
        default=None,
        description="Address. Example '2111 7th Ave, Seattle, WA 98121, United States' or 'Amazon Spheres'",
    )
    pointOfInterestRadius: float = Field(description="Radius of circle in kilometers or miles")
    units: DSPDistanceUnit


class DSPCreateSmartLocation(StrictModel):
    """A smart location targets postal codes based on a sales index."""

    locationIndexId: str = Field(description="The ID of the index used for this smart location.")
    maxIndexValuePercentile: int | None = Field(
        default=None,
        ge=0,
        le=100,
        description="Maximum percentile value (0-100). Must be greater than minIndexValuePercentile. Null will be treated as 0.",
    )
    minIndexValuePercentile: int | None = Field(
        default=None,
        ge=0,
        le=100,
        description="Minimum percentile value (0-100). Must be less than maxIndexValuePercentile. Null will be treated as 0.",
    )
    name: str = Field(description="Name for the smart location.")


class DSPGeoLocation(LenientModel):
    geoLocationId: str = Field(description="The identifier of the geo location.")
    location: DSPGeoLocationUnion


class DSPGeoLocationCoordinates(LenientModel):
    """Coordinates for a point of interest"""

    latitude: float = Field(description="Latitude coordinate. Example 47.6157")
    longitude: float = Field(description="Longitude coordinate. Example 122.339")


class DSPGeoLocationCreate(StrictModel):
    location: DSPCreateGeoLocationUnion


class DSPGeoLocationMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[DSPGeoLocationMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class DSPGeoLocationMultiStatusSuccess(LenientModel):
    geoLocation: DSPGeoLocation
    index: int = Field(ge=0, le=99)


class DSPGeoLocationUnionRadiusLocation(LenientModel):
    radiusLocation: DSPRadiusLocation


class DSPGeoLocationUnionSmartLocation(LenientModel):
    smartLocation: DSPSmartLocation


type DSPGeoLocationUnion = DSPGeoLocationUnionRadiusLocation | DSPGeoLocationUnionSmartLocation


class DSPRadiusLocation(LenientModel):
    """Configuration for a radius-based location. A minimum radius of 0.37 miles (2000 ft, 0.6km) is required."""

    coordinates: DSPGeoLocationCoordinates | None = Field(default=None)
    pointOfInterestAddress: str | None = Field(
        default=None,
        description="Address. Example '2111 7th Ave, Seattle, WA 98121, United States' or 'Amazon Spheres'",
    )
    pointOfInterestRadius: float = Field(description="Radius of circle in kilometers or miles")
    units: DSPDistanceUnit | str


class DSPSmartLocation(LenientModel):
    """A smart location targets postal codes based on a sales index."""

    locationIndexId: str = Field(description="The ID of the index used for this smart location.")
    maxIndexValuePercentile: int | None = Field(
        default=None,
        ge=0,
        le=100,
        description="Maximum percentile value (0-100). Must be greater than minIndexValuePercentile. Null will be treated as 0.",
    )
    minIndexValuePercentile: int | None = Field(
        default=None,
        ge=0,
        le=100,
        description="Minimum percentile value (0-100). Must be less than maxIndexValuePercentile. Null will be treated as 0.",
    )
    name: str = Field(description="Name for the smart location.")


__all__ = [
    "DSPCreateGeoLocationCoordinates",
    "DSPCreateGeoLocationRequest",
    "DSPCreateGeoLocationUnion",
    "DSPCreateRadiusLocation",
    "DSPCreateSmartLocation",
    "DSPDistanceUnit",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPGeoLocation",
    "DSPGeoLocationCoordinates",
    "DSPGeoLocationCreate",
    "DSPGeoLocationMultiStatusResponse",
    "DSPGeoLocationMultiStatusSuccess",
    "DSPGeoLocationUnion",
    "DSPRadiusLocation",
    "DSPSmartLocation",
]
