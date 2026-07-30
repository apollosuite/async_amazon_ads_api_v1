"""Auto-generated models for AdGroups from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorCode, ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .campaigns import (
    SBAdProduct,
    SBCreateState,
    SBCreateTag,
    SBDeliveryReason,
    SBDeliveryStatus,
    SBMarketplace,
    SBMarketplaceScope,
    SBState,
    SBStatus,
    SBTag,
    SBUpdateState,
)


class SBAdGroupNameFilterType(StrEnum):
    """
    **AdGroupNameFilterType Enum:**
    | AdGroupNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBAdGroup(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroupId: str | None = Field(default=None, description="The unique identifier of the ad group.")
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)] | None = Field(default=None)
    campaignId: str | None = Field(
        default=None, description="The unique identifier of the campaign the ad group belongs to."
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the ad group was created.")
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the ad group was last updated."
    )
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)] | None = Field(default=None)
    marketplaces: list[Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: Annotated[SBState | str, lenient_enum(SBState)] | None = Field(default=None)
    status: SBStatus | None = Field(default=None)
    tags: list[SBTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SBAdGroupAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SBAdGroupAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_BRANDS` | Sponsored Brands ad product. |
""",
    )


class SBAdGroupCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SBAdGroupCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    name: str = Field(description="The name of the ad group.")
    state: Annotated[SBCreateState | str, lenient_enum(SBCreateState)]
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SBAdGroupMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBAdGroupMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroup: SBAdGroup | None = Field(default=None)
    index: int | None = Field(default=None, ge=0, le=9)


class SBAdGroupNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SBAdGroupNameFilterType | str, lenient_enum(SBAdGroupNameFilterType)]


class SBAdGroupStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBState | str, lenient_enum(SBState)]] = Field(
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


class SBAdGroupSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroups: list[SBAdGroup] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SBAdGroupUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str = Field(description="The unique identifier of the ad group.")
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: Annotated[SBUpdateState | str, lenient_enum(SBUpdateState)] | None = Field(default=None)
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SBCreateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SBAdGroupCreate] = Field(min_length=1, max_length=10)


class SBDeleteAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIds: list[str] = Field(min_length=1, max_length=10)


class SBQueryAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SBAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SBAdGroupAdProductFilter
    campaignIdFilter: SBAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SBAdGroupNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SBAdGroupStateFilter | None = Field(default=None)


class SBUpdateAdGroupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroups: list[SBAdGroupUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "ErrorCode",
    "SBAdGroupAdGroupIdFilter",
    "SBAdGroupAdProductFilter",
    "SBAdGroupCampaignIdFilter",
    "SBAdGroupCreate",
    "SBAdGroupNameFilter",
    "SBAdGroupNameFilterType",
    "SBAdGroupStateFilter",
    "SBAdGroupUpdate",
    "SBAdProduct",
    "SBCreateAdGroupRequest",
    "SBCreateState",
    "SBCreateTag",
    "SBDeleteAdGroupRequest",
    "SBDeliveryReason",
    "SBDeliveryStatus",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBQueryAdGroupRequest",
    "SBState",
    "SBUpdateAdGroupRequest",
    "SBUpdateState",
]
