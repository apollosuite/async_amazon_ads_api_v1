"""Shared dsp models reused across entities."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class DSPAdvertisingDealType(StrEnum):
    PREFERRED = "PREFERRED"
    PRIVATE_AUCTION = "PRIVATE_AUCTION"
    PROGRAMMATIC_GUARANTEED = "PROGRAMMATIC_GUARANTEED"
    SHARE_OF_VOICE = "SHARE_OF_VOICE"


class DSPAmazonPublisherServicesGoalTargetUnit(StrEnum):
    MILLICENT = "MILLICENT"
    PERCENTAGE = "PERCENTAGE"


class DSPBudgetType(StrEnum):
    MONETARY = "MONETARY"


class DSPDVBrandSafetyAppAgeRatingType(StrEnum):
    ADULTS_ONLY_18_PLUS = "ADULTS_ONLY_18_PLUS"
    EVERYONE_4_PLUS = "EVERYONE_4_PLUS"
    MATURE_17_PLUS = "MATURE_17_PLUS"
    TEENS_12_PLUS = "TEENS_12_PLUS"
    TWEENS_9_PLUS = "TWEENS_9_PLUS"
    UNKNOWN = "UNKNOWN"


class DSPDVBrandSafetyContentCategoryType(StrEnum):
    AD_SERVER = "AD_SERVER"
    CELEBRITY_GOSSIP = "CELEBRITY_GOSSIP"
    CULTS_SURVIVALISM = "CULTS_SURVIVALISM"
    EXTREME_GRAPHIC = "EXTREME_GRAPHIC"
    GAMBLING = "GAMBLING"
    INCENTIVIZED_MALWARE_CLUTTER = "INCENTIVIZED_MALWARE_CLUTTER"
    INFLAMMATORY_POLITICS_NEWS = "INFLAMMATORY_POLITICS_NEWS"
    NEGATIVE_NEWS_FINANCIAL = "NEGATIVE_NEWS_FINANCIAL"
    NEGATIVE_NEWS_PHARMACEUTICAL = "NEGATIVE_NEWS_PHARMACEUTICAL"
    NON_STANDARD_CONTENT_NON_ENGLISH = "NON_STANDARD_CONTENT_NON_ENGLISH"
    NON_STANDARD_CONTENT_PARKING_PAGE = "NON_STANDARD_CONTENT_PARKING_PAGE"
    OCCULT = "OCCULT"
    PIRACY_COPYRIGHT_INFRINGEMENT = "PIRACY_COPYRIGHT_INFRINGEMENT"
    UNMODERATED_UGC_FORUMS_IMAGES_VIDEO = "UNMODERATED_UGC_FORUMS_IMAGES_VIDEO"


class DSPEventType(StrEnum):
    IMPRESSION = "IMPRESSION"


class DSPExcludeAppsAndSitesType(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_TRAFFIC_LEVEL_GTE_02 = "FRAUD_TRAFFIC_LEVEL_GTE_02"
    FRAUD_TRAFFIC_LEVEL_GTE_04 = "FRAUD_TRAFFIC_LEVEL_GTE_04"
    FRAUD_TRAFFIC_LEVEL_GTE_06 = "FRAUD_TRAFFIC_LEVEL_GTE_06"
    FRAUD_TRAFFIC_LEVEL_GTE_08 = "FRAUD_TRAFFIC_LEVEL_GTE_08"
    FRAUD_TRAFFIC_LEVEL_GTE_10 = "FRAUD_TRAFFIC_LEVEL_GTE_10"
    FRAUD_TRAFFIC_LEVEL_GTE_100 = "FRAUD_TRAFFIC_LEVEL_GTE_100"
    FRAUD_TRAFFIC_LEVEL_GTE_25 = "FRAUD_TRAFFIC_LEVEL_GTE_25"
    FRAUD_TRAFFIC_LEVEL_GTE_50 = "FRAUD_TRAFFIC_LEVEL_GTE_50"


class DSPFeesThirdPartyProvider(StrEnum):
    COM_SCORE = "COM_SCORE"
    CPM_1 = "CPM_1"
    CPM_2 = "CPM_2"
    CPM_3 = "CPM_3"
    DOUBLE_CLICK_CAMPAIGN_MANAGER = "DOUBLE_CLICK_CAMPAIGN_MANAGER"
    DOUBLE_VERIFY = "DOUBLE_VERIFY"
    INTEGRAL_AD_SCIENCE = "INTEGRAL_AD_SCIENCE"


class DSPMarketplaceScope(StrEnum):
    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"


class DSPNewsGuardBrandGuardMisinformationSafetyType(StrEnum):
    AI_GENERATED_MFA = "AI_GENERATED_MFA"
    BASIC_EXCLUDE = "BASIC_EXCLUDE"
    CLIMATE_MISINFORMATION = "CLIMATE_MISINFORMATION"
    COVID_MISINFORMATION = "COVID_MISINFORMATION"
    ELECTION_MISINFORMATION = "ELECTION_MISINFORMATION"
    HEALTH_MISINFORMATION = "HEALTH_MISINFORMATION"
    HIGH_EXCLUDE = "HIGH_EXCLUDE"
    ISRAEL_HAMAS_MISINFORMATION = "ISRAEL_HAMAS_MISINFORMATION"
    MAX_EXCLUDE = "MAX_EXCLUDE"
    MISINFORMATION_SITES = "MISINFORMATION_SITES"
    OPINIONATED_NEWS = "OPINIONATED_NEWS"
    QANON_MISINFORMATION = "QANON_MISINFORMATION"
    UKRAINE_MISINFORMATION = "UKRAINE_MISINFORMATION"
    VACCINE_MISINFORMATION = "VACCINE_MISINFORMATION"


class DSPNewsGuardBrandGuardTrustedNewsTargetingType(StrEnum):
    BASIC_INCLUDE = "BASIC_INCLUDE"
    BUSINESS_INCLUDE = "BUSINESS_INCLUDE"
    COMMUNITY_INCLUDE = "COMMUNITY_INCLUDE"
    HEALTH_INCLUDE = "HEALTH_INCLUDE"
    HIGH_INCLUDE = "HIGH_INCLUDE"
    LIFESTYLE_INCLUDE = "LIFESTYLE_INCLUDE"
    LOCAL_INCLUDE = "LOCAL_INCLUDE"
    MAX_INCLUDE = "MAX_INCLUDE"
    POLITICS_INCLUDE = "POLITICS_INCLUDE"
    TECH_INCLUDE = "TECH_INCLUDE"


class DSPNoteOrigin(StrEnum):
    BUYER = "BUYER"
    SUPPLIER = "SUPPLIER"


class DSPRecurrence(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"
    MONTHLY = "MONTHLY"


class DSPSortDirection(StrEnum):
    ASCENDING = "ASCENDING"  # Sort in ascending order
    DESCENDING = "DESCENDING"  # Sort in descending order


class DSPSupplierArchiveReason(StrEnum):
    CREATED_ACCIDENTALLY = "CREATED_ACCIDENTALLY"
    CREATED_FOR_TESTING = "CREATED_FOR_TESTING"
    DUPLICATE = "DUPLICATE"
    NEGOTIATIONS_TERMINATED = "NEGOTIATIONS_TERMINATED"
    NOT_DELIVERING = "NOT_DELIVERING"
    PROLONGED_PAUSE = "PROLONGED_PAUSE"
    UNDERDELIVERING = "UNDERDELIVERING"


class DSPSupplierGroupType(StrEnum):
    LOCATION = "LOCATION"


class DSPSupplierProposedDealType(StrEnum):
    AMAZON_MEDIA = "AMAZON_MEDIA"


class DSPSupplierTargetGroupConstraintType(StrEnum):
    LOCATION = "LOCATION"


class DSPTimeUnit(StrEnum):
    DAYS = "DAYS"
    HOURS = "HOURS"
    MINUTES = "MINUTES"


class DSPTimeZone(StrEnum):
    """
    Each complies with the ISO 8601 TZ identifier standard
    """

    AMERICA_ANCHORAGE = "AMERICA_ANCHORAGE"  # America/Anchorage
    AMERICA_CARACAS = "AMERICA_CARACAS"  # America/Caracas
    AMERICA_CHICAGO = "AMERICA_CHICAGO"  # America/Chicago
    AMERICA_DENVER = "AMERICA_DENVER"  # America/Denver
    AMERICA_HALIFAX = "AMERICA_HALIFAX"  # America/Halifax
    AMERICA_LOS_ANGELES = "AMERICA_LOS_ANGELES"  # America/Los_Angeles
    AMERICA_MEXICO_CITY = "AMERICA_MEXICO_CITY"  # America/Mexico_City
    AMERICA_NEW_YORK = "AMERICA_NEW_YORK"  # America/New_York
    AMERICA_SAO_PAULO = "AMERICA_SAO_PAULO"  # America/Sao_Paulo
    AMERICA_ST_JOHNS = "AMERICA_ST_JOHNS"  # America/St_Johns
    ASIA_ALMATY = "ASIA_ALMATY"  # Asia/Almaty
    ASIA_BAGHDAD = "ASIA_BAGHDAD"  # Asia/Baghdad
    ASIA_BANGKOK = "ASIA_BANGKOK"  # Asia/Bangkok
    ASIA_DUBAI = "ASIA_DUBAI"  # Asia/Dubai
    ASIA_HONG_KONG = "ASIA_HONG_KONG"  # Asia/Hong_Kong
    ASIA_KABUL = "ASIA_KABUL"  # Asia/Kabul
    ASIA_KATHMANDU = "ASIA_KATHMANDU"  # Asia/Kathmandu
    ASIA_KOLKATA = "ASIA_KOLKATA"  # Asia/Kolkata
    ASIA_MAGADAN = "ASIA_MAGADAN"  # Asia/Magadan
    ASIA_RIYADH = "ASIA_RIYADH"  # Asia/Riyadh
    ASIA_SHANGHAI = "ASIA_SHANGHAI"  # Asia/Shanghai
    ASIA_SINGAPORE = "ASIA_SINGAPORE"  # Asia/Singapore
    ASIA_TEHRAN = "ASIA_TEHRAN"  # Asia/Tehran
    ASIA_TOKYO = "ASIA_TOKYO"  # Asia/Tokyo
    ASIA_YEKATERINBURG = "ASIA_YEKATERINBURG"  # Asia/Yekaterinburg
    ASIA_YEREVAN = "ASIA_YEREVAN"  # Asia/Yerevan
    ATLANTIC_AZORES = "ATLANTIC_AZORES"  # Atlantic/Azores
    ATLANTIC_SOUTH_GEORGIA = "ATLANTIC_SOUTH_GEORGIA"  # Atlantic/South_Georgia
    AUSTRALIA_BRISBANE = "AUSTRALIA_BRISBANE"  # Australia/Brisbane
    AUSTRALIA_DARWIN = "AUSTRALIA_DARWIN"  # Australia/Darwin
    AUSTRALIA_SYDNEY = "AUSTRALIA_SYDNEY"  # Australia/Sydney
    EET = "EET"  # EET
    EUROPE_AMSTERDAM = "EUROPE_AMSTERDAM"  # Europe/Amsterdam
    EUROPE_ISTANBUL = "EUROPE_ISTANBUL"  # Europe/Istanbul
    EUROPE_LONDON = "EUROPE_LONDON"  # Europe/London
    EUROPE_PARIS = "EUROPE_PARIS"  # Europe/Paris
    EUROPE_STOCKHOLM = "EUROPE_STOCKHOLM"  # Europe/Stockholm
    INDIAN_COCOS = "INDIAN_COCOS"  # Indian/Cocos
    PACIFIC_AUCKLAND = "PACIFIC_AUCKLAND"  # Pacific/Auckland
    PACIFIC_FIJI = "PACIFIC_FIJI"  # Pacific/Fiji
    PACIFIC_HONOLULU = "PACIFIC_HONOLULU"  # Pacific/Honolulu
    PACIFIC_KWAJALEIN = "PACIFIC_KWAJALEIN"  # Pacific/Kwajalein
    PACIFIC_MIDWAY = "PACIFIC_MIDWAY"  # Pacific/Midway
    UTC = "UTC"  # UTC


class DSPAudioCreativeRequirements(LenientModel):
    """Audio creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for audio creatives in milliseconds.")


class DSPCreateAmazonMediaProposedDealExtension(StrictModel):
    """Amazon Media specific proposed deal attributes."""

    brandName: str | None = Field(
        default=None, pattern="^[ -:<-z|]+$", description="The brand name associated with the deals buyer."
    )
    productCategoryId: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="A list of ADSP product categories. Only required for PG deals.",
    )


class DSPCreateAudioCreativeRequirements(StrictModel):
    """Audio creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for audio creatives in milliseconds.")


class DSPCreateDisplayCreativeRequirements(StrictModel):
    """Display creative requirements."""

    size: DSPCreateSize | None = Field(default=None)


class DSPCreateNotes(StrictModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: Annotated[DSPNoteOrigin | str, lenient_enum(DSPNoteOrigin)]


class DSPCreateSize(StrictModel):
    height: int = Field(description="The height of the creative placement.")
    width: int = Field(description="The width of the creative placement.")


class DSPCreateSupplierAppTarget(StrictModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class DSPCreateSupplierAudienceAgeTarget(StrictModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class DSPCreateSupplierAudienceEducationTarget(StrictModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class DSPCreateSupplierAudienceGenderTarget(StrictModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class DSPCreateSupplierAudienceHomeownershipTarget(StrictModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class DSPCreateSupplierAudienceHouseholdCompositionTarget(StrictModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class DSPCreateSupplierAudienceHouseholdIncomeTarget(StrictModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class DSPCreateSupplierAudienceInMarketTarget(StrictModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class DSPCreateSupplierAudienceInterestsTarget(StrictModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class DSPCreateSupplierAudienceMaritalStatusTarget(StrictModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class DSPCreateSupplierAudienceMoodTarget(StrictModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class DSPCreateSupplierAudienceSocioeconomicGroupTarget(StrictModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class DSPCreateSupplierAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class DSPCreateSupplierContentCategoryTarget(StrictModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class DSPCreateSupplierContentGenreTarget(StrictModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class DSPCreateSupplierContentRatingTarget(StrictModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class DSPCreateSupplierContentSensitiveCategoryTarget(StrictModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class DSPCreateSupplierDayPartDayTarget(StrictModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class DSPCreateSupplierDayPartTimeTarget(StrictModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class DSPCreateSupplierDeviceOperatingSystemTarget(StrictModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class DSPCreateSupplierDeviceTypeTarget(StrictModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class DSPCreateSupplierGroupDetails(StrictModel):
    supplierLocationGroup: DSPCreateSupplierLocationGroup


class DSPCreateSupplierLocationGroup(StrictModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class DSPCreateSupplierLocationTarget(StrictModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class DSPCreateSupplierPositionVideoTarget(StrictModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class DSPCreateSupplierProposedDealExtension(StrictModel):
    amazonMediaProposedDealExtension: DSPCreateAmazonMediaProposedDealExtension


class DSPCreateSupplierStateReason(StrictModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: Annotated[DSPSupplierArchiveReason | str, lenient_enum(DSPSupplierArchiveReason)] | None = Field(
        default=None
    )
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class DSPCreateTag(StrictModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPCreateTimeOfDay(StrictModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPCreateVideoCreativeRequirements(StrictModel):
    """Video creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for video creatives in milliseconds.")
    size: DSPCreateSize | None = Field(default=None)


class DSPDisplayCreativeRequirements(LenientModel):
    """Display creative requirements."""

    size: DSPSize | None = Field(default=None)


class DSPForecastSummary(LenientModel):
    impressionsForecastSummary: DSPImpressionsForecastSummary


class DSPImpressionsForecastSummary(LenientModel):
    """Forecast summary for impressions."""

    availableImpressions: int = Field(
        ge=0, le=9223372036854776000, description="The total impressions available for purchase."
    )


class DSPMarketplaceStringValue(StrictModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class DSPMarketplaceStringValueOut(LenientModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class DSPSize(LenientModel):
    height: int = Field(description="The height of the creative placement.")
    width: int = Field(description="The width of the creative placement.")


class DSPSubmissionFailure(LenientModel):
    """Information about submission failure."""

    failures: list[DSPSubmissionFailureField] | None = Field(
        default=None, min_length=0, max_length=49, description="List of submission failure details."
    )
    traceId: str | None = Field(default=None, description="Trace identifier for the submission failure.")


class DSPSubmissionFailureField(LenientModel):
    """Details of a specific submission failure."""

    code: str | None = Field(default=None, description="The failure code.")
    message: str | None = Field(default=None, description="The failure message.")


class DSPSupplierAdProductBookingConstraints(LenientModel):
    """Booking constraints are the dates in which an advertiser can create a proposed deal. If an advertiser attempts to create a proposed deal outside of the booking constraint dates, an error will be returned by the supplier."""

    range: DSPSupplierBookingRangeConstraint | None = Field(default=None)


class DSPSupplierAdProductFlightConstraints(LenientModel):
    """Flight constraints limit the startDateTime and endDateTime on a proposed deal."""

    fixed: DSPSupplierFlightFixedConstraint | None = Field(default=None)
    range: DSPSupplierFlightRangeConstraint | None = Field(default=None)


class DSPSupplierAdProductShareOfVoiceConstraints(LenientModel):
    fixed: DSPSupplierShareOfVoiceFixedConstraint | None = Field(default=None)
    range: DSPSupplierShareOfVoiceRangeConstraint | None = Field(default=None)


class DSPSupplierBookingRangeConstraint(LenientModel):
    maxDateTime: datetime | None = Field(
        default=None, description="Latest date that this product can be booked as a deal."
    )
    minDateTime: datetime = Field(description="Earliest date that this product can be booked as a deal.")


class DSPSupplierFlightFixedConstraint(LenientModel):
    endDateTime: datetime = Field(description="Fixed end date for deals.")
    startDateTime: datetime = Field(description="Fixed start date for deals.")


class DSPSupplierFlightRangeConstraint(LenientModel):
    maxDateTime: datetime | None = Field(default=None, description="Latest date that deals can execute.")
    maxHours: int | None = Field(default=None, description="Maximum number of hours a deal can run.")
    minDateTime: datetime = Field(description="Earliest date that deals can execute.")
    minHours: int | None = Field(default=None, description="Minimum number of hours a deal must run.")


class DSPSupplierFrequencyRangeConstraint(LenientModel):
    maxCount: int | None = Field(default=None, description="Maximum number of frequency intents allowed.")
    minCount: int | None = Field(default=None, description="Minimum number of frequency intents allowed.")


class DSPSupplierShareOfVoiceFixedConstraint(LenientModel):
    percent: float = Field(description="Fixed percentage of inventory elements.")


class DSPSupplierShareOfVoiceRangeConstraint(LenientModel):
    maxPercent: float | None = Field(default=None, description="Maximum percentage of inventory elements.")
    minPercent: float | None = Field(default=None, description="Minimum percentage of inventory elements.")
    percentIncrement: float | None = Field(default=None, description="Percentage increments for deals.")


class DSPSupplierTargetConstraintLocationDetails(LenientModel):
    allowsRealTimeLocationOnly: bool = Field(
        description="Allows use of onlyUseRealTimeLocation in location targets for this supplier ad product. When enabled, targets customers based only on their real-time location rather than home location. Targeting based on home location may deliver when customers travel and their real-time location is outside the targeted locations, which can lead to discrepancies with reports that validate location based on real-time location."
    )


class DSPSupplierTargetGroupConstraintDetails(LenientModel):
    supplierTargetConstraintLocationDetails: DSPSupplierTargetConstraintLocationDetails


class DSPSupplierTargetValueConstraint(LenientModel):
    maxValues: int | None = Field(
        default=None,
        description="Maximum number of supplier targets of a supplier target type for a proposed deal. If this value is not present, then the max is limited by the schema of SupplierProposedDeal.",
    )
    minValues: int | None = Field(
        default=None,
        description="Minimum number of supplier targets of a supplier target type for a proposed deal. If this value is not present, then there is no minimum.",
    )


class DSPTimeOfDayOut(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPUpdateSupplierStateReason(StrictModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: Annotated[DSPSupplierArchiveReason | str, lenient_enum(DSPSupplierArchiveReason)] | None = Field(
        default=None
    )
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class DSPVideoCreativeRequirements(LenientModel):
    """Video creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for video creatives in milliseconds.")
    size: DSPSize | None = Field(default=None)


__all__ = [
    "DSPAdvertisingDealType",
    "DSPAmazonPublisherServicesGoalTargetUnit",
    "DSPAudioCreativeRequirements",
    "DSPBudgetType",
    "DSPCreateAmazonMediaProposedDealExtension",
    "DSPCreateAudioCreativeRequirements",
    "DSPCreateDisplayCreativeRequirements",
    "DSPCreateNotes",
    "DSPCreateSize",
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
    "DSPCreateSupplierDayPartTimeTarget",
    "DSPCreateSupplierDeviceOperatingSystemTarget",
    "DSPCreateSupplierDeviceTypeTarget",
    "DSPCreateSupplierGroupDetails",
    "DSPCreateSupplierLocationGroup",
    "DSPCreateSupplierLocationTarget",
    "DSPCreateSupplierPositionVideoTarget",
    "DSPCreateSupplierProposedDealExtension",
    "DSPCreateSupplierStateReason",
    "DSPCreateTag",
    "DSPCreateTimeOfDay",
    "DSPCreateVideoCreativeRequirements",
    "DSPDVBrandSafetyAppAgeRatingType",
    "DSPDVBrandSafetyContentCategoryType",
    "DSPDisplayCreativeRequirements",
    "DSPEventType",
    "DSPExcludeAppsAndSitesType",
    "DSPFeesThirdPartyProvider",
    "DSPForecastSummary",
    "DSPImpressionsForecastSummary",
    "DSPMarketplaceScope",
    "DSPMarketplaceStringValue",
    "DSPMarketplaceStringValueOut",
    "DSPNewsGuardBrandGuardMisinformationSafetyType",
    "DSPNewsGuardBrandGuardTrustedNewsTargetingType",
    "DSPNoteOrigin",
    "DSPRecurrence",
    "DSPSize",
    "DSPSortDirection",
    "DSPSubmissionFailure",
    "DSPSubmissionFailureField",
    "DSPSupplierAdProductBookingConstraints",
    "DSPSupplierAdProductFlightConstraints",
    "DSPSupplierAdProductShareOfVoiceConstraints",
    "DSPSupplierArchiveReason",
    "DSPSupplierBookingRangeConstraint",
    "DSPSupplierFlightFixedConstraint",
    "DSPSupplierFlightRangeConstraint",
    "DSPSupplierFrequencyRangeConstraint",
    "DSPSupplierGroupType",
    "DSPSupplierProposedDealType",
    "DSPSupplierShareOfVoiceFixedConstraint",
    "DSPSupplierShareOfVoiceRangeConstraint",
    "DSPSupplierTargetConstraintLocationDetails",
    "DSPSupplierTargetGroupConstraintDetails",
    "DSPSupplierTargetGroupConstraintType",
    "DSPSupplierTargetValueConstraint",
    "DSPTimeOfDayOut",
    "DSPTimeUnit",
    "DSPTimeZone",
    "DSPUpdateSupplierStateReason",
    "DSPVideoCreativeRequirements",
]
