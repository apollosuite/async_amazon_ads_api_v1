"""Auto-generated models for ManagerAccounts from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    Address,
    BusinessDetail,
    CreateAddress,
    CreateBusinessDetail,
    CurrencyCode,
    IndustryVertical,
    TimeZoneIana,
)

type AccountUsageType = Literal["PRODUCTION", "TEST"]


type ErrorCode = Literal[
    "ACCESS_DENIED_FOR_MANAGER_ACCOUNT",  # The request does not have access to the manager account provided in the registration request.
    "ACCOUNT_ALREADY_EXISTS_FOR_ACCOUNT_NAME",  # An advertiser account already exists with this display name.
    "ACCOUNT_ALREADY_EXISTS_FOR_SELLING_ACCOUNT",  # An advertiser account already exists for this selling account.
    "ACCOUNT_ALREADY_EXISTS_FOR_VENDOR",  # An advertiser account already exists for the selected vendor.
    "ADDRESS_BUSINESS_NAME_TOO_LONG",  # Business name provided is too long.
    "ADDRESS_INVALID_STATE",  # The state provided in business address is invalid.
    "BAD_REQUEST",  # The request is not valid considering the documented schema.
    "CONTENT_TOO_LARGE",  # The request is too large. Consider splitting it into multiple requests.
    "FORBIDDEN",  # The caller is not authorized to make the given request.
    "INTERNAL_ERROR",  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    "INVALID_INPUT",  # The request has invalid input parameters.
    "INVALID_STATE_OR_REGION",  # The state provided in business address is invalid.
    "INVALID_WEBSITE_URL",  # The website url provided in business detail is invalid
    "INVALID_ZIP_CODE",  # The zip code provided in business address is invalid.
    "MISSING_ADDRESS_LINE_ONE",  # Address line 1 is missing in business address.
    "MISSING_BUSINESS_NAME",  # Business name is missing from business detail.
    "MISSING_CITY",  # City is missing in business address.
    "MISSING_COUNTRY_CODE",  # Country is missing in business address.
    "MISSING_PHONE_NUMBER",  # Phone number is missing from business detail.
    "MISSING_STATE",  # State is missing in business address.
    "MISSING_WEBSITE_URL",  # Website url is missing from business detail.
    "MISSING_ZIP_CODE",  # Zip code is missing in business address.
    "NOT_FOUND",  # The requested resource does not exist.
    "TOO_MANY_REQUESTS",  # There have been too many requests, please slow down your call rate.
    "UNAUTHORIZED",  # The request lacks the necessary credentials.
]
"""
Supported values:
- `ACCESS_DENIED_FOR_MANAGER_ACCOUNT`: The request does not have access to the manager account provided in the registration request.
- `ACCOUNT_ALREADY_EXISTS_FOR_ACCOUNT_NAME`: An advertiser account already exists with this display name.
- `ACCOUNT_ALREADY_EXISTS_FOR_SELLING_ACCOUNT`: An advertiser account already exists for this selling account.
- `ACCOUNT_ALREADY_EXISTS_FOR_VENDOR`: An advertiser account already exists for the selected vendor.
- `ADDRESS_BUSINESS_NAME_TOO_LONG`: Business name provided is too long.
- `ADDRESS_INVALID_STATE`: The state provided in business address is invalid.
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `FORBIDDEN`: The caller is not authorized to make the given request.
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
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
"""


class CreateManagerAccountRequest(StrictModel):
    managerAccounts: list[ManagerAccountCreate] = Field(min_length=1, max_length=10)


class Error(LenientModel):
    code: ErrorCode | str = Field(description="""
Supported values:
- `ACCESS_DENIED_FOR_MANAGER_ACCOUNT`: The request does not have access to the manager account provided in the registration request.
- `ACCOUNT_ALREADY_EXISTS_FOR_ACCOUNT_NAME`: An advertiser account already exists with this display name.
- `ACCOUNT_ALREADY_EXISTS_FOR_SELLING_ACCOUNT`: An advertiser account already exists for this selling account.
- `ACCOUNT_ALREADY_EXISTS_FOR_VENDOR`: An advertiser account already exists for the selected vendor.
- `ADDRESS_BUSINESS_NAME_TOO_LONG`: Business name provided is too long.
- `ADDRESS_INVALID_STATE`: The state provided in business address is invalid.
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `FORBIDDEN`: The caller is not authorized to make the given request.
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
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
""")
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=99)


class ManagerAccount(LenientModel):
    accountUsageType: AccountUsageType | str | None = Field(default=None)
    businessDetails: BusinessDetail | None = Field(default=None)
    currencyCode: CurrencyCode | str | None = Field(
        default=None,
        description="""
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
""",
    )
    industryVertical: IndustryVertical | str | None = Field(
        default=None,
        description="""
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
""",
    )
    timeZoneIana: TimeZoneIana | str | None = Field(
        default=None,
        description="""
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
""",
    )


class ManagerAccountCreate(StrictModel):
    accountUsageType: AccountUsageType | None = Field(default=None)
    businessDetails: CreateBusinessDetail | None = Field(default=None)
    currencyCode: CurrencyCode | None = Field(
        default=None,
        description="""
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
""",
    )
    industryVertical: IndustryVertical | None = Field(
        default=None,
        description="""
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
""",
    )
    timeZoneIana: TimeZoneIana | None = Field(
        default=None,
        description="""
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
""",
    )


class ManagerAccountManagerAccountIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class ManagerAccountMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[ManagerAccountMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class ManagerAccountMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    managerAccount: ManagerAccount


class ManagerAccountSuccessResponse(LenientModel):
    managerAccounts: list[ManagerAccount] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class ManagerAccountUpdate(StrictModel):
    businessDetails: UpdateBusinessDetail | None = Field(default=None)
    currencyCode: CurrencyCode | None = Field(
        default=None,
        description="""
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
""",
    )
    industryVertical: IndustryVertical | None = Field(
        default=None,
        description="""
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
""",
    )
    managerAccountId: str | None = Field(default=None, description="The identifier of the manager account.")
    timeZoneIana: TimeZoneIana | None = Field(
        default=None,
        description="""
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
""",
    )


class QueryManagerAccountRequest(StrictModel):
    managerAccountIdFilter: ManagerAccountManagerAccountIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=10, le=100)
    nextToken: str | None = Field(default=None)


class UpdateAddress(StrictModel):
    """The business address of advertising account."""

    addressLine1: str | None = Field(default=None, description="The address details - 1 of business.")
    addressLine2: str | None = Field(default=None, description="The address details - 2 of business.")
    businessName: str | None = Field(default=None, description="The name of business.")
    city: str | None = Field(default=None, description="The city where business is located.")
    countryCode: str | None = Field(default=None, description="The country where business is located.")
    phoneNumber: str | None = Field(default=None, description="The phone number of business.")
    state: str | None = Field(default=None, description="The city where business is located.")
    zipCode: str | None = Field(default=None, description="The zipCode where business is located.")


class UpdateBusinessDetail(StrictModel):
    """The business details of advertising account."""

    address: UpdateAddress | None = Field(default=None)
    addressToken: str | None = Field(default=None, description="The token of the business address being linked.")
    businessRegistrationNumber: str | None = Field(
        default=None, description="The business registration number of the business."
    )
    website: str | None = Field(default=None, description="The website of the business.")


class UpdateManagerAccountRequest(StrictModel):
    managerAccounts: list[ManagerAccountUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "AccountUsageType",
    "Address",
    "BusinessDetail",
    "CreateAddress",
    "CreateBusinessDetail",
    "CreateManagerAccountRequest",
    "CurrencyCode",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "IndustryVertical",
    "ManagerAccount",
    "ManagerAccountCreate",
    "ManagerAccountManagerAccountIdFilter",
    "ManagerAccountMultiStatusResponse",
    "ManagerAccountMultiStatusSuccess",
    "ManagerAccountSuccessResponse",
    "ManagerAccountUpdate",
    "QueryManagerAccountRequest",
    "TimeZoneIana",
    "UpdateAddress",
    "UpdateBusinessDetail",
    "UpdateManagerAccountRequest",
]
