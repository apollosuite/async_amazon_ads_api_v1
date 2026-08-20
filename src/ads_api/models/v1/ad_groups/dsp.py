"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAdProduct,
    DSPAutomatedTargetingTactic,
    DSPBidStrategy,
    DSPBudget,
    DSPBudgetAllocation,
    DSPBudgetType,
    DSPBudgetValue,
    DSPCreateBudget,
    DSPCreateBudgetValue,
    DSPCreateFrequency,
    DSPCreateMonetaryBudget,
    DSPCreateMonetaryBudgetValue,
    DSPCreateState,
    DSPCreateTag,
    DSPCurrencyCode,
    DSPDeliveryReason,
    DSPDeliveryStatus,
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
    DSPFrequency,
    DSPFrequencyTargetingSetting,
    DSPMonetaryBudget,
    DSPMonetaryBudgetValue,
    DSPRecurrence,
    DSPState,
    DSPStatus,
    DSPTag,
    DSPTimeUnit,
    DSPUpdateState,
)

type DSPCreativeRotationType = Literal["RANDOM", "WEIGHTED"]
"""
Supported values:
- `RANDOM`: Creatives are rotated randomly with equal weight.
- `WEIGHTED`: Creatives are rotated based on assigned weights.
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


type DSPFeesThirdPartyProvider = Literal[
    "COM_SCORE", "CPM_1", "CPM_2", "CPM_3", "DOUBLE_CLICK_CAMPAIGN_MANAGER", "DOUBLE_VERIFY", "INTEGRAL_AD_SCIENCE"
]


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
    include: list[DSPAdProduct] = Field(min_length=1, max_length=1)


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
    include: list[DSPState] = Field(min_length=1, max_length=3)


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


class DSPCreateFee(StrictModel):
    addToBudgetSpentAmount: bool = Field(
        description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad group budget spent amount in reports."
    )
    feeType: DSPFeeType
    feeValue: float = Field(
        description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the marketplace. All other CPM based fees are in the currency of the advertiser. For percentages, 100 represents 100%."
    )
    thirdPartyProvider: DSPFeesThirdPartyProvider


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
