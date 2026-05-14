"""ad_group models."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import (
        SPAdGroupNameFilterType,
        SPAdProduct,
        SPCreateState,
        SPCurrencyCode,
        SPMarketplace,
        SPMarketplaceScope,
        SPState,
        SPUpdateState,
    )
    from ._errors import ErrorsIndex
    from ._shared import SPCreateTag, SPStatus, SPTag


class SPAdAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdGroup(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    adProduct: SPAdProduct
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

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdGroupAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdProduct
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    currencyCode: SPCurrencyCode
    defaultBid: float  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.


class SPAdGroupCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdGroupCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProduct: SPAdProduct
    bid: SPCreateAdGroupBid
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    name: str  # The name of the ad group.
    state: SPCreateState
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the ad group
    )


class SPAdGroupMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPAdGroupMultiStatusSuccess] | None = None


class SPAdGroupMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroup: SPAdGroup
    index: int


class SPAdGroupNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: SPAdGroupNameFilterType


class SPAdGroupStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPAdGroupSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroups: list[SPAdGroup] | None = None
    nextToken: str | None = None


class SPAdGroupUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    bid: SPUpdateAdGroupBid | None = None
    name: str | None = None  # The name of the ad group.
    state: SPUpdateState | None = None
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the ad group
    )


class SPCreateAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    defaultBid: float  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.


class SPCreateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroups: list[SPAdGroupCreate] | None = None


class SPDeleteAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIds: list[str] | None = None


class SPQueryAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SPAdGroupAdGroupIdFilter | None = None
    adProductFilter: SPAdGroupAdProductFilter
    campaignIdFilter: SPAdGroupCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SPAdGroupNameFilter | None = None
    nextToken: str | None = None
    stateFilter: SPAdGroupStateFilter | None = None


class SPTargetAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPUpdateAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.
    )


class SPUpdateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroups: list[SPAdGroupUpdate] | None = None
