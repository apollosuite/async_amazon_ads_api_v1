"""Auto-generated Pydantic models for sd from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

if TYPE_CHECKING:
    from async_amazon_ads_api_v1.errors import ErrorsIndex

    from .enums import SDAdProduct, SDCreateState, SDCurrencyCode, SDProductIdType, SDState, SDUpdateState
    from .shared import SDStatus
del TYPE_CHECKING


class SDAudienceTarget(BaseModel):
    """Target based on a specified audience ID."""

    model_config = ConfigDict(extra="forbid")

    audienceId: SDMarketplaceStringValue


class SDContentCategoryTarget(BaseModel):
    """Target based on the category of content being viewed."""

    model_config = ConfigDict(extra="forbid")

    contentCategoryId: str  # The content category being targeted.


class SDCreateAudienceTarget(BaseModel):
    """Target based on a specified audience ID."""

    model_config = ConfigDict(extra="forbid")

    audienceId: SDCreateMarketplaceStringValue


class SDCreateContentCategoryTarget(BaseModel):
    """Target based on the category of content being viewed."""

    model_config = ConfigDict(extra="forbid")

    contentCategoryId: str  # The content category being targeted.


class SDCreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints).
    matchType: Annotated[SDKeywordMatchType | str, lenient_enum(SDKeywordMatchType)]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: Annotated[SDLanguageLocale | str, lenient_enum(SDLanguageLocale)] | None = None


class SDCreateLocationTarget(BaseModel):
    """Target based on geographic location."""

    model_config = ConfigDict(extra="forbid")

    locationId: str  # The ID of the geographic location to target.
    locationIdResolved: str | None = None  # A human-readable location text. It's a read-only field.


class SDCreateMarketplaceStringValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    defaultValue: str | None = (
        None  # The default value. Either the default value or the marketplace settings should always be specified
    )


class SDCreateProductAudienceTarget(BaseModel):
    """Target customers who have viewed or purchased a certain product within a specified lookback window."""

    model_config = ConfigDict(extra="forbid")

    asin: SDCreateMarketplaceStringValue
    event: Annotated[SDTargetEvent | str, lenient_enum(SDTargetEvent)]
    lookback: Annotated[SDLookback | str, lenient_enum(SDLookback)]
    matchType: Annotated[SDProductAudienceMatchType | str, lenient_enum(SDProductAudienceMatchType)]


class SDCreateProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productAgeRangeId: str | None = None  # The age range ID to target.
    productAgeRangeIdResolved: str | None = None  # The resolved age range to target.
    productBrandId: str | None = None  # The brand ID to target.
    productBrandIdResolved: str | None = None  # The resolved name of the brand.
    productCategoryId: str | None = None  # The product category ID to target.
    productCategoryIdResolved: str | None = None  # The resolved product category.
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


class SDCreateProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SDCreateProductCategoryRefinement | None = None


class SDCreateProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SDCreateProductCategoryRefinementValue


class SDCreateProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SDProductMatchType | str, lenient_enum(SDProductMatchType)]
    product: SDCreateProductValue
    productIdType: Annotated[SDProductIdType | str, lenient_enum(SDProductIdType)]


class SDCreateProductValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productId: str | None = (
        None  # The product identifier. Either the product id or the marketplace settings should always be specified
    )


class SDCreateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.


class SDCreateTargetDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keywordTarget: SDCreateKeywordTarget | None = None
    productTarget: SDCreateProductTarget | None = None
    productCategoryTarget: SDCreateProductCategoryTarget | None = None
    productAudienceTarget: SDCreateProductAudienceTarget | None = None
    audienceTarget: SDCreateAudienceTarget | None = None
    locationTarget: SDCreateLocationTarget | None = None
    contentCategoryTarget: SDCreateContentCategoryTarget | None = None
    themeTarget: SDCreateThemeTarget | None = None


class SDCreateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SDTargetCreate]


class SDCreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SDThemeMatchType | str, lenient_enum(SDThemeMatchType)]


class SDDeleteTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targetIds: list[str]


class SDKeywordMatchType(StrEnum):
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


class SDKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints).
    matchType: Annotated[SDKeywordMatchType | str, lenient_enum(SDKeywordMatchType)]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: Annotated[SDLanguageLocale | str, lenient_enum(SDLanguageLocale)] | None = None


class SDLanguageLocale(StrEnum):
    """A combination of ISO-639 standard for language code and ISO-3166 for country code.
    **LanguageLocale Enum:**

    | LanguageLocale | Description |
    |------|------|
    | `en_US` | English (United States). |
    """

    en_US = "en_US"


class SDLocationTarget(BaseModel):
    """Target based on geographic location."""

    model_config = ConfigDict(extra="forbid")

    locationId: str  # The ID of the geographic location to target.
    locationIdResolved: str | None = None  # A human-readable location text. It's a read-only field.


class SDLookback(StrEnum):
    """**Lookback Enum:**

    | Lookback | Description |
    |------|------|
    | `DAYS_14` | Two week lookback period. |
    | `DAYS_180` | Six month lookback period. |
    | `DAYS_30` | One month lookback period. |
    | `DAYS_365` | One year lookback period. |
    | `DAYS_60` | Two month lookback period. |
    | `DAYS_7` | One week lookback period. |
    | `DAYS_90` | Three month lookback period. |
    """

    DAYS_14 = "DAYS_14"
    DAYS_180 = "DAYS_180"
    DAYS_30 = "DAYS_30"
    DAYS_365 = "DAYS_365"
    DAYS_60 = "DAYS_60"
    DAYS_7 = "DAYS_7"
    DAYS_90 = "DAYS_90"


class SDMarketplaceStringValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    defaultValue: str | None = (
        None  # The default value. Either the default value or the marketplace settings should always be specified
    )


class SDProductAudienceMatchType(StrEnum):
    """**ProductAudienceMatchType Enum:**

    | ProductAudienceMatchType | Description |
    |------|------|
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    | `PRODUCT_SIMILAR` | Products similar to the specified product. |
    """

    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"


class SDProductAudienceTarget(BaseModel):
    """Target customers who have viewed or purchased a certain product within a specified lookback window."""

    model_config = ConfigDict(extra="forbid")

    asin: SDMarketplaceStringValue
    event: Annotated[SDTargetEvent | str, lenient_enum(SDTargetEvent)]
    lookback: Annotated[SDLookback | str, lenient_enum(SDLookback)]
    matchType: Annotated[SDProductAudienceMatchType | str, lenient_enum(SDProductAudienceMatchType)]


class SDProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productAgeRangeId: str | None = None  # The age range ID to target.
    productAgeRangeIdResolved: str | None = None  # The resolved age range to target.
    productBrandId: str | None = None  # The brand ID to target.
    productBrandIdResolved: str | None = None  # The resolved name of the brand.
    productCategoryId: str | None = None  # The product category ID to target.
    productCategoryIdResolved: str | None = None  # The resolved product category.
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


class SDProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SDProductCategoryRefinement | None = None


class SDProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SDProductCategoryRefinementValue


class SDProductMatchType(StrEnum):
    """**ProductMatchType Enum:**

    | ProductMatchType | Description |
    |------|------|
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    | `PRODUCT_SIMILAR` | Products similar to the specified product. |
    """

    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"


class SDProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SDProductMatchType | str, lenient_enum(SDProductMatchType)]
    product: SDProductValue
    productIdType: Annotated[SDProductIdType | str, lenient_enum(SDProductIdType)]


class SDProductValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productId: str | None = (
        None  # The product identifier. Either the product id or the marketplace settings should always be specified
    )


class SDQueryTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SDTargetAdGroupIdFilter | None = None
    adProductFilter: SDTargetAdProductFilter
    campaignIdFilter: SDTargetCampaignIdFilter | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: SDTargetStateFilter | None = None
    targetIdFilter: SDTargetTargetIdFilter | None = None


class SDTarget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the target. Only used for ad-group level targets.
    )
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    bid: SDTargetBid | None = None
    campaignId: str | None = (
        None  # A unique identifier for the campaign associated with the target. Only used for campaign-level targets.
    )
    creationDateTime: datetime  # The date time the target was created.
    lastUpdatedDateTime: datetime  # The date time the target was last updated.
    negative: bool  # Indicates whether the target is negative or not.
    state: Annotated[SDState | str, lenient_enum(SDState)]
    status: SDStatus | None = None
    targetDetails: SDTargetDetails
    targetId: str  # A unique identifier for the target.
    targetLevel: Annotated[SDTargetLevel | str, lenient_enum(SDTargetLevel)]
    targetType: Annotated[SDTargetType | str, lenient_enum(SDTargetType)]


class SDTargetAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SDTargetAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    ]  # **AdProduct Enum:** AdProduct Description `SPONSORED_DISPLAY` Sponsored Display ad product.


class SDTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.
    currencyCode: Annotated[SDCurrencyCode | str, lenient_enum(SDCurrencyCode)]


class SDTargetCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SDTargetCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the target. Only used for ad-group level targets.
    )
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    bid: SDCreateTargetBid | None = None
    campaignId: str | None = (
        None  # A unique identifier for the campaign associated with the target. Only used for campaign-level targets.
    )
    negative: bool  # Indicates whether the target is negative or not.
    state: Annotated[SDCreateState | str, lenient_enum(SDCreateState)]
    targetDetails: SDCreateTargetDetails
    targetType: Annotated[SDTargetType | str, lenient_enum(SDTargetType)]


class SDTargetDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    audienceTarget: SDAudienceTarget | None = None
    contentCategoryTarget: SDContentCategoryTarget | None = None
    keywordTarget: SDKeywordTarget | None = None
    locationTarget: SDLocationTarget | None = None
    productAudienceTarget: SDProductAudienceTarget | None = None
    productCategoryTarget: SDProductCategoryTarget | None = None
    productTarget: SDProductTarget | None = None
    themeTarget: SDThemeTarget | None = None


class SDTargetEvent(StrEnum):
    """**TargetEvent Enum:**

    | TargetEvent | Description |
    |------|------|
    | `PURCHASE` | A product purchase event. |
    | `VIEW` | A product view event. |
    """

    PURCHASE = "PURCHASE"
    VIEW = "VIEW"


class SDTargetLevel(StrEnum):
    """**TargetLevel Enum:**

    | TargetLevel | Description |
    |------|------|
    | `AD_GROUP` | Target applied at the ad group level. |
    """

    AD_GROUP = "AD_GROUP"


class SDTargetMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SDTargetMultiStatusSuccess] | None = None


class SDTargetMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index: int
    target: SDTarget


class SDTargetStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SDState | str, lenient_enum(SDState)]
    ]  # **State Enum:** State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SDTargetSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nextToken: str | None = None
    targets: list[SDTarget] | None = None


class SDTargetTargetIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SDTargetType(StrEnum):
    """**TargetType Enum:**

    | TargetType | Description |
    |------|------|
    | `AUDIENCE` | Target based on an audience segment. |
    | `CONTENT_CATEGORY` | Target based on content category. |
    | `KEYWORD` | Target based on customer search terms. |
    | `LOCATION` | Target based on geographic location. |
    | `PRODUCT_AUDIENCE` | Target customers who interacted with a specific product. |
    | `PRODUCT_CATEGORY` | Target based on a product category. |
    | `PRODUCT` | Target based on a specific product. |
    | `THEME` | Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products. |
    """

    AUDIENCE = "AUDIENCE"
    CONTENT_CATEGORY = "CONTENT_CATEGORY"
    KEYWORD = "KEYWORD"
    LOCATION = "LOCATION"
    PRODUCT = "PRODUCT"
    PRODUCT_AUDIENCE = "PRODUCT_AUDIENCE"
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"
    THEME = "THEME"


class SDTargetUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: SDUpdateTargetBid | None = None
    state: Annotated[SDUpdateState | str, lenient_enum(SDUpdateState)] | None = None
    targetId: str  # A unique identifier for the target.


class SDThemeMatchType(StrEnum):
    """**ThemeMatchType Enum:**

    | ThemeMatchType | Description |
    |------|------|
    | `INTERESTED_AUDIENCE` | Audiences that are likely interested in the advertised product or service. |
    """

    INTERESTED_AUDIENCE = "INTERESTED_AUDIENCE"


class SDThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SDThemeMatchType | str, lenient_enum(SDThemeMatchType)]


class SDUpdateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.


class SDUpdateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SDTargetUpdate]


__all__ = [
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
    "SDCreateTargetBid",
    "SDCreateTargetDetails",
    "SDCreateTargetRequest",
    "SDCreateThemeTarget",
    "SDDeleteTargetRequest",
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
    "SDProductMatchType",
    "SDProductTarget",
    "SDProductValue",
    "SDQueryTargetRequest",
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
    "SDUpdateTargetBid",
    "SDUpdateTargetRequest",
]
