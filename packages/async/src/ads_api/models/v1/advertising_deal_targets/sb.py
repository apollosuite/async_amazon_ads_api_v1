"""Auto-generated models for AdvertisingDealTargets from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBError,
    SBErrorCode,
    SBErrorsIndex,
)

type SBAdvertisingDealTargetType = Literal["BRANDED_KEYWORD"]


class SBAdvertisingDealBrandedKeywordTargetDetails(LenientModel):
    """The detail of a BRANDED_KEYWORD target."""

    brandedKeyword: str = Field(description="The branded keyword that is an exact match to the shoppers' search term.")


class SBAdvertisingDealTarget(LenientModel):
    advertisingDealId: str = Field(description="A unique identifier for the deal associated with the target.")
    advertisingDealTargetId: str = Field(description="A unique identifier for a deal target.")
    targetDetails: SBAdvertisingDealTargetDetails
    targetType: SBAdvertisingDealTargetType | str


class SBAdvertisingDealTargetAdvertisingDealIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class SBAdvertisingDealTargetCreate(StrictModel):
    advertisingDealId: str = Field(description="A unique identifier for the deal associated with the target.")
    targetDetails: SBCreateAdvertisingDealTargetDetails
    targetType: SBAdvertisingDealTargetType


class SBAdvertisingDealTargetDetails(LenientModel):
    advertisingDealBrandedKeywordTargetDetails: SBAdvertisingDealBrandedKeywordTargetDetails


class SBAdvertisingDealTargetMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SBAdvertisingDealTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SBAdvertisingDealTargetMultiStatusSuccess(LenientModel):
    advertisingDealTarget: SBAdvertisingDealTarget
    index: int = Field(ge=0, le=999)


class SBAdvertisingDealTargetSuccessResponse(LenientModel):
    advertisingDealTargets: list[SBAdvertisingDealTarget] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SBCreateAdvertisingDealBrandedKeywordTargetDetails(StrictModel):
    """The detail of a BRANDED_KEYWORD target."""

    brandedKeyword: str = Field(description="The branded keyword that is an exact match to the shoppers' search term.")


class SBCreateAdvertisingDealTargetDetails(StrictModel):
    advertisingDealBrandedKeywordTargetDetails: SBCreateAdvertisingDealBrandedKeywordTargetDetails


class SBCreateAdvertisingDealTargetRequest(StrictModel):
    advertisingDealTargets: list[SBAdvertisingDealTargetCreate] | None = Field(
        default=None, min_length=1, max_length=1000
    )


class SBDeleteAdvertisingDealTargetRequest(StrictModel):
    advertisingDealTargetIds: list[str] | None = Field(default=None, min_length=1, max_length=1000)


class SBQueryAdvertisingDealTargetRequest(StrictModel):
    advertisingDealIdFilter: SBAdvertisingDealTargetAdvertisingDealIdFilter
    maxResults: int | None = Field(default=100, ge=100, le=1000)
    nextToken: str | None = Field(default=None)


__all__ = [
    "SBAdvertisingDealBrandedKeywordTargetDetails",
    "SBAdvertisingDealTarget",
    "SBAdvertisingDealTargetAdvertisingDealIdFilter",
    "SBAdvertisingDealTargetCreate",
    "SBAdvertisingDealTargetDetails",
    "SBAdvertisingDealTargetMultiStatusResponse",
    "SBAdvertisingDealTargetMultiStatusSuccess",
    "SBAdvertisingDealTargetSuccessResponse",
    "SBAdvertisingDealTargetType",
    "SBCreateAdvertisingDealBrandedKeywordTargetDetails",
    "SBCreateAdvertisingDealTargetDetails",
    "SBCreateAdvertisingDealTargetRequest",
    "SBDeleteAdvertisingDealTargetRequest",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBQueryAdvertisingDealTargetRequest",
]
