"""Auto-generated models for test_accounts from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Any

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class CreateAccountRequestAccountType(StrEnum):
    """
    Type of test account.
    """

    AUTHOR = "AUTHOR"
    VENDOR = "VENDOR"


class CreateAccountRequestCountryCode(StrEnum):
    """
    Country code of the test  account.
    """

    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    UK = "UK"
    US = "US"


class GetAccountInformationResponseAccountType(StrEnum):
    """
    Type of test account.
    """

    AUTHOR = "AUTHOR"
    VENDOR = "VENDOR"


class GetAccountInformationResponseCountryCode(StrEnum):
    """
    Country code of a test account.
    """

    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    UK = "UK"
    US = "US"


class GetAccountInformationResponseStatus(StrEnum):
    """
    Status  of test account creation request.
    """

    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"


class CreateAccountRequest(StrictModel):
    accountMetaData: dict[str, Any] | None = Field(default=None)
    accountType: Annotated[CreateAccountRequestAccountType | str, lenient_enum(CreateAccountRequestAccountType)] = (
        Field(description="Type of test account.")
    )
    countryCode: Annotated[CreateAccountRequestCountryCode | str, lenient_enum(CreateAccountRequestCountryCode)] = (
        Field(description="Country code of the test  account.")
    )


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
