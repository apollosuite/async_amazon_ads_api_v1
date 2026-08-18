"""Shared general models reused across entities."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type CountryCode = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AL",
    "AM",
    "AO",
    "AQ",
    "AR",
    "AS",
    "AT",
    "AU",
    "AW",
    "AX",
    "AZ",
    "BA",
    "BB",
    "BD",
    "BE",
    "BF",
    "BG",
    "BH",
    "BI",
    "BJ",
    "BL",
    "BM",
    "BN",
    "BO",
    "BQ",
    "BR",
    "BS",
    "BT",
    "BV",
    "BW",
    "BY",
    "BZ",
    "CA",
    "CC",
    "CD",
    "CF",
    "CG",
    "CH",
    "CI",
    "CK",
    "CL",
    "CM",
    "CN",
    "CO",
    "CR",
    "CU",
    "CV",
    "CW",
    "CX",
    "CY",
    "CZ",
    "DE",
    "DJ",
    "DK",
    "DM",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "EH",
    "ER",
    "ES",
    "ET",
    "FI",
    "FJ",
    "FK",
    "FM",
    "FO",
    "FR",
    "GA",
    "GB",
    "GD",
    "GE",
    "GF",
    "GG",
    "GH",
    "GI",
    "GL",
    "GM",
    "GN",
    "GP",
    "GQ",
    "GR",
    "GS",
    "GT",
    "GU",
    "GW",
    "GY",
    "HK",
    "HM",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IE",
    "IL",
    "IM",
    "IN",
    "IO",
    "IQ",
    "IR",
    "IS",
    "IT",
    "JE",
    "JM",
    "JO",
    "JP",
    "KE",
    "KG",
    "KH",
    "KI",
    "KM",
    "KN",
    "KP",
    "KR",
    "KW",
    "KY",
    "KZ",
    "LA",
    "LB",
    "LC",
    "LI",
    "LK",
    "LR",
    "LS",
    "LT",
    "LU",
    "LV",
    "LY",
    "MA",
    "MC",
    "MD",
    "ME",
    "MF",
    "MG",
    "MH",
    "MK",
    "ML",
    "MM",
    "MN",
    "MO",
    "MP",
    "MQ",
    "MR",
    "MS",
    "MT",
    "MU",
    "MV",
    "MW",
    "MX",
    "MY",
    "MZ",
    "NA",
    "NC",
    "NE",
    "NF",
    "NG",
    "NI",
    "NL",
    "NO",
    "NP",
    "NR",
    "NU",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PF",
    "PG",
    "PH",
    "PK",
    "PL",
    "PM",
    "PN",
    "PR",
    "PS",
    "PT",
    "PW",
    "PY",
    "QA",
    "RE",
    "RO",
    "RS",
    "RU",
    "RW",
    "SA",
    "SB",
    "SC",
    "SD",
    "SE",
    "SG",
    "SH",
    "SI",
    "SJ",
    "SK",
    "SL",
    "SM",
    "SN",
    "SO",
    "SR",
    "SS",
    "ST",
    "SV",
    "SX",
    "SY",
    "SZ",
    "TC",
    "TD",
    "TF",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TL",
    "TM",
    "TN",
    "TO",
    "TR",
    "TT",
    "TV",
    "TW",
    "TZ",
    "UA",
    "UG",
    "UM",
    "US",
    "UY",
    "UZ",
    "VA",
    "VC",
    "VE",
    "VG",
    "VI",
    "VN",
    "VU",
    "WF",
    "WS",
    "YE",
    "YT",
    "ZA",
    "ZM",
    "ZW",
]


type CurrencyCode = Literal[
    "AED",
    "AUD",
    "BHD",
    "BRL",
    "CAD",
    "CHF",
    "CNY",
    "CZK",
    "DKK",
    "EGP",
    "EUR",
    "GBP",
    "HKD",
    "HUF",
    "ILS",
    "INR",
    "JOD",
    "JPY",
    "KWD",
    "MXN",
    "MXP",
    "NGN",
    "NOK",
    "NZD",
    "PLN",
    "QAR",
    "RON",
    "SAR",
    "SEK",
    "SGD",
    "THB",
    "TRY",
    "USD",
    "ZAR",
]
"""
Supported values:
- `AED`: United Arab Emirates Dirham
- `AUD`: Australian Dollar
- `BHD`: Bahraini Dinar
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `CHF`: Swiss Franc
- `CNY`: Chinese Yuan
- `CZK`: Czech Koruna
- `DKK`: Danish Krone
- `EGP`: Egyptian Pound
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `HKD`: Hong Kong Dollar
- `HUF`: Hungarian Forint
- `ILS`: Israeli New Shekel
- `INR`: Indian Rupee
- `JOD`: Jordanian Dinar
- `JPY`: Japanese Yen
- `KWD`: Kuwaiti Dinar
- `MXN`: Mexican Peso
- `MXP`: Mexican Peso
- `NGN`: Nigerian Naira
- `NOK`: Norwegian Krone
- `NZD`: New Zealand Dollar
- `PLN`: Polish Złoty
- `QAR`: Qatari Riyal
- `RON`: Romanian Leu
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `THB`: Thai Baht
- `TRY`: Turkish Lira
- `USD`: United States Dollar
- `ZAR`: South African Rand
"""


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


type SellingProgram = Literal["AMAZON_AUTHOR", "AMAZON_SELLER", "AMAZON_VENDOR"]


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


class CreateBusinessDetail(StrictModel):
    """The business details of advertising account."""

    address: CreateAddress | None = Field(default=None)
    addressToken: str | None = Field(default=None, description="The token of the business address being linked.")
    businessRegistrationNumber: str | None = Field(
        default=None, description="The business registration number of the business."
    )
    website: str | None = Field(default=None, description="The website of the business.")


__all__ = [
    "Address",
    "BusinessDetail",
    "CountryCode",
    "CreateAddress",
    "CreateBusinessDetail",
    "CurrencyCode",
    "IndustryVertical",
    "SellingProgram",
    "TimeZoneIana",
]
