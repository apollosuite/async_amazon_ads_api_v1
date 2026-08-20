"""Auto-generated models for CampaignForecasts from Amazon Ads API v1."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPKPI,
    DSPAcrossGroupOperator,
    DSPAdPlayerSize,
    DSPAdProduct,
    DSPAppType,
    DSPAutomatedTargetingTactic,
    DSPAverageCompletionAndFullyViewableRateTargetingType,
    DSPBidStrategy,
    DSPBrandExposureViewabilityTargetingType,
    DSPBrandSafetyCategory,
    DSPBrandSafetyTier,
    DSPBrandSuitabilityRiskLevelType,
    DSPBudgetAllocation,
    DSPBudgetType,
    DSPCampaignFeeType,
    DSPCampaignFeeValueType,
    DSPContentGenre,
    DSPContentInstreamPosition,
    DSPContentOutstreamPosition,
    DSPContentRatingTypes,
    DSPCountryCode,
    DSPCreativeRotationType,
    DSPCurrencyCode,
    DSPDayOfWeek,
    DSPDefaultAudienceTargetingMatchType,
    DSPDeliveryProfile,
    DSPDeliveryReason,
    DSPDeliveryStatus,
    DSPDeviceOrientation,
    DSPDeviceType,
    DSPDomainTargetTypes,
    DSPDspContentRatingEnum,
    DSPDVBrandSafetyAppAgeRatingType,
    DSPDVBrandSafetyAppStarRatingType,
    DSPDVBrandSafetyContentCategoryType,
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
    DSPEventType,
    DSPExcludeAppsAndSitesType,
    DSPExtraFrequencyCapImpressionType,
    DSPFeesThirdPartyProvider,
    DSPFeeType,
    DSPFeeValueType,
    DSPFoldPosition,
    DSPFrequencyTargetingSetting,
    DSPGoal,
    DSPIASBrandSafetyLevelType,
    DSPIASFraudInvalidTrafficType,
    DSPIASViewabilityStandardType,
    DSPIneligibleAutomatedTargetingTacticReasonCode,
    DSPInGroupOperator,
    DSPInventorySourceType,
    DSPInventoryType,
    DSPKeywordMatchType,
    DSPMarketplace,
    DSPMarketplaceScope,
    DSPMarketplaceStringValue,
    DSPMarketplaceStringValueOut,
    DSPMobileDevice,
    DSPMobileEnvironment,
    DSPMobileOs,
    DSPMonetaryBudgetOut,
    DSPMrcViewabilityTargetingType,
    DSPNativeContentPosition,
    DSPNewsGuardBrandGuardMisinformationSafetyType,
    DSPNewsGuardBrandGuardTrustedNewsTargetingType,
    DSPPlacementType,
    DSPPrimaryInventoryType,
    DSPProductCategoryMatchType,
    DSPProductIdType,
    DSPProductMatchType,
    DSPRecurrence,
    DSPRolloverStrategy,
    DSPSiteLanguage,
    DSPState,
    DSPTacticsConvertersExclusionType,
    DSPTargetLevel,
    DSPTargetType,
    DSPThemeMatchType,
    DSPThirdPartyTargetType,
    DSPTimeOfDayOut,
    DSPTimeUnit,
    DSPTimeZoneType,
    DSPTwitchContentRatingEnum,
    DSPUserLocationSignal,
    DSPVideoAdFormat,
    DSPVideoCompletionTier,
    DSPVideoContentDuration,
    DSPVideoInitiationType,
    DSPViewabilityTier,
    DSPViewabilityTierType,
)

type DSPDeliverInFullConfidenceLevel = Literal["HIGH", "LOW", "MEDIUM", "UNAVAILABLE"]
"""
Supported values:
- `HIGH`: There is a high level of confidence that the campaign or flight will fully deliver its planned budget or impressions.
- `MEDIUM`: There is a moderate level of confidence that the campaign or flight will fully deliver its planned budget or impressions.
- `LOW`: There is a low level of confidence that the campaign or flight will fully deliver its planned budget or impressions.
- `UNAVAILABLE`: Confidence level cannot be determined due to insufficient or missing data.
"""


type DSPForecastPeriodicity = Literal["DAILY", "LIFETIME", "MONTHLY", "WEEKLY"]
"""
Supported values:
- `DAILY`: Forecast results are generated and presented for each individual day.
- `LIFETIME`: Forecast results represent the total performance over the remaining entire campaign duration.
- `MONTHLY`: Forecast results are aggregated and presented for each calendar month.
- `WEEKLY`: Forecast results are aggregated and presented for each calendar week.
"""


type DSPInsightFeature = Literal[
    "CAMPAIGN_FREQUENCY_CAP",
    "LINE_ITEM_APPBLOCKING_TARGETING",
    "LINE_ITEM_COLD_START_DEALS",
    "LINE_ITEM_COLD_START_SEGMENTS",
    "LINE_ITEM_CONTEXTUAL_TARGETING",
    "LINE_ITEM_DOMAINLIST_TARGETING",
    "LINE_ITEM_FREQUENCY_CAP",
    "LINE_ITEM_GEO_TARGETING",
    "LINE_ITEM_LARGE_TARGETING",
    "LINE_ITEM_MAX_BID",
    "LINE_ITEM_MOBILE_DEVICES_TARGETING",
    "LINE_ITEM_NARROW_SEGMENTS",
    "LINE_ITEM_SIMILAR_AUDIENCES",
    "LINE_ITEM_TOO_FAR_IN_FUTURE",
    "LINE_ITEM_UNSUPPORTED_CONTEXTUAL_TARGETING",
    "LINE_ITEM_UNSUPPORTED_KEYWORD_TARGETING",
]
"""
Supported values:
- `LINE_ITEM_FREQUENCY_CAP`: Insight associated with line item having restrictive frequency cap setting.
- `LINE_ITEM_MAX_BID`: Insight associated with line item having inadequate max bid setting.
- `LINE_ITEM_SIMILAR_AUDIENCES`: Insight associated with line item not presently reaching similar audiences.
- `LINE_ITEM_COLD_START_DEALS`: Insight associated with line item having newly created deals present.
- `LINE_ITEM_COLD_START_SEGMENTS`: Insight associated with line item having newly created behavioral segments present.
- `LINE_ITEM_NARROW_SEGMENTS`: Insight associated with line item having narrowly targeted behavioral segments present.
- `LINE_ITEM_LARGE_TARGETING`: Insight associated with line item having an excessive amount of behavioral segments targeted.
- `LINE_ITEM_UNSUPPORTED_KEYWORD_TARGETING`: Insight associated with line item having unsupported keyword targeting settings present.
- `LINE_ITEM_UNSUPPORTED_CONTEXTUAL_TARGETING`: Insight associated with line item having unsupported contextual targeting settings present.
- `LINE_ITEM_GEO_TARGETING`: Insight associated with line item having restrictive geo-targeting present.
- `LINE_ITEM_TOO_FAR_IN_FUTURE`: Insight associated with line item having end date too far in the future.
- `LINE_ITEM_DOMAINLIST_TARGETING`: Insight associated with line item having restrictive domain list targeting.
- `LINE_ITEM_APPBLOCKING_TARGETING`: Insight associated with line item having restrictive app blocking targeting.
- `LINE_ITEM_MOBILE_DEVICES_TARGETING`: Insight associated with line item having restrictive mobile device targeting.
- `LINE_ITEM_CONTEXTUAL_TARGETING`: Insight associated with line item having restrictive contextual targeting.
- `CAMPAIGN_FREQUENCY_CAP`: Insight associated with restrictive campaign frequency cap setting.
"""


type DSPPointLabel = Literal[
    "AIMP", "AREA", "BID", "CAS", "CPA", "CPC", "CPM", "DC", "EIMP", "EREA", "ROAS", "SPEND", "TAS"
]
"""
Supported values:
- `SPEND`: Spend in monetary value.
- `BID`: Bid in monetary value.
- `DC`: Delivery confidence.
- `TAS`: Total available spend.
- `AIMP`: Available impressions.
- `AREA`: Available reach.
- `EIMP`: Expected impressions.
- `EREA`: Expected reach.
- `CPC`: Cost per click.
- `CPA`: Cost per action.
- `CPM`: Cost per mille.
- `ROAS`: Return on ad spend.
- `CAS`: Capped available spend.
"""


type DSPRecommendedObjectType = Literal["ADGROUP", "CAMPAIGN"]
"""
Supported values:
- `CAMPAIGN`: An advertising campaign that groups together ad groups and ads
- `ADGROUP`: A group of ads within a campaign that share similar targeting
"""


type DSPSelectedForecastMetric = Literal[
    "AIMP", "AREA", "CAS", "CPA", "CPC", "CPM", "DC", "EIMP", "EREA", "IREA", "ROAS", "TAS"
]
"""
Supported values:
- `DC`: Delivery confidence.
- `TAS`: Total available spend.
- `AIMP`: Available impressions.
- `AREA`: Available reach.
- `EIMP`: Expected impressions.
- `EREA`: Expected reach.
- `CPC`: Cost per click.
- `CPA`: Cost per action.
- `CPM`: Cost per mille.
- `ROAS`: Return on ad spend.
- `CAS`: Capped available spend.
- `IREA`: Incremental reach.
"""


class DSPAdGroupBid(StrictModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    currencyCode: DSPCurrencyCode
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPAdGroupBidOut(LenientModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    currencyCode: DSPCurrencyCode | str
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPAdGroupBudgetSettings(StrictModel):
    budgetAllocation: DSPBudgetAllocation | None = Field(default=None)
    dailyMinSpendValue: float | None = Field(
        default=None, description="Denotes the daily minimum spend on the ad group in local currency."
    )


class DSPAdGroupBudgetSettingsOut(LenientModel):
    budgetAllocation: DSPBudgetAllocation | str | None = Field(default=None)
    dailyMinSpendValue: float | None = Field(
        default=None, description="Denotes the daily minimum spend on the ad group in local currency."
    )


class DSPAdInitiationTarget(StrictModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: DSPVideoInitiationType


class DSPAdInitiationTargetOut(LenientModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: DSPVideoInitiationType | str


class DSPAdPlayerSizeTarget(StrictModel):
    """Target based on the size of the ad player."""

    adPlayerSize: DSPAdPlayerSize


class DSPAdPlayerSizeTargetOut(LenientModel):
    """Target based on the size of the ad player."""

    adPlayerSize: DSPAdPlayerSize | str


class DSPAdvertiserDomainList(StrictModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPAdvertiserDomainListOut(LenientModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPAmazonViewability(StrictModel):
    includeUnmeasurableImpressions: bool = Field(
        description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measured when a viewabilityTier other than ALL_TIERS is selected. We recommend setting to false if high viewability is your goal."
    )
    viewabilityTier: DSPViewabilityTier


class DSPAmazonViewabilityOut(LenientModel):
    includeUnmeasurableImpressions: bool = Field(
        description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measured when a viewabilityTier other than ALL_TIERS is selected. We recommend setting to false if high viewability is your goal."
    )
    viewabilityTier: DSPViewabilityTier | str


class DSPAppTarget(StrictModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: DSPAppType


class DSPAppTargetOut(LenientModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: DSPAppType | str


class DSPAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: DSPAcrossGroupOperator | None = Field(default=None)
    audienceId: DSPMarketplaceStringValue
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: DSPInGroupOperator | None = Field(default=None)


class DSPAudienceTargetOut(LenientModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: DSPAcrossGroupOperator | str | None = Field(default=None)
    audienceId: DSPMarketplaceStringValueOut
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: DSPInGroupOperator | str | None = Field(default=None)


class DSPAutoCreationSettings(StrictModel):
    autoManageCampaign: bool | None = Field(
        default=None, description="Flag that allows Amazon to manage the lifecycle of your Campaign."
    )


class DSPAutoCreationSettingsOut(LenientModel):
    autoManageCampaign: bool | None = Field(
        default=None, description="Flag that allows Amazon to manage the lifecycle of your Campaign."
    )


class DSPBidSettings(StrictModel):
    bidStrategy: DSPBidStrategy


class DSPBidSettingsOut(LenientModel):
    bidStrategy: DSPBidStrategy | str


class DSPBrandSafetyCategoryTarget(StrictModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: DSPBrandSafetyCategory


class DSPBrandSafetyCategoryTargetOut(LenientModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: DSPBrandSafetyCategory | str


class DSPBrandSafetyTierTarget(StrictModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: DSPBrandSafetyTier


class DSPBrandSafetyTierTargetOut(LenientModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: DSPBrandSafetyTier | str


class DSPBudget(StrictModel):
    budgetType: DSPBudgetType
    budgetValue: DSPBudgetValue
    recurrenceTimePeriod: DSPRecurrence


class DSPBudgetOut(LenientModel):
    budgetType: DSPBudgetType | str
    budgetValue: DSPBudgetValueOut
    recurrenceTimePeriod: DSPRecurrence | str


class DSPBudgetSettings(StrictModel):
    budgetAllocation: DSPBudgetAllocation | None = Field(default=None)
    flightBudgetRolloverStrategy: DSPRolloverStrategy | None = Field(default=None)


class DSPBudgetSettingsOut(LenientModel):
    budgetAllocation: DSPBudgetAllocation | str | None = Field(default=None)
    flightBudgetRolloverStrategy: DSPRolloverStrategy | str | None = Field(default=None)


class DSPBudgetValue(StrictModel):
    monetaryBudgetValue: DSPMonetaryBudgetValue


class DSPBudgetValueOut(LenientModel):
    monetaryBudgetValue: DSPMonetaryBudgetValueOut


class DSPCampaignFee(StrictModel):
    feeType: DSPCampaignFeeType
    feeValue: float = Field(
        description="A service fee that is subtracted from the campaign budget as a percent of budget. This setting can’t be changed after an ad group has been added to a campaign."
    )
    feeValueType: DSPCampaignFeeValueType


class DSPCampaignFeeOut(LenientModel):
    feeType: DSPCampaignFeeType | str
    feeValue: float = Field(
        description="A service fee that is subtracted from the campaign budget as a percent of budget. This setting can’t be changed after an ad group has been added to a campaign."
    )
    feeValueType: DSPCampaignFeeValueType | str


class DSPCampaignFlight(StrictModel):
    budget: DSPFlightBudget
    endDateTime: datetime = Field(description="The end date of the flight.")
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    name: str | None = Field(default=None, description="The name of the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPCampaignFlightOut(LenientModel):
    budget: DSPFlightBudgetOut
    endDateTime: datetime = Field(description="The end date of the flight.")
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    name: str | None = Field(default=None, description="The name of the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPCampaignForecast(LenientModel):
    availableForecastFlights: list[DSPForecastFlightOut] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
        description="The combination of existing flight settings and proposed flight settings based on forecasting.",
    )
    campaignDisplayName: str = Field(description="The display name of the campaign used for the forecast.")
    campaignForecastDescription: DSPCampaignForecastDescriptionOut
    campaignGoalSettings: DSPGoalSettingsOut | None = Field(default=None)
    creationDateTime: datetime = Field(description="The creation date of the campaign forecast.")
    flightForecasts: list[DSPFlightForecast] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The forecast results of multiple flights of the campaign.",
    )
    hasExistingGuidance: bool | None = Field(
        default=None,
        description="Indicates whether there are existing recommendations/guidance available for the campaign from the Noble ListGuidance API.",
    )


class DSPCampaignForecastDescription(StrictModel):
    """The description of which campaign and what features are enabled for a forecast."""

    campaignId: str = Field(description="The unique identifier of the campaign.")
    enabledFeatures: DSPEnabledFeaturesInCampaignForecast | None = Field(default=None)
    flightIds: list[str] | None = Field(
        default=None, min_length=0, max_length=5, description="The unique identifier of the flight."
    )
    replanningSettings: DSPReplanningSettings | None = Field(default=None)


class DSPCampaignForecastDescriptionOut(LenientModel):
    """The description of which campaign and what features are enabled for a forecast."""

    campaignId: str = Field(description="The unique identifier of the campaign.")
    enabledFeatures: DSPEnabledFeaturesInCampaignForecastOut | None = Field(default=None)
    flightIds: list[str] | None = Field(
        default=None, min_length=0, max_length=5, description="The unique identifier of the flight."
    )
    replanningSettings: DSPReplanningSettingsOut | None = Field(default=None)


class DSPCampaignForecastMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1)
    success: list[DSPCampaignForecastMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1)


class DSPCampaignForecastMultiStatusSuccess(LenientModel):
    campaignForecast: DSPCampaignForecast
    index: int = Field(ge=0, le=0)


class DSPCampaignOptimizations(StrictModel):
    bidSettings: DSPBidSettings
    budgetSettings: DSPBudgetSettings | None = Field(default=None)
    goalSettings: DSPGoalSettings | None = Field(default=None)
    primaryInventoryTypes: list[DSPPrimaryInventoryType] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.",
    )


class DSPCampaignOptimizationsOut(LenientModel):
    bidSettings: DSPBidSettingsOut
    budgetSettings: DSPBudgetSettingsOut | None = Field(default=None)
    goalSettings: DSPGoalSettingsOut | None = Field(default=None)
    primaryInventoryTypes: list[DSPPrimaryInventoryType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.",
    )


class DSPContentCategoryTarget(StrictModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPContentCategoryTargetOut(LenientModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPContentGenreTarget(StrictModel):
    """Target based on the genre of content being viewed."""

    contentGenre: DSPContentGenre


class DSPContentGenreTargetOut(LenientModel):
    """Target based on the genre of content being viewed."""

    contentGenre: DSPContentGenre | str


class DSPContentInstreamPositionTarget(StrictModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: DSPContentInstreamPosition


class DSPContentInstreamPositionTargetOut(LenientModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: DSPContentInstreamPosition | str


class DSPContentOutstreamPositionTarget(StrictModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: DSPContentOutstreamPosition


class DSPContentOutstreamPositionTargetOut(LenientModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: DSPContentOutstreamPosition | str


class DSPContentRatingDspContentRating(StrictModel):
    dspContentRating: DSPDspContentRating


class DSPContentRatingTwitchContentRating(StrictModel):
    twitchContentRating: DSPTwitchContentRating


type DSPContentRating = DSPContentRatingDspContentRating | DSPContentRatingTwitchContentRating


class DSPContentRatingOutDspContentRating(LenientModel):
    dspContentRating: DSPDspContentRatingOut


class DSPContentRatingOutTwitchContentRating(LenientModel):
    twitchContentRating: DSPTwitchContentRatingOut


type DSPContentRatingOut = DSPContentRatingOutDspContentRating | DSPContentRatingOutTwitchContentRating


class DSPContentRatingTarget(StrictModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: DSPContentRatingTypes
    contentRatingTypeDetails: DSPContentRating


class DSPContentRatingTargetOut(LenientModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: DSPContentRatingTypes | str
    contentRatingTypeDetails: DSPContentRatingOut


class DSPCurve(LenientModel):
    """The forecast curve of Bid/Spend vs the metric type based on periodicity."""

    focusPoint: list[DSPPoint] | None = Field(default=None, min_length=0, max_length=10)
    periodicity: DSPForecastPeriodicity | str | None = Field(default=None)
    points: list[DSPPoint] | None = Field(default=None, min_length=0, max_length=1000)


class DSPDVBrandSafetyContentCategoriesWithRiskMap(StrictModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: DSPBrandSuitabilityRiskLevelType


class DSPDVBrandSafetyContentCategoriesWithRiskMapOut(LenientModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: DSPBrandSuitabilityRiskLevelType | str


class DSPDayPartTarget(StrictModel):
    """Target based on time of day."""

    dayOfWeek: DSPDayOfWeek
    timeOfDay: DSPTimeOfDay


class DSPDayPartTargetOut(LenientModel):
    """Target based on time of day."""

    dayOfWeek: DSPDayOfWeek | str
    timeOfDay: DSPTimeOfDayOut


class DSPDeliverInFullConfidence(LenientModel):
    """Description of how confident we delivery 100% of the ads for the specific metric."""

    value: DSPDeliverInFullConfidenceLevel | str


class DSPDeviceTarget(StrictModel):
    """Target based on user device."""

    deviceOrientation: DSPDeviceOrientation | None = Field(default=None)
    deviceType: DSPDeviceType
    mobileDevice: DSPMobileDevice | None = Field(default=None)
    mobileEnvironment: DSPMobileEnvironment | None = Field(default=None)
    mobileOs: DSPMobileOs | None = Field(default=None)


class DSPDeviceTargetOut(LenientModel):
    """Target based on user device."""

    deviceOrientation: DSPDeviceOrientation | str | None = Field(default=None)
    deviceType: DSPDeviceType | str
    mobileDevice: DSPMobileDevice | str | None = Field(default=None)
    mobileEnvironment: DSPMobileEnvironment | str | None = Field(default=None)
    mobileOs: DSPMobileOs | str | None = Field(default=None)


class DSPDomainFileTarget(StrictModel):
    """Targets domains based on list provided via file upload."""

    domainFileId: str | None = Field(
        default=None,
        description="The ID associated to the domain file to target. Read-only and created based on the inputted domainFileKey.",
    )
    domainFileKey: str = Field(
        description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be associated to one ad group."
    )
    domainFileName: str = Field(description="The name of the file.")
    domainFileUrl: str | None = Field(
        default=None, description="The file containing the domains uploaded. It expires in one hour."
    )


class DSPDomainFileTargetOut(LenientModel):
    """Targets domains based on list provided via file upload."""

    domainFileId: str | None = Field(
        default=None,
        description="The ID associated to the domain file to target. Read-only and created based on the inputted domainFileKey.",
    )
    domainFileKey: str = Field(
        description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be associated to one ad group."
    )
    domainFileName: str = Field(description="The name of the file.")
    domainFileUrl: str | None = Field(
        default=None, description="The file containing the domains uploaded. It expires in one hour."
    )


class DSPDomainListTarget(StrictModel):
    """Targets domains based on an existing domain list."""

    domainListId: str = Field(description="The ID of the domain list to target.")


class DSPDomainListTargetOut(LenientModel):
    """Targets domains based on an existing domain list."""

    domainListId: str = Field(description="The ID of the domain list to target.")


class DSPDomainNameTarget(StrictModel):
    """Targets domains based on URL."""

    domainName: str = Field(description="The URL of the domain to target.")


class DSPDomainNameTargetOut(LenientModel):
    """Targets domains based on URL."""

    domainName: str = Field(description="The URL of the domain to target.")


class DSPDomainTarget(StrictModel):
    """Target based on a specified domain."""

    domainTargetDetails: DSPDomainTargetDetails
    domainTargetType: DSPDomainTargetTypes


class DSPDomainTargetDetailsAdvertiserDomainList(StrictModel):
    advertiserDomainList: DSPAdvertiserDomainList


class DSPDomainTargetDetailsDomainFileTarget(StrictModel):
    domainFileTarget: DSPDomainFileTarget


class DSPDomainTargetDetailsDomainListTarget(StrictModel):
    domainListTarget: DSPDomainListTarget


class DSPDomainTargetDetailsDomainNameTarget(StrictModel):
    domainNameTarget: DSPDomainNameTarget


type DSPDomainTargetDetails = DSPDomainTargetDetailsAdvertiserDomainList | DSPDomainTargetDetailsDomainFileTarget | DSPDomainTargetDetailsDomainListTarget | DSPDomainTargetDetailsDomainNameTarget


class DSPDomainTargetDetailsOutAdvertiserDomainList(LenientModel):
    advertiserDomainList: DSPAdvertiserDomainListOut


class DSPDomainTargetDetailsOutDomainFileTarget(LenientModel):
    domainFileTarget: DSPDomainFileTargetOut


class DSPDomainTargetDetailsOutDomainListTarget(LenientModel):
    domainListTarget: DSPDomainListTargetOut


class DSPDomainTargetDetailsOutDomainNameTarget(LenientModel):
    domainNameTarget: DSPDomainNameTargetOut


type DSPDomainTargetDetailsOut = DSPDomainTargetDetailsOutAdvertiserDomainList | DSPDomainTargetDetailsOutDomainFileTarget | DSPDomainTargetDetailsOutDomainListTarget | DSPDomainTargetDetailsOutDomainNameTarget


class DSPDomainTargetOut(LenientModel):
    """Target based on a specified domain."""

    domainTargetDetails: DSPDomainTargetDetailsOut
    domainTargetType: DSPDomainTargetTypes | str


class DSPDoubleVerifyAuthenticAttention(StrictModel):
    universalAttention: bool = Field(
        description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor performing apps and domains."
    )


class DSPDoubleVerifyAuthenticAttentionOut(LenientModel):
    universalAttention: bool = Field(
        description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor performing apps and domains."
    )


class DSPDoubleVerifyAuthenticBrandSafety(StrictModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^51[0-9]{6}$")


class DSPDoubleVerifyAuthenticBrandSafetyOut(LenientModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^51[0-9]{6}$")


class DSPDoubleVerifyBrandSafety(StrictModel):
    appAgeRating: list[DSPDVBrandSafetyAppAgeRatingType] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="A list of app age ratings to be used for excluding apps. For example, TEENS_12_PLUS will only exclude apps with content rated for everyone ages 12 and over. UNKNOWN will exclude apps with content unrated or unknown to Double Verify.",
    )
    appStarRating: DSPDVBrandSafetyAppStarRatingType | None = Field(default=None)
    contentCategories: list[DSPDVBrandSafetyContentCategoryType] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    excludeAppsWithInsufficientRating: bool | None = Field(
        default=None,
        description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).",
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyBrandSafetyOut(LenientModel):
    appAgeRating: list[DSPDVBrandSafetyAppAgeRatingType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="A list of app age ratings to be used for excluding apps. For example, TEENS_12_PLUS will only exclude apps with content rated for everyone ages 12 and over. UNKNOWN will exclude apps with content unrated or unknown to Double Verify.",
    )
    appStarRating: DSPDVBrandSafetyAppStarRatingType | str | None = Field(default=None)
    contentCategories: list[DSPDVBrandSafetyContentCategoryType | str] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMapOut] | None = Field(
        default=None, min_length=0, max_length=50
    )
    excludeAppsWithInsufficientRating: bool | None = Field(
        default=None,
        description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).",
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyCustomContextualSegmentId(StrictModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^52[0-9]{6}$")


class DSPDoubleVerifyCustomContextualSegmentIdOut(LenientModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^52[0-9]{6}$")


class DSPDoubleVerifyFraudInvalidTraffic(StrictModel):
    blockAppAndSites: bool | None = Field(
        default=None,
        description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will not be applicable if ALLOW_ALL is chosen.",
    )
    excludeAppsAndSites: DSPExcludeAppsAndSitesType | None = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPDoubleVerifyFraudInvalidTrafficOut(LenientModel):
    blockAppAndSites: bool | None = Field(
        default=None,
        description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will not be applicable if ALLOW_ALL is chosen.",
    )
    excludeAppsAndSites: DSPExcludeAppsAndSitesType | str | None = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPDoubleVerifyStandardDisplayBrandSafety(StrictModel):
    contentCategories: list[DSPDVBrandSafetyContentCategoryType] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyStandardDisplayBrandSafetyOut(LenientModel):
    contentCategories: list[DSPDVBrandSafetyContentCategoryType | str] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMapOut] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyViewability(StrictModel):
    averageCompletionAndFullyViewableRateTargeting: DSPAverageCompletionAndFullyViewableRateTargetingType | None = (
        Field(default=None)
    )
    brandExposureViewabilityTargeting: DSPBrandExposureViewabilityTargetingType | None = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: DSPMrcViewabilityTargetingType | None = Field(default=None)


class DSPDoubleVerifyViewabilityOut(LenientModel):
    averageCompletionAndFullyViewableRateTargeting: (
        DSPAverageCompletionAndFullyViewableRateTargetingType | str | None
    ) = Field(default=None)
    brandExposureViewabilityTargeting: DSPBrandExposureViewabilityTargetingType | str | None = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: DSPMrcViewabilityTargetingType | str | None = Field(default=None)


class DSPDspContentRating(StrictModel):
    dspContentRating: DSPDspContentRatingEnum


class DSPDspContentRatingOut(LenientModel):
    dspContentRating: DSPDspContentRatingEnum | str


class DSPEnabledFeaturesInCampaignForecast(StrictModel):
    """For the user to specify which features to enable in the forecast result."""

    campaignSettingsCache: bool | None = Field(
        default=None, description="Describe if the forecast will use cached settings of a campaign."
    )
    curve: bool | None = Field(default=None, description="Describe if the user want to see curve or not.")
    deliveryMetrics: bool | None = Field(
        default=None,
        description="Describe if the user wants to see delivery metrics, e.g. spend, projected spend, additional spend potential, and delivery rate.",
    )
    insights: bool | None = Field(
        default=None,
        description="Describe if the user want to see detailed insights for leading drivers of forecast results.",
    )
    metrics: DSPForecastMetricsDescription | None = Field(default=None)
    replanning: bool | None = Field(
        default=None, description="Describe if the forecast will show replanning recommendation."
    )


class DSPEnabledFeaturesInCampaignForecastOut(LenientModel):
    """For the user to specify which features to enable in the forecast result."""

    campaignSettingsCache: bool | None = Field(
        default=None, description="Describe if the forecast will use cached settings of a campaign."
    )
    curve: bool | None = Field(default=None, description="Describe if the user want to see curve or not.")
    deliveryMetrics: bool | None = Field(
        default=None,
        description="Describe if the user wants to see delivery metrics, e.g. spend, projected spend, additional spend potential, and delivery rate.",
    )
    insights: bool | None = Field(
        default=None,
        description="Describe if the user want to see detailed insights for leading drivers of forecast results.",
    )
    metrics: DSPForecastMetricsDescriptionOut | None = Field(default=None)
    replanning: bool | None = Field(
        default=None, description="Describe if the forecast will show replanning recommendation."
    )


class DSPFee(StrictModel):
    addToBudgetSpentAmount: bool = Field(
        description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad group budget spent amount in reports."
    )
    currencyCode: DSPCurrencyCode | None = Field(default=None)
    feeType: DSPFeeType
    feeValue: float = Field(
        description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the marketplace. All other CPM based fees are in the currency of the advertiser. For percentages, 100 represents 100%."
    )
    feeValueType: DSPFeeValueType
    thirdPartyProvider: DSPFeesThirdPartyProvider


class DSPFeeOut(LenientModel):
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


class DSPFlightBudget(StrictModel):
    budgetType: DSPBudgetType
    budgetValue: DSPBudgetValue


class DSPFlightBudgetOut(LenientModel):
    budgetType: DSPBudgetType | str
    budgetValue: DSPBudgetValueOut


class DSPFlightForecast(LenientModel):
    """The forecast result of a specific flight."""

    additionalSpendPotential: float | None = Field(
        default=None,
        description="The additional spend potential beyond the current flight budget. Only populated for in-flight campaigns.",
    )
    budgetAtRisk: DSPMonetaryBudgetOut | None = Field(default=None)
    currencyCode: DSPCurrencyCode | str | None = Field(default=None)
    curves: list[DSPCurve] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="The forecasting curves of a flight based on different periodicities.",
    )
    deliverInFullConfidence: DSPDeliverInFullConfidence | None = Field(default=None)
    deliveryRate: float | None = Field(
        default=None,
        description="The delivery rate of the current flight as a decimal (0 to 1). Only populated for in-flight campaigns.",
    )
    flightId: str = Field(description="The flightId of the flight.")
    forecastEndDateTime: datetime = Field(description="The endtime of the flight for forecasting.")
    forecastStartDateTime: datetime = Field(description="The starttime of the flight for forecasting.")
    insights: DSPFlightForecastInsights | None = Field(default=None)
    metrics: list[DSPForecastMetric] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="The different metrics to measure the performance of the flight.",
    )
    projectedSpend: float | None = Field(
        default=None,
        description="The projected total spend by end of the current flight. Only populated for in-flight campaigns.",
    )
    replanning: list[DSPReplanning] | None = Field(
        default=None, min_length=0, max_length=100, description="The recommendation for replanning."
    )
    spend: float | None = Field(default=None, description="The amount of money spend for this flight.")
    totalBudget: DSPMonetaryBudgetOut | None = Field(default=None)
    warnings: list[DSPWarning] | None = Field(
        default=None, min_length=0, max_length=10, description="Warnings of the campaign forecast."
    )


class DSPFlightForecastInsights(LenientModel):
    """Collection of insights for a particular flight forecast."""

    forecastExplainabilityInsights: list[DSPForecastInsightsGroup] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Detailed insights explaining leading drivers of the flight forecast results, per entity (e.g. campaign or its line items).",
    )
    topExplainabilityFactors: list[DSPInsightFeature | str] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Top factors affecting the forecast results, e.g. max bid, frequency cap, etc.",
    )


class DSPFoldPositionTarget(StrictModel):
    """Targets ads in the specified fold position"""

    foldPosition: DSPFoldPosition


class DSPFoldPositionTargetOut(LenientModel):
    """Targets ads in the specified fold position"""

    foldPosition: DSPFoldPosition | str


class DSPForecastAdGroup(StrictModel):
    """Ad group domain model"""

    adGroupId: str | None = Field(default=None, description="The unique identifier of the ad group.")
    adProduct: DSPAdProduct | None = Field(default=None)
    advertisedProductCategoryIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=500,
        description="The array of identifiers of advertised product categories associated with the forecast.",
    )
    bid: DSPAdGroupBid | None = Field(default=None)
    budgets: list[DSPBudget] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing budget details for the ad group."
    )
    campaignId: str | None = Field(
        default=None, description="The unique identifier of the campaign the ad group belongs to."
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the ad group was created.")
    creativeRotationType: DSPCreativeRotationType | None = Field(default=None)
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad group.")
    fees: list[DSPFee] | None = Field(
        default=None, min_length=0, max_length=100, description="The fees associated with the ad group."
    )
    frequencies: list[DSPFrequency] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="An object containing frequency details for the ad group.",
    )
    globalAdGroupId: str | None = Field(
        default=None, description="The global adGroup identifier that manages this marketplace adGroup."
    )
    inventoryType: DSPInventoryType | None = Field(default=None)
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the ad group was last updated."
    )
    marketplaceConfigurations: list[DSPMarketplaceAdGroupConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individual marketplace level. For example, if a global ad group state is ENABLED and needs to be PAUSED only in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, ad group's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | None = Field(default=None)
    marketplaces: list[DSPMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    optimization: DSPOptimization | None = Field(default=None)
    pacing: DSPPacing | None = Field(default=None)
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the ad group."
    )
    retailerId: str | None = Field(default=None, description="Identifier for retailer associated with this ad group.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad group.")
    state: DSPState | None = Field(default=None)
    status: DSPStatus | None = Field(default=None)
    tags: list[DSPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )
    targetingSettings: DSPTargetingSettings | None = Field(default=None)


class DSPForecastAdGroupOut(LenientModel):
    """Ad group domain model"""

    adGroupId: str | None = Field(default=None, description="The unique identifier of the ad group.")
    adProduct: DSPAdProduct | str | None = Field(default=None)
    advertisedProductCategoryIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=500,
        description="The array of identifiers of advertised product categories associated with the forecast.",
    )
    bid: DSPAdGroupBidOut | None = Field(default=None)
    budgets: list[DSPBudgetOut] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing budget details for the ad group."
    )
    campaignId: str | None = Field(
        default=None, description="The unique identifier of the campaign the ad group belongs to."
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the ad group was created.")
    creativeRotationType: DSPCreativeRotationType | str | None = Field(default=None)
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad group.")
    fees: list[DSPFeeOut] | None = Field(
        default=None, min_length=0, max_length=100, description="The fees associated with the ad group."
    )
    frequencies: list[DSPFrequencyOut] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="An object containing frequency details for the ad group.",
    )
    globalAdGroupId: str | None = Field(
        default=None, description="The global adGroup identifier that manages this marketplace adGroup."
    )
    inventoryType: DSPInventoryType | str | None = Field(default=None)
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the ad group was last updated."
    )
    marketplaceConfigurations: list[DSPMarketplaceAdGroupConfigurationsOut] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individual marketplace level. For example, if a global ad group state is ENABLED and needs to be PAUSED only in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, ad group's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | str | None = Field(default=None)
    marketplaces: list[DSPMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    optimization: DSPOptimizationOut | None = Field(default=None)
    pacing: DSPPacingOut | None = Field(default=None)
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the ad group."
    )
    retailerId: str | None = Field(default=None, description="Identifier for retailer associated with this ad group.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad group.")
    state: DSPState | str | None = Field(default=None)
    status: DSPStatusOut | None = Field(default=None)
    tags: list[DSPTagOut] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )
    targetingSettings: DSPTargetingSettingsOut | None = Field(default=None)


class DSPForecastCampaign(StrictModel):
    """Campaign domain model"""

    adProduct: DSPAdProduct | None = Field(default=None)
    adomains: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case of rotating creatives. Exchanges can mandate that only one domain is allowed.",
    )
    autoCreationSettings: DSPAutoCreationSettings | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[DSPBudget] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str | None = Field(default=None, description="A unique identifier for a campaign.")
    campaignPresetId: str | None = Field(
        default=None,
        description="This is the ID of the originally generated campaign preset that the campaign is associated with.",
    )
    countries: list[DSPCountryCode] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the campaign was created.")
    eligibleAutomatedTargetingTactics: list[DSPTacticKey] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are eligible for use with this campaign",
    )
    endDate: date | None = Field(default=None, description="The end date of the campaign.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    fees: list[DSPCampaignFee] | None = Field(
        default=None, min_length=0, max_length=2, description="Any fees associated with the campaign."
    )
    flights: list[DSPCampaignFlight] | None = Field(
        default=None, min_length=0, max_length=10, description="Flight details associated with the campaign."
    )
    frequencies: list[DSPFrequency] | None = Field(
        default=None, min_length=0, max_length=10, description="Any frequency caps associated with the campaign."
    )
    globalCampaignId: str | None = Field(
        default=None, description="The global campaign identifier that manages this marketplace campaign."
    )
    ineligibleAutomatedTargetingTactics: list[DSPIneligibleAutomatedTargetingTactic] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are ineligible for use with this campaign, along with reasons for ineligibility",
    )
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the campaign was last updated."
    )
    marketplaceConfigurations: list[DSPMarketplaceCampaignConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individual marketplace level. For example, if a global campaign is ENABLED and startDate '2024-06-01' but needs to be PAUSED in DE with startDateTime '2024-06-02' marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED, startDate: '2024-06-02'}}]. When a marketplace-specific override is not provided, the campaign's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | None = Field(default=None)
    marketplaces: list[DSPMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: DSPCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    productCategoryId: str | None = Field(
        default=None, description="This is the ID of the product category that the campaign is associated with."
    )
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the campaign."
    )
    skanAppId: str | None = Field(
        default=None,
        description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.",
    )
    startDate: date | None = Field(default=None, description="The start date of the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: DSPState | None = Field(default=None)
    status: DSPStatus | None = Field(default=None)
    tags: list[DSPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")
    targetsAmazonDeal: bool | None = Field(
        default=None,
        description="If the campaign is targeting an Amazon deal, the value will be true, and the campaign and ad group(s) will be read-only.",
    )


class DSPForecastCampaignOut(LenientModel):
    """Campaign domain model"""

    adProduct: DSPAdProduct | str | None = Field(default=None)
    adomains: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case of rotating creatives. Exchanges can mandate that only one domain is allowed.",
    )
    autoCreationSettings: DSPAutoCreationSettingsOut | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[DSPBudgetOut] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str | None = Field(default=None, description="A unique identifier for a campaign.")
    campaignPresetId: str | None = Field(
        default=None,
        description="This is the ID of the originally generated campaign preset that the campaign is associated with.",
    )
    countries: list[DSPCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the campaign was created.")
    eligibleAutomatedTargetingTactics: list[DSPTacticKeyOut] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are eligible for use with this campaign",
    )
    endDate: date | None = Field(default=None, description="The end date of the campaign.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    fees: list[DSPCampaignFeeOut] | None = Field(
        default=None, min_length=0, max_length=2, description="Any fees associated with the campaign."
    )
    flights: list[DSPCampaignFlightOut] | None = Field(
        default=None, min_length=0, max_length=10, description="Flight details associated with the campaign."
    )
    frequencies: list[DSPFrequencyOut] | None = Field(
        default=None, min_length=0, max_length=10, description="Any frequency caps associated with the campaign."
    )
    globalCampaignId: str | None = Field(
        default=None, description="The global campaign identifier that manages this marketplace campaign."
    )
    ineligibleAutomatedTargetingTactics: list[DSPIneligibleAutomatedTargetingTacticOut] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are ineligible for use with this campaign, along with reasons for ineligibility",
    )
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the campaign was last updated."
    )
    marketplaceConfigurations: list[DSPMarketplaceCampaignConfigurationsOut] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individual marketplace level. For example, if a global campaign is ENABLED and startDate '2024-06-01' but needs to be PAUSED in DE with startDateTime '2024-06-02' marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED, startDate: '2024-06-02'}}]. When a marketplace-specific override is not provided, the campaign's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | str | None = Field(default=None)
    marketplaces: list[DSPMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: DSPCampaignOptimizationsOut | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    productCategoryId: str | None = Field(
        default=None, description="This is the ID of the product category that the campaign is associated with."
    )
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the campaign."
    )
    skanAppId: str | None = Field(
        default=None,
        description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.",
    )
    startDate: date | None = Field(default=None, description="The start date of the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: DSPState | str | None = Field(default=None)
    status: DSPStatusOut | None = Field(default=None)
    tags: list[DSPTagOut] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")
    targetsAmazonDeal: bool | None = Field(
        default=None,
        description="If the campaign is targeting an Amazon deal, the value will be true, and the campaign and ad group(s) will be read-only.",
    )


class DSPForecastFlight(StrictModel):
    budget: DSPForecastFlightBudget
    endDateTime: datetime
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPForecastFlightBudget(StrictModel):
    budgetValue: DSPBudgetValue


class DSPForecastFlightBudgetOut(LenientModel):
    budgetValue: DSPBudgetValueOut


class DSPForecastFlightOut(LenientModel):
    budget: DSPForecastFlightBudgetOut
    endDateTime: datetime
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPForecastInsightsGroup(LenientModel):
    """Insights for leading drivers of forecast results for a specific entity, e.g. campaign frequency cap, line item max bid."""

    coldStartDealNames: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=99,
        description="The names of audience deals attached to the entity, that are newly created and may not be accurately incorporated into the forecast.",
    )
    coldStartSegmentNames: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=99,
        description="The names of audience segments attached to the entity, that are newly created and may not be accurately incorporated into the forecast.",
    )
    displayName: str = Field(
        description="The display name for the entity this insight is for, e.g. campaign/line item display name."
    )
    groupType: DSPRecommendedObjectType | str
    insightsFeatures: list[DSPInsightFeature | str] = Field(
        min_length=1,
        max_length=9,
        description="The features corresponding to this group of insights, e.g. array of line item max bid, campaign frequency cap, etc.",
    )
    tag: str = Field(
        description="The unique identifier for the entity this group of insights refers to, e.g. line item ID, campaign ID, etc."
    )


class DSPForecastMetric(LenientModel):
    """The forecast based on metric and periodicity."""

    metric: DSPSelectedForecastMetric | str
    periodicity: DSPForecastPeriodicity | str | None = Field(default=None)
    value: DSPForecastValue


class DSPForecastMetricsDescription(StrictModel):
    """Describe how user select to see all metrics or selected ones."""

    allMetrics: bool = Field(description="If it is true, all the supported metrics would return.")
    selectedMetrics: list[DSPSelectedForecastMetric] | None = Field(
        default=None, min_length=0, max_length=20, description="The list of selected metrics in order."
    )


class DSPForecastMetricsDescriptionOut(LenientModel):
    """Describe how user select to see all metrics or selected ones."""

    allMetrics: bool = Field(description="If it is true, all the supported metrics would return.")
    selectedMetrics: list[DSPSelectedForecastMetric | str] | None = Field(
        default=None, min_length=0, max_length=20, description="The list of selected metrics in order."
    )


class DSPForecastTarget(StrictModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: DSPAdProduct | None = Field(default=None)
    bid: DSPTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time the target was created.")
    globalTargetId: str | None = Field(
        default=None, description="The global target identifier that manages this marketplace target."
    )
    lastUpdatedDateTime: datetime | None = Field(default=None, description="The date time the target was last updated.")
    marketplaceConfigurations: list[DSPMarketplaceTargetConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual marketplace level. For example, if a global target is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the target's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | None = Field(default=None)
    marketplaces: list[DSPMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    negative: bool | None = Field(default=None, description="Indicates whether the target is negative or not.")
    state: DSPState | None = Field(default=None)
    status: DSPStatus | None = Field(default=None)
    tags: list[DSPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: DSPTargetDetails | None = Field(default=None)
    targetId: str | None = Field(default=None, description="A unique identifier for the target.")
    targetLevel: DSPTargetLevel | None = Field(default=None)
    targetType: DSPTargetType | None = Field(default=None)


class DSPForecastTargetOut(LenientModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: DSPAdProduct | str | None = Field(default=None)
    bid: DSPTargetBidOut | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time the target was created.")
    globalTargetId: str | None = Field(
        default=None, description="The global target identifier that manages this marketplace target."
    )
    lastUpdatedDateTime: datetime | None = Field(default=None, description="The date time the target was last updated.")
    marketplaceConfigurations: list[DSPMarketplaceTargetConfigurationsOut] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual marketplace level. For example, if a global target is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the target's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | str | None = Field(default=None)
    marketplaces: list[DSPMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    negative: bool | None = Field(default=None, description="Indicates whether the target is negative or not.")
    state: DSPState | str | None = Field(default=None)
    status: DSPStatusOut | None = Field(default=None)
    tags: list[DSPTagOut] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: DSPTargetDetailsOut | None = Field(default=None)
    targetId: str | None = Field(default=None, description="A unique identifier for the target.")
    targetLevel: DSPTargetLevel | str | None = Field(default=None)
    targetType: DSPTargetType | str | None = Field(default=None)


class DSPForecastValue(LenientModel):
    high: float
    low: float
    mean: float


class DSPFrequency(StrictModel):
    eventCount: int | None = Field(
        default=None, ge=1, le=500, description="The number of events in a given frequency cap."
    )
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    eventType: DSPEventType | None = Field(default=None)
    extraFrequencyCapImpressionTypes: list[DSPExtraFrequencyCapImpressionType] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Add the additional types of impression to frequency cap. Default to empty list when not selected",
    )
    frequencyTargetingSetting: DSPFrequencyTargetingSetting
    timeCount: int = Field(
        ge=1, le=60, description="The value associated with the time and unit of time for this frequency cap."
    )
    timeUnit: DSPTimeUnit


class DSPFrequencyOut(LenientModel):
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


class DSPGoalSettings(StrictModel):
    currencyCode: DSPCurrencyCode | None = Field(default=None)
    goal: DSPGoal
    kpi: DSPKPI
    kpiValue: float | None = Field(
        default=None, description="The value of the KPI that the campaign is working to optimize."
    )


class DSPGoalSettingsOut(LenientModel):
    currencyCode: DSPCurrencyCode | str | None = Field(default=None)
    goal: DSPGoal | str
    kpi: DSPKPI | str
    kpiValue: float | None = Field(
        default=None, description="The value of the KPI that the campaign is working to optimize."
    )


class DSPIneligibleAutomatedTargetingTactic(StrictModel):
    """Information about an ineligible tactic key and the reasons for ineligibility"""

    reasons: list[DSPIneligibleAutomatedTargetingTacticReason] | None = Field(
        default=None, min_length=0, max_length=10, description="List of reasons why this tactic key is ineligible"
    )
    tacticKey: DSPTacticKey


class DSPIneligibleAutomatedTargetingTacticOut(LenientModel):
    """Information about an ineligible tactic key and the reasons for ineligibility"""

    reasons: list[DSPIneligibleAutomatedTargetingTacticReasonOut] | None = Field(
        default=None, min_length=0, max_length=10, description="List of reasons why this tactic key is ineligible"
    )
    tacticKey: DSPTacticKeyOut


class DSPIneligibleAutomatedTargetingTacticReason(StrictModel):
    """A single reason for tactic type ineligibility"""

    reasonCode: DSPIneligibleAutomatedTargetingTacticReasonCode
    reasonMessage: str = Field(description="Human readable explanation of why this tactic type is ineligible")


class DSPIneligibleAutomatedTargetingTacticReasonOut(LenientModel):
    """A single reason for tactic type ineligibility"""

    reasonCode: DSPIneligibleAutomatedTargetingTacticReasonCode | str
    reasonMessage: str = Field(description="Human readable explanation of why this tactic type is ineligible")


class DSPIntegralAdScienceBrandSafety(StrictModel):
    excludeContent: bool | None = Field(
        default=None, description="Set to true to exclude content that Integral Ad Science is not able to rate."
    )
    iasBrandSafetyAdult: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyAlcohol: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyGambling: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyHateSpeech: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyIllegalDownloads: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyIllegalDrugs: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyOffensiveLanguage: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyViolence: DSPIASBrandSafetyLevelType | None = Field(default=None)


class DSPIntegralAdScienceBrandSafetyOut(LenientModel):
    excludeContent: bool | None = Field(
        default=None, description="Set to true to exclude content that Integral Ad Science is not able to rate."
    )
    iasBrandSafetyAdult: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyAlcohol: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyGambling: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyHateSpeech: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyIllegalDownloads: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyIllegalDrugs: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyOffensiveLanguage: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyViolence: DSPIASBrandSafetyLevelType | str | None = Field(default=None)


class DSPIntegralAdScienceContextualAvoidance(StrictModel):
    avoidanceSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual avoidance segment",
    )


class DSPIntegralAdScienceContextualAvoidanceOut(LenientModel):
    avoidanceSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual avoidance segment",
    )


class DSPIntegralAdScienceContextualTargeting(StrictModel):
    topicalSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual topical targeting segment",
    )
    verticalSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual vertical targeting segment",
    )


class DSPIntegralAdScienceContextualTargetingOut(LenientModel):
    topicalSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual topical targeting segment",
    )
    verticalSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual vertical targeting segment",
    )


class DSPIntegralAdScienceFraudInvalidTraffic(StrictModel):
    targetSetting: DSPIASFraudInvalidTrafficType | None = Field(default=None)


class DSPIntegralAdScienceFraudInvalidTrafficOut(LenientModel):
    targetSetting: DSPIASFraudInvalidTrafficType | str | None = Field(default=None)


class DSPIntegralAdScienceQualitySync(StrictModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPIntegralAdScienceQualitySyncOut(LenientModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPIntegralAdScienceViewability(StrictModel):
    """The IAS viewability standard."""

    standard: DSPIASViewabilityStandardType
    viewabilityTargeting: DSPViewabilityTierType | None = Field(default=None)


class DSPIntegralAdScienceViewabilityOut(LenientModel):
    """The IAS viewability standard."""

    standard: DSPIASViewabilityStandardType | str
    viewabilityTargeting: DSPViewabilityTierType | str | None = Field(default=None)


class DSPInventorySourceTarget(StrictModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPMarketplaceStringValue
    inventorySourceType: DSPInventorySourceType


class DSPInventorySourceTargetOut(LenientModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPMarketplaceStringValueOut
    inventorySourceType: DSPInventorySourceType | str


class DSPKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: DSPKeywordMatchType


class DSPKeywordTargetOut(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: DSPKeywordMatchType | str


class DSPLocationTarget(StrictModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class DSPLocationTargetOut(LenientModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class DSPMarketplaceAdGroupConfigurations(StrictModel):
    pass


class DSPMarketplaceAdGroupConfigurationsOut(LenientModel):
    pass


class DSPMarketplaceCampaignConfigurations(StrictModel):
    pass


class DSPMarketplaceCampaignConfigurationsOut(LenientModel):
    pass


class DSPMarketplaceTargetConfigurations(StrictModel):
    pass


class DSPMarketplaceTargetConfigurationsOut(LenientModel):
    pass


class DSPMonetaryBudget(StrictModel):
    currencyCode: DSPCurrencyCode
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPMonetaryBudgetValue(StrictModel):
    monetaryBudget: DSPMonetaryBudget | None = Field(default=None)


class DSPMonetaryBudgetValueOut(LenientModel):
    monetaryBudget: DSPMonetaryBudgetOut | None = Field(default=None)


class DSPNativeContentPositionTarget(StrictModel):
    """Targets ads to a specific native content position"""

    nativePosition: DSPNativeContentPosition


class DSPNativeContentPositionTargetOut(LenientModel):
    """Targets ads to a specific native content position"""

    nativePosition: DSPNativeContentPosition | str


class DSPNewsGuardBrandGuardMisinformationSafety(StrictModel):
    avoidanceList: list[DSPNewsGuardBrandGuardMisinformationSafetyType] | None = Field(
        default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets"
    )


class DSPNewsGuardBrandGuardMisinformationSafetyOut(LenientModel):
    avoidanceList: list[DSPNewsGuardBrandGuardMisinformationSafetyType | str] | None = Field(
        default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets"
    )


class DSPNewsGuardBrandGuardTrustedNewsTargeting(StrictModel):
    """Only applicable for Web supply."""

    targetingList: list[DSPNewsGuardBrandGuardTrustedNewsTargetingType] | None = Field(
        default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets"
    )


class DSPNewsGuardBrandGuardTrustedNewsTargetingOut(LenientModel):
    """Only applicable for Web supply."""

    targetingList: list[DSPNewsGuardBrandGuardTrustedNewsTargetingType | str] | None = Field(
        default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets"
    )


class DSPOptimization(StrictModel):
    bidStrategy: DSPBidStrategy
    budgetSettings: DSPAdGroupBudgetSettings | None = Field(default=None)


class DSPOptimizationOut(LenientModel):
    bidStrategy: DSPBidStrategy | str
    budgetSettings: DSPAdGroupBudgetSettingsOut | None = Field(default=None)


class DSPPacing(StrictModel):
    deliveryProfile: DSPDeliveryProfile


class DSPPacingOut(LenientModel):
    deliveryProfile: DSPDeliveryProfile | str


class DSPPixalateFraudInvalidTraffic(StrictModel):
    excludeAppsAndDomains: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from Apps and Domains identified to be fraudulent or invalid.",
    )
    excludeIpAddressAndUserAgents: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from IPV4 and IPV6 addresses and user agents identified to be fraudulent or invalid.",
    )
    excludeOttAndMobileDevices: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from OTT and Mobile devices identified to be fraudulent or invalid.",
    )
    excludeRemovedAppsFromAppStores: bool | None = Field(
        default=None,
        description="Set to true to exlude traffic from Apps that have been removed from the google play and apple app stores in the last 6 months.",
    )


class DSPPixalateFraudInvalidTrafficOut(LenientModel):
    excludeAppsAndDomains: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from Apps and Domains identified to be fraudulent or invalid.",
    )
    excludeIpAddressAndUserAgents: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from IPV4 and IPV6 addresses and user agents identified to be fraudulent or invalid.",
    )
    excludeOttAndMobileDevices: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from OTT and Mobile devices identified to be fraudulent or invalid.",
    )
    excludeRemovedAppsFromAppStores: bool | None = Field(
        default=None,
        description="Set to true to exlude traffic from Apps that have been removed from the google play and apple app stores in the last 6 months.",
    )


class DSPPlacementTypeTarget(StrictModel):
    """Target based on the placement type."""

    placementType: DSPPlacementType


class DSPPlacementTypeTargetOut(LenientModel):
    """Target based on the placement type."""

    placementType: DSPPlacementType | str


class DSPPoint(LenientModel):
    pointType: str | None = Field(default=None)
    x: DSPXPoint
    y: list[DSPYPoint] | None = Field(default=None, min_length=0, max_length=1000)


class DSPProductCategoryRefinement(StrictModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPProductCategoryRefinementOut(LenientModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPProductCategoryRefinementValue(StrictModel):
    productCategoryRefinement: DSPProductCategoryRefinement | None = Field(default=None)


class DSPProductCategoryRefinementValueOut(LenientModel):
    productCategoryRefinement: DSPProductCategoryRefinementOut | None = Field(default=None)


class DSPProductCategoryTarget(StrictModel):
    """Targets a specific customer search term."""

    matchType: DSPProductCategoryMatchType | None = Field(default=None)
    productCategoryRefinement: DSPProductCategoryRefinementValue


class DSPProductCategoryTargetOut(LenientModel):
    """Targets a specific customer search term."""

    matchType: DSPProductCategoryMatchType | str | None = Field(default=None)
    productCategoryRefinement: DSPProductCategoryRefinementValueOut


class DSPProductMarketplaceSetting(StrictModel):
    marketplace: DSPMarketplace
    productId: str = Field(description="The product id applicable at the specified marketplace.")


class DSPProductMarketplaceSettingOut(LenientModel):
    marketplace: DSPMarketplace | str
    productId: str = Field(description="The product id applicable at the specified marketplace.")


class DSPProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: DSPProductMatchType
    product: DSPProductValue
    productIdType: DSPProductIdType


class DSPProductTargetOut(LenientModel):
    """Targets a specific product."""

    matchType: DSPProductMatchType | str
    product: DSPProductValueOut
    productIdType: DSPProductIdType | str


class DSPProductValue(StrictModel):
    marketplaceSettings: list[DSPProductMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The product ids at specific marketplace level. Either the product id or the marketplace settings should always be specified",
    )
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class DSPProductValueOut(LenientModel):
    marketplaceSettings: list[DSPProductMarketplaceSettingOut] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The product ids at specific marketplace level. Either the product id or the marketplace settings should always be specified",
    )
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class DSPReplanning(LenientModel):
    """Recommendation for replanning."""

    content: str
    curves: list[DSPCurve] | None = Field(default=None, min_length=0, max_length=4)
    deliverInFullConfidence: DSPDeliverInFullConfidence | None = Field(default=None)
    metrics: list[DSPForecastMetric] | None = Field(default=None, min_length=0, max_length=20)
    scenarioFlight: DSPForecastFlightOut | None = Field(default=None)
    scenarioType: str | None = Field(default=None)
    selectedMetrics: list[DSPSelectedForecastMetric | str] | None = Field(default=None, min_length=0, max_length=20)
    title: str


class DSPReplanningSettings(StrictModel):
    """Forecast request of a campaign, adGroups, flights, and targets with adjusted settings."""

    adGroups: list[DSPForecastAdGroup] | None = Field(default=None, min_length=0, max_length=50)
    campaign: DSPForecastCampaign | None = Field(default=None)
    flights: list[DSPForecastFlight] | None = Field(default=None, min_length=0, max_length=5)
    tags: list[DSPTag] | None = Field(default=None, min_length=0, max_length=49)
    targets: list[DSPForecastTarget] | None = Field(default=None, min_length=0, max_length=1000)


class DSPReplanningSettingsOut(LenientModel):
    """Forecast request of a campaign, adGroups, flights, and targets with adjusted settings."""

    adGroups: list[DSPForecastAdGroupOut] | None = Field(default=None, min_length=0, max_length=50)
    campaign: DSPForecastCampaignOut | None = Field(default=None)
    flights: list[DSPForecastFlightOut] | None = Field(default=None, min_length=0, max_length=5)
    tags: list[DSPTagOut] | None = Field(default=None, min_length=0, max_length=49)
    targets: list[DSPForecastTargetOut] | None = Field(default=None, min_length=0, max_length=1000)


class DSPRetrieveCampaignForecastRequest(StrictModel):
    campaignForecastDescriptions: list[DSPCampaignForecastDescription] = Field(min_length=1, max_length=1)


class DSPStatus(StrictModel):
    deliveryReasons: list[DSPDeliveryReason] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: DSPDeliveryStatus


class DSPStatusOut(LenientModel):
    deliveryReasons: list[DSPDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: DSPDeliveryStatus | str


class DSPTacticKey(StrictModel):
    """A tactic type paired with its compatible inventory type"""

    primaryInventoryType: DSPPrimaryInventoryType
    tacticType: DSPAutomatedTargetingTactic


class DSPTacticKeyOut(LenientModel):
    """A tactic type paired with its compatible inventory type"""

    primaryInventoryType: DSPPrimaryInventoryType | str
    tacticType: DSPAutomatedTargetingTactic | str


class DSPTag(StrictModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPTagOut(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPTargetBid(StrictModel):
    pass


class DSPTargetBidOut(LenientModel):
    pass


class DSPTargetDetailsAdInitiationTarget(StrictModel):
    adInitiationTarget: DSPAdInitiationTarget


class DSPTargetDetailsAdPlayerSizeTarget(StrictModel):
    adPlayerSizeTarget: DSPAdPlayerSizeTarget


class DSPTargetDetailsAppTarget(StrictModel):
    appTarget: DSPAppTarget


class DSPTargetDetailsAudienceTarget(StrictModel):
    audienceTarget: DSPAudienceTarget


class DSPTargetDetailsBrandSafetyCategoryTarget(StrictModel):
    brandSafetyCategoryTarget: DSPBrandSafetyCategoryTarget


class DSPTargetDetailsBrandSafetyTierTarget(StrictModel):
    brandSafetyTierTarget: DSPBrandSafetyTierTarget


class DSPTargetDetailsContentCategoryTarget(StrictModel):
    contentCategoryTarget: DSPContentCategoryTarget


class DSPTargetDetailsContentGenreTarget(StrictModel):
    contentGenreTarget: DSPContentGenreTarget


class DSPTargetDetailsContentInstreamPositionTarget(StrictModel):
    contentInstreamPositionTarget: DSPContentInstreamPositionTarget


class DSPTargetDetailsContentOutstreamPositionTarget(StrictModel):
    contentOutstreamPositionTarget: DSPContentOutstreamPositionTarget


class DSPTargetDetailsContentRatingTarget(StrictModel):
    contentRatingTarget: DSPContentRatingTarget


class DSPTargetDetailsDayPartTarget(StrictModel):
    dayPartTarget: DSPDayPartTarget


class DSPTargetDetailsDeviceTarget(StrictModel):
    deviceTarget: DSPDeviceTarget


class DSPTargetDetailsDomainTarget(StrictModel):
    domainTarget: DSPDomainTarget


class DSPTargetDetailsFoldPositionTarget(StrictModel):
    foldPositionTarget: DSPFoldPositionTarget


class DSPTargetDetailsInventorySourceTarget(StrictModel):
    inventorySourceTarget: DSPInventorySourceTarget


class DSPTargetDetailsKeywordTarget(StrictModel):
    keywordTarget: DSPKeywordTarget


class DSPTargetDetailsLocationTarget(StrictModel):
    locationTarget: DSPLocationTarget


class DSPTargetDetailsNativeContentPositionTarget(StrictModel):
    nativeContentPositionTarget: DSPNativeContentPositionTarget


class DSPTargetDetailsPlacementTypeTarget(StrictModel):
    placementTypeTarget: DSPPlacementTypeTarget


class DSPTargetDetailsProductCategoryTarget(StrictModel):
    productCategoryTarget: DSPProductCategoryTarget


class DSPTargetDetailsProductTarget(StrictModel):
    productTarget: DSPProductTarget


class DSPTargetDetailsThemeTarget(StrictModel):
    themeTarget: DSPThemeTarget


class DSPTargetDetailsThirdPartyTarget(StrictModel):
    thirdPartyTarget: DSPThirdPartyTarget


class DSPTargetDetailsVideoAdFormatTarget(StrictModel):
    videoAdFormatTarget: DSPVideoAdFormatTarget


class DSPTargetDetailsVideoContentDurationTarget(StrictModel):
    videoContentDurationTarget: DSPVideoContentDurationTarget


type DSPTargetDetails = DSPTargetDetailsAdInitiationTarget | DSPTargetDetailsAdPlayerSizeTarget | DSPTargetDetailsAppTarget | DSPTargetDetailsAudienceTarget | DSPTargetDetailsBrandSafetyCategoryTarget | DSPTargetDetailsBrandSafetyTierTarget | DSPTargetDetailsContentCategoryTarget | DSPTargetDetailsContentGenreTarget | DSPTargetDetailsContentInstreamPositionTarget | DSPTargetDetailsContentOutstreamPositionTarget | DSPTargetDetailsContentRatingTarget | DSPTargetDetailsDayPartTarget | DSPTargetDetailsDeviceTarget | DSPTargetDetailsDomainTarget | DSPTargetDetailsFoldPositionTarget | DSPTargetDetailsInventorySourceTarget | DSPTargetDetailsKeywordTarget | DSPTargetDetailsLocationTarget | DSPTargetDetailsNativeContentPositionTarget | DSPTargetDetailsPlacementTypeTarget | DSPTargetDetailsProductCategoryTarget | DSPTargetDetailsProductTarget | DSPTargetDetailsThemeTarget | DSPTargetDetailsThirdPartyTarget | DSPTargetDetailsVideoAdFormatTarget | DSPTargetDetailsVideoContentDurationTarget


class DSPTargetDetailsOutAdInitiationTarget(LenientModel):
    adInitiationTarget: DSPAdInitiationTargetOut


class DSPTargetDetailsOutAdPlayerSizeTarget(LenientModel):
    adPlayerSizeTarget: DSPAdPlayerSizeTargetOut


class DSPTargetDetailsOutAppTarget(LenientModel):
    appTarget: DSPAppTargetOut


class DSPTargetDetailsOutAudienceTarget(LenientModel):
    audienceTarget: DSPAudienceTargetOut


class DSPTargetDetailsOutBrandSafetyCategoryTarget(LenientModel):
    brandSafetyCategoryTarget: DSPBrandSafetyCategoryTargetOut


class DSPTargetDetailsOutBrandSafetyTierTarget(LenientModel):
    brandSafetyTierTarget: DSPBrandSafetyTierTargetOut


class DSPTargetDetailsOutContentCategoryTarget(LenientModel):
    contentCategoryTarget: DSPContentCategoryTargetOut


class DSPTargetDetailsOutContentGenreTarget(LenientModel):
    contentGenreTarget: DSPContentGenreTargetOut


class DSPTargetDetailsOutContentInstreamPositionTarget(LenientModel):
    contentInstreamPositionTarget: DSPContentInstreamPositionTargetOut


class DSPTargetDetailsOutContentOutstreamPositionTarget(LenientModel):
    contentOutstreamPositionTarget: DSPContentOutstreamPositionTargetOut


class DSPTargetDetailsOutContentRatingTarget(LenientModel):
    contentRatingTarget: DSPContentRatingTargetOut


class DSPTargetDetailsOutDayPartTarget(LenientModel):
    dayPartTarget: DSPDayPartTargetOut


class DSPTargetDetailsOutDeviceTarget(LenientModel):
    deviceTarget: DSPDeviceTargetOut


class DSPTargetDetailsOutDomainTarget(LenientModel):
    domainTarget: DSPDomainTargetOut


class DSPTargetDetailsOutFoldPositionTarget(LenientModel):
    foldPositionTarget: DSPFoldPositionTargetOut


class DSPTargetDetailsOutInventorySourceTarget(LenientModel):
    inventorySourceTarget: DSPInventorySourceTargetOut


class DSPTargetDetailsOutKeywordTarget(LenientModel):
    keywordTarget: DSPKeywordTargetOut


class DSPTargetDetailsOutLocationTarget(LenientModel):
    locationTarget: DSPLocationTargetOut


class DSPTargetDetailsOutNativeContentPositionTarget(LenientModel):
    nativeContentPositionTarget: DSPNativeContentPositionTargetOut


class DSPTargetDetailsOutPlacementTypeTarget(LenientModel):
    placementTypeTarget: DSPPlacementTypeTargetOut


class DSPTargetDetailsOutProductCategoryTarget(LenientModel):
    productCategoryTarget: DSPProductCategoryTargetOut


class DSPTargetDetailsOutProductTarget(LenientModel):
    productTarget: DSPProductTargetOut


class DSPTargetDetailsOutThemeTarget(LenientModel):
    themeTarget: DSPThemeTargetOut


class DSPTargetDetailsOutThirdPartyTarget(LenientModel):
    thirdPartyTarget: DSPThirdPartyTargetOut


class DSPTargetDetailsOutVideoAdFormatTarget(LenientModel):
    videoAdFormatTarget: DSPVideoAdFormatTargetOut


class DSPTargetDetailsOutVideoContentDurationTarget(LenientModel):
    videoContentDurationTarget: DSPVideoContentDurationTargetOut


type DSPTargetDetailsOut = DSPTargetDetailsOutAdInitiationTarget | DSPTargetDetailsOutAdPlayerSizeTarget | DSPTargetDetailsOutAppTarget | DSPTargetDetailsOutAudienceTarget | DSPTargetDetailsOutBrandSafetyCategoryTarget | DSPTargetDetailsOutBrandSafetyTierTarget | DSPTargetDetailsOutContentCategoryTarget | DSPTargetDetailsOutContentGenreTarget | DSPTargetDetailsOutContentInstreamPositionTarget | DSPTargetDetailsOutContentOutstreamPositionTarget | DSPTargetDetailsOutContentRatingTarget | DSPTargetDetailsOutDayPartTarget | DSPTargetDetailsOutDeviceTarget | DSPTargetDetailsOutDomainTarget | DSPTargetDetailsOutFoldPositionTarget | DSPTargetDetailsOutInventorySourceTarget | DSPTargetDetailsOutKeywordTarget | DSPTargetDetailsOutLocationTarget | DSPTargetDetailsOutNativeContentPositionTarget | DSPTargetDetailsOutPlacementTypeTarget | DSPTargetDetailsOutProductCategoryTarget | DSPTargetDetailsOutProductTarget | DSPTargetDetailsOutThemeTarget | DSPTargetDetailsOutThirdPartyTarget | DSPTargetDetailsOutVideoAdFormatTarget | DSPTargetDetailsOutVideoContentDurationTarget


class DSPTargetingSettings(StrictModel):
    amazonViewability: DSPAmazonViewability
    automatedTargetingTactic: DSPAutomatedTargetingTactic | None = Field(default=None)
    defaultAudienceTargetingMatchType: DSPDefaultAudienceTargetingMatchType | None = Field(default=None)
    enableLanguageTargeting: bool | None = Field(
        default=None,
        description="If set to true, creatives will only target supply where the content language matches the creative language.",
    )
    siteLanguage: DSPSiteLanguage | None = Field(default=None)
    tacticsConvertersExclusionType: DSPTacticsConvertersExclusionType | None = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed deal, the deal can be provided here.",
    )
    timeZoneType: DSPTimeZoneType
    userLocationSignal: DSPUserLocationSignal
    videoCompletionTier: DSPVideoCompletionTier | None = Field(default=None)


class DSPTargetingSettingsOut(LenientModel):
    amazonViewability: DSPAmazonViewabilityOut
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


class DSPThemeTarget(StrictModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: DSPThemeMatchType


class DSPThemeTargetOut(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: DSPThemeMatchType | str


class DSPThirdPartyTarget(StrictModel):
    thirdPartyTargetDetails: DSPThirdPartyTargetDetails
    thirdPartyTargetType: DSPThirdPartyTargetType


class DSPThirdPartyTargetDetailsDoubleVerifyAuthenticAttention(StrictModel):
    doubleVerifyAuthenticAttention: DSPDoubleVerifyAuthenticAttention


class DSPThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety(StrictModel):
    doubleVerifyAuthenticBrandSafety: DSPDoubleVerifyAuthenticBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyBrandSafety(StrictModel):
    doubleVerifyBrandSafety: DSPDoubleVerifyBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId(StrictModel):
    doubleVerifyCustomContextualSegmentId: DSPDoubleVerifyCustomContextualSegmentId


class DSPThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic(StrictModel):
    doubleVerifyFraudInvalidTraffic: DSPDoubleVerifyFraudInvalidTraffic


class DSPThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety(StrictModel):
    doubleVerifyStandardDisplayBrandSafety: DSPDoubleVerifyStandardDisplayBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyViewability(StrictModel):
    doubleVerifyViewability: DSPDoubleVerifyViewability


class DSPThirdPartyTargetDetailsIntegralAdScienceBrandSafety(StrictModel):
    integralAdScienceBrandSafety: DSPIntegralAdScienceBrandSafety


class DSPThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance(StrictModel):
    integralAdScienceContextualAvoidance: DSPIntegralAdScienceContextualAvoidance


class DSPThirdPartyTargetDetailsIntegralAdScienceContextualTargeting(StrictModel):
    integralAdScienceContextualTargeting: DSPIntegralAdScienceContextualTargeting


class DSPThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic(StrictModel):
    integralAdScienceFraudInvalidTraffic: DSPIntegralAdScienceFraudInvalidTraffic


class DSPThirdPartyTargetDetailsIntegralAdScienceQualitySync(StrictModel):
    integralAdScienceQualitySync: DSPIntegralAdScienceQualitySync


class DSPThirdPartyTargetDetailsIntegralAdScienceViewability(StrictModel):
    integralAdScienceViewability: DSPIntegralAdScienceViewability


class DSPThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety(StrictModel):
    newsGuardBrandGuardMisinformationSafety: DSPNewsGuardBrandGuardMisinformationSafety


class DSPThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting(StrictModel):
    newsGuardBrandGuardTrustedNewsTargeting: DSPNewsGuardBrandGuardTrustedNewsTargeting


class DSPThirdPartyTargetDetailsPixalateFraudInvalidTraffic(StrictModel):
    pixalateFraudInvalidTraffic: DSPPixalateFraudInvalidTraffic


type DSPThirdPartyTargetDetails = DSPThirdPartyTargetDetailsDoubleVerifyAuthenticAttention | DSPThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId | DSPThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic | DSPThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyViewability | DSPThirdPartyTargetDetailsIntegralAdScienceBrandSafety | DSPThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance | DSPThirdPartyTargetDetailsIntegralAdScienceContextualTargeting | DSPThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic | DSPThirdPartyTargetDetailsIntegralAdScienceQualitySync | DSPThirdPartyTargetDetailsIntegralAdScienceViewability | DSPThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety | DSPThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting | DSPThirdPartyTargetDetailsPixalateFraudInvalidTraffic


class DSPThirdPartyTargetDetailsOutDoubleVerifyAuthenticAttention(LenientModel):
    doubleVerifyAuthenticAttention: DSPDoubleVerifyAuthenticAttentionOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyAuthenticBrandSafety(LenientModel):
    doubleVerifyAuthenticBrandSafety: DSPDoubleVerifyAuthenticBrandSafetyOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyBrandSafety(LenientModel):
    doubleVerifyBrandSafety: DSPDoubleVerifyBrandSafetyOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyCustomContextualSegmentId(LenientModel):
    doubleVerifyCustomContextualSegmentId: DSPDoubleVerifyCustomContextualSegmentIdOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyFraudInvalidTraffic(LenientModel):
    doubleVerifyFraudInvalidTraffic: DSPDoubleVerifyFraudInvalidTrafficOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyStandardDisplayBrandSafety(LenientModel):
    doubleVerifyStandardDisplayBrandSafety: DSPDoubleVerifyStandardDisplayBrandSafetyOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyViewability(LenientModel):
    doubleVerifyViewability: DSPDoubleVerifyViewabilityOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceBrandSafety(LenientModel):
    integralAdScienceBrandSafety: DSPIntegralAdScienceBrandSafetyOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceContextualAvoidance(LenientModel):
    integralAdScienceContextualAvoidance: DSPIntegralAdScienceContextualAvoidanceOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceContextualTargeting(LenientModel):
    integralAdScienceContextualTargeting: DSPIntegralAdScienceContextualTargetingOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceFraudInvalidTraffic(LenientModel):
    integralAdScienceFraudInvalidTraffic: DSPIntegralAdScienceFraudInvalidTrafficOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceQualitySync(LenientModel):
    integralAdScienceQualitySync: DSPIntegralAdScienceQualitySyncOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceViewability(LenientModel):
    integralAdScienceViewability: DSPIntegralAdScienceViewabilityOut


class DSPThirdPartyTargetDetailsOutNewsGuardBrandGuardMisinformationSafety(LenientModel):
    newsGuardBrandGuardMisinformationSafety: DSPNewsGuardBrandGuardMisinformationSafetyOut


class DSPThirdPartyTargetDetailsOutNewsGuardBrandGuardTrustedNewsTargeting(LenientModel):
    newsGuardBrandGuardTrustedNewsTargeting: DSPNewsGuardBrandGuardTrustedNewsTargetingOut


class DSPThirdPartyTargetDetailsOutPixalateFraudInvalidTraffic(LenientModel):
    pixalateFraudInvalidTraffic: DSPPixalateFraudInvalidTrafficOut


type DSPThirdPartyTargetDetailsOut = DSPThirdPartyTargetDetailsOutDoubleVerifyAuthenticAttention | DSPThirdPartyTargetDetailsOutDoubleVerifyAuthenticBrandSafety | DSPThirdPartyTargetDetailsOutDoubleVerifyBrandSafety | DSPThirdPartyTargetDetailsOutDoubleVerifyCustomContextualSegmentId | DSPThirdPartyTargetDetailsOutDoubleVerifyFraudInvalidTraffic | DSPThirdPartyTargetDetailsOutDoubleVerifyStandardDisplayBrandSafety | DSPThirdPartyTargetDetailsOutDoubleVerifyViewability | DSPThirdPartyTargetDetailsOutIntegralAdScienceBrandSafety | DSPThirdPartyTargetDetailsOutIntegralAdScienceContextualAvoidance | DSPThirdPartyTargetDetailsOutIntegralAdScienceContextualTargeting | DSPThirdPartyTargetDetailsOutIntegralAdScienceFraudInvalidTraffic | DSPThirdPartyTargetDetailsOutIntegralAdScienceQualitySync | DSPThirdPartyTargetDetailsOutIntegralAdScienceViewability | DSPThirdPartyTargetDetailsOutNewsGuardBrandGuardMisinformationSafety | DSPThirdPartyTargetDetailsOutNewsGuardBrandGuardTrustedNewsTargeting | DSPThirdPartyTargetDetailsOutPixalateFraudInvalidTraffic


class DSPThirdPartyTargetOut(LenientModel):
    thirdPartyTargetDetails: DSPThirdPartyTargetDetailsOut
    thirdPartyTargetType: DSPThirdPartyTargetType | str


class DSPTimeOfDay(StrictModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPTwitchContentRating(StrictModel):
    twitchContentRating: DSPTwitchContentRatingEnum


class DSPTwitchContentRatingOut(LenientModel):
    twitchContentRating: DSPTwitchContentRatingEnum | str


class DSPVideoAdFormatTarget(StrictModel):
    """Target based on the video ad format."""

    videoAdFormat: DSPVideoAdFormat


class DSPVideoAdFormatTargetOut(LenientModel):
    """Target based on the video ad format."""

    videoAdFormat: DSPVideoAdFormat | str


class DSPVideoContentDurationTarget(StrictModel):
    """Targets ads to a specific video content duration"""

    duration: DSPVideoContentDuration


class DSPVideoContentDurationTargetOut(LenientModel):
    """Targets ads to a specific video content duration"""

    duration: DSPVideoContentDuration | str


class DSPWarning(LenientModel):
    """The warning message of a forecast."""

    adGroupIds: list[str] | None = Field(default=None, min_length=0, max_length=50)
    code: str
    message: str
    messageParameters: list[str] | None = Field(default=None, min_length=0, max_length=50)
    warningLevel: int | None = Field(default=None)


class DSPXPoint(LenientModel):
    """The label and value on X axis of the curve."""

    label: DSPPointLabel | str
    value: float


class DSPYPoint(LenientModel):
    """The label and value on Y axis of the curve."""

    label: DSPPointLabel | str
    value: DSPForecastValue


__all__ = [
    "DSPAcrossGroupOperator",
    "DSPAdGroupBid",
    "DSPAdGroupBidOut",
    "DSPAdGroupBudgetSettings",
    "DSPAdGroupBudgetSettingsOut",
    "DSPAdInitiationTarget",
    "DSPAdInitiationTargetOut",
    "DSPAdPlayerSize",
    "DSPAdPlayerSizeTarget",
    "DSPAdPlayerSizeTargetOut",
    "DSPAdProduct",
    "DSPAdvertiserDomainList",
    "DSPAdvertiserDomainListOut",
    "DSPAmazonViewability",
    "DSPAmazonViewabilityOut",
    "DSPAppTarget",
    "DSPAppTargetOut",
    "DSPAppType",
    "DSPAudienceTarget",
    "DSPAudienceTargetOut",
    "DSPAutoCreationSettings",
    "DSPAutoCreationSettingsOut",
    "DSPAutomatedTargetingTactic",
    "DSPAverageCompletionAndFullyViewableRateTargetingType",
    "DSPBidSettings",
    "DSPBidSettingsOut",
    "DSPBidStrategy",
    "DSPBrandExposureViewabilityTargetingType",
    "DSPBrandSafetyCategory",
    "DSPBrandSafetyCategoryTarget",
    "DSPBrandSafetyCategoryTargetOut",
    "DSPBrandSafetyTier",
    "DSPBrandSafetyTierTarget",
    "DSPBrandSafetyTierTargetOut",
    "DSPBrandSuitabilityRiskLevelType",
    "DSPBudget",
    "DSPBudgetAllocation",
    "DSPBudgetOut",
    "DSPBudgetSettings",
    "DSPBudgetSettingsOut",
    "DSPBudgetType",
    "DSPBudgetValue",
    "DSPBudgetValueOut",
    "DSPCampaignFee",
    "DSPCampaignFeeOut",
    "DSPCampaignFeeType",
    "DSPCampaignFeeValueType",
    "DSPCampaignFlight",
    "DSPCampaignFlightOut",
    "DSPCampaignForecast",
    "DSPCampaignForecastDescription",
    "DSPCampaignForecastDescriptionOut",
    "DSPCampaignForecastMultiStatusResponse",
    "DSPCampaignForecastMultiStatusSuccess",
    "DSPCampaignOptimizations",
    "DSPCampaignOptimizationsOut",
    "DSPContentCategoryTarget",
    "DSPContentCategoryTargetOut",
    "DSPContentGenre",
    "DSPContentGenreTarget",
    "DSPContentGenreTargetOut",
    "DSPContentInstreamPosition",
    "DSPContentInstreamPositionTarget",
    "DSPContentInstreamPositionTargetOut",
    "DSPContentOutstreamPosition",
    "DSPContentOutstreamPositionTarget",
    "DSPContentOutstreamPositionTargetOut",
    "DSPContentRating",
    "DSPContentRatingOut",
    "DSPContentRatingTarget",
    "DSPContentRatingTargetOut",
    "DSPContentRatingTypes",
    "DSPCountryCode",
    "DSPCreativeRotationType",
    "DSPCurrencyCode",
    "DSPCurve",
    "DSPDVBrandSafetyAppAgeRatingType",
    "DSPDVBrandSafetyAppStarRatingType",
    "DSPDVBrandSafetyContentCategoriesWithRiskMap",
    "DSPDVBrandSafetyContentCategoriesWithRiskMapOut",
    "DSPDVBrandSafetyContentCategoryType",
    "DSPDayOfWeek",
    "DSPDayPartTarget",
    "DSPDayPartTargetOut",
    "DSPDefaultAudienceTargetingMatchType",
    "DSPDeliverInFullConfidence",
    "DSPDeliverInFullConfidenceLevel",
    "DSPDeliveryProfile",
    "DSPDeliveryReason",
    "DSPDeliveryStatus",
    "DSPDeviceOrientation",
    "DSPDeviceTarget",
    "DSPDeviceTargetOut",
    "DSPDeviceType",
    "DSPDomainFileTarget",
    "DSPDomainFileTargetOut",
    "DSPDomainListTarget",
    "DSPDomainListTargetOut",
    "DSPDomainNameTarget",
    "DSPDomainNameTargetOut",
    "DSPDomainTarget",
    "DSPDomainTargetDetails",
    "DSPDomainTargetDetailsOut",
    "DSPDomainTargetOut",
    "DSPDomainTargetTypes",
    "DSPDoubleVerifyAuthenticAttention",
    "DSPDoubleVerifyAuthenticAttentionOut",
    "DSPDoubleVerifyAuthenticBrandSafety",
    "DSPDoubleVerifyAuthenticBrandSafetyOut",
    "DSPDoubleVerifyBrandSafety",
    "DSPDoubleVerifyBrandSafetyOut",
    "DSPDoubleVerifyCustomContextualSegmentId",
    "DSPDoubleVerifyCustomContextualSegmentIdOut",
    "DSPDoubleVerifyFraudInvalidTraffic",
    "DSPDoubleVerifyFraudInvalidTrafficOut",
    "DSPDoubleVerifyStandardDisplayBrandSafety",
    "DSPDoubleVerifyStandardDisplayBrandSafetyOut",
    "DSPDoubleVerifyViewability",
    "DSPDoubleVerifyViewabilityOut",
    "DSPDspContentRating",
    "DSPDspContentRatingEnum",
    "DSPDspContentRatingOut",
    "DSPEnabledFeaturesInCampaignForecast",
    "DSPEnabledFeaturesInCampaignForecastOut",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPEventType",
    "DSPExcludeAppsAndSitesType",
    "DSPExtraFrequencyCapImpressionType",
    "DSPFee",
    "DSPFeeOut",
    "DSPFeeType",
    "DSPFeeValueType",
    "DSPFeesThirdPartyProvider",
    "DSPFlightBudget",
    "DSPFlightBudgetOut",
    "DSPFlightForecast",
    "DSPFlightForecastInsights",
    "DSPFoldPosition",
    "DSPFoldPositionTarget",
    "DSPFoldPositionTargetOut",
    "DSPForecastAdGroup",
    "DSPForecastAdGroupOut",
    "DSPForecastCampaign",
    "DSPForecastCampaignOut",
    "DSPForecastFlight",
    "DSPForecastFlightBudget",
    "DSPForecastFlightBudgetOut",
    "DSPForecastFlightOut",
    "DSPForecastInsightsGroup",
    "DSPForecastMetric",
    "DSPForecastMetricsDescription",
    "DSPForecastMetricsDescriptionOut",
    "DSPForecastPeriodicity",
    "DSPForecastTarget",
    "DSPForecastTargetOut",
    "DSPForecastValue",
    "DSPFrequency",
    "DSPFrequencyOut",
    "DSPFrequencyTargetingSetting",
    "DSPGoal",
    "DSPGoalSettings",
    "DSPGoalSettingsOut",
    "DSPIASBrandSafetyLevelType",
    "DSPIASFraudInvalidTrafficType",
    "DSPIASViewabilityStandardType",
    "DSPInGroupOperator",
    "DSPIneligibleAutomatedTargetingTactic",
    "DSPIneligibleAutomatedTargetingTacticOut",
    "DSPIneligibleAutomatedTargetingTacticReason",
    "DSPIneligibleAutomatedTargetingTacticReasonCode",
    "DSPIneligibleAutomatedTargetingTacticReasonOut",
    "DSPInsightFeature",
    "DSPIntegralAdScienceBrandSafety",
    "DSPIntegralAdScienceBrandSafetyOut",
    "DSPIntegralAdScienceContextualAvoidance",
    "DSPIntegralAdScienceContextualAvoidanceOut",
    "DSPIntegralAdScienceContextualTargeting",
    "DSPIntegralAdScienceContextualTargetingOut",
    "DSPIntegralAdScienceFraudInvalidTraffic",
    "DSPIntegralAdScienceFraudInvalidTrafficOut",
    "DSPIntegralAdScienceQualitySync",
    "DSPIntegralAdScienceQualitySyncOut",
    "DSPIntegralAdScienceViewability",
    "DSPIntegralAdScienceViewabilityOut",
    "DSPInventorySourceTarget",
    "DSPInventorySourceTargetOut",
    "DSPInventorySourceType",
    "DSPInventoryType",
    "DSPKPI",
    "DSPKeywordMatchType",
    "DSPKeywordTarget",
    "DSPKeywordTargetOut",
    "DSPLocationTarget",
    "DSPLocationTargetOut",
    "DSPMarketplace",
    "DSPMarketplaceAdGroupConfigurations",
    "DSPMarketplaceAdGroupConfigurationsOut",
    "DSPMarketplaceCampaignConfigurations",
    "DSPMarketplaceCampaignConfigurationsOut",
    "DSPMarketplaceScope",
    "DSPMarketplaceStringValue",
    "DSPMarketplaceStringValueOut",
    "DSPMarketplaceTargetConfigurations",
    "DSPMarketplaceTargetConfigurationsOut",
    "DSPMobileDevice",
    "DSPMobileEnvironment",
    "DSPMobileOs",
    "DSPMonetaryBudget",
    "DSPMonetaryBudgetOut",
    "DSPMonetaryBudgetValue",
    "DSPMonetaryBudgetValueOut",
    "DSPMrcViewabilityTargetingType",
    "DSPNativeContentPosition",
    "DSPNativeContentPositionTarget",
    "DSPNativeContentPositionTargetOut",
    "DSPNewsGuardBrandGuardMisinformationSafety",
    "DSPNewsGuardBrandGuardMisinformationSafetyOut",
    "DSPNewsGuardBrandGuardMisinformationSafetyType",
    "DSPNewsGuardBrandGuardTrustedNewsTargeting",
    "DSPNewsGuardBrandGuardTrustedNewsTargetingOut",
    "DSPNewsGuardBrandGuardTrustedNewsTargetingType",
    "DSPOptimization",
    "DSPOptimizationOut",
    "DSPPacing",
    "DSPPacingOut",
    "DSPPixalateFraudInvalidTraffic",
    "DSPPixalateFraudInvalidTrafficOut",
    "DSPPlacementType",
    "DSPPlacementTypeTarget",
    "DSPPlacementTypeTargetOut",
    "DSPPoint",
    "DSPPointLabel",
    "DSPPrimaryInventoryType",
    "DSPProductCategoryMatchType",
    "DSPProductCategoryRefinement",
    "DSPProductCategoryRefinementOut",
    "DSPProductCategoryRefinementValue",
    "DSPProductCategoryRefinementValueOut",
    "DSPProductCategoryTarget",
    "DSPProductCategoryTargetOut",
    "DSPProductIdType",
    "DSPProductMarketplaceSetting",
    "DSPProductMarketplaceSettingOut",
    "DSPProductMatchType",
    "DSPProductTarget",
    "DSPProductTargetOut",
    "DSPProductValue",
    "DSPProductValueOut",
    "DSPRecommendedObjectType",
    "DSPRecurrence",
    "DSPReplanning",
    "DSPReplanningSettings",
    "DSPReplanningSettingsOut",
    "DSPRetrieveCampaignForecastRequest",
    "DSPRolloverStrategy",
    "DSPSelectedForecastMetric",
    "DSPSiteLanguage",
    "DSPState",
    "DSPStatus",
    "DSPStatusOut",
    "DSPTacticKey",
    "DSPTacticKeyOut",
    "DSPTacticsConvertersExclusionType",
    "DSPTag",
    "DSPTagOut",
    "DSPTargetBid",
    "DSPTargetBidOut",
    "DSPTargetDetails",
    "DSPTargetDetailsOut",
    "DSPTargetLevel",
    "DSPTargetType",
    "DSPTargetingSettings",
    "DSPTargetingSettingsOut",
    "DSPThemeMatchType",
    "DSPThemeTarget",
    "DSPThemeTargetOut",
    "DSPThirdPartyTarget",
    "DSPThirdPartyTargetDetails",
    "DSPThirdPartyTargetDetailsOut",
    "DSPThirdPartyTargetOut",
    "DSPThirdPartyTargetType",
    "DSPTimeOfDay",
    "DSPTimeOfDayOut",
    "DSPTimeUnit",
    "DSPTimeZoneType",
    "DSPTwitchContentRating",
    "DSPTwitchContentRatingEnum",
    "DSPTwitchContentRatingOut",
    "DSPUserLocationSignal",
    "DSPVideoAdFormat",
    "DSPVideoAdFormatTarget",
    "DSPVideoAdFormatTargetOut",
    "DSPVideoCompletionTier",
    "DSPVideoContentDuration",
    "DSPVideoContentDurationTarget",
    "DSPVideoContentDurationTargetOut",
    "DSPVideoInitiationType",
    "DSPViewabilityTier",
    "DSPViewabilityTierType",
    "DSPWarning",
    "DSPXPoint",
    "DSPYPoint",
]
