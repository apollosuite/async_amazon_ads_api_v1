"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from enum import StrEnum

if TYPE_CHECKING:
    from amazon_ads_sdk.errors import ErrorsIndex
    from .enums import (
        SBAdProduct,
        SBCreateState,
        SBMarketplace,
        SBMarketplaceScope,
        SBState,
        SBUpdateState,
    )


class SBAdExtension(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    adExtensionSettings: SBAdExtensionSettings
    adExtensionStatus: SBAdExtensionStatus | None = None
    adExtensionType: SBAdExtensionType
    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the ad_extension.
    )
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: SBAdProduct
    creationDateTime: datetime  # The date time the ad_extension was created.
    lastUpdatedDateTime: datetime  # The date time the ad_extension was last updated.
    marketplaceScope: SBMarketplaceScope
    marketplaces: list[
        SBMarketplace
    ]  # The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad
    state: SBState


class SBAdExtensionAdExtensionIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdExtensionAdExtensionStatusFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SBAdExtensionStatus
    ]  # AdExtensionStatus Description `OPTED_OUT` If the advertiser has opted out of this Ad Extension.


class SBAdExtensionAdExtensionTypeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SBAdExtensionType
    ]  # AdExtensionType Description `PROMPTS` Enables Prompt based Ad Extension.


class SBAdExtensionAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdExtensionAdIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdExtensionAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SBAdProduct
    ]  # AdProduct Description `SPONSORED_BRANDS` Sponsored Brands ad product.


class SBAdExtensionCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionSettings: SBCreateAdExtensionSettings
    adExtensionStatus: SBAdExtensionStatus | None = None
    adExtensionType: SBAdExtensionType
    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the ad_extension.
    )
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: SBAdProduct
    marketplaceScope: SBMarketplaceScope
    marketplaces: list[
        SBMarketplace
    ]  # The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad
    state: SBCreateState


class SBAdExtensionMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBAdExtensionMultiStatusSuccess] | None = None


class SBAdExtensionMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtension: SBAdExtension
    index: int


class SBAdExtensionSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    promptExtension: SBPromptExtension | None = None


class SBAdExtensionStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SBState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SBAdExtensionStatus(StrEnum):
    """Ad Extension Status.

    | AdExtensionStatus | Description |
    |------|------|
    | `OPTED_OUT` | If the advertiser has opted out of this Ad Extension. |
    """

    OPTED_OUT = "OPTED_OUT"


class SBAdExtensionSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SBAdExtension] | None = None
    nextToken: str | None = None


class SBAdExtensionType(StrEnum):
    """Ad Extension Type.

    | AdExtensionType | Description |
    |------|------|
    | `PROMPTS` | Enables Prompt based Ad Extension. |
    """

    PROMPTS = "PROMPTS"


class SBAdExtensionUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    state: SBUpdateState | None = None


class SBCreateAdExtensionRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SBAdExtensionCreate] | None = None


class SBCreateAdExtensionSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    promptExtension: SBCreatePromptExtension | None = None


class SBCreatePromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads


class SBPromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads


class SBQueryAdExtensionRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionIdFilter: SBAdExtensionAdExtensionIdFilter | None = None
    adExtensionStatusFilter: SBAdExtensionAdExtensionStatusFilter | None = None
    adExtensionTypeFilter: SBAdExtensionAdExtensionTypeFilter | None = None
    adGroupIdFilter: SBAdExtensionAdGroupIdFilter | None = None
    adIdFilter: SBAdExtensionAdIdFilter | None = None
    adProductFilter: SBAdExtensionAdProductFilter | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: SBAdExtensionStateFilter | None = None


class SBUpdateAdExtensionRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SBAdExtensionUpdate] | None = None
