"""Auto-generated models for AdExtensions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBAdProduct,
    SBCreateState,
    SBError,
    SBErrorCode,
    SBErrorsIndex,
    SBMarketplaceScope,
    SBState,
    SBUpdateState,
)

type SBAdExtensionStatus = Literal["OPTED_OUT"]
"""
Ad Extension Status.

Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
"""


type SBAdExtensionType = Literal["PROMPTS"]
"""
Ad Extension Type.

Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
"""


type SBMarketplace = Literal[
    "AE",
    "AU",
    "BE",
    "BR",
    "CA",
    "DE",
    "EG",
    "ES",
    "FR",
    "GB",
    "IE",
    "IN",
    "IT",
    "JP",
    "MX",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "US",
    "ZA",
]
"""
A list of country codes representing Amazon marketplaces
"""


class SBAdExtension(LenientModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    adExtensionSettings: SBAdExtensionSettings
    adExtensionStatus: SBAdExtensionStatus | str | None = Field(default=None)
    adExtensionType: SBAdExtensionType | str
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SBAdProduct | str
    creationDateTime: datetime = Field(description="The date time the ad_extension was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the ad_extension was last updated.")
    marketplaceScope: SBMarketplaceScope | str
    marketplaces: list[SBMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SBState | str


class SBAdExtensionAdExtensionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBAdExtensionAdExtensionStatusFilter(StrictModel):
    include: list[SBAdExtensionStatus] = Field(min_length=1, max_length=1)


class SBAdExtensionAdExtensionTypeFilter(StrictModel):
    include: list[SBAdExtensionType] = Field(min_length=1, max_length=1)


class SBAdExtensionAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBAdExtensionAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBAdExtensionAdProductFilter(StrictModel):
    include: list[SBAdProduct] = Field(min_length=1, max_length=1)


class SBAdExtensionCreate(StrictModel):
    adExtensionSettings: SBCreateAdExtensionSettings
    adExtensionStatus: SBAdExtensionStatus | None = Field(default=None)
    adExtensionType: SBAdExtensionType
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SBAdProduct
    marketplaceScope: SBMarketplaceScope
    marketplaces: list[SBMarketplace] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SBCreateState


class SBAdExtensionMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=50)
    success: list[SBAdExtensionMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=50)


class SBAdExtensionMultiStatusSuccess(LenientModel):
    adExtension: SBAdExtension
    index: int = Field(ge=0, le=49)


class SBAdExtensionSettings(LenientModel):
    promptExtension: SBPromptExtension


class SBAdExtensionStateFilter(StrictModel):
    include: list[SBState] = Field(min_length=1, max_length=3)


class SBAdExtensionSuccessResponse(LenientModel):
    adExtensions: list[SBAdExtension] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SBAdExtensionUpdate(StrictModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    state: SBUpdateState | None = Field(default=None)


class SBCreateAdExtensionRequest(StrictModel):
    adExtensions: list[SBAdExtensionCreate] = Field(min_length=1, max_length=50)


class SBCreateAdExtensionSettings(StrictModel):
    promptExtension: SBCreatePromptExtension


class SBCreatePromptExtension(StrictModel):
    """Prompts Ad Extension"""

    promptText: str = Field(description="The prompt text rendered in the ads")


class SBPromptExtension(LenientModel):
    """Prompts Ad Extension"""

    promptText: str = Field(description="The prompt text rendered in the ads")


class SBQueryAdExtensionRequest(StrictModel):
    adExtensionIdFilter: SBAdExtensionAdExtensionIdFilter | None = Field(default=None)
    adExtensionStatusFilter: SBAdExtensionAdExtensionStatusFilter | None = Field(default=None)
    adExtensionTypeFilter: SBAdExtensionAdExtensionTypeFilter | None = Field(default=None)
    adGroupIdFilter: SBAdExtensionAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SBAdExtensionAdIdFilter | None = Field(default=None)
    adProductFilter: SBAdExtensionAdProductFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: SBAdExtensionStateFilter | None = Field(default=None)


class SBUpdateAdExtensionRequest(StrictModel):
    adExtensions: list[SBAdExtensionUpdate] = Field(min_length=1, max_length=50)


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
    "SBAdProduct",
    "SBCreateAdExtensionRequest",
    "SBCreateAdExtensionSettings",
    "SBCreatePromptExtension",
    "SBCreateState",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBPromptExtension",
    "SBQueryAdExtensionRequest",
    "SBState",
    "SBUpdateAdExtensionRequest",
    "SBUpdateState",
]
