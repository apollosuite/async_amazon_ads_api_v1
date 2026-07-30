"""Auto-generated models for AdGroups from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .campaigns import (
    SPAdProduct,
    SPCreateState,
    SPCreateTag,
    SPCurrencyCode,
    SPMarketplace,
    SPMarketplaceScope,
    SPState,
    SPStatus,
    SPTag,
    SPUpdateState,
)


class SPAdGroupNameFilterType(StrEnum):
    """
    **AdGroupNameFilterType Enum:**
    | AdGroupNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SPAdGroup(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroupId: str | None = Field(default=None, description="The unique identifier of the ad group.")
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)] | None = Field(default=None)
    adSettings: SPAdSettings | None = Field(default=None)
    bid: SPAdGroupBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None, description="The unique identifier of the campaign the ad group belongs to."
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the ad group was created.")
    globalAdGroupId: str | None = Field(
        default=None, description="The global adGroup identifier that manages this marketplace adGroup."
    )
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the ad group was last updated."
    )
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)] | None = Field(default=None)
    marketplaces: list[Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: Annotated[SPState | str, lenient_enum(SPState)] | None = Field(default=None)
    status: SPStatus | None = Field(default=None)
    tags: list[SPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPAdGroupAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=1000)


class SPAdGroupAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_PRODUCTS` | Sponsored Products ad product. |
""",
    )


class SPAdGroupBid(BaseModel):
    model_config = ConfigDict(extra="allow")

    currencyCode: Annotated[SPCurrencyCode | str, lenient_enum(SPCurrencyCode)] | None = Field(default=None)
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SPAdGroupCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPAdGroupCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    adSettings: SPCreateAdSettings | None = Field(default=None)
    bid: SPCreateAdGroupBid
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    name: str = Field(description="The name of the ad group.")
    state: Annotated[SPCreateState | str, lenient_enum(SPCreateState)]
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPAdGroupMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPAdGroupMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroup: SPAdGroup | None = Field(default=None)
    index: int | None = Field(default=None, ge=0, le=999)


class SPAdGroupNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SPAdGroupNameFilterType | str, lenient_enum(SPAdGroupNameFilterType)]


class SPAdGroupStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPState | str, lenient_enum(SPState)]] = Field(
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


class SPAdGroupSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroups: list[SPAdGroup] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPAdGroupUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adSettings: SPUpdateAdSettings | None = Field(default=None)
    bid: SPUpdateAdGroupBid | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: Annotated[SPUpdateState | str, lenient_enum(SPUpdateState)] | None = Field(default=None)
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPAdSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


class SPCreateAdGroupBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    defaultBid: float = Field(
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction."
    )


class SPCreateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SPAdGroupCreate] = Field(min_length=1, max_length=1000)


class SPCreateAdSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


class SPDeleteAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIds: list[str] = Field(min_length=1, max_length=1000)


class SPQueryAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SPAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SPAdGroupAdProductFilter
    campaignIdFilter: SPAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nameFilter: SPAdGroupNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SPAdGroupStateFilter | None = Field(default=None)


class SPUpdateAdGroupBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SPUpdateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SPAdGroupUpdate] = Field(min_length=1, max_length=1000)


class SPUpdateAdSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


__all__ = [
    "SPAdGroupNameFilterType",
    "SPAdGroup",
    "SPAdGroupAdGroupIdFilter",
    "SPAdGroupAdProductFilter",
    "SPAdGroupBid",
    "SPAdGroupCampaignIdFilter",
    "SPAdGroupCreate",
    "SPAdGroupMultiStatusResponse",
    "SPAdGroupMultiStatusSuccess",
    "SPAdGroupNameFilter",
    "SPAdGroupStateFilter",
    "SPAdGroupSuccessResponse",
    "SPAdGroupUpdate",
    "SPAdSettings",
    "SPCreateAdGroupBid",
    "SPCreateAdGroupRequest",
    "SPCreateAdSettings",
    "SPDeleteAdGroupRequest",
    "SPQueryAdGroupRequest",
    "SPUpdateAdGroupBid",
    "SPUpdateAdGroupRequest",
    "SPUpdateAdSettings",
]
