"""creative models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import SPMarketplace, SPProductIdType


class SPAdvertisedProducts(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    globalStoreSetting: SPGlobalStoreSettings | None = None
    productId: str  # The identifier of the advertised product.
    productIdType: SPProductIdType
    resolvedProductId: str | None = (
        None  # The identifier of product associated with the advertised product. It's a read-only field.
    )
    resolvedProductIdType: SPProductIdType | None = None


class SPCreateAdvertisedProducts(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    globalStoreSetting: SPCreateGlobalStoreSettings | None = None
    productId: str  # The identifier of the advertised product.
    productIdType: SPProductIdType


class SPCreateCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCreative: SPCreateProductCreative | None = None


class SPCreateGlobalStoreSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: SPMarketplace | None = None


class SPCreateProductCreative(BaseModel):
    """"""

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

    optimizeText: (
        bool  # If the advertiser wants text they provided to be optimized by Amazon or not.
    )
    videos: list[SPCreateVideo]  # The video asset(s) to use for the Sponsored Product experience.


class SPCreateVideo(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.
    description: str | None = None  # The description of the video content.
    headline: str | None = None  # The headline/custom text associated with the video.


class SPCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCreative: SPProductCreative | None = None


class SPGlobalStoreSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: SPMarketplace | None = None


class SPProductCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: SPProductCreativeSettings


class SPProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""

    model_config = ConfigDict(extra="forbid")

    advertisedProduct: SPAdvertisedProducts
    headline: str | None = None  # The headline/custom text associated with the ad creative.
    spotlightVideos: SPSpotlightVideoSettings | None = None


class SPSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""

    model_config = ConfigDict(extra="forbid")

    optimizeText: (
        bool  # If the advertiser wants text they provided to be optimized by Amazon or not.
    )
    videos: list[SPVideo]  # The video asset(s) to use for the Sponsored Product experience.


class SPUpdateCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCreative: SPUpdateProductCreative | None = None


class SPUpdateProductCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: SPUpdateProductCreativeSettings | None = None


class SPUpdateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""

    model_config = ConfigDict(extra="forbid")

    spotlightVideos: SPUpdateSpotlightVideoSettings | None = None


class SPUpdateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""

    model_config = ConfigDict(extra="forbid")

    optimizeText: bool | None = (
        None  # If the advertiser wants text they provided to be optimized by Amazon or not.
    )
    videos: list[SPCreateVideo] | None = (
        None  # The video asset(s) to use for the Sponsored Product experience.
    )


class SPVideo(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.
    description: str | None = None  # The description of the video content.
    headline: str | None = None  # The headline/custom text associated with the video.
