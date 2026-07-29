"""Auto-generated models for Targets from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .ads import SBProductIdType
from .campaigns import (
    SBAdProduct,
    SBCreateState,
    SBCurrencyCode,
    SBMarketplace,
    SBMarketplaceScope,
    SBState,
    SBStatus,
    SBUpdateState,
)


class SBKeywordMatchType(StrEnum):
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


class SBLanguageLocale(StrEnum):
    """
    A combination of ISO-639 standard for language code and ISO-3166 for country code.
    **LanguageLocale Enum:**

    | LanguageLocale | Description |
    |------|------|
    | `zh_CN` | Chinese (China). |
    """

    zh_CN = "zh_CN"


class SBMatchType(StrEnum):
    """
    **MatchType Enum:**
    | MatchType | Description |
    | --- | --- |
    | `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES` | Search terms related to your landing pages. |
    | `PHRASE` | Phrase match search terms. This expands matching on user intent beyond EXACT. |
    | `BROAD` | Broad match search terms. This expands matching on user intent beyond PHRASE.  |
    | `EXACT` | Exact match search terms. |
    | `KEYWORDS_RELATED_TO_YOUR_BRAND` | Search terms related to your brand. |
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    """

    BROAD = "BROAD"
    EXACT = "EXACT"
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"
    PHRASE = "PHRASE"
    PRODUCT_EXACT = "PRODUCT_EXACT"


class SBProductMatchType(StrEnum):
    """
    **ProductMatchType Enum:**

    | ProductMatchType | Description |
    |------|------|
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    """

    PRODUCT_EXACT = "PRODUCT_EXACT"


class SBTargetKeywordFilterType(StrEnum):
    """
    **TargetKeywordFilterType Enum:**
    | TargetKeywordFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBTargetLevel(StrEnum):
    """
    **TargetLevel Enum:**

    | TargetLevel | Description |
    |------|------|
    | `AD_GROUP` | Target applied at the ad group level. |
    """

    AD_GROUP = "AD_GROUP"


class SBTargetType(StrEnum):
    """
    **TargetType Enum:**

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


class SBThemeMatchType(StrEnum):
    """
    **ThemeMatchType Enum:**

    | ThemeMatchType | Description |
    |------|------|
    | `KEYWORDS_RELATED_TO_YOUR_BRAND` | Search terms related to your brand. |
    | `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES` | Search terms related to your landing pages. |
    """

    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"


class SBCreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SBKeywordMatchType | str, lenient_enum(SBKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SBLanguageLocale | str, lenient_enum(SBLanguageLocale)] | None = Field(default=None)


class SBCreateProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="forbid")

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


class SBCreateProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SBCreateProductCategoryRefinement | None = Field(default=None)


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

    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SBCreateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float = Field(description="The maximum bid for a target.")


class SBCreateTargetDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keywordTarget: SBCreateKeywordTarget | None = None
    productTarget: SBCreateProductTarget | None = None
    productCategoryTarget: SBCreateProductCategoryTarget | None = None
    themeTarget: SBCreateThemeTarget | None = None


class SBCreateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SBTargetCreate] = Field(min_length=1, max_length=1000)


class SBCreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SBThemeMatchType | str, lenient_enum(SBThemeMatchType)]


class SBDeleteTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SBKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="allow")

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SBKeywordMatchType | str, lenient_enum(SBKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SBLanguageLocale | str, lenient_enum(SBLanguageLocale)] | None = Field(default=None)


class SBProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SBProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    productCategoryRefinement: SBProductCategoryRefinement | None = Field(default=None)


class SBProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="allow")

    productCategoryRefinement: SBProductCategoryRefinementValue


class SBProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="allow")

    matchType: Annotated[SBProductMatchType | str, lenient_enum(SBProductMatchType)]
    product: SBProductValue
    productIdType: Annotated[SBProductIdType | str, lenient_enum(SBProductIdType)]


class SBProductValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SBQueryTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

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


class SBTarget(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SBTargetAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SBTargetAdProductFilter(BaseModel):
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


class SBTargetBid(BaseModel):
    model_config = ConfigDict(extra="allow")

    bid: float = Field(description="The maximum bid for a target.")
    currencyCode: Annotated[SBCurrencyCode | str, lenient_enum(SBCurrencyCode)]


class SBTargetCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SBTargetCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    bid: SBCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SBCreateState | str, lenient_enum(SBCreateState)]
    targetDetails: SBCreateTargetDetails
    targetType: Annotated[SBTargetType | str, lenient_enum(SBTargetType)]


class SBTargetDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    keywordTarget: SBKeywordTarget | None = None
    productCategoryTarget: SBProductCategoryTarget | None = None
    productTarget: SBProductTarget | None = None
    themeTarget: SBThemeTarget | None = None


class SBTargetKeywordFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=2)
    queryTermMatchType: Annotated[SBTargetKeywordFilterType | str, lenient_enum(SBTargetKeywordFilterType)]


class SBTargetLanguageLocaleFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBLanguageLocale | str, lenient_enum(SBLanguageLocale)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**NativeLanguageLocale Enum:**
| NativeLanguageLocale | Description |
| --- | --- |
| `zh_CN` | Chinese (China). |
""",
    )


class SBTargetMatchTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBMatchType | str, lenient_enum(SBMatchType)]] = Field(
        min_length=1,
        max_length=10,
        description="""
**MatchType Enum:**
| MatchType | Description |
| --- | --- |
| `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES` | Search terms related to your landing pages. |
| `PHRASE` | Phrase match search terms. This expands matching on user intent beyond EXACT. |
| `BROAD` | Broad match search terms. This expands matching on user intent beyond PHRASE.  |
| `EXACT` | Exact match search terms. |
| `KEYWORDS_RELATED_TO_YOUR_BRAND` | Search terms related to your brand. |
| `PRODUCT_EXACT` | Products exactly matching the specified product. |
""",
    )


class SBTargetMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SBTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SBTargetMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int = Field(ge=0, le=999)
    target: SBTarget


class SBTargetNegativeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[bool] = Field(min_length=1, max_length=1)


class SBTargetStateFilter(BaseModel):
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


class SBTargetSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    nextToken: str | None = Field(default=None)
    targets: list[SBTarget] | None = Field(default=None, min_length=0, max_length=5000)


class SBTargetTargetIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SBTargetTargetTypeFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBTargetType | str, lenient_enum(SBTargetType)]] = Field(
        min_length=1,
        max_length=4,
        description="""
**TargetType Enum:**
| TargetType | Description |
| --- | --- |
| `KEYWORD` | Target based on customer search terms. |
| `PRODUCT` | Target based on a specific product. |
| `PRODUCT_CATEGORY` | Target based on a product category. |
| `THEME` | Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products. |
""",
    )


class SBTargetUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: SBUpdateTargetBid | None = Field(default=None)
    state: Annotated[SBUpdateState | str, lenient_enum(SBUpdateState)] | None = Field(default=None)
    targetId: str = Field(description="A unique identifier for the target.")


class SBThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="allow")

    matchType: Annotated[SBThemeMatchType | str, lenient_enum(SBThemeMatchType)]


class SBUpdateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = Field(default=None, description="The maximum bid for a target.")


class SBUpdateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SBTargetUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SBKeywordMatchType",
    "SBLanguageLocale",
    "SBMatchType",
    "SBProductMatchType",
    "SBTargetKeywordFilterType",
    "SBTargetLevel",
    "SBTargetType",
    "SBThemeMatchType",
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
    "SBKeywordTarget",
    "SBProductCategoryRefinement",
    "SBProductCategoryRefinementValue",
    "SBProductCategoryTarget",
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
    "SBTargetLanguageLocaleFilter",
    "SBTargetMatchTypeFilter",
    "SBTargetMultiStatusResponse",
    "SBTargetMultiStatusSuccess",
    "SBTargetNegativeFilter",
    "SBTargetStateFilter",
    "SBTargetSuccessResponse",
    "SBTargetTargetIdFilter",
    "SBTargetTargetTypeFilter",
    "SBTargetUpdate",
    "SBThemeTarget",
    "SBUpdateTargetBid",
    "SBUpdateTargetRequest",
]
