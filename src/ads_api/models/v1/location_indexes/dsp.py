"""Auto-generated models for LocationIndexes from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type DSPCountryCode = Literal[
    "AU",
    "BE",
    "BR",
    "CA",
    "DE",
    "ES",
    "FR",
    "GB",
    "IE",
    "IN",
    "IT",
    "JP",
    "MX",
    "NL",
    "SE",
    "TR",
    "US",
]


type DSPErrorCode = Literal[
    "BAD_REQUEST",  # The request is not valid considering the documented schema.
    "FEATURE_NOT_AVAILABLE",  # The requested feature is not available.
    "FIELD_VALUE_IS_EMPTY",  # Update the request with the required information for this resource.
    "FIELD_VALUE_IS_NULL",  # Update the request with the required information for this resource.
    "FIELD_VALUE_IS_OUT_OF_RANGE",  # Update the value to be within the required range.
    "FORBIDDEN",  # The caller is not authorized to make the given request.
    "INTERNAL_ERROR",  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    "NOT_FOUND",  # The requested resource does not exist.
    "UNAUTHORIZED",  # The request lacks the necessary credentials.
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


type DSPIndexStatus = Literal[
    "ENABLED",  # The location index is active and can be used in smart locations.
    "FAILED",  # The location index creation failed and cannot be used in smart locations.
    "PENDING",  # The location index is being created and cannot be used in smart locations yet.
    "UPDATE_FAILED",  # The location index update has failed, but the old version can still be used.
]
"""
Supported values:
- `ENABLED`: The location index is active and can be used in smart locations.
- `FAILED`: The location index creation failed and cannot be used in smart locations.
- `PENDING`: The location index is being created and cannot be used in smart locations yet.
- `UPDATE_FAILED`: The location index update has failed, but the old version can still be used.
"""


class DSPConstituentIndexValue(LenientModel):
    """Values for a location index where the indexValue is calculated from the constituents."""

    brandSales: float = Field(description="The brand sales value for the postal code.")
    categorySales: float = Field(description="The category sales value for the postal code.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class DSPConstituentIndexValues(LenientModel):
    values: list[DSPConstituentIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of brand and category sales values."
    )


class DSPCreateConstituentIndexValue(StrictModel):
    """Values for a location index where the indexValue is calculated from the constituents."""

    brandSales: float = Field(description="The brand sales value for the postal code.")
    categorySales: float = Field(description="The category sales value for the postal code.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class DSPCreateConstituentIndexValues(StrictModel):
    values: list[DSPCreateConstituentIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of brand and category sales values."
    )


class DSPCreateDirectIndexValue(StrictModel):
    """Values for a location index where the indexValue is the pre-calculated index."""

    indexValue: float = Field(description="The pre-calculated index value.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class DSPCreateDirectIndexValues(StrictModel):
    values: list[DSPCreateDirectIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of direct index values."
    )


class DSPCreateIndexValuesDirectIndexValues(StrictModel):
    directIndexValues: DSPCreateDirectIndexValues


class DSPCreateIndexValuesConstituentIndexValues(StrictModel):
    constituentIndexValues: DSPCreateConstituentIndexValues


type DSPCreateIndexValues = DSPCreateIndexValuesDirectIndexValues | DSPCreateIndexValuesConstituentIndexValues


class DSPCreateLocationIndexRequest(StrictModel):
    locationIndexes: list[DSPLocationIndexCreate] = Field(min_length=1, max_length=10)


class DSPDirectIndexValue(LenientModel):
    """Values for a location index where the indexValue is the pre-calculated index."""

    indexValue: float = Field(description="The pre-calculated index value.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class DSPDirectIndexValues(LenientModel):
    values: list[DSPDirectIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of direct index values."
    )


class DSPError(LenientModel):
    code: DSPErrorCode | str = Field(description="""
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
""")
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=99)


class DSPIndexValuesConstituentIndexValues(LenientModel):
    constituentIndexValues: DSPConstituentIndexValues


class DSPIndexValuesDirectIndexValues(LenientModel):
    directIndexValues: DSPDirectIndexValues


type DSPIndexValues = DSPIndexValuesConstituentIndexValues | DSPIndexValuesDirectIndexValues


class DSPLocationIndex(LenientModel):
    countryCode: DSPCountryCode | str | None = Field(default=None)
    creationDateTime: datetime = Field(description="The date time the location index was created.")
    indexData: DSPIndexValues
    indexId: str = Field(description="The identifier of the location index.")
    indexName: str = Field(description="The name of the location index.")
    lastUpdatedDateTime: datetime = Field(description="The date time the location index was last updated successfully.")
    status: DSPIndexStatus | str = Field(description="""
Supported values:
- `ENABLED`: The location index is active and can be used in smart locations.
- `FAILED`: The location index creation failed and cannot be used in smart locations.
- `PENDING`: The location index is being created and cannot be used in smart locations yet.
- `UPDATE_FAILED`: The location index update has failed, but the old version can still be used.
""")


class DSPLocationIndexCreate(StrictModel):
    countryCode: DSPCountryCode | None = Field(default=None)
    indexData: DSPCreateIndexValues
    indexName: str = Field(description="The name of the location index.")


class DSPLocationIndexMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[DSPLocationIndexMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class DSPLocationIndexMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    locationIndex: DSPLocationIndex


class DSPLocationIndexSuccessResponse(LenientModel):
    locationIndexes: list[DSPLocationIndex] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class DSPLocationIndexUpdate(StrictModel):
    indexData: DSPUpdateIndexValues | None = Field(default=None)
    indexId: str = Field(description="The identifier of the location index.")


class DSPRetrieveLocationIndexRequest(StrictModel):
    indexIds: list[str] = Field(min_length=1, max_length=10)


class DSPUpdateConstituentIndexValues(StrictModel):
    values: list[DSPCreateConstituentIndexValue] | None = Field(
        default=None, min_length=1, max_length=1000000, description="List of brand and category sales values."
    )


class DSPUpdateDirectIndexValues(StrictModel):
    values: list[DSPCreateDirectIndexValue] | None = Field(
        default=None, min_length=1, max_length=1000000, description="List of direct index values."
    )


class DSPUpdateIndexValuesDirectIndexValues(StrictModel):
    directIndexValues: DSPUpdateDirectIndexValues


class DSPUpdateIndexValuesConstituentIndexValues(StrictModel):
    constituentIndexValues: DSPUpdateConstituentIndexValues


type DSPUpdateIndexValues = DSPUpdateIndexValuesDirectIndexValues | DSPUpdateIndexValuesConstituentIndexValues


class DSPUpdateLocationIndexRequest(StrictModel):
    locationIndexes: list[DSPLocationIndexUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "DSPConstituentIndexValue",
    "DSPConstituentIndexValues",
    "DSPCountryCode",
    "DSPCreateConstituentIndexValue",
    "DSPCreateConstituentIndexValues",
    "DSPCreateDirectIndexValue",
    "DSPCreateDirectIndexValues",
    "DSPCreateIndexValues",
    "DSPCreateLocationIndexRequest",
    "DSPDirectIndexValue",
    "DSPDirectIndexValues",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPIndexStatus",
    "DSPIndexValues",
    "DSPLocationIndex",
    "DSPLocationIndexCreate",
    "DSPLocationIndexMultiStatusResponse",
    "DSPLocationIndexMultiStatusSuccess",
    "DSPLocationIndexSuccessResponse",
    "DSPLocationIndexUpdate",
    "DSPRetrieveLocationIndexRequest",
    "DSPUpdateConstituentIndexValues",
    "DSPUpdateDirectIndexValues",
    "DSPUpdateIndexValues",
    "DSPUpdateLocationIndexRequest",
]
