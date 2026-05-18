"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from enum import StrEnum

if TYPE_CHECKING:
    from amazon_ads_sdk.errors import ErrorsIndex
    from .enums import (
        SBAdProduct,
        SBCreateState,
        SBMarketplace,
        SBMarketplaceScope,
        SBProductIdType,
        SBState,
        SBUpdateState,
    )
    from .shared import SBCreateTag, SBStatus, SBTag


class SBAd(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    activeCreative: SBCreative | None = None
    adGroupId: str  # The ad group associated with the ad.
    adId: str  # The identifier of the ad.
    adProduct: SBAdProduct
    adType: SBAdType
    campaignId: str  # The campaign associated with the ad. It's a read-only field.
    creationDateTime: datetime  # The date time that the ad was created.
    creative: SBCreative
    lastUpdatedDateTime: datetime  # The date time that the ad was last updated.
    marketplaceScope: SBMarketplaceScope
    marketplaces: list[
        SBMarketplace
    ]  # The list of country codes representing amazon marketplaces in which the global ad is applicable. The marketplaces included should either be same as or subset of parent ad group
    name: str  # The name of the ad.
    state: SBState
    status: SBStatus | None = None
    tags: list[SBTag] | None = None  # Open ended labels with a key value pair applied to the ad


class SBAdAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdAdIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SBAdProduct
    ]  # AdProduct Description `SPONSORED_BRANDS` Sponsored Brands ad product.


class SBAdCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adProduct: SBAdProduct
    adType: SBAdType
    creative: SBCreateCreative
    name: str  # The name of the ad.
    state: SBCreateState
    tags: list[SBCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the ad
    )


class SBAdMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBAdMultiStatusSuccess] | None = None


class SBAdMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ad: SBAd
    index: int


class SBAdNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: SBAdNameFilterType


class SBAdNameFilterType(StrEnum):
    """| AdNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBAdStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SBState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SBAdSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SBAd] | None = None
    nextToken: str | None = None


class SBAdType(StrEnum):
    """| AdType | Description |
    |------|------|
    | `COMPONENT` | A creative that can features a collection of videos, images, and products. |
    """

    COMPONENT = "COMPONENT"


class SBAdUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adId: str  # The identifier of the ad.
    creative: SBUpdateCreative | None = None
    name: str | None = None  # The name of the ad.
    state: SBUpdateState | None = None
    tags: list[SBCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the ad
    )


class SBAdvertisedProducts(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productId: str | None = None  # The identifier of the advertised product.
    productIdType: SBProductIdType


class SBAutoCollectionSettings(BaseModel):
    """Settings for automatically generated collections."""

    model_config = ConfigDict(extra="forbid")

    productExclusions: list[SBAdvertisedProducts] | None = (
        None  # Products to exclude from auto collection.
    )
    sharedSettings: SBSharedCollectionSettings


class SBCardCreativeElement(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    headline: str  # The headline used for the card.
    landingPage: SBStoreSpotlightLandingPage
    products: SBAdvertisedProducts


class SBCollectionLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SBCollectionLandingPageType
    landingPageUrl: str | None = None  # The URL associated to the landing page.


class SBCollectionLandingPageType(StrEnum):
    """| CollectionLandingPageType | Description |
    |------|------|
    | `ASIN_LIST` | A list of products based on the products promoted in the ad creative. |
    | `STORE` | A brand Store landing page. |
    """

    ASIN_LIST = "ASIN_LIST"
    STORE = "STORE"


class SBComponentCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    autoCollectionSettings: SBAutoCollectionSettings | None = None
    manualCollectionSettings: SBManualCollectionSettings | None = None
    productCollectionSettings: SBProductCollectionSettings | None = None
    productVideoSettings: SBProductVideoSettings | None = None
    storeSpotlightSettings: SBStoreSpotlightSettings | None = None


class SBCreateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SBAdCreate] | None = None


class SBCreateAdvertisedProducts(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productId: str | None = None  # The identifier of the advertised product.
    productIdType: SBProductIdType


class SBCreateAutoCollectionSettings(BaseModel):
    """Settings for automatically generated collections."""

    model_config = ConfigDict(extra="forbid")

    productExclusions: list[SBCreateAdvertisedProducts] | None = (
        None  # Products to exclude from auto collection.
    )
    sharedSettings: SBCreateSharedCollectionSettings


class SBCreateCardCreativeElement(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    headline: str  # The headline used for the card.
    landingPage: SBCreateStoreSpotlightLandingPage
    products: SBCreateAdvertisedProducts


class SBCreateCollectionLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SBCollectionLandingPageType
    landingPageUrl: str | None = None  # The URL associated to the landing page.


class SBCreateComponentCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    autoCollectionSettings: SBCreateAutoCollectionSettings | None = None
    manualCollectionSettings: SBCreateManualCollectionSettings | None = None
    productCollectionSettings: SBCreateProductCollectionSettings | None = None
    productVideoSettings: SBCreateProductVideoSettings | None = None
    storeSpotlightSettings: SBCreateStoreSpotlightSettings | None = None


class SBCreateCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    componentCreative: SBCreateComponentCreative | None = None


class SBCreateFormatProperties(BaseModel):
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


class SBCreateImage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the image asset.
    assetVersion: str  # The asset library version associated with the image asset.
    formatProperties: list[SBCreateFormatProperties] | None = (
        None  # The cropping and positioning properties associated with the asset.
    )


class SBCreateLandingPageAsins(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    asins: list[
        str
    ]  # For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.


class SBCreateManualCollectionSettings(BaseModel):
    """Settings for manually curated collections."""

    model_config = ConfigDict(extra="forbid")

    landingPage: SBCreateCollectionLandingPage
    productInclusions: list[
        SBCreateAdvertisedProducts
    ]  # The products featured in the ad. Required for manual collections.
    sharedSettings: SBCreateSharedCollectionSettings


class SBCreateProductCollectionLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageAsins: SBCreateLandingPageAsins | None = None
    landingPageType: SBProductCollectionLandingPageType
    landingPageUrl: str | None = (
        None  # The URL associated to the landing page. Read only if landingPageType is ASIN_LIST
    )


class SBCreateProductCollectionSettings(BaseModel):
    """An ad creative that contains multiple products and a custom image."""

    model_config = ConfigDict(extra="forbid")

    brand: str  # The name of the brand being advertised.
    brandLogos: list[SBCreateImage]  # The brand logo image assets to be used in the ad.
    creativePropertiesToOptimize: list[SBProductCollectionCreativePropertiesToOptimize] | None = (
        None  # The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.
    )
    customImages: list[SBCreateImage]  # The set of custom images featured in the ad.
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[
        str
    ]  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    landingPage: SBCreateProductCollectionLandingPage
    products: list[SBCreateAdvertisedProducts] | None = None  # The products featured in the ad.


class SBCreateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")

    brand: str | None = None  # The name of the brand being advertised.
    brandLogos: list[SBCreateImage] | None = (
        None  # The brand logo image assets to be used in the ad.
    )
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[str] | None = (
        None  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    )
    landingPage: SBCreateVideoLandingPage | None = None
    products: list[SBCreateAdvertisedProducts] | None = (
        None  # The products featured in the video ad.
    )
    videos: list[SBCreateVideo]  # The video assets used in the ad.


class SBCreateSharedCollectionSettings(BaseModel):
    """Settings shared by all collection types."""

    model_config = ConfigDict(extra="forbid")

    brand: str  # The name of the brand being advertised.
    brandLogos: SBCreateImage | None = None


class SBCreateStoreSpotlightLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SBStoreSpotlightLandingPageType
    landingPageUrl: str  # The URL of landing page where the ad directs.


class SBCreateStoreSpotlightSettings(BaseModel):
    """An ad creative that contains ASINs within a brand Store."""

    model_config = ConfigDict(extra="forbid")

    brand: str  # The name of the brand being advertised.
    brandLogos: list[SBCreateImage]  # The brand logo image assets to be used in the ad.
    cards: list[
        SBCreateCardCreativeElement
    ]  # The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.
    creativePropertiesToOptimize: list[SBStoreSpotlightCreativePropertiesToOptimize] | None = (
        None  # The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.
    )
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[
        str
    ]  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    landingPage: SBCreateStoreSpotlightLandingPage


class SBCreateVideo(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.


class SBCreateVideoLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SBVideoLandingPageType
    landingPageUrl: str | None = None  # The URL of landing page where the ad directs.


class SBCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    componentCreative: SBComponentCreative | None = None


class SBCreativeStatus(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    moderationStatus: SBModerationStatus


class SBDeleteAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adIds: list[str] | None = None


class SBFormatProperties(BaseModel):
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


class SBImage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the image asset.
    assetVersion: str  # The asset library version associated with the image asset.
    formatProperties: list[SBFormatProperties] | None = (
        None  # The cropping and positioning properties associated with the asset.
    )


class SBLandingPageAsins(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    asins: list[
        str
    ]  # For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.


class SBManualCollectionSettings(BaseModel):
    """Settings for manually curated collections."""

    model_config = ConfigDict(extra="forbid")

    landingPage: SBCollectionLandingPage
    productInclusions: list[
        SBAdvertisedProducts
    ]  # The products featured in the ad. Required for manual collections.
    sharedSettings: SBSharedCollectionSettings


class SBModerationStatus(StrEnum):
    """| ModerationStatus | Description |
    |------|------|
    | `APPROVED_WITH_EXCEPTIONS` | The creative passed basic moderation but was found to be invalid for some supplies. The creative is serving on approved supplies. |
    | `PENDING_TRANSLATION` | The creative is pending creative Translations. |
    | `PUBLISHED` | The creative passed moderation and is serving. |
    | `REJECTED_BY_MODERATION` | The creative was rejected during the moderation process. |
    | `SUBMITTED_FOR_MODERATION` | The creative has been submitted, but has not yet been reviewed. |
    """

    APPROVED_WITH_EXCEPTIONS = "APPROVED_WITH_EXCEPTIONS"
    PENDING_TRANSLATION = "PENDING_TRANSLATION"
    PUBLISHED = "PUBLISHED"
    REJECTED_BY_MODERATION = "REJECTED_BY_MODERATION"
    SUBMITTED_FOR_MODERATION = "SUBMITTED_FOR_MODERATION"


class SBProductCollectionCreativePropertiesToOptimize(StrEnum):
    """| ProductCollectionCreativePropertiesToOptimize | Description |
    |------|------|
    | `HEADLINE` | The headline in the creative. |
    """

    HEADLINE = "HEADLINE"


class SBProductCollectionLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageAsins: SBLandingPageAsins | None = None
    landingPageType: SBProductCollectionLandingPageType
    landingPageUrl: str | None = (
        None  # The URL associated to the landing page. Read only if landingPageType is ASIN_LIST
    )


class SBProductCollectionLandingPageType(StrEnum):
    """| ProductCollectionLandingPageType | Description |
    |------|------|
    | `ASIN_LIST` | A list of products based on the products promoted in the ad creative. |
    | `CUSTOM_URL` | A custom landing page. Available for vendors only. |
    | `STORE` | A brand Store landing page. |
    """

    ASIN_LIST = "ASIN_LIST"
    CUSTOM_URL = "CUSTOM_URL"
    STORE = "STORE"


class SBProductCollectionSettings(BaseModel):
    """An ad creative that contains multiple products and a custom image."""

    model_config = ConfigDict(extra="forbid")

    brand: str  # The name of the brand being advertised.
    brandLogos: list[SBImage]  # The brand logo image assets to be used in the ad.
    creativePropertiesToOptimize: list[SBProductCollectionCreativePropertiesToOptimize] | None = (
        None  # The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.
    )
    customImages: list[SBImage]  # The set of custom images featured in the ad.
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[
        str
    ]  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    landingPage: SBProductCollectionLandingPage
    moderationStatus: SBCreativeStatus | None = None
    products: list[SBAdvertisedProducts] | None = None  # The products featured in the ad.
    untranslatedHeadlines: list[str] | None = None  # The headlines entered by the advertiser.


class SBProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")

    brand: str | None = None  # The name of the brand being advertised.
    brandLogos: list[SBImage] | None = None  # The brand logo image assets to be used in the ad.
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[str] | None = (
        None  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    )
    landingPage: SBVideoLandingPage | None = None
    moderationStatus: SBCreativeStatus | None = None
    products: list[SBAdvertisedProducts] | None = None  # The products featured in the video ad.
    untranslatedHeadlines: list[str] | None = None  # The headline entered by the advertiser.
    untranslatedVideos: list[
        SBVideo
    ]  # The original video assets submitted as part of the creative.
    videos: list[SBVideo]  # The video assets used in the ad.


class SBQueryAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SBAdAdGroupIdFilter | None = None
    adIdFilter: SBAdAdIdFilter | None = None
    adProductFilter: SBAdAdProductFilter
    campaignIdFilter: SBAdCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SBAdNameFilter | None = None
    nextToken: str | None = None
    stateFilter: SBAdStateFilter | None = None


class SBSharedCollectionSettings(BaseModel):
    """Settings shared by all collection types."""

    model_config = ConfigDict(extra="forbid")

    brand: str  # The name of the brand being advertised.
    brandLogos: SBImage | None = None
    moderationStatus: SBCreativeStatus | None = None


class SBStoreSpotlightCreativePropertiesToOptimize(StrEnum):
    """| StoreSpotlightCreativePropertiesToOptimize | Description |
    |------|------|
    | `HEADLINE` | The headline in the creative. |
    """

    HEADLINE = "HEADLINE"


class SBStoreSpotlightLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SBStoreSpotlightLandingPageType
    landingPageUrl: str  # The URL of landing page where the ad directs.


class SBStoreSpotlightLandingPageType(StrEnum):
    """| StoreSpotlightLandingPageType | Description |
    |------|------|
    | `STORE` | A brand Store landing page. |
    """

    STORE = "STORE"


class SBStoreSpotlightSettings(BaseModel):
    """An ad creative that contains ASINs within a brand Store."""

    model_config = ConfigDict(extra="forbid")

    brand: str  # The name of the brand being advertised.
    brandLogos: list[SBImage]  # The brand logo image assets to be used in the ad.
    cards: list[
        SBCardCreativeElement
    ]  # The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.
    creativePropertiesToOptimize: list[SBStoreSpotlightCreativePropertiesToOptimize] | None = (
        None  # The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.
    )
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[
        str
    ]  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    landingPage: SBStoreSpotlightLandingPage
    moderationStatus: SBCreativeStatus | None = None
    untranslatedHeadlines: list[str] | None = None  # The headline entered by the advertiser.


class SBUpdateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SBAdUpdate] | None = None


class SBUpdateAutoCollectionSettings(BaseModel):
    """Settings for automatically generated collections."""

    model_config = ConfigDict(extra="forbid")

    productExclusions: list[SBCreateAdvertisedProducts] | None = (
        None  # Products to exclude from auto collection.
    )
    sharedSettings: SBUpdateSharedCollectionSettings | None = None


class SBUpdateCollectionLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SBCollectionLandingPageType | None = None
    landingPageUrl: str | None = None  # The URL associated to the landing page.


class SBUpdateComponentCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    autoCollectionSettings: SBUpdateAutoCollectionSettings | None = None
    manualCollectionSettings: SBUpdateManualCollectionSettings | None = None
    productCollectionSettings: SBUpdateProductCollectionSettings | None = None
    productVideoSettings: SBUpdateProductVideoSettings | None = None
    storeSpotlightSettings: SBUpdateStoreSpotlightSettings | None = None


class SBUpdateCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    componentCreative: SBUpdateComponentCreative | None = None


class SBUpdateImage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetId: str | None = None  # The asset library ID associated with the image asset.
    assetVersion: str | None = None  # The asset library version associated with the image asset.
    formatProperties: list[SBCreateFormatProperties] | None = (
        None  # The cropping and positioning properties associated with the asset.
    )


class SBUpdateLandingPageAsins(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    asins: list[str] | None = (
        None  # For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.
    )


class SBUpdateManualCollectionSettings(BaseModel):
    """Settings for manually curated collections."""

    model_config = ConfigDict(extra="forbid")

    landingPage: SBUpdateCollectionLandingPage | None = None
    productInclusions: list[SBCreateAdvertisedProducts] | None = (
        None  # The products featured in the ad. Required for manual collections.
    )
    sharedSettings: SBUpdateSharedCollectionSettings | None = None


class SBUpdateProductCollectionLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageAsins: SBUpdateLandingPageAsins | None = None
    landingPageType: SBProductCollectionLandingPageType | None = None
    landingPageUrl: str | None = (
        None  # The URL associated to the landing page. Read only if landingPageType is ASIN_LIST
    )


class SBUpdateProductCollectionSettings(BaseModel):
    """An ad creative that contains multiple products and a custom image."""

    model_config = ConfigDict(extra="forbid")

    brand: str | None = None  # The name of the brand being advertised.
    brandLogos: list[SBCreateImage] | None = (
        None  # The brand logo image assets to be used in the ad.
    )
    creativePropertiesToOptimize: list[SBProductCollectionCreativePropertiesToOptimize] | None = (
        None  # The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.
    )
    customImages: list[SBCreateImage] | None = None  # The set of custom images featured in the ad.
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[str] | None = (
        None  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    )
    landingPage: SBUpdateProductCollectionLandingPage | None = None
    products: list[SBCreateAdvertisedProducts] | None = None  # The products featured in the ad.


class SBUpdateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")

    brand: str | None = None  # The name of the brand being advertised.
    brandLogos: list[SBCreateImage] | None = (
        None  # The brand logo image assets to be used in the ad.
    )
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[str] | None = (
        None  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    )
    landingPage: SBUpdateVideoLandingPage | None = None
    products: list[SBCreateAdvertisedProducts] | None = (
        None  # The products featured in the video ad.
    )
    videos: list[SBCreateVideo] | None = None  # The video assets used in the ad.


class SBUpdateSharedCollectionSettings(BaseModel):
    """Settings shared by all collection types."""

    model_config = ConfigDict(extra="forbid")

    brand: str | None = None  # The name of the brand being advertised.
    brandLogos: SBUpdateImage | None = None


class SBUpdateStoreSpotlightLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SBStoreSpotlightLandingPageType | None = None
    landingPageUrl: str | None = None  # The URL of landing page where the ad directs.


class SBUpdateStoreSpotlightSettings(BaseModel):
    """An ad creative that contains ASINs within a brand Store."""

    model_config = ConfigDict(extra="forbid")

    brand: str | None = None  # The name of the brand being advertised.
    brandLogos: list[SBCreateImage] | None = (
        None  # The brand logo image assets to be used in the ad.
    )
    cards: list[SBCreateCardCreativeElement] | None = (
        None  # The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.
    )
    creativePropertiesToOptimize: list[SBStoreSpotlightCreativePropertiesToOptimize] | None = (
        None  # The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.
    )
    enableCreativeAutoTranslation: bool | None = (
        None  # If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation.
    )
    headlines: list[str] | None = (
        None  # The headline submitted as part of the ad creative. During your campaign, Amazon will optimize amongst the headlines you provide to match customer intent.
    )
    landingPage: SBUpdateStoreSpotlightLandingPage | None = None


class SBUpdateVideoLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SBVideoLandingPageType | None = None
    landingPageUrl: str | None = None  # The URL of landing page where the ad directs.


class SBVideo(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.


class SBVideoLandingPage(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    landingPageType: SBVideoLandingPageType
    landingPageUrl: str | None = None  # The URL of landing page where the ad directs.


class SBVideoLandingPageType(StrEnum):
    """| VideoLandingPageType | Description |
    |------|------|
    | `DETAIL_PAGE` | A product detail page. |
    | `STORE` | A brand Store landing page. |
    """

    DETAIL_PAGE = "DETAIL_PAGE"
    STORE = "STORE"
