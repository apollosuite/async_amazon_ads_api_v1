"""Auto-generated models for Targets from Amazon Ads API v1."""

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
    SBDeliveryReason,
    SBDeliveryStatus,
    SBMarketplaceScope,
    SBProductIdType,
    SBState,
    SBStatus,
    SBUpdateState,
)


class SBCurrencyCode(StrEnum):
    AED = "AED"  # United Arab Emirates Dirham
    AUD = "AUD"  # Australian Dollar
    BRL = "BRL"  # Brazilian Real
    CAD = "CAD"  # Canadian Dollar
    CHF = "CHF"  # Swiss Franc
    CNY = "CNY"  # Chinese Yuan
    DKK = "DKK"  # Danish Krone
    EGP = "EGP"  # Egyptian Pound
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound Sterling
    INR = "INR"  # Indian Rupee
    JPY = "JPY"  # Japanese Yen
    MXN = "MXN"  # Mexican Peso
    MXP = "MXP"  # Mexican Peso
    NGN = "NGN"  # Nigerian Naira
    NOK = "NOK"  # Norwegian Krone
    NZD = "NZD"  # New Zealand Dollar
    PLN = "PLN"  # Polish Złoty
    SAR = "SAR"  # Saudi Riyal
    SEK = "SEK"  # Swedish Krona
    SGD = "SGD"  # Singapore Dollar
    TRY = "TRY"  # Turkish Lira
    USD = "USD"  # United States Dollar
    ZAR = "ZAR"  # South African Rand


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


class SBKeywordMatchType(StrEnum):
    BROAD = "BROAD"  # Broad match search terms. This expands matching on user intent beyond PHRASE.
    EXACT = "EXACT"  # Exact match search terms.
    PHRASE = "PHRASE"  # Phrase match search terms. This expands matching on user intent beyond EXACT.


class SBLanguageLocale(StrEnum):
    """
    A combination of ISO-639 standard for language code and ISO-3166 for country code.
    """

    zh_CN = "zh_CN"  # Chinese (China).


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


class SBMatchType(StrEnum):
    BROAD = "BROAD"  # Broad match search terms. This expands matching on user intent beyond PHRASE.
    EXACT = "EXACT"  # Exact match search terms.
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"  # Search terms related to your brand.
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = (
        "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"  # Search terms related to your landing pages.
    )
    PHRASE = "PHRASE"  # Phrase match search terms. This expands matching on user intent beyond EXACT.
    PRODUCT_EXACT = "PRODUCT_EXACT"  # Products exactly matching the specified product.


class SBProductMatchType(StrEnum):
    PRODUCT_EXACT = "PRODUCT_EXACT"  # Products exactly matching the specified product.


class SBTargetKeywordFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SBTargetLevel(StrEnum):
    AD_GROUP = "AD_GROUP"  # Target applied at the ad group level.


class SBTargetType(StrEnum):
    KEYWORD = "KEYWORD"  # Target based on customer search terms.
    PRODUCT = "PRODUCT"  # Target based on a specific product.
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"  # Target based on a product category.
    THEME = (
        "THEME"  # Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
    )


class SBThemeMatchType(StrEnum):
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"  # Search terms related to your brand.
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = (
        "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"  # Search terms related to your landing pages.
    )


class SBCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SBKeywordMatchType, lenient_enum(SBKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SBLanguageLocale, lenient_enum(SBLanguageLocale)] | None = Field(default=None)


class SBCreateProductCategoryRefinement(StrictModel):
    productBrandId: str | None = Field(default=None, description="The brand ID to target.")
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")
    productPriceGreaterThan: float | None = Field(
        default=None,
        description="Refinement to target products with a price greater than the value within the product category.",
    )
    productPriceLessThan: float | None = Field(
        default=None,
        description="Refinement to target products with a price less than the value within the product category.",
    )
    productRatingGreaterThan: float | None = Field(
        default=None,
        description="Refinement to target products with a rating greater than the value within the product category.",
    )
    productRatingLessThan: float | None = Field(
        default=None,
        description="Refinement to target products with a rating less than the value within the product category.",
    )


class SBCreateProductCategoryRefinementValue(StrictModel):
    productCategoryRefinement: SBCreateProductCategoryRefinement | None = Field(default=None)


class SBCreateProductCategoryTarget(StrictModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: SBCreateProductCategoryRefinementValue


class SBCreateProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: Annotated[SBProductMatchType, lenient_enum(SBProductMatchType)]
    product: SBCreateProductValue
    productIdType: Annotated[SBProductIdType, lenient_enum(SBProductIdType)]


class SBCreateProductValue(StrictModel):
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SBCreateTargetBid(StrictModel):
    bid: float = Field(description="The maximum bid for a target.")


class SBCreateTargetDetailsKeywordTarget(StrictModel):
    keywordTarget: SBCreateKeywordTarget


class SBCreateTargetDetailsProductTarget(StrictModel):
    productTarget: SBCreateProductTarget


class SBCreateTargetDetailsProductCategoryTarget(StrictModel):
    productCategoryTarget: SBCreateProductCategoryTarget


class SBCreateTargetDetailsThemeTarget(StrictModel):
    themeTarget: SBCreateThemeTarget


type SBCreateTargetDetails = SBCreateTargetDetailsKeywordTarget | SBCreateTargetDetailsProductTarget | SBCreateTargetDetailsProductCategoryTarget | SBCreateTargetDetailsThemeTarget


class SBCreateTargetRequest(StrictModel):
    targets: list[SBTargetCreate] = Field(min_length=1, max_length=1000)


class SBCreateThemeTarget(StrictModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: Annotated[SBThemeMatchType, lenient_enum(SBThemeMatchType)]


class SBDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SBError(LenientModel):
    code: Annotated[SBErrorCode | str, lenient_enum(SBErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class SBErrorsIndex(LenientModel):
    errors: list[SBError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=4999)


class SBKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SBKeywordMatchType | str, lenient_enum(SBKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SBLanguageLocale | str, lenient_enum(SBLanguageLocale)] | None = Field(default=None)


class SBProductCategoryRefinement(LenientModel):
    productBrandId: str | None = Field(default=None, description="The brand ID to target.")
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")
    productPriceGreaterThan: float | None = Field(
        default=None,
        description="Refinement to target products with a price greater than the value within the product category.",
    )
    productPriceLessThan: float | None = Field(
        default=None,
        description="Refinement to target products with a price less than the value within the product category.",
    )
    productRatingGreaterThan: float | None = Field(
        default=None,
        description="Refinement to target products with a rating greater than the value within the product category.",
    )
    productRatingLessThan: float | None = Field(
        default=None,
        description="Refinement to target products with a rating less than the value within the product category.",
    )


class SBProductCategoryRefinementValue(LenientModel):
    productCategoryRefinement: SBProductCategoryRefinement | None = Field(default=None)


class SBProductCategoryTarget(LenientModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: SBProductCategoryRefinementValue


class SBProductTarget(LenientModel):
    """Targets a specific product."""

    matchType: Annotated[SBProductMatchType | str, lenient_enum(SBProductMatchType)]
    product: SBProductValue
    productIdType: Annotated[SBProductIdType | str, lenient_enum(SBProductIdType)]


class SBProductValue(LenientModel):
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SBQueryTargetRequest(StrictModel):
    adGroupIdFilter: SBTargetAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SBTargetAdProductFilter
    campaignIdFilter: SBTargetCampaignIdFilter | None = Field(default=None)
    keywordFilter: SBTargetKeywordFilter | None = Field(default=None)
    matchTypeFilter: SBTargetMatchTypeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=5000, ge=1, le=5000)
    nativeLanguageLocaleFilter: SBTargetLanguageLocaleFilter | None = Field(default=None)
    negativeFilter: SBTargetNegativeFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SBTargetStateFilter | None = Field(default=None)
    targetIdFilter: SBTargetTargetIdFilter | None = Field(default=None)
    targetTypeFilter: SBTargetTargetTypeFilter | None = Field(default=None)


class SBTarget(LenientModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    bid: SBTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime = Field(description="The date time the target was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SBState | str, lenient_enum(SBState)]
    status: SBStatus | None = Field(default=None)
    targetDetails: SBTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: Annotated[SBTargetLevel | str, lenient_enum(SBTargetLevel)]
    targetType: Annotated[SBTargetType | str, lenient_enum(SBTargetType)]


class SBTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBTargetAdProductFilter(StrictModel):
    include: list[Annotated[SBAdProduct, lenient_enum(SBAdProduct)]] = Field(min_length=1, max_length=1)


class SBTargetBid(LenientModel):
    bid: float = Field(description="The maximum bid for a target.")
    currencyCode: Annotated[SBCurrencyCode | str, lenient_enum(SBCurrencyCode)]


class SBTargetCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBTargetCreate(StrictModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: Annotated[SBAdProduct, lenient_enum(SBAdProduct)]
    bid: SBCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SBCreateState, lenient_enum(SBCreateState)]
    targetDetails: SBCreateTargetDetails
    targetType: Annotated[SBTargetType, lenient_enum(SBTargetType)]


class SBTargetDetailsKeywordTarget(LenientModel):
    keywordTarget: SBKeywordTarget


class SBTargetDetailsProductCategoryTarget(LenientModel):
    productCategoryTarget: SBProductCategoryTarget


class SBTargetDetailsProductTarget(LenientModel):
    productTarget: SBProductTarget


class SBTargetDetailsThemeTarget(LenientModel):
    themeTarget: SBThemeTarget


type SBTargetDetails = SBTargetDetailsKeywordTarget | SBTargetDetailsProductCategoryTarget | SBTargetDetailsProductTarget | SBTargetDetailsThemeTarget


class SBTargetKeywordFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=2)
    queryTermMatchType: Annotated[SBTargetKeywordFilterType, lenient_enum(SBTargetKeywordFilterType)]


class SBTargetLanguageLocaleFilter(StrictModel):
    include: list[Annotated[SBLanguageLocale, lenient_enum(SBLanguageLocale)]] = Field(min_length=1, max_length=1)


class SBTargetMatchTypeFilter(StrictModel):
    include: list[Annotated[SBMatchType, lenient_enum(SBMatchType)]] = Field(min_length=1, max_length=10)


class SBTargetMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SBTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SBTargetMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=999)
    target: SBTarget


class SBTargetNegativeFilter(StrictModel):
    include: list[bool] = Field(min_length=1, max_length=1)


class SBTargetStateFilter(StrictModel):
    include: list[Annotated[SBState, lenient_enum(SBState)]] = Field(min_length=1, max_length=3)


class SBTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[SBTarget] | None = Field(default=None, min_length=0, max_length=5000)


class SBTargetTargetIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBTargetTargetTypeFilter(StrictModel):
    include: list[Annotated[SBTargetType, lenient_enum(SBTargetType)]] = Field(min_length=1, max_length=4)


class SBTargetUpdate(StrictModel):
    bid: SBUpdateTargetBid | None = Field(default=None)
    state: Annotated[SBUpdateState, lenient_enum(SBUpdateState)] | None = Field(default=None)
    targetId: str = Field(description="A unique identifier for the target.")


class SBThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: Annotated[SBThemeMatchType | str, lenient_enum(SBThemeMatchType)]


class SBUpdateTargetBid(StrictModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")


class SBUpdateTargetRequest(StrictModel):
    targets: list[SBTargetUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SBAdProduct",
    "SBCreateKeywordTarget",
    "SBCreateProductCategoryRefinement",
    "SBCreateProductCategoryRefinementValue",
    "SBCreateProductCategoryTarget",
    "SBCreateProductTarget",
    "SBCreateProductValue",
    "SBCreateState",
    "SBCreateTargetBid",
    "SBCreateTargetDetails",
    "SBCreateTargetRequest",
    "SBCreateThemeTarget",
    "SBCurrencyCode",
    "SBDeleteTargetRequest",
    "SBDeliveryReason",
    "SBDeliveryStatus",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBKeywordMatchType",
    "SBKeywordTarget",
    "SBLanguageLocale",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBMatchType",
    "SBProductCategoryRefinement",
    "SBProductCategoryRefinementValue",
    "SBProductCategoryTarget",
    "SBProductIdType",
    "SBProductMatchType",
    "SBProductTarget",
    "SBProductValue",
    "SBQueryTargetRequest",
    "SBState",
    "SBStatus",
    "SBTarget",
    "SBTargetAdGroupIdFilter",
    "SBTargetAdProductFilter",
    "SBTargetBid",
    "SBTargetCampaignIdFilter",
    "SBTargetCreate",
    "SBTargetDetails",
    "SBTargetKeywordFilter",
    "SBTargetKeywordFilterType",
    "SBTargetLanguageLocaleFilter",
    "SBTargetLevel",
    "SBTargetMatchTypeFilter",
    "SBTargetMultiStatusResponse",
    "SBTargetMultiStatusSuccess",
    "SBTargetNegativeFilter",
    "SBTargetStateFilter",
    "SBTargetSuccessResponse",
    "SBTargetTargetIdFilter",
    "SBTargetTargetTypeFilter",
    "SBTargetType",
    "SBTargetUpdate",
    "SBThemeMatchType",
    "SBThemeTarget",
    "SBUpdateState",
    "SBUpdateTargetBid",
    "SBUpdateTargetRequest",
]
