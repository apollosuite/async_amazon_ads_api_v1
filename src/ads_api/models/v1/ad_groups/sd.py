"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.sd import (
    SDAdProduct,
    SDCreateState,
    SDCurrencyCode,
    SDDeliveryReason,
    SDDeliveryStatus,
    SDError,
    SDErrorCode,
    SDErrorsIndex,
    SDMarketplace,
    SDMarketplaceScope,
    SDState,
    SDStatus,
    SDUpdateState,
)


class SDAdGroupNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SDCreativeType(StrEnum):
    IMAGE = "IMAGE"  # An image creative.
    VIDEO = "VIDEO"  # A video creative.


class SDKPI(StrEnum):
    ADD_TO_CART = "ADD_TO_CART"  # Indicates a goal of driving improved add to cart
    APPLICATIONS = "APPLICATIONS"  # Indicates a goal of driving applications
    CHECKOUTS = "CHECKOUTS"  # Indicates a goal of driving improved checkouts
    CLICKS = "CLICKS"  # Indicates a goal of driving clicks.
    CONTACTS = "CONTACTS"  # Indicates a goal of driving improved contacts
    LEADS = "LEADS"  # Indicates a goal of driving leads.
    OTHER = "OTHER"  # Indicates a goal of driving other metric
    PAGE_VIEWS = "PAGE_VIEWS"  # Indicates a goal of driving improved page views
    PURCHASES = "PURCHASES"  # Indicates a goal of driving improved purchases
    REACH = "REACH"  # Indicates a goal of driving improved reach.
    SEARCH = "SEARCH"  # Indicates a goal of driving improved search
    SIGN_UP = "SIGN_UP"  # Indicates a goal of driving improved sign up
    SUBSCRIBE = "SUBSCRIBE"  # Indicates a goal of driving improved subscriptions


class SDAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    bid: SDAdGroupBid | None = Field(default=None)
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creationDateTime: datetime = Field(description="The date time that the ad group was created.")
    creativeType: Annotated[SDCreativeType | str, lenient_enum(SDCreativeType)] | None = Field(default=None)
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad group was last updated.")
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    optimization: SDOptimization | None = Field(default=None)
    state: Annotated[SDState | str, lenient_enum(SDState)]
    status: SDStatus | None = Field(default=None)


class SDAdGroupAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDAdGroupAdProductFilter(StrictModel):
    include: list[Annotated[SDAdProduct, lenient_enum(SDAdProduct)]] = Field(min_length=1, max_length=1)


class SDAdGroupBid(LenientModel):
    currencyCode: Annotated[SDCurrencyCode | str, lenient_enum(SDCurrencyCode)]
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SDAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDAdGroupCreate(StrictModel):
    adProduct: Annotated[SDAdProduct, lenient_enum(SDAdProduct)]
    bid: SDCreateAdGroupBid | None = Field(default=None)
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creativeType: Annotated[SDCreativeType, lenient_enum(SDCreativeType)] | None = Field(default=None)
    marketplaceScope: Annotated[SDMarketplaceScope, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace, lenient_enum(SDMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    optimization: SDCreateOptimization | None = Field(default=None)
    state: Annotated[SDCreateState, lenient_enum(SDCreateState)]


class SDAdGroupGoalSettings(LenientModel):
    kpi: Annotated[SDKPI | str, lenient_enum(SDKPI)] | None = Field(default=None)


class SDAdGroupMultiStatusResponse(LenientModel):
    error: list[SDErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[SDAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class SDAdGroupMultiStatusSuccess(LenientModel):
    adGroup: SDAdGroup
    index: int = Field(ge=0, le=99)


class SDAdGroupNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SDAdGroupNameFilterType, lenient_enum(SDAdGroupNameFilterType)]


class SDAdGroupStateFilter(StrictModel):
    include: list[Annotated[SDState, lenient_enum(SDState)]] = Field(min_length=1, max_length=3)


class SDAdGroupSuccessResponse(LenientModel):
    adGroups: list[SDAdGroup] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SDAdGroupUpdate(StrictModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    bid: SDUpdateAdGroupBid | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad group.")
    optimization: SDUpdateOptimization | None = Field(default=None)
    state: Annotated[SDUpdateState, lenient_enum(SDUpdateState)] | None = Field(default=None)


class SDCreateAdGroupBid(StrictModel):
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SDCreateAdGroupGoalSettings(StrictModel):
    kpi: Annotated[SDKPI, lenient_enum(SDKPI)] | None = Field(default=None)


class SDCreateAdGroupRequest(StrictModel):
    adGroups: list[SDAdGroupCreate] = Field(min_length=1, max_length=100)


class SDCreateOptimization(StrictModel):
    goalSettings: SDCreateAdGroupGoalSettings | None = Field(default=None)


class SDDeleteAdGroupRequest(StrictModel):
    adGroupIds: list[str] = Field(min_length=1, max_length=100)


class SDOptimization(LenientModel):
    goalSettings: SDAdGroupGoalSettings | None = Field(default=None)


class SDQueryAdGroupRequest(StrictModel):
    adGroupIdFilter: SDAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SDAdGroupAdProductFilter
    campaignIdFilter: SDAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SDAdGroupNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SDAdGroupStateFilter | None = Field(default=None)


class SDUpdateAdGroupBid(StrictModel):
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SDUpdateAdGroupGoalSettings(StrictModel):
    kpi: Annotated[SDKPI, lenient_enum(SDKPI)] | None = Field(default=None)


class SDUpdateAdGroupRequest(StrictModel):
    adGroups: list[SDAdGroupUpdate] = Field(min_length=1, max_length=100)


class SDUpdateOptimization(StrictModel):
    goalSettings: SDUpdateAdGroupGoalSettings | None = Field(default=None)


__all__ = [
    "SDAdGroup",
    "SDAdGroupAdGroupIdFilter",
    "SDAdGroupAdProductFilter",
    "SDAdGroupBid",
    "SDAdGroupCampaignIdFilter",
    "SDAdGroupCreate",
    "SDAdGroupGoalSettings",
    "SDAdGroupMultiStatusResponse",
    "SDAdGroupMultiStatusSuccess",
    "SDAdGroupNameFilter",
    "SDAdGroupNameFilterType",
    "SDAdGroupStateFilter",
    "SDAdGroupSuccessResponse",
    "SDAdGroupUpdate",
    "SDAdProduct",
    "SDCreateAdGroupBid",
    "SDCreateAdGroupGoalSettings",
    "SDCreateAdGroupRequest",
    "SDCreateOptimization",
    "SDCreateState",
    "SDCreativeType",
    "SDCurrencyCode",
    "SDDeleteAdGroupRequest",
    "SDDeliveryReason",
    "SDDeliveryStatus",
    "SDError",
    "SDErrorCode",
    "SDErrorsIndex",
    "SDKPI",
    "SDMarketplace",
    "SDMarketplaceScope",
    "SDOptimization",
    "SDQueryAdGroupRequest",
    "SDState",
    "SDStatus",
    "SDUpdateAdGroupBid",
    "SDUpdateAdGroupGoalSettings",
    "SDUpdateAdGroupRequest",
    "SDUpdateOptimization",
    "SDUpdateState",
]
