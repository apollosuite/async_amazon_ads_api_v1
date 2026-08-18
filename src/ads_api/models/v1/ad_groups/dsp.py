"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.dsp import (
    DSPBudgetType,
    DSPCreateTag,
    DSPFeesThirdPartyProvider,
    DSPRecurrence,
    DSPTimeUnit,
)


class DSPAdProduct(StrEnum):
    AMAZON_DSP = "AMAZON_DSP"  # Amazon Demand-Side Platform ad product.


class DSPAutomatedTargetingTactic(StrEnum):
    AWARENESS = "AWARENESS"  # Ad Group tactic (Complete TV) that indicates that this line item drives awareness to your selected audience on publisher streaming TV for the linked deal while fulfilling your commitment.
    CUSTOMER_ACQUISITION = (
        "CUSTOMER_ACQUISITION"  # Ad Group Tactic (P+) that reaches shoppers who are similar to past purchasers
    )
    MAXIMIZE_PERFORMANCE = "MAXIMIZE_PERFORMANCE"  # Ad Group Tactic (P+) that reaches shoppers who are similar to past shoppers who viewed a product detail page
    PROSPECTING = "PROSPECTING"  # Ad Group Tactic (B+) that reaches consumers who are highly likely to show interest and engage with your brand or product
    REMARKETING = "REMARKETING"  # Ad Group Tactic (P+) that reaches shoppers who have viewed a product detail page, searched for your product, or visited your homepage
    RETENTION = "RETENTION"  # Ad Group Tactic (P+) that reaches shoppers who have purchased your product
    SEARCH = "SEARCH"  # Ad Group Tactic that targets shoppers based on search signals.


class DSPBidStrategy(StrEnum):
    PRIORITIZE_KPI_TARGET = "PRIORITIZE_KPI_TARGET"  # Optimizes bidding to achieve the KPI target specified.
    SPEND_BUDGET_IN_FULL = "SPEND_BUDGET_IN_FULL"  # Prioritize spending full budget, while maximizing performance
    USE_CAMPAIGN_STRATEGY = "USE_CAMPAIGN_STRATEGY"  # Inherit the bid strategy from the parent campaign.


class DSPBudgetAllocation(StrEnum):
    AUTO = "AUTO"  # Automatically allocate budget to better performing ad groups based on the selected goal KPI.
    MANUAL = "MANUAL"  # Manually allocate budget across ad groups.


class DSPCreateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class DSPCreativeRotationType(StrEnum):
    RANDOM = "RANDOM"  # Creatives are rotated randomly with equal weight.
    WEIGHTED = "WEIGHTED"  # Creatives are rotated based on assigned weights.


class DSPCurrencyCode(StrEnum):
    AED = "AED"  # United Arab Emirates Dirham
    ARS = "ARS"  # Argentine Peso
    AUD = "AUD"  # Australian Dollar
    BGN = "BGN"  # Bulgarian Lev
    BHD = "BHD"  # Bahraini Dinar
    BOB = "BOB"  # Bolivian Boliviano
    BRL = "BRL"  # Brazilian Real
    CAD = "CAD"  # Canadian Dollar
    CHF = "CHF"  # Swiss Franc
    CLP = "CLP"  # Chilean Peso
    CNY = "CNY"  # Chinese Yuan
    COP = "COP"  # Colombian Peso
    CRC = "CRC"  # Costa Rican Colón
    CZK = "CZK"  # Czech Koruna
    DKK = "DKK"  # Danish Krone
    DOP = "DOP"  # Dominican Peso
    DZD = "DZD"  # Algerian Dinar
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound Sterling
    GTQ = "GTQ"  # Guatemalan Quetzal
    HKD = "HKD"  # Hong Kong Dollar
    HNL = "HNL"  # Honduran Lempira
    HRK = "HRK"  # Croatian Kuna
    HUF = "HUF"  # Hungarian Forint
    IDR = "IDR"  # Indonesian Rupiah
    ILS = "ILS"  # Israeli New Shekel
    INR = "INR"  # Indian Rupee
    JMD = "JMD"  # Jamaican Dollar
    JPY = "JPY"  # Japanese Yen
    KRW = "KRW"  # South Korean Won
    KWD = "KWD"  # Kuwaiti Dinar
    MAD = "MAD"  # Moroccan Dirham
    MXN = "MXN"  # Mexican Peso
    MYR = "MYR"  # Malaysian Ringgit
    NOK = "NOK"  # Norwegian Krone
    PAB = "PAB"  # Panamanian Balboa
    PEN = "PEN"  # Peruvian Sol
    PHP = "PHP"  # Philippine Peso
    PKR = "PKR"  # Pakistani Rupee
    PYG = "PYG"  # Paraguayan Guaraní
    QAR = "QAR"  # Qatari Riyal
    RON = "RON"  # Romanian Leu
    RSD = "RSD"  # Serbian Dinar
    RUB = "RUB"  # Russian Ruble
    SAR = "SAR"  # Saudi Riyal
    SEK = "SEK"  # Swedish Krona
    SGD = "SGD"  # Singapore Dollar
    THB = "THB"  # Thai Baht
    TND = "TND"  # Tunisian Dinar
    TRY = "TRY"  # Turkish Lira
    TWD = "TWD"  # New Taiwan Dollar
    UAH = "UAH"  # Ukrainian Hryvnia
    USD = "USD"  # United States Dollar
    UYU = "UYU"  # Uruguayan Peso
    VND = "VND"  # Vietnamese Đồng


class DSPDefaultAudienceTargetingMatchType(StrEnum):
    """
    Match type for audience targeting inclusion groups, if any. You can enhance your ad group’s reach to consumers with similar shopping, streaming, and browsing behaviors or interests as your selected audiences across all inventory sources, regardless of the presence of ad identifiers. Only applicable at the adGroup level, rather than at individual audience level. (Default: SIMILAR). Note, SIMILAR is not applicable to certain advertised product categories, [see here](https://advertising.amazon.com/help/GX8G7HNDS5RBX3EF) for more information.
    """

    EXACT = "EXACT"  # Target the exact audiences specified in the ad group audience targeting.
    SIMILAR = "SIMILAR"  # Reach more audiences who are similar to your included audiences.


class DSPDeliveryProfile(StrEnum):
    ASAP = "ASAP"  # Makes your entire budget available to spend immediately. This is ideal for ad groups with limited inventory or when there's no requirement to spend throughout the length of the campaign.Warning: Selecting ASAP may result in your entire budget being spent immediately.
    EVEN = "EVEN"  # Even pacing spends your budget consistently across the length of the campaign.
    PACE_AHEAD = "PACE_AHEAD"  # Pace Ahead can deliver up to 25% more than the daily Even pace targets.


class DSPDeliveryReason(StrEnum):
    AD_CREATIVES_NOT_RUNNING = "AD_CREATIVES_NOT_RUNNING"
    AD_GROUPS_NOT_RUNNING = "AD_GROUPS_NOT_RUNNING"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_ENDED = "AD_GROUP_ENDED"
    AD_GROUP_INELIGIBLE_GOAL_KPI = "AD_GROUP_INELIGIBLE_GOAL_KPI"  # Indicates that the ad group is suspended because the campaign's goal KPI is not supported.
    AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS"  # Indicates that the ad group is suspended because the campaign is missing conversion tracking selections.
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_PENDING_START_DATE = "AD_GROUP_PENDING_START_DATE"
    AD_GROUP_POLICING_SUSPENDED = "AD_GROUP_POLICING_SUSPENDED"
    AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS"  # Indicates that the ad group is suspended because the campaign has an insufficient number of conversion tracking selections.
    AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS"  # Indicates that the ad group is suspended because the campaign exceeded the maximum number of conversion tracking selections.
    AD_NOT_APPROVED_FOR_ALL_AD_GROUPS = "AD_NOT_APPROVED_FOR_ALL_AD_GROUPS"
    AD_NOT_ASSOCIATED_WITH_AD_GROUP = "AD_NOT_ASSOCIATED_WITH_AD_GROUP"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_END_DATE_REACHED = "CAMPAIGN_END_DATE_REACHED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    CAMPAIGN_POLICING_SUSPENDED = "CAMPAIGN_POLICING_SUSPENDED"
    OTHER = "OTHER"


class DSPDeliveryStatus(StrEnum):
    DELIVERING = "DELIVERING"  # Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
    LIMITED = "LIMITED"  # Represents partial delivery status, applicable to global resources that have different delivery status across marketplaces
    NOT_DELIVERING = "NOT_DELIVERING"  # Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
    UNAVAILABLE = "UNAVAILABLE"  # Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces


class DSPErrorCode(StrEnum):
    ACTION_NOT_SUPPORTED = "ACTION_NOT_SUPPORTED"  # The request is not supported.
    ACTIVE_RESOURCE_LIMIT_EXCEEDED = (
        "ACTIVE_RESOURCE_LIMIT_EXCEEDED"  # Too many live resources. Remove resources and try again.
    )
    ARCHIVED_PARENT_CANNOT_CREATE = (
        "ARCHIVED_PARENT_CANNOT_CREATE"  # New resources cannot be created within an archived parent.
    )
    ARCHIVED_PARENT_CANNOT_EDIT = "ARCHIVED_PARENT_CANNOT_EDIT"  # Resources within an archived parent cannot be edited.
    ARCHIVED_RESOURCE_CANNOT_EDIT = "ARCHIVED_RESOURCE_CANNOT_EDIT"  # Archived resources cannot be edited.
    ASSET_NOT_READY = "ASSET_NOT_READY"  # The provided asset is still being processed.
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


class DSPFeeType(StrEnum):
    AMAZON_AUDIENCE = "AMAZON_AUDIENCE"  # CPM fee for using Amazon audiences.
    AMAZON_DSP = "AMAZON_DSP"  # A service fee for using Amazon DSP and subtracted from the budget. This fee is applied as a percent of supply cost.
    MANAGED_SERVICE_FEE = "MANAGED_SERVICE_FEE"  # The percentage-based fee applied to the Supply Cost for Amazon programmatic managed service.
    OMNICHANNEL_METRICS = "OMNICHANNEL_METRICS"  # Fee for using Amazon Omnichannel Metrics.
    THIRD_PARTY_APPLIED = "THIRD_PARTY_APPLIED"  # User added CPM fee for using third-party data to track CPM costs. This fee is applied as a percent of supply cost.
    THIRD_PARTY_AUDIENCE = "THIRD_PARTY_AUDIENCE"  # CPM fee for using a third party audience.
    THIRD_PARTY_TARGETING = (
        "THIRD_PARTY_TARGETING"  # CPM fee for using targeting provided by a third-party data provider.
    )


class DSPFeeValueType(StrEnum):
    FIXED_CPM = "FIXED_CPM"  # Charged based on a fixed CPM. The currency depends on the feeType.
    PERCENTAGE_OF_BUDGET = "PERCENTAGE_OF_BUDGET"  # Subtracted from the campaign budget as a percent of budget
    PERCENTAGE_OF_SUPPLY_COST = "PERCENTAGE_OF_SUPPLY_COST"  # Charged as a percent of supply (media) cost. Ranges from 0 to 1 where 0.15 represents 15%.


class DSPFrequencyTargetingSetting(StrEnum):
    HOUSEHOLD = "HOUSEHOLD"  # Control frequency an ad will be selected across people within the same household.
    USER = "USER"  # Control frequency an ad will be selected to a person.


class DSPInventoryType(StrEnum):
    AAP_MOBILE_APP = "AAP_MOBILE_APP"
    AMAZON_MOBILE_DISPLAY = "AMAZON_MOBILE_DISPLAY"
    AUDIO = "AUDIO"  # Audio ads that serve on streaming audio inventory.
    AUDIO_AMAZON_DEAL = "AUDIO_AMAZON_DEAL"
    DISPLAY = "DISPLAY"
    LIVE_EVENTS = "LIVE_EVENTS"  # Real-time broadcast inventory (sports, concerts, award shows) with audience volatility and concentrated traffic patterns requiring specialized pacing algorithms and event-specific metadata handling.
    ONLINE_VIDEO = "ONLINE_VIDEO"
    PODCAST = "PODCAST"  # Podcast ads that serve on streaming podcast inventory.
    STANDARD_DISPLAY = "STANDARD_DISPLAY"
    STREAMING_TV = "STREAMING_TV"
    STREAMING_TV_AMAZON_DEAL = "STREAMING_TV_AMAZON_DEAL"
    VIDEO = "VIDEO"


class DSPSiteLanguage(StrEnum):
    AR = "AR"  # Arabic.
    BN = "BN"  # Bengali.
    CS = "CS"  # Czech.
    DA = "DA"  # Danish.
    DE = "DE"  # German.
    EN = "EN"  # English.
    ES = "ES"  # Spanish.
    FI = "FI"  # Finnish.
    FR = "FR"  # French.
    GU = "GU"  # Gujarati.
    HI = "HI"  # Hindi.
    IT = "IT"  # Italian.
    JA = "JA"  # Japanese.
    KN = "KN"  # Kannada.
    ML = "ML"  # Malayalam.
    MR = "MR"  # Marathi.
    NL = "NL"  # Dutch.
    NO = "NO"  # Norwegian.
    OTHER = "OTHER"  # Other language.
    PA = "PA"  # Punjabi.
    PL = "PL"  # Polish.
    PT = "PT"  # Portuguese.
    SV = "SV"  # Swedish.
    TA = "TA"  # Tamil.
    TE = "TE"  # Telugu.
    TR = "TR"  # Turkish.
    ZH = "ZH"  # Chinese.


class DSPState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ARCHIVED = "ARCHIVED"  # The object is permanently stopped and cannot be reactivated. Terminal end state.
    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class DSPTacticsConvertersExclusionType(StrEnum):
    NO_EXCLUSION = "NO_EXCLUSION"  # Do not exclude any converters from targeting.
    RECENT_CONVERTERS = "RECENT_CONVERTERS"  # Exclude recent converters from targeting to focus on new customers.


class DSPTimeZoneType(StrEnum):
    ADVERTISER_REGION = "ADVERTISER_REGION"  # Use the advertiser's regional time zone for daypart targeting.
    VIEWER = "VIEWER"  # Use the viewer's local time zone for daypart targeting.


class DSPUpdateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class DSPUserLocationSignal(StrEnum):
    CURRENT = "CURRENT"  # Target users based on their current geographic location.
    MULTIPLE_SIGNALS = "MULTIPLE_SIGNALS"  # Target users based on multiple location signals.


class DSPVideoCompletionTier(StrEnum):
    ALL_TIERS = "ALL_TIERS"  # Target all video completion tiers.
    GREATER_THAN_10_PERCENT = (
        "GREATER_THAN_10_PERCENT"  # Target videos with greater than 10% predicted completion rate.
    )
    GREATER_THAN_20_PERCENT = (
        "GREATER_THAN_20_PERCENT"  # Target videos with greater than 20% predicted completion rate.
    )
    GREATER_THAN_30_PERCENT = (
        "GREATER_THAN_30_PERCENT"  # Target videos with greater than 30% predicted completion rate.
    )
    GREATER_THAN_40_PERCENT = (
        "GREATER_THAN_40_PERCENT"  # Target videos with greater than 40% predicted completion rate.
    )
    GREATER_THAN_50_PERCENT = (
        "GREATER_THAN_50_PERCENT"  # Target videos with greater than 50% predicted completion rate.
    )
    GREATER_THAN_60_PERCENT = (
        "GREATER_THAN_60_PERCENT"  # Target videos with greater than 60% predicted completion rate.
    )
    GREATER_THAN_70_PERCENT = (
        "GREATER_THAN_70_PERCENT"  # Target videos with greater than 70% predicted completion rate.
    )
    GREATER_THAN_80_PERCENT = (
        "GREATER_THAN_80_PERCENT"  # Target videos with greater than 80% predicted completion rate.
    )
    GREATER_THAN_90_PERCENT = (
        "GREATER_THAN_90_PERCENT"  # Target videos with greater than 90% predicted completion rate.
    )


class DSPViewabilityTier(StrEnum):
    ALL_TIERS = "ALL_TIERS"  # Target all viewability tiers with no filtering.
    GREATER_THAN_40_PERCENT = (
        "GREATER_THAN_40_PERCENT"  # Target impressions with greater than 40% predicted viewability.
    )
    GREATER_THAN_50_PERCENT = (
        "GREATER_THAN_50_PERCENT"  # Target impressions with greater than 50% predicted viewability.
    )
    GREATER_THAN_60_PERCENT = (
        "GREATER_THAN_60_PERCENT"  # Target impressions with greater than 60% predicted viewability.
    )
    GREATER_THAN_70_PERCENT = (
        "GREATER_THAN_70_PERCENT"  # Target impressions with greater than 70% predicted viewability.
    )
    LESS_THAN_40_PERCENT = "LESS_THAN_40_PERCENT"  # Target impressions with less than 40% predicted viewability.


class DSPAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)]
    advertisedProductCategoryIds: list[str] = Field(
        min_length=1,
        max_length=500,
        description="The array of identifiers of advertised product categories associated with the ad group. For VIDEO ad group type only one parent product category or multiple sub-categories from one parent product category are allowed.",
    )
    bid: DSPAdGroupBid
    budgets: list[DSPBudget] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing budget details for the ad group."
    )
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creationDateTime: datetime = Field(description="The date time that the ad group was created.")
    creativeRotationType: Annotated[DSPCreativeRotationType | str, lenient_enum(DSPCreativeRotationType)]
    endDateTime: datetime = Field(description="The end date time for the ad group.")
    fees: list[DSPFee] | None = Field(
        default=None, min_length=0, max_length=7, description="The fees associated with the ad group."
    )
    frequencies: list[DSPFrequency] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing frequency details for the ad group."
    )
    inventoryType: Annotated[DSPInventoryType | str, lenient_enum(DSPInventoryType)]
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad group was last updated.")
    name: str = Field(description="The name of the ad group.")
    optimization: DSPOptimization
    pacing: DSPPacing
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the ad group."
    )
    startDateTime: datetime = Field(description="The start date time for the ad group.")
    state: Annotated[DSPState | str, lenient_enum(DSPState)]
    status: DSPStatus | None = Field(default=None)
    tags: list[DSPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="Open ended labels with a key value pair applied to the ad group",
    )
    targetingSettings: DSPTargetingSettings


class DSPAdGroupAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class DSPAdGroupAdProductFilter(StrictModel):
    include: list[Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)]] = Field(min_length=1, max_length=1)


class DSPAdGroupBid(LenientModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    currencyCode: Annotated[DSPCurrencyCode | str, lenient_enum(DSPCurrencyCode)]
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPAdGroupBudgetSettings(LenientModel):
    budgetAllocation: Annotated[DSPBudgetAllocation | str, lenient_enum(DSPBudgetAllocation)] | None = Field(
        default=None
    )
    dailyMinSpendValue: float | None = Field(
        default=None, description="Denotes the daily minimum spend on the ad group in local currency."
    )


class DSPAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPAdGroupCreate(StrictModel):
    adProduct: Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)]
    advertisedProductCategoryIds: list[str] = Field(
        min_length=1,
        max_length=500,
        description="The array of identifiers of advertised product categories associated with the ad group. For VIDEO ad group type only one parent product category or multiple sub-categories from one parent product category are allowed.",
    )
    bid: DSPCreateAdGroupBid
    budgets: list[DSPCreateBudget] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing budget details for the ad group."
    )
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creativeRotationType: Annotated[DSPCreativeRotationType | str, lenient_enum(DSPCreativeRotationType)]
    endDateTime: datetime = Field(description="The end date time for the ad group.")
    fees: list[DSPCreateFee] | None = Field(
        default=None, min_length=0, max_length=7, description="The fees associated with the ad group."
    )
    frequencies: list[DSPCreateFrequency] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing frequency details for the ad group."
    )
    inventoryType: Annotated[DSPInventoryType | str, lenient_enum(DSPInventoryType)]
    name: str = Field(description="The name of the ad group.")
    optimization: DSPCreateOptimization
    pacing: DSPCreatePacing
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the ad group."
    )
    startDateTime: datetime = Field(description="The start date time for the ad group.")
    state: Annotated[DSPCreateState | str, lenient_enum(DSPCreateState)]
    tags: list[DSPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="Open ended labels with a key value pair applied to the ad group",
    )
    targetingSettings: DSPCreateTargetingSettings


class DSPAdGroupMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=20)
    success: list[DSPAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=20)


class DSPAdGroupMultiStatusSuccess(LenientModel):
    adGroup: DSPAdGroup
    index: int = Field(ge=0, le=19)


class DSPAdGroupStateFilter(StrictModel):
    include: list[Annotated[DSPState | str, lenient_enum(DSPState)]] = Field(min_length=1, max_length=3)


class DSPAdGroupSuccessResponse(LenientModel):
    adGroups: list[DSPAdGroup] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class DSPAdGroupUpdate(StrictModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    advertisedProductCategoryIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=500,
        description="The array of identifiers of advertised product categories associated with the ad group. For VIDEO ad group type only one parent product category or multiple sub-categories from one parent product category are allowed.",
    )
    bid: DSPUpdateAdGroupBid | None = Field(default=None)
    budgets: list[DSPCreateBudget] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing budget details for the ad group."
    )
    creativeRotationType: Annotated[DSPCreativeRotationType | str, lenient_enum(DSPCreativeRotationType)] | None = (
        Field(default=None)
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad group.")
    fees: list[DSPCreateFee] | None = Field(
        default=None, min_length=0, max_length=7, description="The fees associated with the ad group."
    )
    frequencies: list[DSPCreateFrequency] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing frequency details for the ad group."
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    optimization: DSPUpdateOptimization | None = Field(default=None)
    pacing: DSPUpdatePacing | None = Field(default=None)
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the ad group."
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad group.")
    state: Annotated[DSPUpdateState | str, lenient_enum(DSPUpdateState)] | None = Field(default=None)
    tags: list[DSPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="Open ended labels with a key value pair applied to the ad group",
    )
    targetingSettings: DSPUpdateTargetingSettings | None = Field(default=None)


class DSPAmazonViewability(LenientModel):
    includeUnmeasurableImpressions: bool = Field(
        description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measured when a viewabilityTier other than ALL_TIERS is selected. We recommend setting to false if high viewability is your goal."
    )
    viewabilityTier: Annotated[DSPViewabilityTier | str, lenient_enum(DSPViewabilityTier)]


class DSPBudget(LenientModel):
    budgetType: Annotated[DSPBudgetType | str, lenient_enum(DSPBudgetType)]
    budgetValue: DSPBudgetValue
    recurrenceTimePeriod: Annotated[DSPRecurrence | str, lenient_enum(DSPRecurrence)]


class DSPBudgetValue(LenientModel):
    monetaryBudgetValue: DSPMonetaryBudgetValue


class DSPCreateAdGroupBid(StrictModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPCreateAdGroupBudgetSettings(StrictModel):
    budgetAllocation: Annotated[DSPBudgetAllocation | str, lenient_enum(DSPBudgetAllocation)] | None = Field(
        default=None
    )
    dailyMinSpendValue: float | None = Field(
        default=None, description="Denotes the daily minimum spend on the ad group in local currency."
    )


class DSPCreateAdGroupRequest(StrictModel):
    adGroups: list[DSPAdGroupCreate] = Field(min_length=1, max_length=20)


class DSPCreateAmazonViewability(StrictModel):
    includeUnmeasurableImpressions: bool = Field(
        description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measured when a viewabilityTier other than ALL_TIERS is selected. We recommend setting to false if high viewability is your goal."
    )
    viewabilityTier: Annotated[DSPViewabilityTier | str, lenient_enum(DSPViewabilityTier)]


class DSPCreateBudget(StrictModel):
    budgetType: Annotated[DSPBudgetType | str, lenient_enum(DSPBudgetType)]
    budgetValue: DSPCreateBudgetValue
    recurrenceTimePeriod: Annotated[DSPRecurrence | str, lenient_enum(DSPRecurrence)]


class DSPCreateBudgetValue(StrictModel):
    monetaryBudgetValue: DSPCreateMonetaryBudgetValue


class DSPCreateFee(StrictModel):
    addToBudgetSpentAmount: bool = Field(
        description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad group budget spent amount in reports."
    )
    feeType: Annotated[DSPFeeType | str, lenient_enum(DSPFeeType)]
    feeValue: float = Field(
        description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the marketplace. All other CPM based fees are in the currency of the advertiser. For percentages, 100 represents 100%."
    )
    thirdPartyProvider: Annotated[DSPFeesThirdPartyProvider | str, lenient_enum(DSPFeesThirdPartyProvider)]


class DSPCreateFrequency(StrictModel):
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    frequencyTargetingSetting: Annotated[DSPFrequencyTargetingSetting | str, lenient_enum(DSPFrequencyTargetingSetting)]
    timeCount: int = Field(
        ge=1, le=60, description="The value associated with the time and unit of time for this frequency cap."
    )
    timeUnit: Annotated[DSPTimeUnit | str, lenient_enum(DSPTimeUnit)]


class DSPCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPCreateMonetaryBudgetValue(StrictModel):
    monetaryBudget: DSPCreateMonetaryBudget | None = Field(default=None)


class DSPCreateOptimization(StrictModel):
    bidStrategy: Annotated[DSPBidStrategy | str, lenient_enum(DSPBidStrategy)]
    budgetSettings: DSPCreateAdGroupBudgetSettings | None = Field(default=None)


class DSPCreatePacing(StrictModel):
    deliveryProfile: Annotated[DSPDeliveryProfile | str, lenient_enum(DSPDeliveryProfile)]


class DSPCreateTargetingSettings(StrictModel):
    amazonViewability: DSPCreateAmazonViewability
    automatedTargetingTactic: (
        Annotated[DSPAutomatedTargetingTactic | str, lenient_enum(DSPAutomatedTargetingTactic)] | None
    ) = Field(default=None)
    defaultAudienceTargetingMatchType: (
        Annotated[DSPDefaultAudienceTargetingMatchType | str, lenient_enum(DSPDefaultAudienceTargetingMatchType)] | None
    ) = Field(default=None)
    enableLanguageTargeting: bool | None = Field(
        default=None,
        description="If set to true, creatives will only target supply where the content language matches the creative language.",
    )
    tacticsConvertersExclusionType: (
        Annotated[DSPTacticsConvertersExclusionType | str, lenient_enum(DSPTacticsConvertersExclusionType)] | None
    ) = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed deal, the deal can be provided here.",
    )
    timeZoneType: Annotated[DSPTimeZoneType | str, lenient_enum(DSPTimeZoneType)]
    userLocationSignal: Annotated[DSPUserLocationSignal | str, lenient_enum(DSPUserLocationSignal)]
    videoCompletionTier: Annotated[DSPVideoCompletionTier | str, lenient_enum(DSPVideoCompletionTier)] | None = Field(
        default=None
    )


class DSPError(LenientModel):
    code: Annotated[DSPErrorCode | str, lenient_enum(DSPErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=4999)


class DSPFee(LenientModel):
    addToBudgetSpentAmount: bool = Field(
        description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad group budget spent amount in reports."
    )
    currencyCode: Annotated[DSPCurrencyCode | str, lenient_enum(DSPCurrencyCode)] | None = Field(default=None)
    feeType: Annotated[DSPFeeType | str, lenient_enum(DSPFeeType)]
    feeValue: float = Field(
        description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the marketplace. All other CPM based fees are in the currency of the advertiser. For percentages, 100 represents 100%."
    )
    feeValueType: Annotated[DSPFeeValueType | str, lenient_enum(DSPFeeValueType)]
    thirdPartyProvider: Annotated[DSPFeesThirdPartyProvider | str, lenient_enum(DSPFeesThirdPartyProvider)]


class DSPFrequency(LenientModel):
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    frequencyTargetingSetting: Annotated[DSPFrequencyTargetingSetting | str, lenient_enum(DSPFrequencyTargetingSetting)]
    timeCount: int = Field(
        ge=1, le=60, description="The value associated with the time and unit of time for this frequency cap."
    )
    timeUnit: Annotated[DSPTimeUnit | str, lenient_enum(DSPTimeUnit)]


class DSPMonetaryBudget(LenientModel):
    currencyCode: Annotated[DSPCurrencyCode | str, lenient_enum(DSPCurrencyCode)]
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPMonetaryBudgetValue(LenientModel):
    monetaryBudget: DSPMonetaryBudget | None = Field(default=None)


class DSPOptimization(LenientModel):
    bidStrategy: Annotated[DSPBidStrategy | str, lenient_enum(DSPBidStrategy)]
    budgetSettings: DSPAdGroupBudgetSettings | None = Field(default=None)


class DSPPacing(LenientModel):
    deliveryProfile: Annotated[DSPDeliveryProfile | str, lenient_enum(DSPDeliveryProfile)]


class DSPQueryAdGroupRequest(StrictModel):
    adGroupIdFilter: DSPAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: DSPAdGroupAdProductFilter
    campaignIdFilter: DSPAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    stateFilter: DSPAdGroupStateFilter | None = Field(default=None)


class DSPStatus(LenientModel):
    deliveryReasons: list[Annotated[DSPDeliveryReason | str, lenient_enum(DSPDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[DSPDeliveryStatus | str, lenient_enum(DSPDeliveryStatus)]


class DSPTag(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPTargetingSettings(LenientModel):
    amazonViewability: DSPAmazonViewability
    automatedTargetingTactic: (
        Annotated[DSPAutomatedTargetingTactic | str, lenient_enum(DSPAutomatedTargetingTactic)] | None
    ) = Field(default=None)
    defaultAudienceTargetingMatchType: (
        Annotated[DSPDefaultAudienceTargetingMatchType | str, lenient_enum(DSPDefaultAudienceTargetingMatchType)] | None
    ) = Field(default=None)
    enableLanguageTargeting: bool | None = Field(
        default=None,
        description="If set to true, creatives will only target supply where the content language matches the creative language.",
    )
    siteLanguage: Annotated[DSPSiteLanguage | str, lenient_enum(DSPSiteLanguage)] | None = Field(default=None)
    tacticsConvertersExclusionType: (
        Annotated[DSPTacticsConvertersExclusionType | str, lenient_enum(DSPTacticsConvertersExclusionType)] | None
    ) = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed deal, the deal can be provided here.",
    )
    timeZoneType: Annotated[DSPTimeZoneType | str, lenient_enum(DSPTimeZoneType)]
    userLocationSignal: Annotated[DSPUserLocationSignal | str, lenient_enum(DSPUserLocationSignal)]
    videoCompletionTier: Annotated[DSPVideoCompletionTier | str, lenient_enum(DSPVideoCompletionTier)] | None = Field(
        default=None
    )


class DSPUpdateAdGroupBid(StrictModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPUpdateAdGroupBudgetSettings(StrictModel):
    budgetAllocation: Annotated[DSPBudgetAllocation | str, lenient_enum(DSPBudgetAllocation)] | None = Field(
        default=None
    )
    dailyMinSpendValue: float | None = Field(
        default=None, description="Denotes the daily minimum spend on the ad group in local currency."
    )


class DSPUpdateAdGroupRequest(StrictModel):
    adGroups: list[DSPAdGroupUpdate] = Field(min_length=1, max_length=20)


class DSPUpdateAmazonViewability(StrictModel):
    includeUnmeasurableImpressions: bool | None = Field(
        default=None,
        description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measured when a viewabilityTier other than ALL_TIERS is selected. We recommend setting to false if high viewability is your goal.",
    )
    viewabilityTier: Annotated[DSPViewabilityTier | str, lenient_enum(DSPViewabilityTier)] | None = Field(default=None)


class DSPUpdateOptimization(StrictModel):
    bidStrategy: Annotated[DSPBidStrategy | str, lenient_enum(DSPBidStrategy)] | None = Field(default=None)
    budgetSettings: DSPUpdateAdGroupBudgetSettings | None = Field(default=None)


class DSPUpdatePacing(StrictModel):
    deliveryProfile: Annotated[DSPDeliveryProfile | str, lenient_enum(DSPDeliveryProfile)] | None = Field(default=None)


class DSPUpdateTargetingSettings(StrictModel):
    amazonViewability: DSPUpdateAmazonViewability | None = Field(default=None)
    defaultAudienceTargetingMatchType: (
        Annotated[DSPDefaultAudienceTargetingMatchType | str, lenient_enum(DSPDefaultAudienceTargetingMatchType)] | None
    ) = Field(default=None)
    enableLanguageTargeting: bool | None = Field(
        default=None,
        description="If set to true, creatives will only target supply where the content language matches the creative language.",
    )
    tacticsConvertersExclusionType: (
        Annotated[DSPTacticsConvertersExclusionType | str, lenient_enum(DSPTacticsConvertersExclusionType)] | None
    ) = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed deal, the deal can be provided here.",
    )
    timeZoneType: Annotated[DSPTimeZoneType | str, lenient_enum(DSPTimeZoneType)] | None = Field(default=None)
    userLocationSignal: Annotated[DSPUserLocationSignal | str, lenient_enum(DSPUserLocationSignal)] | None = Field(
        default=None
    )
    videoCompletionTier: Annotated[DSPVideoCompletionTier | str, lenient_enum(DSPVideoCompletionTier)] | None = Field(
        default=None
    )


__all__ = [
    "DSPAdGroup",
    "DSPAdGroupAdGroupIdFilter",
    "DSPAdGroupAdProductFilter",
    "DSPAdGroupBid",
    "DSPAdGroupBudgetSettings",
    "DSPAdGroupCampaignIdFilter",
    "DSPAdGroupCreate",
    "DSPAdGroupMultiStatusResponse",
    "DSPAdGroupMultiStatusSuccess",
    "DSPAdGroupStateFilter",
    "DSPAdGroupSuccessResponse",
    "DSPAdGroupUpdate",
    "DSPAdProduct",
    "DSPAmazonViewability",
    "DSPAutomatedTargetingTactic",
    "DSPBidStrategy",
    "DSPBudget",
    "DSPBudgetAllocation",
    "DSPBudgetType",
    "DSPBudgetValue",
    "DSPCreateAdGroupBid",
    "DSPCreateAdGroupBudgetSettings",
    "DSPCreateAdGroupRequest",
    "DSPCreateAmazonViewability",
    "DSPCreateBudget",
    "DSPCreateBudgetValue",
    "DSPCreateFee",
    "DSPCreateFrequency",
    "DSPCreateMonetaryBudget",
    "DSPCreateMonetaryBudgetValue",
    "DSPCreateOptimization",
    "DSPCreatePacing",
    "DSPCreateState",
    "DSPCreateTag",
    "DSPCreateTargetingSettings",
    "DSPCreativeRotationType",
    "DSPCurrencyCode",
    "DSPDefaultAudienceTargetingMatchType",
    "DSPDeliveryProfile",
    "DSPDeliveryReason",
    "DSPDeliveryStatus",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPFee",
    "DSPFeeType",
    "DSPFeeValueType",
    "DSPFeesThirdPartyProvider",
    "DSPFrequency",
    "DSPFrequencyTargetingSetting",
    "DSPInventoryType",
    "DSPMonetaryBudget",
    "DSPMonetaryBudgetValue",
    "DSPOptimization",
    "DSPPacing",
    "DSPQueryAdGroupRequest",
    "DSPRecurrence",
    "DSPSiteLanguage",
    "DSPState",
    "DSPStatus",
    "DSPTacticsConvertersExclusionType",
    "DSPTag",
    "DSPTargetingSettings",
    "DSPTimeUnit",
    "DSPTimeZoneType",
    "DSPUpdateAdGroupBid",
    "DSPUpdateAdGroupBudgetSettings",
    "DSPUpdateAdGroupRequest",
    "DSPUpdateAmazonViewability",
    "DSPUpdateOptimization",
    "DSPUpdatePacing",
    "DSPUpdateState",
    "DSPUpdateTargetingSettings",
    "DSPUserLocationSignal",
    "DSPVideoCompletionTier",
    "DSPViewabilityTier",
]
