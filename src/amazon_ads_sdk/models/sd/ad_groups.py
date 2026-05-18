"""Auto-generated Pydantic models for sd from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from amazon_ads_sdk.models.base import SafeStrEnum

if TYPE_CHECKING:
    from amazon_ads_sdk.errors import ErrorsIndex
    from .enums import (
        SDAdProduct,
        SDCreateState,
        SDCurrencyCode,
        SDMarketplace,
        SDMarketplaceScope,
        SDState,
        SDUpdateState,
    )
    from .shared import SDStatus


class SDAdGroup(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroupId: str  # The unique identifier of the ad group.
    adProduct: SDAdProduct
    bid: SDAdGroupBid | None = None
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    creationDateTime: datetime  # The date time that the ad group was created.
    creativeType: SDCreativeType | None = None
    lastUpdatedDateTime: datetime  # The date time that the ad group was last updated.
    marketplaceScope: SDMarketplaceScope
    marketplaces: list[
        SDMarketplace
    ]  # The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign
    name: str  # The name of the ad group.
    optimization: SDOptimization | None = None
    state: SDState
    status: SDStatus | None = None


class SDAdGroupAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]


class SDAdGroupAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[
        SDAdProduct
    ]  # AdProduct Description `SPONSORED_DISPLAY` Sponsored Display ad product.


class SDAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    currencyCode: SDCurrencyCode
    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.
    )


class SDAdGroupCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]


class SDAdGroupCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adProduct: SDAdProduct
    bid: SDCreateAdGroupBid | None = None
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    creativeType: SDCreativeType | None = None
    marketplaceScope: SDMarketplaceScope
    marketplaces: list[
        SDMarketplace
    ]  # The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign
    name: str  # The name of the ad group.
    optimization: SDCreateOptimization | None = None
    state: SDCreateState


class SDAdGroupGoalSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    kpi: SDKPI | None = None


class SDAdGroupMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = None
    success: list[SDAdGroupMultiStatusSuccess] | None = None


class SDAdGroupMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroup: SDAdGroup
    index: int


class SDAdGroupNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]
    queryTermMatchType: SDAdGroupNameFilterType


class SDAdGroupNameFilterType(SafeStrEnum):
    """| AdGroupNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SDAdGroupStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[
        SDState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SDAdGroupSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroups: list[SDAdGroup] | None = None
    nextToken: str | None = None


class SDAdGroupUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroupId: str  # The unique identifier of the ad group.
    bid: SDUpdateAdGroupBid | None = None
    name: str | None = None  # The name of the ad group.
    optimization: SDUpdateOptimization | None = None
    state: SDUpdateState | None = None


class SDCreateAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.
    )


class SDCreateAdGroupGoalSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    kpi: SDKPI | None = None


class SDCreateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroups: list[SDAdGroupCreate] | None = None


class SDCreateOptimization(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    goalSettings: SDCreateAdGroupGoalSettings | None = None


class SDCreativeType(SafeStrEnum):
    """| CreativeType | Description |
    |------|------|
    | `IMAGE` | An image creative. |
    | `VIDEO` | A video creative. |
    """

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDDeleteAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroupIds: list[str] | None = None


class SDKPI(SafeStrEnum):
    """| KPI | Description |
    |------|------|
    | `ADD_TO_CART` | Indicates a goal of driving improved add to cart |
    | `APPLICATIONS` | Indicates a goal of driving applications |
    | `CHECKOUTS` | Indicates a goal of driving improved checkouts |
    | `CLICKS` | Indicates a goal of driving clicks. |
    | `CONTACTS` | Indicates a goal of driving improved contacts |
    | `LEADS` | Indicates a goal of driving leads. |
    | `OTHER` | Indicates a goal of driving other metric |
    | `PAGE_VIEWS` | Indicates a goal of driving improved page views |
    | `PURCHASES` | Indicates a goal of driving improved purchases |
    | `REACH` | Indicates a goal of driving improved reach. |
    | `SEARCH` | Indicates a goal of driving improved search |
    | `SIGN_UP` | Indicates a goal of driving improved sign up |
    | `SUBSCRIBE` | Indicates a goal of driving improved subscriptions |
    """

    ADD_TO_CART = "ADD_TO_CART"
    APPLICATIONS = "APPLICATIONS"
    CHECKOUTS = "CHECKOUTS"
    CLICKS = "CLICKS"
    CONTACTS = "CONTACTS"
    LEADS = "LEADS"
    OTHER = "OTHER"
    PAGE_VIEWS = "PAGE_VIEWS"
    PURCHASES = "PURCHASES"
    REACH = "REACH"
    SEARCH = "SEARCH"
    SIGN_UP = "SIGN_UP"
    SUBSCRIBE = "SUBSCRIBE"


class SDOptimization(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    goalSettings: SDAdGroupGoalSettings | None = None


class SDQueryAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroupIdFilter: SDAdGroupAdGroupIdFilter | None = None
    adProductFilter: SDAdGroupAdProductFilter
    campaignIdFilter: SDAdGroupCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SDAdGroupNameFilter | None = None
    nextToken: str | None = None
    stateFilter: SDAdGroupStateFilter | None = None


class SDUpdateAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.
    )


class SDUpdateAdGroupGoalSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    kpi: SDKPI | None = None


class SDUpdateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroups: list[SDAdGroupUpdate] | None = None


class SDUpdateOptimization(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    goalSettings: SDUpdateAdGroupGoalSettings | None = None
