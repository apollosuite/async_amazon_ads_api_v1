"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sp_global import (
    SPGlobalAdProduct,
    SPGlobalCreateState,
    SPGlobalCreateTag,
    SPGlobalCurrencyCode,
    SPGlobalDeliveryReason,
    SPGlobalDeliveryStatus,
    SPGlobalError,
    SPGlobalErrorCode,
    SPGlobalErrorMarketplace,
    SPGlobalErrorsIndex,
    SPGlobalMarketplaceScope,
    SPGlobalProductIdType,
    SPGlobalState,
    SPGlobalTag,
    SPGlobalUpdateState,
)

type SPGlobalKeywordMatchType = Literal["BROAD", "EXACT", "PHRASE"]
"""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
"""


type SPGlobalLanguageLocale = Literal["zh_CN"]
"""
A combination of ISO-639 standard for language code and ISO-3166 for country code.

Supported values:
- `zh_CN`: Chinese (China).
"""


type SPGlobalMarketplace = Literal[
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
]
"""
A list of country codes representing Amazon marketplaces
"""


type SPGlobalMatchType = Literal[
    "BROAD",
    "EXACT",
    "KEYWORDS_CLOSE_MATCH",
    "KEYWORDS_LOOSE_MATCH",
    "PHRASE",
    "PRODUCT_COMPLEMENTS",
    "PRODUCT_EXACT",
    "PRODUCT_SIMILAR",
    "PRODUCT_SUBSTITUTES",
]
"""
Supported values:
- `PRODUCT_SIMILAR`: Products similar to the specified product.
- `KEYWORDS_LOOSE_MATCH`: Search terms loosely matching advertised product.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `KEYWORDS_CLOSE_MATCH`: Search terms closely matching advertised product.
- `PRODUCT_COMPLEMENTS`: Products that complement advertised product.
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SUBSTITUTES`: Products that can be substituted for advertised product.
"""


type SPGlobalProductMatchType = Literal["PRODUCT_EXACT", "PRODUCT_SIMILAR"]
"""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
"""


type SPGlobalTargetLevel = Literal["AD_GROUP", "CAMPAIGN"]
"""
Supported values:
- `AD_GROUP`: Target applied at the ad group level.
- `CAMPAIGN`: Target applied at the campaign level.
"""


type SPGlobalTargetProductIdFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SPGlobalTargetType = Literal["KEYWORD", "PRODUCT", "PRODUCT_CATEGORY", "THEME"]
"""
Supported values:
- `KEYWORD`: Target based on customer search terms.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
"""


type SPGlobalThemeMatchType = Literal[
    "KEYWORDS_CLOSE_MATCH", "KEYWORDS_LOOSE_MATCH", "PRODUCT_COMPLEMENTS", "PRODUCT_SUBSTITUTES"
]
"""
Supported values:
- `KEYWORDS_CLOSE_MATCH`: Search terms closely matching advertised product.
- `KEYWORDS_LOOSE_MATCH`: Search terms loosely matching advertised product.
- `PRODUCT_COMPLEMENTS`: Products that complement advertised product.
- `PRODUCT_SUBSTITUTES`: Products that can be substituted for advertised product.
"""


class SPGlobalCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: SPGlobalKeywordMatchType
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: SPGlobalLanguageLocale | None = Field(default=None)


class SPGlobalCreateMarketplaceTargetConfigurations(StrictModel):
    marketplace: SPGlobalMarketplace
    overrides: SPGlobalCreateMarketplaceTargetFieldOverrides


class SPGlobalCreateMarketplaceTargetFieldOverrides(StrictModel):
    state: SPGlobalState | None = Field(default=None)
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPGlobalCreateOverridableTargets | None = Field(default=None)


class SPGlobalCreateOverridableTargetsKeywordTarget(StrictModel):
    keywordTarget: SPGlobalCreateKeywordTarget


class SPGlobalCreateOverridableTargetsThemeTarget(StrictModel):
    themeTarget: SPGlobalCreateThemeTarget


type SPGlobalCreateOverridableTargets = SPGlobalCreateOverridableTargetsKeywordTarget | SPGlobalCreateOverridableTargetsThemeTarget


class SPGlobalCreateProductCategoryRefinement(StrictModel):
    productAgeRangeId: str | None = Field(default=None, description="The age range ID to target.")
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


class SPGlobalCreateProductCategoryRefinementMarketplaceSetting(StrictModel):
    marketplace: SPGlobalMarketplace
    productCategoryRefinement: SPGlobalCreateProductCategoryRefinement


class SPGlobalCreateProductCategoryRefinementValue(StrictModel):
    marketplaceSettings: list[SPGlobalCreateProductCategoryRefinementMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="Marketplace specific product category refinements. Either the value or the marketplaceSettings should always be specified",
    )


class SPGlobalCreateProductCategoryTarget(StrictModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: SPGlobalCreateProductCategoryRefinementValue
    productGenreRefinement: SPGlobalCreateProductGenreRefinement | None = Field(default=None)


class SPGlobalCreateProductGenreRefinement(StrictModel):
    productGenreId: str = Field(description="The product genre ID to target.")


class SPGlobalCreateProductMarketplaceSetting(StrictModel):
    marketplace: SPGlobalMarketplace
    productId: str = Field(description="The product id applicable at the specified marketplace.")


class SPGlobalCreateProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: SPGlobalProductMatchType
    product: SPGlobalCreateProductValue
    productIdType: SPGlobalProductIdType


class SPGlobalCreateProductValue(StrictModel):
    marketplaceSettings: list[SPGlobalCreateProductMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="The product ids at specific marketplace level. Either the product id or the marketplace settings should always be specified",
    )
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SPGlobalCreateTargetBid(StrictModel):
    marketplaceSettings: list[SPGlobalCreateTargetBidMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The bid associated with the target at specified marketplace level. Either one of bid or marketplaceSettings should always be specified",
    )


class SPGlobalCreateTargetBidMarketplaceSetting(StrictModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")
    currencyCode: SPGlobalCurrencyCode
    marketplace: SPGlobalMarketplace


class SPGlobalCreateTargetDetailsKeywordTarget(StrictModel):
    keywordTarget: SPGlobalCreateKeywordTarget


class SPGlobalCreateTargetDetailsProductTarget(StrictModel):
    productTarget: SPGlobalCreateProductTarget


class SPGlobalCreateTargetDetailsProductCategoryTarget(StrictModel):
    productCategoryTarget: SPGlobalCreateProductCategoryTarget


class SPGlobalCreateTargetDetailsThemeTarget(StrictModel):
    themeTarget: SPGlobalCreateThemeTarget


type SPGlobalCreateTargetDetails = SPGlobalCreateTargetDetailsKeywordTarget | SPGlobalCreateTargetDetailsProductTarget | SPGlobalCreateTargetDetailsProductCategoryTarget | SPGlobalCreateTargetDetailsThemeTarget


class SPGlobalCreateTargetRequest(StrictModel):
    targets: list[SPGlobalTargetCreate] = Field(min_length=1, max_length=1000)


class SPGlobalCreateThemeTarget(StrictModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: SPGlobalThemeMatchType


class SPGlobalDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: SPGlobalKeywordMatchType | str
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: SPGlobalLanguageLocale | str | None = Field(default=None)


class SPGlobalMarketplaceTargetConfigurations(LenientModel):
    marketplace: SPGlobalMarketplace | str
    overrides: SPGlobalMarketplaceTargetFieldOverrides
    targetId: str = Field(
        description="Represents marketplace target id (Ex: targetId-US) associated to global target (Ex: targetId-Global)"
    )


class SPGlobalMarketplaceTargetFieldOverrides(LenientModel):
    state: SPGlobalState | str | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPGlobalOverridableTargets | None = Field(default=None)


class SPGlobalOverridableTargetsKeywordTarget(LenientModel):
    keywordTarget: SPGlobalKeywordTarget


class SPGlobalOverridableTargetsThemeTarget(LenientModel):
    themeTarget: SPGlobalThemeTarget


type SPGlobalOverridableTargets = SPGlobalOverridableTargetsKeywordTarget | SPGlobalOverridableTargetsThemeTarget


class SPGlobalProductCategoryRefinement(LenientModel):
    productAgeRangeId: str | None = Field(default=None, description="The age range ID to target.")
    productAgeRangeIdResolved: str | None = Field(default=None, description="The resolved age range to target.")
    productBrandId: str | None = Field(default=None, description="The brand ID to target.")
    productBrandIdResolved: str | None = Field(default=None, description="The resolved name of the brand.")
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")
    productCategoryIdResolved: str | None = Field(default=None, description="The resolved product category.")
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


class SPGlobalProductCategoryRefinementMarketplaceSetting(LenientModel):
    marketplace: SPGlobalMarketplace | str
    productCategoryRefinement: SPGlobalProductCategoryRefinement


class SPGlobalProductCategoryRefinementValue(LenientModel):
    marketplaceSettings: list[SPGlobalProductCategoryRefinementMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="Marketplace specific product category refinements. Either the value or the marketplaceSettings should always be specified",
    )


class SPGlobalProductCategoryTarget(LenientModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: SPGlobalProductCategoryRefinementValue
    productGenreRefinement: SPGlobalProductGenreRefinement | None = Field(default=None)


class SPGlobalProductGenreRefinement(LenientModel):
    productGenreId: str = Field(description="The product genre ID to target.")
    productGenreIdResolved: str | None = Field(default=None, description="The resolved product genre to target.")


class SPGlobalProductMarketplaceSetting(LenientModel):
    marketplace: SPGlobalMarketplace | str
    productId: str = Field(description="The product id applicable at the specified marketplace.")


class SPGlobalProductTarget(LenientModel):
    """Targets a specific product."""

    matchType: SPGlobalProductMatchType | str
    product: SPGlobalProductValue
    productIdType: SPGlobalProductIdType | str


class SPGlobalProductValue(LenientModel):
    marketplaceSettings: list[SPGlobalProductMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="The product ids at specific marketplace level. Either the product id or the marketplace settings should always be specified",
    )
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SPGlobalQueryTargetRequest(StrictModel):
    adGroupIdFilter: SPGlobalTargetAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SPGlobalTargetAdProductFilter
    campaignIdFilter: SPGlobalTargetCampaignIdFilter | None = Field(default=None)
    marketplaceScopeFilter: SPGlobalTargetMarketplaceScopeFilter | None = Field(default=None)
    matchTypeFilter: SPGlobalTargetMatchTypeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=5000, ge=1, le=5000)
    negativeFilter: SPGlobalTargetNegativeFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    productIdFilter: SPGlobalTargetProductIdFilter | None = Field(default=None)
    stateFilter: SPGlobalTargetStateFilter | None = Field(default=None)
    targetIdFilter: SPGlobalTargetTargetIdFilter | None = Field(default=None)
    targetTypeFilter: SPGlobalTargetTargetTypeFilter | None = Field(default=None)


class SPGlobalStatus(LenientModel):
    deliveryReasons: list[SPGlobalDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: SPGlobalDeliveryStatus | str
    marketplaceSettings: list[SPGlobalStatusMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace level delivery status and reasons of global resources, for all the marketplaces the global resource is applicable in.",
    )


class SPGlobalStatusMarketplaceSetting(LenientModel):
    deliveryReasons: list[SPGlobalDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: SPGlobalDeliveryStatus | str
    marketplace: SPGlobalMarketplace | str


class SPGlobalTarget(LenientModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: SPGlobalAdProduct | str
    bid: SPGlobalTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime = Field(description="The date time the target was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    marketplaceConfigurations: list[SPGlobalMarketplaceTargetConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual marketplace level. For example, if a global target is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the target's global value is applied to that marketplace.",
    )
    marketplaceScope: SPGlobalMarketplaceScope | str
    marketplaces: list[SPGlobalMarketplace | str] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: SPGlobalState | str
    status: SPGlobalStatus | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPGlobalTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: SPGlobalTargetLevel | str
    targetType: SPGlobalTargetType | str


class SPGlobalTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalTargetAdProductFilter(StrictModel):
    include: list[SPGlobalAdProduct | str] = Field(min_length=1, max_length=1)


class SPGlobalTargetBid(LenientModel):
    marketplaceSettings: list[SPGlobalTargetBidMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The bid associated with the target at specified marketplace level. Either one of bid or marketplaceSettings should always be specified",
    )


class SPGlobalTargetBidMarketplaceSetting(LenientModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")
    currencyCode: SPGlobalCurrencyCode | str
    marketplace: SPGlobalMarketplace | str


class SPGlobalTargetCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalTargetCreate(StrictModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: SPGlobalAdProduct
    bid: SPGlobalCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceTargetConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual marketplace level. For example, if a global target is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the target's global value is applied to that marketplace.",
    )
    marketplaceScope: SPGlobalMarketplaceScope
    marketplaces: list[SPGlobalMarketplace | str] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: SPGlobalCreateState
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPGlobalCreateTargetDetails
    targetType: SPGlobalTargetType


class SPGlobalTargetDetailsKeywordTarget(LenientModel):
    keywordTarget: SPGlobalKeywordTarget


class SPGlobalTargetDetailsProductCategoryTarget(LenientModel):
    productCategoryTarget: SPGlobalProductCategoryTarget


class SPGlobalTargetDetailsProductTarget(LenientModel):
    productTarget: SPGlobalProductTarget


class SPGlobalTargetDetailsThemeTarget(LenientModel):
    themeTarget: SPGlobalThemeTarget


type SPGlobalTargetDetails = SPGlobalTargetDetailsKeywordTarget | SPGlobalTargetDetailsProductCategoryTarget | SPGlobalTargetDetailsProductTarget | SPGlobalTargetDetailsThemeTarget


class SPGlobalTargetMarketplaceScopeFilter(StrictModel):
    include: list[SPGlobalMarketplaceScope | str] = Field(min_length=1, max_length=1)


class SPGlobalTargetMatchTypeFilter(StrictModel):
    include: list[SPGlobalMatchType | str] = Field(min_length=1, max_length=10)


class SPGlobalTargetMultiStatusResponseWithPartialErrors(LenientModel):
    error: list[SPGlobalErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    partialSuccess: list[SPGlobalTargetPartialIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPGlobalTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPGlobalTargetMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=999)
    target: SPGlobalTarget


class SPGlobalTargetNegativeFilter(StrictModel):
    include: list[bool] = Field(min_length=1, max_length=1)


class SPGlobalTargetPartialIndex(LenientModel):
    errors: list[SPGlobalError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)
    target: SPGlobalTarget


class SPGlobalTargetProductIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: SPGlobalTargetProductIdFilterType


class SPGlobalTargetStateFilter(StrictModel):
    include: list[SPGlobalState | str] = Field(min_length=1, max_length=3)


class SPGlobalTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[SPGlobalTarget] | None = Field(default=None, min_length=0, max_length=5000)


class SPGlobalTargetTargetIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalTargetTargetTypeFilter(StrictModel):
    include: list[SPGlobalTargetType | str] = Field(min_length=1, max_length=4)


class SPGlobalTargetUpdate(StrictModel):
    bid: SPGlobalUpdateTargetBid | None = Field(default=None)
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceTargetConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual marketplace level. For example, if a global target is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the target's global value is applied to that marketplace.",
    )
    marketplaces: list[SPGlobalMarketplace | str] | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    state: SPGlobalUpdateState | None = Field(default=None)
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetId: str = Field(description="A unique identifier for the target.")


class SPGlobalThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: SPGlobalThemeMatchType | str


class SPGlobalUpdateTargetBid(StrictModel):
    marketplaceSettings: list[SPGlobalCreateTargetBidMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The bid associated with the target at specified marketplace level. Either one of bid or marketplaceSettings should always be specified",
    )


class SPGlobalUpdateTargetRequest(StrictModel):
    targets: list[SPGlobalTargetUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SPGlobalAdProduct",
    "SPGlobalCreateKeywordTarget",
    "SPGlobalCreateMarketplaceTargetConfigurations",
    "SPGlobalCreateMarketplaceTargetFieldOverrides",
    "SPGlobalCreateOverridableTargets",
    "SPGlobalCreateProductCategoryRefinement",
    "SPGlobalCreateProductCategoryRefinementMarketplaceSetting",
    "SPGlobalCreateProductCategoryRefinementValue",
    "SPGlobalCreateProductCategoryTarget",
    "SPGlobalCreateProductGenreRefinement",
    "SPGlobalCreateProductMarketplaceSetting",
    "SPGlobalCreateProductTarget",
    "SPGlobalCreateProductValue",
    "SPGlobalCreateState",
    "SPGlobalCreateTag",
    "SPGlobalCreateTargetBid",
    "SPGlobalCreateTargetBidMarketplaceSetting",
    "SPGlobalCreateTargetDetails",
    "SPGlobalCreateTargetRequest",
    "SPGlobalCreateThemeTarget",
    "SPGlobalCurrencyCode",
    "SPGlobalDeleteTargetRequest",
    "SPGlobalDeliveryReason",
    "SPGlobalDeliveryStatus",
    "SPGlobalError",
    "SPGlobalErrorCode",
    "SPGlobalErrorMarketplace",
    "SPGlobalErrorsIndex",
    "SPGlobalKeywordMatchType",
    "SPGlobalKeywordTarget",
    "SPGlobalLanguageLocale",
    "SPGlobalMarketplace",
    "SPGlobalMarketplaceScope",
    "SPGlobalMarketplaceTargetConfigurations",
    "SPGlobalMarketplaceTargetFieldOverrides",
    "SPGlobalMatchType",
    "SPGlobalOverridableTargets",
    "SPGlobalProductCategoryRefinement",
    "SPGlobalProductCategoryRefinementMarketplaceSetting",
    "SPGlobalProductCategoryRefinementValue",
    "SPGlobalProductCategoryTarget",
    "SPGlobalProductGenreRefinement",
    "SPGlobalProductIdType",
    "SPGlobalProductMarketplaceSetting",
    "SPGlobalProductMatchType",
    "SPGlobalProductTarget",
    "SPGlobalProductValue",
    "SPGlobalQueryTargetRequest",
    "SPGlobalState",
    "SPGlobalStatus",
    "SPGlobalStatusMarketplaceSetting",
    "SPGlobalTag",
    "SPGlobalTarget",
    "SPGlobalTargetAdGroupIdFilter",
    "SPGlobalTargetAdProductFilter",
    "SPGlobalTargetBid",
    "SPGlobalTargetBidMarketplaceSetting",
    "SPGlobalTargetCampaignIdFilter",
    "SPGlobalTargetCreate",
    "SPGlobalTargetDetails",
    "SPGlobalTargetLevel",
    "SPGlobalTargetMarketplaceScopeFilter",
    "SPGlobalTargetMatchTypeFilter",
    "SPGlobalTargetMultiStatusResponseWithPartialErrors",
    "SPGlobalTargetMultiStatusSuccess",
    "SPGlobalTargetNegativeFilter",
    "SPGlobalTargetPartialIndex",
    "SPGlobalTargetProductIdFilter",
    "SPGlobalTargetProductIdFilterType",
    "SPGlobalTargetStateFilter",
    "SPGlobalTargetSuccessResponse",
    "SPGlobalTargetTargetIdFilter",
    "SPGlobalTargetTargetTypeFilter",
    "SPGlobalTargetType",
    "SPGlobalTargetUpdate",
    "SPGlobalThemeMatchType",
    "SPGlobalThemeTarget",
    "SPGlobalUpdateState",
    "SPGlobalUpdateTargetBid",
    "SPGlobalUpdateTargetRequest",
]
