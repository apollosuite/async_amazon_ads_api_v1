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
    IndustryVertical,
    TimeZoneIana,
)

type AccountUsageType = Literal["PRODUCTION", "TEST"]


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


type ErrorCode = Literal[
    "ACCESS_DENIED_FOR_MANAGER_ACCOUNT",
    "ACCOUNT_ALREADY_EXISTS_FOR_ACCOUNT_NAME",
    "ACCOUNT_ALREADY_EXISTS_FOR_SELLING_ACCOUNT",
    "ACCOUNT_ALREADY_EXISTS_FOR_VENDOR",
    "ADDRESS_BUSINESS_NAME_TOO_LONG",
    "ADDRESS_INVALID_STATE",
    "BAD_REQUEST",
    "CONTENT_TOO_LARGE",
    "FORBIDDEN",
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
    "TOO_MANY_REQUESTS",
    "UNAUTHORIZED",
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
    code: ErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=99)


class ManagerAccount(LenientModel):
    accountUsageType: AccountUsageType | str | None = Field(default=None)
    businessDetails: BusinessDetail | None = Field(default=None)
    currencyCode: CurrencyCode | str | None = Field(default=None)
    industryVertical: IndustryVertical | str | None = Field(default=None)
    timeZoneIana: TimeZoneIana | str | None = Field(default=None)


class ManagerAccountCreate(StrictModel):
    accountUsageType: AccountUsageType | None = Field(default=None)
    businessDetails: CreateBusinessDetail | None = Field(default=None)
    currencyCode: CurrencyCode | None = Field(default=None)
    industryVertical: IndustryVertical | None = Field(default=None)
    timeZoneIana: TimeZoneIana | None = Field(default=None)


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
    currencyCode: CurrencyCode | None = Field(default=None)
    industryVertical: IndustryVertical | None = Field(default=None)
    managerAccountId: str | None = Field(default=None, description="The identifier of the manager account.")
    timeZoneIana: TimeZoneIana | None = Field(default=None)


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
