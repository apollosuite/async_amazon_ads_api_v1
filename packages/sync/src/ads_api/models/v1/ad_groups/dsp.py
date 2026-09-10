"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAdProduct,
    DSPAutomatedTargetingTactic,
    DSPBidStrategy,
    DSPBudgetAllocation,
    DSPBudgetType,
    DSPCreateBudget,
    DSPCreateBudgetValue,
    DSPCreateFrequency,
    DSPCreateMonetaryBudget,
    DSPCreateMonetaryBudgetValue,
    DSPCreateState,
    DSPCreateTag,
    DSPCreativeRotationType,
    DSPCurrencyCode,
    DSPDefaultAudienceTargetingMatchType,
    DSPDeliveryProfile,
    DSPDeliveryReason,
    DSPDeliveryStatus,
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
    DSPEventType,
    DSPExtraFrequencyCapImpressionType,
    DSPFeesThirdPartyProvider,
    DSPFeeType,
    DSPFeeValueType,
    DSPFrequencyTargetingSetting,
    DSPInventoryType,
    DSPRecurrence,
    DSPSiteLanguage,
    DSPState,
    DSPTacticsConvertersExclusionType,
    DSPTimeUnit,
    DSPTimeZoneType,
    DSPUpdateState,
    DSPUserLocationSignal,
    DSPVideoCompletionTier,
    DSPViewabilityTier,
)


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
    baseBid: float | None = Field(
        default=None,
        description="The lower bound bid used for the ads in the ad group. This field is optional for ad groups that use automated bid optimization; when omitted, the system manages bidding on your behalf. It remains required when automated bid optimization is false, or if automated bid optimization is not available (e.g. programmatic guaranteed deal).",
    )
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


class DSPAdGroupInventoryTypeFilter(StrictModel):
    include: list[DSPInventoryType] = Field(min_length=1, max_length=1)


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


class DSPBudget(LenientModel):
    budgetType: DSPBudgetType | str
    budgetValue: DSPBudgetValue
    recurrenceTimePeriod: DSPRecurrence | str


class DSPBudgetValue(LenientModel):
    monetaryBudgetValue: DSPMonetaryBudgetValue


class DSPCreateAdGroupBid(StrictModel):
    baseBid: float | None = Field(
        default=None,
        description="The lower bound bid used for the ads in the ad group. This field is optional for ad groups that use automated bid optimization; when omitted, the system manages bidding on your behalf. It remains required when automated bid optimization is false, or if automated bid optimization is not available (e.g. programmatic guaranteed deal).",
    )
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


class DSPFrequency(LenientModel):
    eventCount: int | None = Field(
        default=None, ge=1, le=500, description="The number of events in a given frequency cap."
    )
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    eventType: DSPEventType | str | None = Field(default=None)
    extraFrequencyCapImpressionTypes: list[DSPExtraFrequencyCapImpressionType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Add the additional types of impression to frequency cap. Default to empty list when not selected",
    )
    frequencyTargetingSetting: DSPFrequencyTargetingSetting | str
    timeCount: int = Field(
        ge=1, le=60, description="The value associated with the time and unit of time for this frequency cap."
    )
    timeUnit: DSPTimeUnit | str


class DSPMonetaryBudget(LenientModel):
    currencyCode: DSPCurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
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
    inventoryTypeFilter: DSPAdGroupInventoryTypeFilter | None = Field(default=None)
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
    baseBid: float | None = Field(
        default=None,
        description="The lower bound bid used for the ads in the ad group. This field is optional for ad groups that use automated bid optimization; when omitted, the system manages bidding on your behalf. It remains required when automated bid optimization is false, or if automated bid optimization is not available (e.g. programmatic guaranteed deal).",
    )
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
    "DSPAdGroupInventoryTypeFilter",
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
    "DSPEventType",
    "DSPExtraFrequencyCapImpressionType",
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
