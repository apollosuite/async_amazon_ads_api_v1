"""Auto-generated models for Campaigns from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPKPI,
    DSPAdProduct,
    DSPAutomatedTargetingTactic,
    DSPBidStrategy,
    DSPBudgetAllocation,
    DSPBudgetType,
    DSPCampaignFeeType,
    DSPCampaignFeeValueType,
    DSPCountryCode,
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
    DSPEventType,
    DSPExtraFrequencyCapImpressionType,
    DSPFrequencyTargetingSetting,
    DSPGoal,
    DSPIneligibleAutomatedTargetingTacticReasonCode,
    DSPMarketplace,
    DSPPrimaryInventoryType,
    DSPRecurrence,
    DSPRolloverStrategy,
    DSPState,
    DSPTimeUnit,
    DSPUpdateState,
)


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
    include: list[DSPAdProduct] = Field(min_length=1, max_length=1)


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
    countries: list[DSPCountryCode] | None = Field(
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
    marketplaces: list[DSPMarketplace] | None = Field(
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
    include: list[DSPState] = Field(min_length=1, max_length=3)


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


class DSPCreateBudgetSettings(StrictModel):
    budgetAllocation: DSPBudgetAllocation | None = Field(default=None)
    flightBudgetRolloverStrategy: DSPRolloverStrategy | None = Field(default=None)


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
    primaryInventoryTypes: list[DSPPrimaryInventoryType] | None = Field(
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


class DSPCreateGoalSettings(StrictModel):
    kpi: DSPKPI
    kpiValue: float | None = Field(
        default=None, description="The value of the KPI that the campaign is working to optimize."
    )


class DSPFlightBudget(LenientModel):
    budgetType: DSPBudgetType | str
    budgetValue: DSPBudgetValue


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
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
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
    primaryInventoryTypes: list[DSPPrimaryInventoryType] | None = Field(
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
    "DSPEventType",
    "DSPExtraFrequencyCapImpressionType",
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
