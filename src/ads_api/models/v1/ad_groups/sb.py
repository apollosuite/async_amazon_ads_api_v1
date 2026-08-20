"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBAdProduct,
    SBCreateState,
    SBCreateTag,
    SBDeliveryReason,
    SBDeliveryStatus,
    SBError,
    SBErrorCode,
    SBErrorsIndex,
    SBMarketplaceScope,
    SBState,
    SBStatus,
    SBTag,
    SBUpdateState,
)

type SBAdGroupNameFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SBMarketplace = Literal[
    "AE",
    "AU",
    "BE",
    "BR",
    "CA",
    "DE",
    "EG",
    "ES",
    "FR",
    "GB",
    "IE",
    "IN",
    "IT",
    "JP",
    "MX",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "US",
    "ZA",
]
"""
A list of country codes representing Amazon marketplaces
"""


class SBAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: SBAdProduct | str
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creationDateTime: datetime = Field(description="The date time that the ad group was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad group was last updated.")
    marketplaceScope: SBMarketplaceScope | str
    marketplaces: list[SBMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: SBState | str
    status: SBStatus | None = Field(default=None)
    tags: list[SBTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SBAdGroupAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBAdGroupAdProductFilter(StrictModel):
    include: list[SBAdProduct] = Field(min_length=1, max_length=1)


class SBAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBAdGroupCreate(StrictModel):
    adProduct: SBAdProduct
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    name: str = Field(description="The name of the ad group.")
    state: SBCreateState
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SBAdGroupMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBAdGroupMultiStatusSuccess(LenientModel):
    adGroup: SBAdGroup
    index: int = Field(ge=0, le=9)


class SBAdGroupNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: SBAdGroupNameFilterType


class SBAdGroupStateFilter(StrictModel):
    include: list[SBState] = Field(min_length=1, max_length=3)


class SBAdGroupSuccessResponse(LenientModel):
    adGroups: list[SBAdGroup] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SBAdGroupUpdate(StrictModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: SBUpdateState | None = Field(default=None)
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SBCreateAdGroupRequest(StrictModel):
    adGroups: list[SBAdGroupCreate] = Field(min_length=1, max_length=10)


class SBDeleteAdGroupRequest(StrictModel):
    adGroupIds: list[str] = Field(min_length=1, max_length=10)


class SBQueryAdGroupRequest(StrictModel):
    adGroupIdFilter: SBAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SBAdGroupAdProductFilter
    campaignIdFilter: SBAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SBAdGroupNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SBAdGroupStateFilter | None = Field(default=None)


class SBUpdateAdGroupRequest(StrictModel):
    adGroups: list[SBAdGroupUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "SBAdGroup",
    "SBAdGroupAdGroupIdFilter",
    "SBAdGroupAdProductFilter",
    "SBAdGroupCampaignIdFilter",
    "SBAdGroupCreate",
    "SBAdGroupMultiStatusResponse",
    "SBAdGroupMultiStatusSuccess",
    "SBAdGroupNameFilter",
    "SBAdGroupNameFilterType",
    "SBAdGroupStateFilter",
    "SBAdGroupSuccessResponse",
    "SBAdGroupUpdate",
    "SBAdProduct",
    "SBCreateAdGroupRequest",
    "SBCreateState",
    "SBCreateTag",
    "SBDeleteAdGroupRequest",
    "SBDeliveryReason",
    "SBDeliveryStatus",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBQueryAdGroupRequest",
    "SBState",
    "SBStatus",
    "SBTag",
    "SBUpdateAdGroupRequest",
    "SBUpdateState",
]
