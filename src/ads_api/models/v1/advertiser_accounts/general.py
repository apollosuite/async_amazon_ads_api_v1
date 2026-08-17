"""Auto-generated models for AdvertiserAccounts from Amazon Ads API v1."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.general import (
    Address,
    BusinessDetail,
    CountryCode,
    CreateAddress,
    CreateBusinessDetail,
    CurrencyCode,
    IndustryVertical,
    SellingProgram,
    TimeZoneIana,
)


class AccountState(StrEnum):
    """
    This represents the current state of an advertising account.
    """

    APPROVED = "APPROVED"  # This signifies that the account has been successfully registered and is eligible to create and manage campaigns.
    ARCHIVED = "ARCHIVED"  # This account has been permanently closed and cannot be reactivated. This may occur if the account was shut down at your request. To advertise again, you'll need to create a new account.
    REGISTRATION_IN_PROGRESS = "REGISTRATION_IN_PROGRESS"  # This means the account registration request has been received and is currently in progress.
    REJECTED = "REJECTED"  # This signifies that the account registration could not be completed successfully. To advertise again, you'll need to create a new account.


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


class RegionCode(StrEnum):
    EU = "EU"  # Europe
    FE = "FE"  # Far East
    NA = "NA"  # North America


class SellingAccountLinkState(StrEnum):
    APPROVED = "APPROVED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    REJECTED = "REJECTED"


class AdvertiserAccount(LenientModel):
    advertiserAccountId: str = Field(description="The unique identifier for the advertiser account.")
    alternateIds: list[AlternateIdentifier] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The list of additional identifiers associated with advertising account.",
    )
    businessDetails: list[BusinessDetail] = Field(
        min_length=1,
        max_length=1,
        description="The business details for an advertising account, containing either an address token for sellingAccount, or an address object if the sellingAccount lacks a valid address.",
    )
    currencyCode: Annotated[CurrencyCode | str, lenient_enum(CurrencyCode)] | None = Field(default=None)
    displayName: str | None = Field(default=None, description="Display name for the advertiser account.")
    industryVertical: Annotated[IndustryVertical | str, lenient_enum(IndustryVertical)] | None = Field(default=None)
    isGlobalAccount: bool | None = Field(
        default=None, description="Indicates whether the advertising account is global or not."
    )
    isTestAccount: bool | None = Field(
        default=None, description="Indicates whether the advertising account is a test account or not."
    )
    managerAccountId: str | None = Field(
        default=None,
        description="Manager Account ID to link to the advertiser account. Required for ADSP-enabled accounts. Without this parameter, accounts will only be enabled for Sponsored Ads.",
    )
    sellingAccountLinkRequests: list[SellingAccountLinkRequest] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The selling account link requests for an advertiser account, containing details for linking.",
    )
    status: AdvertiserAccountStatus
    timeZoneIana: Annotated[TimeZoneIana | str, lenient_enum(TimeZoneIana)] | None = Field(default=None)


class AdvertiserAccountAdvertiserAccountIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class AdvertiserAccountCreate(StrictModel):
    businessDetails: list[CreateBusinessDetail] = Field(
        min_length=1,
        max_length=1,
        description="The business details for an advertising account, containing either an address token for sellingAccount, or an address object if the sellingAccount lacks a valid address.",
    )
    currencyCode: Annotated[CurrencyCode, lenient_enum(CurrencyCode)] | None = Field(default=None)
    displayName: str | None = Field(default=None, description="Display name for the advertiser account.")
    industryVertical: Annotated[IndustryVertical, lenient_enum(IndustryVertical)] | None = Field(default=None)
    isGlobalAccount: bool | None = Field(
        default=None, description="Indicates whether the advertising account is global or not."
    )
    isTestAccount: bool | None = Field(
        default=None, description="Indicates whether the advertising account is a test account or not."
    )
    managerAccountId: str | None = Field(
        default=None,
        description="Manager Account ID to link to the advertiser account. Required for ADSP-enabled accounts. Without this parameter, accounts will only be enabled for Sponsored Ads.",
    )
    sellingAccountLinkRequests: list[CreateSellingAccountLinkRequest] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The selling account link requests for an advertiser account, containing details for linking.",
    )
    timeZoneIana: Annotated[TimeZoneIana, lenient_enum(TimeZoneIana)] | None = Field(default=None)


class AdvertiserAccountIsGlobalAccountFilter(StrictModel):
    include: list[bool] = Field(min_length=1, max_length=1)


class AdvertiserAccountMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[AdvertiserAccountMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class AdvertiserAccountMultiStatusSuccess(LenientModel):
    advertiserAccount: AdvertiserAccount
    index: int = Field(ge=0, le=99)


class AdvertiserAccountStatus(LenientModel):
    """The current status of an AdvertiserAccount, including a status code and a human-readable message."""

    statusCode: Annotated[AccountState | str, lenient_enum(AccountState)]
    statusMessage: str = Field(description="A human-friendly message describing the status of the advertising account.")


class AdvertiserAccountSuccessResponse(LenientModel):
    advertiserAccounts: list[AdvertiserAccount] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class AdvertiserAccountUpdate(StrictModel):
    advertiserAccountId: str = Field(description="The unique identifier for the advertiser account.")
    businessDetails: list[CreateBusinessDetail] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The business details for an advertising account, containing either an address token for sellingAccount, or an address object if the sellingAccount lacks a valid address.",
    )
    currencyCode: Annotated[CurrencyCode, lenient_enum(CurrencyCode)] | None = Field(default=None)
    displayName: str | None = Field(default=None, description="Display name for the advertiser account.")
    industryVertical: Annotated[IndustryVertical, lenient_enum(IndustryVertical)] | None = Field(default=None)
    isGlobalAccount: bool | None = Field(
        default=None, description="Indicates whether the advertising account is global or not."
    )
    isTestAccount: bool | None = Field(
        default=None, description="Indicates whether the advertising account is a test account or not."
    )
    managerAccountId: str | None = Field(
        default=None,
        description="Manager Account ID to link to the advertiser account. Required for ADSP-enabled accounts. Without this parameter, accounts will only be enabled for Sponsored Ads.",
    )
    sellingAccountLinkRequests: list[CreateSellingAccountLinkRequest] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The selling account link requests for an advertiser account, containing details for linking.",
    )
    timeZoneIana: Annotated[TimeZoneIana, lenient_enum(TimeZoneIana)] | None = Field(default=None)


class AlternateIdentifier(LenientModel):
    """Marketplace identifiers associated with advertising account, including profile ID, dsp advertiser ID and entity ID"""

    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = Field(default=None)
    dspAdvertiserId: str | None = Field(
        default=None, description="The regional ADSP advertiser identifier of the advertising account."
    )
    entityId: str | None = Field(
        default=None, description="The marketplace entity identifier of the advertising account."
    )
    profileId: str | None = Field(
        default=None, description="The marketplace profile identifier of the advertising account."
    )
    region: Annotated[RegionCode | str, lenient_enum(RegionCode)] | None = Field(default=None)


class CreateAdvertiserAccountRequest(StrictModel):
    advertiserAccounts: list[AdvertiserAccountCreate] = Field(min_length=1, max_length=100)


class CreateSellingAccountLinkDetails(StrictModel):
    sellingAccountLinkToken: str = Field(description="The token to locate a selling account to be linked.")
    sellingProgram: Annotated[SellingProgram, lenient_enum(SellingProgram)] | None = Field(default=None)


class CreateSellingAccountLinkRequest(StrictModel):
    sellingAccountLinkDetails: CreateSellingAccountLinkDetails


class Error(LenientModel):
    code: Annotated[ErrorCode | str, lenient_enum(ErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=99)


class QueryAdvertiserAccountRequest(StrictModel):
    advertiserAccountIdFilter: AdvertiserAccountAdvertiserAccountIdFilter | None = Field(default=None)
    isGlobalAccountFilter: AdvertiserAccountIsGlobalAccountFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=10, le=100)
    nextToken: str | None = Field(default=None)


class SellingAccountLinkDetails(LenientModel):
    linkStatus: SellingAccountLinkStatus
    sellingAccountLinkToken: str = Field(description="The token to locate a selling account to be linked.")
    sellingProgram: Annotated[SellingProgram | str, lenient_enum(SellingProgram)] | None = Field(default=None)


class SellingAccountLinkRequest(LenientModel):
    sellingAccountLinkDetails: SellingAccountLinkDetails


class SellingAccountLinkStatus(LenientModel):
    statusCode: Annotated[SellingAccountLinkState | str, lenient_enum(SellingAccountLinkState)]
    statusMessage: str = Field(description="The human friendly status message.")


class UpdateAdvertiserAccountRequest(StrictModel):
    advertiserAccounts: list[AdvertiserAccountUpdate] = Field(min_length=1, max_length=100)


__all__ = [
    "AccountState",
    "Address",
    "AdvertiserAccount",
    "AdvertiserAccountAdvertiserAccountIdFilter",
    "AdvertiserAccountCreate",
    "AdvertiserAccountIsGlobalAccountFilter",
    "AdvertiserAccountMultiStatusResponse",
    "AdvertiserAccountMultiStatusSuccess",
    "AdvertiserAccountStatus",
    "AdvertiserAccountSuccessResponse",
    "AdvertiserAccountUpdate",
    "AlternateIdentifier",
    "BusinessDetail",
    "CountryCode",
    "CreateAddress",
    "CreateAdvertiserAccountRequest",
    "CreateBusinessDetail",
    "CreateSellingAccountLinkDetails",
    "CreateSellingAccountLinkRequest",
    "CurrencyCode",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "IndustryVertical",
    "QueryAdvertiserAccountRequest",
    "RegionCode",
    "SellingAccountLinkDetails",
    "SellingAccountLinkRequest",
    "SellingAccountLinkState",
    "SellingAccountLinkStatus",
    "SellingProgram",
    "TimeZoneIana",
    "UpdateAdvertiserAccountRequest",
]
