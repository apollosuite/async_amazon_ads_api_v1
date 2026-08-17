"""Auto-generated models for Profiles from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class AccountType(StrEnum):
    """
    The `seller` and `vendor` account types are associated with Sponsored Ads APIs. The `agency` account type is associated with DSP and Data Provider APIs.
    """

    vendor = "vendor"
    seller = "seller"
    agency = "agency"


class CountryCode(StrEnum):
    """
    The countryCode for a given country
    """

    BR = "BR"
    CA = "CA"
    MX = "MX"
    US = "US"
    AE = "AE"
    BE = "BE"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    IE = "IE"
    IN = "IN"
    IT = "IT"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    TR = "TR"
    UK = "UK"
    AU = "AU"
    JP = "JP"
    SG = "SG"
    ZA = "ZA"


class AccountInfo(StrictModel):
    marketplaceStringId: str | None = Field(
        default=None, description="The identifier of the marketplace to which the account is associated."
    )
    id: str | None = Field(
        default=None,
        description="Identifier for sellers and vendors. Note that this value is not unique and may be the same across marketplace.",
    )
    type: Annotated[AccountType, lenient_enum(AccountType)] | None = Field(default=None)
    name: str | None = Field(default=None, description="Account name.")
    subType: str | None = Field(default=None, description="The account subtype.")
    validPaymentMethod: bool | None = Field(
        default=None,
        description="Only present for Vendors, this returns whether the Advertiser has set up a valid payment method or not.",
    )


class AccountInfoOut(LenientModel):
    marketplaceStringId: str | None = Field(
        default=None, description="The identifier of the marketplace to which the account is associated."
    )
    id: str | None = Field(
        default=None,
        description="Identifier for sellers and vendors. Note that this value is not unique and may be the same across marketplace.",
    )
    type: Annotated[AccountType | str, lenient_enum(AccountType)] | None = Field(default=None)
    name: str | None = Field(default=None, description="Account name.")
    subType: str | None = Field(default=None, description="The account subtype.")
    validPaymentMethod: bool | None = Field(
        default=None,
        description="Only present for Vendors, this returns whether the Advertiser has set up a valid payment method or not.",
    )


class Profile(StrictModel):
    profileId: int | None = Field(default=None)
    countryCode: Annotated[CountryCode, lenient_enum(CountryCode)] | None = Field(default=None)
    currencyCode: str | None = Field(
        default=None, description="The currency used for all monetary values for entities under this profile."
    )
    dailyBudget: float | None = Field(
        default=None,
        description="Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts.",
    )
    timezone: str | None = Field(
        default=None, description="The time zone used for all date-based campaign management and reporting."
    )
    accountInfo: AccountInfo | None = Field(default=None)


class ProfileOut(LenientModel):
    profileId: int | None = Field(default=None)
    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = Field(default=None)
    currencyCode: str | None = Field(
        default=None, description="The currency used for all monetary values for entities under this profile."
    )
    dailyBudget: float | None = Field(
        default=None,
        description="Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts.",
    )
    timezone: str | None = Field(
        default=None, description="The time zone used for all date-based campaign management and reporting."
    )
    accountInfo: AccountInfoOut | None = Field(default=None)


class ProfileResult(LenientModel):
    profileId: int | None = Field(default=None)
    code: str | None = Field(default=None)
    details: str | None = Field(default=None)


__all__ = ["AccountInfo", "AccountInfoOut", "AccountType", "CountryCode", "Profile", "ProfileOut", "ProfileResult"]
