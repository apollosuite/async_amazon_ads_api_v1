"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
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

type SDKeywordMatchType = Literal[
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


type SDLanguageLocale = Literal["en_US",]  # English (United States).
"""
A combination of ISO-639 standard for language code and ISO-3166 for country code.

Supported values:
- `en_US`: English (United States).
"""


type SDLookback = Literal[
    "DAYS_14",  # Two week lookback period.
    "DAYS_180",  # Six month lookback period.
    "DAYS_30",  # One month lookback period.
    "DAYS_365",  # One year lookback period.
    "DAYS_60",  # Two month lookback period.
    "DAYS_7",  # One week lookback period.
    "DAYS_90",  # Three month lookback period.
]
"""
Supported values:
- `DAYS_14`: Two week lookback period.
- `DAYS_180`: Six month lookback period.
- `DAYS_30`: One month lookback period.
- `DAYS_365`: One year lookback period.
- `DAYS_60`: Two month lookback period.
- `DAYS_7`: One week lookback period.
- `DAYS_90`: Three month lookback period.
"""


type SDProductAudienceMatchType = Literal[
    "PRODUCT_EXACT",  # Products exactly matching the specified product.
    "PRODUCT_SIMILAR",  # Products similar to the specified product.
]
"""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
"""


type SDProductMatchType = Literal[
    "PRODUCT_EXACT",  # Products exactly matching the specified product.
    "PRODUCT_SIMILAR",  # Products similar to the specified product.
]
"""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
"""


type SDTargetEvent = Literal[
    "PURCHASE",  # A product purchase event.
    "VIEW",  # A product view event.
]
"""
Supported values:
- `PURCHASE`: A product purchase event.
- `VIEW`: A product view event.
"""


type SDTargetLevel = Literal["AD_GROUP",]  # Target applied at the ad group level.
"""
Supported values:
- `AD_GROUP`: Target applied at the ad group level.
"""


type SDTargetType = Literal[
    "AUDIENCE",  # Target based on an audience segment.
    "CONTENT_CATEGORY",  # Target based on content category.
    "KEYWORD",  # Target based on customer search terms.
    "LOCATION",  # Target based on geographic location.
    "PRODUCT",  # Target based on a specific product.
    "PRODUCT_AUDIENCE",  # Target customers who interacted with a specific product.
    "PRODUCT_CATEGORY",  # Target based on a product category.
    "THEME",  # Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
]
"""
Supported values:
- `AUDIENCE`: Target based on an audience segment.
- `CONTENT_CATEGORY`: Target based on content category.
- `KEYWORD`: Target based on customer search terms.
- `LOCATION`: Target based on geographic location.
- `PRODUCT_AUDIENCE`: Target customers who interacted with a specific product.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
"""


type SDThemeMatchType = Literal[
    "INTERESTED_AUDIENCE",  # Audiences that are likely interested in the advertised product or service.
]
"""
Supported values:
- `INTERESTED_AUDIENCE`: Audiences that are likely interested in the advertised product or service.
"""


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
    matchType: SDKeywordMatchType = Field(description="""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
""")
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: SDLanguageLocale | None = Field(
        default=None,
        description="""
Supported values:
- `en_US`: English (United States).
""",
    )


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
    event: SDTargetEvent = Field(description="""
Supported values:
- `PURCHASE`: A product purchase event.
- `VIEW`: A product view event.
""")
    lookback: SDLookback = Field(description="""
Supported values:
- `DAYS_14`: Two week lookback period.
- `DAYS_180`: Six month lookback period.
- `DAYS_30`: One month lookback period.
- `DAYS_365`: One year lookback period.
- `DAYS_60`: Two month lookback period.
- `DAYS_7`: One week lookback period.
- `DAYS_90`: Three month lookback period.
""")
    matchType: SDProductAudienceMatchType = Field(description="""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
""")


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

    matchType: SDProductMatchType = Field(description="""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
""")
    product: SDCreateProductValue
    productIdType: SDProductIdType = Field(description="""
Supported values:
- `ASIN`: ASIN identifier type.
- `SKU`: SKU identifier type.
""")


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

    matchType: SDThemeMatchType = Field(description="""
Supported values:
- `INTERESTED_AUDIENCE`: Audiences that are likely interested in the advertised product or service.
""")


class SDDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SDKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: SDKeywordMatchType | str = Field(description="""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
- `EXACT`: Exact match search terms.
- `PHRASE`: Phrase match search terms. This expands matching on user intent beyond EXACT.
""")
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: SDLanguageLocale | str | None = Field(
        default=None,
        description="""
Supported values:
- `en_US`: English (United States).
""",
    )


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
    event: SDTargetEvent | str = Field(description="""
Supported values:
- `PURCHASE`: A product purchase event.
- `VIEW`: A product view event.
""")
    lookback: SDLookback | str = Field(description="""
Supported values:
- `DAYS_14`: Two week lookback period.
- `DAYS_180`: Six month lookback period.
- `DAYS_30`: One month lookback period.
- `DAYS_365`: One year lookback period.
- `DAYS_60`: Two month lookback period.
- `DAYS_7`: One week lookback period.
- `DAYS_90`: Three month lookback period.
""")
    matchType: SDProductAudienceMatchType | str = Field(description="""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
""")


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

    matchType: SDProductMatchType | str = Field(description="""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
""")
    product: SDProductValue
    productIdType: SDProductIdType | str = Field(description="""
Supported values:
- `ASIN`: ASIN identifier type.
- `SKU`: SKU identifier type.
""")


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
    adProduct: SDAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_DISPLAY`: Sponsored Display ad product.
""")
    bid: SDTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime = Field(description="The date time the target was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: SDState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    status: SDStatus | None = Field(default=None)
    targetDetails: SDTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: SDTargetLevel | str = Field(description="""
Supported values:
- `AD_GROUP`: Target applied at the ad group level.
""")
    targetType: SDTargetType | str = Field(description="""
Supported values:
- `AUDIENCE`: Target based on an audience segment.
- `CONTENT_CATEGORY`: Target based on content category.
- `KEYWORD`: Target based on customer search terms.
- `LOCATION`: Target based on geographic location.
- `PRODUCT_AUDIENCE`: Target customers who interacted with a specific product.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
""")


class SDTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDTargetAdProductFilter(StrictModel):
    include: list[SDAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_DISPLAY`: Sponsored Display ad product.
""",
    )


class SDTargetBid(LenientModel):
    bid: float | None = Field(default=None, description="The maximum bid for a target.")
    currencyCode: SDCurrencyCode | str = Field(description="""
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


class SDTargetCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDTargetCreate(StrictModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: SDAdProduct = Field(description="""
Supported values:
- `SPONSORED_DISPLAY`: Sponsored Display ad product.
""")
    bid: SDCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: SDCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    targetDetails: SDCreateTargetDetails
    targetType: SDTargetType = Field(description="""
Supported values:
- `AUDIENCE`: Target based on an audience segment.
- `CONTENT_CATEGORY`: Target based on content category.
- `KEYWORD`: Target based on customer search terms.
- `LOCATION`: Target based on geographic location.
- `PRODUCT_AUDIENCE`: Target customers who interacted with a specific product.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
""")


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
    include: list[SDState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SDTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[SDTarget] | None = Field(default=None, min_length=0, max_length=5000)


class SDTargetTargetIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDTargetUpdate(StrictModel):
    bid: SDUpdateTargetBid | None = Field(default=None)
    state: SDUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )
    targetId: str = Field(description="A unique identifier for the target.")


class SDThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: SDThemeMatchType | str = Field(description="""
Supported values:
- `INTERESTED_AUDIENCE`: Audiences that are likely interested in the advertised product or service.
""")


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
