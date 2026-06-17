"""Auto-generated Pydantic models for sp from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

if TYPE_CHECKING:
    from async_amazon_ads_api_v1.errors import ErrorsIndex

    from .enums import (
        SPAdProduct,
        SPCreateState,
        SPCurrencyCode,
        SPMarketplace,
        SPMarketplaceScope,
        SPProductIdType,
        SPState,
        SPUpdateState,
    )
    from .shared import SPCreateTag, SPStatus, SPTag
del TYPE_CHECKING


class SPCreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target
    matchType: Annotated[SPKeywordMatchType | str, lenient_enum(SPKeywordMatchType)]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: Annotated[SPLanguageLocale | str, lenient_enum(SPLanguageLocale)] | None = None


class SPCreateLocationTarget(BaseModel):
    """Target based on geographic location."""

    model_config = ConfigDict(extra="forbid")

    locationId: str  # The ID of the geographic location to target.


class SPCreateProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productAgeRangeId: str | None = None  # The age range ID to target.
    productBrandId: str | None = None  # The brand ID to target.
    productCategoryId: str | None = None  # The product category ID to target.
    productGenreId: str | None = None  # The product genre ID to target.
    productPriceGreaterThan: float | None = (
        None  # Refinement to target products with a price greater than the value within the product category.
    )
    productPriceLessThan: float | None = (
        None  # Refinement to target products with a price less than the value within the product category.
    )
    productPrimeShippingEligible: bool | None = None  # Target based on if a product is Prime-shipping eligible.
    productRatingGreaterThan: float | None = (
        None  # Refinement to target products with a rating greater than the value within the product category.
    )
    productRatingLessThan: float | None = (
        None  # Refinement to target products with a rating less than the value within the product category.
    )


class SPCreateProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SPCreateProductCategoryRefinement


class SPCreateProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SPCreateProductCategoryRefinementValue


class SPCreateProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SPProductMatchType | str, lenient_enum(SPProductMatchType)]
    product: SPCreateProductValue
    productIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)]


class SPCreateProductValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productId: (
        str  # The product identifier. Either the product id or the marketplace settings should always be specified
    )


class SPCreateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.


class SPCreateTargetDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keywordTarget: SPCreateKeywordTarget | None = None
    productTarget: SPCreateProductTarget | None = None
    productCategoryTarget: SPCreateProductCategoryTarget | None = None
    locationTarget: SPCreateLocationTarget | None = None
    themeTarget: SPCreateThemeTarget | None = None


class SPCreateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SPTargetCreate] | None = None


class SPCreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SPThemeMatchType | str, lenient_enum(SPThemeMatchType)]


class SPDeleteTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targetIds: list[str] | None = None


class SPKeywordMatchType(StrEnum):
    """| KeywordMatchType | Description |
    |------|------|
    | `BROAD` | Broad match search terms. This expands matching on user intent beyond PHRASE. |
    | `EXACT` | Exact match search terms. |
    | `PHRASE` | Phrase match search terms. This expands matching on user intent beyond EXACT. |
    """

    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class SPKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target
    matchType: Annotated[SPKeywordMatchType | str, lenient_enum(SPKeywordMatchType)]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: Annotated[SPLanguageLocale | str, lenient_enum(SPLanguageLocale)] | None = None


class SPLanguageLocale(StrEnum):
    """A combination of ISO-639 standard for language code and ISO-3166 for country code.

    | LanguageLocale | Description |
    |------|------|
    | `zh_CN` | Chinese (China). |
    """

    zh_CN = "zh_CN"


class SPLocationTarget(BaseModel):
    """Target based on geographic location."""

    model_config = ConfigDict(extra="forbid")

    locationId: str  # The ID of the geographic location to target.


class SPMatchType(StrEnum):
    """| MatchType | Description |
    | --- | --- |
    | `KEYWORDS_RELATED_TO_GIFTS` | Search terms related to gifts. |
    | `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY` | Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically. |
    | `PRODUCT_SIMILAR` | Products similar to the specified product. |
    | `BROAD` | Broad match search terms. This expands matching on user intent beyond PHRASE.  |
    | `EXACT` | Exact match search terms. |
    | `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY` | Search terms shoppers often use to search for products in the same category as the products you're advertising. |
    | `KEYWORDS_RELATED_TO_YOUR_BRAND` | Search terms related to your brand. |
    | `PRODUCT_SUBSTITUTES` | Products that can be substituted for advertised product. |
    | `KEYWORDS_LOOSE_MATCH` | Search terms loosely matching advertised product. |
    | `PHRASE` | Phrase match search terms. This expands matching on user intent beyond EXACT. |
    | `KEYWORDS_CLOSE_MATCH` | Search terms closely matching advertised product. |
    | `PRODUCT_COMPLEMENTS` | Products that complement advertised product. |
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    | `KEYWORDS_RELATED_TO_PRIME_DAY` | Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day. |
    """

    BROAD = "BROAD"
    EXACT = "EXACT"
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"
    KEYWORDS_RELATED_TO_GIFTS = "KEYWORDS_RELATED_TO_GIFTS"
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"
    KEYWORDS_RELATED_TO_PRIME_DAY = "KEYWORDS_RELATED_TO_PRIME_DAY"
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"
    PHRASE = "PHRASE"
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"
    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"


class SPProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productAgeRangeId: str | None = None  # The age range ID to target.
    productAgeRangeIdResolved: str | None = None  # The resolved age range to target.
    productBrandId: str | None = None  # The brand ID to target.
    productBrandIdResolved: str | None = None  # The resolved name of the brand.
    productCategoryId: str | None = None  # The product category ID to target.
    productCategoryIdResolved: str | None = None  # The resolved product category.
    productGenreId: str | None = None  # The product genre ID to target.
    productGenreIdResolved: str | None = None  # The resolved product genre to target.
    productPriceGreaterThan: float | None = (
        None  # Refinement to target products with a price greater than the value within the product category.
    )
    productPriceLessThan: float | None = (
        None  # Refinement to target products with a price less than the value within the product category.
    )
    productPrimeShippingEligible: bool | None = None  # Target based on if a product is Prime-shipping eligible.
    productRatingGreaterThan: float | None = (
        None  # Refinement to target products with a rating greater than the value within the product category.
    )
    productRatingLessThan: float | None = (
        None  # Refinement to target products with a rating less than the value within the product category.
    )


class SPProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SPProductCategoryRefinement


class SPProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SPProductCategoryRefinementValue


class SPProductMatchType(StrEnum):
    """| ProductMatchType | Description |
    |------|------|
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    | `PRODUCT_SIMILAR` | Products similar to the specified product. |
    """

    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"


class SPProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SPProductMatchType | str, lenient_enum(SPProductMatchType)]
    product: SPProductValue
    productIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)]


class SPProductValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productId: (
        str  # The product identifier. Either the product id or the marketplace settings should always be specified
    )


class SPQueryTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SPTargetAdGroupIdFilter | None = None
    adProductFilter: SPTargetAdProductFilter
    campaignIdFilter: SPTargetCampaignIdFilter | None = None
    keywordFilter: SPTargetKeywordFilter | None = None
    matchTypeFilter: SPTargetMatchTypeFilter | None = None
    maxResults: int | None = None
    negativeFilter: SPTargetNegativeFilter | None = None
    nextToken: str | None = None
    productIdFilter: SPTargetProductIdFilter | None = None
    stateFilter: SPTargetStateFilter | None = None
    targetIdFilter: SPTargetTargetIdFilter | None = None
    targetTypeFilter: SPTargetTargetTypeFilter | None = None


class SPTarget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the target. Only used for ad-group level targets.
    )
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    bid: SPTargetBid | None = None
    campaignId: str | None = (
        None  # A unique identifier for the campaign associated with the target. Only used for campaign-level targets.
    )
    creationDateTime: datetime  # The date time the target was created.
    globalTargetId: str | None = None  # The global target identifier that manages this marketplace target.
    lastUpdatedDateTime: datetime  # The date time the target was last updated.
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[
        Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]
    ]  # The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group
    negative: bool  # Indicates whether the target is negative or not.
    state: Annotated[SPState | str, lenient_enum(SPState)]
    status: SPStatus | None = None
    tags: list[SPTag] | None = None  # Open ended labels with a key value pair applied to the target
    targetDetails: SPTargetDetails
    targetId: str  # A unique identifier for the target.
    targetLevel: Annotated[SPTargetLevel | str, lenient_enum(SPTargetLevel)]
    targetType: Annotated[SPTargetType | str, lenient_enum(SPTargetType)]


class SPTargetAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPTargetAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.
    currencyCode: Annotated[SPCurrencyCode | str, lenient_enum(SPCurrencyCode)]


class SPTargetCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPTargetCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the target. Only used for ad-group level targets.
    )
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    bid: SPCreateTargetBid | None = None
    campaignId: str | None = (
        None  # A unique identifier for the campaign associated with the target. Only used for campaign-level targets.
    )
    negative: bool  # Indicates whether the target is negative or not.
    state: Annotated[SPCreateState | str, lenient_enum(SPCreateState)]
    tags: list[SPCreateTag] | None = None  # Open ended labels with a key value pair applied to the target
    targetDetails: SPCreateTargetDetails
    targetType: Annotated[SPTargetType | str, lenient_enum(SPTargetType)]


class SPTargetDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keywordTarget: SPKeywordTarget | None = None
    locationTarget: SPLocationTarget | None = None
    productCategoryTarget: SPProductCategoryTarget | None = None
    productTarget: SPProductTarget | None = None
    themeTarget: SPThemeTarget | None = None


class SPTargetKeywordFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: Annotated[SPTargetKeywordFilterType | str, lenient_enum(SPTargetKeywordFilterType)]


class SPTargetKeywordFilterType(StrEnum):
    """| TargetKeywordFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SPTargetLevel(StrEnum):
    """| TargetLevel | Description |
    |------|------|
    | `AD_GROUP` | Target applied at the ad group level. |
    | `CAMPAIGN` | Target applied at the campaign level. |
    """

    AD_GROUP = "AD_GROUP"
    CAMPAIGN = "CAMPAIGN"


class SPTargetMatchTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPMatchType | str, lenient_enum(SPMatchType)]
    ]  # MatchType Description `KEYWORDS_RELATED_TO_GIFTS` Search terms related to gifts. `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY` Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically. `PRODUCT_SIMILAR` Products similar to the specified product. `BROAD` Broad match search terms. This expands matching on user intent beyond PHRASE. `EXACT` Exact match search terms. `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY` Search terms shoppers often use to search for products in the same category as the products you're advertising. `KEYWORDS_RELATED_TO_YOUR_BRAND` Search terms related to your brand. `PRODUCT_SUBSTITUTES` Products that can be substituted for advertised product. `KEYWORDS_LOOSE_MATCH` Search terms loosely matching advertised product. `PHRASE` Phrase match search terms. This expands matching on user intent beyond EXACT. `KEYWORDS_CLOSE_MATCH` Search terms closely matching advertised product. `PRODUCT_COMPLEMENTS` Products that complement advertised product. `PRODUCT_EXACT` Products exactly matching the specified product. `KEYWORDS_RELATED_TO_PRIME_DAY` Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.


class SPTargetMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPTargetMultiStatusSuccess] | None = None


class SPTargetMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index: int
    target: SPTarget


class SPTargetNegativeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[bool]


class SPTargetProductIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: Annotated[SPTargetProductIdFilterType | str, lenient_enum(SPTargetProductIdFilterType)]


class SPTargetProductIdFilterType(StrEnum):
    """| TargetProductIdFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SPTargetStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPState | str, lenient_enum(SPState)]
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPTargetSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nextToken: str | None = None
    targets: list[SPTarget] | None = None


class SPTargetTargetIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPTargetTargetTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SPTargetType | str, lenient_enum(SPTargetType)]
    ]  # TargetType Description `KEYWORD` Target based on customer search terms. `PRODUCT` Target based on a specific product. `PRODUCT_CATEGORY` Target based on a product category. `LOCATION` Target based on geographic location. `THEME` Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.


class SPTargetType(StrEnum):
    """| TargetType | Description |
    |------|------|
    | `KEYWORD` | Target based on customer search terms. |
    | `LOCATION` | Target based on geographic location. |
    | `PRODUCT_CATEGORY` | Target based on a product category. |
    | `PRODUCT` | Target based on a specific product. |
    | `THEME` | Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products. |
    """

    KEYWORD = "KEYWORD"
    LOCATION = "LOCATION"
    PRODUCT = "PRODUCT"
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"
    THEME = "THEME"


class SPTargetUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: SPUpdateTargetBid | None = None
    state: Annotated[SPUpdateState | str, lenient_enum(SPUpdateState)] | None = None
    tags: list[SPCreateTag] | None = None  # Open ended labels with a key value pair applied to the target
    targetId: str  # A unique identifier for the target.


class SPThemeMatchType(StrEnum):
    """| ThemeMatchType | Description |
    |------|------|
    | `KEYWORDS_CLOSE_MATCH` | Search terms closely matching advertised product. |
    | `KEYWORDS_LOOSE_MATCH` | Search terms loosely matching advertised product. |
    | `KEYWORDS_RELATED_TO_GIFTS` | Search terms related to gifts. |
    | `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY` | Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically. |
    | `KEYWORDS_RELATED_TO_PRIME_DAY` | Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day. |
    | `KEYWORDS_RELATED_TO_YOUR_BRAND` | Search terms related to your brand. |
    | `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY` | Search terms shoppers often use to search for products in the same category as the products you're advertising. |
    | `PRODUCT_COMPLEMENTS` | Products that complement advertised product. |
    | `PRODUCT_SUBSTITUTES` | Products that can be substituted for advertised product. |
    """

    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"
    KEYWORDS_RELATED_TO_GIFTS = "KEYWORDS_RELATED_TO_GIFTS"
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"
    KEYWORDS_RELATED_TO_PRIME_DAY = "KEYWORDS_RELATED_TO_PRIME_DAY"
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"


class SPThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SPThemeMatchType | str, lenient_enum(SPThemeMatchType)]


class SPUpdateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.


class SPUpdateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SPTargetUpdate] | None = None


__all__ = [
    "SPCreateKeywordTarget",
    "SPCreateLocationTarget",
    "SPCreateProductCategoryRefinement",
    "SPCreateProductCategoryRefinementValue",
    "SPCreateProductCategoryTarget",
    "SPCreateProductTarget",
    "SPCreateProductValue",
    "SPCreateTargetBid",
    "SPCreateTargetDetails",
    "SPCreateTargetRequest",
    "SPCreateThemeTarget",
    "SPDeleteTargetRequest",
    "SPKeywordMatchType",
    "SPKeywordTarget",
    "SPLanguageLocale",
    "SPLocationTarget",
    "SPMatchType",
    "SPProductCategoryRefinement",
    "SPProductCategoryRefinementValue",
    "SPProductCategoryTarget",
    "SPProductMatchType",
    "SPProductTarget",
    "SPProductValue",
    "SPQueryTargetRequest",
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
    "SPUpdateTargetBid",
    "SPUpdateTargetRequest",
]
