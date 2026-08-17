"""Auto-generated models for Campaigns from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.sb import (
    SBAdProduct,
    SBCreateState,
    SBCreateTag,
    SBDeliveryReason,
    SBDeliveryStatus,
    SBMarketplaceScope,
    SBState,
    SBStatus,
    SBTag,
    SBUpdateState,
)


class SBBidStrategy(StrEnum):
    MANUAL = (
        "MANUAL"  # Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
    )
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"  # Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.


class SBBudgetType(StrEnum):
    MONETARY = "MONETARY"


class SBCampaignNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SBCostType(StrEnum):
    CPC = "CPC"  # Cost per click.
    CPM = "CPM"  # Cost per thousand impressions.
    FIXED_PRICE = "FIXED_PRICE"  # Sale price for a specific ad placement regardless of auction performance.
    VCPM = "VCPM"  # Cost per thousand views.


class SBCountryCode(StrEnum):
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
    IE = "IE"
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
    ZA = "ZA"


class SBCurrencyCode(StrEnum):
    AED = "AED"  # United Arab Emirates Dirham
    AUD = "AUD"  # Australian Dollar
    BRL = "BRL"  # Brazilian Real
    CAD = "CAD"  # Canadian Dollar
    CHF = "CHF"  # Swiss Franc
    CNY = "CNY"  # Chinese Yuan
    DKK = "DKK"  # Danish Krone
    EGP = "EGP"  # Egyptian Pound
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound Sterling
    INR = "INR"  # Indian Rupee
    JPY = "JPY"  # Japanese Yen
    MXN = "MXN"  # Mexican Peso
    MXP = "MXP"  # Mexican Peso
    NGN = "NGN"  # Nigerian Naira
    NOK = "NOK"  # Norwegian Krone
    NZD = "NZD"  # New Zealand Dollar
    PLN = "PLN"  # Polish Złoty
    SAR = "SAR"  # Saudi Riyal
    SEK = "SEK"  # Swedish Krona
    SGD = "SGD"  # Singapore Dollar
    TRY = "TRY"  # Turkish Lira
    USD = "USD"  # United States Dollar
    ZAR = "ZAR"  # South African Rand


class SBErrorCode(StrEnum):
    ACTION_NOT_SUPPORTED = "ACTION_NOT_SUPPORTED"  # The request is not supported.
    ACTIVE_RESOURCE_LIMIT_EXCEEDED = (
        "ACTIVE_RESOURCE_LIMIT_EXCEEDED"  # Too many live resources. Remove resources and try again.
    )
    ARCHIVED_PARENT_CANNOT_CREATE = (
        "ARCHIVED_PARENT_CANNOT_CREATE"  # New resources cannot be created within an archived parent.
    )
    ARCHIVED_PARENT_CANNOT_EDIT = "ARCHIVED_PARENT_CANNOT_EDIT"  # Resources within an archived parent cannot be edited.
    ARCHIVED_RESOURCE_CANNOT_EDIT = "ARCHIVED_RESOURCE_CANNOT_EDIT"  # Archived resources cannot be edited.
    AUTOCREATED_ENTITY_CANNOT_EDIT = "AUTOCREATED_ENTITY_CANNOT_EDIT"  # Autocreated entities cannot be edited. To complete this action, create the resource manually.
    BAD_REQUEST = "BAD_REQUEST"  # The request is not valid considering the documented schema.
    CONFLICT = "CONFLICT"  # Operation could not be completed due to a conflict. Please retry your request.
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"  # The request is too large. Consider splitting it into multiple requests.
    DATE_CANNOT_BE_IN_PAST = "DATE_CANNOT_BE_IN_PAST"  # Update the date to be in the future.
    DATE_CANNOT_BE_NULL = "DATE_CANNOT_BE_NULL"  # Update the date.
    DATE_TOO_SOON = "DATE_TOO_SOON"  # Update the date to be further in the future.
    DUPLICATE_FIELD_VALUE_FOUND = "DUPLICATE_FIELD_VALUE_FOUND"  # Multiple resources share the non-unique field values. Remove the non-unique field value.
    DUPLICATE_RESOURCE_ID_FOUND = (
        "DUPLICATE_RESOURCE_ID_FOUND"  # Multiple resources share the same ID. Remove the duplicate ID.
    )
    DURATION_TOO_SHORT = "DURATION_TOO_SHORT"  # Update the length to be within the required range.
    FEATURE_DISCONTINUED = "FEATURE_DISCONTINUED"  # Feature has been discontinued.
    FEATURE_NOT_AVAILABLE = "FEATURE_NOT_AVAILABLE"  # The requested feature is not available.
    FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_SIZE_IS_OUT_OF_RANGE = "FIELD_SIZE_IS_OUT_OF_RANGE"  # Update the value to be within the required range.
    FIELD_VALUE_CANNOT_EDIT = "FIELD_VALUE_CANNOT_EDIT"  # Field value cannot be edited.
    FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS = (
        "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_CONTAINS_INVALID_CHARACTERS = (
        "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS"  # Remove the invalid characters and try again.
    )
    FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_VALUE_IS_EMPTY = "FIELD_VALUE_IS_EMPTY"  # Update the request with the required information for this resource.
    FIELD_VALUE_IS_INVALID = (
        "FIELD_VALUE_IS_INVALID"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_IS_NULL = "FIELD_VALUE_IS_NULL"  # Update the request with the required information for this resource.
    FIELD_VALUE_IS_OUT_OF_RANGE = "FIELD_VALUE_IS_OUT_OF_RANGE"  # Update the value to be within the required range.
    FIELD_VALUE_MISMATCH = "FIELD_VALUE_MISMATCH"  # Mismatch among resource field values.
    FIELD_VALUE_MUST_BE_EMPTY_OR_NULL = (
        "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_NOT_FOUND = (
        "FIELD_VALUE_NOT_FOUND"  # Resource specified in the field value not found. Try again with valid value.
    )
    FIELD_VALUE_NOT_UNIQUE = "FIELD_VALUE_NOT_UNIQUE"  # Resource field value conflicts with existing resource. Try again with an unique field value.
    FORBIDDEN = "FORBIDDEN"  # The caller is not authorized to make the given request.
    INTERNAL_ERROR = "INTERNAL_ERROR"  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    NOT_FOUND = "NOT_FOUND"  # The requested resource does not exist.
    PAYMENT_ISSUE = "PAYMENT_ISSUE"  # Payment failed.
    PRODUCT_INELIGIBLE = (
        "PRODUCT_INELIGIBLE"  # Product is not eligible for advertising. Try again with a valid product.
    )
    RESOURCE_DOES_NOT_BELONG_TO_PARENT = "RESOURCE_DOES_NOT_BELONG_TO_PARENT"  # Resource does not belong to the specified parent. Try again with a valid parent ID.
    RESOURCE_ID_NOT_FOUND = "RESOURCE_ID_NOT_FOUND"  # Resource ID not found. Try again with valid ID.
    RESOURCE_IS_EMPTY = "RESOURCE_IS_EMPTY"  # Update the request with the required information for this resource.
    RESOURCE_IS_IN_TERMINAL_STATE = "RESOURCE_IS_IN_TERMINAL_STATE"  # Resource is in terminal state.
    RESOURCE_IS_NULL = "RESOURCE_IS_NULL"  # Update the request with the required information for this resource.
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"  # There have been too many requests, please slow down your call rate.
    TOTAL_RESOURCE_LIMIT_EXCEEDED = (
        "TOTAL_RESOURCE_LIMIT_EXCEEDED"  # Too many resources. Remove resources and try again.
    )
    UNAUTHORIZED = "UNAUTHORIZED"  # The request lacks the necessary credentials.
    UNSUPPORTED_MARKETPLACE = (
        "UNSUPPORTED_MARKETPLACE"  # Marketplace not supported. Try again with a supported marketplace.
    )


class SBGoal(StrEnum):
    AWARENESS = "AWARENESS"  # Indicates a goal of driving awareness.
    CONSIDERATION = "CONSIDERATION"  # Indicates a goal of driving consideration.
    CONVERSIONS = "CONVERSIONS"  # Indicates a goal of driving conversions.


class SBKPI(StrEnum):
    CLICKS = "CLICKS"  # Indicates a goal of driving clicks.
    TOP_OF_SEARCH_IMPRESSION_SHARE = (
        "TOP_OF_SEARCH_IMPRESSION_SHARE"  # Indicates a goal of maximizing impression for top search placement.
    )


class SBMarketplace(StrEnum):
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
    IE = "IE"
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
    ZA = "ZA"


class SBPlacement(StrEnum):
    HOME_PAGE = "HOME_PAGE"  # Home page.
    PRODUCT_PAGE = "PRODUCT_PAGE"  # Placements on the product detail page, and all nonsearch placements such as the add-to-cart page.
    REST_OF_SEARCH = "REST_OF_SEARCH"  # Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond.
    TOP_OF_SEARCH = "TOP_OF_SEARCH"  # Placements on the top row of the first-page search results.


class SBRecurrence(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"


class SBSalesChannel(StrEnum):
    AMAZON = "AMAZON"  # A product sold on Amazon-owned sites.
    OFF_AMAZON = "OFF_AMAZON"  # A product sold on a site not owned by Amazon.


class SBShopperSegment(StrEnum):
    NEW_TO_BRAND = "NEW_TO_BRAND"


class SBSiteRestriction(StrEnum):
    AMAZON_BUSINESS = "AMAZON_BUSINESS"  # Restrict the ad to only show on Amazon Business.


class SBAudienceBidAdjustment(LenientModel):
    audienceId: str = Field(description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(
        description="The selection of the percentage change associated with a given audience and bid adjustment settings."
    )


class SBAutoCreationSettings(LenientModel):
    autoCreateTargets: bool | None = Field(
        default=None,
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.",
    )


class SBBidAdjustments(LenientModel):
    audienceBidAdjustments: list[SBAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    placementBidAdjustments: list[SBPlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )
    shopperSegmentBidAdjustments: list[SBShopperSegmentBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Legacy SB field (marked for deprecation)"
    )


class SBBidSettings(LenientModel):
    bidAdjustments: SBBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SBBidStrategy | str, lenient_enum(SBBidStrategy)] | None = Field(default=None)


class SBBudget(LenientModel):
    budgetType: Annotated[SBBudgetType | str, lenient_enum(SBBudgetType)]
    budgetValue: SBBudgetValue
    recurrenceTimePeriod: Annotated[SBRecurrence | str, lenient_enum(SBRecurrence)]


class SBBudgetValue(LenientModel):
    monetaryBudgetValue: SBMonetaryBudgetValue


class SBCampaign(LenientModel):
    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    autoCreationSettings: SBAutoCreationSettings | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[SBBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    costType: Annotated[SBCostType | str, lenient_enum(SBCostType)]
    countries: list[Annotated[SBCountryCode | str, lenient_enum(SBCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime = Field(description="The date time that the campaign was created.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    isMultiAdGroupsEnabled: bool = Field(
        description="A read-only field that indicates whether a campaign supports multiple adGroups."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the campaign was last updated.")
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SBCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    salesChannel: Annotated[SBSalesChannel | str, lenient_enum(SBSalesChannel)] | None = Field(default=None)
    siteRestrictions: list[Annotated[SBSiteRestriction | str, lenient_enum(SBSiteRestriction)]] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SBState | str, lenient_enum(SBState)]
    status: SBStatus | None = Field(default=None)
    tags: list[SBTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class SBCampaignAdProductFilter(StrictModel):
    include: list[Annotated[SBAdProduct, lenient_enum(SBAdProduct)]] = Field(min_length=1, max_length=1)


class SBCampaignCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBCampaignCreate(StrictModel):
    adProduct: Annotated[SBAdProduct, lenient_enum(SBAdProduct)]
    autoCreationSettings: SBCreateAutoCreationSettings | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[SBCreateBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    costType: Annotated[SBCostType, lenient_enum(SBCostType)]
    countries: list[Annotated[SBCountryCode, lenient_enum(SBCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaceScope: Annotated[SBMarketplaceScope, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[Annotated[SBMarketplace, lenient_enum(SBMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SBCreateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    salesChannel: Annotated[SBSalesChannel, lenient_enum(SBSalesChannel)] | None = Field(default=None)
    siteRestrictions: list[Annotated[SBSiteRestriction, lenient_enum(SBSiteRestriction)]] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SBCreateState, lenient_enum(SBCreateState)]
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class SBCampaignGoalFilter(StrictModel):
    include: list[Annotated[SBGoal, lenient_enum(SBGoal)]] = Field(min_length=1, max_length=3)


class SBCampaignMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBCampaignMultiStatusSuccess(LenientModel):
    campaign: SBCampaign
    index: int = Field(ge=0, le=9)


class SBCampaignNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SBCampaignNameFilterType, lenient_enum(SBCampaignNameFilterType)]


class SBCampaignOptimizations(LenientModel):
    bidSettings: SBBidSettings | None = Field(default=None)
    goalSettings: SBGoalSettings | None = Field(default=None)


class SBCampaignPortfolioIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBCampaignStateFilter(StrictModel):
    include: list[Annotated[SBState, lenient_enum(SBState)]] = Field(min_length=1, max_length=3)


class SBCampaignSuccessResponse(LenientModel):
    campaigns: list[SBCampaign] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SBCampaignUpdate(StrictModel):
    budgets: list[SBCreateBudget] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: SBUpdateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: Annotated[SBUpdateState, lenient_enum(SBUpdateState)] | None = Field(default=None)
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class SBCreateAudienceBidAdjustment(StrictModel):
    audienceId: str = Field(description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(
        description="The selection of the percentage change associated with a given audience and bid adjustment settings."
    )


class SBCreateAutoCreationSettings(StrictModel):
    autoCreateTargets: bool | None = Field(
        default=None,
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.",
    )


class SBCreateBidAdjustments(StrictModel):
    audienceBidAdjustments: list[SBCreateAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    placementBidAdjustments: list[SBCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )
    shopperSegmentBidAdjustments: list[SBCreateShopperSegmentBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Legacy SB field (marked for deprecation)"
    )


class SBCreateBidSettings(StrictModel):
    bidAdjustments: SBCreateBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SBBidStrategy, lenient_enum(SBBidStrategy)] | None = Field(default=None)


class SBCreateBudget(StrictModel):
    budgetType: Annotated[SBBudgetType, lenient_enum(SBBudgetType)]
    budgetValue: SBCreateBudgetValue
    recurrenceTimePeriod: Annotated[SBRecurrence, lenient_enum(SBRecurrence)]


class SBCreateBudgetValue(StrictModel):
    monetaryBudgetValue: SBCreateMonetaryBudgetValue


class SBCreateCampaignOptimizations(StrictModel):
    bidSettings: SBCreateBidSettings | None = Field(default=None)
    goalSettings: SBCreateGoalSettings | None = Field(default=None)


class SBCreateCampaignRequest(StrictModel):
    campaigns: list[SBCampaignCreate] = Field(min_length=1, max_length=10)


class SBCreateGoalSettings(StrictModel):
    kpi: Annotated[SBKPI, lenient_enum(SBKPI)]


class SBCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SBCreateMonetaryBudgetValue(StrictModel):
    monetaryBudget: SBCreateMonetaryBudget


class SBCreatePlacementBidAdjustment(StrictModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: Annotated[SBPlacement, lenient_enum(SBPlacement)]


class SBCreateShopperSegmentBidAdjustment(StrictModel):
    pass


class SBDeleteCampaignRequest(StrictModel):
    campaignIds: list[str] = Field(min_length=1, max_length=10)


class SBError(LenientModel):
    code: Annotated[SBErrorCode | str, lenient_enum(SBErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class SBErrorsIndex(LenientModel):
    errors: list[SBError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=4999)


class SBGoalSettings(LenientModel):
    goal: Annotated[SBGoal | str, lenient_enum(SBGoal)]
    kpi: Annotated[SBKPI | str, lenient_enum(SBKPI)]


class SBMonetaryBudget(LenientModel):
    currencyCode: Annotated[SBCurrencyCode | str, lenient_enum(SBCurrencyCode)]
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SBMonetaryBudgetValue(LenientModel):
    monetaryBudget: SBMonetaryBudget


class SBPlacementBidAdjustment(LenientModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: Annotated[SBPlacement | str, lenient_enum(SBPlacement)]


class SBQueryCampaignRequest(StrictModel):
    adProductFilter: SBCampaignAdProductFilter
    campaignIdFilter: SBCampaignCampaignIdFilter | None = Field(default=None)
    goalFilter: SBCampaignGoalFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SBCampaignNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    portfolioIdFilter: SBCampaignPortfolioIdFilter | None = Field(default=None)
    stateFilter: SBCampaignStateFilter | None = Field(default=None)


class SBShopperSegmentBidAdjustment(LenientModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given shopper segment and bid adjustment settings."
    )
    shopperSegment: Annotated[SBShopperSegment | str, lenient_enum(SBShopperSegment)]


class SBUpdateBidAdjustments(StrictModel):
    audienceBidAdjustments: list[SBCreateAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    placementBidAdjustments: list[SBCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )
    shopperSegmentBidAdjustments: list[SBCreateShopperSegmentBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Legacy SB field (marked for deprecation)"
    )


class SBUpdateBidSettings(StrictModel):
    bidAdjustments: SBUpdateBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SBBidStrategy, lenient_enum(SBBidStrategy)] | None = Field(default=None)


class SBUpdateCampaignOptimizations(StrictModel):
    bidSettings: SBUpdateBidSettings | None = Field(default=None)


class SBUpdateCampaignRequest(StrictModel):
    campaigns: list[SBCampaignUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "SBAdProduct",
    "SBAudienceBidAdjustment",
    "SBAutoCreationSettings",
    "SBBidAdjustments",
    "SBBidSettings",
    "SBBidStrategy",
    "SBBudget",
    "SBBudgetType",
    "SBBudgetValue",
    "SBCampaign",
    "SBCampaignAdProductFilter",
    "SBCampaignCampaignIdFilter",
    "SBCampaignCreate",
    "SBCampaignGoalFilter",
    "SBCampaignMultiStatusResponse",
    "SBCampaignMultiStatusSuccess",
    "SBCampaignNameFilter",
    "SBCampaignNameFilterType",
    "SBCampaignOptimizations",
    "SBCampaignPortfolioIdFilter",
    "SBCampaignStateFilter",
    "SBCampaignSuccessResponse",
    "SBCampaignUpdate",
    "SBCostType",
    "SBCountryCode",
    "SBCreateAudienceBidAdjustment",
    "SBCreateAutoCreationSettings",
    "SBCreateBidAdjustments",
    "SBCreateBidSettings",
    "SBCreateBudget",
    "SBCreateBudgetValue",
    "SBCreateCampaignOptimizations",
    "SBCreateCampaignRequest",
    "SBCreateGoalSettings",
    "SBCreateMonetaryBudget",
    "SBCreateMonetaryBudgetValue",
    "SBCreatePlacementBidAdjustment",
    "SBCreateShopperSegmentBidAdjustment",
    "SBCreateState",
    "SBCreateTag",
    "SBCurrencyCode",
    "SBDeleteCampaignRequest",
    "SBDeliveryReason",
    "SBDeliveryStatus",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBGoal",
    "SBGoalSettings",
    "SBKPI",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBMonetaryBudget",
    "SBMonetaryBudgetValue",
    "SBPlacement",
    "SBPlacementBidAdjustment",
    "SBQueryCampaignRequest",
    "SBRecurrence",
    "SBSalesChannel",
    "SBShopperSegment",
    "SBShopperSegmentBidAdjustment",
    "SBSiteRestriction",
    "SBState",
    "SBStatus",
    "SBTag",
    "SBUpdateBidAdjustments",
    "SBUpdateBidSettings",
    "SBUpdateCampaignOptimizations",
    "SBUpdateCampaignRequest",
    "SBUpdateState",
]
