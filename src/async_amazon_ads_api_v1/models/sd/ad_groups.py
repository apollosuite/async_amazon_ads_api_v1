"""Auto-generated models for AdGroups from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import (
    SDAdProduct,
    SDCreateState,
    SDCurrencyCode,
    SDDeliveryReason,
    SDDeliveryStatus,
    SDErrorCode,
    SDMarketplace,
    SDMarketplaceScope,
    SDState,
    SDUpdateState,
)
from .shared import SDErrorsIndex, SDStatus


class SDAdGroupNameFilterType(StrEnum):
    """
    **AdGroupNameFilterType Enum:**
    | AdGroupNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SDCreativeType(StrEnum):
    """
    **CreativeType Enum:**

    | CreativeType | Description |
    |------|------|
    | `IMAGE` | An image creative. |
    | `VIDEO` | A video creative. |
    """

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDKPI(StrEnum):
    """
    **KPI Enum:**

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


class SDAdGroup(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SDAdGroupAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SDAdGroupAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_DISPLAY` | Sponsored Display ad product. |
""",
    )


class SDAdGroupBid(BaseModel):
    model_config = ConfigDict(extra="allow")

    currencyCode: Annotated[SDCurrencyCode | str, lenient_enum(SDCurrencyCode)]
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SDAdGroupCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SDAdGroupCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    bid: SDCreateAdGroupBid | None = Field(default=None)
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creativeType: Annotated[SDCreativeType | str, lenient_enum(SDCreativeType)] | None = Field(default=None)
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    optimization: SDCreateOptimization | None = Field(default=None)
    state: Annotated[SDCreateState | str, lenient_enum(SDCreateState)]


class SDAdGroupGoalSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    kpi: Annotated[SDKPI | str, lenient_enum(SDKPI)] | None = Field(default=None)


class SDAdGroupMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[SDErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[SDAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class SDAdGroupMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroup: SDAdGroup
    index: int = Field(ge=0, le=99)


class SDAdGroupNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SDAdGroupNameFilterType | str, lenient_enum(SDAdGroupNameFilterType)]


class SDAdGroupStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SDState | str, lenient_enum(SDState)]] = Field(
        min_length=1,
        max_length=3,
        description="""
**State Enum:**
| State | Description |
| --- | --- |
| `ENABLED` | The object is set active by user and eligible for delivery. |
| `PAUSED` | The object is stopped by user and not eligible for delivery. |
| `ARCHIVED` | The object is permanently stopped and cannot be reactivated. Terminal end state. |
""",
    )


class SDAdGroupSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroups: list[SDAdGroup] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SDAdGroupUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str = Field(description="The unique identifier of the ad group.")
    bid: SDUpdateAdGroupBid | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad group.")
    optimization: SDUpdateOptimization | None = Field(default=None)
    state: Annotated[SDUpdateState | str, lenient_enum(SDUpdateState)] | None = Field(default=None)


class SDCreateAdGroupBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SDCreateAdGroupGoalSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kpi: Annotated[SDKPI | str, lenient_enum(SDKPI)] | None = Field(default=None)


class SDCreateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SDAdGroupCreate] = Field(min_length=1, max_length=100)


class SDCreateOptimization(BaseModel):
    model_config = ConfigDict(extra="forbid")

    goalSettings: SDCreateAdGroupGoalSettings | None = Field(default=None)


class SDDeleteAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIds: list[str] = Field(min_length=1, max_length=100)


class SDOptimization(BaseModel):
    model_config = ConfigDict(extra="allow")

    goalSettings: SDAdGroupGoalSettings | None = Field(default=None)


class SDQueryAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SDAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SDAdGroupAdProductFilter
    campaignIdFilter: SDAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SDAdGroupNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SDAdGroupStateFilter | None = Field(default=None)


class SDUpdateAdGroupBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SDUpdateAdGroupGoalSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kpi: Annotated[SDKPI | str, lenient_enum(SDKPI)] | None = Field(default=None)


class SDUpdateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SDAdGroupUpdate] = Field(min_length=1, max_length=100)


class SDUpdateOptimization(BaseModel):
    model_config = ConfigDict(extra="forbid")

    goalSettings: SDUpdateAdGroupGoalSettings | None = Field(default=None)


__all__ = [
    "SDAdGroupAdGroupIdFilter",
    "SDAdGroupAdProductFilter",
    "SDAdGroupCampaignIdFilter",
    "SDAdGroupCreate",
    "SDAdGroupNameFilter",
    "SDAdGroupNameFilterType",
    "SDAdGroupStateFilter",
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
    "SDErrorCode",
    "SDKPI",
    "SDMarketplace",
    "SDMarketplaceScope",
    "SDQueryAdGroupRequest",
    "SDState",
    "SDUpdateAdGroupBid",
    "SDUpdateAdGroupGoalSettings",
    "SDUpdateAdGroupRequest",
    "SDUpdateOptimization",
    "SDUpdateState",
]
