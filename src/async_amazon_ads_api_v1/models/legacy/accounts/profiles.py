"""Auto-generated Pydantic models for Profiles API."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class AccountInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    marketplaceStringId: str | None = Field(
        default=None,
        description="The identifier of the marketplace to which the account is associated.",
    )
    id: str | None = Field(
        default=None,
        description="Identifier for sellers and vendors. Note that this value is not unique and may be the same across marketplace.",
    )
    type: Annotated[AccountType | str, lenient_enum(AccountType)] | None = Field(
        default=None,
    )
    name: str | None = Field(
        default=None,
        description="Account name.",
    )
    subType: str | None = Field(
        default=None,
        description="The account subtype.",
    )
    validPaymentMethod: bool | None = Field(
        default=None,
        description="Only present for Vendors, this returns whether the Advertiser has set up a valid payment method or not.",
    )


class AccountType(StrEnum):
    """The `seller` and `vendor` account types are associated with Sponsored Ads APIs. The `agency` account type is associated with DSP and Data Provider APIs."""

    vendor = "vendor"
    seller = "seller"
    agency = "agency"


class Profile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    profileId: int | None = Field(default=None)
    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = Field(
        default=None,
    )
    currencyCode: str | None = Field(
        default=None,
        description="The currency used for all monetary values for entities under this profile. Region `countryCode` Country Name `currencyCode` ----- ------ ------ ------ NA BR Brazil BRL NA CA Canada CAD NA MX Mexico MXN NA US United States USD EU AE United Arab Emirates AED EU BE Belgium EUR EU DE Germany EUR EU EG Egypt EGP EU ES Spain EUR EU FR France EUR EU IE Ireland EUR EU IN India INR EU IT Italy EUR EU NL The Netherlands EUR EU PL Poland PLN EU SA Saudi Arabia SAR EU SE Sweden SEK EU TR Turkey TRY EU UK United Kingdom GBP EU ZA South Africa ZAR FE AU Australia AUD FE JP Japan JPY FE SG Singapore SGD",
    )
    dailyBudget: float | None = Field(
        default=None,
        description="Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts.",
    )
    timezone: str | None = Field(
        default=None,
        description="The time zone used for all date-based campaign management and reporting. Region `countryCode` Country Name `timezone` ------ ----- ----- ------ NA BR Brazil America/Sao_Paulo NA CA Canada America/Los_Angeles NA MX Mexico America/Los_Angeles NA US United States America/Los_Angeles EU AE United Arab Emirates Asia/Dubai EU BE Belgium Europe/Brussels EU DE Germany Europe/Paris EU EG Egypt Africa/Cairo EU ES Spain Europe/Paris EU FR France Europe/Paris EU IE Ireland Europe/Dublin EU IN India Asia/Kolkata EU IT Italy Europe/Paris EU NL The Netherlands Europe/Amsterdam EU PL Poland Europe/Warsaw EU SA Saudi Arabia Asia/Riyadh EU SE Sweden Europe/Stockholm EU TR Turkey Europe/Istanbul EU UK United Kingdom Europe/London EU ZA South Africa Africa/Johannesburg FE AU Australia Australia/Sydney FE JP Japan Asia/Tokyo FE SG Singapore Asia/Singapore",
    )
    accountInfo: AccountInfo | None = Field(default=None)


class ProfileResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    profileId: int | None = Field(default=None)
    code: str | None = Field(default=None)
    details: str | None = Field(default=None)


class CountryCode(StrEnum):
    """The countryCode for a given country Region `countryCode` Country Name ------ ----- ------- NA BR Brazil NA CA Canada NA MX Mexico NA US United States EU AE United Arab Emirates EU BE Belgium EU DE Germany EU EG Egypt EU ES Spain EU FR France EU IE Ireland EU IN India EU IT Italy EU NL The Netherlands EU PL Poland EU SA Saudi Arabia EU SE Sweden EU TR Turkey EU UK United Kingdom EU ZA South Africa FE AU Australia FE JP Japan FE SG Singapore"""

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


class ListProfilesResponseContent(BaseModel):
    """Wrapper for listProfiles response (bare array → dict)."""

    model_config = ConfigDict(extra="forbid")

    profiles: list[Profile]


class UpdateProfilesResponseContent(BaseModel):
    """Wrapper for updateProfiles response (bare array → dict)."""

    model_config = ConfigDict(extra="forbid")

    results: list[ProfileResponse]
