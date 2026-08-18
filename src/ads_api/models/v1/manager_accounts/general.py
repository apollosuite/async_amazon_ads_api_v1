"""Auto-generated models for ManagerAccounts from Amazon Ads API v1."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.general import (
    Address,
    BusinessDetail,
    CreateAddress,
    CreateBusinessDetail,
    CurrencyCode,
    IndustryVertical,
    TimeZoneIana,
)


class AccountUsageType(StrEnum):
    PRODUCTION = "PRODUCTION"
    TEST = "TEST"


class ErrorCode(StrEnum):
    ACCESS_DENIED_FOR_MANAGER_ACCOUNT = "ACCESS_DENIED_FOR_MANAGER_ACCOUNT"  # The request does not have access to the manager account provided in the registration request.
    ACCOUNT_ALREADY_EXISTS_FOR_ACCOUNT_NAME = (
        "ACCOUNT_ALREADY_EXISTS_FOR_ACCOUNT_NAME"  # An advertiser account already exists with this display name.
    )
    ACCOUNT_ALREADY_EXISTS_FOR_SELLING_ACCOUNT = (
        "ACCOUNT_ALREADY_EXISTS_FOR_SELLING_ACCOUNT"  # An advertiser account already exists for this selling account.
    )
    ACCOUNT_ALREADY_EXISTS_FOR_VENDOR = (
        "ACCOUNT_ALREADY_EXISTS_FOR_VENDOR"  # An advertiser account already exists for the selected vendor.
    )
    ADDRESS_BUSINESS_NAME_TOO_LONG = "ADDRESS_BUSINESS_NAME_TOO_LONG"  # Business name provided is too long.
    ADDRESS_INVALID_STATE = "ADDRESS_INVALID_STATE"  # The state provided in business address is invalid.
    BAD_REQUEST = "BAD_REQUEST"  # The request is not valid considering the documented schema.
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"  # The request is too large. Consider splitting it into multiple requests.
    FORBIDDEN = "FORBIDDEN"  # The caller is not authorized to make the given request.
    INTERNAL_ERROR = "INTERNAL_ERROR"  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    INVALID_INPUT = "INVALID_INPUT"  # The request has invalid input parameters.
    INVALID_STATE_OR_REGION = "INVALID_STATE_OR_REGION"  # The state provided in business address is invalid.
    INVALID_WEBSITE_URL = "INVALID_WEBSITE_URL"  # The website url provided in business detail is invalid
    INVALID_ZIP_CODE = "INVALID_ZIP_CODE"  # The zip code provided in business address is invalid.
    MISSING_ADDRESS_LINE_ONE = "MISSING_ADDRESS_LINE_ONE"  # Address line 1 is missing in business address.
    MISSING_BUSINESS_NAME = "MISSING_BUSINESS_NAME"  # Business name is missing from business detail.
    MISSING_CITY = "MISSING_CITY"  # City is missing in business address.
    MISSING_COUNTRY_CODE = "MISSING_COUNTRY_CODE"  # Country is missing in business address.
    MISSING_PHONE_NUMBER = "MISSING_PHONE_NUMBER"  # Phone number is missing from business detail.
    MISSING_STATE = "MISSING_STATE"  # State is missing in business address.
    MISSING_WEBSITE_URL = "MISSING_WEBSITE_URL"  # Website url is missing from business detail.
    MISSING_ZIP_CODE = "MISSING_ZIP_CODE"  # Zip code is missing in business address.
    NOT_FOUND = "NOT_FOUND"  # The requested resource does not exist.
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"  # There have been too many requests, please slow down your call rate.
    UNAUTHORIZED = "UNAUTHORIZED"  # The request lacks the necessary credentials.


class CreateManagerAccountRequest(StrictModel):
    managerAccounts: list[ManagerAccountCreate] = Field(min_length=1, max_length=10)


class Error(LenientModel):
    code: Annotated[ErrorCode | str, lenient_enum(ErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=99)


class ManagerAccount(LenientModel):
    accountUsageType: Annotated[AccountUsageType | str, lenient_enum(AccountUsageType)] | None = Field(default=None)
    businessDetails: BusinessDetail | None = Field(default=None)
    currencyCode: Annotated[CurrencyCode | str, lenient_enum(CurrencyCode)] | None = Field(default=None)
    industryVertical: Annotated[IndustryVertical | str, lenient_enum(IndustryVertical)] | None = Field(default=None)
    timeZoneIana: Annotated[TimeZoneIana | str, lenient_enum(TimeZoneIana)] | None = Field(default=None)


class ManagerAccountCreate(StrictModel):
    accountUsageType: Annotated[AccountUsageType | str, lenient_enum(AccountUsageType)] | None = Field(default=None)
    businessDetails: CreateBusinessDetail | None = Field(default=None)
    currencyCode: Annotated[CurrencyCode | str, lenient_enum(CurrencyCode)] | None = Field(default=None)
    industryVertical: Annotated[IndustryVertical | str, lenient_enum(IndustryVertical)] | None = Field(default=None)
    timeZoneIana: Annotated[TimeZoneIana | str, lenient_enum(TimeZoneIana)] | None = Field(default=None)


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
    currencyCode: Annotated[CurrencyCode | str, lenient_enum(CurrencyCode)] | None = Field(default=None)
    industryVertical: Annotated[IndustryVertical | str, lenient_enum(IndustryVertical)] | None = Field(default=None)
    managerAccountId: str | None = Field(default=None, description="The identifier of the manager account.")
    timeZoneIana: Annotated[TimeZoneIana | str, lenient_enum(TimeZoneIana)] | None = Field(default=None)


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
