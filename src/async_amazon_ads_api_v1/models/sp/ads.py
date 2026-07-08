"""Auto-generated Pydantic models for sp from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import (
    SPAdProduct,
    SPCreateState,
    SPMarketplace,
    SPMarketplaceScope,
    SPProductIdType,
    SPState,
    SPUpdateState,
)
from .shared import SPCreateTag, SPStatus, SPTag


class SPAd(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adId: str  # The identifier of the ad.
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    adType: Annotated[SPAdType | str, lenient_enum(SPAdType)]
    campaignId: str  # The campaign associated with the ad. It's a read-only field.
    creationDateTime: datetime  # The date time that the ad was created.
    creative: SPCreative
    globalAdId: str | None = None  # The global ad identifier that manages this marketplace ad.
    lastUpdatedDateTime: datetime  # The date time that the ad was last updated.
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[
        Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]
    ]  # The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.
    state: Annotated[SPState | str, lenient_enum(SPState)]
    status: SPStatus | None = None
    tags: list[SPTag] | None = None  # Open ended labels with a key value pair applied to the ad


class SPAdAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdAdIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    ]  # **AdProduct Enum:** AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    adType: Annotated[SPAdType | str, lenient_enum(SPAdType)]
    creative: SPCreateCreative
    state: Annotated[SPCreateState | str, lenient_enum(SPCreateState)]
    tags: list[SPCreateTag] | None = None  # Open ended labels with a key value pair applied to the ad


class SPAdMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPAdMultiStatusSuccess] | None = None


class SPAdMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ad: SPAd
    index: int


class SPAdStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPState | str, lenient_enum(SPState)]
    ]  # **State Enum:** State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPAdSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ads: list[SPAd] | None = None
    nextToken: str | None = None


class SPAdType(StrEnum):
    """**AdType Enum:**

    | AdType | Description |
    |------|------|
    | `PRODUCT_AD` | A creative built based on a specified product. |
    """

    PRODUCT_AD = "PRODUCT_AD"


class SPAdUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adId: str  # The identifier of the ad.
    creative: SPUpdateCreative | None = None
    state: Annotated[SPUpdateState | str, lenient_enum(SPUpdateState)] | None = None
    tags: list[SPCreateTag] | None = None  # Open ended labels with a key value pair applied to the ad


class SPAdvertisedProducts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    globalStoreSetting: SPGlobalStoreSettings | None = None
    productId: str  # The identifier of the advertised product.
    productIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)]
    resolvedProductId: str | None = (
        None  # The identifier of product associated with the advertised product. It's a read-only field.
    )
    resolvedProductIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)] | None = None


class SPCreateAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ads: list[SPAdCreate]


class SPCreateAdvertisedProducts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    globalStoreSetting: SPCreateGlobalStoreSettings | None = None
    productId: str  # The identifier of the advertised product.
    productIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)]


class SPCreateCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreative: SPCreateProductCreative | None = None


class SPCreateGlobalStoreSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)] | None = None


class SPCreateProductCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: SPCreateProductCreativeSettings


class SPCreateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""

    model_config = ConfigDict(extra="forbid")

    advertisedProduct: SPCreateAdvertisedProducts
    headline: str | None = None  # The headline/custom text associated with the ad creative.
    spotlightVideos: SPCreateSpotlightVideoSettings | None = None


class SPCreateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""

    model_config = ConfigDict(extra="forbid")

    optimizeText: bool  # If the advertiser wants text they provided to be optimized by Amazon or not.
    videos: list[SPCreateVideo]  # The video asset(s) to use for the Sponsored Product experience.


class SPCreateVideo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.
    description: str | None = None  # The description of the video content.
    headline: str | None = None  # The headline/custom text associated with the video.


class SPCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreative: SPProductCreative | None = None


class SPDeleteAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adIds: list[str]


class SPGlobalStoreSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)] | None = None


class SPProductCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: SPProductCreativeSettings


class SPProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""

    model_config = ConfigDict(extra="forbid")

    advertisedProduct: SPAdvertisedProducts
    headline: str | None = None  # The headline/custom text associated with the ad creative.
    spotlightVideos: SPSpotlightVideoSettings | None = None


class SPQueryAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SPAdAdGroupIdFilter | None = None
    adIdFilter: SPAdAdIdFilter | None = None
    adProductFilter: SPAdAdProductFilter
    campaignIdFilter: SPAdCampaignIdFilter | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: SPAdStateFilter | None = None


class SPSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""

    model_config = ConfigDict(extra="forbid")

    optimizeText: bool  # If the advertiser wants text they provided to be optimized by Amazon or not.
    videos: list[SPVideo]  # The video asset(s) to use for the Sponsored Product experience.


class SPUpdateAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ads: list[SPAdUpdate]


class SPUpdateCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreative: SPUpdateProductCreative | None = None


class SPUpdateProductCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: SPUpdateProductCreativeSettings | None = None


class SPUpdateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""

    model_config = ConfigDict(extra="forbid")

    spotlightVideos: SPUpdateSpotlightVideoSettings | None = None


class SPUpdateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""

    model_config = ConfigDict(extra="forbid")

    optimizeText: bool | None = None  # If the advertiser wants text they provided to be optimized by Amazon or not.
    videos: list[SPCreateVideo] | None = None  # The video asset(s) to use for the Sponsored Product experience.


class SPVideo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.
    description: str | None = None  # The description of the video content.
    headline: str | None = None  # The headline/custom text associated with the video.


__all__ = [
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
    "SPAdType",
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
