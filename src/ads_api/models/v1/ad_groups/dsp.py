"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPBudgetType,
    DSPCreateTag,
    DSPFeesThirdPartyProvider,
    DSPRecurrence,
    DSPTimeUnit,
)

type DSPAdProduct = Literal["AMAZON_DSP"]
"""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
"""


type DSPAutomatedTargetingTactic = Literal[
    "AWARENESS", "CUSTOMER_ACQUISITION", "MAXIMIZE_PERFORMANCE", "PROSPECTING", "REMARKETING", "RETENTION", "SEARCH"
]
"""
Supported values:
- `AWARENESS`: Ad Group tactic (Complete TV) that indicates that this line item drives awareness to your selected audience on publisher streaming TV for the linked deal while fulfilling your commitment.
- `CUSTOMER_ACQUISITION`: Ad Group Tactic (P+) that reaches shoppers who are similar to past purchasers
- `MAXIMIZE_PERFORMANCE`: Ad Group Tactic (P+) that reaches shoppers who are similar to past shoppers who viewed a product detail page
- `PROSPECTING`: Ad Group Tactic (B+) that reaches consumers who are highly likely to show interest and engage with your brand or product
- `REMARKETING`: Ad Group Tactic (P+) that reaches shoppers who have viewed a product detail page, searched for your product, or visited your homepage
- `RETENTION`: Ad Group Tactic (P+) that reaches shoppers who have purchased your product
- `SEARCH`: Ad Group Tactic that targets shoppers based on search signals.
"""


type DSPBidStrategy = Literal["PRIORITIZE_KPI_TARGET", "SPEND_BUDGET_IN_FULL", "USE_CAMPAIGN_STRATEGY"]
"""
Supported values:
- `PRIORITIZE_KPI_TARGET`: Optimizes bidding to achieve the KPI target specified.
- `SPEND_BUDGET_IN_FULL`: Prioritize spending full budget, while maximizing performance
- `USE_CAMPAIGN_STRATEGY`: Inherit the bid strategy from the parent campaign.
"""


type DSPBudgetAllocation = Literal["AUTO", "MANUAL"]
"""
Supported values:
- `AUTO`: Automatically allocate budget to better performing ad groups based on the selected goal KPI.
- `MANUAL`: Manually allocate budget across ad groups.
"""


type DSPCreateState = Literal["ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


type DSPCreativeRotationType = Literal["RANDOM", "WEIGHTED"]
"""
Supported values:
- `RANDOM`: Creatives are rotated randomly with equal weight.
- `WEIGHTED`: Creatives are rotated based on assigned weights.
"""


type DSPCurrencyCode = Literal[
    "AED",
    "ARS",
    "AUD",
    "BGN",
    "BHD",
    "BOB",
    "BRL",
    "CAD",
    "CHF",
    "CLP",
    "CNY",
    "COP",
    "CRC",
    "CZK",
    "DKK",
    "DOP",
    "DZD",
    "EUR",
    "GBP",
    "GTQ",
    "HKD",
    "HNL",
    "HRK",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "JMD",
    "JPY",
    "KRW",
    "KWD",
    "MAD",
    "MXN",
    "MYR",
    "NOK",
    "PAB",
    "PEN",
    "PHP",
    "PKR",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "SAR",
    "SEK",
    "SGD",
    "THB",
    "TND",
    "TRY",
    "TWD",
    "UAH",
    "USD",
    "UYU",
    "VND",
]
"""
Supported values:
- `AED`: United Arab Emirates Dirham
- `ARS`: Argentine Peso
- `AUD`: Australian Dollar
- `BGN`: Bulgarian Lev
- `BHD`: Bahraini Dinar
- `BOB`: Bolivian Boliviano
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `CHF`: Swiss Franc
- `CLP`: Chilean Peso
- `CNY`: Chinese Yuan
- `COP`: Colombian Peso
- `CRC`: Costa Rican Colón
- `CZK`: Czech Koruna
- `DKK`: Danish Krone
- `DOP`: Dominican Peso
- `DZD`: Algerian Dinar
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `GTQ`: Guatemalan Quetzal
- `HKD`: Hong Kong Dollar
- `HNL`: Honduran Lempira
- `HRK`: Croatian Kuna
- `HUF`: Hungarian Forint
- `IDR`: Indonesian Rupiah
- `ILS`: Israeli New Shekel
- `INR`: Indian Rupee
- `JMD`: Jamaican Dollar
- `JPY`: Japanese Yen
- `KRW`: South Korean Won
- `KWD`: Kuwaiti Dinar
- `MAD`: Moroccan Dirham
- `MXN`: Mexican Peso
- `MYR`: Malaysian Ringgit
- `NOK`: Norwegian Krone
- `PAB`: Panamanian Balboa
- `PEN`: Peruvian Sol
- `PHP`: Philippine Peso
- `PKR`: Pakistani Rupee
- `PYG`: Paraguayan Guaraní
- `QAR`: Qatari Riyal
- `RON`: Romanian Leu
- `RSD`: Serbian Dinar
- `RUB`: Russian Ruble
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `THB`: Thai Baht
- `TND`: Tunisian Dinar
- `TRY`: Turkish Lira
- `TWD`: New Taiwan Dollar
- `UAH`: Ukrainian Hryvnia
- `USD`: United States Dollar
- `UYU`: Uruguayan Peso
- `VND`: Vietnamese Đồng
"""


type DSPDefaultAudienceTargetingMatchType = Literal["EXACT", "SIMILAR"]
"""
Match type for audience targeting inclusion groups, if any. You can enhance your ad group’s reach to consumers with similar shopping, streaming, and browsing behaviors or interests as your selected audiences across all inventory sources, regardless of the presence of ad identifiers. Only applicable at the adGroup level, rather than at individual audience level. (Default: SIMILAR). Note, SIMILAR is not applicable to certain advertised product categories, [see here](https://advertising.amazon.com/help/GX8G7HNDS5RBX3EF) for more information.

Supported values:
- `EXACT`: Target the exact audiences specified in the ad group audience targeting.
- `SIMILAR`: Reach more audiences who are similar to your included audiences.
"""


type DSPDeliveryProfile = Literal["ASAP", "EVEN", "PACE_AHEAD"]
"""
Supported values:
- `ASAP`: Makes your entire budget available to spend immediately. This is ideal for ad groups with limited inventory or when there's no requirement to spend throughout the length of the campaign.Warning: Selecting ASAP may result in your entire budget being spent immediately.
- `EVEN`: Even pacing spends your budget consistently across the length of the campaign.
- `PACE_AHEAD`: Pace Ahead can deliver up to 25% more than the daily Even pace targets.
"""


type DSPDeliveryReason = Literal[
    "AD_CREATIVES_NOT_RUNNING",
    "AD_GROUPS_NOT_RUNNING",
    "AD_GROUP_ARCHIVED",
    "AD_GROUP_ENDED",
    "AD_GROUP_INELIGIBLE_GOAL_KPI",
    "AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS",
    "AD_GROUP_PAUSED",
    "AD_GROUP_PENDING_START_DATE",
    "AD_GROUP_POLICING_SUSPENDED",
    "AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS",
    "AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS",
    "AD_NOT_APPROVED_FOR_ALL_AD_GROUPS",
    "AD_NOT_ASSOCIATED_WITH_AD_GROUP",
    "AD_POLICING_PENDING_REVIEW",
    "AD_POLICING_SUSPENDED",
    "CAMPAIGN_ARCHIVED",
    "CAMPAIGN_END_DATE_REACHED",
    "CAMPAIGN_PAUSED",
    "CAMPAIGN_PENDING_START_DATE",
    "CAMPAIGN_POLICING_SUSPENDED",
    "OTHER",
]
"""
Supported values:
- `AD_GROUP_INELIGIBLE_GOAL_KPI`: Indicates that the ad group is suspended because the campaign's goal KPI is not supported.
- `AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS`: Indicates that the ad group is suspended because the campaign is missing conversion tracking selections.
- `AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS`: Indicates that the ad group is suspended because the campaign has an insufficient number of conversion tracking selections.
- `AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS`: Indicates that the ad group is suspended because the campaign exceeded the maximum number of conversion tracking selections.
"""


type DSPDeliveryStatus = Literal["DELIVERING", "LIMITED", "NOT_DELIVERING", "UNAVAILABLE"]
"""
Supported values:
- `DELIVERING`: Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
- `LIMITED`: Represents partial delivery status, applicable to global resources that have different delivery status across marketplaces
- `NOT_DELIVERING`: Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
- `UNAVAILABLE`: Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces
"""


type DSPErrorCode = Literal[
    "ACTION_NOT_SUPPORTED",
    "ACTIVE_RESOURCE_LIMIT_EXCEEDED",
    "ARCHIVED_PARENT_CANNOT_CREATE",
    "ARCHIVED_PARENT_CANNOT_EDIT",
    "ARCHIVED_RESOURCE_CANNOT_EDIT",
    "ASSET_NOT_READY",
    "AUTOCREATED_ENTITY_CANNOT_EDIT",
    "BAD_REQUEST",
    "CONFLICT",
    "CONTENT_TOO_LARGE",
    "DATE_CANNOT_BE_IN_PAST",
    "DATE_CANNOT_BE_NULL",
    "DATE_TOO_SOON",
    "DUPLICATE_FIELD_VALUE_FOUND",
    "DUPLICATE_RESOURCE_ID_FOUND",
    "DURATION_TOO_SHORT",
    "FEATURE_DISCONTINUED",
    "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT",
    "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT",
    "FIELD_SIZE_IS_OUT_OF_RANGE",
    "FIELD_VALUE_CANNOT_EDIT",
    "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS",
    "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS",
    "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT",
    "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT",
    "FIELD_VALUE_IS_EMPTY",
    "FIELD_VALUE_IS_INVALID",
    "FIELD_VALUE_IS_NULL",
    "FIELD_VALUE_IS_OUT_OF_RANGE",
    "FIELD_VALUE_MISMATCH",
    "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL",
    "FIELD_VALUE_NOT_FOUND",
    "FIELD_VALUE_NOT_UNIQUE",
    "FORBIDDEN",
    "INTERNAL_ERROR",
    "NOT_FOUND",
    "PAYMENT_ISSUE",
    "PRODUCT_INELIGIBLE",
    "RESOURCE_DOES_NOT_BELONG_TO_PARENT",
    "RESOURCE_ID_NOT_FOUND",
    "RESOURCE_IS_EMPTY",
    "RESOURCE_IS_IN_TERMINAL_STATE",
    "RESOURCE_IS_NULL",
    "TOO_MANY_REQUESTS",
    "TOTAL_RESOURCE_LIMIT_EXCEEDED",
    "UNAUTHORIZED",
    "UNSUPPORTED_MARKETPLACE",
]
"""
Supported values:
- `ACTION_NOT_SUPPORTED`: The request is not supported.
- `ACTIVE_RESOURCE_LIMIT_EXCEEDED`: Too many live resources. Remove resources and try again.
- `ARCHIVED_PARENT_CANNOT_CREATE`: New resources cannot be created within an archived parent.
- `ARCHIVED_PARENT_CANNOT_EDIT`: Resources within an archived parent cannot be edited.
- `ARCHIVED_RESOURCE_CANNOT_EDIT`: Archived resources cannot be edited.
- `ASSET_NOT_READY`: The provided asset is still being processed.
- `AUTOCREATED_ENTITY_CANNOT_EDIT`: Autocreated entities cannot be edited. To complete this action, create the resource manually.
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `CONFLICT`: Operation could not be completed due to a conflict. Please retry your request.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `DATE_CANNOT_BE_IN_PAST`: Update the date to be in the future.
- `DATE_CANNOT_BE_NULL`: Update the date.
- `DATE_TOO_SOON`: Update the date to be further in the future.
- `DUPLICATE_FIELD_VALUE_FOUND`: Multiple resources share the non-unique field values. Remove the non-unique field value.
- `DUPLICATE_RESOURCE_ID_FOUND`: Multiple resources share the same ID. Remove the duplicate ID.
- `DURATION_TOO_SHORT`: Update the length to be within the required range.
- `FEATURE_DISCONTINUED`: Feature has been discontinued.
- `FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_SIZE_IS_OUT_OF_RANGE`: Update the value to be within the required range.
- `FIELD_VALUE_CANNOT_EDIT`: Field value cannot be edited.
- `FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS`: Update the request with the required information for this resource.
- `FIELD_VALUE_CONTAINS_INVALID_CHARACTERS`: Remove the invalid characters and try again.
- `FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_VALUE_IS_EMPTY`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_INVALID`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_NULL`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_OUT_OF_RANGE`: Update the value to be within the required range.
- `FIELD_VALUE_MISMATCH`: Mismatch among resource field values.
- `FIELD_VALUE_MUST_BE_EMPTY_OR_NULL`: Update the request with the required information for this resource.
- `FIELD_VALUE_NOT_FOUND`: Resource specified in the field value not found. Try again with valid value.
- `FIELD_VALUE_NOT_UNIQUE`: Resource field value conflicts with existing resource. Try again with an unique field value.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `PAYMENT_ISSUE`: Payment failed.
- `PRODUCT_INELIGIBLE`: Product is not eligible for advertising. Try again with a valid product.
- `RESOURCE_DOES_NOT_BELONG_TO_PARENT`: Resource does not belong to the specified parent. Try again with a valid parent ID.
- `RESOURCE_ID_NOT_FOUND`: Resource ID not found. Try again with valid ID.
- `RESOURCE_IS_EMPTY`: Update the request with the required information for this resource.
- `RESOURCE_IS_IN_TERMINAL_STATE`: Resource is in terminal state.
- `RESOURCE_IS_NULL`: Update the request with the required information for this resource.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `TOTAL_RESOURCE_LIMIT_EXCEEDED`: Too many resources. Remove resources and try again.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
- `UNSUPPORTED_MARKETPLACE`: Marketplace not supported. Try again with a supported marketplace.
"""


type DSPFeeType = Literal[
    "AMAZON_AUDIENCE",
    "AMAZON_DSP",
    "MANAGED_SERVICE_FEE",
    "OMNICHANNEL_METRICS",
    "THIRD_PARTY_APPLIED",
    "THIRD_PARTY_AUDIENCE",
    "THIRD_PARTY_TARGETING",
]
"""
Supported values:
- `AMAZON_AUDIENCE`: CPM fee for using Amazon audiences.
- `AMAZON_DSP`: A service fee for using Amazon DSP and subtracted from the budget. This fee is applied as a percent of supply cost.
- `MANAGED_SERVICE_FEE`: The percentage-based fee applied to the Supply Cost for Amazon programmatic managed service.
- `OMNICHANNEL_METRICS`: Fee for using Amazon Omnichannel Metrics.
- `THIRD_PARTY_APPLIED`: User added CPM fee for using third-party data to track CPM costs. This fee is applied as a percent of supply cost.
- `THIRD_PARTY_AUDIENCE`: CPM fee for using a third party audience.
- `THIRD_PARTY_TARGETING`: CPM fee for using targeting provided by a third-party data provider.
"""


type DSPFeeValueType = Literal["FIXED_CPM", "PERCENTAGE_OF_BUDGET", "PERCENTAGE_OF_SUPPLY_COST"]
"""
Supported values:
- `FIXED_CPM`: Charged based on a fixed CPM. The currency depends on the feeType.
- `PERCENTAGE_OF_BUDGET`: Subtracted from the campaign budget as a percent of budget
- `PERCENTAGE_OF_SUPPLY_COST`: Charged as a percent of supply (media) cost. Ranges from 0 to 1 where 0.15 represents 15%.
"""


type DSPFrequencyTargetingSetting = Literal["HOUSEHOLD", "USER"]
"""
Supported values:
- `HOUSEHOLD`: Control frequency an ad will be selected across people within the same household.
- `USER`: Control frequency an ad will be selected to a person.
"""


type DSPInventoryType = Literal[
    "AAP_MOBILE_APP",
    "AMAZON_MOBILE_DISPLAY",
    "AUDIO",
    "AUDIO_AMAZON_DEAL",
    "DISPLAY",
    "LIVE_EVENTS",
    "ONLINE_VIDEO",
    "PODCAST",
    "STANDARD_DISPLAY",
    "STREAMING_TV",
    "STREAMING_TV_AMAZON_DEAL",
    "VIDEO",
]
"""
Supported values:
- `AUDIO`: Audio ads that serve on streaming audio inventory.
- `LIVE_EVENTS`: Real-time broadcast inventory (sports, concerts, award shows) with audience volatility and concentrated traffic patterns requiring specialized pacing algorithms and event-specific metadata handling.
- `PODCAST`: Podcast ads that serve on streaming podcast inventory.
"""


type DSPSiteLanguage = Literal[
    "AR",
    "BN",
    "CS",
    "DA",
    "DE",
    "EN",
    "ES",
    "FI",
    "FR",
    "GU",
    "HI",
    "IT",
    "JA",
    "KN",
    "ML",
    "MR",
    "NL",
    "NO",
    "OTHER",
    "PA",
    "PL",
    "PT",
    "SV",
    "TA",
    "TE",
    "TR",
    "ZH",
]
"""
Supported values:
- `AR`: Arabic.
- `BN`: Bengali.
- `CS`: Czech.
- `DA`: Danish.
- `DE`: German.
- `EN`: English.
- `ES`: Spanish.
- `FI`: Finnish.
- `FR`: French.
- `GU`: Gujarati.
- `HI`: Hindi.
- `IT`: Italian.
- `JA`: Japanese.
- `KN`: Kannada.
- `ML`: Malayalam.
- `MR`: Marathi.
- `NL`: Dutch.
- `NO`: Norwegian.
- `OTHER`: Other language.
- `PA`: Punjabi.
- `PL`: Polish.
- `PT`: Portuguese.
- `SV`: Swedish.
- `TA`: Tamil.
- `TE`: Telugu.
- `TR`: Turkish.
- `ZH`: Chinese.
"""


type DSPState = Literal["ARCHIVED", "ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


type DSPTacticsConvertersExclusionType = Literal["NO_EXCLUSION", "RECENT_CONVERTERS"]
"""
Supported values:
- `NO_EXCLUSION`: Do not exclude any converters from targeting.
- `RECENT_CONVERTERS`: Exclude recent converters from targeting to focus on new customers.
"""


type DSPTimeZoneType = Literal["ADVERTISER_REGION", "VIEWER"]
"""
Supported values:
- `ADVERTISER_REGION`: Use the advertiser's regional time zone for daypart targeting.
- `VIEWER`: Use the viewer's local time zone for daypart targeting.
"""


type DSPUpdateState = Literal["ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


type DSPUserLocationSignal = Literal["CURRENT", "MULTIPLE_SIGNALS"]
"""
Supported values:
- `CURRENT`: Target users based on their current geographic location.
- `MULTIPLE_SIGNALS`: Target users based on multiple location signals.
"""


type DSPVideoCompletionTier = Literal[
    "ALL_TIERS",
    "GREATER_THAN_10_PERCENT",
    "GREATER_THAN_20_PERCENT",
    "GREATER_THAN_30_PERCENT",
    "GREATER_THAN_40_PERCENT",
    "GREATER_THAN_50_PERCENT",
    "GREATER_THAN_60_PERCENT",
    "GREATER_THAN_70_PERCENT",
    "GREATER_THAN_80_PERCENT",
    "GREATER_THAN_90_PERCENT",
]
"""
Supported values:
- `ALL_TIERS`: Target all video completion tiers.
- `GREATER_THAN_10_PERCENT`: Target videos with greater than 10% predicted completion rate.
- `GREATER_THAN_20_PERCENT`: Target videos with greater than 20% predicted completion rate.
- `GREATER_THAN_30_PERCENT`: Target videos with greater than 30% predicted completion rate.
- `GREATER_THAN_40_PERCENT`: Target videos with greater than 40% predicted completion rate.
- `GREATER_THAN_50_PERCENT`: Target videos with greater than 50% predicted completion rate.
- `GREATER_THAN_60_PERCENT`: Target videos with greater than 60% predicted completion rate.
- `GREATER_THAN_70_PERCENT`: Target videos with greater than 70% predicted completion rate.
- `GREATER_THAN_80_PERCENT`: Target videos with greater than 80% predicted completion rate.
- `GREATER_THAN_90_PERCENT`: Target videos with greater than 90% predicted completion rate.
"""


type DSPViewabilityTier = Literal[
    "ALL_TIERS",
    "GREATER_THAN_40_PERCENT",
    "GREATER_THAN_50_PERCENT",
    "GREATER_THAN_60_PERCENT",
    "GREATER_THAN_70_PERCENT",
    "LESS_THAN_40_PERCENT",
]
"""
Supported values:
- `ALL_TIERS`: Target all viewability tiers with no filtering.
- `GREATER_THAN_40_PERCENT`: Target impressions with greater than 40% predicted viewability.
- `GREATER_THAN_50_PERCENT`: Target impressions with greater than 50% predicted viewability.
- `GREATER_THAN_60_PERCENT`: Target impressions with greater than 60% predicted viewability.
- `GREATER_THAN_70_PERCENT`: Target impressions with greater than 70% predicted viewability.
- `LESS_THAN_40_PERCENT`: Target impressions with less than 40% predicted viewability.
"""


class DSPAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: DSPAdProduct | str
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
    creativeRotationType: DSPCreativeRotationType | str
    endDateTime: datetime = Field(description="The end date time for the ad group.")
    fees: list[DSPFee] | None = Field(
        default=None, min_length=0, max_length=7, description="The fees associated with the ad group."
    )
    frequencies: list[DSPFrequency] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing frequency details for the ad group."
    )
    inventoryType: DSPInventoryType | str
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad group was last updated.")
    name: str = Field(description="The name of the ad group.")
    optimization: DSPOptimization
    pacing: DSPPacing
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the ad group."
    )
    startDateTime: datetime = Field(description="The start date time for the ad group.")
    state: DSPState | str
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
    include: list[DSPAdProduct | str] = Field(min_length=1, max_length=1)


class DSPAdGroupBid(LenientModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    currencyCode: DSPCurrencyCode | str
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPAdGroupBudgetSettings(LenientModel):
    budgetAllocation: DSPBudgetAllocation | str | None = Field(default=None)
    dailyMinSpendValue: float | None = Field(
        default=None, description="Denotes the daily minimum spend on the ad group in local currency."
    )


class DSPAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPAdGroupCreate(StrictModel):
    adProduct: DSPAdProduct
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
    creativeRotationType: DSPCreativeRotationType
    endDateTime: datetime = Field(description="The end date time for the ad group.")
    fees: list[DSPCreateFee] | None = Field(
        default=None, min_length=0, max_length=7, description="The fees associated with the ad group."
    )
    frequencies: list[DSPCreateFrequency] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing frequency details for the ad group."
    )
    inventoryType: DSPInventoryType
    name: str = Field(description="The name of the ad group.")
    optimization: DSPCreateOptimization
    pacing: DSPCreatePacing
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the ad group."
    )
    startDateTime: datetime = Field(description="The start date time for the ad group.")
    state: DSPCreateState
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
    include: list[DSPState | str] = Field(min_length=1, max_length=3)


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
    creativeRotationType: DSPCreativeRotationType | None = Field(default=None)
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
    state: DSPUpdateState | None = Field(default=None)
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
    viewabilityTier: DSPViewabilityTier | str


class DSPBudget(LenientModel):
    budgetType: DSPBudgetType | str
    budgetValue: DSPBudgetValue
    recurrenceTimePeriod: DSPRecurrence | str


class DSPBudgetValue(LenientModel):
    monetaryBudgetValue: DSPMonetaryBudgetValue


class DSPCreateAdGroupBid(StrictModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPCreateAdGroupBudgetSettings(StrictModel):
    budgetAllocation: DSPBudgetAllocation | None = Field(default=None)
    dailyMinSpendValue: float | None = Field(
        default=None, description="Denotes the daily minimum spend on the ad group in local currency."
    )


class DSPCreateAdGroupRequest(StrictModel):
    adGroups: list[DSPAdGroupCreate] = Field(min_length=1, max_length=20)


class DSPCreateAmazonViewability(StrictModel):
    includeUnmeasurableImpressions: bool = Field(
        description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measured when a viewabilityTier other than ALL_TIERS is selected. We recommend setting to false if high viewability is your goal."
    )
    viewabilityTier: DSPViewabilityTier


class DSPCreateBudget(StrictModel):
    budgetType: DSPBudgetType
    budgetValue: DSPCreateBudgetValue
    recurrenceTimePeriod: DSPRecurrence


class DSPCreateBudgetValue(StrictModel):
    monetaryBudgetValue: DSPCreateMonetaryBudgetValue


class DSPCreateFee(StrictModel):
    addToBudgetSpentAmount: bool = Field(
        description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad group budget spent amount in reports."
    )
    feeType: DSPFeeType
    feeValue: float = Field(
        description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the marketplace. All other CPM based fees are in the currency of the advertiser. For percentages, 100 represents 100%."
    )
    thirdPartyProvider: DSPFeesThirdPartyProvider


class DSPCreateFrequency(StrictModel):
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    frequencyTargetingSetting: DSPFrequencyTargetingSetting
    timeCount: int = Field(
        ge=1, le=60, description="The value associated with the time and unit of time for this frequency cap."
    )
    timeUnit: DSPTimeUnit


class DSPCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPCreateMonetaryBudgetValue(StrictModel):
    monetaryBudget: DSPCreateMonetaryBudget | None = Field(default=None)


class DSPCreateOptimization(StrictModel):
    bidStrategy: DSPBidStrategy
    budgetSettings: DSPCreateAdGroupBudgetSettings | None = Field(default=None)


class DSPCreatePacing(StrictModel):
    deliveryProfile: DSPDeliveryProfile


class DSPCreateTargetingSettings(StrictModel):
    amazonViewability: DSPCreateAmazonViewability
    automatedTargetingTactic: DSPAutomatedTargetingTactic | None = Field(default=None)
    defaultAudienceTargetingMatchType: DSPDefaultAudienceTargetingMatchType | None = Field(default=None)
    enableLanguageTargeting: bool | None = Field(
        default=None,
        description="If set to true, creatives will only target supply where the content language matches the creative language.",
    )
    tacticsConvertersExclusionType: DSPTacticsConvertersExclusionType | None = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed deal, the deal can be provided here.",
    )
    timeZoneType: DSPTimeZoneType
    userLocationSignal: DSPUserLocationSignal
    videoCompletionTier: DSPVideoCompletionTier | None = Field(default=None)


class DSPError(LenientModel):
    code: DSPErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=4999)


class DSPFee(LenientModel):
    addToBudgetSpentAmount: bool = Field(
        description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad group budget spent amount in reports."
    )
    currencyCode: DSPCurrencyCode | str | None = Field(default=None)
    feeType: DSPFeeType | str
    feeValue: float = Field(
        description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the marketplace. All other CPM based fees are in the currency of the advertiser. For percentages, 100 represents 100%."
    )
    feeValueType: DSPFeeValueType | str
    thirdPartyProvider: DSPFeesThirdPartyProvider | str


class DSPFrequency(LenientModel):
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    frequencyTargetingSetting: DSPFrequencyTargetingSetting | str
    timeCount: int = Field(
        ge=1, le=60, description="The value associated with the time and unit of time for this frequency cap."
    )
    timeUnit: DSPTimeUnit | str


class DSPMonetaryBudget(LenientModel):
    currencyCode: DSPCurrencyCode | str
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPMonetaryBudgetValue(LenientModel):
    monetaryBudget: DSPMonetaryBudget | None = Field(default=None)


class DSPOptimization(LenientModel):
    bidStrategy: DSPBidStrategy | str
    budgetSettings: DSPAdGroupBudgetSettings | None = Field(default=None)


class DSPPacing(LenientModel):
    deliveryProfile: DSPDeliveryProfile | str


class DSPQueryAdGroupRequest(StrictModel):
    adGroupIdFilter: DSPAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: DSPAdGroupAdProductFilter
    campaignIdFilter: DSPAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    stateFilter: DSPAdGroupStateFilter | None = Field(default=None)


class DSPStatus(LenientModel):
    deliveryReasons: list[DSPDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: DSPDeliveryStatus | str


class DSPTag(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPTargetingSettings(LenientModel):
    amazonViewability: DSPAmazonViewability
    automatedTargetingTactic: DSPAutomatedTargetingTactic | str | None = Field(default=None)
    defaultAudienceTargetingMatchType: DSPDefaultAudienceTargetingMatchType | str | None = Field(default=None)
    enableLanguageTargeting: bool | None = Field(
        default=None,
        description="If set to true, creatives will only target supply where the content language matches the creative language.",
    )
    siteLanguage: DSPSiteLanguage | str | None = Field(default=None)
    tacticsConvertersExclusionType: DSPTacticsConvertersExclusionType | str | None = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed deal, the deal can be provided here.",
    )
    timeZoneType: DSPTimeZoneType | str
    userLocationSignal: DSPUserLocationSignal | str
    videoCompletionTier: DSPVideoCompletionTier | str | None = Field(default=None)


class DSPUpdateAdGroupBid(StrictModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPUpdateAdGroupBudgetSettings(StrictModel):
    budgetAllocation: DSPBudgetAllocation | None = Field(default=None)
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
    viewabilityTier: DSPViewabilityTier | None = Field(default=None)


class DSPUpdateOptimization(StrictModel):
    bidStrategy: DSPBidStrategy | None = Field(default=None)
    budgetSettings: DSPUpdateAdGroupBudgetSettings | None = Field(default=None)


class DSPUpdatePacing(StrictModel):
    deliveryProfile: DSPDeliveryProfile | None = Field(default=None)


class DSPUpdateTargetingSettings(StrictModel):
    amazonViewability: DSPUpdateAmazonViewability | None = Field(default=None)
    defaultAudienceTargetingMatchType: DSPDefaultAudienceTargetingMatchType | None = Field(default=None)
    enableLanguageTargeting: bool | None = Field(
        default=None,
        description="If set to true, creatives will only target supply where the content language matches the creative language.",
    )
    tacticsConvertersExclusionType: DSPTacticsConvertersExclusionType | None = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed deal, the deal can be provided here.",
    )
    timeZoneType: DSPTimeZoneType | None = Field(default=None)
    userLocationSignal: DSPUserLocationSignal | None = Field(default=None)
    videoCompletionTier: DSPVideoCompletionTier | None = Field(default=None)


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
