"""Auto-generated models for Targets from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorCode, ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .ads import SPProductIdType
from .campaigns import (
    SPAdProduct,
    SPCreateState,
    SPCreateTag,
    SPCurrencyCode,
    SPDeliveryReason,
    SPDeliveryStatus,
    SPMarketplace,
    SPMarketplaceScope,
    SPState,
    SPStatus,
    SPTag,
    SPUpdateState,
)


class SPKeywordMatchType(StrEnum):
    """
    **KeywordMatchType Enum:**

    | KeywordMatchType | Description |
    |------|------|
    | `BROAD` | Broad match search terms. This expands matching on user intent beyond PHRASE. |
    | `EXACT` | Exact match search terms. |
    | `PHRASE` | Phrase match search terms. This expands matching on user intent beyond EXACT. |
    """

    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class SPLanguageLocale(StrEnum):
    """
    A combination of ISO-639 standard for language code and ISO-3166 for country code.
    **LanguageLocale Enum:**

    | LanguageLocale | Description |
    |------|------|
    | `zh_CN` | Chinese (China). |
    """

    zh_CN = "zh_CN"


class SPMatchType(StrEnum):
    """
    **MatchType Enum:**
    | MatchType | Description |
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


class SPProductMatchType(StrEnum):
    """
    **ProductMatchType Enum:**

    | ProductMatchType | Description |
    |------|------|
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    | `PRODUCT_SIMILAR` | Products similar to the specified product. |
    """

    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"


class SPTargetKeywordFilterType(StrEnum):
    """
    **TargetKeywordFilterType Enum:**
    | TargetKeywordFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SPTargetLevel(StrEnum):
    """
    **TargetLevel Enum:**

    | TargetLevel | Description |
    |------|------|
    | `AD_GROUP` | Target applied at the ad group level. |
    | `CAMPAIGN` | Target applied at the campaign level. |
    """

    AD_GROUP = "AD_GROUP"
    CAMPAIGN = "CAMPAIGN"


class SPTargetProductIdFilterType(StrEnum):
    """
    **TargetProductIdFilterType Enum:**
    | TargetProductIdFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SPTargetType(StrEnum):
    """
    **TargetType Enum:**

    | TargetType | Description |
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


class SPThemeMatchType(StrEnum):
    """
    **ThemeMatchType Enum:**

    | ThemeMatchType | Description |
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


class SPCreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SPKeywordMatchType | str, lenient_enum(SPKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SPLanguageLocale | str, lenient_enum(SPLanguageLocale)] | None = Field(default=None)


class SPCreateLocationTarget(BaseModel):
    """Target based on geographic location."""

    model_config = ConfigDict(extra="forbid")

    locationId: str = Field(description="The ID of the geographic location to target.")


class SPCreateProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="forbid")

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

    productId: str = Field(
        description="The product identifier. Either the product id or the marketplace settings should always be specified"
    )


class SPCreateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = Field(default=None, description="The maximum bid for a target.")


class SPCreateTargetDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keywordTarget: SPCreateKeywordTarget | None = None
    productTarget: SPCreateProductTarget | None = None
    productCategoryTarget: SPCreateProductCategoryTarget | None = None
    locationTarget: SPCreateLocationTarget | None = None
    themeTarget: SPCreateThemeTarget | None = None


class SPCreateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SPTargetCreate] = Field(min_length=1, max_length=1000)


class SPCreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SPThemeMatchType | str, lenient_enum(SPThemeMatchType)]


class SPDeleteTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SPKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="allow")

    keyword: str | None = Field(
        default=None,
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints).",
    )
    matchType: Annotated[SPKeywordMatchType | str, lenient_enum(SPKeywordMatchType)] | None = Field(default=None)
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SPLanguageLocale | str, lenient_enum(SPLanguageLocale)] | None = Field(default=None)


class SPLocationTarget(BaseModel):
    """Target based on geographic location."""

    model_config = ConfigDict(extra="allow")

    locationId: str | None = Field(default=None, description="The ID of the geographic location to target.")


class SPProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SPProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    productCategoryRefinement: SPProductCategoryRefinement | None = Field(default=None)


class SPProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="allow")

    productCategoryRefinement: SPProductCategoryRefinementValue | None = Field(default=None)


class SPProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="allow")

    matchType: Annotated[SPProductMatchType | str, lenient_enum(SPProductMatchType)] | None = Field(default=None)
    product: SPProductValue | None = Field(default=None)
    productIdType: Annotated[SPProductIdType | str, lenient_enum(SPProductIdType)] | None = Field(default=None)


class SPProductValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SPQueryTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

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


class SPTarget(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)] | None = Field(default=None)
    bid: SPTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time the target was created.")
    globalTargetId: str | None = Field(
        default=None, description="The global target identifier that manages this marketplace target."
    )
    lastUpdatedDateTime: datetime | None = Field(default=None, description="The date time the target was last updated.")
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)] | None = Field(default=None)
    marketplaces: list[Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    negative: bool | None = Field(default=None, description="Indicates whether the target is negative or not.")
    state: Annotated[SPState | str, lenient_enum(SPState)] | None = Field(default=None)
    status: SPStatus | None = Field(default=None)
    tags: list[SPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPTargetDetails | None = Field(default=None)
    targetId: str | None = Field(default=None, description="A unique identifier for the target.")
    targetLevel: Annotated[SPTargetLevel | str, lenient_enum(SPTargetLevel)] | None = Field(default=None)
    targetType: Annotated[SPTargetType | str, lenient_enum(SPTargetType)] | None = Field(default=None)


class SPTargetAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPTargetAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_PRODUCTS` | Sponsored Products ad product. |
""",
    )


class SPTargetBid(BaseModel):
    model_config = ConfigDict(extra="allow")

    bid: float | None = Field(default=None, description="The maximum bid for a target.")
    currencyCode: Annotated[SPCurrencyCode | str, lenient_enum(SPCurrencyCode)] | None = Field(default=None)


class SPTargetCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPTargetCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    bid: SPCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SPCreateState | str, lenient_enum(SPCreateState)]
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPCreateTargetDetails
    targetType: Annotated[SPTargetType | str, lenient_enum(SPTargetType)]


class SPTargetDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    keywordTarget: SPKeywordTarget | None = None
    locationTarget: SPLocationTarget | None = None
    productCategoryTarget: SPProductCategoryTarget | None = None
    productTarget: SPProductTarget | None = None
    themeTarget: SPThemeTarget | None = None


class SPTargetKeywordFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SPTargetKeywordFilterType | str, lenient_enum(SPTargetKeywordFilterType)]


class SPTargetMatchTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPMatchType | str, lenient_enum(SPMatchType)]] = Field(
        min_length=1,
        max_length=10,
        description="""
**MatchType Enum:**
| MatchType | Description |
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
""",
    )


class SPTargetMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPTargetMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int | None = Field(default=None, ge=0, le=999)
    target: SPTarget | None = Field(default=None)


class SPTargetNegativeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[bool] = Field(min_length=1, max_length=1)


class SPTargetProductIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SPTargetProductIdFilterType | str, lenient_enum(SPTargetProductIdFilterType)]


class SPTargetStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPState | str, lenient_enum(SPState)]] = Field(
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


class SPTargetSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    nextToken: str | None = Field(default=None)
    targets: list[SPTarget] | None = Field(default=None, min_length=0, max_length=1000)


class SPTargetTargetIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPTargetTargetTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPTargetType | str, lenient_enum(SPTargetType)]] = Field(
        min_length=1,
        max_length=4,
        description="""
**TargetType Enum:**
| TargetType | Description |
| --- | --- |
| `KEYWORD` | Target based on customer search terms. |
| `PRODUCT` | Target based on a specific product. |
| `PRODUCT_CATEGORY` | Target based on a product category. |
| `LOCATION` | Target based on geographic location. |
| `THEME` | Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products. |
""",
    )


class SPTargetUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: SPUpdateTargetBid | None = Field(default=None)
    state: Annotated[SPUpdateState | str, lenient_enum(SPUpdateState)] | None = Field(default=None)
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetId: str = Field(description="A unique identifier for the target.")


class SPThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="allow")

    matchType: Annotated[SPThemeMatchType | str, lenient_enum(SPThemeMatchType)] | None = Field(default=None)


class SPUpdateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = Field(default=None, description="The maximum bid for a target.")


class SPUpdateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SPTargetUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "ErrorCode",
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
    "SPKeywordMatchType",
    "SPLanguageLocale",
    "SPMarketplace",
    "SPMarketplaceScope",
    "SPMatchType",
    "SPProductIdType",
    "SPProductMatchType",
    "SPQueryTargetRequest",
    "SPState",
    "SPTargetAdGroupIdFilter",
    "SPTargetAdProductFilter",
    "SPTargetCampaignIdFilter",
    "SPTargetCreate",
    "SPTargetKeywordFilter",
    "SPTargetKeywordFilterType",
    "SPTargetLevel",
    "SPTargetMatchTypeFilter",
    "SPTargetNegativeFilter",
    "SPTargetProductIdFilter",
    "SPTargetProductIdFilterType",
    "SPTargetStateFilter",
    "SPTargetTargetIdFilter",
    "SPTargetTargetTypeFilter",
    "SPTargetType",
    "SPTargetUpdate",
    "SPThemeMatchType",
    "SPUpdateState",
    "SPUpdateTargetBid",
    "SPUpdateTargetRequest",
]
