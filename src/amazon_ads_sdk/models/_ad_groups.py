"""ad_group models."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import (
        SPAdProduct,
        SPCreateState,
        SPCurrencyCode,
        SPMarketplace,
        SPMarketplaceScope,
        SPState,
        SPUpdateState,
    )
    from ._shared import SPCreateTag, SPStatus, SPTag


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


class SPAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    currencyCode: SPCurrencyCode
    defaultBid: float  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.


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


class SPAdGroupMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroup: SPAdGroup
    index: int


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


class SPUpdateAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.
    )
