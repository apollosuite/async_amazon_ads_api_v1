"""Auto-generated Pydantic models for sd from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

if TYPE_CHECKING:
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
del TYPE_CHECKING


class SDAdGroup(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    bid: SDAdGroupBid | None = None
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    creationDateTime: datetime  # The date time that the ad group was created.
    creativeType: Annotated[SDCreativeType | str, lenient_enum(SDCreativeType)] | None = None
    lastUpdatedDateTime: datetime  # The date time that the ad group was last updated.
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[
        Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]
    ]  # The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign
    name: str  # The name of the ad group.
    optimization: SDOptimization | None = None
    state: Annotated[SDState | str, lenient_enum(SDState)]
    status: SDStatus | None = None


class SDAdGroupAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SDAdGroupAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    ]  # **AdProduct Enum:** AdProduct Description `SPONSORED_DISPLAY` Sponsored Display ad product.


class SDAdGroupBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    currencyCode: Annotated[SDCurrencyCode | str, lenient_enum(SDCurrencyCode)]
    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.
    )


class SDAdGroupCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SDAdGroupCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    bid: SDCreateAdGroupBid | None = None
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    creativeType: Annotated[SDCreativeType | str, lenient_enum(SDCreativeType)] | None = None
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[
        Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]
    ]  # The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign
    name: str  # The name of the ad group.
    optimization: SDCreateOptimization | None = None
    state: Annotated[SDCreateState | str, lenient_enum(SDCreateState)]


class SDAdGroupGoalSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kpi: Annotated[SDKPI | str, lenient_enum(SDKPI)] | None = None


class SDAdGroupMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SDAdGroupMultiStatusSuccess] | None = None


class SDAdGroupMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroup: SDAdGroup
    index: int


class SDAdGroupNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: Annotated[SDAdGroupNameFilterType | str, lenient_enum(SDAdGroupNameFilterType)]


class SDAdGroupNameFilterType(StrEnum):
    """**AdGroupNameFilterType Enum:**
    | AdGroupNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SDAdGroupStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SDState | str, lenient_enum(SDState)]
    ]  # **State Enum:** State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SDAdGroupSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SDAdGroup] | None = None
    nextToken: str | None = None


class SDAdGroupUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    bid: SDUpdateAdGroupBid | None = None
    name: str | None = None  # The name of the ad group.
    optimization: SDUpdateOptimization | None = None
    state: Annotated[SDUpdateState | str, lenient_enum(SDUpdateState)] | None = None


class SDCreateAdGroupBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.
    )


class SDCreateAdGroupGoalSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kpi: Annotated[SDKPI | str, lenient_enum(SDKPI)] | None = None


class SDCreateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SDAdGroupCreate]


class SDCreateOptimization(BaseModel):
    model_config = ConfigDict(extra="forbid")

    goalSettings: SDCreateAdGroupGoalSettings | None = None


class SDCreativeType(StrEnum):
    """**CreativeType Enum:**

    | CreativeType | Description |
    |------|------|
    | `IMAGE` | An image creative. |
    | `VIDEO` | A video creative. |
    """

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDDeleteAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIds: list[str]


class SDKPI(StrEnum):
    """**KPI Enum:**

    | KPI | Description |
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
    model_config = ConfigDict(extra="forbid")

    goalSettings: SDAdGroupGoalSettings | None = None


class SDQueryAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SDAdGroupAdGroupIdFilter | None = None
    adProductFilter: SDAdGroupAdProductFilter
    campaignIdFilter: SDAdGroupCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SDAdGroupNameFilter | None = None
    nextToken: str | None = None
    stateFilter: SDAdGroupStateFilter | None = None


class SDUpdateAdGroupBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.
    )


class SDUpdateAdGroupGoalSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kpi: Annotated[SDKPI | str, lenient_enum(SDKPI)] | None = None


class SDUpdateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SDAdGroupUpdate]


class SDUpdateOptimization(BaseModel):
    model_config = ConfigDict(extra="forbid")

    goalSettings: SDUpdateAdGroupGoalSettings | None = None


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
    "SDCreateAdGroupBid",
    "SDCreateAdGroupGoalSettings",
    "SDCreateAdGroupRequest",
    "SDCreateOptimization",
    "SDCreativeType",
    "SDDeleteAdGroupRequest",
    "SDKPI",
    "SDOptimization",
    "SDQueryAdGroupRequest",
    "SDUpdateAdGroupBid",
    "SDUpdateAdGroupGoalSettings",
    "SDUpdateAdGroupRequest",
    "SDUpdateOptimization",
]
