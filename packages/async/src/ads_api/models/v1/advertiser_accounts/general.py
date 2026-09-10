"""Auto-generated models for AdvertiserAccounts from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    Address,
    BusinessDetail,
    CountryCode,
    CreateAddress,
    CreateBusinessDetail,
    CurrencyCode,
    Error,
    ErrorCode,
    ErrorsIndex,
    IndustryVertical,
    SellingProgram,
    TimeZoneIana,
)

type AccountState = Literal["APPROVED", "ARCHIVED", "REGISTRATION_IN_PROGRESS", "REJECTED"]
"""
This represents the current state of an advertising account.

Supported values:
- `APPROVED`: This signifies that the account has been successfully registered and is eligible to create and manage campaigns.
- `ARCHIVED`: This account has been permanently closed and cannot be reactivated. This may occur if the account was shut down at your request. To advertise again, you'll need to create a new account.
- `REGISTRATION_IN_PROGRESS`: This means the account registration request has been received and is currently in progress.
- `REJECTED`: This signifies that the account registration could not be completed successfully. To advertise again, you'll need to create a new account.
"""


type RegionCode = Literal["EU", "FE", "NA"]
"""
Supported values:
- `EU`: Europe
- `FE`: Far East
- `NA`: North America
"""


type SellingAccountLinkState = Literal["APPROVED", "IN_PROGRESS", "PENDING_APPROVAL", "REJECTED"]


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
    currencyCode: CurrencyCode | str | None = Field(default=None)
    displayName: str | None = Field(default=None, description="Display name for the advertiser account.")
    industryVertical: IndustryVertical | str | None = Field(default=None)
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
    timeZoneIana: TimeZoneIana | str | None = Field(default=None)


class AdvertiserAccountAdvertiserAccountIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class AdvertiserAccountCreate(StrictModel):
    businessDetails: list[CreateBusinessDetail] = Field(
        min_length=1,
        max_length=1,
        description="The business details for an advertising account, containing either an address token for sellingAccount, or an address object if the sellingAccount lacks a valid address.",
    )
    currencyCode: CurrencyCode | None = Field(default=None)
    displayName: str | None = Field(default=None, description="Display name for the advertiser account.")
    industryVertical: IndustryVertical | None = Field(default=None)
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
    timeZoneIana: TimeZoneIana | None = Field(default=None)


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

    statusCode: AccountState | str
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
    currencyCode: CurrencyCode | None = Field(default=None)
    displayName: str | None = Field(default=None, description="Display name for the advertiser account.")
    industryVertical: IndustryVertical | None = Field(default=None)
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
    timeZoneIana: TimeZoneIana | None = Field(default=None)


class AlternateIdentifier(LenientModel):
    """Marketplace identifiers associated with advertising account, including profile ID, dsp advertiser ID and entity ID"""

    countryCode: CountryCode | str | None = Field(default=None)
    dspAdvertiserId: str | None = Field(
        default=None, description="The regional ADSP advertiser identifier of the advertising account."
    )
    entityId: str | None = Field(
        default=None, description="The marketplace entity identifier of the advertising account."
    )
    profileId: str | None = Field(
        default=None, description="The marketplace profile identifier of the advertising account."
    )
    region: RegionCode | str | None = Field(default=None)


class CreateAdvertiserAccountRequest(StrictModel):
    advertiserAccounts: list[AdvertiserAccountCreate] = Field(min_length=1, max_length=100)


class CreateSellingAccountLinkDetails(StrictModel):
    sellingAccountLinkToken: str = Field(description="The token to locate a selling account to be linked.")
    sellingProgram: SellingProgram | None = Field(default=None)


class CreateSellingAccountLinkRequest(StrictModel):
    sellingAccountLinkDetails: CreateSellingAccountLinkDetails


class QueryAdvertiserAccountRequest(StrictModel):
    advertiserAccountIdFilter: AdvertiserAccountAdvertiserAccountIdFilter | None = Field(default=None)
    isGlobalAccountFilter: AdvertiserAccountIsGlobalAccountFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=10, le=100)
    nextToken: str | None = Field(default=None)


class SellingAccountLinkDetails(LenientModel):
    linkStatus: SellingAccountLinkStatus
    sellingAccountLinkToken: str = Field(description="The token to locate a selling account to be linked.")
    sellingProgram: SellingProgram | str | None = Field(default=None)


class SellingAccountLinkRequest(LenientModel):
    sellingAccountLinkDetails: SellingAccountLinkDetails


class SellingAccountLinkStatus(LenientModel):
    statusCode: SellingAccountLinkState | str
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
