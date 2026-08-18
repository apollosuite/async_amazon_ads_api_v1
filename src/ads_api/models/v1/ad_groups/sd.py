"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
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

type SDAdGroupNameFilterType = Literal[
    "BROAD_MATCH",  # Filter by broad match.
    "EXACT_MATCH",  # Filter by exact match.
]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SDCreativeType = Literal[
    "IMAGE",  # An image creative.
    "VIDEO",  # A video creative.
]
"""
Supported values:
- `IMAGE`: An image creative.
- `VIDEO`: A video creative.
"""


type SDKPI = Literal[
    "ADD_TO_CART",  # Indicates a goal of driving improved add to cart
    "APPLICATIONS",  # Indicates a goal of driving applications
    "CHECKOUTS",  # Indicates a goal of driving improved checkouts
    "CLICKS",  # Indicates a goal of driving clicks.
    "CONTACTS",  # Indicates a goal of driving improved contacts
    "LEADS",  # Indicates a goal of driving leads.
    "OTHER",  # Indicates a goal of driving other metric
    "PAGE_VIEWS",  # Indicates a goal of driving improved page views
    "PURCHASES",  # Indicates a goal of driving improved purchases
    "REACH",  # Indicates a goal of driving improved reach.
    "SEARCH",  # Indicates a goal of driving improved search
    "SIGN_UP",  # Indicates a goal of driving improved sign up
    "SUBSCRIBE",  # Indicates a goal of driving improved subscriptions
]
"""
Supported values:
- `ADD_TO_CART`: Indicates a goal of driving improved add to cart
- `APPLICATIONS`: Indicates a goal of driving applications
- `CHECKOUTS`: Indicates a goal of driving improved checkouts
- `CLICKS`: Indicates a goal of driving clicks.
- `CONTACTS`: Indicates a goal of driving improved contacts
- `LEADS`: Indicates a goal of driving leads.
- `OTHER`: Indicates a goal of driving other metric
- `PAGE_VIEWS`: Indicates a goal of driving improved page views
- `PURCHASES`: Indicates a goal of driving improved purchases
- `REACH`: Indicates a goal of driving improved reach.
- `SEARCH`: Indicates a goal of driving improved search
- `SIGN_UP`: Indicates a goal of driving improved sign up
- `SUBSCRIBE`: Indicates a goal of driving improved subscriptions
"""


class SDAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: SDAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_DISPLAY`: Sponsored Display ad product.
""")
    bid: SDAdGroupBid | None = Field(default=None)
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creationDateTime: datetime = Field(description="The date time that the ad group was created.")
    creativeType: SDCreativeType | str | None = Field(
        default=None,
        description="""
Supported values:
- `IMAGE`: An image creative.
- `VIDEO`: A video creative.
""",
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad group was last updated.")
    marketplaceScope: SDMarketplaceScope | str
    marketplaces: list[SDMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    optimization: SDOptimization | None = Field(default=None)
    state: SDState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    status: SDStatus | None = Field(default=None)


class SDAdGroupAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDAdGroupAdProductFilter(StrictModel):
    include: list[SDAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_DISPLAY`: Sponsored Display ad product.
""",
    )


class SDAdGroupBid(LenientModel):
    currencyCode: SDCurrencyCode | str = Field(description="""
Supported values:
- `AED`: United Arab Emirates Dirham
- `AUD`: Australian Dollar
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `CHF`: Swiss Franc
- `CNY`: Chinese Yuan
- `DKK`: Danish Krone
- `EGP`: Egyptian Pound
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `INR`: Indian Rupee
- `JPY`: Japanese Yen
- `MXN`: Mexican Peso
- `MXP`: Mexican Peso
- `NGN`: Nigerian Naira
- `NOK`: Norwegian Krone
- `NZD`: New Zealand Dollar
- `PLN`: Polish Złoty
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `TRY`: Turkish Lira
- `USD`: United States Dollar
- `ZAR`: South African Rand
""")
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SDAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDAdGroupCreate(StrictModel):
    adProduct: SDAdProduct = Field(description="""
Supported values:
- `SPONSORED_DISPLAY`: Sponsored Display ad product.
""")
    bid: SDCreateAdGroupBid | None = Field(default=None)
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creativeType: SDCreativeType | None = Field(
        default=None,
        description="""
Supported values:
- `IMAGE`: An image creative.
- `VIDEO`: A video creative.
""",
    )
    marketplaceScope: SDMarketplaceScope
    marketplaces: list[SDMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    optimization: SDCreateOptimization | None = Field(default=None)
    state: SDCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")


class SDAdGroupGoalSettings(LenientModel):
    kpi: SDKPI | str | None = Field(
        default=None,
        description="""
Supported values:
- `ADD_TO_CART`: Indicates a goal of driving improved add to cart
- `APPLICATIONS`: Indicates a goal of driving applications
- `CHECKOUTS`: Indicates a goal of driving improved checkouts
- `CLICKS`: Indicates a goal of driving clicks.
- `CONTACTS`: Indicates a goal of driving improved contacts
- `LEADS`: Indicates a goal of driving leads.
- `OTHER`: Indicates a goal of driving other metric
- `PAGE_VIEWS`: Indicates a goal of driving improved page views
- `PURCHASES`: Indicates a goal of driving improved purchases
- `REACH`: Indicates a goal of driving improved reach.
- `SEARCH`: Indicates a goal of driving improved search
- `SIGN_UP`: Indicates a goal of driving improved sign up
- `SUBSCRIBE`: Indicates a goal of driving improved subscriptions
""",
    )


class SDAdGroupMultiStatusResponse(LenientModel):
    error: list[SDErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[SDAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class SDAdGroupMultiStatusSuccess(LenientModel):
    adGroup: SDAdGroup
    index: int = Field(ge=0, le=99)


class SDAdGroupNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: SDAdGroupNameFilterType = Field(description="""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
""")


class SDAdGroupStateFilter(StrictModel):
    include: list[SDState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SDAdGroupSuccessResponse(LenientModel):
    adGroups: list[SDAdGroup] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SDAdGroupUpdate(StrictModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    bid: SDUpdateAdGroupBid | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad group.")
    optimization: SDUpdateOptimization | None = Field(default=None)
    state: SDUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SDCreateAdGroupBid(StrictModel):
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SDCreateAdGroupGoalSettings(StrictModel):
    kpi: SDKPI | None = Field(
        default=None,
        description="""
Supported values:
- `ADD_TO_CART`: Indicates a goal of driving improved add to cart
- `APPLICATIONS`: Indicates a goal of driving applications
- `CHECKOUTS`: Indicates a goal of driving improved checkouts
- `CLICKS`: Indicates a goal of driving clicks.
- `CONTACTS`: Indicates a goal of driving improved contacts
- `LEADS`: Indicates a goal of driving leads.
- `OTHER`: Indicates a goal of driving other metric
- `PAGE_VIEWS`: Indicates a goal of driving improved page views
- `PURCHASES`: Indicates a goal of driving improved purchases
- `REACH`: Indicates a goal of driving improved reach.
- `SEARCH`: Indicates a goal of driving improved search
- `SIGN_UP`: Indicates a goal of driving improved sign up
- `SUBSCRIBE`: Indicates a goal of driving improved subscriptions
""",
    )


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
    kpi: SDKPI | None = Field(
        default=None,
        description="""
Supported values:
- `ADD_TO_CART`: Indicates a goal of driving improved add to cart
- `APPLICATIONS`: Indicates a goal of driving applications
- `CHECKOUTS`: Indicates a goal of driving improved checkouts
- `CLICKS`: Indicates a goal of driving clicks.
- `CONTACTS`: Indicates a goal of driving improved contacts
- `LEADS`: Indicates a goal of driving leads.
- `OTHER`: Indicates a goal of driving other metric
- `PAGE_VIEWS`: Indicates a goal of driving improved page views
- `PURCHASES`: Indicates a goal of driving improved purchases
- `REACH`: Indicates a goal of driving improved reach.
- `SEARCH`: Indicates a goal of driving improved search
- `SIGN_UP`: Indicates a goal of driving improved sign up
- `SUBSCRIBE`: Indicates a goal of driving improved subscriptions
""",
    )


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
