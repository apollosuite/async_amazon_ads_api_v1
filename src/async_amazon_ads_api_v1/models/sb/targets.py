"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

if TYPE_CHECKING:
    from .enums import (
        SBAdProduct,
        SBCreateState,
        SBCurrencyCode,
        SBMarketplace,
        SBMarketplaceScope,
        SBProductIdType,
        SBState,
        SBUpdateState,
    )
    from .shared import SBStatus
del TYPE_CHECKING


class SBCreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints).
    matchType: Annotated[SBKeywordMatchType | str, lenient_enum(SBKeywordMatchType)]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: Annotated[SBLanguageLocale | str, lenient_enum(SBLanguageLocale)] | None = None


class SBCreateProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productBrandId: str | None = None  # The brand ID to target.
    productCategoryId: str | None = None  # The product category ID to target.
    productPriceGreaterThan: float | None = (
        None  # Refinement to target products with a price greater than the value within the product category.
    )
    productPriceLessThan: float | None = (
        None  # Refinement to target products with a price less than the value within the product category.
    )
    productRatingGreaterThan: float | None = (
        None  # Refinement to target products with a rating greater than the value within the product category.
    )
    productRatingLessThan: float | None = (
        None  # Refinement to target products with a rating less than the value within the product category.
    )


class SBCreateProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SBCreateProductCategoryRefinement | None = None


class SBCreateProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SBCreateProductCategoryRefinementValue


class SBCreateProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SBProductMatchType | str, lenient_enum(SBProductMatchType)]
    product: SBCreateProductValue
    productIdType: Annotated[SBProductIdType | str, lenient_enum(SBProductIdType)]


class SBCreateProductValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productId: str | None = (
        None  # The product identifier. Either the product id or the marketplace settings should always be specified
    )


class SBCreateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float  # The maximum bid for a target.


class SBCreateTargetDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keywordTarget: SBCreateKeywordTarget | None = None
    productTarget: SBCreateProductTarget | None = None
    productCategoryTarget: SBCreateProductCategoryTarget | None = None
    themeTarget: SBCreateThemeTarget | None = None


class SBCreateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SBTargetCreate]


class SBCreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SBThemeMatchType | str, lenient_enum(SBThemeMatchType)]


class SBDeleteTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targetIds: list[str]


class SBKeywordMatchType(StrEnum):
    """**KeywordMatchType Enum:**

    | KeywordMatchType | Description |
    |------|------|
    | `BROAD` | Broad match search terms. This expands matching on user intent beyond PHRASE. |
    | `EXACT` | Exact match search terms. |
    | `PHRASE` | Phrase match search terms. This expands matching on user intent beyond EXACT. |
    """

    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"


class SBKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints).
    matchType: Annotated[SBKeywordMatchType | str, lenient_enum(SBKeywordMatchType)]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: Annotated[SBLanguageLocale | str, lenient_enum(SBLanguageLocale)] | None = None


class SBLanguageLocale(StrEnum):
    """A combination of ISO-639 standard for language code and ISO-3166 for country code.
    **LanguageLocale Enum:**

    | LanguageLocale | Description |
    |------|------|
    | `zh_CN` | Chinese (China). |
    """

    zh_CN = "zh_CN"


class SBMatchType(StrEnum):
    """**MatchType Enum:**
    | MatchType | Description |
    | --- | --- |
    | `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES` | Search terms related to your landing pages. |
    | `PHRASE` | Phrase match search terms. This expands matching on user intent beyond EXACT. |
    | `BROAD` | Broad match search terms. This expands matching on user intent beyond PHRASE.  |
    | `EXACT` | Exact match search terms. |
    | `KEYWORDS_RELATED_TO_YOUR_BRAND` | Search terms related to your brand. |
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |"""

    BROAD = "BROAD"
    EXACT = "EXACT"
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"
    PHRASE = "PHRASE"
    PRODUCT_EXACT = "PRODUCT_EXACT"


class SBProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productBrandId: str | None = None  # The brand ID to target.
    productCategoryId: str | None = None  # The product category ID to target.
    productPriceGreaterThan: float | None = (
        None  # Refinement to target products with a price greater than the value within the product category.
    )
    productPriceLessThan: float | None = (
        None  # Refinement to target products with a price less than the value within the product category.
    )
    productRatingGreaterThan: float | None = (
        None  # Refinement to target products with a rating greater than the value within the product category.
    )
    productRatingLessThan: float | None = (
        None  # Refinement to target products with a rating less than the value within the product category.
    )


class SBProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SBProductCategoryRefinement | None = None


class SBProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SBProductCategoryRefinementValue


class SBProductMatchType(StrEnum):
    """**ProductMatchType Enum:**

    | ProductMatchType | Description |
    |------|------|
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    """

    PRODUCT_EXACT = "PRODUCT_EXACT"


class SBProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SBProductMatchType | str, lenient_enum(SBProductMatchType)]
    product: SBProductValue
    productIdType: Annotated[SBProductIdType | str, lenient_enum(SBProductIdType)]


class SBProductValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productId: str | None = (
        None  # The product identifier. Either the product id or the marketplace settings should always be specified
    )


class SBQueryTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SBTargetAdGroupIdFilter | None = None
    adProductFilter: SBTargetAdProductFilter
    campaignIdFilter: SBTargetCampaignIdFilter | None = None
    keywordFilter: SBTargetKeywordFilter | None = None
    matchTypeFilter: SBTargetMatchTypeFilter | None = None
    maxResults: int | None = None
    nativeLanguageLocaleFilter: SBTargetLanguageLocaleFilter | None = None
    negativeFilter: SBTargetNegativeFilter | None = None
    nextToken: str | None = None
    stateFilter: SBTargetStateFilter | None = None
    targetIdFilter: SBTargetTargetIdFilter | None = None
    targetTypeFilter: SBTargetTargetTypeFilter | None = None


class SBTarget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: (
        str  # A unique identifier for the ad group associated with the target. Only used for ad-group level targets.
    )
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    bid: SBTargetBid | None = None
    campaignId: str | None = (
        None  # A unique identifier for the campaign associated with the target. Only used for campaign-level targets.
    )
    creationDateTime: datetime  # The date time the target was created.
    lastUpdatedDateTime: datetime  # The date time the target was last updated.
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[
        Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]
    ]  # The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group
    negative: bool  # Indicates whether the target is negative or not.
    state: Annotated[SBState | str, lenient_enum(SBState)]
    status: SBStatus | None = None
    targetDetails: SBTargetDetails
    targetId: str  # A unique identifier for the target.
    targetLevel: Annotated[SBTargetLevel | str, lenient_enum(SBTargetLevel)]
    targetType: Annotated[SBTargetType | str, lenient_enum(SBTargetType)]


class SBTargetAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBTargetAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    ]  # **AdProduct Enum:** AdProduct Description `SPONSORED_BRANDS` Sponsored Brands ad product.


class SBTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float  # The maximum bid for a target.
    currencyCode: Annotated[SBCurrencyCode | str, lenient_enum(SBCurrencyCode)]


class SBTargetCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBTargetCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: (
        str  # A unique identifier for the ad group associated with the target. Only used for ad-group level targets.
    )
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    bid: SBCreateTargetBid | None = None
    campaignId: str | None = (
        None  # A unique identifier for the campaign associated with the target. Only used for campaign-level targets.
    )
    negative: bool  # Indicates whether the target is negative or not.
    state: Annotated[SBCreateState | str, lenient_enum(SBCreateState)]
    targetDetails: SBCreateTargetDetails
    targetType: Annotated[SBTargetType | str, lenient_enum(SBTargetType)]


class SBTargetDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keywordTarget: SBKeywordTarget | None = None
    productCategoryTarget: SBProductCategoryTarget | None = None
    productTarget: SBProductTarget | None = None
    themeTarget: SBThemeTarget | None = None


class SBTargetKeywordFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: Annotated[SBTargetKeywordFilterType | str, lenient_enum(SBTargetKeywordFilterType)]


class SBTargetKeywordFilterType(StrEnum):
    """**TargetKeywordFilterType Enum:**
    | TargetKeywordFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBTargetLanguageLocaleFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBLanguageLocale | str, lenient_enum(SBLanguageLocale)]
    ]  # **NativeLanguageLocale Enum:** NativeLanguageLocale Description `zh_CN` Chinese (China).


class SBTargetLevel(StrEnum):
    """**TargetLevel Enum:**

    | TargetLevel | Description |
    |------|------|
    | `AD_GROUP` | Target applied at the ad group level. |
    """

    AD_GROUP = "AD_GROUP"


class SBTargetMatchTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBMatchType | str, lenient_enum(SBMatchType)]
    ]  # **MatchType Enum:** MatchType Description `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES` Search terms related to your landing pages. `PHRASE` Phrase match search terms. This expands matching on user intent beyond EXACT. `BROAD` Broad match search terms. This expands matching on user intent beyond PHRASE. `EXACT` Exact match search terms. `KEYWORDS_RELATED_TO_YOUR_BRAND` Search terms related to your brand. `PRODUCT_EXACT` Products exactly matching the specified product.


class SBTargetMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBTargetMultiStatusSuccess] | None = None


class SBTargetMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index: int
    target: SBTarget


class SBTargetNegativeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[bool]


class SBTargetStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBState | str, lenient_enum(SBState)]
    ]  # **State Enum:** State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SBTargetSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nextToken: str | None = None
    targets: list[SBTarget] | None = None


class SBTargetTargetIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBTargetTargetTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SBTargetType | str, lenient_enum(SBTargetType)]
    ]  # **TargetType Enum:** TargetType Description `KEYWORD` Target based on customer search terms. `PRODUCT` Target based on a specific product. `PRODUCT_CATEGORY` Target based on a product category. `THEME` Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.


class SBTargetType(StrEnum):
    """**TargetType Enum:**

    | TargetType | Description |
    |------|------|
    | `KEYWORD` | Target based on customer search terms. |
    | `PRODUCT_CATEGORY` | Target based on a product category. |
    | `PRODUCT` | Target based on a specific product. |
    | `THEME` | Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products. |
    """

    KEYWORD = "KEYWORD"
    PRODUCT = "PRODUCT"
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"
    THEME = "THEME"


class SBTargetUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: SBUpdateTargetBid | None = None
    state: Annotated[SBUpdateState | str, lenient_enum(SBUpdateState)] | None = None
    targetId: str  # A unique identifier for the target.


class SBThemeMatchType(StrEnum):
    """**ThemeMatchType Enum:**

    | ThemeMatchType | Description |
    |------|------|
    | `KEYWORDS_RELATED_TO_YOUR_BRAND` | Search terms related to your brand. |
    | `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES` | Search terms related to your landing pages. |
    """

    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"


class SBThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SBThemeMatchType | str, lenient_enum(SBThemeMatchType)]


class SBUpdateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.


class SBUpdateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SBTargetUpdate]


__all__ = [
    "SBCreateKeywordTarget",
    "SBCreateProductCategoryRefinement",
    "SBCreateProductCategoryRefinementValue",
    "SBCreateProductCategoryTarget",
    "SBCreateProductTarget",
    "SBCreateProductValue",
    "SBCreateTargetBid",
    "SBCreateTargetDetails",
    "SBCreateTargetRequest",
    "SBCreateThemeTarget",
    "SBDeleteTargetRequest",
    "SBKeywordMatchType",
    "SBKeywordTarget",
    "SBLanguageLocale",
    "SBMatchType",
    "SBProductCategoryRefinement",
    "SBProductCategoryRefinementValue",
    "SBProductCategoryTarget",
    "SBProductMatchType",
    "SBProductTarget",
    "SBProductValue",
    "SBQueryTargetRequest",
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
    "SBUpdateTargetBid",
    "SBUpdateTargetRequest",
]
