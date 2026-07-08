"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import SBAdProduct, SBCreateState, SBMarketplace, SBMarketplaceScope, SBState, SBUpdateState
from .shared import SBCreateTag, SBStatus, SBTag


class SBAdGroup(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    creationDateTime: datetime  # The date time that the ad group was created.
    lastUpdatedDateTime: datetime  # The date time that the ad group was last updated.
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[
        Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]
    ]  # The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign
    name: str  # The name of the ad group.
    state: Annotated[SBState | str, lenient_enum(SBState)]
    status: SBStatus | None = None
    tags: list[SBTag] | None = None  # Open ended labels with a key value pair applied to the ad group


class SBAdGroupAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdGroupAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    ]  # **AdProduct Enum:** AdProduct Description `SPONSORED_BRANDS` Sponsored Brands ad product.


class SBAdGroupCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdGroupCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    name: str  # The name of the ad group.
    state: Annotated[SBCreateState | str, lenient_enum(SBCreateState)]
    tags: list[SBCreateTag] | None = None  # Open ended labels with a key value pair applied to the ad group


class SBAdGroupMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBAdGroupMultiStatusSuccess] | None = None


class SBAdGroupMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroup: SBAdGroup
    index: int


class SBAdGroupNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: Annotated[SBAdGroupNameFilterType | str, lenient_enum(SBAdGroupNameFilterType)]


class SBAdGroupNameFilterType(StrEnum):
    """**AdGroupNameFilterType Enum:**
    | AdGroupNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBAdGroupStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBState | str, lenient_enum(SBState)]
    ]  # **State Enum:** State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SBAdGroupSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SBAdGroup] | None = None
    nextToken: str | None = None


class SBAdGroupUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    name: str | None = None  # The name of the ad group.
    state: Annotated[SBUpdateState | str, lenient_enum(SBUpdateState)] | None = None
    tags: list[SBCreateTag] | None = None  # Open ended labels with a key value pair applied to the ad group


class SBCreateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SBAdGroupCreate]


class SBDeleteAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIds: list[str]


class SBQueryAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SBAdGroupAdGroupIdFilter | None = None
    adProductFilter: SBAdGroupAdProductFilter
    campaignIdFilter: SBAdGroupCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SBAdGroupNameFilter | None = None
    nextToken: str | None = None
    stateFilter: SBAdGroupStateFilter | None = None


class SBUpdateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SBAdGroupUpdate]


__all__ = [
    "SBAdGroup",
    "SBAdGroupAdGroupIdFilter",
    "SBAdGroupAdProductFilter",
    "SBAdGroupCampaignIdFilter",
    "SBAdGroupCreate",
    "SBAdGroupMultiStatusResponse",
    "SBAdGroupMultiStatusSuccess",
    "SBAdGroupNameFilter",
    "SBAdGroupNameFilterType",
    "SBAdGroupStateFilter",
    "SBAdGroupSuccessResponse",
    "SBAdGroupUpdate",
    "SBCreateAdGroupRequest",
    "SBDeleteAdGroupRequest",
    "SBQueryAdGroupRequest",
    "SBUpdateAdGroupRequest",
]
