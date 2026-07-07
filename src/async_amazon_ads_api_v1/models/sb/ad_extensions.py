"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

if TYPE_CHECKING:
    from .enums import SBAdProduct, SBCreateState, SBMarketplace, SBMarketplaceScope, SBState, SBUpdateState
del TYPE_CHECKING


class SBAdExtension(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    adExtensionSettings: SBAdExtensionSettings
    adExtensionStatus: Annotated[SBAdExtensionStatus | str, lenient_enum(SBAdExtensionStatus)] | None = None
    adExtensionType: Annotated[SBAdExtensionType | str, lenient_enum(SBAdExtensionType)]
    adGroupId: str | None = None  # A unique identifier for the ad group associated with the ad_extension.
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    creationDateTime: datetime  # The date time the ad_extension was created.
    lastUpdatedDateTime: datetime  # The date time the ad_extension was last updated.
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[
        Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]
    ]  # The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad
    state: Annotated[SBState | str, lenient_enum(SBState)]


class SBAdExtensionAdExtensionIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdExtensionAdExtensionStatusFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBAdExtensionStatus | str, lenient_enum(SBAdExtensionStatus)]
    ]  # **AdExtensionStatus Enum:** AdExtensionStatus Description `OPTED_OUT` If the advertiser has opted out of this Ad Extension.


class SBAdExtensionAdExtensionTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBAdExtensionType | str, lenient_enum(SBAdExtensionType)]
    ]  # **AdExtensionType Enum:** AdExtensionType Description `PROMPTS` Enables Prompt based Ad Extension.


class SBAdExtensionAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdExtensionAdIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdExtensionAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    ]  # **AdProduct Enum:** AdProduct Description `SPONSORED_BRANDS` Sponsored Brands ad product.


class SBAdExtensionCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionSettings: SBCreateAdExtensionSettings
    adExtensionStatus: Annotated[SBAdExtensionStatus | str, lenient_enum(SBAdExtensionStatus)] | None = None
    adExtensionType: Annotated[SBAdExtensionType | str, lenient_enum(SBAdExtensionType)]
    adGroupId: str | None = None  # A unique identifier for the ad group associated with the ad_extension.
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[
        Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]
    ]  # The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad
    state: Annotated[SBCreateState | str, lenient_enum(SBCreateState)]


class SBAdExtensionMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBAdExtensionMultiStatusSuccess] | None = None


class SBAdExtensionMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtension: SBAdExtension
    index: int


class SBAdExtensionSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    promptExtension: SBPromptExtension | None = None


class SBAdExtensionStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBState | str, lenient_enum(SBState)]
    ]  # **State Enum:** State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SBAdExtensionStatus(StrEnum):
    """Ad Extension Status.
    **AdExtensionStatus Enum:**

    | AdExtensionStatus | Description |
    |------|------|
    | `OPTED_OUT` | If the advertiser has opted out of this Ad Extension. |
    """

    OPTED_OUT = "OPTED_OUT"


class SBAdExtensionSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SBAdExtension] | None = None
    nextToken: str | None = None


class SBAdExtensionType(StrEnum):
    """Ad Extension Type.
    **AdExtensionType Enum:**

    | AdExtensionType | Description |
    |------|------|
    | `PROMPTS` | Enables Prompt based Ad Extension. |
    """

    PROMPTS = "PROMPTS"


class SBAdExtensionUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    state: Annotated[SBUpdateState | str, lenient_enum(SBUpdateState)] | None = None


class SBCreateAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SBAdExtensionCreate]


class SBCreateAdExtensionSettings(BaseModel):
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
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SBAdExtensionUpdate]


__all__ = [
    "SBAdExtension",
    "SBAdExtensionAdExtensionIdFilter",
    "SBAdExtensionAdExtensionStatusFilter",
    "SBAdExtensionAdExtensionTypeFilter",
    "SBAdExtensionAdGroupIdFilter",
    "SBAdExtensionAdIdFilter",
    "SBAdExtensionAdProductFilter",
    "SBAdExtensionCreate",
    "SBAdExtensionMultiStatusResponse",
    "SBAdExtensionMultiStatusSuccess",
    "SBAdExtensionSettings",
    "SBAdExtensionStateFilter",
    "SBAdExtensionStatus",
    "SBAdExtensionSuccessResponse",
    "SBAdExtensionType",
    "SBAdExtensionUpdate",
    "SBCreateAdExtensionRequest",
    "SBCreateAdExtensionSettings",
    "SBCreatePromptExtension",
    "SBPromptExtension",
    "SBQueryAdExtensionRequest",
    "SBUpdateAdExtensionRequest",
]
