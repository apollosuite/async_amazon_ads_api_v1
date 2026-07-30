"""Auto-generated models for AdExtensions from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import SBAdProduct, SBCreateState, SBErrorCode, SBMarketplace, SBMarketplaceScope, SBState, SBUpdateState
from .shared import SBErrorsIndex


class SBAdExtensionStatus(StrEnum):
    """
    Ad Extension Status.
    **AdExtensionStatus Enum:**

    | AdExtensionStatus | Description |
    |------|------|
    | `OPTED_OUT` | If the advertiser has opted out of this Ad Extension. |
    """

    OPTED_OUT = "OPTED_OUT"


class SBAdExtensionType(StrEnum):
    """
    Ad Extension Type.
    **AdExtensionType Enum:**

    | AdExtensionType | Description |
    |------|------|
    | `PROMPTS` | Enables Prompt based Ad Extension. |
    """

    PROMPTS = "PROMPTS"


class SBAdExtension(BaseModel):
    model_config = ConfigDict(extra="allow")

    adExtensionId: str | None = Field(default=None, description="A unique identifier for the ad_extension.")
    adExtensionSettings: SBAdExtensionSettings | None = Field(default=None)
    adExtensionStatus: Annotated[SBAdExtensionStatus | str, lenient_enum(SBAdExtensionStatus)] | None = Field(
        default=None
    )
    adExtensionType: Annotated[SBAdExtensionType | str, lenient_enum(SBAdExtensionType)] | None = Field(default=None)
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)] | None = Field(default=None)
    creationDateTime: datetime | None = Field(default=None, description="The date time the ad_extension was created.")
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time the ad_extension was last updated."
    )
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)] | None = Field(default=None)
    marketplaces: list[Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: Annotated[SBState | str, lenient_enum(SBState)] | None = Field(default=None)


class SBAdExtensionAdExtensionIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SBAdExtensionAdExtensionStatusFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBAdExtensionStatus | str, lenient_enum(SBAdExtensionStatus)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdExtensionStatus Enum:**
| AdExtensionStatus | Description |
| --- | --- |
| `OPTED_OUT` | If the advertiser has opted out of this Ad Extension. |
""",
    )


class SBAdExtensionAdExtensionTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBAdExtensionType | str, lenient_enum(SBAdExtensionType)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdExtensionType Enum:**
| AdExtensionType | Description |
| --- | --- |
| `PROMPTS` | Enables Prompt based Ad Extension. |
""",
    )


class SBAdExtensionAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SBAdExtensionAdIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SBAdExtensionAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_BRANDS` | Sponsored Brands ad product. |
""",
    )


class SBAdExtensionCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionSettings: SBCreateAdExtensionSettings
    adExtensionStatus: Annotated[SBAdExtensionStatus | str, lenient_enum(SBAdExtensionStatus)] | None = Field(
        default=None
    )
    adExtensionType: Annotated[SBAdExtensionType | str, lenient_enum(SBAdExtensionType)]
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: Annotated[SBCreateState | str, lenient_enum(SBCreateState)]


class SBAdExtensionMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=50)
    success: list[SBAdExtensionMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=50)


class SBAdExtensionMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    adExtension: SBAdExtension | None = Field(default=None)
    index: int | None = Field(default=None, ge=0, le=49)


class SBAdExtensionSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    promptExtension: SBPromptExtension | None = None


class SBAdExtensionStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBState | str, lenient_enum(SBState)]] = Field(
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


class SBAdExtensionSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    adExtensions: list[SBAdExtension] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SBAdExtensionUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    state: Annotated[SBUpdateState | str, lenient_enum(SBUpdateState)] | None = Field(default=None)


class SBCreateAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SBAdExtensionCreate] = Field(min_length=1, max_length=50)


class SBCreateAdExtensionSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    promptExtension: SBCreatePromptExtension | None = None


class SBCreatePromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str = Field(description="The prompt text rendered in the ads")


class SBPromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="allow")

    promptText: str | None = Field(default=None, description="The prompt text rendered in the ads")


class SBQueryAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensionIdFilter: SBAdExtensionAdExtensionIdFilter | None = Field(default=None)
    adExtensionStatusFilter: SBAdExtensionAdExtensionStatusFilter | None = Field(default=None)
    adExtensionTypeFilter: SBAdExtensionAdExtensionTypeFilter | None = Field(default=None)
    adGroupIdFilter: SBAdExtensionAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SBAdExtensionAdIdFilter | None = Field(default=None)
    adProductFilter: SBAdExtensionAdProductFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: SBAdExtensionStateFilter | None = Field(default=None)


class SBUpdateAdExtensionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SBAdExtensionUpdate] = Field(min_length=1, max_length=50)


__all__ = [
    "SBAdExtensionAdExtensionIdFilter",
    "SBAdExtensionAdExtensionStatusFilter",
    "SBAdExtensionAdExtensionTypeFilter",
    "SBAdExtensionAdGroupIdFilter",
    "SBAdExtensionAdIdFilter",
    "SBAdExtensionAdProductFilter",
    "SBAdExtensionCreate",
    "SBAdExtensionStateFilter",
    "SBAdExtensionStatus",
    "SBAdExtensionType",
    "SBAdExtensionUpdate",
    "SBAdProduct",
    "SBCreateAdExtensionRequest",
    "SBCreateAdExtensionSettings",
    "SBCreatePromptExtension",
    "SBCreateState",
    "SBErrorCode",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBQueryAdExtensionRequest",
    "SBState",
    "SBUpdateAdExtensionRequest",
    "SBUpdateState",
]
