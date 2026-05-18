"""Auto-generated Pydantic models for sp from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from amazon_ads_sdk.models.base import SafeStrEnum

if TYPE_CHECKING:
    from amazon_ads_sdk.errors import ErrorsIndex
    from .enums import (
        SPAdProduct,
        SPCreateState,
        SPCurrencyCode,
        SPMarketplace,
        SPMarketplaceScope,
        SPState,
        SPUpdateState,
    )
    from .shared import SPCreateTag, SPStatus, SPTag


class SPAdGroup(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroupId: str  # The unique identifier of the ad group.
    adProduct: SPAdProduct
    adSettings: SPAdSettings | None = None
    bid: SPAdGroupBid
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    creationDateTime: datetime  # The date time that the ad group was created.
    globalAdGroupId: str | None = (
        None  # The global adGroup identifier that manages this marketplace adGroup.
    )
    lastUpdatedDateTime: datetime  # The date time that the ad group was last updated.
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[
        SPMarketplace
    ]  # The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign
    name: str  # The name of the ad group.
    state: SPState
    status: SPStatus | None = None
    tags: list[SPTag] | None = (
        None  # Open ended labels with a key value pair applied to the ad group
    )


class SPAdGroupAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]


class SPAdGroupAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[
        SPAdProduct
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    currencyCode: SPCurrencyCode
    defaultBid: float  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.


class SPAdGroupCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]


class SPAdGroupCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adProduct: SPAdProduct
    adSettings: SPCreateAdSettings | None = None
    bid: SPCreateAdGroupBid
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    name: str  # The name of the ad group.
    state: SPCreateState
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the ad group
    )


class SPAdGroupMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = None
    success: list[SPAdGroupMultiStatusSuccess] | None = None


class SPAdGroupMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroup: SPAdGroup
    index: int


class SPAdGroupNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]
    queryTermMatchType: SPAdGroupNameFilterType


class SPAdGroupNameFilterType(SafeStrEnum):
    """| AdGroupNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SPAdGroupStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPAdGroupSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroups: list[SPAdGroup] | None = None
    nextToken: str | None = None


class SPAdGroupUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroupId: str  # The unique identifier of the ad group.
    adSettings: SPUpdateAdSettings | None = None
    bid: SPUpdateAdGroupBid | None = None
    name: str | None = None  # The name of the ad group.
    state: SPUpdateState | None = None
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the ad group
    )


class SPAdSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    productAttributeSetRefinementConfigurationId: str | None = (
        None  # Identifier for the product attribute configuration set associated with this ad group.
    )


class SPCreateAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    defaultBid: float  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.


class SPCreateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroups: list[SPAdGroupCreate] | None = None


class SPCreateAdSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    productAttributeSetRefinementConfigurationId: str | None = (
        None  # Identifier for the product attribute configuration set associated with this ad group.
    )


class SPDeleteAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroupIds: list[str] | None = None


class SPQueryAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroupIdFilter: SPAdGroupAdGroupIdFilter | None = None
    adProductFilter: SPAdGroupAdProductFilter
    campaignIdFilter: SPAdGroupCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SPAdGroupNameFilter | None = None
    nextToken: str | None = None
    stateFilter: SPAdGroupStateFilter | None = None


class SPUpdateAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.
    )


class SPUpdateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adGroups: list[SPAdGroupUpdate] | None = None


class SPUpdateAdSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    productAttributeSetRefinementConfigurationId: str | None = (
        None  # Identifier for the product attribute configuration set associated with this ad group.
    )
