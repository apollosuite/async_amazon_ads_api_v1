"""Auto-generated models for Ads from Amazon Ads API v1."""

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
    SPCreateTag,
    SPDeliveryReason,
    SPDeliveryStatus,
    SPError,
    SPErrorCode,
    SPErrorsIndex,
    SPMarketplaceScope,
    SPProductIdType,
    SPState,
    SPStatus,
    SPTag,
    SPUpdateState,
)


class SPAdType(StrEnum):
    PRODUCT_AD = "PRODUCT_AD"  # A creative built based on a specified product.


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


class SPAd(LenientModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The identifier of the ad.")
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    adType: Annotated[SPAdType | str, lenient_enum(SPAdType)]
    campaignId: str = Field(description="The campaign associated with the ad. It's a read-only field.")
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: SPCreative
    globalAdId: str | None = Field(
        default=None, description="The global ad identifier that manages this marketplace ad."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    state: Annotated[SPState | str, lenient_enum(SPState)]
    status: SPStatus | None = Field(default=None)
    tags: list[SPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPAdAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdAdProductFilter(StrictModel):
    include: list[Annotated[SPAdProduct, lenient_enum(SPAdProduct)]] = Field(min_length=1, max_length=1)


class SPAdCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdCreate(StrictModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: Annotated[SPAdProduct, lenient_enum(SPAdProduct)]
    adType: Annotated[SPAdType, lenient_enum(SPAdType)]
    creative: SPCreateCreative
    state: Annotated[SPCreateState, lenient_enum(SPCreateState)]
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPAdMultiStatusResponse(LenientModel):
    error: list[SPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPAdMultiStatusSuccess(LenientModel):
    ad: SPAd
    index: int = Field(ge=0, le=999)


class SPAdStateFilter(StrictModel):
    include: list[Annotated[SPState, lenient_enum(SPState)]] = Field(min_length=1, max_length=3)


class SPAdSuccessResponse(LenientModel):
    ads: list[SPAd] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPAdUpdate(StrictModel):
    adId: str = Field(description="The identifier of the ad.")
    creative: SPUpdateCreative | None = Field(default=None)
    state: Annotated[SPUpdateState, lenient_enum(SPUpdateState)] | None = Field(default=None)
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPAdvertisedProducts(LenientModel):
    globalStoreSetting: SPGlobalStoreSettings | None = Field(default=None)
    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)]
    resolvedProductId: str | None = Field(
        default=None,
        description="The identifier of product associated with the advertised product. It's a read-only field.",
    )
    resolvedProductIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)] | None = Field(default=None)


class SPCreateAdRequest(StrictModel):
    ads: list[SPAdCreate] = Field(min_length=1, max_length=1000)


class SPCreateAdvertisedProducts(StrictModel):
    globalStoreSetting: SPCreateGlobalStoreSettings | None = Field(default=None)
    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: Annotated[SPProductIdType, lenient_enum(SPProductIdType)]


class SPCreateCreative(StrictModel):
    productCreative: SPCreateProductCreative


class SPCreateGlobalStoreSettings(StrictModel):
    catalogSourceMarketplace: Annotated[SPMarketplace, lenient_enum(SPMarketplace)] | None = Field(default=None)


class SPCreateProductCreative(StrictModel):
    productCreativeSettings: SPCreateProductCreativeSettings


class SPCreateProductCreativeSettings(StrictModel):
    """An ad with a creative built based on the product being advertised."""

    advertisedProduct: SPCreateAdvertisedProducts
    headline: str | None = Field(default=None, description="The headline/custom text associated with the ad creative.")
    spotlightVideos: SPCreateSpotlightVideoSettings | None = Field(default=None)


class SPCreateSpotlightVideoSettings(StrictModel):
    """An ad with a creative built with spotlight videos."""

    optimizeText: bool = Field(
        description="If the advertiser wants text they provided to be optimized by Amazon or not."
    )
    videos: list[SPCreateVideo] = Field(
        min_length=1, max_length=5, description="The video asset(s) to use for the Sponsored Product experience."
    )


class SPCreateVideo(StrictModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")
    description: str | None = Field(default=None, description="The description of the video content.")
    headline: str | None = Field(default=None, description="The headline/custom text associated with the video.")


class SPCreative(LenientModel):
    productCreative: SPProductCreative


class SPDeleteAdRequest(StrictModel):
    adIds: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalStoreSettings(LenientModel):
    catalogSourceMarketplace: Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)] | None = Field(default=None)


class SPProductCreative(LenientModel):
    productCreativeSettings: SPProductCreativeSettings


class SPProductCreativeSettings(LenientModel):
    """An ad with a creative built based on the product being advertised."""

    advertisedProduct: SPAdvertisedProducts
    headline: str | None = Field(default=None, description="The headline/custom text associated with the ad creative.")
    spotlightVideos: SPSpotlightVideoSettings | None = Field(default=None)


class SPQueryAdRequest(StrictModel):
    adGroupIdFilter: SPAdAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SPAdAdIdFilter | None = Field(default=None)
    adProductFilter: SPAdAdProductFilter
    campaignIdFilter: SPAdCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: SPAdStateFilter | None = Field(default=None)


class SPSpotlightVideoSettings(LenientModel):
    """An ad with a creative built with spotlight videos."""

    optimizeText: bool = Field(
        description="If the advertiser wants text they provided to be optimized by Amazon or not."
    )
    videos: list[SPVideo] = Field(
        min_length=1, max_length=5, description="The video asset(s) to use for the Sponsored Product experience."
    )


class SPUpdateAdRequest(StrictModel):
    ads: list[SPAdUpdate] = Field(min_length=1, max_length=1000)


class SPUpdateCreative(StrictModel):
    productCreative: SPUpdateProductCreative


class SPUpdateProductCreative(StrictModel):
    productCreativeSettings: SPUpdateProductCreativeSettings | None = Field(default=None)


class SPUpdateProductCreativeSettings(StrictModel):
    """An ad with a creative built based on the product being advertised."""

    spotlightVideos: SPUpdateSpotlightVideoSettings | None = Field(default=None)


class SPUpdateSpotlightVideoSettings(StrictModel):
    """An ad with a creative built with spotlight videos."""

    optimizeText: bool | None = Field(
        default=None, description="If the advertiser wants text they provided to be optimized by Amazon or not."
    )
    videos: list[SPCreateVideo] | None = Field(
        default=None,
        min_length=1,
        max_length=5,
        description="The video asset(s) to use for the Sponsored Product experience.",
    )


class SPVideo(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")
    description: str | None = Field(default=None, description="The description of the video content.")
    headline: str | None = Field(default=None, description="The headline/custom text associated with the video.")


__all__ = [
    "SPAd",
    "SPAdAdGroupIdFilter",
    "SPAdAdIdFilter",
    "SPAdAdProductFilter",
    "SPAdCampaignIdFilter",
    "SPAdCreate",
    "SPAdMultiStatusResponse",
    "SPAdMultiStatusSuccess",
    "SPAdProduct",
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
    "SPCreateState",
    "SPCreateTag",
    "SPCreateVideo",
    "SPCreative",
    "SPDeleteAdRequest",
    "SPDeliveryReason",
    "SPDeliveryStatus",
    "SPError",
    "SPErrorCode",
    "SPErrorsIndex",
    "SPGlobalStoreSettings",
    "SPMarketplace",
    "SPMarketplaceScope",
    "SPProductCreative",
    "SPProductCreativeSettings",
    "SPProductIdType",
    "SPQueryAdRequest",
    "SPSpotlightVideoSettings",
    "SPState",
    "SPStatus",
    "SPTag",
    "SPUpdateAdRequest",
    "SPUpdateCreative",
    "SPUpdateProductCreative",
    "SPUpdateProductCreativeSettings",
    "SPUpdateSpotlightVideoSettings",
    "SPUpdateState",
    "SPVideo",
]
