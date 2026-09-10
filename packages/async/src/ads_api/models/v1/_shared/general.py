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
    "EGP",
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
    "JOD",
    "JPY",
    "KRW",
    "KWD",
    "MAD",
    "MXN",
    "MXP",
    "MYR",
    "NGN",
    "NOK",
    "NZD",
    "PAB",
    "PEN",
    "PHP",
    "PKR",
    "PLN",
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
    "ZAR",
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
- `EGP`: Egyptian Pound
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
- `JOD`: Jordanian Dinar
- `JPY`: Japanese Yen
- `KRW`: South Korean Won
- `KWD`: Kuwaiti Dinar
- `MAD`: Moroccan Dirham
- `MXN`: Mexican Peso
- `MXP`: Mexican Peso
- `MYR`: Malaysian Ringgit
- `NGN`: Nigerian Naira
- `NOK`: Norwegian Krone
- `NZD`: New Zealand Dollar
- `PAB`: Panamanian Balboa
- `PEN`: Peruvian Sol
- `PHP`: Philippine Peso
- `PKR`: Pakistani Rupee
- `PLN`: Polish Złoty
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
- `ZAR`: South African Rand
"""


type ErrorCode = Literal[
    "ACCESS_DENIED_FOR_MANAGER_ACCOUNT",
    "ACCOUNT_ALREADY_EXISTS_FOR_ACCOUNT_NAME",
    "ACCOUNT_ALREADY_EXISTS_FOR_SELLING_ACCOUNT",
    "ACCOUNT_ALREADY_EXISTS_FOR_VENDOR",
    "ACTION_NOT_SUPPORTED",
    "ACTIVE_RESOURCE_LIMIT_EXCEEDED",
    "ADDRESS_BUSINESS_NAME_TOO_LONG",
    "ADDRESS_INVALID_STATE",
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
    "FEATURE_NOT_AVAILABLE",
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
    "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO",
    "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE",
    "GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT",
    "INTERNAL_ERROR",
    "INVALID_INPUT",
    "INVALID_STATE_OR_REGION",
    "INVALID_WEBSITE_URL",
    "INVALID_ZIP_CODE",
    "MISSING_ADDRESS_LINE_ONE",
    "MISSING_BUSINESS_NAME",
    "MISSING_CITY",
    "MISSING_COUNTRY_CODE",
    "MISSING_PHONE_NUMBER",
    "MISSING_STATE",
    "MISSING_WEBSITE_URL",
    "MISSING_ZIP_CODE",
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
- `ACCESS_DENIED_FOR_MANAGER_ACCOUNT`: The request does not have access to the manager account provided in the registration request.
- `ACCOUNT_ALREADY_EXISTS_FOR_ACCOUNT_NAME`: An advertiser account already exists with this display name.
- `ACCOUNT_ALREADY_EXISTS_FOR_SELLING_ACCOUNT`: An advertiser account already exists for this selling account.
- `ACCOUNT_ALREADY_EXISTS_FOR_VENDOR`: An advertiser account already exists for the selected vendor.
- `ACTION_NOT_SUPPORTED`: The request is not supported.
- `ACTIVE_RESOURCE_LIMIT_EXCEEDED`: Too many live resources. Remove resources and try again.
- `ADDRESS_BUSINESS_NAME_TOO_LONG`: Business name provided is too long.
- `ADDRESS_INVALID_STATE`: The state provided in business address is invalid.
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
- `FEATURE_NOT_AVAILABLE`: The requested feature is not available.
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
- `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO`: The campaign is associated with a global campaign. Portfolio association cannot be updated on a child campaign. Please perform operation on the global campaign.
- `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE`: The campaign is associated with a global campaign. The state on child campaign cannot be set to archived. Please perform operation on global campaign.
- `GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT`: The campaign is associated with a global campaign. Only one ad group can be created under this campaign.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `INVALID_INPUT`: The request has invalid input parameters.
- `INVALID_STATE_OR_REGION`: The state provided in business address is invalid.
- `INVALID_WEBSITE_URL`: The website url provided in business detail is invalid
- `INVALID_ZIP_CODE`: The zip code provided in business address is invalid.
- `MISSING_ADDRESS_LINE_ONE`: Address line 1 is missing in business address.
- `MISSING_BUSINESS_NAME`: Business name is missing from business detail.
- `MISSING_CITY`: City is missing in business address.
- `MISSING_COUNTRY_CODE`: Country is missing in business address.
- `MISSING_PHONE_NUMBER`: Phone number is missing from business detail.
- `MISSING_STATE`: State is missing in business address.
- `MISSING_WEBSITE_URL`: Website url is missing from business detail.
- `MISSING_ZIP_CODE`: Zip code is missing in business address.
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


class Error(LenientModel):
    code: ErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=19)


__all__ = [
    "Address",
    "BusinessDetail",
    "CountryCode",
    "CreateAddress",
    "CreateBusinessDetail",
    "CurrencyCode",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "IndustryVertical",
    "SellingProgram",
    "TimeZoneIana",
]
