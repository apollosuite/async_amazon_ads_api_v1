"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
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

type SPKeywordMatchType = Literal[
    "BROAD",  # Broad match search terms. This expands matching on user intent beyond PHRASE.
    "EXACT",  # Exact match search terms.
    "PHRASE",  # Phrase match search terms. This expands matching on user intent beyond EXACT.
]
"""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
"""


type SPLanguageLocale = Literal["zh_CN",]  # Chinese (China).
"""
A combination of ISO-639 standard for language code and ISO-3166 for country code.

Supported values:
- `zh_CN`: Chinese (China).
"""


type SPMarketplace = Literal[
    "AE",
    "AU",
    "BE",
    "BR",
    "CA",
    "DE",
    "EG",
    "ES",
    "FR",
    "GB",
    "IE",
    "IN",
    "IT",
    "JP",
    "MX",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "US",
    "ZA",
]
"""
A list of country codes representing Amazon marketplaces
"""


type SPMatchType = Literal[
    "BROAD",  # Broad match search terms. This expands matching on user intent beyond PHRASE.
    "EXACT",  # Exact match search terms.
    "KEYWORDS_CLOSE_MATCH",  # Search terms closely matching advertised product.
    "KEYWORDS_LOOSE_MATCH",  # Search terms loosely matching advertised product.
    "KEYWORDS_RELATED_TO_GIFTS",  # Search terms related to gifts.
    "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY",  # Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically.
    "KEYWORDS_RELATED_TO_PRIME_DAY",  # Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.
    "KEYWORDS_RELATED_TO_YOUR_BRAND",  # Search terms related to your brand.
    "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY",  # Search terms shoppers often use to search for products in the same category as the products you're advertising.
    "PHRASE",  # Phrase match search terms. This expands matching on user intent beyond EXACT.
    "PRODUCT_COMPLEMENTS",  # Products that complement advertised product.
    "PRODUCT_EXACT",  # Products exactly matching the specified product.
    "PRODUCT_SIMILAR",  # Products similar to the specified product.
    "PRODUCT_SUBSTITUTES",  # Products that can be substituted for advertised product.
]
"""
Supported values:
- `KEYWORDS_RELATED_TO_GIFTS`: Search terms related to gifts.
- `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY`: Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY`: Search terms shoppers often use to search for products in the same category as the products you're advertising.
- `KEYWORDS_RELATED_TO_YOUR_BRAND`: Search terms related to your brand.
- `PRODUCT_SUBSTITUTES`: Products that can be substituted for advertised product.
- `KEYWORDS_LOOSE_MATCH`: Search terms loosely matching advertised product.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
- `KEYWORDS_CLOSE_MATCH`: Search terms closely matching advertised product.
- `PRODUCT_COMPLEMENTS`: Products that complement advertised product.
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `KEYWORDS_RELATED_TO_PRIME_DAY`: Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.
"""


type SPProductMatchType = Literal[
    "PRODUCT_EXACT",  # Products exactly matching the specified product.
    "PRODUCT_SIMILAR",  # Products similar to the specified product.
]
"""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
"""


type SPTargetKeywordFilterType = Literal[
    "BROAD_MATCH",  # Filter by broad match.
    "EXACT_MATCH",  # Filter by exact match.
]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SPTargetLevel = Literal[
    "AD_GROUP",  # Target applied at the ad group level.
    "CAMPAIGN",  # Target applied at the campaign level.
]
"""
Supported values:
- `AD_GROUP`: Target applied at the ad group level.
- `CAMPAIGN`: Target applied at the campaign level.
"""


type SPTargetProductIdFilterType = Literal[
    "BROAD_MATCH",  # Filter by broad match.
    "EXACT_MATCH",  # Filter by exact match.
]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SPTargetType = Literal[
    "KEYWORD",  # Target based on customer search terms.
    "LOCATION",  # Target based on geographic location.
    "PRODUCT",  # Target based on a specific product.
    "PRODUCT_CATEGORY",  # Target based on a product category.
    "THEME",  # Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
]
"""
Supported values:
- `KEYWORD`: Target based on customer search terms.
- `LOCATION`: Target based on geographic location.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
"""


type SPThemeMatchType = Literal[
    "KEYWORDS_CLOSE_MATCH",  # Search terms closely matching advertised product.
    "KEYWORDS_LOOSE_MATCH",  # Search terms loosely matching advertised product.
    "KEYWORDS_RELATED_TO_GIFTS",  # Search terms related to gifts.
    "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY",  # Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically.
    "KEYWORDS_RELATED_TO_PRIME_DAY",  # Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.
    "KEYWORDS_RELATED_TO_YOUR_BRAND",  # Search terms related to your brand.
    "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY",  # Search terms shoppers often use to search for products in the same category as the products you're advertising.
    "PRODUCT_COMPLEMENTS",  # Products that complement advertised product.
    "PRODUCT_SUBSTITUTES",  # Products that can be substituted for advertised product.
]
"""
Supported values:
- `KEYWORDS_CLOSE_MATCH`: Search terms closely matching advertised product.
- `KEYWORDS_LOOSE_MATCH`: Search terms loosely matching advertised product.
- `KEYWORDS_RELATED_TO_GIFTS`: Search terms related to gifts.
- `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY`: Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically.
- `KEYWORDS_RELATED_TO_PRIME_DAY`: Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.
- `KEYWORDS_RELATED_TO_YOUR_BRAND`: Search terms related to your brand.
- `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY`: Search terms shoppers often use to search for products in the same category as the products you're advertising.
- `PRODUCT_COMPLEMENTS`: Products that complement advertised product.
- `PRODUCT_SUBSTITUTES`: Products that can be substituted for advertised product.
"""


class SPCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: SPKeywordMatchType = Field(description="""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
""")
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: SPLanguageLocale | None = Field(
        default=None,
        description="""
Supported values:
- `zh_CN`: Chinese (China).
""",
    )


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

    matchType: SPProductMatchType = Field(description="""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
""")
    product: SPCreateProductValue
    productIdType: SPProductIdType = Field(description="""
Supported values:
- `ASIN`: ASIN identifier type.
- `SKU`: SKU identifier type.
""")


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

    matchType: SPThemeMatchType = Field(description="""
Supported values:
- `KEYWORDS_CLOSE_MATCH`: Search terms closely matching advertised product.
- `KEYWORDS_LOOSE_MATCH`: Search terms loosely matching advertised product.
- `KEYWORDS_RELATED_TO_GIFTS`: Search terms related to gifts.
- `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY`: Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically.
- `KEYWORDS_RELATED_TO_PRIME_DAY`: Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.
- `KEYWORDS_RELATED_TO_YOUR_BRAND`: Search terms related to your brand.
- `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY`: Search terms shoppers often use to search for products in the same category as the products you're advertising.
- `PRODUCT_COMPLEMENTS`: Products that complement advertised product.
- `PRODUCT_SUBSTITUTES`: Products that can be substituted for advertised product.
""")


class SPDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SPKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: SPKeywordMatchType | str = Field(description="""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
""")
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: SPLanguageLocale | str | None = Field(
        default=None,
        description="""
Supported values:
- `zh_CN`: Chinese (China).
""",
    )


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

    matchType: SPProductMatchType | str = Field(description="""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
""")
    product: SPProductValue
    productIdType: SPProductIdType | str = Field(description="""
Supported values:
- `ASIN`: ASIN identifier type.
- `SKU`: SKU identifier type.
""")


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
    adProduct: SPAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
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
    marketplaceScope: SPMarketplaceScope | str
    marketplaces: list[SPMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: SPState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    status: SPStatus | None = Field(default=None)
    tags: list[SPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: SPTargetLevel | str = Field(description="""
Supported values:
- `AD_GROUP`: Target applied at the ad group level.
- `CAMPAIGN`: Target applied at the campaign level.
""")
    targetType: SPTargetType | str = Field(description="""
Supported values:
- `KEYWORD`: Target based on customer search terms.
- `LOCATION`: Target based on geographic location.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
""")


class SPTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPTargetAdProductFilter(StrictModel):
    include: list[SPAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""",
    )


class SPTargetBid(LenientModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")
    currencyCode: SPCurrencyCode | str = Field(description="""
Supported values:
- `AED`: United Arab Emirates Dirham
- `AUD`: Australian Dollar
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `CHF`: Swiss Franc
- `CNY`: Chinese Yuan
- `DKK`: Danish Krone
- `EGP`: Egyptian Pound
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `INR`: Indian Rupee
- `JPY`: Japanese Yen
- `MXN`: Mexican Peso
- `MXP`: Mexican Peso
- `NGN`: Nigerian Naira
- `NOK`: Norwegian Krone
- `NZD`: New Zealand Dollar
- `PLN`: Polish Złoty
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `TRY`: Turkish Lira
- `USD`: United States Dollar
- `ZAR`: South African Rand
""")


class SPTargetCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPTargetCreate(StrictModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: SPAdProduct = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
    bid: SPCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: SPCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPCreateTargetDetails
    targetType: SPTargetType = Field(description="""
Supported values:
- `KEYWORD`: Target based on customer search terms.
- `LOCATION`: Target based on geographic location.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
""")


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
    queryTermMatchType: SPTargetKeywordFilterType = Field(description="""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
""")


class SPTargetMatchTypeFilter(StrictModel):
    include: list[SPMatchType | str] = Field(
        min_length=1,
        max_length=10,
        description="""
Supported values:
- `KEYWORDS_RELATED_TO_GIFTS`: Search terms related to gifts.
- `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY`: Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY`: Search terms shoppers often use to search for products in the same category as the products you're advertising.
- `KEYWORDS_RELATED_TO_YOUR_BRAND`: Search terms related to your brand.
- `PRODUCT_SUBSTITUTES`: Products that can be substituted for advertised product.
- `KEYWORDS_LOOSE_MATCH`: Search terms loosely matching advertised product.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
- `KEYWORDS_CLOSE_MATCH`: Search terms closely matching advertised product.
- `PRODUCT_COMPLEMENTS`: Products that complement advertised product.
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `KEYWORDS_RELATED_TO_PRIME_DAY`: Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.
""",
    )


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
    queryTermMatchType: SPTargetProductIdFilterType = Field(description="""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
""")


class SPTargetStateFilter(StrictModel):
    include: list[SPState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SPTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[SPTarget] | None = Field(default=None, min_length=0, max_length=1000)


class SPTargetTargetIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPTargetTargetTypeFilter(StrictModel):
    include: list[SPTargetType | str] = Field(
        min_length=1,
        max_length=4,
        description="""
Supported values:
- `KEYWORD`: Target based on customer search terms.
- `LOCATION`: Target based on geographic location.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
""",
    )


class SPTargetUpdate(StrictModel):
    bid: SPUpdateTargetBid | None = Field(default=None)
    state: SPUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetId: str = Field(description="A unique identifier for the target.")


class SPThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: SPThemeMatchType | str = Field(description="""
Supported values:
- `KEYWORDS_CLOSE_MATCH`: Search terms closely matching advertised product.
- `KEYWORDS_LOOSE_MATCH`: Search terms loosely matching advertised product.
- `KEYWORDS_RELATED_TO_GIFTS`: Search terms related to gifts.
- `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY`: Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically.
- `KEYWORDS_RELATED_TO_PRIME_DAY`: Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.
- `KEYWORDS_RELATED_TO_YOUR_BRAND`: Search terms related to your brand.
- `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY`: Search terms shoppers often use to search for products in the same category as the products you're advertising.
- `PRODUCT_COMPLEMENTS`: Products that complement advertised product.
- `PRODUCT_SUBSTITUTES`: Products that can be substituted for advertised product.
""")


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
