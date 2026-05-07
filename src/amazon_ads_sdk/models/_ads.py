"""ad models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class SPAd(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adId: str  # The identifier of the ad.
    adProduct: dict[str, Any]
    adType: dict[str, Any]
    campaignId: str  # The campaign associated with the ad. It's a read-only field.
    creationDateTime: datetime  # The date time that the ad was created.
    creative: dict[str, Any]
    globalAdId: str | None = None  # The global ad identifier that manages this marketplace ad.
    lastUpdatedDateTime: datetime  # The date time that the ad was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]]  # The list of country codes representing amazon marketplaces in which the global a
    state: dict[str, Any]
    status: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the ad
class SPAdCreate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adProduct: dict[str, Any]
    adType: dict[str, Any]
    creative: dict[str, Any]
    state: dict[str, Any]
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the ad
class SPAdMultiStatusSuccess(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    ad: dict[str, Any]
    index: int
class SPAdUpdate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adId: str  # The identifier of the ad.
    creative: dict[str, Any] | None = None
    state: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the ad
class SPAdvertisedProducts(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    globalStoreSetting: dict[str, Any] | None = None
    productId: str  # The identifier of the advertised product.
    productIdType: dict[str, Any]
    resolvedProductId: str | None = None  # The identifier of product associated with the advertised product. It's a read-on
    resolvedProductIdType: dict[str, Any] | None = None
class SPAudienceBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid
class SPCreateAdvertisedProducts(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    globalStoreSetting: dict[str, Any] | None = None
    productId: str  # The identifier of the advertised product.
    productIdType: dict[str, Any]
class SPCreateAudienceBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid
class SPCreateCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")
class SPCreateCreativeBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    creativeType: dict[str, Any] | None = None
    percentage: int  # The selection of the percentage change associated with the creative type and bid
class SPCreateProductCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: dict[str, Any]
class SPCreateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""
    model_config = ConfigDict(extra="forbid")

    advertisedProduct: dict[str, Any]
    headline: str | None = None  # The headline/custom text associated with the ad creative.
    spotlightVideos: dict[str, Any] | None = None
class SPCreateProductValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productId: str  # The product identifier. Either the product id or the marketplace settings should
class SPCreateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""
    model_config = ConfigDict(extra="forbid")

    optimizeText: bool  # If the advertiser wants text they provided to be optimized by Amazon or not.
    videos: list[dict[str, Any]]  # The video asset(s) to use for the Sponsored Product experience.
class SPCreateVideo(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.
    description: str | None = None  # The description of the video content.
    headline: str | None = None  # The headline/custom text associated with the video.
class SPCreateVideoExtension(BaseModel):
    """Video Ad Extension"""
    model_config = ConfigDict(extra="forbid")
class SPCreativeBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    creativeType: dict[str, Any] | None = None
    percentage: int  # The selection of the percentage change associated with the creative type and bid
class SPProductCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: dict[str, Any]
class SPProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""
    model_config = ConfigDict(extra="forbid")

    advertisedProduct: dict[str, Any]
    headline: str | None = None  # The headline/custom text associated with the ad creative.
    spotlightVideos: dict[str, Any] | None = None
class SPProductValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productId: str  # The product identifier. Either the product id or the marketplace settings should
class SPSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""
    model_config = ConfigDict(extra="forbid")

    optimizeText: bool  # If the advertiser wants text they provided to be optimized by Amazon or not.
    videos: list[dict[str, Any]]  # The video asset(s) to use for the Sponsored Product experience.
class SPVideo(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.
    description: str | None = None  # The description of the video content.
    headline: str | None = None  # The headline/custom text associated with the video.
class SPVideoExtension(BaseModel):
    """Video Ad Extension"""
    model_config = ConfigDict(extra="forbid")

    renderedAssetId: str | None = None  # The video asset ID rendered in the ad.
    renderedCoverImageUrl: str | None = None  # The image displayed over the video player before the video is played.
    videoType: dict[str, Any]

