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
    SPGlobalMarketplaceScope,
    SPGlobalState,
    SPGlobalUpdateState,
)

type SPGlobalAdExtensionStatus = Literal["OPTED_OUT",]  # If the advertiser has opted out of this Ad Extension.
"""
Ad Extension Status.

Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
"""


type SPGlobalAdExtensionType = Literal["PROMPTS",]  # Enables Prompt based Ad Extension.
"""
Ad Extension Type.

Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
"""


type SPGlobalMarketplace = Literal[
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
]
"""
A list of country codes representing Amazon marketplaces
"""


class SPGlobalAdExtension(LenientModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    adExtensionSettings: SPGlobalAdExtensionSettings
    adExtensionStatus: SPGlobalAdExtensionStatus | str | None = Field(
        default=None,
        description="""
Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
""",
    )
    adExtensionType: SPGlobalAdExtensionType | str = Field(description="""
Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
""")
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SPGlobalAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
    creationDateTime: datetime = Field(description="The date time the ad_extension was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the ad_extension was last updated.")
    marketplaceScope: SPGlobalMarketplaceScope | str
    marketplaces: list[SPGlobalMarketplace | str] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SPGlobalState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")


class SPGlobalAdExtensionAdExtensionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdExtensionAdExtensionStatusFilter(StrictModel):
    include: list[SPGlobalAdExtensionStatus | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
""",
    )


class SPGlobalAdExtensionAdExtensionTypeFilter(StrictModel):
    include: list[SPGlobalAdExtensionType | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
""",
    )


class SPGlobalAdExtensionAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdExtensionAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdExtensionAdProductFilter(StrictModel):
    include: list[SPGlobalAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""",
    )


class SPGlobalAdExtensionCreate(StrictModel):
    adExtensionSettings: SPGlobalCreateAdExtensionSettings
    adExtensionStatus: SPGlobalAdExtensionStatus | None = Field(
        default=None,
        description="""
Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
""",
    )
    adExtensionType: SPGlobalAdExtensionType = Field(description="""
Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
""")
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SPGlobalAdProduct = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
    marketplaceScope: SPGlobalMarketplaceScope
    marketplaces: list[SPGlobalMarketplace | str] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SPGlobalCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")


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
    include: list[SPGlobalState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SPGlobalAdExtensionSuccessResponse(LenientModel):
    adExtensions: list[SPGlobalAdExtension] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPGlobalAdExtensionUpdate(StrictModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    marketplaces: list[SPGlobalMarketplace | str] | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SPGlobalUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


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
