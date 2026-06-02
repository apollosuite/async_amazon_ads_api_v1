"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from async_amazon_ads_api_v1.errors import ErrorsIndex
del TYPE_CHECKING


class SBAdvertisingDealBrandedKeywordTargetDetails(BaseModel):
    """The detail of a BRANDED_KEYWORD target."""

    model_config = ConfigDict(extra="forbid")

    brandedKeyword: str  # The branded keyword that is an exact match to the shoppers' search term.


class SBAdvertisingDealTarget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealId: str  # A unique identifier for the deal associated with the target.
    advertisingDealTargetId: str  # A unique identifier for a deal target.
    targetDetails: SBAdvertisingDealTargetDetails
    targetType: SBAdvertisingDealTargetType


class SBAdvertisingDealTargetAdvertisingDealIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdvertisingDealTargetCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealId: str  # A unique identifier for the deal associated with the target.
    targetDetails: SBCreateAdvertisingDealTargetDetails
    targetType: SBAdvertisingDealTargetType


class SBAdvertisingDealTargetDetails(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealBrandedKeywordTargetDetails: (
        SBAdvertisingDealBrandedKeywordTargetDetails | None
    ) = None


class SBAdvertisingDealTargetMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBAdvertisingDealTargetMultiStatusSuccess] | None = None


class SBAdvertisingDealTargetMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealTarget: SBAdvertisingDealTarget
    index: int


class SBAdvertisingDealTargetSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealTargets: list[SBAdvertisingDealTarget] | None = None
    nextToken: str | None = None


class SBAdvertisingDealTargetType(StrEnum):
    """| AdvertisingDealTargetType | Description |
    |------|------|
    | `BRANDED_KEYWORD` |  |
    """

    BRANDED_KEYWORD = "BRANDED_KEYWORD"


class SBCreateAdvertisingDealBrandedKeywordTargetDetails(BaseModel):
    """The detail of a BRANDED_KEYWORD target."""

    model_config = ConfigDict(extra="forbid")

    brandedKeyword: str  # The branded keyword that is an exact match to the shoppers' search term.


class SBCreateAdvertisingDealTargetDetails(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealBrandedKeywordTargetDetails: (
        SBCreateAdvertisingDealBrandedKeywordTargetDetails | None
    ) = None


class SBCreateAdvertisingDealTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealTargets: list[SBAdvertisingDealTargetCreate] | None = None


class SBDeleteAdvertisingDealTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealTargetIds: list[str] | None = None


class SBQueryAdvertisingDealTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealIdFilter: SBAdvertisingDealTargetAdvertisingDealIdFilter
    maxResults: int | None = None
    nextToken: str | None = None


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
    "SBQueryAdvertisingDealTargetRequest",
]
