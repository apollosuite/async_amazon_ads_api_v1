"""Auto-generated models for LocationIndexes from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .selling_accounts import CountryCode


class IndexStatus(StrEnum):
    """**IndexStatus Enum:**  IndexStatus Description ------ ------ `ENABLED` The location index is active and can be
    used in smart locations.

    `FAILED` The location index creation failed and cannot be used in smart locations. `PENDING` The location index is
    being created and cannot be used in smart locations yet. `UPDATE_FAILED` The location index update has failed, but
    the old version can still be used.
    """

    ENABLED = "ENABLED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    UPDATE_FAILED = "UPDATE_FAILED"


class ConstituentIndexValue(BaseModel):
    """Values for a location index where the indexValue is calculated from the constituents."""

    model_config = ConfigDict(extra="forbid")

    brandSales: float = Field(description="The brand sales value for the postal code.")
    categorySales: float = Field(description="The category sales value for the postal code.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class ConstituentIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[ConstituentIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of brand and category sales values."
    )


class CreateConstituentIndexValue(BaseModel):
    """Values for a location index where the indexValue is calculated from the constituents."""

    model_config = ConfigDict(extra="forbid")

    brandSales: float = Field(description="The brand sales value for the postal code.")
    categorySales: float = Field(description="The category sales value for the postal code.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class CreateConstituentIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[CreateConstituentIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of brand and category sales values."
    )


class CreateDirectIndexValue(BaseModel):
    """Values for a location index where the indexValue is the pre-calculated index."""

    model_config = ConfigDict(extra="forbid")

    indexValue: float = Field(description="The pre-calculated index value.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class CreateDirectIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[CreateDirectIndexValue] = Field(
        min_length=1, max_length=1000000, description="List of direct index values."
    )


class CreateIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    directIndexValues: CreateDirectIndexValues | None = None
    constituentIndexValues: CreateConstituentIndexValues | None = None


class CreateLocationIndexRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    locationIndexes: list[LocationIndexCreate] = Field(min_length=1, max_length=10)


class DirectIndexValue(BaseModel):
    """Values for a location index where the indexValue is the pre-calculated index."""

    model_config = ConfigDict(extra="forbid")

    indexValue: float = Field(description="The pre-calculated index value.")
    postalCode: str = Field(
        description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class DirectIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[DirectIndexValue] = Field(min_length=1, max_length=1000000, description="List of direct index values.")


class IndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    constituentIndexValues: ConstituentIndexValues | None = None
    directIndexValues: DirectIndexValues | None = None


class LocationIndex(BaseModel):
    model_config = ConfigDict(extra="forbid")

    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = Field(default=None)
    creationDateTime: datetime = Field(description="The date time the location index was created.")
    indexData: IndexValues
    indexId: str = Field(description="The identifier of the location index.")
    indexName: str = Field(description="The name of the location index.")
    lastUpdatedDateTime: datetime = Field(description="The date time the location index was last updated successfully.")
    status: Annotated[IndexStatus | str, lenient_enum(IndexStatus)]


class LocationIndexCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = Field(default=None)
    indexData: CreateIndexValues
    indexName: str = Field(description="The name of the location index.")


class LocationIndexMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[LocationIndexMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class LocationIndexMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index: int = Field(ge=0, le=9)
    locationIndex: LocationIndex


class LocationIndexSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    locationIndexes: list[LocationIndex] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class LocationIndexUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    indexData: UpdateIndexValues | None = Field(default=None)
    indexId: str = Field(description="The identifier of the location index.")


class RetrieveLocationIndexRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    indexIds: list[str] = Field(min_length=1, max_length=10)


class UpdateConstituentIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[CreateConstituentIndexValue] | None = Field(
        default=None, min_length=1, max_length=1000000, description="List of brand and category sales values."
    )


class UpdateDirectIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[CreateDirectIndexValue] | None = Field(
        default=None, min_length=1, max_length=1000000, description="List of direct index values."
    )


class UpdateIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    directIndexValues: UpdateDirectIndexValues | None = None
    constituentIndexValues: UpdateConstituentIndexValues | None = None


class UpdateLocationIndexRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    locationIndexes: list[LocationIndexUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "IndexStatus",
    "ConstituentIndexValue",
    "ConstituentIndexValues",
    "CreateConstituentIndexValue",
    "CreateConstituentIndexValues",
    "CreateDirectIndexValue",
    "CreateDirectIndexValues",
    "CreateIndexValues",
    "CreateLocationIndexRequest",
    "DirectIndexValue",
    "DirectIndexValues",
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
