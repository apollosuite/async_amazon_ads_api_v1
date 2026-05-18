"""Auto-generated Pydantic models for sd from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from enum import StrEnum

if TYPE_CHECKING:
    from async_amazon_ads_api_v1.errors import ErrorsIndex
    from .enums import (
        SDAdProduct,
        SDCreateState,
        SDMarketplace,
        SDMarketplaceScope,
        SDProductIdType,
        SDState,
        SDUpdateState,
    )
    from .shared import SDStatus


class SDAd(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adId: str  # The identifier of the ad.
    adProduct: SDAdProduct
    adType: SDAdType
    campaignId: str  # The campaign associated with the ad. It's a read-only field.
    creationDateTime: datetime  # The date time that the ad was created.
    creative: SDCreative
    lastUpdatedDateTime: datetime  # The date time that the ad was last updated.
    marketplaceScope: SDMarketplaceScope
    marketplaces: list[
        SDMarketplace
    ]  # The list of country codes representing amazon marketplaces in which the global ad is applicable. The marketplaces included should either be same as or subset of parent ad group
    name: str | None = None  # The name of the ad.
    state: SDState
    status: SDStatus | None = None


class SDAdAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SDAdProduct
    ]  # AdProduct Description `SPONSORED_DISPLAY` Sponsored Display ad product.


class SDAdCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adProduct: SDAdProduct
    adType: SDAdType
    creative: SDCreateCreative
    name: str | None = None  # The name of the ad.
    state: SDCreateState


class SDAdMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SDAdMultiStatusSuccess] | None = None


class SDAdMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ad: SDAd
    index: int


class SDAdSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SDAd] | None = None
    nextToken: str | None = None


class SDAdType(StrEnum):
    """| AdType | Description |
    |------|------|
    | `COMPONENT` | A creative that can features a collection of videos, images, and products. |
    """

    COMPONENT = "COMPONENT"


class SDAdUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adId: str  # The identifier of the ad.
    creative: SDUpdateCreative | None = None
    state: SDUpdateState | None = None


class SDAdvertisedProducts(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productId: str  # The identifier of the advertised product.
    productIdType: SDProductIdType


class SDAssetBasedCreativeSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    backgrounds: list[SDBackground] | None = None  # The background which is displayed on the ad.
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    hasTermsAndConditions: bool | None = (
        None  # Indicates that the ad promotes a free product or service and has qualifying terms and conditions applicable to the customer. LandingPageURL must link out to a page detailing terms and conditions or contain a link to those.
    )
    headlines: list[str]  # The headline(s) to use for the Asset Based Creative experience.
    images: list[SDImage] | None = None  # The image(s) to use.
    landingPage: SDComponentLandingPage
    logos: list[SDImage] | None = None  # The logos to use for the Asset Based Creative experience.
    moderationStatus: SDCreativeStatus | None = None
    untranslatedHeadlines: list[str]  # The headline entered by the advertiser.


class SDBackground(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    color: str | None = None  # The color hex code of the background.


class SDComponentCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetBasedCreativeSettings: SDAssetBasedCreativeSettings | None = None
    productVideoSettings: SDProductVideoSettings | None = None
    responsiveEcommerceSettings: SDResponsiveEcommerceSettings | None = None


class SDComponentLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SDComponentLandingPageType
    landingPageUrl: str  # The URL of landing page where the ad directs.


class SDComponentLandingPageType(StrEnum):
    """| ComponentLandingPageType | Description |
    |------|------|
    | `OFF_AMAZON_LINK` | An off-Amazon landing page. |
    """

    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


class SDCreateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SDAdCreate] | None = None


class SDCreateAdvertisedProducts(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productId: str  # The identifier of the advertised product.
    productIdType: SDProductIdType


class SDCreateAssetBasedCreativeSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPage: SDCreateComponentLandingPage


class SDCreateComponentCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetBasedCreativeSettings: SDCreateAssetBasedCreativeSettings | None = None
    productVideoSettings: SDCreateProductVideoSettings | None = None
    responsiveEcommerceSettings: SDCreateResponsiveEcommerceSettings | None = None


class SDCreateComponentLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SDComponentLandingPageType
    landingPageUrl: str  # The URL of landing page where the ad directs.


class SDCreateCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    componentCreative: SDCreateComponentCreative | None = None


class SDCreateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")

    landingPage: SDCreateVideoLandingPage | None = None
    products: list[SDCreateAdvertisedProducts] | None = (
        None  # The products featured in the video ad.
    )


class SDCreateResponsiveEcommerceLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SDResponsiveEcommerceLandingPageType
    landingPageUrl: str  # The URL of landing page where the ad directs.


class SDCreateResponsiveEcommerceSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPage: SDCreateResponsiveEcommerceLandingPage | None = None
    products: list[SDCreateAdvertisedProducts] | None = (
        None  # The products advertised for the Responsive eCommerce experience.
    )


class SDCreateVideoLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SDVideoLandingPageType
    landingPageUrl: str  # The URL of landing page where the ad directs.


class SDCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    componentCreative: SDComponentCreative | None = None


class SDCreativeStatus(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    moderationStatus: SDModerationStatus


class SDDeleteAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adIds: list[str] | None = None


class SDFormatProperties(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    height: int | None = None  # The height (in pixels) of the cropped image.
    left: int | None = (
        None  # The number of pixels from the left of the image where the crop should begin.
    )
    top: int | None = (
        None  # The number of pixels from the top of the image where the crop should begin.
    )
    width: int | None = None  # The width (in pixels) of the cropped image.


class SDImage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the image asset.
    assetVersion: str  # The asset library version associated with the image asset.
    formatProperties: list[SDFormatProperties] | None = (
        None  # The cropping and positioning properties associated with the asset.
    )


class SDModerationStatus(StrEnum):
    """| ModerationStatus | Description |
    |------|------|
    | `PUBLISHED` | The creative passed moderation and is serving. |
    | `REJECTED_BY_MODERATION` | The creative was rejected during the moderation process. |
    | `SUBMITTED_FOR_MODERATION` | The creative has been submitted, but has not yet been reviewed. |
    """

    PUBLISHED = "PUBLISHED"
    REJECTED_BY_MODERATION = "REJECTED_BY_MODERATION"
    SUBMITTED_FOR_MODERATION = "SUBMITTED_FOR_MODERATION"


class SDProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")

    brandLogos: list[SDImage] | None = None  # The brand logo image assets to be used in the ad.
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[str] | None = (
        None  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    )
    landingPage: SDVideoLandingPage | None = None
    moderationStatus: SDCreativeStatus | None = None
    products: list[SDAdvertisedProducts] | None = None  # The products featured in the video ad.
    untranslatedHeadlines: list[str] | None = None  # The headline entered by the advertiser.
    untranslatedVideos: list[
        SDVideo
    ]  # The original video assets submitted as part of the creative.
    videos: list[SDVideo]  # The video assets used in the ad.


class SDQueryAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProductFilter: SDAdAdProductFilter
    maxResults: int | None = None
    nextToken: str | None = None


class SDResponsiveEcommerceLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SDResponsiveEcommerceLandingPageType
    landingPageUrl: str  # The URL of landing page where the ad directs.


class SDResponsiveEcommerceLandingPageType(StrEnum):
    """| ResponsiveEcommerceLandingPageType | Description |
    |------|------|
    | `MOMENT` | A moment landing page. |
    | `STORE` | A brand Store landing page. |
    """

    MOMENT = "MOMENT"
    STORE = "STORE"


class SDResponsiveEcommerceSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: str | None = None  # The headline to use for the Responsive eCommerce experience.
    images: list[SDImage] | None = None  # The image(s) to use.
    landingPage: SDResponsiveEcommerceLandingPage | None = None
    logos: SDImage | None = None
    moderationStatus: SDCreativeStatus | None = None
    products: list[SDAdvertisedProducts] | None = (
        None  # The products advertised for the Responsive eCommerce experience.
    )
    untranslatedHeadlines: str | None = None  # The headline entered by the advertiser.


class SDUpdateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SDAdUpdate] | None = None


class SDUpdateAssetBasedCreativeSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")


class SDUpdateComponentCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetBasedCreativeSettings: SDUpdateAssetBasedCreativeSettings | None = None
    productVideoSettings: SDUpdateProductVideoSettings | None = None
    responsiveEcommerceSettings: SDUpdateResponsiveEcommerceSettings | None = None


class SDUpdateCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    componentCreative: SDUpdateComponentCreative | None = None


class SDUpdateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")


class SDUpdateResponsiveEcommerceSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")


class SDVideo(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.


class SDVideoLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SDVideoLandingPageType
    landingPageUrl: str  # The URL of landing page where the ad directs.


class SDVideoLandingPageType(StrEnum):
    """| VideoLandingPageType | Description |
    |------|------|
    | `MOMENT` | A moment landing page. |
    | `STORE` | A brand Store landing page. |
    """

    MOMENT = "MOMENT"
    STORE = "STORE"
