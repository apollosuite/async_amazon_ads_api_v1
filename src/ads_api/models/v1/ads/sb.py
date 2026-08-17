"""Auto-generated models for Ads from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.sb import (
    SBAdProduct,
    SBCreateState,
    SBCreateTag,
    SBDeliveryReason,
    SBDeliveryStatus,
    SBMarketplaceScope,
    SBProductIdType,
    SBState,
    SBStatus,
    SBTag,
    SBUpdateState,
)


class SBAdNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SBAdType(StrEnum):
    COMPONENT = "COMPONENT"  # A creative that can features a collection of videos, images, and products.


class SBBrandGalleryCreativePropertiesToOptimize(StrEnum):
    HEADLINE = "HEADLINE"  # The headline in the creative.


class SBCollectionLandingPageType(StrEnum):
    ASIN_LIST = "ASIN_LIST"  # A list of products based on the products promoted in the ad creative.
    STORE = "STORE"  # A brand Store landing page.


class SBErrorCode(StrEnum):
    ACTION_NOT_SUPPORTED = "ACTION_NOT_SUPPORTED"  # The request is not supported.
    ACTIVE_RESOURCE_LIMIT_EXCEEDED = (
        "ACTIVE_RESOURCE_LIMIT_EXCEEDED"  # Too many live resources. Remove resources and try again.
    )
    ARCHIVED_PARENT_CANNOT_CREATE = (
        "ARCHIVED_PARENT_CANNOT_CREATE"  # New resources cannot be created within an archived parent.
    )
    ARCHIVED_PARENT_CANNOT_EDIT = "ARCHIVED_PARENT_CANNOT_EDIT"  # Resources within an archived parent cannot be edited.
    ARCHIVED_RESOURCE_CANNOT_EDIT = "ARCHIVED_RESOURCE_CANNOT_EDIT"  # Archived resources cannot be edited.
    AUTOCREATED_ENTITY_CANNOT_EDIT = "AUTOCREATED_ENTITY_CANNOT_EDIT"  # Autocreated entities cannot be edited. To complete this action, create the resource manually.
    BAD_REQUEST = "BAD_REQUEST"  # The request is not valid considering the documented schema.
    CONFLICT = "CONFLICT"  # Operation could not be completed due to a conflict. Please retry your request.
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"  # The request is too large. Consider splitting it into multiple requests.
    DATE_CANNOT_BE_IN_PAST = "DATE_CANNOT_BE_IN_PAST"  # Update the date to be in the future.
    DATE_CANNOT_BE_NULL = "DATE_CANNOT_BE_NULL"  # Update the date.
    DATE_TOO_SOON = "DATE_TOO_SOON"  # Update the date to be further in the future.
    DUPLICATE_FIELD_VALUE_FOUND = "DUPLICATE_FIELD_VALUE_FOUND"  # Multiple resources share the non-unique field values. Remove the non-unique field value.
    DUPLICATE_RESOURCE_ID_FOUND = (
        "DUPLICATE_RESOURCE_ID_FOUND"  # Multiple resources share the same ID. Remove the duplicate ID.
    )
    DURATION_TOO_SHORT = "DURATION_TOO_SHORT"  # Update the length to be within the required range.
    FEATURE_DISCONTINUED = "FEATURE_DISCONTINUED"  # Feature has been discontinued.
    FEATURE_NOT_AVAILABLE = "FEATURE_NOT_AVAILABLE"  # The requested feature is not available.
    FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_SIZE_IS_OUT_OF_RANGE = "FIELD_SIZE_IS_OUT_OF_RANGE"  # Update the value to be within the required range.
    FIELD_VALUE_CANNOT_EDIT = "FIELD_VALUE_CANNOT_EDIT"  # Field value cannot be edited.
    FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS = (
        "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_CONTAINS_INVALID_CHARACTERS = (
        "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS"  # Remove the invalid characters and try again.
    )
    FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_VALUE_IS_EMPTY = "FIELD_VALUE_IS_EMPTY"  # Update the request with the required information for this resource.
    FIELD_VALUE_IS_INVALID = (
        "FIELD_VALUE_IS_INVALID"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_IS_NULL = "FIELD_VALUE_IS_NULL"  # Update the request with the required information for this resource.
    FIELD_VALUE_IS_OUT_OF_RANGE = "FIELD_VALUE_IS_OUT_OF_RANGE"  # Update the value to be within the required range.
    FIELD_VALUE_MISMATCH = "FIELD_VALUE_MISMATCH"  # Mismatch among resource field values.
    FIELD_VALUE_MUST_BE_EMPTY_OR_NULL = (
        "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_NOT_FOUND = (
        "FIELD_VALUE_NOT_FOUND"  # Resource specified in the field value not found. Try again with valid value.
    )
    FIELD_VALUE_NOT_UNIQUE = "FIELD_VALUE_NOT_UNIQUE"  # Resource field value conflicts with existing resource. Try again with an unique field value.
    FORBIDDEN = "FORBIDDEN"  # The caller is not authorized to make the given request.
    INTERNAL_ERROR = "INTERNAL_ERROR"  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    NOT_FOUND = "NOT_FOUND"  # The requested resource does not exist.
    PAYMENT_ISSUE = "PAYMENT_ISSUE"  # Payment failed.
    PRODUCT_INELIGIBLE = (
        "PRODUCT_INELIGIBLE"  # Product is not eligible for advertising. Try again with a valid product.
    )
    RESOURCE_DOES_NOT_BELONG_TO_PARENT = "RESOURCE_DOES_NOT_BELONG_TO_PARENT"  # Resource does not belong to the specified parent. Try again with a valid parent ID.
    RESOURCE_ID_NOT_FOUND = "RESOURCE_ID_NOT_FOUND"  # Resource ID not found. Try again with valid ID.
    RESOURCE_IS_EMPTY = "RESOURCE_IS_EMPTY"  # Update the request with the required information for this resource.
    RESOURCE_IS_IN_TERMINAL_STATE = "RESOURCE_IS_IN_TERMINAL_STATE"  # Resource is in terminal state.
    RESOURCE_IS_NULL = "RESOURCE_IS_NULL"  # Update the request with the required information for this resource.
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"  # There have been too many requests, please slow down your call rate.
    TOTAL_RESOURCE_LIMIT_EXCEEDED = (
        "TOTAL_RESOURCE_LIMIT_EXCEEDED"  # Too many resources. Remove resources and try again.
    )
    UNAUTHORIZED = "UNAUTHORIZED"  # The request lacks the necessary credentials.
    UNSUPPORTED_MARKETPLACE = (
        "UNSUPPORTED_MARKETPLACE"  # Marketplace not supported. Try again with a supported marketplace.
    )


class SBMarketplace(StrEnum):
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


class SBModerationStatus(StrEnum):
    APPROVED_WITH_EXCEPTIONS = "APPROVED_WITH_EXCEPTIONS"  # The creative passed basic moderation but was found to be invalid for some supplies. The creative is serving on approved supplies.
    PENDING_TRANSLATION = "PENDING_TRANSLATION"  # The creative is pending creative Translations.
    PUBLISHED = "PUBLISHED"  # The creative passed moderation and is serving.
    REJECTED_BY_MODERATION = "REJECTED_BY_MODERATION"  # The creative was rejected during the moderation process.
    SUBMITTED_FOR_MODERATION = (
        "SUBMITTED_FOR_MODERATION"  # The creative has been submitted, but has not yet been reviewed.
    )


class SBProductCollectionCreativePropertiesToOptimize(StrEnum):
    HEADLINE = "HEADLINE"  # The headline in the creative.


class SBProductCollectionLandingPageType(StrEnum):
    ASIN_LIST = "ASIN_LIST"  # A list of products based on the products promoted in the ad creative.
    CUSTOM_URL = "CUSTOM_URL"  # A custom landing page. Available for vendors only.
    STORE = "STORE"  # A brand Store landing page.


class SBStoreSpotlightCreativePropertiesToOptimize(StrEnum):
    HEADLINE = "HEADLINE"  # The headline in the creative.


class SBStoreSpotlightLandingPageType(StrEnum):
    STORE = "STORE"  # A brand Store landing page.


class SBVideoLandingPageType(StrEnum):
    DETAIL_PAGE = "DETAIL_PAGE"  # A product detail page.
    STORE = "STORE"  # A brand Store landing page.


class SBAd(LenientModel):
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


class SBAdAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBAdAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBAdAdProductFilter(StrictModel):
    include: list[Annotated[SBAdProduct, lenient_enum(SBAdProduct)]] = Field(min_length=1, max_length=1)


class SBAdCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBAdCreate(StrictModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: Annotated[SBAdProduct, lenient_enum(SBAdProduct)]
    adType: Annotated[SBAdType, lenient_enum(SBAdType)]
    creative: SBCreateCreative
    name: str = Field(description="The name of the ad.")
    state: Annotated[SBCreateState, lenient_enum(SBCreateState)]
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
    queryTermMatchType: Annotated[SBAdNameFilterType, lenient_enum(SBAdNameFilterType)]


class SBAdStateFilter(StrictModel):
    include: list[Annotated[SBState, lenient_enum(SBState)]] = Field(min_length=1, max_length=3)


class SBAdSuccessResponse(LenientModel):
    ads: list[SBAd] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SBAdUpdate(StrictModel):
    adId: str = Field(description="The identifier of the ad.")
    creative: SBUpdateCreative | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad.")
    state: Annotated[SBUpdateState, lenient_enum(SBUpdateState)] | None = Field(default=None)
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SBAdvertisedProducts(LenientModel):
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: Annotated[SBProductIdType | str, lenient_enum(SBProductIdType)]


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


class SBCardCreativeElement(LenientModel):
    headline: str = Field(description="The headline used for the card.")
    landingPage: SBStoreSpotlightLandingPage
    products: SBAdvertisedProducts


class SBCollectionLandingPage(LenientModel):
    landingPageType: Annotated[SBCollectionLandingPageType | str, lenient_enum(SBCollectionLandingPageType)]
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
    productIdType: Annotated[SBProductIdType, lenient_enum(SBProductIdType)]


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
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBBrandGalleryCreativePropertiesToOptimize, lenient_enum(SBBrandGalleryCreativePropertiesToOptimize)
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


class SBCreateCardCreativeElement(StrictModel):
    headline: str = Field(description="The headline used for the card.")
    landingPage: SBCreateStoreSpotlightLandingPage
    products: SBCreateAdvertisedProducts


class SBCreateCollectionLandingPage(StrictModel):
    landingPageType: Annotated[SBCollectionLandingPageType, lenient_enum(SBCollectionLandingPageType)]
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
    landingPageType: Annotated[SBProductCollectionLandingPageType, lenient_enum(SBProductCollectionLandingPageType)]
    landingPageUrl: str | None = Field(
        default=None, description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST"
    )


class SBCreateProductCollectionSettings(StrictModel):
    """An ad creative that contains multiple products and a custom image."""

    brand: str = Field(description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] = Field(
        min_length=1, max_length=2, description="The brand logo image assets to be used in the ad."
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBProductCollectionCreativePropertiesToOptimize,
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
    landingPageType: Annotated[SBStoreSpotlightLandingPageType, lenient_enum(SBStoreSpotlightLandingPageType)]
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
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBStoreSpotlightCreativePropertiesToOptimize, lenient_enum(SBStoreSpotlightCreativePropertiesToOptimize)
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


class SBCreateVideo(StrictModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class SBCreateVideoLandingPage(StrictModel):
    landingPageType: Annotated[SBVideoLandingPageType, lenient_enum(SBVideoLandingPageType)]
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class SBCreative(LenientModel):
    componentCreative: SBComponentCreative


class SBCreativeStatus(LenientModel):
    moderationStatus: Annotated[SBModerationStatus | str, lenient_enum(SBModerationStatus)]


class SBDeleteAdRequest(StrictModel):
    adIds: list[str] = Field(min_length=1, max_length=10)


class SBError(LenientModel):
    code: Annotated[SBErrorCode | str, lenient_enum(SBErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class SBErrorsIndex(LenientModel):
    errors: list[SBError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=4999)


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
    landingPageType: Annotated[
        SBProductCollectionLandingPageType | str, lenient_enum(SBProductCollectionLandingPageType)
    ]
    landingPageUrl: str | None = Field(
        default=None, description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST"
    )


class SBProductCollectionSettings(LenientModel):
    """An ad creative that contains multiple products and a custom image."""

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
    landingPageType: Annotated[SBStoreSpotlightLandingPageType | str, lenient_enum(SBStoreSpotlightLandingPageType)]
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
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBBrandGalleryCreativePropertiesToOptimize, lenient_enum(SBBrandGalleryCreativePropertiesToOptimize)
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


class SBUpdateCollectionLandingPage(StrictModel):
    landingPageType: Annotated[SBCollectionLandingPageType, lenient_enum(SBCollectionLandingPageType)] | None = Field(
        default=None
    )
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
    landingPageType: (
        Annotated[SBProductCollectionLandingPageType, lenient_enum(SBProductCollectionLandingPageType)] | None
    ) = Field(default=None)
    landingPageUrl: str | None = Field(
        default=None, description="The URL associated to the landing page. Read only if landingPageType is ASIN_LIST"
    )


class SBUpdateProductCollectionSettings(StrictModel):
    """An ad creative that contains multiple products and a custom image."""

    brand: str | None = Field(default=None, description="The name of the brand being advertised.")
    brandLogos: list[SBCreateImage] | None = Field(
        default=None, min_length=1, max_length=2, description="The brand logo image assets to be used in the ad."
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBProductCollectionCreativePropertiesToOptimize,
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
    landingPageType: (
        Annotated[SBStoreSpotlightLandingPageType, lenient_enum(SBStoreSpotlightLandingPageType)] | None
    ) = Field(default=None)
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
    creativePropertiesToOptimize: (
        list[
            Annotated[
                SBStoreSpotlightCreativePropertiesToOptimize, lenient_enum(SBStoreSpotlightCreativePropertiesToOptimize)
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


class SBUpdateVideoLandingPage(StrictModel):
    landingPageType: Annotated[SBVideoLandingPageType, lenient_enum(SBVideoLandingPageType)] | None = Field(
        default=None
    )
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class SBVideo(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class SBVideoLandingPage(LenientModel):
    landingPageType: Annotated[SBVideoLandingPageType | str, lenient_enum(SBVideoLandingPageType)]
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
