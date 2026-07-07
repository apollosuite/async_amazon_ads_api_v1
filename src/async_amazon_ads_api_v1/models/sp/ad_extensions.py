"""Auto-generated Pydantic models for sp from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

if TYPE_CHECKING:
    from async_amazon_ads_api_v1.errors import ErrorsIndex

    from .enums import SPAdProduct, SPCreateState, SPMarketplace, SPMarketplaceScope, SPState, SPUpdateState
    from .shared import SPStatus
del TYPE_CHECKING


class SPAdExtension(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    adExtensionSettings: SPAdExtensionSettings
    adExtensionStatus: Annotated[SPAdExtensionStatus | str, lenient_enum(SPAdExtensionStatus)] | None = None
    adExtensionType: Annotated[SPAdExtensionType | str, lenient_enum(SPAdExtensionType)]
    adGroupId: str | None = None  # A unique identifier for the ad group associated with the ad_extension.
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    creationDateTime: datetime  # The date time the ad_extension was created.
    lastUpdatedDateTime: datetime  # The date time the ad_extension was last updated.
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[
        Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]
    ]  # The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad
    state: Annotated[SPState | str, lenient_enum(SPState)]
    status: SPStatus | None = None


class SPAdExtensionAdExtensionIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdExtensionStatusFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPAdExtensionStatus | str, lenient_enum(SPAdExtensionStatus)]
    ]  # **AdExtensionStatus Enum:** AdExtensionStatus Description `OPTED_OUT` If the advertiser has opted out of this Ad Extension.


class SPAdExtensionAdExtensionTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPAdExtensionType | str, lenient_enum(SPAdExtensionType)]
    ]  # **AdExtensionType Enum:** AdExtensionType Description `PROMPTS` Enables Prompt based Ad Extension. `VIDEO` Enables Video based Ad Extension.


class SPAdExtensionAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    ]  # **AdProduct Enum:** AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdExtensionCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionSettings: SPCreateAdExtensionSettings
    adExtensionStatus: Annotated[SPAdExtensionStatus | str, lenient_enum(SPAdExtensionStatus)] | None = None
    adExtensionType: Annotated[SPAdExtensionType | str, lenient_enum(SPAdExtensionType)]
    adGroupId: str | None = None  # A unique identifier for the ad group associated with the ad_extension.
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[
        Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]
    ]  # The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad
    state: Annotated[SPCreateState | str, lenient_enum(SPCreateState)]


class SPAdExtensionMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPAdExtensionMultiStatusSuccess] | None = None


class SPAdExtensionMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtension: SPAdExtension
    index: int


class SPAdExtensionSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    promptExtension: SPPromptExtension | None = None
    videoExtension: SPVideoExtension | None = None


class SPAdExtensionStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPState | str, lenient_enum(SPState)]
    ]  # **State Enum:** State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPAdExtensionStatus(StrEnum):
    """Ad Extension Status.
    **AdExtensionStatus Enum:**

    | AdExtensionStatus | Description |
    |------|------|
    | `OPTED_OUT` | If the advertiser has opted out of this Ad Extension. |
    """

    OPTED_OUT = "OPTED_OUT"


class SPAdExtensionSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtension] | None = None
    nextToken: str | None = None


class SPAdExtensionType(StrEnum):
    """Ad Extension Type.
    **AdExtensionType Enum:**

    | AdExtensionType | Description |
    |------|------|
    | `PROMPTS` | Enables Prompt based Ad Extension. |
    | `VIDEO` | Enables Video based Ad Extension. |
    """

    PROMPTS = "PROMPTS"
    VIDEO = "VIDEO"


class SPAdExtensionUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    state: Annotated[SPUpdateState | str, lenient_enum(SPUpdateState)] | None = None


class SPCreateAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtensionCreate]


class SPCreateAdExtensionSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    promptExtension: SPCreatePromptExtension | None = None
    videoExtension: SPCreateVideoExtension | None = None


class SPCreatePromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads


class SPCreateVideoExtension(BaseModel):
    """Video Ad Extension"""

    model_config = ConfigDict(extra="forbid")


class SPPromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads


class SPQueryAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionIdFilter: SPAdExtensionAdExtensionIdFilter | None = None
    adExtensionStatusFilter: SPAdExtensionAdExtensionStatusFilter | None = None
    adExtensionTypeFilter: SPAdExtensionAdExtensionTypeFilter | None = None
    adGroupIdFilter: SPAdExtensionAdGroupIdFilter | None = None
    adIdFilter: SPAdExtensionAdIdFilter | None = None
    adProductFilter: SPAdExtensionAdProductFilter | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: SPAdExtensionStateFilter | None = None


class SPUpdateAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtensionUpdate]


class SPVideoExtension(BaseModel):
    """Video Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    renderedAssetId: str | None = None  # The video asset ID rendered in the ad.
    renderedCoverImageUrl: str | None = None  # The image displayed over the video player before the video is played.
    videoType: Annotated[SPVideoType | str, lenient_enum(SPVideoType)]


class SPVideoType(StrEnum):
    """Video Type: Video type of the asset added in the ad extension and its rendering form.
    **VideoType Enum:**

    | VideoType | Description |
    |------|------|
    | `SPOTLIGHT` | SPOTLIGHT Video Asset. |
    """

    SPOTLIGHT = "SPOTLIGHT"


__all__ = [
    "SPAdExtension",
    "SPAdExtensionAdExtensionIdFilter",
    "SPAdExtensionAdExtensionStatusFilter",
    "SPAdExtensionAdExtensionTypeFilter",
    "SPAdExtensionAdGroupIdFilter",
    "SPAdExtensionAdIdFilter",
    "SPAdExtensionAdProductFilter",
    "SPAdExtensionCreate",
    "SPAdExtensionMultiStatusResponse",
    "SPAdExtensionMultiStatusSuccess",
    "SPAdExtensionSettings",
    "SPAdExtensionStateFilter",
    "SPAdExtensionStatus",
    "SPAdExtensionSuccessResponse",
    "SPAdExtensionType",
    "SPAdExtensionUpdate",
    "SPCreateAdExtensionRequest",
    "SPCreateAdExtensionSettings",
    "SPCreatePromptExtension",
    "SPCreateVideoExtension",
    "SPPromptExtension",
    "SPQueryAdExtensionRequest",
    "SPUpdateAdExtensionRequest",
    "SPVideoExtension",
    "SPVideoType",
]
