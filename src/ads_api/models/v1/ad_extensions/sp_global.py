"""Auto-generated models for AdExtensions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.sp_global import (
    SPGlobalAdProduct,
    SPGlobalCreateState,
    SPGlobalError,
    SPGlobalErrorCode,
    SPGlobalErrorMarketplace,
    SPGlobalErrorsIndex,
    SPGlobalMarketplaceScope,
    SPGlobalState,
    SPGlobalUpdateState,
)


class SPGlobalAdExtensionStatus(StrEnum):
    """
    Ad Extension Status.
    """

    OPTED_OUT = "OPTED_OUT"  # If the advertiser has opted out of this Ad Extension.


class SPGlobalAdExtensionType(StrEnum):
    """
    Ad Extension Type.
    """

    PROMPTS = "PROMPTS"  # Enables Prompt based Ad Extension.


class SPGlobalMarketplace(StrEnum):
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


class SPGlobalAdExtension(LenientModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    adExtensionSettings: SPGlobalAdExtensionSettings
    adExtensionStatus: Annotated[SPGlobalAdExtensionStatus | str, lenient_enum(SPGlobalAdExtensionStatus)] | None = (
        Field(default=None)
    )
    adExtensionType: Annotated[SPGlobalAdExtensionType | str, lenient_enum(SPGlobalAdExtensionType)]
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: Annotated[SPGlobalAdProduct | str, lenient_enum(SPGlobalAdProduct)]
    creationDateTime: datetime = Field(description="The date time the ad_extension was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the ad_extension was last updated.")
    marketplaceScope: Annotated[SPGlobalMarketplaceScope | str, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)]


class SPGlobalAdExtensionAdExtensionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdExtensionAdExtensionStatusFilter(StrictModel):
    include: list[Annotated[SPGlobalAdExtensionStatus | str, lenient_enum(SPGlobalAdExtensionStatus)]] = Field(
        min_length=1, max_length=1
    )


class SPGlobalAdExtensionAdExtensionTypeFilter(StrictModel):
    include: list[Annotated[SPGlobalAdExtensionType | str, lenient_enum(SPGlobalAdExtensionType)]] = Field(
        min_length=1, max_length=1
    )


class SPGlobalAdExtensionAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdExtensionAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdExtensionAdProductFilter(StrictModel):
    include: list[Annotated[SPGlobalAdProduct | str, lenient_enum(SPGlobalAdProduct)]] = Field(
        min_length=1, max_length=1
    )


class SPGlobalAdExtensionCreate(StrictModel):
    adExtensionSettings: SPGlobalCreateAdExtensionSettings
    adExtensionStatus: Annotated[SPGlobalAdExtensionStatus | str, lenient_enum(SPGlobalAdExtensionStatus)] | None = (
        Field(default=None)
    )
    adExtensionType: Annotated[SPGlobalAdExtensionType | str, lenient_enum(SPGlobalAdExtensionType)]
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: Annotated[SPGlobalAdProduct | str, lenient_enum(SPGlobalAdProduct)]
    marketplaceScope: Annotated[SPGlobalMarketplaceScope | str, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: Annotated[SPGlobalCreateState | str, lenient_enum(SPGlobalCreateState)]


class SPGlobalAdExtensionMultiStatusResponseWithPartialErrors(LenientModel):
    error: list[SPGlobalErrorsIndex] | None = Field(default=None, min_length=0, max_length=50)
    partialSuccess: list[SPGlobalAdExtensionPartialIndex] | None = Field(default=None, min_length=0, max_length=50)
    success: list[SPGlobalAdExtensionMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=50)


class SPGlobalAdExtensionMultiStatusSuccess(LenientModel):
    adExtension: SPGlobalAdExtension
    index: int = Field(ge=0, le=49)


class SPGlobalAdExtensionPartialIndex(LenientModel):
    adExtension: SPGlobalAdExtension
    errors: list[SPGlobalError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=49)


class SPGlobalAdExtensionSettings(LenientModel):
    promptExtension: SPGlobalPromptExtension


class SPGlobalAdExtensionStateFilter(StrictModel):
    include: list[Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)]] = Field(min_length=1, max_length=3)


class SPGlobalAdExtensionSuccessResponse(LenientModel):
    adExtensions: list[SPGlobalAdExtension] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPGlobalAdExtensionUpdate(StrictModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    marketplaces: list[Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]] | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: Annotated[SPGlobalUpdateState | str, lenient_enum(SPGlobalUpdateState)] | None = Field(default=None)


class SPGlobalCreateAdExtensionRequest(StrictModel):
    adExtensions: list[SPGlobalAdExtensionCreate] = Field(min_length=1, max_length=50)


class SPGlobalCreateAdExtensionSettings(StrictModel):
    promptExtension: SPGlobalCreatePromptExtension


class SPGlobalCreatePromptExtension(StrictModel):
    """Prompts Ad Extension"""

    promptText: str = Field(description="The prompt text rendered in the ads")


class SPGlobalPromptExtension(LenientModel):
    """Prompts Ad Extension"""

    promptText: str = Field(description="The prompt text rendered in the ads")


class SPGlobalQueryAdExtensionRequest(StrictModel):
    adExtensionIdFilter: SPGlobalAdExtensionAdExtensionIdFilter | None = Field(default=None)
    adExtensionStatusFilter: SPGlobalAdExtensionAdExtensionStatusFilter | None = Field(default=None)
    adExtensionTypeFilter: SPGlobalAdExtensionAdExtensionTypeFilter | None = Field(default=None)
    adGroupIdFilter: SPGlobalAdExtensionAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SPGlobalAdExtensionAdIdFilter | None = Field(default=None)
    adProductFilter: SPGlobalAdExtensionAdProductFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: SPGlobalAdExtensionStateFilter | None = Field(default=None)


class SPGlobalUpdateAdExtensionRequest(StrictModel):
    adExtensions: list[SPGlobalAdExtensionUpdate] = Field(min_length=1, max_length=50)


__all__ = [
    "SPGlobalAdExtension",
    "SPGlobalAdExtensionAdExtensionIdFilter",
    "SPGlobalAdExtensionAdExtensionStatusFilter",
    "SPGlobalAdExtensionAdExtensionTypeFilter",
    "SPGlobalAdExtensionAdGroupIdFilter",
    "SPGlobalAdExtensionAdIdFilter",
    "SPGlobalAdExtensionAdProductFilter",
    "SPGlobalAdExtensionCreate",
    "SPGlobalAdExtensionMultiStatusResponseWithPartialErrors",
    "SPGlobalAdExtensionMultiStatusSuccess",
    "SPGlobalAdExtensionPartialIndex",
    "SPGlobalAdExtensionSettings",
    "SPGlobalAdExtensionStateFilter",
    "SPGlobalAdExtensionStatus",
    "SPGlobalAdExtensionSuccessResponse",
    "SPGlobalAdExtensionType",
    "SPGlobalAdExtensionUpdate",
    "SPGlobalAdProduct",
    "SPGlobalCreateAdExtensionRequest",
    "SPGlobalCreateAdExtensionSettings",
    "SPGlobalCreatePromptExtension",
    "SPGlobalCreateState",
    "SPGlobalError",
    "SPGlobalErrorCode",
    "SPGlobalErrorMarketplace",
    "SPGlobalErrorsIndex",
    "SPGlobalMarketplace",
    "SPGlobalMarketplaceScope",
    "SPGlobalPromptExtension",
    "SPGlobalQueryAdExtensionRequest",
    "SPGlobalState",
    "SPGlobalUpdateAdExtensionRequest",
    "SPGlobalUpdateState",
]
