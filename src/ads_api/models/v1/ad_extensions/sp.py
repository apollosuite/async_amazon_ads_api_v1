"""Auto-generated models for AdExtensions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.sp import (
    SPAdProduct,
    SPCreateState,
    SPDeliveryReason,
    SPDeliveryStatus,
    SPError,
    SPErrorCode,
    SPErrorsIndex,
    SPMarketplaceScope,
    SPState,
    SPStatus,
    SPUpdateState,
)


class SPAdExtensionStatus(StrEnum):
    """
    Ad Extension Status.
    """

    OPTED_OUT = "OPTED_OUT"  # If the advertiser has opted out of this Ad Extension.


class SPAdExtensionType(StrEnum):
    """
    Ad Extension Type.
    """

    PROMPTS = "PROMPTS"  # Enables Prompt based Ad Extension.
    VIDEO = "VIDEO"  # Enables Video based Ad Extension.


class SPMarketplace(StrEnum):
    """
    A list of country codes representing Amazon marketplaces
    """

    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IE = "IE"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"
    ZA = "ZA"


class SPVideoType(StrEnum):
    """
    Video Type: Video type of the asset added in the ad extension and its rendering form.
    """

    SPOTLIGHT = "SPOTLIGHT"  # SPOTLIGHT Video Asset.


class SPAdExtension(LenientModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    adExtensionSettings: SPAdExtensionSettings
    adExtensionStatus: Annotated[SPAdExtensionStatus | str, lenient_enum(SPAdExtensionStatus)] | None = Field(
        default=None
    )
    adExtensionType: Annotated[SPAdExtensionType | str, lenient_enum(SPAdExtensionType)]
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    creationDateTime: datetime = Field(description="The date time the ad_extension was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the ad_extension was last updated.")
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: Annotated[SPState | str, lenient_enum(SPState)]
    status: SPStatus | None = Field(default=None)


class SPAdExtensionAdExtensionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdExtensionAdExtensionStatusFilter(StrictModel):
    include: list[Annotated[SPAdExtensionStatus, lenient_enum(SPAdExtensionStatus)]] = Field(min_length=1, max_length=1)


class SPAdExtensionAdExtensionTypeFilter(StrictModel):
    include: list[Annotated[SPAdExtensionType, lenient_enum(SPAdExtensionType)]] = Field(min_length=1, max_length=1)


class SPAdExtensionAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdExtensionAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdExtensionAdProductFilter(StrictModel):
    include: list[Annotated[SPAdProduct, lenient_enum(SPAdProduct)]] = Field(min_length=1, max_length=1)


class SPAdExtensionCreate(StrictModel):
    adExtensionSettings: SPCreateAdExtensionSettings
    adExtensionStatus: Annotated[SPAdExtensionStatus, lenient_enum(SPAdExtensionStatus)] | None = Field(default=None)
    adExtensionType: Annotated[SPAdExtensionType, lenient_enum(SPAdExtensionType)]
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: Annotated[SPAdProduct, lenient_enum(SPAdProduct)]
    marketplaceScope: Annotated[SPMarketplaceScope, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[Annotated[SPMarketplace, lenient_enum(SPMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: Annotated[SPCreateState, lenient_enum(SPCreateState)]


class SPAdExtensionMultiStatusResponse(LenientModel):
    error: list[SPErrorsIndex] | None = Field(default=None, min_length=0, max_length=50)
    success: list[SPAdExtensionMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=50)


class SPAdExtensionMultiStatusSuccess(LenientModel):
    adExtension: SPAdExtension
    index: int = Field(ge=0, le=49)


class SPAdExtensionSettingsPromptExtension(LenientModel):
    promptExtension: SPPromptExtension


class SPAdExtensionSettingsVideoExtension(LenientModel):
    videoExtension: SPVideoExtension


type SPAdExtensionSettings = SPAdExtensionSettingsPromptExtension | SPAdExtensionSettingsVideoExtension


class SPAdExtensionStateFilter(StrictModel):
    include: list[Annotated[SPState, lenient_enum(SPState)]] = Field(min_length=1, max_length=3)


class SPAdExtensionSuccessResponse(LenientModel):
    adExtensions: list[SPAdExtension] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPAdExtensionUpdate(StrictModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    state: Annotated[SPUpdateState, lenient_enum(SPUpdateState)] | None = Field(default=None)


class SPCreateAdExtensionRequest(StrictModel):
    adExtensions: list[SPAdExtensionCreate] = Field(min_length=1, max_length=50)


class SPCreateAdExtensionSettingsPromptExtension(StrictModel):
    promptExtension: SPCreatePromptExtension


class SPCreateAdExtensionSettingsVideoExtension(StrictModel):
    videoExtension: SPCreateVideoExtension


type SPCreateAdExtensionSettings = SPCreateAdExtensionSettingsPromptExtension | SPCreateAdExtensionSettingsVideoExtension


class SPCreatePromptExtension(StrictModel):
    """Prompts Ad Extension"""

    promptText: str = Field(description="The prompt text rendered in the ads")


class SPCreateVideoExtension(StrictModel):
    """Video Ad Extension"""

    pass


class SPPromptExtension(LenientModel):
    """Prompts Ad Extension"""

    promptText: str = Field(description="The prompt text rendered in the ads")


class SPQueryAdExtensionRequest(StrictModel):
    adExtensionIdFilter: SPAdExtensionAdExtensionIdFilter | None = Field(default=None)
    adExtensionStatusFilter: SPAdExtensionAdExtensionStatusFilter | None = Field(default=None)
    adExtensionTypeFilter: SPAdExtensionAdExtensionTypeFilter | None = Field(default=None)
    adGroupIdFilter: SPAdExtensionAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SPAdExtensionAdIdFilter | None = Field(default=None)
    adProductFilter: SPAdExtensionAdProductFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: SPAdExtensionStateFilter | None = Field(default=None)


class SPUpdateAdExtensionRequest(StrictModel):
    adExtensions: list[SPAdExtensionUpdate] = Field(min_length=1, max_length=50)


class SPVideoExtension(LenientModel):
    """Video Ad Extension"""

    renderedAssetId: str | None = Field(default=None, description="The video asset ID rendered in the ad.")
    renderedCoverImageUrl: str | None = Field(
        default=None, description="The image displayed over the video player before the video is played."
    )
    videoType: Annotated[SPVideoType | str, lenient_enum(SPVideoType)]


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
    "SPAdProduct",
    "SPCreateAdExtensionRequest",
    "SPCreateAdExtensionSettings",
    "SPCreatePromptExtension",
    "SPCreateState",
    "SPCreateVideoExtension",
    "SPDeliveryReason",
    "SPDeliveryStatus",
    "SPError",
    "SPErrorCode",
    "SPErrorsIndex",
    "SPMarketplace",
    "SPMarketplaceScope",
    "SPPromptExtension",
    "SPQueryAdExtensionRequest",
    "SPState",
    "SPStatus",
    "SPUpdateAdExtensionRequest",
    "SPUpdateState",
    "SPVideoExtension",
    "SPVideoType",
]
