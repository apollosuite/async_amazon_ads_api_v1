"""Auto-generated models for AdvertisingDealTargets from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import SBErrorCode
from .shared import SBErrorsIndex


class SBAdvertisingDealTargetType(StrEnum):
    """
    | AdvertisingDealTargetType | Description |
    |------|------|
    | `BRANDED_KEYWORD` |  |
    """

    BRANDED_KEYWORD = "BRANDED_KEYWORD"


class SBAdvertisingDealBrandedKeywordTargetDetails(BaseModel):
    """The detail of a BRANDED_KEYWORD target."""

    model_config = ConfigDict(extra="allow")

    brandedKeyword: str | None = Field(
        default=None, description="The branded keyword that is an exact match to the shoppers' search term."
    )


class SBAdvertisingDealTarget(BaseModel):
    model_config = ConfigDict(extra="allow")

    advertisingDealId: str | None = Field(
        default=None, description="A unique identifier for the deal associated with the target."
    )
    advertisingDealTargetId: str | None = Field(default=None, description="A unique identifier for a deal target.")
    targetDetails: SBAdvertisingDealTargetDetails | None = Field(default=None)
    targetType: Annotated[SBAdvertisingDealTargetType | str, lenient_enum(SBAdvertisingDealTargetType)] | None = Field(
        default=None
    )


class SBAdvertisingDealTargetAdvertisingDealIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=1)


class SBAdvertisingDealTargetCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDealId: str = Field(description="A unique identifier for the deal associated with the target.")
    targetDetails: SBCreateAdvertisingDealTargetDetails
    targetType: Annotated[SBAdvertisingDealTargetType | str, lenient_enum(SBAdvertisingDealTargetType)]


class SBAdvertisingDealTargetDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    advertisingDealBrandedKeywordTargetDetails: SBAdvertisingDealBrandedKeywordTargetDetails | None = None


class SBAdvertisingDealTargetMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SBAdvertisingDealTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SBAdvertisingDealTargetMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    advertisingDealTarget: SBAdvertisingDealTarget | None = Field(default=None)
    index: int | None = Field(default=None, ge=0, le=999)


class SBAdvertisingDealTargetSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    advertisingDealTargets: list[SBAdvertisingDealTarget] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SBCreateAdvertisingDealBrandedKeywordTargetDetails(BaseModel):
    """The detail of a BRANDED_KEYWORD target."""

    model_config = ConfigDict(extra="forbid")

    brandedKeyword: str = Field(description="The branded keyword that is an exact match to the shoppers' search term.")


class SBCreateAdvertisingDealTargetDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDealBrandedKeywordTargetDetails: SBCreateAdvertisingDealBrandedKeywordTargetDetails | None = None


class SBCreateAdvertisingDealTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDealTargets: list[SBAdvertisingDealTargetCreate] | None = Field(
        default=None, min_length=1, max_length=1000
    )


class SBDeleteAdvertisingDealTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDealTargetIds: list[str] | None = Field(default=None, min_length=1, max_length=1000)


class SBQueryAdvertisingDealTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDealIdFilter: SBAdvertisingDealTargetAdvertisingDealIdFilter
    maxResults: int | None = Field(default=100, ge=100, le=1000)
    nextToken: str | None = Field(default=None)


__all__ = [
    "SBAdvertisingDealTargetAdvertisingDealIdFilter",
    "SBAdvertisingDealTargetCreate",
    "SBAdvertisingDealTargetType",
    "SBCreateAdvertisingDealBrandedKeywordTargetDetails",
    "SBCreateAdvertisingDealTargetDetails",
    "SBCreateAdvertisingDealTargetRequest",
    "SBDeleteAdvertisingDealTargetRequest",
    "SBErrorCode",
    "SBQueryAdvertisingDealTargetRequest",
]
