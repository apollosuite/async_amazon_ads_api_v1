"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.sd import (
    SDAdProduct,
    SDCreateState,
    SDCurrencyCode,
    SDDeliveryReason,
    SDDeliveryStatus,
    SDError,
    SDErrorCode,
    SDErrorsIndex,
    SDProductIdType,
    SDState,
    SDStatus,
    SDUpdateState,
)


class SDKeywordMatchType(StrEnum):
    BROAD = "BROAD"  # Broad match search terms. This expands matching on user intent beyond PHRASE.
    EXACT = "EXACT"  # Exact match search terms.
    PHRASE = "PHRASE"  # Phrase match search terms. This expands matching on user intent beyond EXACT.


class SDLanguageLocale(StrEnum):
    """
    A combination of ISO-639 standard for language code and ISO-3166 for country code.
    """

    en_US = "en_US"  # English (United States).


class SDLookback(StrEnum):
    DAYS_14 = "DAYS_14"  # Two week lookback period.
    DAYS_180 = "DAYS_180"  # Six month lookback period.
    DAYS_30 = "DAYS_30"  # One month lookback period.
    DAYS_365 = "DAYS_365"  # One year lookback period.
    DAYS_60 = "DAYS_60"  # Two month lookback period.
    DAYS_7 = "DAYS_7"  # One week lookback period.
    DAYS_90 = "DAYS_90"  # Three month lookback period.


class SDProductAudienceMatchType(StrEnum):
    PRODUCT_EXACT = "PRODUCT_EXACT"  # Products exactly matching the specified product.
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"  # Products similar to the specified product.


class SDProductMatchType(StrEnum):
    PRODUCT_EXACT = "PRODUCT_EXACT"  # Products exactly matching the specified product.
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"  # Products similar to the specified product.


class SDTargetEvent(StrEnum):
    PURCHASE = "PURCHASE"  # A product purchase event.
    VIEW = "VIEW"  # A product view event.


class SDTargetLevel(StrEnum):
    AD_GROUP = "AD_GROUP"  # Target applied at the ad group level.


class SDTargetType(StrEnum):
    AUDIENCE = "AUDIENCE"  # Target based on an audience segment.
    CONTENT_CATEGORY = "CONTENT_CATEGORY"  # Target based on content category.
    KEYWORD = "KEYWORD"  # Target based on customer search terms.
    LOCATION = "LOCATION"  # Target based on geographic location.
    PRODUCT = "PRODUCT"  # Target based on a specific product.
    PRODUCT_AUDIENCE = "PRODUCT_AUDIENCE"  # Target customers who interacted with a specific product.
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"  # Target based on a product category.
    THEME = (
        "THEME"  # Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
    )


class SDThemeMatchType(StrEnum):
    INTERESTED_AUDIENCE = (
        "INTERESTED_AUDIENCE"  # Audiences that are likely interested in the advertised product or service.
    )


class SDAudienceTarget(LenientModel):
    """Target based on a specified audience ID."""

    audienceId: SDMarketplaceStringValue


class SDContentCategoryTarget(LenientModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class SDCreateAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    audienceId: SDCreateMarketplaceStringValue


class SDCreateContentCategoryTarget(StrictModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class SDCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SDKeywordMatchType, lenient_enum(SDKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SDLanguageLocale, lenient_enum(SDLanguageLocale)] | None = Field(default=None)


class SDCreateLocationTarget(StrictModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")
    locationIdResolved: str | None = Field(
        default=None, description="A human-readable location text. It's a read-only field."
    )


class SDCreateMarketplaceStringValue(StrictModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class SDCreateProductAudienceTarget(StrictModel):
    """Target customers who have viewed or purchased a certain product within a specified lookback window."""

    asin: SDCreateMarketplaceStringValue
    event: Annotated[SDTargetEvent, lenient_enum(SDTargetEvent)]
    lookback: Annotated[SDLookback, lenient_enum(SDLookback)]
    matchType: Annotated[SDProductAudienceMatchType, lenient_enum(SDProductAudienceMatchType)]


class SDCreateProductCategoryRefinement(StrictModel):
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


class SDCreateProductCategoryRefinementValue(StrictModel):
    productCategoryRefinement: SDCreateProductCategoryRefinement | None = Field(default=None)


class SDCreateProductCategoryTarget(StrictModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: SDCreateProductCategoryRefinementValue


class SDCreateProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: Annotated[SDProductMatchType, lenient_enum(SDProductMatchType)]
    product: SDCreateProductValue
    productIdType: Annotated[SDProductIdType, lenient_enum(SDProductIdType)]


class SDCreateProductValue(StrictModel):
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SDCreateTargetBid(StrictModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")


class SDCreateTargetDetailsKeywordTarget(StrictModel):
    keywordTarget: SDCreateKeywordTarget


class SDCreateTargetDetailsProductTarget(StrictModel):
    productTarget: SDCreateProductTarget


class SDCreateTargetDetailsProductCategoryTarget(StrictModel):
    productCategoryTarget: SDCreateProductCategoryTarget


class SDCreateTargetDetailsProductAudienceTarget(StrictModel):
    productAudienceTarget: SDCreateProductAudienceTarget


class SDCreateTargetDetailsAudienceTarget(StrictModel):
    audienceTarget: SDCreateAudienceTarget


class SDCreateTargetDetailsLocationTarget(StrictModel):
    locationTarget: SDCreateLocationTarget


class SDCreateTargetDetailsContentCategoryTarget(StrictModel):
    contentCategoryTarget: SDCreateContentCategoryTarget


class SDCreateTargetDetailsThemeTarget(StrictModel):
    themeTarget: SDCreateThemeTarget


type SDCreateTargetDetails = SDCreateTargetDetailsKeywordTarget | SDCreateTargetDetailsProductTarget | SDCreateTargetDetailsProductCategoryTarget | SDCreateTargetDetailsProductAudienceTarget | SDCreateTargetDetailsAudienceTarget | SDCreateTargetDetailsLocationTarget | SDCreateTargetDetailsContentCategoryTarget | SDCreateTargetDetailsThemeTarget


class SDCreateTargetRequest(StrictModel):
    targets: list[SDTargetCreate] = Field(min_length=1, max_length=1000)


class SDCreateThemeTarget(StrictModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: Annotated[SDThemeMatchType, lenient_enum(SDThemeMatchType)]


class SDDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SDKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SDKeywordMatchType | str, lenient_enum(SDKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SDLanguageLocale | str, lenient_enum(SDLanguageLocale)] | None = Field(default=None)


class SDLocationTarget(LenientModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")
    locationIdResolved: str | None = Field(
        default=None, description="A human-readable location text. It's a read-only field."
    )


class SDMarketplaceStringValue(LenientModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class SDProductAudienceTarget(LenientModel):
    """Target customers who have viewed or purchased a certain product within a specified lookback window."""

    asin: SDMarketplaceStringValue
    event: Annotated[SDTargetEvent | str, lenient_enum(SDTargetEvent)]
    lookback: Annotated[SDLookback | str, lenient_enum(SDLookback)]
    matchType: Annotated[SDProductAudienceMatchType | str, lenient_enum(SDProductAudienceMatchType)]


class SDProductCategoryRefinement(LenientModel):
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


class SDProductCategoryRefinementValue(LenientModel):
    productCategoryRefinement: SDProductCategoryRefinement | None = Field(default=None)


class SDProductCategoryTarget(LenientModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: SDProductCategoryRefinementValue


class SDProductTarget(LenientModel):
    """Targets a specific product."""

    matchType: Annotated[SDProductMatchType | str, lenient_enum(SDProductMatchType)]
    product: SDProductValue
    productIdType: Annotated[SDProductIdType | str, lenient_enum(SDProductIdType)]


class SDProductValue(LenientModel):
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SDQueryTargetRequest(StrictModel):
    adGroupIdFilter: SDTargetAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SDTargetAdProductFilter
    campaignIdFilter: SDTargetCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=5000, ge=1, le=5000)
    nextToken: str | None = Field(default=None)
    stateFilter: SDTargetStateFilter | None = Field(default=None)
    targetIdFilter: SDTargetTargetIdFilter | None = Field(default=None)


class SDTarget(LenientModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    bid: SDTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime = Field(description="The date time the target was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SDState | str, lenient_enum(SDState)]
    status: SDStatus | None = Field(default=None)
    targetDetails: SDTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: Annotated[SDTargetLevel | str, lenient_enum(SDTargetLevel)]
    targetType: Annotated[SDTargetType | str, lenient_enum(SDTargetType)]


class SDTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDTargetAdProductFilter(StrictModel):
    include: list[Annotated[SDAdProduct, lenient_enum(SDAdProduct)]] = Field(min_length=1, max_length=1)


class SDTargetBid(LenientModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")
    currencyCode: Annotated[SDCurrencyCode | str, lenient_enum(SDCurrencyCode)]


class SDTargetCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDTargetCreate(StrictModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SDAdProduct, lenient_enum(SDAdProduct)]
    bid: SDCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SDCreateState, lenient_enum(SDCreateState)]
    targetDetails: SDCreateTargetDetails
    targetType: Annotated[SDTargetType, lenient_enum(SDTargetType)]


class SDTargetDetailsAudienceTarget(LenientModel):
    audienceTarget: SDAudienceTarget


class SDTargetDetailsContentCategoryTarget(LenientModel):
    contentCategoryTarget: SDContentCategoryTarget


class SDTargetDetailsKeywordTarget(LenientModel):
    keywordTarget: SDKeywordTarget


class SDTargetDetailsLocationTarget(LenientModel):
    locationTarget: SDLocationTarget


class SDTargetDetailsProductAudienceTarget(LenientModel):
    productAudienceTarget: SDProductAudienceTarget


class SDTargetDetailsProductCategoryTarget(LenientModel):
    productCategoryTarget: SDProductCategoryTarget


class SDTargetDetailsProductTarget(LenientModel):
    productTarget: SDProductTarget


class SDTargetDetailsThemeTarget(LenientModel):
    themeTarget: SDThemeTarget


type SDTargetDetails = SDTargetDetailsAudienceTarget | SDTargetDetailsContentCategoryTarget | SDTargetDetailsKeywordTarget | SDTargetDetailsLocationTarget | SDTargetDetailsProductAudienceTarget | SDTargetDetailsProductCategoryTarget | SDTargetDetailsProductTarget | SDTargetDetailsThemeTarget


class SDTargetMultiStatusResponse(LenientModel):
    error: list[SDErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SDTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SDTargetMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=999)
    target: SDTarget


class SDTargetStateFilter(StrictModel):
    include: list[Annotated[SDState, lenient_enum(SDState)]] = Field(min_length=1, max_length=3)


class SDTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[SDTarget] | None = Field(default=None, min_length=0, max_length=5000)


class SDTargetTargetIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDTargetUpdate(StrictModel):
    bid: SDUpdateTargetBid | None = Field(default=None)
    state: Annotated[SDUpdateState, lenient_enum(SDUpdateState)] | None = Field(default=None)
    targetId: str = Field(description="A unique identifier for the target.")


class SDThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: Annotated[SDThemeMatchType | str, lenient_enum(SDThemeMatchType)]


class SDUpdateTargetBid(StrictModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")


class SDUpdateTargetRequest(StrictModel):
    targets: list[SDTargetUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SDAdProduct",
    "SDAudienceTarget",
    "SDContentCategoryTarget",
    "SDCreateAudienceTarget",
    "SDCreateContentCategoryTarget",
    "SDCreateKeywordTarget",
    "SDCreateLocationTarget",
    "SDCreateMarketplaceStringValue",
    "SDCreateProductAudienceTarget",
    "SDCreateProductCategoryRefinement",
    "SDCreateProductCategoryRefinementValue",
    "SDCreateProductCategoryTarget",
    "SDCreateProductTarget",
    "SDCreateProductValue",
    "SDCreateState",
    "SDCreateTargetBid",
    "SDCreateTargetDetails",
    "SDCreateTargetRequest",
    "SDCreateThemeTarget",
    "SDCurrencyCode",
    "SDDeleteTargetRequest",
    "SDDeliveryReason",
    "SDDeliveryStatus",
    "SDError",
    "SDErrorCode",
    "SDErrorsIndex",
    "SDKeywordMatchType",
    "SDKeywordTarget",
    "SDLanguageLocale",
    "SDLocationTarget",
    "SDLookback",
    "SDMarketplaceStringValue",
    "SDProductAudienceMatchType",
    "SDProductAudienceTarget",
    "SDProductCategoryRefinement",
    "SDProductCategoryRefinementValue",
    "SDProductCategoryTarget",
    "SDProductIdType",
    "SDProductMatchType",
    "SDProductTarget",
    "SDProductValue",
    "SDQueryTargetRequest",
    "SDState",
    "SDStatus",
    "SDTarget",
    "SDTargetAdGroupIdFilter",
    "SDTargetAdProductFilter",
    "SDTargetBid",
    "SDTargetCampaignIdFilter",
    "SDTargetCreate",
    "SDTargetDetails",
    "SDTargetEvent",
    "SDTargetLevel",
    "SDTargetMultiStatusResponse",
    "SDTargetMultiStatusSuccess",
    "SDTargetStateFilter",
    "SDTargetSuccessResponse",
    "SDTargetTargetIdFilter",
    "SDTargetType",
    "SDTargetUpdate",
    "SDThemeMatchType",
    "SDThemeTarget",
    "SDUpdateState",
    "SDUpdateTargetBid",
    "SDUpdateTargetRequest",
]
