"""Auto-generated models for Ads from Amazon Ads API schema."""

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
    SPCreateTag,
    SPMarketplace,
    SPMarketplaceScope,
    SPState,
    SPStatus,
    SPTag,
    SPUpdateState,
)


class SPAdType(StrEnum):
    """
    **AdType Enum:**

    | AdType | Description |
    |------|------|
    | `PRODUCT_AD` | A creative built based on a specified product. |
    """

    PRODUCT_AD = "PRODUCT_AD"


class SPProductIdType(StrEnum):
    """
    **ProductIdType Enum:**

    | ProductIdType | Description |
    |------|------|
    | `ASIN` | ASIN identifier type. |
    | `SKU` | SKU identifier type. |
    """

    ASIN = "ASIN"
    SKU = "SKU"


class SPAd(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroupId: str | None = Field(default=None, description="The ad group associated with the ad.")
    adId: str | None = Field(default=None, description="The identifier of the ad.")
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)] | None = Field(default=None)
    adType: Annotated[SPAdType | str, lenient_enum(SPAdType)] | None = Field(default=None)
    campaignId: str | None = Field(
        default=None, description="The campaign associated with the ad. It's a read-only field."
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the ad was created.")
    creative: SPCreative | None = Field(default=None)
    globalAdId: str | None = Field(
        default=None, description="The global ad identifier that manages this marketplace ad."
    )
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the ad was last updated."
    )
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)] | None = Field(default=None)
    marketplaces: list[Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    state: Annotated[SPState | str, lenient_enum(SPState)] | None = Field(default=None)
    status: SPStatus | None = Field(default=None)
    tags: list[SPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPAdAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPAdAdIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPAdAdProductFilter(BaseModel):
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


class SPAdCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPAdCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    adType: Annotated[SPAdType | str, lenient_enum(SPAdType)]
    creative: SPCreateCreative
    state: Annotated[SPCreateState | str, lenient_enum(SPCreateState)]
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPAdMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPAdMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    ad: SPAd | None = Field(default=None)
    index: int | None = Field(default=None, ge=0, le=999)


class SPAdStateFilter(BaseModel):
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


class SPAdSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    ads: list[SPAd] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPAdUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adId: str = Field(description="The identifier of the ad.")
    creative: SPUpdateCreative | None = Field(default=None)
    state: Annotated[SPUpdateState | str, lenient_enum(SPUpdateState)] | None = Field(default=None)
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPAdvertisedProducts(BaseModel):
    model_config = ConfigDict(extra="allow")

    globalStoreSetting: SPGlobalStoreSettings | None = Field(default=None)
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)] | None = Field(default=None)
    resolvedProductId: str | None = Field(
        default=None,
        description="The identifier of product associated with the advertised product. It's a read-only field.",
    )
    resolvedProductIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)] | None = Field(default=None)


class SPCreateAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ads: list[SPAdCreate] = Field(min_length=1, max_length=1000)


class SPCreateAdvertisedProducts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    globalStoreSetting: SPCreateGlobalStoreSettings | None = Field(default=None)
    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)]


class SPCreateCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreative: SPCreateProductCreative | None = None


class SPCreateGlobalStoreSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)] | None = Field(default=None)


class SPCreateProductCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: SPCreateProductCreativeSettings


class SPCreateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""

    model_config = ConfigDict(extra="forbid")

    advertisedProduct: SPCreateAdvertisedProducts
    headline: str | None = Field(default=None, description="The headline/custom text associated with the ad creative.")
    spotlightVideos: SPCreateSpotlightVideoSettings | None = Field(default=None)


class SPCreateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""

    model_config = ConfigDict(extra="forbid")

    optimizeText: bool = Field(
        description="If the advertiser wants text they provided to be optimized by Amazon or not."
    )
    videos: list[SPCreateVideo] = Field(
        min_length=1, max_length=5, description="The video asset(s) to use for the Sponsored Product experience."
    )


class SPCreateVideo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")
    description: str | None = Field(default=None, description="The description of the video content.")
    headline: str | None = Field(default=None, description="The headline/custom text associated with the video.")


class SPCreative(BaseModel):
    model_config = ConfigDict(extra="allow")

    productCreative: SPProductCreative | None = None


class SPDeleteAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adIds: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalStoreSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    catalogSourceMarketplace: Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)] | None = Field(default=None)


class SPProductCreative(BaseModel):
    model_config = ConfigDict(extra="allow")

    productCreativeSettings: SPProductCreativeSettings | None = Field(default=None)


class SPProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""

    model_config = ConfigDict(extra="allow")

    advertisedProduct: SPAdvertisedProducts | None = Field(default=None)
    headline: str | None = Field(default=None, description="The headline/custom text associated with the ad creative.")
    spotlightVideos: SPSpotlightVideoSettings | None = Field(default=None)


class SPQueryAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SPAdAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SPAdAdIdFilter | None = Field(default=None)
    adProductFilter: SPAdAdProductFilter
    campaignIdFilter: SPAdCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: SPAdStateFilter | None = Field(default=None)


class SPSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""

    model_config = ConfigDict(extra="allow")

    optimizeText: bool | None = Field(
        default=None, description="If the advertiser wants text they provided to be optimized by Amazon or not."
    )
    videos: list[SPVideo] | None = Field(
        default=None,
        min_length=1,
        max_length=5,
        description="The video asset(s) to use for the Sponsored Product experience.",
    )


class SPUpdateAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ads: list[SPAdUpdate] = Field(min_length=1, max_length=1000)


class SPUpdateCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreative: SPUpdateProductCreative | None = None


class SPUpdateProductCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: SPUpdateProductCreativeSettings | None = Field(default=None)


class SPUpdateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""

    model_config = ConfigDict(extra="forbid")

    spotlightVideos: SPUpdateSpotlightVideoSettings | None = Field(default=None)


class SPUpdateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""

    model_config = ConfigDict(extra="forbid")

    optimizeText: bool | None = Field(
        default=None, description="If the advertiser wants text they provided to be optimized by Amazon or not."
    )
    videos: list[SPCreateVideo] | None = Field(
        default=None,
        min_length=1,
        max_length=5,
        description="The video asset(s) to use for the Sponsored Product experience.",
    )


class SPVideo(BaseModel):
    model_config = ConfigDict(extra="allow")

    assetId: str | None = Field(default=None, description="The asset library ID associated with the video asset.")
    assetVersion: str | None = Field(
        default=None, description="The asset library version associated with the video asset."
    )
    description: str | None = Field(default=None, description="The description of the video content.")
    headline: str | None = Field(default=None, description="The headline/custom text associated with the video.")


__all__ = [
    "SPAdType",
    "SPProductIdType",
    "SPAd",
    "SPAdAdGroupIdFilter",
    "SPAdAdIdFilter",
    "SPAdAdProductFilter",
    "SPAdCampaignIdFilter",
    "SPAdCreate",
    "SPAdMultiStatusResponse",
    "SPAdMultiStatusSuccess",
    "SPAdStateFilter",
    "SPAdSuccessResponse",
    "SPAdUpdate",
    "SPAdvertisedProducts",
    "SPCreateAdRequest",
    "SPCreateAdvertisedProducts",
    "SPCreateCreative",
    "SPCreateGlobalStoreSettings",
    "SPCreateProductCreative",
    "SPCreateProductCreativeSettings",
    "SPCreateSpotlightVideoSettings",
    "SPCreateVideo",
    "SPCreative",
    "SPDeleteAdRequest",
    "SPGlobalStoreSettings",
    "SPProductCreative",
    "SPProductCreativeSettings",
    "SPQueryAdRequest",
    "SPSpotlightVideoSettings",
    "SPUpdateAdRequest",
    "SPUpdateCreative",
    "SPUpdateProductCreative",
    "SPUpdateProductCreativeSettings",
    "SPUpdateSpotlightVideoSettings",
    "SPVideo",
]
