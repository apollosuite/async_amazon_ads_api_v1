"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.st import (
    STAdProduct,
    STCreateState,
    STCurrencyCode,
    STDeliveryReason,
    STDeliveryStatus,
    STError,
    STErrorCode,
    STErrorsIndex,
    STMarketplace,
    STState,
    STStatus,
    STUpdateState,
)

type STAdGroupNameFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


class STAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: STAdProduct | str
    bid: STAdGroupBid | None = Field(default=None)
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creationDateTime: datetime = Field(description="The date time that the ad group was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad group was last updated.")
    marketplaces: list[STMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: STState | str
    status: STStatus | None = Field(default=None)


class STAdGroupAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdGroupAdProductFilter(StrictModel):
    include: list[STAdProduct] = Field(min_length=1, max_length=1)


class STAdGroupBid(LenientModel):
    baseBid: float | None = Field(
        default=None,
        description="The lower bound bid used for the ads in the ad group. This field is optional for ad groups that use automated bid optimization; when omitted, the system manages bidding on your behalf. It remains required when automated bid optimization is false, or if automated bid optimization is not available (e.g. programmatic guaranteed deal).",
    )
    currencyCode: STCurrencyCode | str
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class STAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdGroupCreate(StrictModel):
    adProduct: STAdProduct
    bid: STCreateAdGroupBid | None = Field(default=None)
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    marketplaces: list[STMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: STCreateState


class STAdGroupMultiStatusResponse(LenientModel):
    error: list[STErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[STAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class STAdGroupMultiStatusSuccess(LenientModel):
    adGroup: STAdGroup
    index: int = Field(ge=0, le=99)


class STAdGroupNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: STAdGroupNameFilterType


class STAdGroupStateFilter(StrictModel):
    include: list[STState] = Field(min_length=1, max_length=3)


class STAdGroupSuccessResponse(LenientModel):
    adGroups: list[STAdGroup] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class STAdGroupUpdate(StrictModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: STAdProduct | None = Field(default=None)
    bid: STUpdateAdGroupBid | None = Field(default=None)
    marketplaces: list[STMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: STUpdateState | None = Field(default=None)


class STCreateAdGroupBid(StrictModel):
    baseBid: float | None = Field(
        default=None,
        description="The lower bound bid used for the ads in the ad group. This field is optional for ad groups that use automated bid optimization; when omitted, the system manages bidding on your behalf. It remains required when automated bid optimization is false, or if automated bid optimization is not available (e.g. programmatic guaranteed deal).",
    )
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class STCreateAdGroupRequest(StrictModel):
    adGroups: list[STAdGroupCreate] = Field(min_length=1, max_length=100)


class STQueryAdGroupRequest(StrictModel):
    adGroupIdFilter: STAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: STAdGroupAdProductFilter
    campaignIdFilter: STAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: STAdGroupNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: STAdGroupStateFilter | None = Field(default=None)


class STUpdateAdGroupBid(StrictModel):
    baseBid: float | None = Field(
        default=None,
        description="The lower bound bid used for the ads in the ad group. This field is optional for ad groups that use automated bid optimization; when omitted, the system manages bidding on your behalf. It remains required when automated bid optimization is false, or if automated bid optimization is not available (e.g. programmatic guaranteed deal).",
    )
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class STUpdateAdGroupRequest(StrictModel):
    adGroups: list[STAdGroupUpdate] = Field(min_length=1, max_length=100)


__all__ = [
    "STAdGroup",
    "STAdGroupAdGroupIdFilter",
    "STAdGroupAdProductFilter",
    "STAdGroupBid",
    "STAdGroupCampaignIdFilter",
    "STAdGroupCreate",
    "STAdGroupMultiStatusResponse",
    "STAdGroupMultiStatusSuccess",
    "STAdGroupNameFilter",
    "STAdGroupNameFilterType",
    "STAdGroupStateFilter",
    "STAdGroupSuccessResponse",
    "STAdGroupUpdate",
    "STAdProduct",
    "STCreateAdGroupBid",
    "STCreateAdGroupRequest",
    "STCreateState",
    "STCurrencyCode",
    "STDeliveryReason",
    "STDeliveryStatus",
    "STError",
    "STErrorCode",
    "STErrorsIndex",
    "STMarketplace",
    "STQueryAdGroupRequest",
    "STState",
    "STStatus",
    "STUpdateAdGroupBid",
    "STUpdateAdGroupRequest",
    "STUpdateState",
]
