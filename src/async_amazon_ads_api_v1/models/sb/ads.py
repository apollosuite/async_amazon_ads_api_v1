"""Auto-generated models for Ads from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import (
    SBAdProduct,
    SBCreateState,
    SBDeliveryReason,
    SBDeliveryStatus,
    SBErrorCode,
    SBMarketplace,
    SBMarketplaceScope,
    SBProductIdType,
    SBState,
    SBUpdateState,
)
from .shared import SBCreateTag, SBErrorsIndex, SBStatus, SBTag


class SBAdNameFilterType(StrEnum):
    """
    **AdNameFilterType Enum:**
    | AdNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBAdType(StrEnum):
    """
    **AdType Enum:**

    | AdType | Description |
    |------|------|
    | `COMPONENT` | A creative that can features a collection of videos, images, and products. |
    """

    COMPONENT = "COMPONENT"


class SBBrandGalleryCreativePropertiesToOptimize(StrEnum):
    """
    **BrandGalleryCreativePropertiesToOptimize Enum:**

    | BrandGalleryCreativePropertiesToOptimize | Description |
    |------|------|
    | `HEADLINE` | The headline in the creative. |
    """

    HEADLINE = "HEADLINE"


class SBCollectionLandingPageType(StrEnum):
    """
    **CollectionLandingPageType Enum:**

    | CollectionLandingPageType | Description |
    |------|------|
    | `ASIN_LIST` | A list of products based on the products promoted in the ad creative. |
    | `STORE` | A brand Store landing page. |
    """

    ASIN_LIST = "ASIN_LIST"
    STORE = "STORE"


class SBModerationStatus(StrEnum):
    """
    **ModerationStatus Enum:**

    | ModerationStatus | Description |
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
    """
    **ProductCollectionCreativePropertiesToOptimize Enum:**

    | ProductCollectionCreativePropertiesToOptimize | Description |
    |------|------|
    | `HEADLINE` | The headline in the creative. |
    """

    HEADLINE = "HEADLINE"


class SBProductCollectionLandingPageType(StrEnum):
    """
    **ProductCollectionLandingPageType Enum:**

    | ProductCollectionLandingPageType | Description |
    |------|------|
    | `ASIN_LIST` | A list of products based on the products promoted in the ad creative. |
    | `CUSTOM_URL` | A custom landing page. Available for vendors only. |
    | `STORE` | A brand Store landing page. |
    """

    ASIN_LIST = "ASIN_LIST"
    CUSTOM_URL = "CUSTOM_URL"
    STORE = "STORE"


class SBStoreSpotlightCreativePropertiesToOptimize(StrEnum):
    """
    **StoreSpotlightCreativePropertiesToOptimize Enum:**

    | StoreSpotlightCreativePropertiesToOptimize | Description |
    |------|------|
    | `HEADLINE` | The headline in the creative. |
    """

    HEADLINE = "HEADLINE"


class SBStoreSpotlightLandingPageType(StrEnum):
    """
    **StoreSpotlightLandingPageType Enum:**

    | StoreSpotlightLandingPageType | Description |
    |------|------|
    | `STORE` | A brand Store landing page. |
    """

    STORE = "STORE"


class SBVideoLandingPageType(StrEnum):
    """
    **VideoLandingPageType Enum:**

    | VideoLandingPageType | Description |
    |------|------|
    | `DETAIL_PAGE` | A product detail page. |
    | `STORE` | A brand Store landing page. |
    """

    DETAIL_PAGE = "DETAIL_PAGE"
    STORE = "STORE"


class SBAd(BaseModel):
    model_config = ConfigDict(extra="allow")

    activeCreative: SBCreative | None = Field(default=None)
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The identifier of the ad.")
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    adType: Annotated[SBAdType | str, lenient_enum(SBAdType)]
    campaignId: str = Field(description="The campaign associated with the ad. It's a read-only field.")
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: SBCreative
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str = Field(description="The name of the ad.")
    state: Annotated[SBState | str, lenient_enum(SBState)]
    status: SBStatus | None = Field(default=None)
    tags: list[SBTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SBAdAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=10)


class SBAdAdIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=10)


class SBAdAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_BRANDS` | Sponsored Brands ad product. |
""",
    )


class SBAdCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=10)


class SBAdCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    adType: Annotated[SBAdType | str, lenient_enum(SBAdType)]
    creative: SBCreateCreative
    name: str = Field(description="The name of the ad.")
    state: Annotated[SBCreateState | str, lenient_enum(SBCreateState)]
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SBAdMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBAdMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    ad: SBAd
    index: int = Field(ge=0, le=9)


class SBAdNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=10)
    queryTermMatchType: Annotated[SBAdNameFilterType | str, lenient_enum(SBAdNameFilterType)]


class SBAdStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBState | str, lenient_enum(SBState)]] = Field(
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


class SBAdSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    ads: list[SBAd] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SBAdUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adId: str = Field(description="The identifier of the ad.")
    creative: SBUpdateCreative | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad.")
    state: Annotated[SBUpdateState | str, lenient_enum(SBUpdateState)] | None = Field(default=None)
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SBAdvertisedProducts(BaseModel):
    model_config = ConfigDict(extra="allow")

    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: Annotated[SBProductIdType | str, lenient_enum(SBProductIdType)]


class SBAutoCollectionSettings(BaseModel):
    """Settings for automatically generated collections."""

    model_config = ConfigDict(extra="allow")

    productExclusions: list[SBAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1000, description="Products to exclude from auto collection."
    )
    sharedSettings: SBSharedCollectionSettings


class SBBrandGalleryCardCreativeElement(BaseModel):
    model_config = ConfigDict(extra="allow")

    customImage: SBImage
    headline: str = Field(description="The headline used for the card.")
    landingPage: SBStoreSpotlightLandingPage


class SBBrandGallerySettings(BaseModel):
    """An ad creative that showcases a brand and its categories and collections."""

    model_config = ConfigDict(extra="allow")

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
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBBrandGalleryCreativePropertiesToOptimize | str,
                lenient_enum(SBBrandGalleryCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
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


class SBCardCreativeElement(BaseModel):
    model_config = ConfigDict(extra="allow")

    headline: str = Field(description="The headline used for the card.")
    landingPage: SBStoreSpotlightLandingPage
    products: SBAdvertisedProducts


class SBCollectionLandingPage(BaseModel):
    model_config = ConfigDict(extra="allow")

    landingPageType: Annotated[SBCollectionLandingPageType | str, lenient_enum(SBCollectionLandingPageType)]
    landingPageUrl: str | None = Field(default=None, description="The URL associated to the landing page.")


class SBComponentCreative(BaseModel):
    model_config = ConfigDict(extra="allow")

    autoCollectionSettings: SBAutoCollectionSettings | None = Field(default=None)
    brandGallerySettings: SBBrandGallerySettings | None = Field(default=None)
    manualCollectionSettings: SBManualCollectionSettings | None = Field(default=None)
    productCollectionSettings: SBProductCollectionSettings | None = Field(default=None)
    productVideoSettings: SBProductVideoSettings | None = Field(default=None)
    storeSpotlightSettings: SBStoreSpotlightSettings | None = Field(default=None)


class SBCreateAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ads: list[SBAdCreate] = Field(min_length=1, max_length=10)


class SBCreateAdvertisedProducts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: Annotated[SBProductIdType | str, lenient_enum(SBProductIdType)]


class SBCreateAutoCollectionSettings(BaseModel):
    """Settings for automatically generated collections."""

    model_config = ConfigDict(extra="forbid")

    productExclusions: list[SBCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1000, description="Products to exclude from auto collection."
    )
    sharedSettings: SBCreateSharedCollectionSettings


class SBCreateBrandGalleryCardCreativeElement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    customImage: SBCreateImage
    headline: str = Field(description="The headline used for the card.")
    landingPage: SBCreateStoreSpotlightLandingPage


class SBCreateBrandGallerySettings(BaseModel):
    """An ad creative that showcases a brand and its categories and collections."""

    model_config = ConfigDict(extra="forbid")

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
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBBrandGalleryCreativePropertiesToOptimize | str,
                lenient_enum(SBBrandGalleryCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
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


class SBCreateCardCreativeElement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    headline: str = Field(description="The headline used for the card.")
    landingPage: SBCreateStoreSpotlightLandingPage
    products: SBCreateAdvertisedProducts


class SBCreateCollectionLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageType: Annotated[SBCollectionLandingPageType | str, lenient_enum(SBCollectionLandingPageType)]
    landingPageUrl: str | None = Field(default=None, description="The URL associated to the landing page.")


class SBCreateComponentCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    autoCollectionSettings: SBCreateAutoCollectionSettings | None = Field(default=None)
    brandGallerySettings: SBCreateBrandGallerySettings | None = Field(default=None)
    manualCollectionSettings: SBCreateManualCollectionSettings | None = Field(default=None)
    productCollectionSettings: SBCreateProductCollectionSettings | None = Field(default=None)
    productVideoSettings: SBCreateProductVideoSettings | None = Field(default=None)
    storeSpotlightSettings: SBCreateStoreSpotlightSettings | None = Field(default=None)


class SBCreateCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    componentCreative: SBCreateComponentCreative | None = None


class SBCreateFormatProperties(BaseModel):
    model_config = ConfigDict(extra="forbid")

    height: int | None = Field(default=None, description="The height (in pixels) of the cropped image.")
    left: int | None = Field(
        default=None, description="The number of pixels from the left of the image where the crop should begin."
    )
    top: int | None = Field(
        default=None, description="The number of pixels from the top of the image where the crop should begin."
    )
    width: int | None = Field(default=None, description="The width (in pixels) of the cropped image.")


class SBCreateImage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetId: str = Field(description="The asset library ID associated with the image asset.")
    assetVersion: str = Field(description="The asset library version associated with the image asset.")
    formatProperties: list[SBCreateFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class SBCreateLandingPageAsins(BaseModel):
    model_config = ConfigDict(extra="forbid")

    asins: list[str] = Field(
        min_length=1,
        max_length=100,
        description="For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.",
    )


class SBCreateManualCollectionSettings(BaseModel):
    """Settings for manually curated collections."""

    model_config = ConfigDict(extra="forbid")

    landingPage: SBCreateCollectionLandingPage
    productInclusions: list[SBCreateAdvertisedProducts] = Field(
        min_length=3, max_length=10, description="The products featured in the ad. Required for manual collections."
    )
    sharedSettings: SBCreateSharedCollectionSettings
    title: str | None = Field(
        default=None, description="Optional title for the collection. If not provided, title will be auto-generated."
    )


class SBCreateProductCollectionLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageAsins: SBCreateLandingPageAsins | None = Field(default=None)
    landingPageType: Annotated[
        SBProductCollectionLandingPageType | str, lenient_enum(SBProductCollectionLandingPageType)
    ]
    landingPageUrl: str | None = Field(
        default=None, description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST"
    )


class SBCreateProductCollectionSettings(BaseModel):
    """An ad creative that contains multiple products and a custom image."""

    model_config = ConfigDict(extra="forbid")

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] = Field(
        min_length=1, max_length=2, description="The brand logo image assets to be used in the ad."
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBProductCollectionCreativePropertiesToOptimize | str,
                lenient_enum(SBProductCollectionCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
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


class SBCreateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")

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


class SBCreateSharedCollectionSettings(BaseModel):
    """Settings shared by all collection types."""

    model_config = ConfigDict(extra="forbid")

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: SBCreateImage | None = Field(default=None)


class SBCreateStoreSpotlightLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageType: Annotated[SBStoreSpotlightLandingPageType | str, lenient_enum(SBStoreSpotlightLandingPageType)]
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SBCreateStoreSpotlightSettings(BaseModel):
    """An ad creative that contains ASINs within a brand Store."""

    model_config = ConfigDict(extra="forbid")

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] = Field(
        min_length=1, max_length=1, description="The brand logo image assets to be used in the ad."
    )
    cards: list[SBCreateCardCreativeElement] = Field(
        min_length=3,
        max_length=3,
        description="The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.",
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBStoreSpotlightCreativePropertiesToOptimize | str,
                lenient_enum(SBStoreSpotlightCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
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


class SBCreateVideo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class SBCreateVideoLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageType: Annotated[SBVideoLandingPageType | str, lenient_enum(SBVideoLandingPageType)]
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class SBCreative(BaseModel):
    model_config = ConfigDict(extra="allow")

    componentCreative: SBComponentCreative | None = None


class SBCreativeStatus(BaseModel):
    model_config = ConfigDict(extra="allow")

    moderationStatus: Annotated[SBModerationStatus | str, lenient_enum(SBModerationStatus)]


class SBDeleteAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adIds: list[str] = Field(min_length=1, max_length=10)


class SBFormatProperties(BaseModel):
    model_config = ConfigDict(extra="allow")

    height: int | None = Field(default=None, description="The height (in pixels) of the cropped image.")
    left: int | None = Field(
        default=None, description="The number of pixels from the left of the image where the crop should begin."
    )
    top: int | None = Field(
        default=None, description="The number of pixels from the top of the image where the crop should begin."
    )
    width: int | None = Field(default=None, description="The width (in pixels) of the cropped image.")


class SBImage(BaseModel):
    model_config = ConfigDict(extra="allow")

    assetId: str = Field(description="The asset library ID associated with the image asset.")
    assetVersion: str = Field(description="The asset library version associated with the image asset.")
    formatProperties: list[SBFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class SBLandingPageAsins(BaseModel):
    model_config = ConfigDict(extra="allow")

    asins: list[str] = Field(
        min_length=1,
        max_length=100,
        description="For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.",
    )


class SBManualCollectionSettings(BaseModel):
    """Settings for manually curated collections."""

    model_config = ConfigDict(extra="allow")

    landingPage: SBCollectionLandingPage
    productInclusions: list[SBAdvertisedProducts] = Field(
        min_length=3, max_length=10, description="The products featured in the ad. Required for manual collections."
    )
    sharedSettings: SBSharedCollectionSettings
    title: str | None = Field(
        default=None, description="Optional title for the collection. If not provided, title will be auto-generated."
    )


class SBProductCollectionLandingPage(BaseModel):
    model_config = ConfigDict(extra="allow")

    landingPageAsins: SBLandingPageAsins | None = Field(default=None)
    landingPageType: Annotated[
        SBProductCollectionLandingPageType | str, lenient_enum(SBProductCollectionLandingPageType)
    ]
    landingPageUrl: str | None = Field(
        default=None, description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST"
    )


class SBProductCollectionSettings(BaseModel):
    """An ad creative that contains multiple products and a custom image."""

    model_config = ConfigDict(extra="allow")

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBImage] = Field(
        min_length=1, max_length=2, description="The brand logo image assets to be used in the ad."
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBProductCollectionCreativePropertiesToOptimize | str,
                lenient_enum(SBProductCollectionCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
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


class SBProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="allow")

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


class SBQueryAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SBAdAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SBAdAdIdFilter | None = Field(default=None)
    adProductFilter: SBAdAdProductFilter
    campaignIdFilter: SBAdCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SBAdNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SBAdStateFilter | None = Field(default=None)


class SBSharedCollectionSettings(BaseModel):
    """Settings shared by all collection types."""

    model_config = ConfigDict(extra="allow")

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: SBImage | None = Field(default=None)
    moderationStatus: SBCreativeStatus | None = Field(default=None)


class SBStoreSpotlightLandingPage(BaseModel):
    model_config = ConfigDict(extra="allow")

    landingPageType: Annotated[SBStoreSpotlightLandingPageType | str, lenient_enum(SBStoreSpotlightLandingPageType)]
    landingPageUrl: str = Field(description="The URL of landing page where the ad directs.")


class SBStoreSpotlightSettings(BaseModel):
    """An ad creative that contains ASINs within a brand Store."""

    model_config = ConfigDict(extra="allow")

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBImage] = Field(
        min_length=1, max_length=1, description="The brand logo image assets to be used in the ad."
    )
    cards: list[SBCardCreativeElement] = Field(
        min_length=3,
        max_length=3,
        description="The sub-elements of the creative. Each card highlights a different ASIN associated to a brand Store.",
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBStoreSpotlightCreativePropertiesToOptimize | str,
                lenient_enum(SBStoreSpotlightCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
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


class SBUpdateAdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ads: list[SBAdUpdate] = Field(min_length=1, max_length=10)


class SBUpdateAutoCollectionSettings(BaseModel):
    """Settings for automatically generated collections."""

    model_config = ConfigDict(extra="forbid")

    productExclusions: list[SBCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1000, description="Products to exclude from auto collection."
    )
    sharedSettings: SBUpdateSharedCollectionSettings | None = Field(default=None)


class SBUpdateBrandGallerySettings(BaseModel):
    """An ad creative that showcases a brand and its categories and collections."""

    model_config = ConfigDict(extra="forbid")

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
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBBrandGalleryCreativePropertiesToOptimize | str,
                lenient_enum(SBBrandGalleryCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
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


class SBUpdateCollectionLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageType: Annotated[SBCollectionLandingPageType | str, lenient_enum(SBCollectionLandingPageType)] | None = (
        Field(default=None)
    )
    landingPageUrl: str | None = Field(default=None, description="The URL associated to the landing page.")


class SBUpdateComponentCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    autoCollectionSettings: SBUpdateAutoCollectionSettings | None = Field(default=None)
    brandGallerySettings: SBUpdateBrandGallerySettings | None = Field(default=None)
    manualCollectionSettings: SBUpdateManualCollectionSettings | None = Field(default=None)
    productCollectionSettings: SBUpdateProductCollectionSettings | None = Field(default=None)
    productVideoSettings: SBUpdateProductVideoSettings | None = Field(default=None)
    storeSpotlightSettings: SBUpdateStoreSpotlightSettings | None = Field(default=None)


class SBUpdateCreative(BaseModel):
    model_config = ConfigDict(extra="forbid")

    componentCreative: SBUpdateComponentCreative | None = None


class SBUpdateImage(BaseModel):
    model_config = ConfigDict(extra="forbid")

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


class SBUpdateLandingPageAsins(BaseModel):
    model_config = ConfigDict(extra="forbid")

    asins: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="For landing page of type ASIN_LIST, the list of ASINs used to create the landing page.",
    )


class SBUpdateManualCollectionSettings(BaseModel):
    """Settings for manually curated collections."""

    model_config = ConfigDict(extra="forbid")

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


class SBUpdateProductCollectionLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageAsins: SBUpdateLandingPageAsins | None = Field(default=None)
    landingPageType: (
        Annotated[SBProductCollectionLandingPageType | str, lenient_enum(SBProductCollectionLandingPageType)] | None
    ) = Field(default=None)
    landingPageUrl: str | None = Field(
        default=None, description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST"
    )


class SBUpdateProductCollectionSettings(BaseModel):
    """An ad creative that contains multiple products and a custom image."""

    model_config = ConfigDict(extra="forbid")

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] | None = Field(
        default=None, min_length=1, max_length=2, description="The brand logo image assets to be used in the ad."
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBProductCollectionCreativePropertiesToOptimize | str,
                lenient_enum(SBProductCollectionCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
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


class SBUpdateProductVideoSettings(BaseModel):
    """An ad with a creative that includes a video."""

    model_config = ConfigDict(extra="forbid")

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


class SBUpdateSharedCollectionSettings(BaseModel):
    """Settings shared by all collection types."""

    model_config = ConfigDict(extra="forbid")

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: SBUpdateImage | None = Field(default=None)


class SBUpdateStoreSpotlightLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageType: (
        Annotated[SBStoreSpotlightLandingPageType | str, lenient_enum(SBStoreSpotlightLandingPageType)] | None
    ) = Field(default=None)
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class SBUpdateStoreSpotlightSettings(BaseModel):
    """An ad creative that contains ASINs within a brand Store."""

    model_config = ConfigDict(extra="forbid")

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
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBStoreSpotlightCreativePropertiesToOptimize | str,
                lenient_enum(SBStoreSpotlightCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
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


class SBUpdateVideoLandingPage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    landingPageType: Annotated[SBVideoLandingPageType | str, lenient_enum(SBVideoLandingPageType)] | None = Field(
        default=None
    )
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class SBVideo(BaseModel):
    model_config = ConfigDict(extra="allow")

    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class SBVideoLandingPage(BaseModel):
    model_config = ConfigDict(extra="allow")

    landingPageType: Annotated[SBVideoLandingPageType | str, lenient_enum(SBVideoLandingPageType)]
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


__all__ = [
    "SBAdAdGroupIdFilter",
    "SBAdAdIdFilter",
    "SBAdAdProductFilter",
    "SBAdCampaignIdFilter",
    "SBAdCreate",
    "SBAdNameFilter",
    "SBAdNameFilterType",
    "SBAdProduct",
    "SBAdStateFilter",
    "SBAdType",
    "SBAdUpdate",
    "SBBrandGalleryCreativePropertiesToOptimize",
    "SBCollectionLandingPageType",
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
    "SBDeleteAdRequest",
    "SBDeliveryReason",
    "SBDeliveryStatus",
    "SBErrorCode",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBModerationStatus",
    "SBProductCollectionCreativePropertiesToOptimize",
    "SBProductCollectionLandingPageType",
    "SBProductIdType",
    "SBQueryAdRequest",
    "SBState",
    "SBStoreSpotlightCreativePropertiesToOptimize",
    "SBStoreSpotlightLandingPageType",
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
    "SBVideoLandingPageType",
]
