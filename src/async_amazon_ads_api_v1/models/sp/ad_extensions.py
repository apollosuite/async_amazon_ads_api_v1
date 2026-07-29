"""Auto-generated models for AdExtensions from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .campaigns import (
    SPAdProduct,
    SPCreateState,
    SPMarketplace,
    SPMarketplaceScope,
    SPState,
    SPStatus,
    SPUpdateState,
)


class SPAdExtensionStatus(StrEnum):
    """
    Ad Extension Status.
    **AdExtensionStatus Enum:**

    | AdExtensionStatus | Description |
    |------|------|
    | `OPTED_OUT` | If the advertiser has opted out of this Ad Extension. |
    """

    OPTED_OUT = "OPTED_OUT"


class SPAdExtensionType(StrEnum):
    """
    Ad Extension Type.
    **AdExtensionType Enum:**

    | AdExtensionType | Description |
    |------|------|
    | `PROMPTS` | Enables Prompt based Ad Extension. |
    | `VIDEO` | Enables Video based Ad Extension. |
    """

    PROMPTS = "PROMPTS"
    VIDEO = "VIDEO"


class SPVideoType(StrEnum):
    """
    Video Type: Video type of the asset added in the ad extension and its rendering form.
    **VideoType Enum:**

    | VideoType | Description |
    |------|------|
    | `SPOTLIGHT` | SPOTLIGHT Video Asset. |
    """

    SPOTLIGHT = "SPOTLIGHT"


class SPAdExtension(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SPAdExtensionAdExtensionIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPAdExtensionAdExtensionStatusFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPAdExtensionStatus | str, lenient_enum(SPAdExtensionStatus)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdExtensionStatus Enum:**
| AdExtensionStatus | Description |
| --- | --- |
| `OPTED_OUT` | If the advertiser has opted out of this Ad Extension. |
""",
    )


class SPAdExtensionAdExtensionTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPAdExtensionType | str, lenient_enum(SPAdExtensionType)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdExtensionType Enum:**
| AdExtensionType | Description |
| --- | --- |
| `PROMPTS` | Enables Prompt based Ad Extension. |
| `VIDEO` | Enables Video based Ad Extension. |
""",
    )


class SPAdExtensionAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPAdExtensionAdIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPAdExtensionAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_PRODUCTS` | Sponsored Products ad product. |
""",
    )


class SPAdExtensionCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionSettings: SPCreateAdExtensionSettings
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
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: Annotated[SPCreateState | str, lenient_enum(SPCreateState)]


class SPAdExtensionMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=50)
    success: list[SPAdExtensionMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=50)


class SPAdExtensionMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    adExtension: SPAdExtension
    index: int = Field(ge=0, le=49)


class SPAdExtensionSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    promptExtension: SPPromptExtension | None = None
    videoExtension: SPVideoExtension | None = None


class SPAdExtensionStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPState | str, lenient_enum(SPState)]] = Field(
        min_length=1,
        max_length=3,
        description="""
**State Enum:**
| State | Description |
| --- | --- |
| `ENABLED` | The object is set active by user and eligible for delivery. |
| `PAUSED` | The object is stopped by user and not eligible for delivery. |
| `ARCHIVED` | The object is permanently stopped and cannot be reactivated. Terminal end state. |
""",
    )


class SPAdExtensionSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    adExtensions: list[SPAdExtension] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPAdExtensionUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    state: Annotated[SPUpdateState | str, lenient_enum(SPUpdateState)] | None = Field(default=None)


class SPCreateAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtensionCreate] = Field(min_length=1, max_length=50)


class SPCreateAdExtensionSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    promptExtension: SPCreatePromptExtension | None = None
    videoExtension: SPCreateVideoExtension | None = None


class SPCreatePromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str = Field(description="The prompt text rendered in the ads")


class SPCreateVideoExtension(BaseModel):
    """Video Ad Extension"""

    model_config = ConfigDict(extra="forbid")


class SPPromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="allow")

    promptText: str = Field(description="The prompt text rendered in the ads")


class SPQueryAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionIdFilter: SPAdExtensionAdExtensionIdFilter | None = Field(default=None)
    adExtensionStatusFilter: SPAdExtensionAdExtensionStatusFilter | None = Field(default=None)
    adExtensionTypeFilter: SPAdExtensionAdExtensionTypeFilter | None = Field(default=None)
    adGroupIdFilter: SPAdExtensionAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SPAdExtensionAdIdFilter | None = Field(default=None)
    adProductFilter: SPAdExtensionAdProductFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: SPAdExtensionStateFilter | None = Field(default=None)


class SPUpdateAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtensionUpdate] = Field(min_length=1, max_length=50)


class SPVideoExtension(BaseModel):
    """Video Ad Extension"""

    model_config = ConfigDict(extra="allow")

    renderedAssetId: str | None = Field(default=None, description="The video asset ID rendered in the ad.")
    renderedCoverImageUrl: str | None = Field(
        default=None, description="The image displayed over the video player before the video is played."
    )
    videoType: Annotated[SPVideoType | str, lenient_enum(SPVideoType)]


__all__ = [
    "SPAdExtensionStatus",
    "SPAdExtensionType",
    "SPVideoType",
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
    "SPAdExtensionSuccessResponse",
    "SPAdExtensionUpdate",
    "SPCreateAdExtensionRequest",
    "SPCreateAdExtensionSettings",
    "SPCreatePromptExtension",
    "SPCreateVideoExtension",
    "SPPromptExtension",
    "SPQueryAdExtensionRequest",
    "SPUpdateAdExtensionRequest",
    "SPVideoExtension",
]
