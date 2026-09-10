"""Auto-generated models for SupplierAdProductPrices from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAdvertisingDealPriceType,
    DSPAmazonPublisherCloudDeliveryIntentGoals,
    DSPAmazonPublisherDirectDeliveryIntentGoals,
    DSPAmazonPublisherServicesGoalDetails,
    DSPAmazonPublisherServicesGoalTargetUnit,
    DSPAmazonPublisherServicesGoalTypes,
    DSPAudioCreativeRequirements,
    DSPCreateAmazonPublisherCloudDeliveryIntentGoals,
    DSPCreateAmazonPublisherDirectDeliveryIntentGoals,
    DSPCreateAmazonPublisherServicesGoalDetails,
    DSPCreateAudioCreativeRequirements,
    DSPCreateDeliveryIntent,
    DSPCreateDeliveryIntentGoals,
    DSPCreateDeliveryIntentGoalsExtension,
    DSPCreateDisplayCreativeRequirements,
    DSPCreateFrequency,
    DSPCreateFrequencyCap,
    DSPCreateSize,
    DSPCreateSupplierAppTarget,
    DSPCreateSupplierAudienceAgeTarget,
    DSPCreateSupplierAudienceEducationTarget,
    DSPCreateSupplierAudienceGenderTarget,
    DSPCreateSupplierAudienceHomeownershipTarget,
    DSPCreateSupplierAudienceHouseholdCompositionTarget,
    DSPCreateSupplierAudienceHouseholdIncomeTarget,
    DSPCreateSupplierAudienceInMarketTarget,
    DSPCreateSupplierAudienceInterestsTarget,
    DSPCreateSupplierAudienceMaritalStatusTarget,
    DSPCreateSupplierAudienceMoodTarget,
    DSPCreateSupplierAudienceSocioeconomicGroupTarget,
    DSPCreateSupplierAudienceTarget,
    DSPCreateSupplierContentCategoryTarget,
    DSPCreateSupplierContentGenreTarget,
    DSPCreateSupplierContentRatingTarget,
    DSPCreateSupplierContentSensitiveCategoryTarget,
    DSPCreateSupplierDayPartDayTarget,
    DSPCreateSupplierDayPartTarget,
    DSPCreateSupplierDayPartTimeTarget,
    DSPCreateSupplierDeviceOperatingSystemTarget,
    DSPCreateSupplierDeviceTypeTarget,
    DSPCreateSupplierGroupDetails,
    DSPCreateSupplierLocationGroup,
    DSPCreateSupplierLocationTarget,
    DSPCreateSupplierPositionVideoTarget,
    DSPCreateSupplierProposedDealCreativeRequirement,
    DSPCreateSupplierProposedDealCreativeRequirements,
    DSPCreateSupplierTarget,
    DSPCreateSupplierTargetDetails,
    DSPCreateSupplierTargetGroup,
    DSPCreateTimeOfDay,
    DSPCreateVideoCreativeRequirements,
    DSPCurrencyCode,
    DSPDayOfWeek,
    DSPDeliveryIntentGoals,
    DSPDeliveryIntentGoalsExtension,
    DSPDisplayCreativeRequirements,
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
    DSPEventType,
    DSPExtraFrequencyCapImpressionType,
    DSPFrequencyTargetingSetting,
    DSPInventoryType,
    DSPLanguageIso,
    DSPSize,
    DSPSupplierGroupType,
    DSPSupplierProposedDealCreativeRequirement,
    DSPSupplierProposedDealCreativeRequirements,
    DSPSupplierTargetingDaypartTimezoneType,
    DSPSupplierTargetType,
    DSPTimeUnit,
    DSPVideoCreativeRequirements,
)

type DSPPriceComponentType = Literal["SUPPLIER_PRICE", "THIRD_PARTY_DATA_TARGETING_FEE"]


type DSPSupplierAdProductPriceDescriptionType = Literal["AMAZON_MEDIA"]


class DSPAdvertisingDealPrice(LenientModel):
    currencyCode: DSPCurrencyCode | str
    priceType: DSPAdvertisingDealPriceType | str
    value: float = Field(description="The monetary amount of the price in the given currency.")


class DSPCreateSupplierAdProductPriceDescription(StrictModel):
    """The description of the supplier ad product price request parameters."""

    advertiserAccountId: str = Field(
        description="The advertiser ID. A required field since advertiserId may impact the price returned."
    )
    creativeRequirements: list[DSPCreateSupplierProposedDealCreativeRequirement] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Creative requirements for this supplier ad product price.",
    )
    deliveryIntent: DSPCreateDeliveryIntent | None = Field(default=None)
    endDateTime: datetime | None = Field(default=None, description="End datetime for rate calculation.")
    startDateTime: datetime = Field(description="Start datetime for rate calculation.")
    supplierAdProductId: str = Field(description="The supplier ad product ID.")
    supplierAdProductPriceDescriptionType: DSPSupplierAdProductPriceDescriptionType
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The proposal supplier proposal destination ID."
    )
    targeting: list[DSPCreateSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )


class DSPCreateSupplierAdProductPriceRequest(StrictModel):
    supplierAdProductPrices: list[DSPSupplierAdProductPriceCreate] = Field(min_length=1, max_length=10)


class DSPDeliveryIntent(LenientModel):
    """Delivery control configuration for proposed deals."""

    frequencyCap: DSPFrequencyCap | None = Field(default=None)
    goals: DSPDeliveryIntentGoals | None = Field(default=None)


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


class DSPFrequencyCap(LenientModel):
    """Frequency cap configuration."""

    frequencyCaps: list[DSPFrequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency caps for this deal."
    )


class DSPPriceComponent(LenientModel):
    price: DSPAdvertisingDealPrice
    priceComponentType: DSPPriceComponentType | str


class DSPSupplierAdProductPrice(LenientModel):
    itemizedPrice: list[DSPPriceComponent] | None = Field(
        default=None, min_length=0, max_length=49, description="Itemized breakdown of the price components."
    )
    lastUpdatedProductPriceDateTime: datetime = Field(description="The timestamp at which the rate was calculated.")
    price: DSPAdvertisingDealPrice
    supplierAdProductPriceDescription: DSPSupplierAdProductPriceDescription


class DSPSupplierAdProductPriceCreate(StrictModel):
    supplierAdProductPriceDescription: DSPCreateSupplierAdProductPriceDescription


class DSPSupplierAdProductPriceDescription(LenientModel):
    """The description of the supplier ad product price request parameters."""

    advertiserAccountId: str = Field(
        description="The advertiser ID. A required field since advertiserId may impact the price returned."
    )
    creativeRequirements: list[DSPSupplierProposedDealCreativeRequirement] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Creative requirements for this supplier ad product price.",
    )
    deliveryIntent: DSPDeliveryIntent | None = Field(default=None)
    endDateTime: datetime | None = Field(default=None, description="End datetime for rate calculation.")
    startDateTime: datetime = Field(description="Start datetime for rate calculation.")
    supplierAdProductId: str = Field(description="The supplier ad product ID.")
    supplierAdProductPriceDescriptionType: DSPSupplierAdProductPriceDescriptionType | str
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The proposal supplier proposal destination ID."
    )
    targeting: list[DSPSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )


class DSPSupplierAdProductPriceMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[DSPSupplierAdProductPriceMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class DSPSupplierAdProductPriceMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    supplierAdProductPrice: DSPSupplierAdProductPrice


class DSPSupplierAppTarget(LenientModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class DSPSupplierAudienceAgeTarget(LenientModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class DSPSupplierAudienceEducationTarget(LenientModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class DSPSupplierAudienceGenderTarget(LenientModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class DSPSupplierAudienceHomeownershipTarget(LenientModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class DSPSupplierAudienceHouseholdCompositionTarget(LenientModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class DSPSupplierAudienceHouseholdIncomeTarget(LenientModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class DSPSupplierAudienceInMarketTarget(LenientModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class DSPSupplierAudienceInterestsTarget(LenientModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class DSPSupplierAudienceMaritalStatusTarget(LenientModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class DSPSupplierAudienceMoodTarget(LenientModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class DSPSupplierAudienceSocioeconomicGroupTarget(LenientModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class DSPSupplierAudienceTarget(LenientModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class DSPSupplierContentCategoryTarget(LenientModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class DSPSupplierContentGenreTarget(LenientModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class DSPSupplierContentRatingTarget(LenientModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class DSPSupplierContentSensitiveCategoryTarget(LenientModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class DSPSupplierDayPartDayTarget(LenientModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class DSPSupplierDayPartTarget(LenientModel):
    """Supplier target based on time of day."""

    dayOfWeek: DSPDayOfWeek | str
    timeOfDay: DSPTimeOfDay
    timeZoneType: DSPSupplierTargetingDaypartTimezoneType | str | None = Field(default=None)


class DSPSupplierDayPartTimeTarget(LenientModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class DSPSupplierDeviceOperatingSystemTarget(LenientModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class DSPSupplierDeviceTypeTarget(LenientModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class DSPSupplierGroupDetails(LenientModel):
    supplierLocationGroup: DSPSupplierLocationGroup


class DSPSupplierLocationGroup(LenientModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class DSPSupplierLocationTarget(LenientModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class DSPSupplierPositionVideoTarget(LenientModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class DSPSupplierTarget(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: DSPSupplierTargetDetails
    supplierTargetType: DSPSupplierTargetType | str


class DSPSupplierTargetDetailsSupplierAppTarget(LenientModel):
    supplierAppTarget: DSPSupplierAppTarget


class DSPSupplierTargetDetailsSupplierAudienceAgeTarget(LenientModel):
    supplierAudienceAgeTarget: DSPSupplierAudienceAgeTarget


class DSPSupplierTargetDetailsSupplierAudienceEducationTarget(LenientModel):
    supplierAudienceEducationTarget: DSPSupplierAudienceEducationTarget


class DSPSupplierTargetDetailsSupplierAudienceGenderTarget(LenientModel):
    supplierAudienceGenderTarget: DSPSupplierAudienceGenderTarget


class DSPSupplierTargetDetailsSupplierAudienceHomeownershipTarget(LenientModel):
    supplierAudienceHomeownershipTarget: DSPSupplierAudienceHomeownershipTarget


class DSPSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(LenientModel):
    supplierAudienceHouseholdCompositionTarget: DSPSupplierAudienceHouseholdCompositionTarget


class DSPSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(LenientModel):
    supplierAudienceHouseholdIncomeTarget: DSPSupplierAudienceHouseholdIncomeTarget


class DSPSupplierTargetDetailsSupplierAudienceInMarketTarget(LenientModel):
    supplierAudienceInMarketTarget: DSPSupplierAudienceInMarketTarget


class DSPSupplierTargetDetailsSupplierAudienceInterestsTarget(LenientModel):
    supplierAudienceInterestsTarget: DSPSupplierAudienceInterestsTarget


class DSPSupplierTargetDetailsSupplierAudienceMaritalStatusTarget(LenientModel):
    supplierAudienceMaritalStatusTarget: DSPSupplierAudienceMaritalStatusTarget


class DSPSupplierTargetDetailsSupplierAudienceMoodTarget(LenientModel):
    supplierAudienceMoodTarget: DSPSupplierAudienceMoodTarget


class DSPSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(LenientModel):
    supplierAudienceSocioeconomicGroupTarget: DSPSupplierAudienceSocioeconomicGroupTarget


class DSPSupplierTargetDetailsSupplierAudienceTarget(LenientModel):
    supplierAudienceTarget: DSPSupplierAudienceTarget


class DSPSupplierTargetDetailsSupplierContentCategoryTarget(LenientModel):
    supplierContentCategoryTarget: DSPSupplierContentCategoryTarget


class DSPSupplierTargetDetailsSupplierContentGenreTarget(LenientModel):
    supplierContentGenreTarget: DSPSupplierContentGenreTarget


class DSPSupplierTargetDetailsSupplierContentRatingTarget(LenientModel):
    supplierContentRatingTarget: DSPSupplierContentRatingTarget


class DSPSupplierTargetDetailsSupplierContentSensitiveCategoryTarget(LenientModel):
    supplierContentSensitiveCategoryTarget: DSPSupplierContentSensitiveCategoryTarget


class DSPSupplierTargetDetailsSupplierDayPartDayTarget(LenientModel):
    supplierDayPartDayTarget: DSPSupplierDayPartDayTarget


class DSPSupplierTargetDetailsSupplierDayPartTarget(LenientModel):
    supplierDayPartTarget: DSPSupplierDayPartTarget


class DSPSupplierTargetDetailsSupplierDayPartTimeTarget(LenientModel):
    supplierDayPartTimeTarget: DSPSupplierDayPartTimeTarget


class DSPSupplierTargetDetailsSupplierDeviceOperatingSystemTarget(LenientModel):
    supplierDeviceOperatingSystemTarget: DSPSupplierDeviceOperatingSystemTarget


class DSPSupplierTargetDetailsSupplierDeviceTypeTarget(LenientModel):
    supplierDeviceTypeTarget: DSPSupplierDeviceTypeTarget


class DSPSupplierTargetDetailsSupplierLocationTarget(LenientModel):
    supplierLocationTarget: DSPSupplierLocationTarget


class DSPSupplierTargetDetailsSupplierPositionVideoTarget(LenientModel):
    supplierPositionVideoTarget: DSPSupplierPositionVideoTarget


type DSPSupplierTargetDetails = DSPSupplierTargetDetailsSupplierAppTarget | DSPSupplierTargetDetailsSupplierAudienceAgeTarget | DSPSupplierTargetDetailsSupplierAudienceEducationTarget | DSPSupplierTargetDetailsSupplierAudienceGenderTarget | DSPSupplierTargetDetailsSupplierAudienceHomeownershipTarget | DSPSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | DSPSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | DSPSupplierTargetDetailsSupplierAudienceInMarketTarget | DSPSupplierTargetDetailsSupplierAudienceInterestsTarget | DSPSupplierTargetDetailsSupplierAudienceMaritalStatusTarget | DSPSupplierTargetDetailsSupplierAudienceMoodTarget | DSPSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | DSPSupplierTargetDetailsSupplierAudienceTarget | DSPSupplierTargetDetailsSupplierContentCategoryTarget | DSPSupplierTargetDetailsSupplierContentGenreTarget | DSPSupplierTargetDetailsSupplierContentRatingTarget | DSPSupplierTargetDetailsSupplierContentSensitiveCategoryTarget | DSPSupplierTargetDetailsSupplierDayPartDayTarget | DSPSupplierTargetDetailsSupplierDayPartTarget | DSPSupplierTargetDetailsSupplierDayPartTimeTarget | DSPSupplierTargetDetailsSupplierDeviceOperatingSystemTarget | DSPSupplierTargetDetailsSupplierDeviceTypeTarget | DSPSupplierTargetDetailsSupplierLocationTarget | DSPSupplierTargetDetailsSupplierPositionVideoTarget


class DSPSupplierTargetGroup(LenientModel):
    groupDetails: DSPSupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[DSPSupplierTarget] = Field(min_length=1, max_length=49)
    groupType: DSPSupplierGroupType | str | None = Field(default=None)


class DSPTimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


__all__ = [
    "DSPAdvertisingDealPrice",
    "DSPAdvertisingDealPriceType",
    "DSPAmazonPublisherCloudDeliveryIntentGoals",
    "DSPAmazonPublisherDirectDeliveryIntentGoals",
    "DSPAmazonPublisherServicesGoalDetails",
    "DSPAmazonPublisherServicesGoalTargetUnit",
    "DSPAmazonPublisherServicesGoalTypes",
    "DSPAudioCreativeRequirements",
    "DSPCreateAmazonPublisherCloudDeliveryIntentGoals",
    "DSPCreateAmazonPublisherDirectDeliveryIntentGoals",
    "DSPCreateAmazonPublisherServicesGoalDetails",
    "DSPCreateAudioCreativeRequirements",
    "DSPCreateDeliveryIntent",
    "DSPCreateDeliveryIntentGoals",
    "DSPCreateDeliveryIntentGoalsExtension",
    "DSPCreateDisplayCreativeRequirements",
    "DSPCreateFrequency",
    "DSPCreateFrequencyCap",
    "DSPCreateSize",
    "DSPCreateSupplierAdProductPriceDescription",
    "DSPCreateSupplierAdProductPriceRequest",
    "DSPCreateSupplierAppTarget",
    "DSPCreateSupplierAudienceAgeTarget",
    "DSPCreateSupplierAudienceEducationTarget",
    "DSPCreateSupplierAudienceGenderTarget",
    "DSPCreateSupplierAudienceHomeownershipTarget",
    "DSPCreateSupplierAudienceHouseholdCompositionTarget",
    "DSPCreateSupplierAudienceHouseholdIncomeTarget",
    "DSPCreateSupplierAudienceInMarketTarget",
    "DSPCreateSupplierAudienceInterestsTarget",
    "DSPCreateSupplierAudienceMaritalStatusTarget",
    "DSPCreateSupplierAudienceMoodTarget",
    "DSPCreateSupplierAudienceSocioeconomicGroupTarget",
    "DSPCreateSupplierAudienceTarget",
    "DSPCreateSupplierContentCategoryTarget",
    "DSPCreateSupplierContentGenreTarget",
    "DSPCreateSupplierContentRatingTarget",
    "DSPCreateSupplierContentSensitiveCategoryTarget",
    "DSPCreateSupplierDayPartDayTarget",
    "DSPCreateSupplierDayPartTarget",
    "DSPCreateSupplierDayPartTimeTarget",
    "DSPCreateSupplierDeviceOperatingSystemTarget",
    "DSPCreateSupplierDeviceTypeTarget",
    "DSPCreateSupplierGroupDetails",
    "DSPCreateSupplierLocationGroup",
    "DSPCreateSupplierLocationTarget",
    "DSPCreateSupplierPositionVideoTarget",
    "DSPCreateSupplierProposedDealCreativeRequirement",
    "DSPCreateSupplierProposedDealCreativeRequirements",
    "DSPCreateSupplierTarget",
    "DSPCreateSupplierTargetDetails",
    "DSPCreateSupplierTargetGroup",
    "DSPCreateTimeOfDay",
    "DSPCreateVideoCreativeRequirements",
    "DSPCurrencyCode",
    "DSPDayOfWeek",
    "DSPDeliveryIntent",
    "DSPDeliveryIntentGoals",
    "DSPDeliveryIntentGoalsExtension",
    "DSPDisplayCreativeRequirements",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPEventType",
    "DSPExtraFrequencyCapImpressionType",
    "DSPFrequency",
    "DSPFrequencyCap",
    "DSPFrequencyTargetingSetting",
    "DSPInventoryType",
    "DSPLanguageIso",
    "DSPPriceComponent",
    "DSPPriceComponentType",
    "DSPSize",
    "DSPSupplierAdProductPrice",
    "DSPSupplierAdProductPriceCreate",
    "DSPSupplierAdProductPriceDescription",
    "DSPSupplierAdProductPriceDescriptionType",
    "DSPSupplierAdProductPriceMultiStatusResponse",
    "DSPSupplierAdProductPriceMultiStatusSuccess",
    "DSPSupplierAppTarget",
    "DSPSupplierAudienceAgeTarget",
    "DSPSupplierAudienceEducationTarget",
    "DSPSupplierAudienceGenderTarget",
    "DSPSupplierAudienceHomeownershipTarget",
    "DSPSupplierAudienceHouseholdCompositionTarget",
    "DSPSupplierAudienceHouseholdIncomeTarget",
    "DSPSupplierAudienceInMarketTarget",
    "DSPSupplierAudienceInterestsTarget",
    "DSPSupplierAudienceMaritalStatusTarget",
    "DSPSupplierAudienceMoodTarget",
    "DSPSupplierAudienceSocioeconomicGroupTarget",
    "DSPSupplierAudienceTarget",
    "DSPSupplierContentCategoryTarget",
    "DSPSupplierContentGenreTarget",
    "DSPSupplierContentRatingTarget",
    "DSPSupplierContentSensitiveCategoryTarget",
    "DSPSupplierDayPartDayTarget",
    "DSPSupplierDayPartTarget",
    "DSPSupplierDayPartTimeTarget",
    "DSPSupplierDeviceOperatingSystemTarget",
    "DSPSupplierDeviceTypeTarget",
    "DSPSupplierGroupDetails",
    "DSPSupplierGroupType",
    "DSPSupplierLocationGroup",
    "DSPSupplierLocationTarget",
    "DSPSupplierPositionVideoTarget",
    "DSPSupplierProposedDealCreativeRequirement",
    "DSPSupplierProposedDealCreativeRequirements",
    "DSPSupplierTarget",
    "DSPSupplierTargetDetails",
    "DSPSupplierTargetGroup",
    "DSPSupplierTargetType",
    "DSPSupplierTargetingDaypartTimezoneType",
    "DSPTimeOfDay",
    "DSPTimeUnit",
    "DSPVideoCreativeRequirements",
]
