"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
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


class SPGlobalKeywordMatchType(StrEnum):
    BROAD = "BROAD"  # Broad match search terms. This expands matching on user intent beyond PHRASE.
    EXACT = "EXACT"  # Exact match search terms.
    PHRASE = "PHRASE"  # Phrase match search terms. This expands matching on user intent beyond EXACT.


class SPGlobalLanguageLocale(StrEnum):
    """
    A combination of ISO-639 standard for language code and ISO-3166 for country code.
    """

    zh_CN = "zh_CN"  # Chinese (China).


class SPGlobalMarketplace(StrEnum):
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


class SPGlobalMatchType(StrEnum):
    BROAD = "BROAD"  # Broad match search terms. This expands matching on user intent beyond PHRASE.
    EXACT = "EXACT"  # Exact match search terms.
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"  # Search terms closely matching advertised product.
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"  # Search terms loosely matching advertised product.
    PHRASE = "PHRASE"  # Phrase match search terms. This expands matching on user intent beyond EXACT.
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"  # Products that complement advertised product.
    PRODUCT_EXACT = "PRODUCT_EXACT"  # Products exactly matching the specified product.
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"  # Products similar to the specified product.
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"  # Products that can be substituted for advertised product.


class SPGlobalProductMatchType(StrEnum):
    PRODUCT_EXACT = "PRODUCT_EXACT"  # Products exactly matching the specified product.
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"  # Products similar to the specified product.


class SPGlobalTargetLevel(StrEnum):
    AD_GROUP = "AD_GROUP"  # Target applied at the ad group level.
    CAMPAIGN = "CAMPAIGN"  # Target applied at the campaign level.


class SPGlobalTargetProductIdFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SPGlobalTargetType(StrEnum):
    KEYWORD = "KEYWORD"  # Target based on customer search terms.
    PRODUCT = "PRODUCT"  # Target based on a specific product.
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"  # Target based on a product category.
    THEME = (
        "THEME"  # Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
    )


class SPGlobalThemeMatchType(StrEnum):
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"  # Search terms closely matching advertised product.
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"  # Search terms loosely matching advertised product.
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"  # Products that complement advertised product.
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"  # Products that can be substituted for advertised product.


class SPGlobalCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SPGlobalKeywordMatchType, lenient_enum(SPGlobalKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SPGlobalLanguageLocale, lenient_enum(SPGlobalLanguageLocale)] | None = Field(
        default=None
    )


class SPGlobalCreateMarketplaceTargetConfigurations(StrictModel):
    marketplace: Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]
    overrides: SPGlobalCreateMarketplaceTargetFieldOverrides


class SPGlobalCreateMarketplaceTargetFieldOverrides(StrictModel):
    state: Annotated[SPGlobalState, lenient_enum(SPGlobalState)] | None = Field(default=None)
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
    marketplace: Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]
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
    marketplace: Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]
    productId: str = Field(description="The product id applicable at the specified marketplace.")


class SPGlobalCreateProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: Annotated[SPGlobalProductMatchType, lenient_enum(SPGlobalProductMatchType)]
    product: SPGlobalCreateProductValue
    productIdType: Annotated[SPGlobalProductIdType, lenient_enum(SPGlobalProductIdType)]


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
    currencyCode: Annotated[SPGlobalCurrencyCode, lenient_enum(SPGlobalCurrencyCode)]
    marketplace: Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]


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

    matchType: Annotated[SPGlobalThemeMatchType, lenient_enum(SPGlobalThemeMatchType)]


class SPGlobalDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SPGlobalKeywordMatchType | str, lenient_enum(SPGlobalKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SPGlobalLanguageLocale | str, lenient_enum(SPGlobalLanguageLocale)] | None = Field(
        default=None
    )


class SPGlobalMarketplaceTargetConfigurations(LenientModel):
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
    overrides: SPGlobalMarketplaceTargetFieldOverrides
    targetId: str = Field(
        description="Represents marketplace target id (Ex: targetId-US) associated to global target (Ex: targetId-Global)"
    )


class SPGlobalMarketplaceTargetFieldOverrides(LenientModel):
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)] | None = Field(default=None)
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
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
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
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
    productId: str = Field(description="The product id applicable at the specified marketplace.")


class SPGlobalProductTarget(LenientModel):
    """Targets a specific product."""

    matchType: Annotated[SPGlobalProductMatchType | str, lenient_enum(SPGlobalProductMatchType)]
    product: SPGlobalProductValue
    productIdType: Annotated[SPGlobalProductIdType | str, lenient_enum(SPGlobalProductIdType)]


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
    deliveryReasons: list[Annotated[SPGlobalDeliveryReason | str, lenient_enum(SPGlobalDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SPGlobalDeliveryStatus | str, lenient_enum(SPGlobalDeliveryStatus)]
    marketplaceSettings: list[SPGlobalStatusMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace level delivery status and reasons of global resources, for all the marketplaces the global resource is applicable in.",
    )


class SPGlobalStatusMarketplaceSetting(LenientModel):
    deliveryReasons: list[Annotated[SPGlobalDeliveryReason | str, lenient_enum(SPGlobalDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SPGlobalDeliveryStatus | str, lenient_enum(SPGlobalDeliveryStatus)]
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]


class SPGlobalTarget(LenientModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SPGlobalAdProduct | str, lenient_enum(SPGlobalAdProduct)]
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
    marketplaceScope: Annotated[SPGlobalMarketplaceScope | str, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)]
    status: SPGlobalStatus | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPGlobalTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: Annotated[SPGlobalTargetLevel | str, lenient_enum(SPGlobalTargetLevel)]
    targetType: Annotated[SPGlobalTargetType | str, lenient_enum(SPGlobalTargetType)]


class SPGlobalTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalTargetAdProductFilter(StrictModel):
    include: list[Annotated[SPGlobalAdProduct, lenient_enum(SPGlobalAdProduct)]] = Field(min_length=1, max_length=1)


class SPGlobalTargetBid(LenientModel):
    marketplaceSettings: list[SPGlobalTargetBidMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The bid associated with the target at specified marketplace level. Either one of bid or marketplaceSettings should always be specified",
    )


class SPGlobalTargetBidMarketplaceSetting(LenientModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")
    currencyCode: Annotated[SPGlobalCurrencyCode | str, lenient_enum(SPGlobalCurrencyCode)]
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]


class SPGlobalTargetCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalTargetCreate(StrictModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SPGlobalAdProduct, lenient_enum(SPGlobalAdProduct)]
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
    marketplaceScope: Annotated[SPGlobalMarketplaceScope, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SPGlobalCreateState, lenient_enum(SPGlobalCreateState)]
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: SPGlobalCreateTargetDetails
    targetType: Annotated[SPGlobalTargetType, lenient_enum(SPGlobalTargetType)]


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
    include: list[Annotated[SPGlobalMarketplaceScope, lenient_enum(SPGlobalMarketplaceScope)]] = Field(
        min_length=1, max_length=1
    )


class SPGlobalTargetMatchTypeFilter(StrictModel):
    include: list[Annotated[SPGlobalMatchType, lenient_enum(SPGlobalMatchType)]] = Field(min_length=1, max_length=10)


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
    queryTermMatchType: Annotated[SPGlobalTargetProductIdFilterType, lenient_enum(SPGlobalTargetProductIdFilterType)]


class SPGlobalTargetStateFilter(StrictModel):
    include: list[Annotated[SPGlobalState, lenient_enum(SPGlobalState)]] = Field(min_length=1, max_length=3)


class SPGlobalTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[SPGlobalTarget] | None = Field(default=None, min_length=0, max_length=5000)


class SPGlobalTargetTargetIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalTargetTargetTypeFilter(StrictModel):
    include: list[Annotated[SPGlobalTargetType, lenient_enum(SPGlobalTargetType)]] = Field(min_length=1, max_length=4)


class SPGlobalTargetUpdate(StrictModel):
    bid: SPGlobalUpdateTargetBid | None = Field(default=None)
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceTargetConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual marketplace level. For example, if a global target is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the target's global value is applied to that marketplace.",
    )
    marketplaces: list[Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]] | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="The list of marketplace in which the global target is applicable. The marketplaces included should either be same as or subset of parent campaign/ad group",
    )
    state: Annotated[SPGlobalUpdateState, lenient_enum(SPGlobalUpdateState)] | None = Field(default=None)
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetId: str = Field(description="A unique identifier for the target.")


class SPGlobalThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: Annotated[SPGlobalThemeMatchType | str, lenient_enum(SPGlobalThemeMatchType)]


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
