"""ad_group models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class SPAdGroup(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    adProduct: dict[str, Any]
    bid: dict[str, Any]
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    creationDateTime: datetime  # The date time that the ad group was created.
    globalAdGroupId: str | None = (
        None  # The global adGroup identifier that manages this marketplace adGroup.
    )
    lastUpdatedDateTime: datetime  # The date time that the ad group was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[
        dict[str, Any]
    ]  # The list of country codes representing amazon marketplaces in which the global a
    name: str  # The name of the ad group.
    state: dict[str, Any]
    status: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = (
        None  # Open ended labels with a key value pair applied to the ad group
    )


class SPAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    currencyCode: dict[str, Any]
    defaultBid: (
        float  # The default maximum bid for ads and targets in the ad group. This is used in spo
    )


class SPAdGroupCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProduct: dict[str, Any]
    bid: dict[str, Any]
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    name: str  # The name of the ad group.
    state: dict[str, Any]
    tags: list[dict[str, Any]] | None = (
        None  # Open ended labels with a key value pair applied to the ad group
    )


class SPAdGroupMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroup: dict[str, Any]
    index: int


class SPAdGroupUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    bid: dict[str, Any] | None = None
    name: str | None = None  # The name of the ad group.
    state: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = (
        None  # Open ended labels with a key value pair applied to the ad group
    )


class SPCreateAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    defaultBid: (
        float  # The default maximum bid for ads and targets in the ad group. This is used in spo
    )


class SPUpdateAdGroupBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    defaultBid: float | None = (
        None  # The default maximum bid for ads and targets in the ad group. This is used in spo
    )
