"""Auto-generated models for GeoLocations from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class DistanceUnit(StrEnum):
    """**DistanceUnit Enum:** DistanceUnit Description `KILOMETERS` Distance in kilometers `MILES` Distance in miles"""

    KILOMETERS = "KILOMETERS"
    MILES = "MILES"


class CreateGeoLocationCoordinates(BaseModel):
    """Coordinates for a point of interest"""

    model_config = ConfigDict(extra="forbid")

    latitude: float  # Latitude coordinate. Example 47.6157
    longitude: float  # Longitude coordinate. Example 122.339


class CreateGeoLocationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    geoLocations: list[GeoLocationCreate]


class CreateGeoLocationUnion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    radiusLocation: CreateRadiusLocation | None = None
    smartLocation: CreateSmartLocation | None = None


class CreateRadiusLocation(BaseModel):
    """Configuration for a radius-based location. A minimum radius of 0.37 miles (2000 ft, 0.6km) is required."""

    model_config = ConfigDict(extra="forbid")

    coordinates: CreateGeoLocationCoordinates | None = None
    pointOfInterestAddress: str | None = (
        None  # Address. Example '2111 7th Ave, Seattle, WA 98121, United States' or 'Amazon Spheres'
    )
    pointOfInterestRadius: float  # Radius of circle in kilometers or miles
    units: Annotated[DistanceUnit | str, lenient_enum(DistanceUnit)]


class CreateSmartLocation(BaseModel):
    """A smart location targets postal codes based on a sales index."""

    model_config = ConfigDict(extra="forbid")

    locationIndexId: str  # The ID of the index used for this smart location.
    maxIndexValuePercentile: int | None = (
        None  # Maximum percentile value (0-100). Must be greater than minIndexValuePercentile. Null will be treated as 0.
    )
    minIndexValuePercentile: int | None = (
        None  # Minimum percentile value (0-100). Must be less than maxIndexValuePercentile. Null will be treated as 0.
    )
    name: str  # Name for the smart location.


class GeoLocation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    geoLocationId: str  # The identifier of the geo location.
    location: GeoLocationUnion


class GeoLocationCoordinates(BaseModel):
    """Coordinates for a point of interest"""

    model_config = ConfigDict(extra="forbid")

    latitude: float  # Latitude coordinate. Example 47.6157
    longitude: float  # Longitude coordinate. Example 122.339


class GeoLocationCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    location: CreateGeoLocationUnion


class GeoLocationMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[GeoLocationMultiStatusSuccess] | None = None


class GeoLocationMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    geoLocation: GeoLocation
    index: int


class GeoLocationUnion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    radiusLocation: RadiusLocation | None = None
    smartLocation: SmartLocation | None = None


class RadiusLocation(BaseModel):
    """Configuration for a radius-based location. A minimum radius of 0.37 miles (2000 ft, 0.6km) is required."""

    model_config = ConfigDict(extra="forbid")

    coordinates: GeoLocationCoordinates | None = None
    pointOfInterestAddress: str | None = (
        None  # Address. Example '2111 7th Ave, Seattle, WA 98121, United States' or 'Amazon Spheres'
    )
    pointOfInterestRadius: float  # Radius of circle in kilometers or miles
    units: Annotated[DistanceUnit | str, lenient_enum(DistanceUnit)]


class SmartLocation(BaseModel):
    """A smart location targets postal codes based on a sales index."""

    model_config = ConfigDict(extra="forbid")

    locationIndexId: str  # The ID of the index used for this smart location.
    maxIndexValuePercentile: int | None = (
        None  # Maximum percentile value (0-100). Must be greater than minIndexValuePercentile. Null will be treated as 0.
    )
    minIndexValuePercentile: int | None = (
        None  # Minimum percentile value (0-100). Must be less than maxIndexValuePercentile. Null will be treated as 0.
    )
    name: str  # Name for the smart location.


__all__ = [
    "DistanceUnit",
    "CreateGeoLocationCoordinates",
    "CreateGeoLocationRequest",
    "CreateGeoLocationUnion",
    "CreateRadiusLocation",
    "CreateSmartLocation",
    "GeoLocation",
    "GeoLocationCoordinates",
    "GeoLocationCreate",
    "GeoLocationMultiStatusResponse",
    "GeoLocationMultiStatusSuccess",
    "GeoLocationUnion",
    "RadiusLocation",
    "SmartLocation",
]
