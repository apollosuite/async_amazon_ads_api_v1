"""Auto-generated models for LocationIndexes from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type CountryCode = Literal[
    "AU", "BE", "BR", "CA", "DE", "ES", "FR", "GB", "IE", "IN", "IT", "JP", "MX", "NL", "SE", "TR", "US"
]


type ErrorCode = Literal[
    "BAD_REQUEST",
    "FEATURE_NOT_AVAILABLE",
    "FIELD_VALUE_IS_EMPTY",
    "FIELD_VALUE_IS_NULL",
    "FIELD_VALUE_IS_OUT_OF_RANGE",
    "FORBIDDEN",
    "INTERNAL_ERROR",
    "NOT_FOUND",
    "UNAUTHORIZED",
]
"""
Supported values:
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `FEATURE_NOT_AVAILABLE`: The requested feature is not available.
- `FIELD_VALUE_IS_EMPTY`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_NULL`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_OUT_OF_RANGE`: Update the value to be within the required range.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
"""


type IndexStatus = Literal["ENABLED", "FAILED", "PENDING", "UPDATE_FAILED"]
"""
Supported values:
- `ENABLED`: The location index is active and can be used in smart locations.
- `FAILED`: The location index creation failed and cannot be used in smart locations.
- `PENDING`: The location index is being created and cannot be used in smart locations yet.
- `UPDATE_FAILED`: The location index update has failed, but the old version can still be used.
"""


class ConstituentIndexValue(LenientModel):
    """Values for a location index where the indexValue is calculated from the constituents."""

    brandSales: float = Field(description="The brand sales value for the postal code.")
    categorySales: float = Field(description="The category sales value for the postal code.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class ConstituentIndexValues(LenientModel):
    values: list[ConstituentIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of brand and category sales values."
    )


class CreateConstituentIndexValue(StrictModel):
    """Values for a location index where the indexValue is calculated from the constituents."""

    brandSales: float = Field(description="The brand sales value for the postal code.")
    categorySales: float = Field(description="The category sales value for the postal code.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class CreateConstituentIndexValues(StrictModel):
    values: list[CreateConstituentIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of brand and category sales values."
    )


class CreateDirectIndexValue(StrictModel):
    """Values for a location index where the indexValue is the pre-calculated index."""

    indexValue: float = Field(description="The pre-calculated index value.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class CreateDirectIndexValues(StrictModel):
    values: list[CreateDirectIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of direct index values."
    )


class CreateIndexValuesDirectIndexValues(StrictModel):
    directIndexValues: CreateDirectIndexValues


class CreateIndexValuesConstituentIndexValues(StrictModel):
    constituentIndexValues: CreateConstituentIndexValues


type CreateIndexValues = CreateIndexValuesDirectIndexValues | CreateIndexValuesConstituentIndexValues


class CreateLocationIndexRequest(StrictModel):
    locationIndexes: list[LocationIndexCreate] = Field(min_length=1, max_length=10)


class DirectIndexValue(LenientModel):
    """Values for a location index where the indexValue is the pre-calculated index."""

    indexValue: float = Field(description="The pre-calculated index value.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class DirectIndexValues(LenientModel):
    values: list[DirectIndexValue] = Field(min_length=1, max_length=1000000, description="List of direct index values.")


class Error(LenientModel):
    code: ErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=99)


class IndexValuesConstituentIndexValues(LenientModel):
    constituentIndexValues: ConstituentIndexValues


class IndexValuesDirectIndexValues(LenientModel):
    directIndexValues: DirectIndexValues


type IndexValues = IndexValuesConstituentIndexValues | IndexValuesDirectIndexValues


class LocationIndex(LenientModel):
    countryCode: CountryCode | str | None = Field(default=None)
    creationDateTime: datetime = Field(description="The date time the location index was created.")
    indexData: IndexValues
    indexId: str = Field(description="The identifier of the location index.")
    indexName: str = Field(description="The name of the location index.")
    lastUpdatedDateTime: datetime = Field(description="The date time the location index was last updated successfully.")
    status: IndexStatus | str


class LocationIndexCreate(StrictModel):
    countryCode: CountryCode | None = Field(default=None)
    indexData: CreateIndexValues
    indexName: str = Field(description="The name of the location index.")


class LocationIndexMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[LocationIndexMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class LocationIndexMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    locationIndex: LocationIndex


class LocationIndexSuccessResponse(LenientModel):
    locationIndexes: list[LocationIndex] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class LocationIndexUpdate(StrictModel):
    indexData: UpdateIndexValues | None = Field(default=None)
    indexId: str = Field(description="The identifier of the location index.")


class RetrieveLocationIndexRequest(StrictModel):
    indexIds: list[str] = Field(min_length=1, max_length=10)


class UpdateConstituentIndexValues(StrictModel):
    values: list[CreateConstituentIndexValue] | None = Field(
        default=None, min_length=1, max_length=1000000, description="List of brand and category sales values."
    )


class UpdateDirectIndexValues(StrictModel):
    values: list[CreateDirectIndexValue] | None = Field(
        default=None, min_length=1, max_length=1000000, description="List of direct index values."
    )


class UpdateIndexValuesDirectIndexValues(StrictModel):
    directIndexValues: UpdateDirectIndexValues


class UpdateIndexValuesConstituentIndexValues(StrictModel):
    constituentIndexValues: UpdateConstituentIndexValues


type UpdateIndexValues = UpdateIndexValuesDirectIndexValues | UpdateIndexValuesConstituentIndexValues


class UpdateLocationIndexRequest(StrictModel):
    locationIndexes: list[LocationIndexUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "ConstituentIndexValue",
    "ConstituentIndexValues",
    "CountryCode",
    "CreateConstituentIndexValue",
    "CreateConstituentIndexValues",
    "CreateDirectIndexValue",
    "CreateDirectIndexValues",
    "CreateIndexValues",
    "CreateLocationIndexRequest",
    "DirectIndexValue",
    "DirectIndexValues",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "IndexStatus",
    "IndexValues",
    "LocationIndex",
    "LocationIndexCreate",
    "LocationIndexMultiStatusResponse",
    "LocationIndexMultiStatusSuccess",
    "LocationIndexSuccessResponse",
    "LocationIndexUpdate",
    "RetrieveLocationIndexRequest",
    "UpdateConstituentIndexValues",
    "UpdateDirectIndexValues",
    "UpdateIndexValues",
    "UpdateLocationIndexRequest",
]
