"""Auto-generated models for Targets from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .ads import SDProductIdType
from .campaigns import (
    SDAdProduct,
    SDCreateState,
    SDCurrencyCode,
    SDState,
    SDStatus,
    SDUpdateState,
)


class SDKeywordMatchType(StrEnum):
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


class SDLanguageLocale(StrEnum):
    """
    A combination of ISO-639 standard for language code and ISO-3166 for country code.
    **LanguageLocale Enum:**

    | LanguageLocale | Description |
    |------|------|
    | `en_US` | English (United States). |
    """

    en_US = "en_US"


class SDLookback(StrEnum):
    """
    **Lookback Enum:**

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


class SDProductAudienceMatchType(StrEnum):
    """
    **ProductAudienceMatchType Enum:**

    | ProductAudienceMatchType | Description |
    |------|------|
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    | `PRODUCT_SIMILAR` | Products similar to the specified product. |
    """

    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"


class SDProductMatchType(StrEnum):
    """
    **ProductMatchType Enum:**

    | ProductMatchType | Description |
    |------|------|
    | `PRODUCT_EXACT` | Products exactly matching the specified product. |
    | `PRODUCT_SIMILAR` | Products similar to the specified product. |
    """

    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"


class SDTargetEvent(StrEnum):
    """
    **TargetEvent Enum:**

    | TargetEvent | Description |
    |------|------|
    | `PURCHASE` | A product purchase event. |
    | `VIEW` | A product view event. |
    """

    PURCHASE = "PURCHASE"
    VIEW = "VIEW"


class SDTargetLevel(StrEnum):
    """
    **TargetLevel Enum:**

    | TargetLevel | Description |
    |------|------|
    | `AD_GROUP` | Target applied at the ad group level. |
    """

    AD_GROUP = "AD_GROUP"


class SDTargetType(StrEnum):
    """
    **TargetType Enum:**

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


class SDThemeMatchType(StrEnum):
    """
    **ThemeMatchType Enum:**

    | ThemeMatchType | Description |
    |------|------|
    | `INTERESTED_AUDIENCE` | Audiences that are likely interested in the advertised product or service. |
    """

    INTERESTED_AUDIENCE = "INTERESTED_AUDIENCE"


class SDAudienceTarget(BaseModel):
    """Target based on a specified audience ID."""

    model_config = ConfigDict(extra="allow")

    audienceId: SDMarketplaceStringValue | None = Field(default=None)


class SDContentCategoryTarget(BaseModel):
    """Target based on the category of content being viewed."""

    model_config = ConfigDict(extra="allow")

    contentCategoryId: str | None = Field(default=None, description="The content category being targeted.")


class SDCreateAudienceTarget(BaseModel):
    """Target based on a specified audience ID."""

    model_config = ConfigDict(extra="forbid")

    audienceId: SDCreateMarketplaceStringValue


class SDCreateContentCategoryTarget(BaseModel):
    """Target based on the category of content being viewed."""

    model_config = ConfigDict(extra="forbid")

    contentCategoryId: str = Field(description="The content category being targeted.")


class SDCreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[SDKeywordMatchType | str, lenient_enum(SDKeywordMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SDLanguageLocale | str, lenient_enum(SDLanguageLocale)] | None = Field(default=None)


class SDCreateLocationTarget(BaseModel):
    """Target based on geographic location."""

    model_config = ConfigDict(extra="forbid")

    locationId: str = Field(description="The ID of the geographic location to target.")
    locationIdResolved: str | None = Field(
        default=None, description="A human-readable location text. It's a read-only field."
    )


class SDCreateMarketplaceStringValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
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


class SDCreateProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SDCreateProductCategoryRefinement | None = Field(default=None)


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

    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SDCreateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = Field(default=None, description="The maximum bid for a target.")


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

    targets: list[SDTargetCreate] = Field(min_length=1, max_length=1000)


class SDCreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: Annotated[SDThemeMatchType | str, lenient_enum(SDThemeMatchType)]


class SDDeleteTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targetIds: list[str] = Field(min_length=1, max_length=1000)


class SDKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="allow")

    keyword: str | None = Field(
        default=None,
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints).",
    )
    matchType: Annotated[SDKeywordMatchType | str, lenient_enum(SDKeywordMatchType)] | None = Field(default=None)
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: Annotated[SDLanguageLocale | str, lenient_enum(SDLanguageLocale)] | None = Field(default=None)


class SDLocationTarget(BaseModel):
    """Target based on geographic location."""

    model_config = ConfigDict(extra="allow")

    locationId: str | None = Field(default=None, description="The ID of the geographic location to target.")
    locationIdResolved: str | None = Field(
        default=None, description="A human-readable location text. It's a read-only field."
    )


class SDMarketplaceStringValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class SDProductAudienceTarget(BaseModel):
    """Target customers who have viewed or purchased a certain product within a specified lookback window."""

    model_config = ConfigDict(extra="allow")

    asin: SDMarketplaceStringValue | None = Field(default=None)
    event: Annotated[SDTargetEvent | str, lenient_enum(SDTargetEvent)] | None = Field(default=None)
    lookback: Annotated[SDLookback | str, lenient_enum(SDLookback)] | None = Field(default=None)
    matchType: Annotated[SDProductAudienceMatchType | str, lenient_enum(SDProductAudienceMatchType)] | None = Field(
        default=None
    )


class SDProductCategoryRefinement(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SDProductCategoryRefinementValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    productCategoryRefinement: SDProductCategoryRefinement | None = Field(default=None)


class SDProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="allow")

    productCategoryRefinement: SDProductCategoryRefinementValue | None = Field(default=None)


class SDProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="allow")

    matchType: Annotated[SDProductMatchType | str, lenient_enum(SDProductMatchType)] | None = Field(default=None)
    product: SDProductValue | None = Field(default=None)
    productIdType: Annotated[SDProductIdType | str, lenient_enum(SDProductIdType)] | None = Field(default=None)


class SDProductValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class SDQueryTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SDTargetAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SDTargetAdProductFilter
    campaignIdFilter: SDTargetCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=5000, ge=1, le=5000)
    nextToken: str | None = Field(default=None)
    stateFilter: SDTargetStateFilter | None = Field(default=None)
    targetIdFilter: SDTargetTargetIdFilter | None = Field(default=None)


class SDTarget(BaseModel):
    model_config = ConfigDict(extra="allow")

    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)] | None = Field(default=None)
    bid: SDTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time the target was created.")
    lastUpdatedDateTime: datetime | None = Field(default=None, description="The date time the target was last updated.")
    negative: bool | None = Field(default=None, description="Indicates whether the target is negative or not.")
    state: Annotated[SDState | str, lenient_enum(SDState)] | None = Field(default=None)
    status: SDStatus | None = Field(default=None)
    targetDetails: SDTargetDetails | None = Field(default=None)
    targetId: str | None = Field(default=None, description="A unique identifier for the target.")
    targetLevel: Annotated[SDTargetLevel | str, lenient_enum(SDTargetLevel)] | None = Field(default=None)
    targetType: Annotated[SDTargetType | str, lenient_enum(SDTargetType)] | None = Field(default=None)


class SDTargetAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SDTargetAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_DISPLAY` | Sponsored Display ad product. |
""",
    )


class SDTargetBid(BaseModel):
    model_config = ConfigDict(extra="allow")

    bid: float | None = Field(default=None, description="The maximum bid for a target.")
    currencyCode: Annotated[SDCurrencyCode | str, lenient_enum(SDCurrencyCode)] | None = Field(default=None)


class SDTargetCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SDTargetCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    bid: SDCreateTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[SDCreateState | str, lenient_enum(SDCreateState)]
    targetDetails: SDCreateTargetDetails
    targetType: Annotated[SDTargetType | str, lenient_enum(SDTargetType)]


class SDTargetDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    audienceTarget: SDAudienceTarget | None = None
    contentCategoryTarget: SDContentCategoryTarget | None = None
    keywordTarget: SDKeywordTarget | None = None
    locationTarget: SDLocationTarget | None = None
    productAudienceTarget: SDProductAudienceTarget | None = None
    productCategoryTarget: SDProductCategoryTarget | None = None
    productTarget: SDProductTarget | None = None
    themeTarget: SDThemeTarget | None = None


class SDTargetMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SDTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SDTargetMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int | None = Field(default=None, ge=0, le=999)
    target: SDTarget | None = Field(default=None)


class SDTargetStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SDState | str, lenient_enum(SDState)]] = Field(
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


class SDTargetSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    nextToken: str | None = Field(default=None)
    targets: list[SDTarget] | None = Field(default=None, min_length=0, max_length=5000)


class SDTargetTargetIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SDTargetUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: SDUpdateTargetBid | None = Field(default=None)
    state: Annotated[SDUpdateState | str, lenient_enum(SDUpdateState)] | None = Field(default=None)
    targetId: str = Field(description="A unique identifier for the target.")


class SDThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="allow")

    matchType: Annotated[SDThemeMatchType | str, lenient_enum(SDThemeMatchType)] | None = Field(default=None)


class SDUpdateTargetBid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bid: float | None = Field(default=None, description="The maximum bid for a target.")


class SDUpdateTargetRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targets: list[SDTargetUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SDKeywordMatchType",
    "SDLanguageLocale",
    "SDLookback",
    "SDProductAudienceMatchType",
    "SDProductMatchType",
    "SDTargetEvent",
    "SDTargetLevel",
    "SDTargetType",
    "SDThemeMatchType",
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
    "SDKeywordTarget",
    "SDLocationTarget",
    "SDMarketplaceStringValue",
    "SDProductAudienceTarget",
    "SDProductCategoryRefinement",
    "SDProductCategoryRefinementValue",
    "SDProductCategoryTarget",
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
    "SDTargetMultiStatusResponse",
    "SDTargetMultiStatusSuccess",
    "SDTargetStateFilter",
    "SDTargetSuccessResponse",
    "SDTargetTargetIdFilter",
    "SDTargetUpdate",
    "SDThemeTarget",
    "SDUpdateTargetBid",
    "SDUpdateTargetRequest",
]
