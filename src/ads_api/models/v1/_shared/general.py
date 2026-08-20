"""Shared general models reused across entities."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type AdvertisingDealType = Literal["PREFERRED", "PRIVATE_AUCTION", "PROGRAMMATIC_GUARANTEED", "SHARE_OF_VOICE"]


type AmazonPublisherServicesGoalTargetUnit = Literal["MILLICENT", "PERCENTAGE"]


type EventType = Literal["IMPRESSION"]


type IndustryVertical = Literal[
    "AMS Keyword",
    "AMS Self Service",
    "Automotive",
    "Consumer Goods",
    "Entertainment",
    "Financial Services",
    "Hardware & Electronics",
    "Health",
    "House Ads",
    "Public Services",
    "Remnant Networks",
    "Retail Goods & Services",
    "Software",
    "Telecommunications",
    "Travel",
    "Twitch",
    "Twitch TV",
    "Web Media",
    "eCommerce",
]
"""
Supported values:
- `AMS Keyword`: AMS Keyword
- `AMS Self Service`: AMS Self Service
- `Automotive`: Automotive
- `Consumer Goods`: Consumer Goods
- `Entertainment`: Entertainment
- `Financial Services`: Financial Services
- `Hardware & Electronics`: Hardware & Electronics
- `Health`: Health
- `House Ads`: House Ads
- `Public Services`: Public Services
- `Remnant Networks`: Remnant Networks
- `Retail Goods & Services`: Retail Goods & Services
- `Software`: Software
- `Telecommunications`: Telecommunications
- `Travel`: Travel
- `Twitch TV`: Twitch TV
- `Twitch`: Twitch
- `Web Media`: Web Media
- `eCommerce`: eCommerce
"""


type NoteOrigin = Literal["BUYER", "SUPPLIER"]


type SBAdvertisingDealPriceType = Literal["FIXED_PRICE"]
"""
Supported values:
- `FIXED_PRICE`: Sale price for a specific ad placement regardless of auction performance.
"""


type SBCurrencyCode = Literal[
    "AED",
    "AUD",
    "BRL",
    "CAD",
    "CHF",
    "CNY",
    "DKK",
    "EGP",
    "EUR",
    "GBP",
    "INR",
    "JPY",
    "MXN",
    "MXP",
    "NGN",
    "NOK",
    "NZD",
    "PLN",
    "SAR",
    "SEK",
    "SGD",
    "TRY",
    "USD",
    "ZAR",
]
"""
Supported values:
- `AED`: United Arab Emirates Dirham
- `AUD`: Australian Dollar
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `CHF`: Swiss Franc
- `CNY`: Chinese Yuan
- `DKK`: Danish Krone
- `EGP`: Egyptian Pound
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `INR`: Indian Rupee
- `JPY`: Japanese Yen
- `MXN`: Mexican Peso
- `MXP`: Mexican Peso
- `NGN`: Nigerian Naira
- `NOK`: Norwegian Krone
- `NZD`: New Zealand Dollar
- `PLN`: Polish Złoty
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `TRY`: Turkish Lira
- `USD`: United States Dollar
- `ZAR`: South African Rand
"""


type SellingProgram = Literal["AMAZON_AUTHOR", "AMAZON_SELLER", "AMAZON_VENDOR"]


type SortDirection = Literal["ASCENDING", "DESCENDING"]
"""
Supported values:
- `ASCENDING`: Sort in ascending order
- `DESCENDING`: Sort in descending order
"""


type SupplierArchiveReason = Literal[
    "CREATED_ACCIDENTALLY",
    "CREATED_FOR_TESTING",
    "DUPLICATE",
    "NEGOTIATIONS_TERMINATED",
    "NOT_DELIVERING",
    "PROLONGED_PAUSE",
    "UNDERDELIVERING",
]


type SupplierGroupType = Literal["LOCATION"]


type SupplierProposedDealType = Literal["AMAZON_MEDIA"]


type SupplierTargetGroupConstraintType = Literal["LOCATION"]


type TimeUnit = Literal["DAYS", "HOURS", "MINUTES"]


type TimeZone = Literal[
    "AMERICA_ANCHORAGE",
    "AMERICA_CARACAS",
    "AMERICA_CHICAGO",
    "AMERICA_DENVER",
    "AMERICA_HALIFAX",
    "AMERICA_LOS_ANGELES",
    "AMERICA_MEXICO_CITY",
    "AMERICA_NEW_YORK",
    "AMERICA_SAO_PAULO",
    "AMERICA_ST_JOHNS",
    "ASIA_ALMATY",
    "ASIA_BAGHDAD",
    "ASIA_BANGKOK",
    "ASIA_DUBAI",
    "ASIA_HONG_KONG",
    "ASIA_KABUL",
    "ASIA_KATHMANDU",
    "ASIA_KOLKATA",
    "ASIA_MAGADAN",
    "ASIA_RIYADH",
    "ASIA_SHANGHAI",
    "ASIA_SINGAPORE",
    "ASIA_TEHRAN",
    "ASIA_TOKYO",
    "ASIA_YEKATERINBURG",
    "ASIA_YEREVAN",
    "ATLANTIC_AZORES",
    "ATLANTIC_SOUTH_GEORGIA",
    "AUSTRALIA_BRISBANE",
    "AUSTRALIA_DARWIN",
    "AUSTRALIA_SYDNEY",
    "EET",
    "EUROPE_AMSTERDAM",
    "EUROPE_ISTANBUL",
    "EUROPE_LONDON",
    "EUROPE_PARIS",
    "EUROPE_STOCKHOLM",
    "INDIAN_COCOS",
    "PACIFIC_AUCKLAND",
    "PACIFIC_FIJI",
    "PACIFIC_HONOLULU",
    "PACIFIC_KWAJALEIN",
    "PACIFIC_MIDWAY",
    "UTC",
]
"""
Each complies with the ISO 8601 TZ identifier standard

Supported values:
- `AMERICA_ANCHORAGE`: America/Anchorage
- `AMERICA_CARACAS`: America/Caracas
- `AMERICA_CHICAGO`: America/Chicago
- `AMERICA_DENVER`: America/Denver
- `AMERICA_HALIFAX`: America/Halifax
- `AMERICA_LOS_ANGELES`: America/Los_Angeles
- `AMERICA_NEW_YORK`: America/New_York
- `AMERICA_MEXICO_CITY`: America/Mexico_City
- `AMERICA_SAO_PAULO`: America/Sao_Paulo
- `AMERICA_ST_JOHNS`: America/St_Johns
- `ASIA_ALMATY`: Asia/Almaty
- `ASIA_BAGHDAD`: Asia/Baghdad
- `ASIA_BANGKOK`: Asia/Bangkok
- `ASIA_DUBAI`: Asia/Dubai
- `ASIA_HONG_KONG`: Asia/Hong_Kong
- `ASIA_KABUL`: Asia/Kabul
- `ASIA_KATHMANDU`: Asia/Kathmandu
- `ASIA_KOLKATA`: Asia/Kolkata
- `ASIA_MAGADAN`: Asia/Magadan
- `ASIA_RIYADH`: Asia/Riyadh
- `ASIA_SHANGHAI`: Asia/Shanghai
- `ASIA_SINGAPORE`: Asia/Singapore
- `ASIA_TEHRAN`: Asia/Tehran
- `ASIA_TOKYO`: Asia/Tokyo
- `ASIA_YEKATERINBURG`: Asia/Yekaterinburg
- `ASIA_YEREVAN`: Asia/Yerevan
- `ATLANTIC_AZORES`: Atlantic/Azores
- `ATLANTIC_SOUTH_GEORGIA`: Atlantic/South_Georgia
- `AUSTRALIA_BRISBANE`: Australia/Brisbane
- `AUSTRALIA_DARWIN`: Australia/Darwin
- `AUSTRALIA_SYDNEY`: Australia/Sydney
- `EET`: EET
- `EUROPE_AMSTERDAM`: Europe/Amsterdam
- `EUROPE_ISTANBUL`: Europe/Istanbul
- `EUROPE_LONDON`: Europe/London
- `EUROPE_PARIS`: Europe/Paris
- `EUROPE_STOCKHOLM`: Europe/Stockholm
- `INDIAN_COCOS`: Indian/Cocos
- `PACIFIC_FIJI`: Pacific/Fiji
- `PACIFIC_HONOLULU`: Pacific/Honolulu
- `PACIFIC_KWAJALEIN`: Pacific/Kwajalein
- `PACIFIC_MIDWAY`: Pacific/Midway
- `PACIFIC_AUCKLAND`: Pacific/Auckland
- `UTC`: UTC
"""


type TimeZoneIana = Literal[
    "America/Anchorage",
    "America/Caracas",
    "America/Chicago",
    "America/Denver",
    "America/Halifax",
    "America/Los_Angeles",
    "America/Mexico_City",
    "America/New_York",
    "America/Sao_Paulo",
    "America/St_Johns",
    "Asia/Almaty",
    "Asia/Baghdad",
    "Asia/Bangkok",
    "Asia/Dubai",
    "Asia/Hong_Kong",
    "Asia/Kabul",
    "Asia/Kathmandu",
    "Asia/Kolkata",
    "Asia/Magadan",
    "Asia/Riyadh",
    "Asia/Shanghai",
    "Asia/Singapore",
    "Asia/Tehran",
    "Asia/Tokyo",
    "Asia/Yekaterinburg",
    "Asia/Yerevan",
    "Atlantic/Azores",
    "Atlantic/South_Georgia",
    "Australia/Brisbane",
    "Australia/Darwin",
    "Australia/Sydney",
    "EET",
    "Europe/Amsterdam",
    "Europe/Istanbul",
    "Europe/London",
    "Europe/Paris",
    "Europe/Stockholm",
    "Indian/Cocos",
    "Pacific/Auckland",
    "Pacific/Fiji",
    "Pacific/Honolulu",
    "Pacific/Kwajalein",
    "Pacific/Midway",
]
"""
Each enum member is in the IANA Time Zone Database

Supported values:
- `America/Anchorage`: Alaska Time Zone (UTC-09:00)
- `America/Caracas`: Venezuela Time Zone (UTC-04:00)
- `America/Chicago`: Central Time Zone (UTC-06:00)
- `America/Denver`: Mountain Time Zone (UTC-07:00)
- `America/Halifax`: Atlantic Time Zone (UTC-04:00)
- `America/Los_Angeles`: Pacific Time Zone (UTC-08:00)
- `America/Mexico_City`: Central Mexico Time Zone (UTC-06:00)
- `America/New_York`: Eastern Time Zone (UTC-05:00)
- `America/Sao_Paulo`: Brasilia Time Zone (UTC-03:00)
- `America/St_Johns`: Newfoundland Time Zone (UTC-03:30)
- `Asia/Almaty`: Kazakhstan Time Zone (UTC+06:00)
- `Asia/Baghdad`: Arabian Time Zone (UTC+03:00)
- `Asia/Bangkok`: Indochina Time Zone (UTC+07:00)
- `Asia/Dubai`: Gulf Time Zone (UTC+04:00)
- `Asia/Hong_Kong`: Hong Kong Time Zone (UTC+08:00)
- `Asia/Kabul`: Afghanistan Time Zone (UTC+04:30)
- `Asia/Kathmandu`: Nepal Time Zone (UTC+05:45)
- `Asia/Kolkata`: India Time Zone (UTC+05:30)
- `Asia/Magadan`: Magadan Time Zone (UTC+11:00)
- `Asia/Riyadh`: Saudi Arabia Time Zone (UTC+03:00)
- `Asia/Shanghai`: China Time Zone (UTC+08:00)
- `Asia/Singapore`: Singapore Time Zone (UTC+08:00)
- `Asia/Tehran`: Iran Time Zone (UTC+03:30)
- `Asia/Tokyo`: Japan Time Zone (UTC+09:00)
- `Asia/Yekaterinburg`: Yekaterinburg Time Zone (UTC+05:00)
- `Asia/Yerevan`: Armenia Time Zone (UTC+04:00)
- `Atlantic/Azores`: Azores Time Zone (UTC-01:00)
- `Atlantic/South_Georgia`: South Georgia Time Zone (UTC-02:00)
- `Australia/Brisbane`: Australian Eastern Time Zone (UTC+10:00)
- `Australia/Darwin`: Australian Central Time Zone (UTC+09:30)
- `Australia/Sydney`: Australian Eastern Time Zone (UTC+10:00/+11:00)
- `EET`: Eastern European Time Zone (UTC+02:00)
- `Europe/Amsterdam`: Central European Time Zone (UTC+01:00)
- `Europe/Istanbul`: Turkey Time Zone (UTC+03:00)
- `Europe/London`: British Time Zone (UTC+00:00)
- `Europe/Paris`: Central European Time Zone (UTC+01:00)
- `Europe/Stockholm`: Central European Time Zone (UTC+01:00)
- `Indian/Cocos`: Cocos Islands Time Zone (UTC+06:30)
- `Pacific/Auckland`: New Zealand Time Zone (UTC+12:00/+13:00)
- `Pacific/Fiji`: Fiji Time Zone (UTC+12:00)
- `Pacific/Honolulu`: Hawaii Time Zone (UTC-10:00)
- `Pacific/Kwajalein`: Marshall Islands Time Zone (UTC+12:00)
- `Pacific/Midway`: Samoa Time Zone (UTC-11:00)
"""


class Address(LenientModel):
    """The business address of advertising account."""

    addressLine1: str = Field(description="The address details - 1 of business.")
    addressLine2: str | None = Field(default=None, description="The address details - 2 of business.")
    businessName: str = Field(description="The name of business.")
    city: str = Field(description="The city where business is located.")
    countryCode: str = Field(description="The country where business is located.")
    phoneNumber: str | None = Field(default=None, description="The phone number of business.")
    state: str | None = Field(default=None, description="The city where business is located.")
    zipCode: str | None = Field(default=None, description="The zipCode where business is located.")


class AudioCreativeRequirements(LenientModel):
    """Audio creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for audio creatives in milliseconds.")


class BusinessDetail(LenientModel):
    """The business details of advertising account."""

    address: Address | None = Field(default=None)
    addressToken: str | None = Field(default=None, description="The token of the business address being linked.")
    businessRegistrationNumber: str | None = Field(
        default=None, description="The business registration number of the business."
    )
    website: str | None = Field(default=None, description="The website of the business.")


class CreateAddress(StrictModel):
    """The business address of advertising account."""

    addressLine1: str = Field(description="The address details - 1 of business.")
    addressLine2: str | None = Field(default=None, description="The address details - 2 of business.")
    businessName: str = Field(description="The name of business.")
    city: str = Field(description="The city where business is located.")
    countryCode: str = Field(description="The country where business is located.")
    phoneNumber: str | None = Field(default=None, description="The phone number of business.")
    state: str | None = Field(default=None, description="The city where business is located.")
    zipCode: str | None = Field(default=None, description="The zipCode where business is located.")


class CreateAmazonMediaProposedDealExtension(StrictModel):
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


class CreateAudioCreativeRequirements(StrictModel):
    """Audio creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for audio creatives in milliseconds.")


class CreateBusinessDetail(StrictModel):
    """The business details of advertising account."""

    address: CreateAddress | None = Field(default=None)
    addressToken: str | None = Field(default=None, description="The token of the business address being linked.")
    businessRegistrationNumber: str | None = Field(
        default=None, description="The business registration number of the business."
    )
    website: str | None = Field(default=None, description="The website of the business.")


class CreateDisplayCreativeRequirements(StrictModel):
    """Display creative requirements."""

    size: CreateSize | None = Field(default=None)


class CreateNotes(StrictModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: NoteOrigin


class CreateSize(StrictModel):
    height: int = Field(description="The height of the creative placement.")
    width: int = Field(description="The width of the creative placement.")


class CreateSupplierAppTarget(StrictModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class CreateSupplierAudienceAgeTarget(StrictModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class CreateSupplierAudienceEducationTarget(StrictModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class CreateSupplierAudienceGenderTarget(StrictModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class CreateSupplierAudienceHomeownershipTarget(StrictModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class CreateSupplierAudienceHouseholdCompositionTarget(StrictModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class CreateSupplierAudienceHouseholdIncomeTarget(StrictModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class CreateSupplierAudienceInMarketTarget(StrictModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class CreateSupplierAudienceInterestsTarget(StrictModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class CreateSupplierAudienceMaritalStatusTarget(StrictModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class CreateSupplierAudienceMoodTarget(StrictModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class CreateSupplierAudienceSocioeconomicGroupTarget(StrictModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class CreateSupplierAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class CreateSupplierContentCategoryTarget(StrictModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class CreateSupplierContentGenreTarget(StrictModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class CreateSupplierContentRatingTarget(StrictModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class CreateSupplierContentSensitiveCategoryTarget(StrictModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class CreateSupplierDayPartDayTarget(StrictModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class CreateSupplierDayPartTimeTarget(StrictModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class CreateSupplierDeviceOperatingSystemTarget(StrictModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class CreateSupplierDeviceTypeTarget(StrictModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class CreateSupplierGroupDetails(StrictModel):
    supplierLocationGroup: CreateSupplierLocationGroup


class CreateSupplierLocationGroup(StrictModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class CreateSupplierLocationTarget(StrictModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class CreateSupplierPositionVideoTarget(StrictModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class CreateSupplierProposedDealExtension(StrictModel):
    amazonMediaProposedDealExtension: CreateAmazonMediaProposedDealExtension


class CreateSupplierStateReason(StrictModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: SupplierArchiveReason | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class CreateTimeOfDay(StrictModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class CreateVideoCreativeRequirements(StrictModel):
    """Video creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for video creatives in milliseconds.")
    size: CreateSize | None = Field(default=None)


class DisplayCreativeRequirements(LenientModel):
    """Display creative requirements."""

    size: Size | None = Field(default=None)


class ForecastSummary(LenientModel):
    impressionsForecastSummary: ImpressionsForecastSummary


class ImpressionsForecastSummary(LenientModel):
    """Forecast summary for impressions."""

    availableImpressions: int = Field(
        ge=0, le=9223372036854776000, description="The total impressions available for purchase."
    )


class SBAdvertisingDealPrice(LenientModel):
    currencyCode: SBCurrencyCode | str
    priceType: SBAdvertisingDealPriceType | str
    value: float = Field(description="The monetary amount of the price in the given currency.")


class Size(LenientModel):
    height: int = Field(description="The height of the creative placement.")
    width: int = Field(description="The width of the creative placement.")


class SubmissionFailure(LenientModel):
    """Information about submission failure."""

    failures: list[SubmissionFailureField] | None = Field(
        default=None, min_length=0, max_length=49, description="List of submission failure details."
    )
    traceId: str | None = Field(default=None, description="Trace identifier for the submission failure.")


class SubmissionFailureField(LenientModel):
    """Details of a specific submission failure."""

    code: str | None = Field(default=None, description="The failure code.")
    message: str | None = Field(default=None, description="The failure message.")


class SupplierAdProductBookingConstraints(LenientModel):
    """Booking constraints are the dates in which an advertiser can create a proposed deal. If an advertiser attempts to create a proposed deal outside of the booking constraint dates, an error will be returned by the supplier."""

    range: SupplierBookingRangeConstraint | None = Field(default=None)


class SupplierAdProductFlightConstraints(LenientModel):
    """Flight constraints limit the startDateTime and endDateTime on a proposed deal."""

    fixed: SupplierFlightFixedConstraint | None = Field(default=None)
    range: SupplierFlightRangeConstraint | None = Field(default=None)


class SupplierAdProductShareOfVoiceConstraints(LenientModel):
    fixed: SupplierShareOfVoiceFixedConstraint | None = Field(default=None)
    range: SupplierShareOfVoiceRangeConstraint | None = Field(default=None)


class SupplierBookingRangeConstraint(LenientModel):
    maxDateTime: datetime | None = Field(
        default=None, description="Latest date that this product can be booked as a deal."
    )
    minDateTime: datetime = Field(description="Earliest date that this product can be booked as a deal.")


class SupplierFlightFixedConstraint(LenientModel):
    endDateTime: datetime = Field(description="Fixed end date for deals.")
    startDateTime: datetime = Field(description="Fixed start date for deals.")


class SupplierFlightRangeConstraint(LenientModel):
    maxDateTime: datetime | None = Field(default=None, description="Latest date that deals can execute.")
    maxHours: int | None = Field(default=None, description="Maximum number of hours a deal can run.")
    minDateTime: datetime = Field(description="Earliest date that deals can execute.")
    minHours: int | None = Field(default=None, description="Minimum number of hours a deal must run.")


class SupplierFrequencyRangeConstraint(LenientModel):
    maxCount: int | None = Field(default=None, description="Maximum number of frequency intents allowed.")
    minCount: int | None = Field(default=None, description="Minimum number of frequency intents allowed.")


class SupplierShareOfVoiceFixedConstraint(LenientModel):
    percent: float = Field(description="Fixed percentage of inventory elements.")


class SupplierShareOfVoiceRangeConstraint(LenientModel):
    maxPercent: float | None = Field(default=None, description="Maximum percentage of inventory elements.")
    minPercent: float | None = Field(default=None, description="Minimum percentage of inventory elements.")
    percentIncrement: float | None = Field(default=None, description="Percentage increments for deals.")


class SupplierTargetConstraintLocationDetails(LenientModel):
    allowsRealTimeLocationOnly: bool = Field(
        description="Allows use of onlyUseRealTimeLocation in location targets for this supplier ad product. When enabled, targets customers based only on their real-time location rather than home location. Targeting based on home location may deliver when customers travel and their real-time location is outside the targeted locations, which can lead to discrepancies with reports that validate location based on real-time location."
    )


class SupplierTargetGroupConstraintDetails(LenientModel):
    supplierTargetConstraintLocationDetails: SupplierTargetConstraintLocationDetails


class SupplierTargetValueConstraint(LenientModel):
    maxValues: int | None = Field(
        default=None,
        description="Maximum number of supplier targets of a supplier target type for a proposed deal. If this value is not present, then the max is limited by the schema of SupplierProposedDeal.",
    )
    minValues: int | None = Field(
        default=None,
        description="Minimum number of supplier targets of a supplier target type for a proposed deal. If this value is not present, then there is no minimum.",
    )


class UpdateSupplierStateReason(StrictModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: SupplierArchiveReason | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class VideoCreativeRequirements(LenientModel):
    """Video creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for video creatives in milliseconds.")
    size: Size | None = Field(default=None)


__all__ = [
    "Address",
    "AdvertisingDealType",
    "AmazonPublisherServicesGoalTargetUnit",
    "AudioCreativeRequirements",
    "BusinessDetail",
    "CreateAddress",
    "CreateAmazonMediaProposedDealExtension",
    "CreateAudioCreativeRequirements",
    "CreateBusinessDetail",
    "CreateDisplayCreativeRequirements",
    "CreateNotes",
    "CreateSize",
    "CreateSupplierAppTarget",
    "CreateSupplierAudienceAgeTarget",
    "CreateSupplierAudienceEducationTarget",
    "CreateSupplierAudienceGenderTarget",
    "CreateSupplierAudienceHomeownershipTarget",
    "CreateSupplierAudienceHouseholdCompositionTarget",
    "CreateSupplierAudienceHouseholdIncomeTarget",
    "CreateSupplierAudienceInMarketTarget",
    "CreateSupplierAudienceInterestsTarget",
    "CreateSupplierAudienceMaritalStatusTarget",
    "CreateSupplierAudienceMoodTarget",
    "CreateSupplierAudienceSocioeconomicGroupTarget",
    "CreateSupplierAudienceTarget",
    "CreateSupplierContentCategoryTarget",
    "CreateSupplierContentGenreTarget",
    "CreateSupplierContentRatingTarget",
    "CreateSupplierContentSensitiveCategoryTarget",
    "CreateSupplierDayPartDayTarget",
    "CreateSupplierDayPartTimeTarget",
    "CreateSupplierDeviceOperatingSystemTarget",
    "CreateSupplierDeviceTypeTarget",
    "CreateSupplierGroupDetails",
    "CreateSupplierLocationGroup",
    "CreateSupplierLocationTarget",
    "CreateSupplierPositionVideoTarget",
    "CreateSupplierProposedDealExtension",
    "CreateSupplierStateReason",
    "CreateTimeOfDay",
    "CreateVideoCreativeRequirements",
    "DisplayCreativeRequirements",
    "EventType",
    "ForecastSummary",
    "ImpressionsForecastSummary",
    "IndustryVertical",
    "NoteOrigin",
    "SBAdvertisingDealPrice",
    "SBAdvertisingDealPriceType",
    "SBCurrencyCode",
    "SellingProgram",
    "Size",
    "SortDirection",
    "SubmissionFailure",
    "SubmissionFailureField",
    "SupplierAdProductBookingConstraints",
    "SupplierAdProductFlightConstraints",
    "SupplierAdProductShareOfVoiceConstraints",
    "SupplierArchiveReason",
    "SupplierBookingRangeConstraint",
    "SupplierFlightFixedConstraint",
    "SupplierFlightRangeConstraint",
    "SupplierFrequencyRangeConstraint",
    "SupplierGroupType",
    "SupplierProposedDealType",
    "SupplierShareOfVoiceFixedConstraint",
    "SupplierShareOfVoiceRangeConstraint",
    "SupplierTargetConstraintLocationDetails",
    "SupplierTargetGroupConstraintDetails",
    "SupplierTargetGroupConstraintType",
    "SupplierTargetValueConstraint",
    "TimeUnit",
    "TimeZone",
    "TimeZoneIana",
    "UpdateSupplierStateReason",
    "VideoCreativeRequirements",
]
