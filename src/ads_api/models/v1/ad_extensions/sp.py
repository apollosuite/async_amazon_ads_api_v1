"""Auto-generated models for AdExtensions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
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

type SPAdExtensionStatus = Literal["OPTED_OUT",]  # If the advertiser has opted out of this Ad Extension.
"""
Ad Extension Status.

Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
"""


type SPAdExtensionType = Literal[
    "PROMPTS",  # Enables Prompt based Ad Extension.
    "VIDEO",  # Enables Video based Ad Extension.
]
"""
Ad Extension Type.

Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
- `VIDEO`: Enables Video based Ad Extension.
"""


type SPMarketplace = Literal[
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


type SPVideoType = Literal["SPOTLIGHT",]  # SPOTLIGHT Video Asset.
"""
Video Type: Video type of the asset added in the ad extension and its rendering form.

Supported values:
- `SPOTLIGHT`: SPOTLIGHT Video Asset.
"""


class SPAdExtension(LenientModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    adExtensionSettings: SPAdExtensionSettings
    adExtensionStatus: SPAdExtensionStatus | str | None = Field(
        default=None,
        description="""
Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
""",
    )
    adExtensionType: SPAdExtensionType | str = Field(description="""
Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
- `VIDEO`: Enables Video based Ad Extension.
""")
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SPAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
    creationDateTime: datetime = Field(description="The date time the ad_extension was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the ad_extension was last updated.")
    marketplaceScope: SPMarketplaceScope | str
    marketplaces: list[SPMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SPState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    status: SPStatus | None = Field(default=None)


class SPAdExtensionAdExtensionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdExtensionAdExtensionStatusFilter(StrictModel):
    include: list[SPAdExtensionStatus | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
""",
    )


class SPAdExtensionAdExtensionTypeFilter(StrictModel):
    include: list[SPAdExtensionType | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
- `VIDEO`: Enables Video based Ad Extension.
""",
    )


class SPAdExtensionAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdExtensionAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdExtensionAdProductFilter(StrictModel):
    include: list[SPAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""",
    )


class SPAdExtensionCreate(StrictModel):
    adExtensionSettings: SPCreateAdExtensionSettings
    adExtensionStatus: SPAdExtensionStatus | None = Field(
        default=None,
        description="""
Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
""",
    )
    adExtensionType: SPAdExtensionType = Field(description="""
Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
- `VIDEO`: Enables Video based Ad Extension.
""")
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SPAdProduct = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[SPMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SPCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")


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
    include: list[SPState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SPAdExtensionSuccessResponse(LenientModel):
    adExtensions: list[SPAdExtension] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPAdExtensionUpdate(StrictModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    state: SPUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


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
    videoType: SPVideoType | str = Field(description="""
Supported values:
- `SPOTLIGHT`: SPOTLIGHT Video Asset.
""")


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
