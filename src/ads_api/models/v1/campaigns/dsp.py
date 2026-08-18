"""Auto-generated models for Campaigns from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPBudgetType,
    DSPCreateTag,
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


type DSPCampaignFeeType = Literal["AGENCY"]
"""
Supported values:
- `AGENCY`: A service fee that is subtracted from the campaign budget as a percent of budget.
"""


type DSPCampaignFeeValueType = Literal["PERCENTAGE_OF_BUDGET"]
"""
Supported values:
- `PERCENTAGE_OF_BUDGET`: Subtracted from the campaign budget as a percent of budget
"""


type DSPCountryCode = Literal[
    "AE",
    "AR",
    "AT",
    "AU",
    "BE",
    "BG",
    "BH",
    "BR",
    "CA",
    "CH",
    "CL",
    "CO",
    "CR",
    "CY",
    "CZ",
    "DE",
    "DK",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "ES",
    "FI",
    "FR",
    "GB",
    "GR",
    "GT",
    "HK",
    "HN",
    "HR",
    "HU",
    "ID",
    "IE",
    "IL",
    "IN",
    "IT",
    "JM",
    "JO",
    "JP",
    "KW",
    "LT",
    "LU",
    "LV",
    "MA",
    "MX",
    "MY",
    "NL",
    "NO",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PH",
    "PK",
    "PL",
    "PR",
    "PT",
    "PY",
    "QA",
    "RO",
    "SA",
    "SE",
    "SG",
    "SK",
    "SV",
    "TH",
    "TN",
    "TR",
    "TW",
    "US",
    "UY",
    "VN",
    "ZA",
]


type DSPCreateState = Literal["ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
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


type DSPFrequencyTargetingSetting = Literal["HOUSEHOLD", "USER"]
"""
Supported values:
- `HOUSEHOLD`: Control frequency an ad will be selected across people within the same household.
- `USER`: Control frequency an ad will be selected to a person.
"""


type DSPGoal = Literal["AWARENESS", "CONSIDERATION", "CONVERSIONS"]
"""
Supported values:
- `AWARENESS`: Indicates a goal of driving awareness.
- `CONSIDERATION`: Indicates a goal of driving consideration.
- `CONVERSIONS`: Indicates a goal of driving conversions.
"""


type DSPIneligibleAutomatedTargetingTacticReasonCode = Literal[
    "CONVERSION_SELECTIONS_EMPTY",
    "CONVERSION_SELECTIONS_EXCEEDED",
    "CONVERSION_SELECTIONS_MINIMUM_NOT_MET",
    "NOT_ELIGIBLE_ADVERTISER",
    "NOT_ELIGIBLE_GOAL",
    "NOT_ELIGIBLE_INVENTORY_TYPE",
    "UNSUPPORTED_COUNTRY",
]
"""
Reason codes for why a tactic type is ineligible

Supported values:
- `CONVERSION_SELECTIONS_EMPTY`: Campaign has no product or conversion event associations.
- `CONVERSION_SELECTIONS_EXCEEDED`: Campaign is associated with too many products or conversion events.
- `CONVERSION_SELECTIONS_MINIMUM_NOT_MET`: Minimum product or conversion event constraints not met.
- `NOT_ELIGIBLE_ADVERTISER`: The advertiser is not eligible for this tactic.
- `NOT_ELIGIBLE_GOAL`: The current campaign goal is not compatible with this tactic type.
- `NOT_ELIGIBLE_INVENTORY_TYPE`: This campaign's primary inventory types are not supported with this tactic type.
- `UNSUPPORTED_COUNTRY`: Selected tactic type is not available for the given country.
"""


type DSPKPI = Literal[
    "CLICK_THROUGH_RATE",
    "COMBINED_RETURN_ON_AD_SPEND",
    "COST_PER_ACTION",
    "COST_PER_CLICK",
    "COST_PER_CONVERSION_OFF_AMAZON",
    "COST_PER_DETAIL_PAGE_VIEW",
    "COST_PER_FIRST_APP_OPEN",
    "COST_PER_INSTALL",
    "COST_PER_SIGN_UP",
    "COST_PER_VIDEO_COMPLETION",
    "DETAIL_PAGE_VIEW_RATE",
    "FREQUENCY_AVERAGE",
    "REACH",
    "RETURN_ON_AD_SPEND",
    "ROAS",
    "ROAS_COMBINED",
    "ROAS_PROMOTED",
    "TOTAL_RETURN_ON_AD_SPEND",
    "VIDEO_COMPLETION_RATE",
]
"""
Supported values:
- `CLICK_THROUGH_RATE`: Indicates a goal of driving clickthrough rate.
- `COMBINED_RETURN_ON_AD_SPEND`: Deprecated. Please use ROAS_COMBINED.
- `COST_PER_ACTION`: Deprecated. Please use COST_PER_CONVERSION_OFF_AMAZON.
- `COST_PER_CLICK`: Indicates a goal of driving improved cost per click.
- `COST_PER_CONVERSION_OFF_AMAZON`: Indicates a goal of driving improved cost per conversion off Amazon.
- `COST_PER_DETAIL_PAGE_VIEW`: Indicates a goal of driving improved cost per detail page view.
- `COST_PER_FIRST_APP_OPEN`: Indicates a goal of improved cost per first app open.
- `COST_PER_INSTALL`: Indicates a goal of driving improved cost per app install.
- `COST_PER_SIGN_UP`: Indicates a goal of driving improved cost per sign up.
- `COST_PER_VIDEO_COMPLETION`: Indicates a goal of driving improved cost per video completion.
- `DETAIL_PAGE_VIEW_RATE`: Indicates a goal of driving improved detail page view rate.
- `FREQUENCY_AVERAGE`: Indicates a goal of driving to a target frequency.
- `REACH`: Indicates a goal of driving improved reach.
- `RETURN_ON_AD_SPEND`: Deprecated. Please use ROAS_PROMOTED.
- `ROAS_COMBINED`: Indicates a goal of driving improved return of ad spend (combined).
- `ROAS_PROMOTED`: Indicates a goal of driving improved return of ad spend (promoted).
- `ROAS`: Indicates a goal of driving improved return of ad spend.
- `TOTAL_RETURN_ON_AD_SPEND`: Deprecated. Please use ROAS.
- `VIDEO_COMPLETION_RATE`: Indicates a goal of driving improved video completion rate.
"""


type DSPMarketplace = Literal[
    "AE", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IN", "IT", "JP", "MX", "NL", "SA", "SE", "TR", "US"
]
"""
A list of country codes representing Amazon marketplaces
"""


type DSPPrimaryInventoryType = Literal["AUDIO", "DISPLAY", "VIDEO_OLV", "VIDEO_STV"]
"""
Supported values:
- `AUDIO`: Audio ads that serve on streaming audio and podcast inventory.
- `DISPLAY`: Image ads that serve across Amazon and third-party inventory.
- `VIDEO_OLV`: Video ads that serve on online video inventory.
- `VIDEO_STV`: Video ads that serve on streaming TV inventory.
"""


type DSPRolloverStrategy = Literal["CUMULATIVE_BUDGET_ROLLOVER", "NO_ROLLOVER", "PRIOR_BUDGET_ROLLOVER"]
"""
Supported values:
- `CUMULATIVE_BUDGET_ROLLOVER`: Rollover cumulative unused budget.
- `NO_ROLLOVER`: Do not rollover flight budgets.
- `PRIOR_BUDGET_ROLLOVER`: Rollover prior flight unused budget.
"""


type DSPState = Literal["ARCHIVED", "ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


type DSPUpdateState = Literal["ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


class DSPAutoCreationSettings(LenientModel):
    autoManageCampaign: bool | None = Field(
        default=None, description="Flag that allows Amazon to manage the lifecycle of your Campaign."
    )


class DSPBidSettings(LenientModel):
    bidStrategy: DSPBidStrategy | str


class DSPBudget(LenientModel):
    budgetType: DSPBudgetType | str
    budgetValue: DSPBudgetValue
    recurrenceTimePeriod: DSPRecurrence | str


class DSPBudgetSettings(LenientModel):
    budgetAllocation: DSPBudgetAllocation | str | None = Field(default=None)
    flightBudgetRolloverStrategy: DSPRolloverStrategy | str | None = Field(default=None)


class DSPBudgetValue(LenientModel):
    monetaryBudgetValue: DSPMonetaryBudgetValue


class DSPCampaign(LenientModel):
    adProduct: DSPAdProduct | str
    adomains: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case of rotating creatives. Exchanges can mandate that only one domain is allowed.",
    )
    autoCreationSettings: DSPAutoCreationSettings | None = Field(default=None)
    budgets: list[DSPBudget] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    countries: list[DSPCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime = Field(description="The date time that the campaign was created.")
    eligibleAutomatedTargetingTactics: list[DSPTacticKey] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are eligible for use with this campaign",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    fees: list[DSPCampaignFee] | None = Field(
        default=None, min_length=0, max_length=1, description="Any fees associated with the campaign."
    )
    flights: list[DSPCampaignFlight] = Field(
        min_length=1, max_length=150, description="Flight details associated with the campaign."
    )
    frequencies: list[DSPFrequency] | None = Field(
        default=None, min_length=0, max_length=3, description="Any frequency caps associated with the campaign."
    )
    ineligibleAutomatedTargetingTactics: list[DSPIneligibleAutomatedTargetingTactic] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are ineligible for use with this campaign, along with reasons for ineligibility",
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the campaign was last updated.")
    marketplaces: list[DSPMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: DSPCampaignOptimizations
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the campaign."
    )
    skanAppId: str | None = Field(
        default=None,
        description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.",
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: DSPState | str
    status: DSPStatus | None = Field(default=None)
    tags: list[DSPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetsAmazonDeal: bool | None = Field(
        default=None,
        description="If the campaign is targeting an Amazon deal, the value will be true, and the campaign and ad group(s) will be read-only.",
    )


class DSPCampaignAdProductFilter(StrictModel):
    include: list[DSPAdProduct | str] = Field(min_length=1, max_length=1)


class DSPCampaignCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class DSPCampaignCreate(StrictModel):
    adProduct: DSPAdProduct
    adomains: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case of rotating creatives. Exchanges can mandate that only one domain is allowed.",
    )
    autoCreationSettings: DSPCreateAutoCreationSettings | None = Field(default=None)
    budgets: list[DSPCreateBudget] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    countries: list[DSPCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    fees: list[DSPCreateCampaignFee] | None = Field(
        default=None, min_length=0, max_length=1, description="Any fees associated with the campaign."
    )
    flights: list[DSPCreateCampaignFlight] = Field(
        min_length=1, max_length=150, description="Flight details associated with the campaign."
    )
    frequencies: list[DSPCreateFrequency] | None = Field(
        default=None, min_length=0, max_length=3, description="Any frequency caps associated with the campaign."
    )
    marketplaces: list[DSPMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: DSPCreateCampaignOptimizations
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the campaign."
    )
    skanAppId: str | None = Field(
        default=None,
        description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.",
    )
    state: DSPCreateState
    tags: list[DSPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class DSPCampaignFee(LenientModel):
    feeType: DSPCampaignFeeType | str
    feeValue: float = Field(
        description="A service fee that is subtracted from the campaign budget as a percent of budget. This setting can’t be changed after an ad group has been added to a campaign."
    )
    feeValueType: DSPCampaignFeeValueType | str


class DSPCampaignFlight(LenientModel):
    budget: DSPFlightBudget
    endDateTime: datetime = Field(description="The end date of the flight.")
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    name: str | None = Field(default=None, description="The name of the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPCampaignMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=5)
    success: list[DSPCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=5)


class DSPCampaignMultiStatusSuccess(LenientModel):
    campaign: DSPCampaign
    index: int = Field(ge=0, le=4)


class DSPCampaignOptimizations(LenientModel):
    bidSettings: DSPBidSettings
    budgetSettings: DSPBudgetSettings | None = Field(default=None)
    goalSettings: DSPGoalSettings | None = Field(default=None)
    primaryInventoryTypes: list[DSPPrimaryInventoryType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.",
    )


class DSPCampaignStateFilter(StrictModel):
    include: list[DSPState | str] = Field(min_length=1, max_length=3)


class DSPCampaignSuccessResponse(LenientModel):
    campaigns: list[DSPCampaign] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class DSPCampaignUpdate(StrictModel):
    adomains: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case of rotating creatives. Exchanges can mandate that only one domain is allowed.",
    )
    budgets: list[DSPCreateBudget] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    fees: list[DSPCreateCampaignFee] | None = Field(
        default=None, min_length=0, max_length=1, description="Any fees associated with the campaign."
    )
    flights: list[DSPCreateCampaignFlight] | None = Field(
        default=None, min_length=1, max_length=150, description="Flight details associated with the campaign."
    )
    frequencies: list[DSPCreateFrequency] | None = Field(
        default=None, min_length=0, max_length=3, description="Any frequency caps associated with the campaign."
    )
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: DSPUpdateCampaignOptimizations | None = Field(default=None)
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the campaign."
    )
    skanAppId: str | None = Field(
        default=None,
        description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.",
    )
    state: DSPUpdateState | None = Field(default=None)
    tags: list[DSPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class DSPCreateAutoCreationSettings(StrictModel):
    autoManageCampaign: bool | None = Field(
        default=None, description="Flag that allows Amazon to manage the lifecycle of your Campaign."
    )


class DSPCreateBidSettings(StrictModel):
    bidStrategy: DSPBidStrategy


class DSPCreateBudget(StrictModel):
    budgetType: DSPBudgetType
    budgetValue: DSPCreateBudgetValue
    recurrenceTimePeriod: DSPRecurrence


class DSPCreateBudgetSettings(StrictModel):
    budgetAllocation: DSPBudgetAllocation | None = Field(default=None)
    flightBudgetRolloverStrategy: DSPRolloverStrategy | None = Field(default=None)


class DSPCreateBudgetValue(StrictModel):
    monetaryBudgetValue: DSPCreateMonetaryBudgetValue


class DSPCreateCampaignFee(StrictModel):
    feeType: DSPCampaignFeeType
    feeValue: float = Field(
        description="A service fee that is subtracted from the campaign budget as a percent of budget. This setting can’t be changed after an ad group has been added to a campaign."
    )
    feeValueType: DSPCampaignFeeValueType


class DSPCreateCampaignFlight(StrictModel):
    budget: DSPCreateFlightBudget
    endDateTime: datetime = Field(description="The end date of the flight.")
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    name: str | None = Field(default=None, description="The name of the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPCreateCampaignOptimizations(StrictModel):
    bidSettings: DSPCreateBidSettings
    budgetSettings: DSPCreateBudgetSettings | None = Field(default=None)
    goalSettings: DSPCreateGoalSettings | None = Field(default=None)
    primaryInventoryTypes: list[DSPPrimaryInventoryType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.",
    )


class DSPCreateCampaignRequest(StrictModel):
    campaigns: list[DSPCampaignCreate] = Field(min_length=1, max_length=5)


class DSPCreateFlightBudget(StrictModel):
    budgetType: DSPBudgetType
    budgetValue: DSPCreateBudgetValue


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


class DSPCreateGoalSettings(StrictModel):
    kpi: DSPKPI
    kpiValue: float | None = Field(
        default=None, description="The value of the KPI that the campaign is working to optimize."
    )


class DSPCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPCreateMonetaryBudgetValue(StrictModel):
    monetaryBudget: DSPCreateMonetaryBudget | None = Field(default=None)


class DSPError(LenientModel):
    code: DSPErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=4999)


class DSPFlightBudget(LenientModel):
    budgetType: DSPBudgetType | str
    budgetValue: DSPBudgetValue


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


class DSPGoalSettings(LenientModel):
    currencyCode: DSPCurrencyCode | str | None = Field(default=None)
    goal: DSPGoal | str
    kpi: DSPKPI | str
    kpiValue: float | None = Field(
        default=None, description="The value of the KPI that the campaign is working to optimize."
    )


class DSPIneligibleAutomatedTargetingTactic(LenientModel):
    """Information about an ineligible tactic key and the reasons for ineligibility"""

    reasons: list[DSPIneligibleAutomatedTargetingTacticReason] | None = Field(
        default=None, min_length=0, max_length=10, description="List of reasons why this tactic key is ineligible"
    )
    tacticKey: DSPTacticKey


class DSPIneligibleAutomatedTargetingTacticReason(LenientModel):
    """A single reason for tactic type ineligibility"""

    reasonCode: DSPIneligibleAutomatedTargetingTacticReasonCode | str
    reasonMessage: str = Field(description="Human readable explanation of why this tactic type is ineligible")


class DSPMonetaryBudget(LenientModel):
    currencyCode: DSPCurrencyCode | str
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPMonetaryBudgetValue(LenientModel):
    monetaryBudget: DSPMonetaryBudget | None = Field(default=None)


class DSPQueryCampaignRequest(StrictModel):
    adProductFilter: DSPCampaignAdProductFilter
    campaignIdFilter: DSPCampaignCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    stateFilter: DSPCampaignStateFilter | None = Field(default=None)


class DSPStatus(LenientModel):
    deliveryReasons: list[DSPDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: DSPDeliveryStatus | str


class DSPTacticKey(LenientModel):
    """A tactic type paired with its compatible inventory type"""

    primaryInventoryType: DSPPrimaryInventoryType | str
    tacticType: DSPAutomatedTargetingTactic | str


class DSPTag(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPUpdateBidSettings(StrictModel):
    bidStrategy: DSPBidStrategy | None = Field(default=None)


class DSPUpdateBudgetSettings(StrictModel):
    budgetAllocation: DSPBudgetAllocation | None = Field(default=None)
    flightBudgetRolloverStrategy: DSPRolloverStrategy | None = Field(default=None)


class DSPUpdateCampaignOptimizations(StrictModel):
    bidSettings: DSPUpdateBidSettings | None = Field(default=None)
    budgetSettings: DSPUpdateBudgetSettings | None = Field(default=None)
    goalSettings: DSPUpdateGoalSettings | None = Field(default=None)
    primaryInventoryTypes: list[DSPPrimaryInventoryType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.",
    )


class DSPUpdateCampaignRequest(StrictModel):
    campaigns: list[DSPCampaignUpdate] = Field(min_length=1, max_length=5)


class DSPUpdateGoalSettings(StrictModel):
    kpi: DSPKPI | None = Field(default=None)
    kpiValue: float | None = Field(
        default=None, description="The value of the KPI that the campaign is working to optimize."
    )


__all__ = [
    "DSPAdProduct",
    "DSPAutoCreationSettings",
    "DSPAutomatedTargetingTactic",
    "DSPBidSettings",
    "DSPBidStrategy",
    "DSPBudget",
    "DSPBudgetAllocation",
    "DSPBudgetSettings",
    "DSPBudgetType",
    "DSPBudgetValue",
    "DSPCampaign",
    "DSPCampaignAdProductFilter",
    "DSPCampaignCampaignIdFilter",
    "DSPCampaignCreate",
    "DSPCampaignFee",
    "DSPCampaignFeeType",
    "DSPCampaignFeeValueType",
    "DSPCampaignFlight",
    "DSPCampaignMultiStatusResponse",
    "DSPCampaignMultiStatusSuccess",
    "DSPCampaignOptimizations",
    "DSPCampaignStateFilter",
    "DSPCampaignSuccessResponse",
    "DSPCampaignUpdate",
    "DSPCountryCode",
    "DSPCreateAutoCreationSettings",
    "DSPCreateBidSettings",
    "DSPCreateBudget",
    "DSPCreateBudgetSettings",
    "DSPCreateBudgetValue",
    "DSPCreateCampaignFee",
    "DSPCreateCampaignFlight",
    "DSPCreateCampaignOptimizations",
    "DSPCreateCampaignRequest",
    "DSPCreateFlightBudget",
    "DSPCreateFrequency",
    "DSPCreateGoalSettings",
    "DSPCreateMonetaryBudget",
    "DSPCreateMonetaryBudgetValue",
    "DSPCreateState",
    "DSPCreateTag",
    "DSPCurrencyCode",
    "DSPDeliveryReason",
    "DSPDeliveryStatus",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPFlightBudget",
    "DSPFrequency",
    "DSPFrequencyTargetingSetting",
    "DSPGoal",
    "DSPGoalSettings",
    "DSPIneligibleAutomatedTargetingTactic",
    "DSPIneligibleAutomatedTargetingTacticReason",
    "DSPIneligibleAutomatedTargetingTacticReasonCode",
    "DSPKPI",
    "DSPMarketplace",
    "DSPMonetaryBudget",
    "DSPMonetaryBudgetValue",
    "DSPPrimaryInventoryType",
    "DSPQueryCampaignRequest",
    "DSPRecurrence",
    "DSPRolloverStrategy",
    "DSPState",
    "DSPStatus",
    "DSPTacticKey",
    "DSPTag",
    "DSPTimeUnit",
    "DSPUpdateBidSettings",
    "DSPUpdateBudgetSettings",
    "DSPUpdateCampaignOptimizations",
    "DSPUpdateCampaignRequest",
    "DSPUpdateGoalSettings",
    "DSPUpdateState",
]
