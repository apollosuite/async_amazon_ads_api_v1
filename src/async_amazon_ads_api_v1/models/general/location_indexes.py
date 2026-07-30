"""Auto-generated models for LocationIndexes from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import GeneralCountryCode, GeneralErrorCode
from .shared import GeneralErrorsIndex


class IndexStatus(StrEnum):
    """
    **IndexStatus Enum:**

    | IndexStatus | Description |
    |------|------|
    | `ENABLED` | The location index is active and can be used in smart locations. |
    | `FAILED` | The location index creation failed and cannot be used in smart locations. |
    | `PENDING` | The location index is being created and cannot be used in smart locations yet. |
    | `UPDATE_FAILED` | The location index update has failed, but the old version can still be used. |
    """

    ENABLED = "ENABLED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    UPDATE_FAILED = "UPDATE_FAILED"


class ConstituentIndexValue(BaseModel):
    """Values for a location index where the indexValue is calculated from the constituents."""

    model_config = ConfigDict(extra="allow")

    brandSales: float | None = Field(default=None, description="The brand sales value for the postal code.")
    categorySales: float | None = Field(default=None, description="The category sales value for the postal code.")
    postalCode: str | None = Field(
        default=None, description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class ConstituentIndexValues(BaseModel):
    model_config = ConfigDict(extra="allow")

    values: list[ConstituentIndexValue] | None = Field(
        default=None, min_length=1, max_length=1000000, description="List of brand and category sales values."
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

    model_config = ConfigDict(extra="allow")

    indexValue: float | None = Field(default=None, description="The pre-calculated index value.")
    postalCode: str | None = Field(
        default=None, description="The postal code for the location index prefixed by country code (i.e. US-10118)."
    )


class DirectIndexValues(BaseModel):
    model_config = ConfigDict(extra="allow")

    values: list[DirectIndexValue] | None = Field(
        default=None, min_length=1, max_length=1000000, description="List of direct index values."
    )


class IndexValues(BaseModel):
    model_config = ConfigDict(extra="allow")

    constituentIndexValues: ConstituentIndexValues | None = None
    directIndexValues: DirectIndexValues | None = None


class LocationIndex(BaseModel):
    model_config = ConfigDict(extra="allow")

    countryCode: Annotated[GeneralCountryCode | str, lenient_enum(GeneralCountryCode)] | None = Field(default=None)
    creationDateTime: datetime | None = Field(default=None, description="The date time the location index was created.")
    indexData: IndexValues | None = Field(default=None)
    indexId: str | None = Field(default=None, description="The identifier of the location index.")
    indexName: str | None = Field(default=None, description="The name of the location index.")
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time the location index was last updated successfully."
    )
    status: Annotated[IndexStatus | str, lenient_enum(IndexStatus)] | None = Field(default=None)


class LocationIndexCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    countryCode: Annotated[GeneralCountryCode | str, lenient_enum(GeneralCountryCode)] | None = Field(default=None)
    indexData: CreateIndexValues
    indexName: str = Field(description="The name of the location index.")


class LocationIndexMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[GeneralErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[LocationIndexMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class LocationIndexMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int | None = Field(default=None, ge=0, le=9)
    locationIndex: LocationIndex | None = Field(default=None)


class LocationIndexSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

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
    "CreateConstituentIndexValue",
    "CreateConstituentIndexValues",
    "CreateDirectIndexValue",
    "CreateDirectIndexValues",
    "CreateIndexValues",
    "CreateLocationIndexRequest",
    "GeneralCountryCode",
    "GeneralErrorCode",
    "IndexStatus",
    "LocationIndexCreate",
    "LocationIndexUpdate",
    "RetrieveLocationIndexRequest",
    "UpdateConstituentIndexValues",
    "UpdateDirectIndexValues",
    "UpdateIndexValues",
    "UpdateLocationIndexRequest",
]
