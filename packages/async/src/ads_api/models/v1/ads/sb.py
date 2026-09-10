"""Auto-generated models for Ads from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBAdProduct,
    SBCreateState,
    SBCreateTag,
    SBDeliveryReason,
    SBDeliveryStatus,
    SBError,
    SBErrorCode,
    SBErrorsIndex,
    SBMarketplace,
    SBMarketplaceScope,
    SBProductIdType,
    SBState,
    SBStatus,
    SBTag,
    SBUpdateState,
)

type SBAdNameFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SBAdType = Literal["COMPONENT"]
"""
Supported values:
- `COMPONENT`: A creative that can features a collection of videos, images, and products.
"""


type SBBrandGalleryCreativePropertiesToOptimize = Literal["HEADLINE"]
"""
Supported values:
- `HEADLINE`: The headline in the creative.
"""


type SBCollectionLandingPageType = Literal["ASIN_LIST", "STORE"]
"""
Supported values:
- `ASIN_LIST`: A list of products based on the products promoted in the ad creative.
- `STORE`: A brand Store landing page.
"""


type SBModerationStatus = Literal[
    "APPROVED_WITH_EXCEPTIONS", "PENDING_TRANSLATION", "PUBLISHED", "REJECTED_BY_MODERATION", "SUBMITTED_FOR_MODERATION"
]
"""
Supported values:
- `APPROVED_WITH_EXCEPTIONS`: The creative passed basic moderation but was found to be invalid for some supplies. The creative is serving on approved supplies.
- `PENDING_TRANSLATION`: The creative is pending creative Translations.
- `PUBLISHED`: The creative passed moderation and is serving.
- `REJECTED_BY_MODERATION`: The creative was rejected during the moderation process.
- `SUBMITTED_FOR_MODERATION`: The creative has been submitted, but has not yet been reviewed.
"""


type SBProductCollectionCreativePropertiesToOptimize = Literal["HEADLINE"]
"""
Supported values:
- `HEADLINE`: The headline in the creative.
"""


type SBProductCollectionLandingPageType = Literal["ASIN_LIST", "CUSTOM_URL", "STORE"]
"""
Supported values:
- `ASIN_LIST`: A list of products based on the products promoted in the ad creative.
- `CUSTOM_URL`: A custom landing page. Available for vendors only.
- `STORE`: A brand Store landing page.
"""


type SBStoreSpotlightCreativePropertiesToOptimize = Literal["HEADLINE"]
"""
Supported values:
- `HEADLINE`: The headline in the creative.
"""


type SBStoreSpotlightLandingPageType = Literal["STORE"]
"""
Supported values:
- `STORE`: A brand Store landing page.
"""


type SBVideoLandingPageType = Literal["DETAIL_PAGE", "STORE"]
"""
Supported values:
- `DETAIL_PAGE`: A product detail page.
- `STORE`: A brand Store landing page.
"""


class SBAd(LenientModel):
    activeCreative: SBCreative | None = Field(default=None)
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The identifier of the ad.")
    adProduct: SBAdProduct | str
    adType: SBAdType | str
    campaignId: str = Field(description="The campaign associated with the ad. It's a read-only field.")
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: SBCreative
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceScope: SBMarketplaceScope | str
    marketplaces: list[SBMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str = Field(description="The name of the ad.")
    state: SBState | str
    status: SBStatus | None = Field(default=None)
    tags: list[SBTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SBAdAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBAdAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBAdAdProductFilter(StrictModel):
    include: list[SBAdProduct] = Field(min_length=1, max_length=1)


class SBAdCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBAdCreate(StrictModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: SBAdProduct
    adType: SBAdType
    creative: SBCreateCreative
    name: str = Field(description="The name of the ad.")
    state: SBCreateState
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SBAdMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBAdMultiStatusSuccess(LenientModel):
    ad: SBAd
    index: int = Field(ge=0, le=9)


class SBAdNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)
    queryTermMatchType: SBAdNameFilterType


class SBAdStateFilter(StrictModel):
    include: list[SBState] = Field(min_length=1, max_length=3)


class SBAdSuccessResponse(LenientModel):
    ads: list[SBAd] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SBAdUpdate(StrictModel):
    adId: str = Field(description="The identifier of the ad.")
    creative: SBUpdateCreative | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad.")
    state: SBUpdateState | None = Field(default=None)
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SBAdvertisedProducts(LenientModel):
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: SBProductIdType | str


class SBAutoCollectionSettings(LenientModel):
    """Settings for automatically generated collections."""

    productExclusions: list[SBAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1000, description="Products to exclude from auto collection."
    )
    sharedSettings: SBSharedCollectionSettings


class SBBrandGalleryCardCreativeElement(LenientModel):
    customImage: SBImage
    headline: str = Field(description="The headline used for the card.")
    landingPage: SBStoreSpotlightLandingPage


class SBBrandGallerySettings(LenientModel):
    """An ad creative that showcases a brand and its categories and collections."""

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBImage] = Field(
        min_length=1, max_length=1, description="The brand logo image assets to be used in the ad."
    )
    cards: list[SBBrandGalleryCardCreativeElement] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The sub-elements of the creative. Each card highlights a different category associated to a brand.",
    )
    creativePropertiesToOptimize: list[SBBrandGalleryCreativePropertiesToOptimize | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    customImages: list[SBImage] | None = Field(
        default=None, min_length=0, max_length=1, description="The custom images featured in the ad."
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] = Field(
        min_length=1,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SBStoreSpotlightLandingPage
    moderationStatus: SBCreativeStatus | None = Field(default=None)
    untranslatedHeadlines: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="The headline entered by the advertiser."
    )


class SBCardCreativeElement(LenientModel):
    headline: str = Field(description="The headline used for the card.")
    landingPage: SBStoreSpotlightLandingPage
    products: SBAdvertisedProducts


class SBCollectionLandingPage(LenientModel):
    landingPageType: SBCollectionLandingPageType | str
    landingPageUrl: str | None = Field(default=None, description="The URL associated to the landing page.")


class SBComponentCreative(LenientModel):
    autoCollectionSettings: SBAutoCollectionSettings | None = Field(default=None)
    brandGallerySettings: SBBrandGallerySettings | None = Field(default=None)
    manualCollectionSettings: SBManualCollectionSettings | None = Field(default=None)
    productCollectionSettings: SBProductCollectionSettings | None = Field(default=None)
    productVideoSettings: SBProductVideoSettings | None = Field(default=None)
    storeSpotlightSettings: SBStoreSpotlightSettings | None = Field(default=None)


class SBCreateAdRequest(StrictModel):
    ads: list[SBAdCreate] = Field(min_length=1, max_length=10)


class SBCreateAdvertisedProducts(StrictModel):
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: SBProductIdType


class SBCreateAutoCollectionSettings(StrictModel):
    """Settings for automatically generated collections."""

    productExclusions: list[SBCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1000, description="Products to exclude from auto collection."
    )
    sharedSettings: SBCreateSharedCollectionSettings


class SBCreateBrandGalleryCardCreativeElement(StrictModel):
    customImage: SBCreateImage
    headline: str = Field(description="The headline used for the card.")
    landingPage: SBCreateStoreSpotlightLandingPage


class SBCreateBrandGallerySettings(StrictModel):
    """An ad creative that showcases a brand and its categories and collections."""

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] = Field(
        min_length=1, max_length=1, description="The brand logo image assets to be used in the ad."
    )
    cards: list[SBCreateBrandGalleryCardCreativeElement] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The sub-elements of the creative. Each card highlights a different category associated to a brand.",
    )
    creativePropertiesToOptimize: list[SBBrandGalleryCreativePropertiesToOptimize] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    customImages: list[SBCreateImage] | None = Field(
        default=None, min_length=0, max_length=1, description="The custom images featured in the ad."
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] = Field(
        min_length=1,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SBCreateStoreSpotlightLandingPage


class SBCreateCardCreativeElement(StrictModel):
    headline: str = Field(description="The headline used for the card.")
    landingPage: SBCreateStoreSpotlightLandingPage
    products: SBCreateAdvertisedProducts


class SBCreateCollectionLandingPage(StrictModel):
    landingPageType: SBCollectionLandingPageType
    landingPageUrl: str | None = Field(default=None, description="The URL associated to the landing page.")


class SBCreateComponentCreative(StrictModel):
    autoCollectionSettings: SBCreateAutoCollectionSettings | None = Field(default=None)
    brandGallerySettings: SBCreateBrandGallerySettings | None = Field(default=None)
    manualCollectionSettings: SBCreateManualCollectionSettings | None = Field(default=None)
    productCollectionSettings: SBCreateProductCollectionSettings | None = Field(default=None)
    productVideoSettings: SBCreateProductVideoSettings | None = Field(default=None)
    storeSpotlightSettings: SBCreateStoreSpotlightSettings | None = Field(default=None)


class SBCreateCreative(StrictModel):
    componentCreative: SBCreateComponentCreative


class SBCreateFormatProperties(StrictModel):
    height: int | None = Field(default=None, description="The height (in pixels) of the cropped image.")
    left: int | None = Field(
        default=None, description="The number of pixels from the left of the image where the crop should begin."
    )
    top: int | None = Field(
        default=None, description="The number of pixels from the top of the image where the crop should begin."
    )
    width: int | None = Field(default=None, description="The width (in pixels) of the cropped image.")


class SBCreateImage(StrictModel):
    assetId: str = Field(description="The asset library ID associated with the image asset.")
    assetVersion: str = Field(description="The asset library version associated with the image asset.")
    formatProperties: list[SBCreateFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class SBCreateLandingPageAsins(StrictModel):
    asins: list[str] = Field(
        min_length=1,
        max_length=100,
        description="For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.",
    )


class SBCreateManualCollectionSettings(StrictModel):
    """Settings for manually curated collections."""

    landingPage: SBCreateCollectionLandingPage
    productInclusions: list[SBCreateAdvertisedProducts] = Field(
        min_length=3, max_length=10, description="The products featured in the ad. Required for manual collections."
    )
    sharedSettings: SBCreateSharedCollectionSettings
    title: str | None = Field(
        default=None, description="Optional title for the collection. If not provided, title will be auto-generated."
    )


class SBCreateProductCollectionLandingPage(StrictModel):
    landingPageAsins: SBCreateLandingPageAsins | None = Field(default=None)
    landingPageType: SBProductCollectionLandingPageType
    landingPageUrl: str | None = Field(
        default=None, description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST"
    )


class SBCreateProductCollectionSettings(StrictModel):
    """An ad creative that contains multiple products and a custom image."""

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] = Field(
        min_length=1, max_length=2, description="The brand logo image assets to be used in the ad."
    )
    creativePropertiesToOptimize: list[SBProductCollectionCreativePropertiesToOptimize] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    customImages: list[SBCreateImage] = Field(
        min_length=1, max_length=5, description="The set of custom images featured in the ad."
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] = Field(
        min_length=1,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SBCreateProductCollectionLandingPage
    products: list[SBCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=3, description="The products featured in the ad."
    )


class SBCreateProductVideoSettings(StrictModel):
    """An ad with a creative that includes a video."""

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] | None = Field(
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
    landingPage: SBCreateVideoLandingPage | None = Field(default=None)
    products: list[SBCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=3, description="The products featured in the video ad."
    )
    videos: list[SBCreateVideo] = Field(min_length=1, max_length=1, description="The video assets used in the ad.")


class SBCreateSharedCollectionSettings(StrictModel):
    """Settings shared by all collection types."""

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: SBCreateImage | None = Field(default=None)


class SBCreateStoreSpotlightLandingPage(StrictModel):
    landingPageType: SBStoreSpotlightLandingPageType
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SBCreateStoreSpotlightSettings(StrictModel):
    """An ad creative that contains ASINs within a brand Store."""

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] = Field(
        min_length=1, max_length=1, description="The brand logo image assets to be used in the ad."
    )
    cards: list[SBCreateCardCreativeElement] = Field(
        min_length=3,
        max_length=3,
        description="The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.",
    )
    creativePropertiesToOptimize: list[SBStoreSpotlightCreativePropertiesToOptimize] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] = Field(
        min_length=1,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SBCreateStoreSpotlightLandingPage


class SBCreateVideo(StrictModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class SBCreateVideoLandingPage(StrictModel):
    landingPageType: SBVideoLandingPageType
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class SBCreative(LenientModel):
    componentCreative: SBComponentCreative


class SBCreativeStatus(LenientModel):
    moderationStatus: SBModerationStatus | str


class SBDeleteAdRequest(StrictModel):
    adIds: list[str] = Field(min_length=1, max_length=10)


class SBFormatProperties(LenientModel):
    height: int | None = Field(default=None, description="The height (in pixels) of the cropped image.")
    left: int | None = Field(
        default=None, description="The number of pixels from the left of the image where the crop should begin."
    )
    top: int | None = Field(
        default=None, description="The number of pixels from the top of the image where the crop should begin."
    )
    width: int | None = Field(default=None, description="The width (in pixels) of the cropped image.")


class SBImage(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the image asset.")
    assetVersion: str = Field(description="The asset library version associated with the image asset.")
    formatProperties: list[SBFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class SBLandingPageAsins(LenientModel):
    asins: list[str] = Field(
        min_length=1,
        max_length=100,
        description="For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.",
    )


class SBManualCollectionSettings(LenientModel):
    """Settings for manually curated collections."""

    landingPage: SBCollectionLandingPage
    productInclusions: list[SBAdvertisedProducts] = Field(
        min_length=3, max_length=10, description="The products featured in the ad. Required for manual collections."
    )
    sharedSettings: SBSharedCollectionSettings
    title: str | None = Field(
        default=None, description="Optional title for the collection. If not provided, title will be auto-generated."
    )


class SBProductCollectionLandingPage(LenientModel):
    landingPageAsins: SBLandingPageAsins | None = Field(default=None)
    landingPageType: SBProductCollectionLandingPageType | str
    landingPageUrl: str | None = Field(
        default=None, description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST"
    )


class SBProductCollectionSettings(LenientModel):
    """An ad creative that contains multiple products and a custom image."""

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBImage] = Field(
        min_length=1, max_length=2, description="The brand logo image assets to be used in the ad."
    )
    creativePropertiesToOptimize: list[SBProductCollectionCreativePropertiesToOptimize | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    customImages: list[SBImage] = Field(
        min_length=1, max_length=5, description="The set of custom images featured in the ad."
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] = Field(
        min_length=1,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SBProductCollectionLandingPage
    moderationStatus: SBCreativeStatus | None = Field(default=None)
    products: list[SBAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=3, description="The products featured in the ad."
    )
    untranslatedHeadlines: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="The headlines entered by the advertiser."
    )


class SBProductVideoSettings(LenientModel):
    """An ad with a creative that includes a video."""

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: list[SBImage] | None = Field(
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
    landingPage: SBVideoLandingPage | None = Field(default=None)
    moderationStatus: SBCreativeStatus | None = Field(default=None)
    products: list[SBAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=3, description="The products featured in the video ad."
    )
    untranslatedHeadlines: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="The headline entered by the advertiser."
    )
    untranslatedVideos: list[SBVideo] = Field(
        min_length=1, max_length=2, description="The original video assets submitted as part of the creative."
    )
    videos: list[SBVideo] = Field(min_length=1, max_length=1, description="The video assets used in the ad.")


class SBQueryAdRequest(StrictModel):
    adGroupIdFilter: SBAdAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SBAdAdIdFilter | None = Field(default=None)
    adProductFilter: SBAdAdProductFilter
    campaignIdFilter: SBAdCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SBAdNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SBAdStateFilter | None = Field(default=None)


class SBSharedCollectionSettings(LenientModel):
    """Settings shared by all collection types."""

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: SBImage | None = Field(default=None)
    moderationStatus: SBCreativeStatus | None = Field(default=None)


class SBStoreSpotlightLandingPage(LenientModel):
    landingPageType: SBStoreSpotlightLandingPageType | str
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SBStoreSpotlightSettings(LenientModel):
    """An ad creative that contains ASINs within a brand Store."""

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBImage] = Field(
        min_length=1, max_length=1, description="The brand logo image assets to be used in the ad."
    )
    cards: list[SBCardCreativeElement] = Field(
        min_length=3,
        max_length=3,
        description="The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.",
    )
    creativePropertiesToOptimize: list[SBStoreSpotlightCreativePropertiesToOptimize | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] = Field(
        min_length=1,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SBStoreSpotlightLandingPage
    moderationStatus: SBCreativeStatus | None = Field(default=None)
    untranslatedHeadlines: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="The headline entered by the advertiser."
    )


class SBUpdateAdRequest(StrictModel):
    ads: list[SBAdUpdate] = Field(min_length=1, max_length=10)


class SBUpdateAutoCollectionSettings(StrictModel):
    """Settings for automatically generated collections."""

    productExclusions: list[SBCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1000, description="Products to exclude from auto collection."
    )
    sharedSettings: SBUpdateSharedCollectionSettings | None = Field(default=None)


class SBUpdateBrandGallerySettings(StrictModel):
    """An ad creative that showcases a brand and its categories and collections."""

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] | None = Field(
        default=None, min_length=1, max_length=1, description="The brand logo image assets to be used in the ad."
    )
    cards: list[SBCreateBrandGalleryCardCreativeElement] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The sub-elements of the creative. Each card highlights a different category associated to a brand.",
    )
    creativePropertiesToOptimize: list[SBBrandGalleryCreativePropertiesToOptimize] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    customImages: list[SBCreateImage] | None = Field(
        default=None, min_length=0, max_length=1, description="The custom images featured in the ad."
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SBUpdateStoreSpotlightLandingPage | None = Field(default=None)


class SBUpdateCollectionLandingPage(StrictModel):
    landingPageType: SBCollectionLandingPageType | None = Field(default=None)
    landingPageUrl: str | None = Field(default=None, description="The URL associated to the landing page.")


class SBUpdateComponentCreative(StrictModel):
    autoCollectionSettings: SBUpdateAutoCollectionSettings | None = Field(default=None)
    brandGallerySettings: SBUpdateBrandGallerySettings | None = Field(default=None)
    manualCollectionSettings: SBUpdateManualCollectionSettings | None = Field(default=None)
    productCollectionSettings: SBUpdateProductCollectionSettings | None = Field(default=None)
    productVideoSettings: SBUpdateProductVideoSettings | None = Field(default=None)
    storeSpotlightSettings: SBUpdateStoreSpotlightSettings | None = Field(default=None)


class SBUpdateCreative(StrictModel):
    componentCreative: SBUpdateComponentCreative


class SBUpdateImage(StrictModel):
    assetId: str | None = Field(default=None, description="The asset library ID associated with the image asset.")
    assetVersion: str | None = Field(
        default=None, description="The asset library version associated with the image asset."
    )
    formatProperties: list[SBCreateFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class SBUpdateLandingPageAsins(StrictModel):
    asins: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.",
    )


class SBUpdateManualCollectionSettings(StrictModel):
    """Settings for manually curated collections."""

    landingPage: SBUpdateCollectionLandingPage | None = Field(default=None)
    productInclusions: list[SBCreateAdvertisedProducts] | None = Field(
        default=None,
        min_length=3,
        max_length=10,
        description="The products featured in the ad. Required for manual collections.",
    )
    sharedSettings: SBUpdateSharedCollectionSettings | None = Field(default=None)
    title: str | None = Field(
        default=None, description="Optional title for the collection. If not provided, title will be auto-generated."
    )


class SBUpdateProductCollectionLandingPage(StrictModel):
    landingPageAsins: SBUpdateLandingPageAsins | None = Field(default=None)
    landingPageType: SBProductCollectionLandingPageType | None = Field(default=None)
    landingPageUrl: str | None = Field(
        default=None, description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST"
    )


class SBUpdateProductCollectionSettings(StrictModel):
    """An ad creative that contains multiple products and a custom image."""

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] | None = Field(
        default=None, min_length=1, max_length=2, description="The brand logo image assets to be used in the ad."
    )
    creativePropertiesToOptimize: list[SBProductCollectionCreativePropertiesToOptimize] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    customImages: list[SBCreateImage] | None = Field(
        default=None, min_length=1, max_length=5, description="The set of custom images featured in the ad."
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SBUpdateProductCollectionLandingPage | None = Field(default=None)
    products: list[SBCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=3, description="The products featured in the ad."
    )


class SBUpdateProductVideoSettings(StrictModel):
    """An ad with a creative that includes a video."""

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] | None = Field(
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
    landingPage: SBUpdateVideoLandingPage | None = Field(default=None)
    products: list[SBCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=3, description="The products featured in the video ad."
    )
    videos: list[SBCreateVideo] | None = Field(
        default=None, min_length=1, max_length=1, description="The video assets used in the ad."
    )


class SBUpdateSharedCollectionSettings(StrictModel):
    """Settings shared by all collection types."""

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: SBUpdateImage | None = Field(default=None)


class SBUpdateStoreSpotlightLandingPage(StrictModel):
    landingPageType: SBStoreSpotlightLandingPageType | None = Field(default=None)
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class SBUpdateStoreSpotlightSettings(StrictModel):
    """An ad creative that contains ASINs within a brand Store."""

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] | None = Field(
        default=None, min_length=1, max_length=1, description="The brand logo image assets to be used in the ad."
    )
    cards: list[SBCreateCardCreativeElement] | None = Field(
        default=None,
        min_length=3,
        max_length=3,
        description="The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.",
    )
    creativePropertiesToOptimize: list[SBStoreSpotlightCreativePropertiesToOptimize] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    enableCreativeAutoTranslation: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.",
    )
    headlines: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.",
    )
    landingPage: SBUpdateStoreSpotlightLandingPage | None = Field(default=None)


class SBUpdateVideoLandingPage(StrictModel):
    landingPageType: SBVideoLandingPageType | None = Field(default=None)
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class SBVideo(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class SBVideoLandingPage(LenientModel):
    landingPageType: SBVideoLandingPageType | str
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


__all__ = [
    "SBAd",
    "SBAdAdGroupIdFilter",
    "SBAdAdIdFilter",
    "SBAdAdProductFilter",
    "SBAdCampaignIdFilter",
    "SBAdCreate",
    "SBAdMultiStatusResponse",
    "SBAdMultiStatusSuccess",
    "SBAdNameFilter",
    "SBAdNameFilterType",
    "SBAdProduct",
    "SBAdStateFilter",
    "SBAdSuccessResponse",
    "SBAdType",
    "SBAdUpdate",
    "SBAdvertisedProducts",
    "SBAutoCollectionSettings",
    "SBBrandGalleryCardCreativeElement",
    "SBBrandGalleryCreativePropertiesToOptimize",
    "SBBrandGallerySettings",
    "SBCardCreativeElement",
    "SBCollectionLandingPage",
    "SBCollectionLandingPageType",
    "SBComponentCreative",
    "SBCreateAdRequest",
    "SBCreateAdvertisedProducts",
    "SBCreateAutoCollectionSettings",
    "SBCreateBrandGalleryCardCreativeElement",
    "SBCreateBrandGallerySettings",
    "SBCreateCardCreativeElement",
    "SBCreateCollectionLandingPage",
    "SBCreateComponentCreative",
    "SBCreateCreative",
    "SBCreateFormatProperties",
    "SBCreateImage",
    "SBCreateLandingPageAsins",
    "SBCreateManualCollectionSettings",
    "SBCreateProductCollectionLandingPage",
    "SBCreateProductCollectionSettings",
    "SBCreateProductVideoSettings",
    "SBCreateSharedCollectionSettings",
    "SBCreateState",
    "SBCreateStoreSpotlightLandingPage",
    "SBCreateStoreSpotlightSettings",
    "SBCreateTag",
    "SBCreateVideo",
    "SBCreateVideoLandingPage",
    "SBCreative",
    "SBCreativeStatus",
    "SBDeleteAdRequest",
    "SBDeliveryReason",
    "SBDeliveryStatus",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBFormatProperties",
    "SBImage",
    "SBLandingPageAsins",
    "SBManualCollectionSettings",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBModerationStatus",
    "SBProductCollectionCreativePropertiesToOptimize",
    "SBProductCollectionLandingPage",
    "SBProductCollectionLandingPageType",
    "SBProductCollectionSettings",
    "SBProductIdType",
    "SBProductVideoSettings",
    "SBQueryAdRequest",
    "SBSharedCollectionSettings",
    "SBState",
    "SBStatus",
    "SBStoreSpotlightCreativePropertiesToOptimize",
    "SBStoreSpotlightLandingPage",
    "SBStoreSpotlightLandingPageType",
    "SBStoreSpotlightSettings",
    "SBTag",
    "SBUpdateAdRequest",
    "SBUpdateAutoCollectionSettings",
    "SBUpdateBrandGallerySettings",
    "SBUpdateCollectionLandingPage",
    "SBUpdateComponentCreative",
    "SBUpdateCreative",
    "SBUpdateImage",
    "SBUpdateLandingPageAsins",
    "SBUpdateManualCollectionSettings",
    "SBUpdateProductCollectionLandingPage",
    "SBUpdateProductCollectionSettings",
    "SBUpdateProductVideoSettings",
    "SBUpdateSharedCollectionSettings",
    "SBUpdateState",
    "SBUpdateStoreSpotlightLandingPage",
    "SBUpdateStoreSpotlightSettings",
    "SBUpdateVideoLandingPage",
    "SBVideo",
    "SBVideoLandingPage",
    "SBVideoLandingPageType",
]
