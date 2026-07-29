"""Auto-generated models for Ads from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .campaigns import (
    SDAdProduct,
    SDCreateState,
    SDMarketplace,
    SDMarketplaceScope,
    SDState,
    SDStatus,
    SDUpdateState,
)


class SDAdType(StrEnum):
    """
    **AdType Enum:**

    | AdType | Description |
    |------|------|
    | `COMPONENT` | A creative that can features a collection of videos, images, and products. |
    """

    COMPONENT = "COMPONENT"


class SDComponentLandingPageType(StrEnum):
    """
    **ComponentLandingPageType Enum:**

    | ComponentLandingPageType | Description |
    |------|------|
    | `OFF_AMAZON_LINK` | An off-Amazon landing page. |
    """

    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


class SDModerationStatus(StrEnum):
    """
    **ModerationStatus Enum:**

    | ModerationStatus | Description |
    |------|------|
    | `PUBLISHED` | The creative passed moderation and is serving. |
    | `REJECTED_BY_MODERATION` | The creative was rejected during the moderation process. |
    | `SUBMITTED_FOR_MODERATION` | The creative has been submitted, but has not yet been reviewed. |
    """

    PUBLISHED = "PUBLISHED"
    REJECTED_BY_MODERATION = "REJECTED_BY_MODERATION"
    SUBMITTED_FOR_MODERATION = "SUBMITTED_FOR_MODERATION"


class SDProductIdType(StrEnum):
    """
    **ProductIdType Enum:**

    | ProductIdType | Description |
    |------|------|
    | `ASIN` | ASIN identifier type. |
    | `SKU` | SKU identifier type. |
    """

    ASIN = "ASIN"
    SKU = "SKU"


class SDResponsiveEcommerceLandingPageType(StrEnum):
    """
    **ResponsiveEcommerceLandingPageType Enum:**

    | ResponsiveEcommerceLandingPageType | Description |
    |------|------|
    | `MOMENT` | A moment landing page. |
    | `STORE` | A brand Store landing page. |
    """

    MOMENT = "MOMENT"
    STORE = "STORE"


class SDVideoLandingPageType(StrEnum):
    """
    **VideoLandingPageType Enum:**

    | VideoLandingPageType | Description |
    |------|------|
    | `MOMENT` | A moment landing page. |
    | `STORE` | A brand Store landing page. |
    """

    MOMENT = "MOMENT"
    STORE = "STORE"


class SDAd(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The identifier of the ad.")
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    adType: Annotated[SDAdType | str, lenient_enum(SDAdType)]
    campaignId: str = Field(description="The campaign associated with the ad. It's a read-only field.")
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: SDCreative
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str | None = Field(default=None, description="The name of the ad.")
    state: Annotated[SDState | str, lenient_enum(SDState)]
    status: SDStatus | None = Field(default=None)


class SDAdAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_DISPLAY` | Sponsored Display ad product. |
""",
    )


class SDAdCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    adType: Annotated[SDAdType | str, lenient_enum(SDAdType)]
    creative: SDCreateCreative
    name: str | None = Field(default=None, description="The name of the ad.")
    state: Annotated[SDCreateState | str, lenient_enum(SDCreateState)]


class SDAdMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[SDAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class SDAdMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    ad: SDAd
    index: int = Field(ge=0, le=99)


class SDAdSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    ads: list[SDAd] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SDAdUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adId: str = Field(description="The identifier of the ad.")
    creative: SDUpdateCreative | None = Field(default=None)
    state: Annotated[SDUpdateState | str, lenient_enum(SDUpdateState)] | None = Field(default=None)


class SDAdvertisedProducts(BaseModel):
    model_config = ConfigDict(extra="allow")

    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: Annotated[SDProductIdType | str, lenient_enum(SDProductIdType)]


class SDAssetBasedCreativeSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SDBackground(BaseModel):
    model_config = ConfigDict(extra="allow")

    color: str | None = Field(default=None, description="The color hex code of the background.")


class SDComponentCreative(BaseModel):
    model_config = ConfigDict(extra="allow")

    assetBasedCreativeSettings: SDAssetBasedCreativeSettings | None = Field(default=None)
    productVideoSettings: SDProductVideoSettings | None = Field(default=None)
    responsiveEcommerceSettings: SDResponsiveEcommerceSettings | None = Field(default=None)


class SDComponentLandingPage(BaseModel):
    model_config = ConfigDict(extra="allow")

    landingPageType: Annotated[SDComponentLandingPageType | str, lenient_enum(SDComponentLandingPageType)]
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDCreateAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ads: list[SDAdCreate] = Field(min_length=1, max_length=100)


class SDCreateAdvertisedProducts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: Annotated[SDProductIdType | str, lenient_enum(SDProductIdType)]


class SDCreateAssetBasedCreativeSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPage: SDCreateComponentLandingPage


class SDCreateComponentCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetBasedCreativeSettings: SDCreateAssetBasedCreativeSettings | None = Field(default=None)
    productVideoSettings: SDCreateProductVideoSettings | None = Field(default=None)
    responsiveEcommerceSettings: SDCreateResponsiveEcommerceSettings | None = Field(default=None)


class SDCreateComponentLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageType: Annotated[SDComponentLandingPageType | str, lenient_enum(SDComponentLandingPageType)]
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDCreateCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    componentCreative: SDCreateComponentCreative | None = None


class SDCreateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")

    landingPage: SDCreateVideoLandingPage | None = Field(default=None)
    products: list[SDCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1, description="The products featured in the video ad."
    )


class SDCreateResponsiveEcommerceLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageType: Annotated[
        SDResponsiveEcommerceLandingPageType | str, lenient_enum(SDResponsiveEcommerceLandingPageType)
    ]
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDCreateResponsiveEcommerceSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPage: SDCreateResponsiveEcommerceLandingPage | None = Field(default=None)
    products: list[SDCreateAdvertisedProducts] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The products advertised for the Responsive eCommerce experience.",
    )


class SDCreateVideoLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageType: Annotated[SDVideoLandingPageType | str, lenient_enum(SDVideoLandingPageType)]
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDCreative(BaseModel):
    model_config = ConfigDict(extra="allow")

    componentCreative: SDComponentCreative | None = None


class SDCreativeStatus(BaseModel):
    model_config = ConfigDict(extra="allow")

    moderationStatus: Annotated[SDModerationStatus | str, lenient_enum(SDModerationStatus)]


class SDDeleteAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adIds: list[str] = Field(min_length=1, max_length=100)


class SDFormatProperties(BaseModel):
    model_config = ConfigDict(extra="allow")

    height: int | None = Field(default=None, description="The height (in pixels) of the cropped image.")
    left: int | None = Field(
        default=None, description="The number of pixels from the left of the image where the crop should begin."
    )
    top: int | None = Field(
        default=None, description="The number of pixels from the top of the image where the crop should begin."
    )
    width: int | None = Field(default=None, description="The width (in pixels) of the cropped image.")


class SDImage(BaseModel):
    model_config = ConfigDict(extra="allow")

    assetId: str = Field(description="The asset library ID associated with the image asset.")
    assetVersion: str = Field(description="The asset library version associated with the image asset.")
    formatProperties: list[SDFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class SDProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="allow")

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


class SDQueryAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProductFilter: SDAdAdProductFilter
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)


class SDResponsiveEcommerceLandingPage(BaseModel):
    model_config = ConfigDict(extra="allow")

    landingPageType: Annotated[
        SDResponsiveEcommerceLandingPageType | str, lenient_enum(SDResponsiveEcommerceLandingPageType)
    ]
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SDResponsiveEcommerceSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SDUpdateAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ads: list[SDAdUpdate] = Field(min_length=1, max_length=100)


class SDUpdateAssetBasedCreativeSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SDUpdateComponentCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetBasedCreativeSettings: SDUpdateAssetBasedCreativeSettings | None = Field(default=None)
    productVideoSettings: SDUpdateProductVideoSettings | None = Field(default=None)
    responsiveEcommerceSettings: SDUpdateResponsiveEcommerceSettings | None = Field(default=None)


class SDUpdateCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    componentCreative: SDUpdateComponentCreative | None = None


class SDUpdateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")


class SDUpdateResponsiveEcommerceSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SDVideo(BaseModel):
    model_config = ConfigDict(extra="allow")

    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class SDVideoLandingPage(BaseModel):
    model_config = ConfigDict(extra="allow")

    landingPageType: Annotated[SDVideoLandingPageType | str, lenient_enum(SDVideoLandingPageType)]
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


__all__ = [
    "SDAdType",
    "SDComponentLandingPageType",
    "SDModerationStatus",
    "SDProductIdType",
    "SDResponsiveEcommerceLandingPageType",
    "SDVideoLandingPageType",
    "SDAd",
    "SDAdAdProductFilter",
    "SDAdCreate",
    "SDAdMultiStatusResponse",
    "SDAdMultiStatusSuccess",
    "SDAdSuccessResponse",
    "SDAdUpdate",
    "SDAdvertisedProducts",
    "SDAssetBasedCreativeSettings",
    "SDBackground",
    "SDComponentCreative",
    "SDComponentLandingPage",
    "SDCreateAdRequest",
    "SDCreateAdvertisedProducts",
    "SDCreateAssetBasedCreativeSettings",
    "SDCreateComponentCreative",
    "SDCreateComponentLandingPage",
    "SDCreateCreative",
    "SDCreateProductVideoSettings",
    "SDCreateResponsiveEcommerceLandingPage",
    "SDCreateResponsiveEcommerceSettings",
    "SDCreateVideoLandingPage",
    "SDCreative",
    "SDCreativeStatus",
    "SDDeleteAdRequest",
    "SDFormatProperties",
    "SDImage",
    "SDProductVideoSettings",
    "SDQueryAdRequest",
    "SDResponsiveEcommerceLandingPage",
    "SDResponsiveEcommerceSettings",
    "SDUpdateAdRequest",
    "SDUpdateAssetBasedCreativeSettings",
    "SDUpdateComponentCreative",
    "SDUpdateCreative",
    "SDUpdateProductVideoSettings",
    "SDUpdateResponsiveEcommerceSettings",
    "SDVideo",
    "SDVideoLandingPage",
]
