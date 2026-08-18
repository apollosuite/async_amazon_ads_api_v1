"""Auto-generated models for Ads from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sd import (
    SDAdProduct,
    SDCreateState,
    SDDeliveryReason,
    SDDeliveryStatus,
    SDError,
    SDErrorCode,
    SDErrorsIndex,
    SDMarketplace,
    SDMarketplaceScope,
    SDProductIdType,
    SDState,
    SDStatus,
    SDUpdateState,
)

type SDAdType = Literal["COMPONENT"]
"""
Supported values:
- `COMPONENT`: A creative that can features a collection of videos, images, and products.
"""


type SDComponentLandingPageType = Literal["OFF_AMAZON_LINK"]
"""
Supported values:
- `OFF_AMAZON_LINK`: An off-Amazon landing page.
"""


type SDModerationStatus = Literal["PUBLISHED", "REJECTED_BY_MODERATION", "SUBMITTED_FOR_MODERATION"]
"""
Supported values:
- `PUBLISHED`: The creative passed moderation and is serving.
- `REJECTED_BY_MODERATION`: The creative was rejected during the moderation process.
- `SUBMITTED_FOR_MODERATION`: The creative has been submitted, but has not yet been reviewed.
"""


type SDResponsiveEcommerceLandingPageType = Literal["MOMENT", "STORE"]
"""
Supported values:
- `MOMENT`: A moment landing page.
- `STORE`: A brand Store landing page.
"""


type SDVideoLandingPageType = Literal["MOMENT", "STORE"]
"""
Supported values:
- `MOMENT`: A moment landing page.
- `STORE`: A brand Store landing page.
"""


class SDAd(LenientModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The identifier of the ad.")
    adProduct: SDAdProduct | str
    adType: SDAdType | str
    campaignId: str = Field(description="The campaign associated with the ad. It's a read-only field.")
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: SDCreative
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceScope: SDMarketplaceScope | str
    marketplaces: list[SDMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str | None = Field(default=None, description="The name of the ad.")
    state: SDState | str
    status: SDStatus | None = Field(default=None)


class SDAdAdProductFilter(StrictModel):
    include: list[SDAdProduct | str] = Field(min_length=1, max_length=1)


class SDAdCreate(StrictModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: SDAdProduct
    adType: SDAdType
    creative: SDCreateCreative
    name: str | None = Field(default=None, description="The name of the ad.")
    state: SDCreateState


class SDAdMultiStatusResponse(LenientModel):
    error: list[SDErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[SDAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class SDAdMultiStatusSuccess(LenientModel):
    ad: SDAd
    index: int = Field(ge=0, le=99)


class SDAdSuccessResponse(LenientModel):
    ads: list[SDAd] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SDAdUpdate(StrictModel):
    adId: str = Field(description="The identifier of the ad.")
    creative: SDUpdateCreative | None = Field(default=None)
    state: SDUpdateState | None = Field(default=None)


class SDAdvertisedProducts(LenientModel):
    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: SDProductIdType | str


class SDAssetBasedCreativeSettings(LenientModel):
    backgrounds: list[SDBackground] | None = Field(
        default=None, min_length=0, max_length=1, description="The background which is displayed on the ad."
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    hasTermsAndConditions: bool | None = Field(
        default=None,
        description="Indicates that the ad promotes a free product or service and has qualifying terms and conditions applicable to the customer. LandingPageURL must link out to a page detailing terms and conditions or contain a link to those.",
    )
    headlines: list[str] = Field(
        min_length=1, max_length=1, description="The headline(s) to use for the Asset Based Creative experience."
    )
    images: list[SDImage] | None = Field(default=None, min_length=0, max_length=3, description="The image(s) to use.")
    landingPage: SDComponentLandingPage
    logos: list[SDImage] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The logos to use for the Asset Based Creative experience.",
    )
    moderationStatus: SDCreativeStatus | None = Field(default=None)
    untranslatedHeadlines: list[str] = Field(
        min_length=1, max_length=1, description="The headline entered by the advertiser."
    )


class SDBackground(LenientModel):
    color: str | None = Field(default=None, description="The color hex code of the background.")


class SDComponentCreative(LenientModel):
    assetBasedCreativeSettings: SDAssetBasedCreativeSettings | None = Field(default=None)
    productVideoSettings: SDProductVideoSettings | None = Field(default=None)
    responsiveEcommerceSettings: SDResponsiveEcommerceSettings | None = Field(default=None)


class SDComponentLandingPage(LenientModel):
    landingPageType: SDComponentLandingPageType | str
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDCreateAdRequest(StrictModel):
    ads: list[SDAdCreate] = Field(min_length=1, max_length=100)


class SDCreateAdvertisedProducts(StrictModel):
    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: SDProductIdType


class SDCreateAssetBasedCreativeSettings(StrictModel):
    landingPage: SDCreateComponentLandingPage


class SDCreateComponentCreative(StrictModel):
    assetBasedCreativeSettings: SDCreateAssetBasedCreativeSettings | None = Field(default=None)
    productVideoSettings: SDCreateProductVideoSettings | None = Field(default=None)
    responsiveEcommerceSettings: SDCreateResponsiveEcommerceSettings | None = Field(default=None)


class SDCreateComponentLandingPage(StrictModel):
    landingPageType: SDComponentLandingPageType
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDCreateCreative(StrictModel):
    componentCreative: SDCreateComponentCreative


class SDCreateProductVideoSettings(StrictModel):
    """An ad with a creative that includes a video."""

    landingPage: SDCreateVideoLandingPage | None = Field(default=None)
    products: list[SDCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1, description="The products featured in the video ad."
    )


class SDCreateResponsiveEcommerceLandingPage(StrictModel):
    landingPageType: SDResponsiveEcommerceLandingPageType
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDCreateResponsiveEcommerceSettings(StrictModel):
    landingPage: SDCreateResponsiveEcommerceLandingPage | None = Field(default=None)
    products: list[SDCreateAdvertisedProducts] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The products advertised for the Responsive eCommerce experience.",
    )


class SDCreateVideoLandingPage(StrictModel):
    landingPageType: SDVideoLandingPageType
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDCreative(LenientModel):
    componentCreative: SDComponentCreative


class SDCreativeStatus(LenientModel):
    moderationStatus: SDModerationStatus | str


class SDDeleteAdRequest(StrictModel):
    adIds: list[str] = Field(min_length=1, max_length=100)


class SDFormatProperties(LenientModel):
    height: int | None = Field(default=None, description="The height (in pixels) of the cropped image.")
    left: int | None = Field(
        default=None, description="The number of pixels from the left of the image where the crop should begin."
    )
    top: int | None = Field(
        default=None, description="The number of pixels from the top of the image where the crop should begin."
    )
    width: int | None = Field(default=None, description="The width (in pixels) of the cropped image.")


class SDImage(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the image asset.")
    assetVersion: str = Field(description="The asset library version associated with the image asset.")
    formatProperties: list[SDFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class SDProductVideoSettings(LenientModel):
    """An ad with a creative that includes a video."""

    brandLogos: list[SDImage] | None = Field(
        default=None, min_length=0, max_length=1, description="The brand logo image assets to be used in the ad."
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SDVideoLandingPage | None = Field(default=None)
    moderationStatus: SDCreativeStatus | None = Field(default=None)
    products: list[SDAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1, description="The products featured in the video ad."
    )
    untranslatedHeadlines: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="The headline entered by the advertiser."
    )
    untranslatedVideos: list[SDVideo] = Field(
        min_length=1, max_length=2, description="The original video assets submitted as part of the creative."
    )
    videos: list[SDVideo] = Field(min_length=1, max_length=2, description="The video assets used in the ad.")


class SDQueryAdRequest(StrictModel):
    adProductFilter: SDAdAdProductFilter
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)


class SDResponsiveEcommerceLandingPage(LenientModel):
    landingPageType: SDResponsiveEcommerceLandingPageType | str
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDResponsiveEcommerceSettings(LenientModel):
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: str | None = Field(
        default=None, description="The headline to use for the Responsive eCommerce experience."
    )
    images: list[SDImage] | None = Field(default=None, min_length=0, max_length=3, description="The image(s) to use.")
    landingPage: SDResponsiveEcommerceLandingPage | None = Field(default=None)
    logos: SDImage | None = Field(default=None)
    moderationStatus: SDCreativeStatus | None = Field(default=None)
    products: list[SDAdvertisedProducts] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The products advertised for the Responsive eCommerce experience.",
    )
    untranslatedHeadlines: str | None = Field(default=None, description="The headline entered by the advertiser.")


class SDUpdateAdRequest(StrictModel):
    ads: list[SDAdUpdate] = Field(min_length=1, max_length=100)


class SDUpdateAssetBasedCreativeSettings(StrictModel):
    pass


class SDUpdateComponentCreative(StrictModel):
    assetBasedCreativeSettings: SDUpdateAssetBasedCreativeSettings | None = Field(default=None)
    productVideoSettings: SDUpdateProductVideoSettings | None = Field(default=None)
    responsiveEcommerceSettings: SDUpdateResponsiveEcommerceSettings | None = Field(default=None)


class SDUpdateCreative(StrictModel):
    componentCreative: SDUpdateComponentCreative


class SDUpdateProductVideoSettings(StrictModel):
    """An ad with a creative that includes a video."""

    pass


class SDUpdateResponsiveEcommerceSettings(StrictModel):
    pass


class SDVideo(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class SDVideoLandingPage(LenientModel):
    landingPageType: SDVideoLandingPageType | str
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


__all__ = [
    "SDAd",
    "SDAdAdProductFilter",
    "SDAdCreate",
    "SDAdMultiStatusResponse",
    "SDAdMultiStatusSuccess",
    "SDAdProduct",
    "SDAdSuccessResponse",
    "SDAdType",
    "SDAdUpdate",
    "SDAdvertisedProducts",
    "SDAssetBasedCreativeSettings",
    "SDBackground",
    "SDComponentCreative",
    "SDComponentLandingPage",
    "SDComponentLandingPageType",
    "SDCreateAdRequest",
    "SDCreateAdvertisedProducts",
    "SDCreateAssetBasedCreativeSettings",
    "SDCreateComponentCreative",
    "SDCreateComponentLandingPage",
    "SDCreateCreative",
    "SDCreateProductVideoSettings",
    "SDCreateResponsiveEcommerceLandingPage",
    "SDCreateResponsiveEcommerceSettings",
    "SDCreateState",
    "SDCreateVideoLandingPage",
    "SDCreative",
    "SDCreativeStatus",
    "SDDeleteAdRequest",
    "SDDeliveryReason",
    "SDDeliveryStatus",
    "SDError",
    "SDErrorCode",
    "SDErrorsIndex",
    "SDFormatProperties",
    "SDImage",
    "SDMarketplace",
    "SDMarketplaceScope",
    "SDModerationStatus",
    "SDProductIdType",
    "SDProductVideoSettings",
    "SDQueryAdRequest",
    "SDResponsiveEcommerceLandingPage",
    "SDResponsiveEcommerceLandingPageType",
    "SDResponsiveEcommerceSettings",
    "SDState",
    "SDStatus",
    "SDUpdateAdRequest",
    "SDUpdateAssetBasedCreativeSettings",
    "SDUpdateComponentCreative",
    "SDUpdateCreative",
    "SDUpdateProductVideoSettings",
    "SDUpdateResponsiveEcommerceSettings",
    "SDUpdateState",
    "SDVideo",
    "SDVideoLandingPage",
    "SDVideoLandingPageType",
]
