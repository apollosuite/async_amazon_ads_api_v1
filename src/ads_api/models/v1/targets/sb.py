"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBAdProduct,
    SBCreateState,
    SBCurrencyCode,
    SBDeliveryReason,
    SBDeliveryStatus,
    SBError,
    SBErrorCode,
    SBErrorsIndex,
    SBMarketplaceScope,
    SBProductIdType,
    SBState,
    SBStatus,
    SBUpdateState,
)

type SBKeywordMatchType = Literal["BROAD", "EXACT", "PHRASE"]
"""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
"""


type SBLanguageLocale = Literal["zh_CN"]
"""
A combination of ISO-639 standard for language code and ISO-3166 for country code.

Supported values:
- `zh_CN`: Chinese (China).
"""


type SBMarketplace = Literal[
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


type SBMatchType = Literal[
    "BROAD",
    "EXACT",
    "KEYWORDS_RELATED_TO_YOUR_BRAND",
    "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES",
    "PHRASE",
    "PRODUCT_EXACT",
]
"""
Supported values:
- `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES`: Search terms related to your landing pages.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `KEYWORDS_RELATED_TO_YOUR_BRAND`: Search terms related to your brand.
- `PRODUCT_EXACT`: Products exactly matching the specified product.
"""


type SBProductMatchType = Literal["PRODUCT_EXACT"]
"""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
"""


type SBTargetKeywordFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SBTargetLevel = Literal["AD_GROUP"]
"""
Supported values:
- `AD_GROUP`: Target applied at the ad group level.
"""


type SBTargetType = Literal["KEYWORD", "PRODUCT", "PRODUCT_CATEGORY", "THEME"]
"""
Supported values:
- `KEYWORD`: Target based on customer search terms.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
"""


type SBThemeMatchType = Literal["KEYWORDS_RELATED_TO_YOUR_BRAND", "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"]
"""
Supported values:
- `KEYWORDS_RELATED_TO_YOUR_BRAND`: Search terms related to your brand.
- `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES`: Search terms related to your landing pages.
"""


class SBCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: SBKeywordMatchType
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: SBLanguageLocale | None = Field(default=None)


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

    matchType: SBProductMatchType
    product: SBCreateProductValue
    productIdType: SBProductIdType


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

    matchType: SBThemeMatchType


class SBDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SBKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: SBKeywordMatchType | str
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: SBLanguageLocale | str | None = Field(default=None)


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

    matchType: SBProductMatchType | str
    product: SBProductValue
    productIdType: SBProductIdType | str


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
    adProduct: SBAdProduct | str
    bid: SBTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime = Field(description="The date time the target was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    marketplaceScope: SBMarketplaceScope | str
    marketplaces: list[SBMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: SBState | str
    status: SBStatus | None = Field(default=None)
    targetDetails: SBTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: SBTargetLevel | str
    targetType: SBTargetType | str


class SBTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBTargetAdProductFilter(StrictModel):
    include: list[SBAdProduct] = Field(min_length=1, max_length=1)


class SBTargetBid(LenientModel):
    bid: float = Field(description="The maximum bid for a target.")
    currencyCode: SBCurrencyCode | str


class SBTargetCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBTargetCreate(StrictModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: SBAdProduct
    bid: SBCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: SBCreateState
    targetDetails: SBCreateTargetDetails
    targetType: SBTargetType


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
    queryTermMatchType: SBTargetKeywordFilterType


class SBTargetLanguageLocaleFilter(StrictModel):
    include: list[SBLanguageLocale] = Field(min_length=1, max_length=1)


class SBTargetMatchTypeFilter(StrictModel):
    include: list[SBMatchType] = Field(min_length=1, max_length=10)


class SBTargetMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SBTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SBTargetMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=999)
    target: SBTarget


class SBTargetNegativeFilter(StrictModel):
    include: list[bool] = Field(min_length=1, max_length=1)


class SBTargetStateFilter(StrictModel):
    include: list[SBState] = Field(min_length=1, max_length=3)


class SBTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[SBTarget] | None = Field(default=None, min_length=0, max_length=5000)


class SBTargetTargetIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBTargetTargetTypeFilter(StrictModel):
    include: list[SBTargetType] = Field(min_length=1, max_length=4)


class SBTargetUpdate(StrictModel):
    bid: SBUpdateTargetBid | None = Field(default=None)
    state: SBUpdateState | None = Field(default=None)
    targetId: str = Field(description="A unique identifier for the target.")


class SBThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: SBThemeMatchType | str


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
