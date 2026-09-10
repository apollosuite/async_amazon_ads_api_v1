"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAcrossGroupOperator,
    DSPAdPlayerSize,
    DSPAdProduct,
    DSPAppType,
    DSPAverageCompletionAndFullyViewableRateTargetingType,
    DSPBrandExposureViewabilityTargetingType,
    DSPBrandSafetyCategory,
    DSPBrandSafetyTier,
    DSPBrandSuitabilityRiskLevelType,
    DSPContentGenre,
    DSPContentInstreamPosition,
    DSPContentOutstreamPosition,
    DSPContentRatingTypes,
    DSPCreateState,
    DSPCreateTimeOfDay,
    DSPDayOfWeek,
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
    DSPExcludeAppsAndSitesType,
    DSPFoldPosition,
    DSPIASBrandSafetyLevelType,
    DSPIASFraudInvalidTrafficType,
    DSPIASViewabilityStandardType,
    DSPInGroupOperator,
    DSPInventorySourceType,
    DSPKeywordMatchType,
    DSPMarketplace,
    DSPMarketplaceStringValue,
    DSPMarketplaceStringValueOut,
    DSPMobileDevice,
    DSPMobileEnvironment,
    DSPMobileOs,
    DSPMrcViewabilityTargetingType,
    DSPNativeContentPosition,
    DSPNewsGuardBrandGuardMisinformationSafetyType,
    DSPNewsGuardBrandGuardTrustedNewsTargetingType,
    DSPPlacementType,
    DSPProductCategoryMatchType,
    DSPProductIdType,
    DSPProductMatchType,
    DSPState,
    DSPTargetLevel,
    DSPTargetType,
    DSPThemeMatchType,
    DSPThirdPartyTargetType,
    DSPTwitchContentRatingEnum,
    DSPVideoAdFormat,
    DSPVideoContentDuration,
    DSPVideoInitiationType,
    DSPViewabilityTierType,
)


class DSPAdInitiationTarget(LenientModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: DSPVideoInitiationType | str


class DSPAdPlayerSizeTarget(LenientModel):
    """Target based on the size of the ad player."""

    adPlayerSize: DSPAdPlayerSize | str


class DSPAdvertiserDomainList(LenientModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPAppTarget(LenientModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: DSPAppType | str


class DSPAudienceTarget(LenientModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: DSPAcrossGroupOperator | str | None = Field(default=None)
    audienceId: DSPMarketplaceStringValueOut
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: DSPInGroupOperator | str | None = Field(default=None)


class DSPBrandSafetyCategoryTarget(LenientModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: DSPBrandSafetyCategory | str


class DSPBrandSafetyTierTarget(LenientModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: DSPBrandSafetyTier | str


class DSPContentCategoryTarget(LenientModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPContentGenreTarget(LenientModel):
    """Target based on the genre of content being viewed."""

    contentGenre: DSPContentGenre | str


class DSPContentInstreamPositionTarget(LenientModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: DSPContentInstreamPosition | str


class DSPContentOutstreamPositionTarget(LenientModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: DSPContentOutstreamPosition | str


class DSPContentRatingDspContentRating(LenientModel):
    dspContentRating: DSPDspContentRating


class DSPContentRatingTwitchContentRating(LenientModel):
    twitchContentRating: DSPTwitchContentRating


type DSPContentRating = DSPContentRatingDspContentRating | DSPContentRatingTwitchContentRating


class DSPContentRatingTarget(LenientModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: DSPContentRatingTypes | str
    contentRatingTypeDetails: DSPContentRating


class DSPCreateAdInitiationTarget(StrictModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: DSPVideoInitiationType


class DSPCreateAdPlayerSizeTarget(StrictModel):
    """Target based on the size of the ad player."""

    adPlayerSize: DSPAdPlayerSize


class DSPCreateAdvertiserDomainList(StrictModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPCreateAppTarget(StrictModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: DSPAppType


class DSPCreateAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: DSPAcrossGroupOperator | None = Field(default=None)
    audienceId: DSPCreateMarketplaceStringValue
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: DSPInGroupOperator | None = Field(default=None)


class DSPCreateBrandSafetyCategoryTarget(StrictModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: DSPBrandSafetyCategory


class DSPCreateBrandSafetyTierTarget(StrictModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: DSPBrandSafetyTier


class DSPCreateContentCategoryTarget(StrictModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPCreateContentGenreTarget(StrictModel):
    """Target based on the genre of content being viewed."""

    contentGenre: DSPContentGenre


class DSPCreateContentInstreamPositionTarget(StrictModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: DSPContentInstreamPosition


class DSPCreateContentOutstreamPositionTarget(StrictModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: DSPContentOutstreamPosition


class DSPCreateContentRatingDspContentRating(StrictModel):
    dspContentRating: DSPCreateDspContentRating


class DSPCreateContentRatingTwitchContentRating(StrictModel):
    twitchContentRating: DSPCreateTwitchContentRating


type DSPCreateContentRating = DSPCreateContentRatingDspContentRating | DSPCreateContentRatingTwitchContentRating


class DSPCreateContentRatingTarget(StrictModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: DSPContentRatingTypes
    contentRatingTypeDetails: DSPCreateContentRating


class DSPCreateDVBrandSafetyContentCategoriesWithRiskMap(StrictModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: DSPBrandSuitabilityRiskLevelType


class DSPCreateDayPartTarget(StrictModel):
    """Target based on time of day."""

    dayOfWeek: DSPDayOfWeek
    timeOfDay: DSPCreateTimeOfDay


class DSPCreateDeviceTarget(StrictModel):
    """Target based on user device."""

    deviceOrientation: DSPDeviceOrientation | None = Field(default=None)
    deviceType: DSPDeviceType
    mobileDevice: DSPMobileDevice | None = Field(default=None)
    mobileEnvironment: DSPMobileEnvironment | None = Field(default=None)
    mobileOs: DSPMobileOs | None = Field(default=None)


class DSPCreateDomainFileTarget(StrictModel):
    """Targets domains based on list provided via file upload."""

    domainFileKey: str = Field(
        description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be associated to one ad group."
    )
    domainFileName: str = Field(description="The name of the file.")


class DSPCreateDomainListTarget(StrictModel):
    """Targets domains based on an existing domain list."""

    domainListId: str = Field(description="The ID of the domain list to target.")


class DSPCreateDomainNameTarget(StrictModel):
    """Targets domains based on URL."""

    domainName: str = Field(description="The URL of the domain to target.")


class DSPCreateDomainTarget(StrictModel):
    """Target based on a specified domain."""

    domainTargetDetails: DSPCreateDomainTargetDetails
    domainTargetType: DSPDomainTargetTypes


class DSPCreateDomainTargetDetailsDomainListTarget(StrictModel):
    domainListTarget: DSPCreateDomainListTarget


class DSPCreateDomainTargetDetailsDomainNameTarget(StrictModel):
    domainNameTarget: DSPCreateDomainNameTarget


class DSPCreateDomainTargetDetailsDomainFileTarget(StrictModel):
    domainFileTarget: DSPCreateDomainFileTarget


class DSPCreateDomainTargetDetailsAdvertiserDomainList(StrictModel):
    advertiserDomainList: DSPCreateAdvertiserDomainList


type DSPCreateDomainTargetDetails = DSPCreateDomainTargetDetailsDomainListTarget | DSPCreateDomainTargetDetailsDomainNameTarget | DSPCreateDomainTargetDetailsDomainFileTarget | DSPCreateDomainTargetDetailsAdvertiserDomainList


class DSPCreateDoubleVerifyAuthenticAttention(StrictModel):
    universalAttention: bool = Field(
        description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor performing apps and domains."
    )


class DSPCreateDoubleVerifyAuthenticBrandSafety(StrictModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^51[0-9]{6}$")


class DSPCreateDoubleVerifyBrandSafety(StrictModel):
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
    contentCategoriesWithRisk: list[DSPCreateDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    excludeAppsWithInsufficientRating: bool | None = Field(
        default=None,
        description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).",
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPCreateDoubleVerifyCustomContextualSegmentId(StrictModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^52[0-9]{6}$")


class DSPCreateDoubleVerifyFraudInvalidTraffic(StrictModel):
    blockAppAndSites: bool | None = Field(
        default=None,
        description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will not be applicable if ALLOW_ALL is chosen.",
    )
    excludeAppsAndSites: DSPExcludeAppsAndSitesType | None = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPCreateDoubleVerifyStandardDisplayBrandSafety(StrictModel):
    contentCategories: list[DSPDVBrandSafetyContentCategoryType] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPCreateDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPCreateDoubleVerifyViewability(StrictModel):
    averageCompletionAndFullyViewableRateTargeting: DSPAverageCompletionAndFullyViewableRateTargetingType | None = (
        Field(default=None)
    )
    brandExposureViewabilityTargeting: DSPBrandExposureViewabilityTargetingType | None = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: DSPMrcViewabilityTargetingType | None = Field(default=None)


class DSPCreateDspContentRating(StrictModel):
    dspContentRating: DSPDspContentRatingEnum


class DSPCreateFoldPositionTarget(StrictModel):
    """Targets ads in the specified fold position"""

    foldPosition: DSPFoldPosition


class DSPCreateIntegralAdScienceBrandSafety(StrictModel):
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


class DSPCreateIntegralAdScienceContextualAvoidance(StrictModel):
    avoidanceSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual avoidance segment",
    )


class DSPCreateIntegralAdScienceContextualTargeting(StrictModel):
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


class DSPCreateIntegralAdScienceFraudInvalidTraffic(StrictModel):
    targetSetting: DSPIASFraudInvalidTrafficType | None = Field(default=None)


class DSPCreateIntegralAdScienceQualitySync(StrictModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPCreateIntegralAdScienceViewability(StrictModel):
    """The IAS viewability standard."""

    standard: DSPIASViewabilityStandardType
    viewabilityTargeting: DSPViewabilityTierType | None = Field(default=None)


class DSPCreateInventorySourceTarget(StrictModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPCreateMarketplaceStringValue
    inventorySourceType: DSPInventorySourceType


class DSPCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: DSPKeywordMatchType


class DSPCreateLocationTarget(StrictModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class DSPCreateMarketplaceStringValue(StrictModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class DSPCreateNativeContentPositionTarget(StrictModel):
    """Targets ads to a specific native content position"""

    nativePosition: DSPNativeContentPosition


class DSPCreateNewsGuardBrandGuardMisinformationSafety(StrictModel):
    avoidanceList: list[DSPNewsGuardBrandGuardMisinformationSafetyType] | None = Field(
        default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets"
    )


class DSPCreateNewsGuardBrandGuardTrustedNewsTargeting(StrictModel):
    """Only applicable for Web supply."""

    targetingList: list[DSPNewsGuardBrandGuardTrustedNewsTargetingType] | None = Field(
        default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets"
    )


class DSPCreatePixalateFraudInvalidTraffic(StrictModel):
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


class DSPCreatePlacementTypeTarget(StrictModel):
    """Target based on the placement type."""

    placementType: DSPPlacementType


class DSPCreateProductCategoryRefinement(StrictModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPCreateProductCategoryRefinementValue(StrictModel):
    productCategoryRefinement: DSPCreateProductCategoryRefinement | None = Field(default=None)


class DSPCreateProductCategoryTarget(StrictModel):
    """Targets a specific customer search term."""

    matchType: DSPProductCategoryMatchType | None = Field(default=None)
    productCategoryRefinement: DSPCreateProductCategoryRefinementValue


class DSPCreateProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: DSPProductMatchType
    product: DSPCreateProductValue
    productIdType: DSPProductIdType


class DSPCreateProductValue(StrictModel):
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class DSPCreateTargetDetailsKeywordTarget(StrictModel):
    keywordTarget: DSPCreateKeywordTarget


class DSPCreateTargetDetailsProductTarget(StrictModel):
    productTarget: DSPCreateProductTarget


class DSPCreateTargetDetailsProductCategoryTarget(StrictModel):
    productCategoryTarget: DSPCreateProductCategoryTarget


class DSPCreateTargetDetailsAudienceTarget(StrictModel):
    audienceTarget: DSPCreateAudienceTarget


class DSPCreateTargetDetailsLocationTarget(StrictModel):
    locationTarget: DSPCreateLocationTarget


class DSPCreateTargetDetailsDomainTarget(StrictModel):
    domainTarget: DSPCreateDomainTarget


class DSPCreateTargetDetailsAppTarget(StrictModel):
    appTarget: DSPCreateAppTarget


class DSPCreateTargetDetailsDeviceTarget(StrictModel):
    deviceTarget: DSPCreateDeviceTarget


class DSPCreateTargetDetailsDayPartTarget(StrictModel):
    dayPartTarget: DSPCreateDayPartTarget


class DSPCreateTargetDetailsContentCategoryTarget(StrictModel):
    contentCategoryTarget: DSPCreateContentCategoryTarget


class DSPCreateTargetDetailsContentGenreTarget(StrictModel):
    contentGenreTarget: DSPCreateContentGenreTarget


class DSPCreateTargetDetailsContentRatingTarget(StrictModel):
    contentRatingTarget: DSPCreateContentRatingTarget


class DSPCreateTargetDetailsBrandSafetyTierTarget(StrictModel):
    brandSafetyTierTarget: DSPCreateBrandSafetyTierTarget


class DSPCreateTargetDetailsBrandSafetyCategoryTarget(StrictModel):
    brandSafetyCategoryTarget: DSPCreateBrandSafetyCategoryTarget


class DSPCreateTargetDetailsInventorySourceTarget(StrictModel):
    inventorySourceTarget: DSPCreateInventorySourceTarget


class DSPCreateTargetDetailsAdInitiationTarget(StrictModel):
    adInitiationTarget: DSPCreateAdInitiationTarget


class DSPCreateTargetDetailsAdPlayerSizeTarget(StrictModel):
    adPlayerSizeTarget: DSPCreateAdPlayerSizeTarget


class DSPCreateTargetDetailsVideoAdFormatTarget(StrictModel):
    videoAdFormatTarget: DSPCreateVideoAdFormatTarget


class DSPCreateTargetDetailsThirdPartyTarget(StrictModel):
    thirdPartyTarget: DSPCreateThirdPartyTarget


class DSPCreateTargetDetailsThemeTarget(StrictModel):
    themeTarget: DSPCreateThemeTarget


class DSPCreateTargetDetailsContentInstreamPositionTarget(StrictModel):
    contentInstreamPositionTarget: DSPCreateContentInstreamPositionTarget


class DSPCreateTargetDetailsContentOutstreamPositionTarget(StrictModel):
    contentOutstreamPositionTarget: DSPCreateContentOutstreamPositionTarget


class DSPCreateTargetDetailsVideoContentDurationTarget(StrictModel):
    videoContentDurationTarget: DSPCreateVideoContentDurationTarget


class DSPCreateTargetDetailsFoldPositionTarget(StrictModel):
    foldPositionTarget: DSPCreateFoldPositionTarget


class DSPCreateTargetDetailsNativeContentPositionTarget(StrictModel):
    nativeContentPositionTarget: DSPCreateNativeContentPositionTarget


class DSPCreateTargetDetailsPlacementTypeTarget(StrictModel):
    placementTypeTarget: DSPCreatePlacementTypeTarget


type DSPCreateTargetDetails = DSPCreateTargetDetailsKeywordTarget | DSPCreateTargetDetailsProductTarget | DSPCreateTargetDetailsProductCategoryTarget | DSPCreateTargetDetailsAudienceTarget | DSPCreateTargetDetailsLocationTarget | DSPCreateTargetDetailsDomainTarget | DSPCreateTargetDetailsAppTarget | DSPCreateTargetDetailsDeviceTarget | DSPCreateTargetDetailsDayPartTarget | DSPCreateTargetDetailsContentCategoryTarget | DSPCreateTargetDetailsContentGenreTarget | DSPCreateTargetDetailsContentRatingTarget | DSPCreateTargetDetailsBrandSafetyTierTarget | DSPCreateTargetDetailsBrandSafetyCategoryTarget | DSPCreateTargetDetailsInventorySourceTarget | DSPCreateTargetDetailsAdInitiationTarget | DSPCreateTargetDetailsAdPlayerSizeTarget | DSPCreateTargetDetailsVideoAdFormatTarget | DSPCreateTargetDetailsThirdPartyTarget | DSPCreateTargetDetailsThemeTarget | DSPCreateTargetDetailsContentInstreamPositionTarget | DSPCreateTargetDetailsContentOutstreamPositionTarget | DSPCreateTargetDetailsVideoContentDurationTarget | DSPCreateTargetDetailsFoldPositionTarget | DSPCreateTargetDetailsNativeContentPositionTarget | DSPCreateTargetDetailsPlacementTypeTarget


class DSPCreateTargetRequest(StrictModel):
    targets: list[DSPTargetCreate] = Field(min_length=1, max_length=1000)


class DSPCreateThemeTarget(StrictModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: DSPThemeMatchType


class DSPCreateThirdPartyTarget(StrictModel):
    thirdPartyTargetDetails: DSPCreateThirdPartyTargetDetails
    thirdPartyTargetType: DSPThirdPartyTargetType


class DSPCreateThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic(StrictModel):
    doubleVerifyFraudInvalidTraffic: DSPCreateDoubleVerifyFraudInvalidTraffic


class DSPCreateThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety(StrictModel):
    doubleVerifyStandardDisplayBrandSafety: DSPCreateDoubleVerifyStandardDisplayBrandSafety


class DSPCreateThirdPartyTargetDetailsDoubleVerifyBrandSafety(StrictModel):
    doubleVerifyBrandSafety: DSPCreateDoubleVerifyBrandSafety


class DSPCreateThirdPartyTargetDetailsDoubleVerifyViewability(StrictModel):
    doubleVerifyViewability: DSPCreateDoubleVerifyViewability


class DSPCreateThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety(StrictModel):
    doubleVerifyAuthenticBrandSafety: DSPCreateDoubleVerifyAuthenticBrandSafety


class DSPCreateThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId(StrictModel):
    doubleVerifyCustomContextualSegmentId: DSPCreateDoubleVerifyCustomContextualSegmentId


class DSPCreateThirdPartyTargetDetailsDoubleVerifyAuthenticAttention(StrictModel):
    doubleVerifyAuthenticAttention: DSPCreateDoubleVerifyAuthenticAttention


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic(StrictModel):
    integralAdScienceFraudInvalidTraffic: DSPCreateIntegralAdScienceFraudInvalidTraffic


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceBrandSafety(StrictModel):
    integralAdScienceBrandSafety: DSPCreateIntegralAdScienceBrandSafety


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceViewability(StrictModel):
    integralAdScienceViewability: DSPCreateIntegralAdScienceViewability


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceContextualTargeting(StrictModel):
    integralAdScienceContextualTargeting: DSPCreateIntegralAdScienceContextualTargeting


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance(StrictModel):
    integralAdScienceContextualAvoidance: DSPCreateIntegralAdScienceContextualAvoidance


class DSPCreateThirdPartyTargetDetailsPixalateFraudInvalidTraffic(StrictModel):
    pixalateFraudInvalidTraffic: DSPCreatePixalateFraudInvalidTraffic


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceQualitySync(StrictModel):
    integralAdScienceQualitySync: DSPCreateIntegralAdScienceQualitySync


class DSPCreateThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting(StrictModel):
    newsGuardBrandGuardTrustedNewsTargeting: DSPCreateNewsGuardBrandGuardTrustedNewsTargeting


class DSPCreateThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety(StrictModel):
    newsGuardBrandGuardMisinformationSafety: DSPCreateNewsGuardBrandGuardMisinformationSafety


type DSPCreateThirdPartyTargetDetails = DSPCreateThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic | DSPCreateThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety | DSPCreateThirdPartyTargetDetailsDoubleVerifyBrandSafety | DSPCreateThirdPartyTargetDetailsDoubleVerifyViewability | DSPCreateThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety | DSPCreateThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId | DSPCreateThirdPartyTargetDetailsDoubleVerifyAuthenticAttention | DSPCreateThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic | DSPCreateThirdPartyTargetDetailsIntegralAdScienceBrandSafety | DSPCreateThirdPartyTargetDetailsIntegralAdScienceViewability | DSPCreateThirdPartyTargetDetailsIntegralAdScienceContextualTargeting | DSPCreateThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance | DSPCreateThirdPartyTargetDetailsPixalateFraudInvalidTraffic | DSPCreateThirdPartyTargetDetailsIntegralAdScienceQualitySync | DSPCreateThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting | DSPCreateThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety


class DSPCreateTwitchContentRating(StrictModel):
    twitchContentRating: DSPTwitchContentRatingEnum


class DSPCreateVideoAdFormatTarget(StrictModel):
    """Target based on the video ad format."""

    videoAdFormat: DSPVideoAdFormat


class DSPCreateVideoContentDurationTarget(StrictModel):
    """Targets ads to a specific video content duration"""

    duration: DSPVideoContentDuration


class DSPDVBrandSafetyContentCategoriesWithRiskMap(LenientModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: DSPBrandSuitabilityRiskLevelType | str


class DSPDayPartTarget(LenientModel):
    """Target based on time of day."""

    dayOfWeek: DSPDayOfWeek | str
    timeOfDay: DSPTimeOfDay


class DSPDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class DSPDeviceTarget(LenientModel):
    """Target based on user device."""

    deviceOrientation: DSPDeviceOrientation | str | None = Field(default=None)
    deviceType: DSPDeviceType | str
    mobileDevice: DSPMobileDevice | str | None = Field(default=None)
    mobileEnvironment: DSPMobileEnvironment | str | None = Field(default=None)
    mobileOs: DSPMobileOs | str | None = Field(default=None)


class DSPDomainFileTarget(LenientModel):
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


class DSPDomainListTarget(LenientModel):
    """Targets domains based on an existing domain list."""

    domainListId: str = Field(description="The ID of the domain list to target.")


class DSPDomainNameTarget(LenientModel):
    """Targets domains based on URL."""

    domainName: str = Field(description="The URL of the domain to target.")


class DSPDomainTarget(LenientModel):
    """Target based on a specified domain."""

    domainTargetDetails: DSPDomainTargetDetails
    domainTargetType: DSPDomainTargetTypes | str


class DSPDomainTargetDetailsAdvertiserDomainList(LenientModel):
    advertiserDomainList: DSPAdvertiserDomainList


class DSPDomainTargetDetailsDomainFileTarget(LenientModel):
    domainFileTarget: DSPDomainFileTarget


class DSPDomainTargetDetailsDomainListTarget(LenientModel):
    domainListTarget: DSPDomainListTarget


class DSPDomainTargetDetailsDomainNameTarget(LenientModel):
    domainNameTarget: DSPDomainNameTarget


type DSPDomainTargetDetails = DSPDomainTargetDetailsAdvertiserDomainList | DSPDomainTargetDetailsDomainFileTarget | DSPDomainTargetDetailsDomainListTarget | DSPDomainTargetDetailsDomainNameTarget


class DSPDoubleVerifyAuthenticAttention(LenientModel):
    universalAttention: bool = Field(
        description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor performing apps and domains."
    )


class DSPDoubleVerifyAuthenticBrandSafety(LenientModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^51[0-9]{6}$")


class DSPDoubleVerifyBrandSafety(LenientModel):
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
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    excludeAppsWithInsufficientRating: bool | None = Field(
        default=None,
        description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).",
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyCustomContextualSegmentId(LenientModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^52[0-9]{6}$")


class DSPDoubleVerifyFraudInvalidTraffic(LenientModel):
    blockAppAndSites: bool | None = Field(
        default=None,
        description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will not be applicable if ALLOW_ALL is chosen.",
    )
    excludeAppsAndSites: DSPExcludeAppsAndSitesType | str | None = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPDoubleVerifyStandardDisplayBrandSafety(LenientModel):
    contentCategories: list[DSPDVBrandSafetyContentCategoryType | str] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyViewability(LenientModel):
    averageCompletionAndFullyViewableRateTargeting: (
        DSPAverageCompletionAndFullyViewableRateTargetingType | str | None
    ) = Field(default=None)
    brandExposureViewabilityTargeting: DSPBrandExposureViewabilityTargetingType | str | None = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: DSPMrcViewabilityTargetingType | str | None = Field(default=None)


class DSPDspContentRating(LenientModel):
    dspContentRating: DSPDspContentRatingEnum | str


class DSPFoldPositionTarget(LenientModel):
    """Targets ads in the specified fold position"""

    foldPosition: DSPFoldPosition | str


class DSPIntegralAdScienceBrandSafety(LenientModel):
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


class DSPIntegralAdScienceContextualAvoidance(LenientModel):
    avoidanceSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual avoidance segment",
    )


class DSPIntegralAdScienceContextualTargeting(LenientModel):
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


class DSPIntegralAdScienceFraudInvalidTraffic(LenientModel):
    targetSetting: DSPIASFraudInvalidTrafficType | str | None = Field(default=None)


class DSPIntegralAdScienceQualitySync(LenientModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPIntegralAdScienceViewability(LenientModel):
    """The IAS viewability standard."""

    standard: DSPIASViewabilityStandardType | str
    viewabilityTargeting: DSPViewabilityTierType | str | None = Field(default=None)


class DSPInventorySourceTarget(LenientModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPMarketplaceStringValueOut
    inventorySourceType: DSPInventorySourceType | str


class DSPKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: DSPKeywordMatchType | str


class DSPLocationTarget(LenientModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class DSPNativeContentPositionTarget(LenientModel):
    """Targets ads to a specific native content position"""

    nativePosition: DSPNativeContentPosition | str


class DSPNewsGuardBrandGuardMisinformationSafety(LenientModel):
    avoidanceList: list[DSPNewsGuardBrandGuardMisinformationSafetyType | str] | None = Field(
        default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets"
    )


class DSPNewsGuardBrandGuardTrustedNewsTargeting(LenientModel):
    """Only applicable for Web supply."""

    targetingList: list[DSPNewsGuardBrandGuardTrustedNewsTargetingType | str] | None = Field(
        default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets"
    )


class DSPPixalateFraudInvalidTraffic(LenientModel):
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


class DSPPlacementTypeTarget(LenientModel):
    """Target based on the placement type."""

    placementType: DSPPlacementType | str


class DSPProductCategoryRefinement(LenientModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPProductCategoryRefinementValue(LenientModel):
    productCategoryRefinement: DSPProductCategoryRefinement | None = Field(default=None)


class DSPProductCategoryTarget(LenientModel):
    """Targets a specific customer search term."""

    matchType: DSPProductCategoryMatchType | str | None = Field(default=None)
    productCategoryRefinement: DSPProductCategoryRefinementValue


class DSPProductMarketplaceSetting(LenientModel):
    marketplace: DSPMarketplace | str
    productId: str = Field(description="The product id applicable at the specified marketplace.")


class DSPProductTarget(LenientModel):
    """Targets a specific product."""

    matchType: DSPProductMatchType | str
    product: DSPProductValue
    productIdType: DSPProductIdType | str


class DSPProductValue(LenientModel):
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


class DSPQueryTargetRequest(StrictModel):
    adGroupIdFilter: DSPTargetAdGroupIdFilter | None = Field(default=None)
    adProductFilter: DSPTargetAdProductFilter
    inventorySourceIdFilter: DSPTargetMarketplaceStringValueFilter | None = Field(default=None)
    inventorySourceTypeFilter: DSPTargetInventorySourceTypeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=5000, ge=1, le=5000)
    nextToken: str | None = Field(default=None)
    stateFilter: DSPTargetStateFilter | None = Field(default=None)
    targetTypeFilter: DSPTargetTargetTypeFilter | None = Field(default=None)


class DSPStatus(LenientModel):
    deliveryReasons: list[DSPDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: DSPDeliveryStatus | str


class DSPTarget(LenientModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: DSPAdProduct | str
    creationDateTime: datetime = Field(description="The date time the target was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: DSPState | str
    status: DSPStatus | None = Field(default=None)
    targetDetails: DSPTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: DSPTargetLevel | str
    targetType: DSPTargetType | str


class DSPTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPTargetAdProductFilter(StrictModel):
    include: list[DSPAdProduct] = Field(min_length=1, max_length=1)


class DSPTargetCreate(StrictModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: DSPAdProduct
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: DSPCreateState
    targetDetails: DSPCreateTargetDetails
    targetType: DSPTargetType


class DSPTargetDetailsAdInitiationTarget(LenientModel):
    adInitiationTarget: DSPAdInitiationTarget


class DSPTargetDetailsAdPlayerSizeTarget(LenientModel):
    adPlayerSizeTarget: DSPAdPlayerSizeTarget


class DSPTargetDetailsAppTarget(LenientModel):
    appTarget: DSPAppTarget


class DSPTargetDetailsAudienceTarget(LenientModel):
    audienceTarget: DSPAudienceTarget


class DSPTargetDetailsBrandSafetyCategoryTarget(LenientModel):
    brandSafetyCategoryTarget: DSPBrandSafetyCategoryTarget


class DSPTargetDetailsBrandSafetyTierTarget(LenientModel):
    brandSafetyTierTarget: DSPBrandSafetyTierTarget


class DSPTargetDetailsContentCategoryTarget(LenientModel):
    contentCategoryTarget: DSPContentCategoryTarget


class DSPTargetDetailsContentGenreTarget(LenientModel):
    contentGenreTarget: DSPContentGenreTarget


class DSPTargetDetailsContentInstreamPositionTarget(LenientModel):
    contentInstreamPositionTarget: DSPContentInstreamPositionTarget


class DSPTargetDetailsContentOutstreamPositionTarget(LenientModel):
    contentOutstreamPositionTarget: DSPContentOutstreamPositionTarget


class DSPTargetDetailsContentRatingTarget(LenientModel):
    contentRatingTarget: DSPContentRatingTarget


class DSPTargetDetailsDayPartTarget(LenientModel):
    dayPartTarget: DSPDayPartTarget


class DSPTargetDetailsDeviceTarget(LenientModel):
    deviceTarget: DSPDeviceTarget


class DSPTargetDetailsDomainTarget(LenientModel):
    domainTarget: DSPDomainTarget


class DSPTargetDetailsFoldPositionTarget(LenientModel):
    foldPositionTarget: DSPFoldPositionTarget


class DSPTargetDetailsInventorySourceTarget(LenientModel):
    inventorySourceTarget: DSPInventorySourceTarget


class DSPTargetDetailsKeywordTarget(LenientModel):
    keywordTarget: DSPKeywordTarget


class DSPTargetDetailsLocationTarget(LenientModel):
    locationTarget: DSPLocationTarget


class DSPTargetDetailsNativeContentPositionTarget(LenientModel):
    nativeContentPositionTarget: DSPNativeContentPositionTarget


class DSPTargetDetailsPlacementTypeTarget(LenientModel):
    placementTypeTarget: DSPPlacementTypeTarget


class DSPTargetDetailsProductCategoryTarget(LenientModel):
    productCategoryTarget: DSPProductCategoryTarget


class DSPTargetDetailsProductTarget(LenientModel):
    productTarget: DSPProductTarget


class DSPTargetDetailsThemeTarget(LenientModel):
    themeTarget: DSPThemeTarget


class DSPTargetDetailsThirdPartyTarget(LenientModel):
    thirdPartyTarget: DSPThirdPartyTarget


class DSPTargetDetailsVideoAdFormatTarget(LenientModel):
    videoAdFormatTarget: DSPVideoAdFormatTarget


class DSPTargetDetailsVideoContentDurationTarget(LenientModel):
    videoContentDurationTarget: DSPVideoContentDurationTarget


type DSPTargetDetails = DSPTargetDetailsAdInitiationTarget | DSPTargetDetailsAdPlayerSizeTarget | DSPTargetDetailsAppTarget | DSPTargetDetailsAudienceTarget | DSPTargetDetailsBrandSafetyCategoryTarget | DSPTargetDetailsBrandSafetyTierTarget | DSPTargetDetailsContentCategoryTarget | DSPTargetDetailsContentGenreTarget | DSPTargetDetailsContentInstreamPositionTarget | DSPTargetDetailsContentOutstreamPositionTarget | DSPTargetDetailsContentRatingTarget | DSPTargetDetailsDayPartTarget | DSPTargetDetailsDeviceTarget | DSPTargetDetailsDomainTarget | DSPTargetDetailsFoldPositionTarget | DSPTargetDetailsInventorySourceTarget | DSPTargetDetailsKeywordTarget | DSPTargetDetailsLocationTarget | DSPTargetDetailsNativeContentPositionTarget | DSPTargetDetailsPlacementTypeTarget | DSPTargetDetailsProductCategoryTarget | DSPTargetDetailsProductTarget | DSPTargetDetailsThemeTarget | DSPTargetDetailsThirdPartyTarget | DSPTargetDetailsVideoAdFormatTarget | DSPTargetDetailsVideoContentDurationTarget


class DSPTargetInventorySourceTypeFilter(StrictModel):
    include: list[DSPInventorySourceType] = Field(min_length=1, max_length=1)


class DSPTargetMarketplaceStringValueFilter(StrictModel):
    include: list[DSPMarketplaceStringValue] = Field(min_length=1, max_length=10)


class DSPTargetMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[DSPTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class DSPTargetMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=999)
    target: DSPTarget


class DSPTargetStateFilter(StrictModel):
    include: list[DSPState] = Field(min_length=1, max_length=3)


class DSPTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[DSPTarget] | None = Field(default=None, min_length=0, max_length=5000)


class DSPTargetTargetTypeFilter(StrictModel):
    include: list[DSPTargetType] = Field(min_length=1, max_length=17)


class DSPThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: DSPThemeMatchType | str


class DSPThirdPartyTarget(LenientModel):
    thirdPartyTargetDetails: DSPThirdPartyTargetDetails
    thirdPartyTargetType: DSPThirdPartyTargetType | str


class DSPThirdPartyTargetDetailsDoubleVerifyAuthenticAttention(LenientModel):
    doubleVerifyAuthenticAttention: DSPDoubleVerifyAuthenticAttention


class DSPThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety(LenientModel):
    doubleVerifyAuthenticBrandSafety: DSPDoubleVerifyAuthenticBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyBrandSafety(LenientModel):
    doubleVerifyBrandSafety: DSPDoubleVerifyBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId(LenientModel):
    doubleVerifyCustomContextualSegmentId: DSPDoubleVerifyCustomContextualSegmentId


class DSPThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic(LenientModel):
    doubleVerifyFraudInvalidTraffic: DSPDoubleVerifyFraudInvalidTraffic


class DSPThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety(LenientModel):
    doubleVerifyStandardDisplayBrandSafety: DSPDoubleVerifyStandardDisplayBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyViewability(LenientModel):
    doubleVerifyViewability: DSPDoubleVerifyViewability


class DSPThirdPartyTargetDetailsIntegralAdScienceBrandSafety(LenientModel):
    integralAdScienceBrandSafety: DSPIntegralAdScienceBrandSafety


class DSPThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance(LenientModel):
    integralAdScienceContextualAvoidance: DSPIntegralAdScienceContextualAvoidance


class DSPThirdPartyTargetDetailsIntegralAdScienceContextualTargeting(LenientModel):
    integralAdScienceContextualTargeting: DSPIntegralAdScienceContextualTargeting


class DSPThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic(LenientModel):
    integralAdScienceFraudInvalidTraffic: DSPIntegralAdScienceFraudInvalidTraffic


class DSPThirdPartyTargetDetailsIntegralAdScienceQualitySync(LenientModel):
    integralAdScienceQualitySync: DSPIntegralAdScienceQualitySync


class DSPThirdPartyTargetDetailsIntegralAdScienceViewability(LenientModel):
    integralAdScienceViewability: DSPIntegralAdScienceViewability


class DSPThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety(LenientModel):
    newsGuardBrandGuardMisinformationSafety: DSPNewsGuardBrandGuardMisinformationSafety


class DSPThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting(LenientModel):
    newsGuardBrandGuardTrustedNewsTargeting: DSPNewsGuardBrandGuardTrustedNewsTargeting


class DSPThirdPartyTargetDetailsPixalateFraudInvalidTraffic(LenientModel):
    pixalateFraudInvalidTraffic: DSPPixalateFraudInvalidTraffic


type DSPThirdPartyTargetDetails = DSPThirdPartyTargetDetailsDoubleVerifyAuthenticAttention | DSPThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId | DSPThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic | DSPThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyViewability | DSPThirdPartyTargetDetailsIntegralAdScienceBrandSafety | DSPThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance | DSPThirdPartyTargetDetailsIntegralAdScienceContextualTargeting | DSPThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic | DSPThirdPartyTargetDetailsIntegralAdScienceQualitySync | DSPThirdPartyTargetDetailsIntegralAdScienceViewability | DSPThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety | DSPThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting | DSPThirdPartyTargetDetailsPixalateFraudInvalidTraffic


class DSPTimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPTwitchContentRating(LenientModel):
    twitchContentRating: DSPTwitchContentRatingEnum | str


class DSPVideoAdFormatTarget(LenientModel):
    """Target based on the video ad format."""

    videoAdFormat: DSPVideoAdFormat | str


class DSPVideoContentDurationTarget(LenientModel):
    """Targets ads to a specific video content duration"""

    duration: DSPVideoContentDuration | str


__all__ = [
    "DSPAcrossGroupOperator",
    "DSPAdInitiationTarget",
    "DSPAdPlayerSize",
    "DSPAdPlayerSizeTarget",
    "DSPAdProduct",
    "DSPAdvertiserDomainList",
    "DSPAppTarget",
    "DSPAppType",
    "DSPAudienceTarget",
    "DSPAverageCompletionAndFullyViewableRateTargetingType",
    "DSPBrandExposureViewabilityTargetingType",
    "DSPBrandSafetyCategory",
    "DSPBrandSafetyCategoryTarget",
    "DSPBrandSafetyTier",
    "DSPBrandSafetyTierTarget",
    "DSPBrandSuitabilityRiskLevelType",
    "DSPContentCategoryTarget",
    "DSPContentGenre",
    "DSPContentGenreTarget",
    "DSPContentInstreamPosition",
    "DSPContentInstreamPositionTarget",
    "DSPContentOutstreamPosition",
    "DSPContentOutstreamPositionTarget",
    "DSPContentRating",
    "DSPContentRatingTarget",
    "DSPContentRatingTypes",
    "DSPCreateAdInitiationTarget",
    "DSPCreateAdPlayerSizeTarget",
    "DSPCreateAdvertiserDomainList",
    "DSPCreateAppTarget",
    "DSPCreateAudienceTarget",
    "DSPCreateBrandSafetyCategoryTarget",
    "DSPCreateBrandSafetyTierTarget",
    "DSPCreateContentCategoryTarget",
    "DSPCreateContentGenreTarget",
    "DSPCreateContentInstreamPositionTarget",
    "DSPCreateContentOutstreamPositionTarget",
    "DSPCreateContentRating",
    "DSPCreateContentRatingTarget",
    "DSPCreateDVBrandSafetyContentCategoriesWithRiskMap",
    "DSPCreateDayPartTarget",
    "DSPCreateDeviceTarget",
    "DSPCreateDomainFileTarget",
    "DSPCreateDomainListTarget",
    "DSPCreateDomainNameTarget",
    "DSPCreateDomainTarget",
    "DSPCreateDomainTargetDetails",
    "DSPCreateDoubleVerifyAuthenticAttention",
    "DSPCreateDoubleVerifyAuthenticBrandSafety",
    "DSPCreateDoubleVerifyBrandSafety",
    "DSPCreateDoubleVerifyCustomContextualSegmentId",
    "DSPCreateDoubleVerifyFraudInvalidTraffic",
    "DSPCreateDoubleVerifyStandardDisplayBrandSafety",
    "DSPCreateDoubleVerifyViewability",
    "DSPCreateDspContentRating",
    "DSPCreateFoldPositionTarget",
    "DSPCreateIntegralAdScienceBrandSafety",
    "DSPCreateIntegralAdScienceContextualAvoidance",
    "DSPCreateIntegralAdScienceContextualTargeting",
    "DSPCreateIntegralAdScienceFraudInvalidTraffic",
    "DSPCreateIntegralAdScienceQualitySync",
    "DSPCreateIntegralAdScienceViewability",
    "DSPCreateInventorySourceTarget",
    "DSPCreateKeywordTarget",
    "DSPCreateLocationTarget",
    "DSPCreateMarketplaceStringValue",
    "DSPCreateNativeContentPositionTarget",
    "DSPCreateNewsGuardBrandGuardMisinformationSafety",
    "DSPCreateNewsGuardBrandGuardTrustedNewsTargeting",
    "DSPCreatePixalateFraudInvalidTraffic",
    "DSPCreatePlacementTypeTarget",
    "DSPCreateProductCategoryRefinement",
    "DSPCreateProductCategoryRefinementValue",
    "DSPCreateProductCategoryTarget",
    "DSPCreateProductTarget",
    "DSPCreateProductValue",
    "DSPCreateState",
    "DSPCreateTargetDetails",
    "DSPCreateTargetRequest",
    "DSPCreateThemeTarget",
    "DSPCreateThirdPartyTarget",
    "DSPCreateThirdPartyTargetDetails",
    "DSPCreateTimeOfDay",
    "DSPCreateTwitchContentRating",
    "DSPCreateVideoAdFormatTarget",
    "DSPCreateVideoContentDurationTarget",
    "DSPDVBrandSafetyAppAgeRatingType",
    "DSPDVBrandSafetyAppStarRatingType",
    "DSPDVBrandSafetyContentCategoriesWithRiskMap",
    "DSPDVBrandSafetyContentCategoryType",
    "DSPDayOfWeek",
    "DSPDayPartTarget",
    "DSPDeleteTargetRequest",
    "DSPDeliveryReason",
    "DSPDeliveryStatus",
    "DSPDeviceOrientation",
    "DSPDeviceTarget",
    "DSPDeviceType",
    "DSPDomainFileTarget",
    "DSPDomainListTarget",
    "DSPDomainNameTarget",
    "DSPDomainTarget",
    "DSPDomainTargetDetails",
    "DSPDomainTargetTypes",
    "DSPDoubleVerifyAuthenticAttention",
    "DSPDoubleVerifyAuthenticBrandSafety",
    "DSPDoubleVerifyBrandSafety",
    "DSPDoubleVerifyCustomContextualSegmentId",
    "DSPDoubleVerifyFraudInvalidTraffic",
    "DSPDoubleVerifyStandardDisplayBrandSafety",
    "DSPDoubleVerifyViewability",
    "DSPDspContentRating",
    "DSPDspContentRatingEnum",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPExcludeAppsAndSitesType",
    "DSPFoldPosition",
    "DSPFoldPositionTarget",
    "DSPIASBrandSafetyLevelType",
    "DSPIASFraudInvalidTrafficType",
    "DSPIASViewabilityStandardType",
    "DSPInGroupOperator",
    "DSPIntegralAdScienceBrandSafety",
    "DSPIntegralAdScienceContextualAvoidance",
    "DSPIntegralAdScienceContextualTargeting",
    "DSPIntegralAdScienceFraudInvalidTraffic",
    "DSPIntegralAdScienceQualitySync",
    "DSPIntegralAdScienceViewability",
    "DSPInventorySourceTarget",
    "DSPInventorySourceType",
    "DSPKeywordMatchType",
    "DSPKeywordTarget",
    "DSPLocationTarget",
    "DSPMarketplace",
    "DSPMarketplaceStringValue",
    "DSPMarketplaceStringValueOut",
    "DSPMobileDevice",
    "DSPMobileEnvironment",
    "DSPMobileOs",
    "DSPMrcViewabilityTargetingType",
    "DSPNativeContentPosition",
    "DSPNativeContentPositionTarget",
    "DSPNewsGuardBrandGuardMisinformationSafety",
    "DSPNewsGuardBrandGuardMisinformationSafetyType",
    "DSPNewsGuardBrandGuardTrustedNewsTargeting",
    "DSPNewsGuardBrandGuardTrustedNewsTargetingType",
    "DSPPixalateFraudInvalidTraffic",
    "DSPPlacementType",
    "DSPPlacementTypeTarget",
    "DSPProductCategoryMatchType",
    "DSPProductCategoryRefinement",
    "DSPProductCategoryRefinementValue",
    "DSPProductCategoryTarget",
    "DSPProductIdType",
    "DSPProductMarketplaceSetting",
    "DSPProductMatchType",
    "DSPProductTarget",
    "DSPProductValue",
    "DSPQueryTargetRequest",
    "DSPState",
    "DSPStatus",
    "DSPTarget",
    "DSPTargetAdGroupIdFilter",
    "DSPTargetAdProductFilter",
    "DSPTargetCreate",
    "DSPTargetDetails",
    "DSPTargetInventorySourceTypeFilter",
    "DSPTargetLevel",
    "DSPTargetMarketplaceStringValueFilter",
    "DSPTargetMultiStatusResponse",
    "DSPTargetMultiStatusSuccess",
    "DSPTargetStateFilter",
    "DSPTargetSuccessResponse",
    "DSPTargetTargetTypeFilter",
    "DSPTargetType",
    "DSPThemeMatchType",
    "DSPThemeTarget",
    "DSPThirdPartyTarget",
    "DSPThirdPartyTargetDetails",
    "DSPThirdPartyTargetType",
    "DSPTimeOfDay",
    "DSPTwitchContentRating",
    "DSPTwitchContentRatingEnum",
    "DSPVideoAdFormat",
    "DSPVideoAdFormatTarget",
    "DSPVideoContentDuration",
    "DSPVideoContentDurationTarget",
    "DSPVideoInitiationType",
    "DSPViewabilityTierType",
]
