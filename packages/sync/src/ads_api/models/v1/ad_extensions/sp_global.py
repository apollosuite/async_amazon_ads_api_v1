"""Auto-generated models for AdExtensions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sp_global import (
    SPGlobalAdProduct,
    SPGlobalCreateState,
    SPGlobalError,
    SPGlobalErrorCode,
    SPGlobalErrorMarketplace,
    SPGlobalErrorsIndex,
    SPGlobalMarketplace,
    SPGlobalMarketplaceScope,
    SPGlobalState,
    SPGlobalUpdateState,
)

type SPGlobalAdExtensionStatus = Literal["OPTED_OUT"]
"""
Ad Extension Status.

Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
"""


type SPGlobalAdExtensionType = Literal["PROMPTS"]
"""
Ad Extension Type.

Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
"""


class SPGlobalAdExtension(LenientModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    adExtensionSettings: SPGlobalAdExtensionSettings
    adExtensionStatus: SPGlobalAdExtensionStatus | str | None = Field(default=None)
    adExtensionType: SPGlobalAdExtensionType | str
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SPGlobalAdProduct | str
    creationDateTime: datetime = Field(description="The date time the ad_extension was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the ad_extension was last updated.")
    marketplaceScope: SPGlobalMarketplaceScope | str
    marketplaces: list[SPGlobalMarketplace | str] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SPGlobalState | str


class SPGlobalAdExtensionAdExtensionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdExtensionAdExtensionStatusFilter(StrictModel):
    include: list[SPGlobalAdExtensionStatus] = Field(min_length=1, max_length=1)


class SPGlobalAdExtensionAdExtensionTypeFilter(StrictModel):
    include: list[SPGlobalAdExtensionType] = Field(min_length=1, max_length=1)


class SPGlobalAdExtensionAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdExtensionAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdExtensionAdProductFilter(StrictModel):
    include: list[SPGlobalAdProduct] = Field(min_length=1, max_length=1)


class SPGlobalAdExtensionCreate(StrictModel):
    adExtensionSettings: SPGlobalCreateAdExtensionSettings
    adExtensionStatus: SPGlobalAdExtensionStatus | None = Field(default=None)
    adExtensionType: SPGlobalAdExtensionType
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SPGlobalAdProduct
    marketplaceScope: SPGlobalMarketplaceScope
    marketplaces: list[SPGlobalMarketplace] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SPGlobalCreateState


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
    include: list[SPGlobalState] = Field(min_length=1, max_length=3)


class SPGlobalAdExtensionSuccessResponse(LenientModel):
    adExtensions: list[SPGlobalAdExtension] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPGlobalAdExtensionUpdate(StrictModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    marketplaces: list[SPGlobalMarketplace] | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SPGlobalUpdateState | None = Field(default=None)


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
