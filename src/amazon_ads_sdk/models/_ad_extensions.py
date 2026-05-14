"""ad_extension models."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import (
        SPAdExtensionStatus,
        SPAdExtensionType,
        SPAdProduct,
        SPCreateState,
        SPMarketplace,
        SPMarketplaceScope,
        SPState,
        SPUpdateState,
        SPVideoType,
    )
    from ._errors import ErrorsIndex
    from ._shared import SPStatus


class SPAdExtension(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    adExtensionSettings: SPAdExtensionSettings
    adExtensionStatus: SPAdExtensionStatus | None = None
    adExtensionType: SPAdExtensionType
    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the ad_extension.
    )
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: SPAdProduct
    creationDateTime: datetime  # The date time the ad_extension was created.
    lastUpdatedDateTime: datetime  # The date time the ad_extension was last updated.
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[
        SPMarketplace
    ]  # The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad
    state: SPState
    status: SPStatus | None = None


class SPAdExtensionAdExtensionIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdExtensionStatusFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdExtensionStatus
    ]  # AdExtensionStatus Description `OPTED_OUT` If the advertiser has opted out of this Ad Extension.


class SPAdExtensionAdExtensionTypeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdExtensionType
    ]  # AdExtensionType Description `PROMPTS` Enables Prompt based Ad Extension. `VIDEO` Enables Video based Ad Extension.


class SPAdExtensionAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdProduct
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdExtensionCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionSettings: SPCreateAdExtensionSettings
    adExtensionStatus: SPAdExtensionStatus | None = None
    adExtensionType: SPAdExtensionType
    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the ad_extension.
    )
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: SPAdProduct
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[
        SPMarketplace
    ]  # The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad
    state: SPCreateState


class SPAdExtensionMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPAdExtensionMultiStatusSuccess] | None = None


class SPAdExtensionMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtension: SPAdExtension
    index: int


class SPAdExtensionSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    promptExtension: SPPromptExtension | None = None
    videoExtension: SPVideoExtension | None = None


class SPAdExtensionStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPAdExtensionSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtension] | None = None
    nextToken: str | None = None


class SPAdExtensionUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    state: SPUpdateState | None = None


class SPCreateAdExtensionRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtensionCreate] | None = None


class SPCreateAdExtensionSettings(BaseModel):
    """"""

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
    """"""

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
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtensionUpdate] | None = None


class SPVideoExtension(BaseModel):
    """Video Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    renderedAssetId: str | None = None  # The video asset ID rendered in the ad.
    renderedCoverImageUrl: str | None = (
        None  # The image displayed over the video player before the video is played.
    )
    videoType: SPVideoType
