"""Auto-generated models for test_accounts from Amazon Ads API v0."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type CreateAccountRequestAccountType = Literal["AUTHOR", "VENDOR"]
"""
Type of test account.
"""


type CreateAccountRequestCountryCode = Literal[
    "AE",
    "AU",
    "BE",
    "BR",
    "CA",
    "DE",
    "EG",
    "ES",
    "FR",
    "IT",
    "JP",
    "MX",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "UK",
    "US",
]
"""
Country code of the test  account.
"""


type GetAccountInformationResponseAccountType = Literal["AUTHOR", "VENDOR"]
"""
Type of test account.
"""


type GetAccountInformationResponseCountryCode = Literal[
    "AE",
    "AU",
    "BE",
    "BR",
    "CA",
    "DE",
    "EG",
    "ES",
    "FR",
    "IT",
    "JP",
    "MX",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "UK",
    "US",
]
"""
Country code of a test account.
"""


type GetAccountInformationResponseStatus = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
"""
Status  of test account creation request.
"""


class CreateAccountRequest(StrictModel):
    accountMetaData: dict[str, Any] | None = Field(default=None)
    accountType: CreateAccountRequestAccountType = Field(description="Type of test account.")
    countryCode: CreateAccountRequestCountryCode = Field(description="Country code of the test  account.")


class CreateAccountResponse(LenientModel):
    requestId: str | None = Field(default=None, description="request id.")


class GetAccountInformationResponse(LenientModel):
    pass


__all__ = [
    "CreateAccountRequest",
    "CreateAccountRequestAccountType",
    "CreateAccountRequestCountryCode",
    "CreateAccountResponse",
    "GetAccountInformationResponse",
    "GetAccountInformationResponseAccountType",
    "GetAccountInformationResponseCountryCode",
    "GetAccountInformationResponseStatus",
]
