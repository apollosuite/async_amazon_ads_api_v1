"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from amazon_ads_sdk.models.base import SafeStrEnum

if TYPE_CHECKING:
    from amazon_ads_sdk.errors import ErrorsIndex


class SBAdvertisingDealBrandedKeywordTargetDetails(BaseModel):
    """The detail of a BRANDED_KEYWORD target."""

    model_config = ConfigDict(extra="allow")

    brandedKeyword: str  # The branded keyword that is an exact match to the shoppers' search term.


class SBAdvertisingDealTarget(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    advertisingDealId: str  # A unique identifier for the deal associated with the target.
    advertisingDealTargetId: str  # A unique identifier for a deal target.
    targetDetails: SBAdvertisingDealTargetDetails
    targetType: SBAdvertisingDealTargetType


class SBAdvertisingDealTargetAdvertisingDealIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]


class SBAdvertisingDealTargetCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    advertisingDealId: str  # A unique identifier for the deal associated with the target.
    targetDetails: SBCreateAdvertisingDealTargetDetails
    targetType: SBAdvertisingDealTargetType


class SBAdvertisingDealTargetDetails(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    advertisingDealBrandedKeywordTargetDetails: (
        SBAdvertisingDealBrandedKeywordTargetDetails | None
    ) = None


class SBAdvertisingDealTargetMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = None
    success: list[SBAdvertisingDealTargetMultiStatusSuccess] | None = None


class SBAdvertisingDealTargetMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    advertisingDealTarget: SBAdvertisingDealTarget
    index: int


class SBAdvertisingDealTargetSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    advertisingDealTargets: list[SBAdvertisingDealTarget] | None = None
    nextToken: str | None = None


class SBAdvertisingDealTargetType(SafeStrEnum):
    """| AdvertisingDealTargetType | Description |
    |------|------|
    | `BRANDED_KEYWORD` |  |
    """

    BRANDED_KEYWORD = "BRANDED_KEYWORD"


class SBCreateAdvertisingDealBrandedKeywordTargetDetails(BaseModel):
    """The detail of a BRANDED_KEYWORD target."""

    model_config = ConfigDict(extra="allow")

    brandedKeyword: str  # The branded keyword that is an exact match to the shoppers' search term.


class SBCreateAdvertisingDealTargetDetails(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    advertisingDealBrandedKeywordTargetDetails: (
        SBCreateAdvertisingDealBrandedKeywordTargetDetails | None
    ) = None


class SBCreateAdvertisingDealTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    advertisingDealTargets: list[SBAdvertisingDealTargetCreate] | None = None


class SBDeleteAdvertisingDealTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    advertisingDealTargetIds: list[str] | None = None


class SBQueryAdvertisingDealTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    advertisingDealIdFilter: SBAdvertisingDealTargetAdvertisingDealIdFilter
    maxResults: int | None = None
    nextToken: str | None = None
