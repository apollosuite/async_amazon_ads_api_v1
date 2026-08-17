"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.sp import (
    SPAdProduct,
    SPCreateState,
    SPCreateTag,
    SPCurrencyCode,
    SPDeliveryReason,
    SPDeliveryStatus,
    SPError,
    SPErrorCode,
    SPErrorsIndex,
    SPMarketplaceScope,
    SPProductIdType,
    SPState,
    SPStatus,
    SPTag,
    SPUpdateState,
)


class SPKeywordMatchType(StrEnum):
    BROAD = "BROAD"  # Broad match search terms. This expands matching on user intent beyond PHRASE.
    EXACT = "EXACT"  # Exact match search terms.
    PHRASE = "PHRASE"  # Phrase match search terms. This expands matching on user intent beyond EXACT.


class SPLanguageLocale(StrEnum):
    """
    A combination of ISO-639 standard for language code and ISO-3166 for country code.
    """

    zh_CN = "zh_CN"  # Chinese (China).


class SPMarketplace(StrEnum):
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


class SPMatchType(StrEnum):
    BROAD = "BROAD"  # Broad match search terms. This expands matching on user intent beyond PHRASE.
    EXACT = "EXACT"  # Exact match search terms.
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"  # Search terms closely matching advertised product.
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"  # Search terms loosely matching advertised product.
    KEYWORDS_RELATED_TO_GIFTS = "KEYWORDS_RELATED_TO_GIFTS"  # Search terms related to gifts.
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"  # Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically.
    KEYWORDS_RELATED_TO_PRIME_DAY = "KEYWORDS_RELATED_TO_PRIME_DAY"  # Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"  # Search terms related to your brand.
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"  # Search terms shoppers often use to search for products in the same category as the products you're advertising.
    PHRASE = "PHRASE"  # Phrase match search terms. This expands matching on user intent beyond EXACT.
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"  # Products that complement advertised product.
    PRODUCT_EXACT = "PRODUCT_EXACT"  # Products exactly matching the specified product.
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"  # Products similar to the specified product.
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"  # Products that can be substituted for advertised product.


class SPProductMatchType(StrEnum):
    PRODUCT_EXACT = "PRODUCT_EXACT"  # Products exactly matching the specified product.
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"  # Products similar to the specified product.


class SPTargetKeywordFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SPTargetLevel(StrEnum):
    AD_GROUP = "AD_GROUP"  # Target applied at the ad group level.
    CAMPAIGN = "CAMPAIGN"  # Target applied at the campaign level.


class SPTargetProductIdFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SPTargetType(StrEnum):
    KEYWORD = "KEYWORD"  # Target based on customer search terms.
    LOCATION = "LOCATION"  # Target based on geographic location.
    PRODUCT = "PRODUCT"  # Target based on a specific product.
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"  # Target based on a product category.
    THEME = (
        "THEME"  # Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
    )


class SPThemeMatchType(StrEnum):
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"  # Search terms closely matching advertised product.
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"  # Search terms loosely matching advertised product.
    KEYWORDS_RELATED_TO_GIFTS = "KEYWORDS_RELATED_TO_GIFTS"  # Search terms related to gifts.
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"  # Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically.
    KEYWORDS_RELATED_TO_PRIME_DAY = "KEYWORDS_RELATED_TO_PRIME_DAY"  # Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"  # Search terms related to your brand.
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"  # Search terms shoppers often use to search for products in the same category as the products you're advertising.
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"  # Products that complement advertised product.
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"  # Products that can be substituted for advertised product.


class SPCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SPKeywordMatchType, lenient_enum(SPKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SPLanguageLocale, lenient_enum(SPLanguageLocale)] | None = Field(default=None)


class SPCreateLocationTarget(StrictModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class SPCreateProductCategoryRefinement(StrictModel):
    productAgeRangeId: str | None = Field(default=None, description="The age range ID to target.")
    productBrandId: str | None = Field(default=None, description="The brand ID to target.")
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")
    productGenreId: str | None = Field(default=None, description="The product genre ID to target.")
    productPriceGreaterThan: float | None = Field(
        default=None,
        description="Refinement to target products with a price greater than the value within the product category.",
    )
    productPriceLessThan: float | None = Field(
        default=None,
        description="Refinement to target products with a price less than the value within the product category.",
    )
    productPrimeShippingEligible: bool | None = Field(
        default=None, description="Target based on if a product is Prime-shipping eligible."
    )
    productRatingGreaterThan: float | None = Field(
        default=None,
        description="Refinement to target products with a rating greater than the value within the product category.",
    )
    productRatingLessThan: float | None = Field(
        default=None,
        description="Refinement to target products with a rating less than the value within the product category.",
    )


class SPCreateProductCategoryRefinementValue(StrictModel):
    productCategoryRefinement: SPCreateProductCategoryRefinement


class SPCreateProductCategoryTarget(StrictModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: SPCreateProductCategoryRefinementValue


class SPCreateProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: Annotated[SPProductMatchType, lenient_enum(SPProductMatchType)]
    product: SPCreateProductValue
    productIdType: Annotated[SPProductIdType, lenient_enum(SPProductIdType)]


class SPCreateProductValue(StrictModel):
    productId: str = Field(
        description="The product identifier. Either the product id or the marketplace settings should always be specified"
    )


class SPCreateTargetBid(StrictModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")


class SPCreateTargetDetailsKeywordTarget(StrictModel):
    keywordTarget: SPCreateKeywordTarget


class SPCreateTargetDetailsProductTarget(StrictModel):
    productTarget: SPCreateProductTarget


class SPCreateTargetDetailsProductCategoryTarget(StrictModel):
    productCategoryTarget: SPCreateProductCategoryTarget


class SPCreateTargetDetailsLocationTarget(StrictModel):
    locationTarget: SPCreateLocationTarget


class SPCreateTargetDetailsThemeTarget(StrictModel):
    themeTarget: SPCreateThemeTarget


type SPCreateTargetDetails = SPCreateTargetDetailsKeywordTarget | SPCreateTargetDetailsProductTarget | SPCreateTargetDetailsProductCategoryTarget | SPCreateTargetDetailsLocationTarget | SPCreateTargetDetailsThemeTarget


class SPCreateTargetRequest(StrictModel):
    targets: list[SPTargetCreate] = Field(min_length=1, max_length=1000)


class SPCreateThemeTarget(StrictModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: Annotated[SPThemeMatchType, lenient_enum(SPThemeMatchType)]


class SPDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SPKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SPKeywordMatchType | str, lenient_enum(SPKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SPLanguageLocale | str, lenient_enum(SPLanguageLocale)] | None = Field(default=None)


class SPLocationTarget(LenientModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class SPProductCategoryRefinement(LenientModel):
    productAgeRangeId: str | None = Field(default=None, description="The age range ID to target.")
    productAgeRangeIdResolved: str | None = Field(default=None, description="The resolved age range to target.")
    productBrandId: str | None = Field(default=None, description="The brand ID to target.")
    productBrandIdResolved: str | None = Field(default=None, description="The resolved name of the brand.")
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")
    productCategoryIdResolved: str | None = Field(default=None, description="The resolved product category.")
    productGenreId: str | None = Field(default=None, description="The product genre ID to target.")
    productGenreIdResolved: str | None = Field(default=None, description="The resolved product genre to target.")
    productPriceGreaterThan: float | None = Field(
        default=None,
        description="Refinement to target products with a price greater than the value within the product category.",
    )
    productPriceLessThan: float | None = Field(
        default=None,
        description="Refinement to target products with a price less than the value within the product category.",
    )
    productPrimeShippingEligible: bool | None = Field(
        default=None, description="Target based on if a product is Prime-shipping eligible."
    )
    productRatingGreaterThan: float | None = Field(
        default=None,
        description="Refinement to target products with a rating greater than the value within the product category.",
    )
    productRatingLessThan: float | None = Field(
        default=None,
        description="Refinement to target products with a rating less than the value within the product category.",
    )


class SPProductCategoryRefinementValue(LenientModel):
    productCategoryRefinement: SPProductCategoryRefinement


class SPProductCategoryTarget(LenientModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: SPProductCategoryRefinementValue


class SPProductTarget(LenientModel):
    """Targets a specific product."""

    matchType: Annotated[SPProductMatchType | str, lenient_enum(SPProductMatchType)]
    product: SPProductValue
    productIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)]


class SPProductValue(LenientModel):
    productId: str = Field(
        description="The product identifier. Either the product id or the marketplace settings should always be specified"
    )


class SPQueryTargetRequest(StrictModel):
    adGroupIdFilter: SPTargetAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SPTargetAdProductFilter
    campaignIdFilter: SPTargetCampaignIdFilter | None = Field(default=None)
    keywordFilter: SPTargetKeywordFilter | None = Field(default=None)
    matchTypeFilter: SPTargetMatchTypeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    negativeFilter: SPTargetNegativeFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    productIdFilter: SPTargetProductIdFilter | None = Field(default=None)
    stateFilter: SPTargetStateFilter | None = Field(default=None)
    targetIdFilter: SPTargetTargetIdFilter | None = Field(default=None)
    targetTypeFilter: SPTargetTargetTypeFilter | None = Field(default=None)


class SPTarget(LenientModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    bid: SPTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime = Field(description="The date time the target was created.")
    globalTargetId: str | None = Field(
        default=None, description="The global target identifier that manages this marketplace target."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SPState | str, lenient_enum(SPState)]
    status: SPStatus | None = Field(default=None)
    tags: list[SPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: Annotated[SPTargetLevel | str, lenient_enum(SPTargetLevel)]
    targetType: Annotated[SPTargetType | str, lenient_enum(SPTargetType)]


class SPTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPTargetAdProductFilter(StrictModel):
    include: list[Annotated[SPAdProduct, lenient_enum(SPAdProduct)]] = Field(min_length=1, max_length=1)


class SPTargetBid(LenientModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")
    currencyCode: Annotated[SPCurrencyCode | str, lenient_enum(SPCurrencyCode)]


class SPTargetCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPTargetCreate(StrictModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SPAdProduct, lenient_enum(SPAdProduct)]
    bid: SPCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SPCreateState, lenient_enum(SPCreateState)]
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPCreateTargetDetails
    targetType: Annotated[SPTargetType, lenient_enum(SPTargetType)]


class SPTargetDetailsKeywordTarget(LenientModel):
    keywordTarget: SPKeywordTarget


class SPTargetDetailsLocationTarget(LenientModel):
    locationTarget: SPLocationTarget


class SPTargetDetailsProductCategoryTarget(LenientModel):
    productCategoryTarget: SPProductCategoryTarget


class SPTargetDetailsProductTarget(LenientModel):
    productTarget: SPProductTarget


class SPTargetDetailsThemeTarget(LenientModel):
    themeTarget: SPThemeTarget


type SPTargetDetails = SPTargetDetailsKeywordTarget | SPTargetDetailsLocationTarget | SPTargetDetailsProductCategoryTarget | SPTargetDetailsProductTarget | SPTargetDetailsThemeTarget


class SPTargetKeywordFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SPTargetKeywordFilterType, lenient_enum(SPTargetKeywordFilterType)]


class SPTargetMatchTypeFilter(StrictModel):
    include: list[Annotated[SPMatchType, lenient_enum(SPMatchType)]] = Field(min_length=1, max_length=10)


class SPTargetMultiStatusResponse(LenientModel):
    error: list[SPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPTargetMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=999)
    target: SPTarget


class SPTargetNegativeFilter(StrictModel):
    include: list[bool] = Field(min_length=1, max_length=1)


class SPTargetProductIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SPTargetProductIdFilterType, lenient_enum(SPTargetProductIdFilterType)]


class SPTargetStateFilter(StrictModel):
    include: list[Annotated[SPState, lenient_enum(SPState)]] = Field(min_length=1, max_length=3)


class SPTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[SPTarget] | None = Field(default=None, min_length=0, max_length=1000)


class SPTargetTargetIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPTargetTargetTypeFilter(StrictModel):
    include: list[Annotated[SPTargetType, lenient_enum(SPTargetType)]] = Field(min_length=1, max_length=4)


class SPTargetUpdate(StrictModel):
    bid: SPUpdateTargetBid | None = Field(default=None)
    state: Annotated[SPUpdateState, lenient_enum(SPUpdateState)] | None = Field(default=None)
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetId: str = Field(description="A unique identifier for the target.")


class SPThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: Annotated[SPThemeMatchType | str, lenient_enum(SPThemeMatchType)]


class SPUpdateTargetBid(StrictModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")


class SPUpdateTargetRequest(StrictModel):
    targets: list[SPTargetUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SPAdProduct",
    "SPCreateKeywordTarget",
    "SPCreateLocationTarget",
    "SPCreateProductCategoryRefinement",
    "SPCreateProductCategoryRefinementValue",
    "SPCreateProductCategoryTarget",
    "SPCreateProductTarget",
    "SPCreateProductValue",
    "SPCreateState",
    "SPCreateTag",
    "SPCreateTargetBid",
    "SPCreateTargetDetails",
    "SPCreateTargetRequest",
    "SPCreateThemeTarget",
    "SPCurrencyCode",
    "SPDeleteTargetRequest",
    "SPDeliveryReason",
    "SPDeliveryStatus",
    "SPError",
    "SPErrorCode",
    "SPErrorsIndex",
    "SPKeywordMatchType",
    "SPKeywordTarget",
    "SPLanguageLocale",
    "SPLocationTarget",
    "SPMarketplace",
    "SPMarketplaceScope",
    "SPMatchType",
    "SPProductCategoryRefinement",
    "SPProductCategoryRefinementValue",
    "SPProductCategoryTarget",
    "SPProductIdType",
    "SPProductMatchType",
    "SPProductTarget",
    "SPProductValue",
    "SPQueryTargetRequest",
    "SPState",
    "SPStatus",
    "SPTag",
    "SPTarget",
    "SPTargetAdGroupIdFilter",
    "SPTargetAdProductFilter",
    "SPTargetBid",
    "SPTargetCampaignIdFilter",
    "SPTargetCreate",
    "SPTargetDetails",
    "SPTargetKeywordFilter",
    "SPTargetKeywordFilterType",
    "SPTargetLevel",
    "SPTargetMatchTypeFilter",
    "SPTargetMultiStatusResponse",
    "SPTargetMultiStatusSuccess",
    "SPTargetNegativeFilter",
    "SPTargetProductIdFilter",
    "SPTargetProductIdFilterType",
    "SPTargetStateFilter",
    "SPTargetSuccessResponse",
    "SPTargetTargetIdFilter",
    "SPTargetTargetTypeFilter",
    "SPTargetType",
    "SPTargetUpdate",
    "SPThemeMatchType",
    "SPThemeTarget",
    "SPUpdateState",
    "SPUpdateTargetBid",
    "SPUpdateTargetRequest",
]
