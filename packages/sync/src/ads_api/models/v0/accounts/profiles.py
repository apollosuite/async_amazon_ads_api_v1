"""Auto-generated models for Profiles from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type AccountType = Literal["vendor", "seller", "agency"]
"""
The `seller` and `vendor` account types are associated with Sponsored Ads APIs. The `agency` account type is associated with DSP and Data Provider APIs.
"""


type CountryCode = Literal[
    "BR",
    "CA",
    "MX",
    "US",
    "AE",
    "BE",
    "DE",
    "EG",
    "ES",
    "FR",
    "IE",
    "IN",
    "IT",
    "NL",
    "PL",
    "SA",
    "SE",
    "TR",
    "UK",
    "AU",
    "JP",
    "SG",
    "ZA",
]
"""
The countryCode for a given country
|Region|`countryCode`|Country Name|
|------|-----|-------|
|NA|BR|Brazil|
|NA|CA|Canada|
|NA|MX|Mexico|
|NA|US|United States|
|EU|AE|United Arab Emirates|
|EU|BE|Belgium|
|EU|DE|Germany|
|EU|EG|Egypt|
|EU|ES|Spain|
|EU|FR|France|
|EU|IE|Ireland|
|EU|IN|India|
|EU|IT|Italy|
|EU|NL|The Netherlands|
|EU|PL|Poland|
|EU|SA|Saudi Arabia|
|EU|SE|Sweden|
|EU|TR|Turkey|
|EU|UK|United Kingdom|
|EU|ZA| South Africa |
|FE|AU|Australia|
|FE|JP|Japan|
|FE|SG|Singapore|
"""


class AccountInfo(StrictModel):
    marketplaceStringId: str | None = Field(
        default=None, description="The identifier of the marketplace to which the account is associated."
    )
    id: str | None = Field(
        default=None,
        description="Identifier for sellers and vendors. Note that this value is not unique and may be the same across marketplace.",
    )
    type: AccountType | None = Field(default=None)
    name: str | None = Field(default=None, description="Account name.")
    subType: Literal["KDP_AUTHOR", "AMAZON_ATTRIBUTION"] | None = Field(
        default=None, description="The account subtype."
    )
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
    type: AccountType | str | None = Field(default=None)
    name: str | None = Field(default=None, description="Account name.")
    subType: Literal["KDP_AUTHOR", "AMAZON_ATTRIBUTION"] | str | None = Field(
        default=None, description="The account subtype."
    )
    validPaymentMethod: bool | None = Field(
        default=None,
        description="Only present for Vendors, this returns whether the Advertiser has set up a valid payment method or not.",
    )


class Profile(StrictModel):
    profileId: int | None = Field(default=None)
    countryCode: CountryCode | None = Field(default=None)
    currencyCode: (
        Literal[
            "BRL",
            "CAD",
            "MXN",
            "USD",
            "AED",
            "EUR",
            "EGP",
            "INR",
            "PLN",
            "SAR",
            "SEK",
            "TRY",
            "GBP",
            "AUD",
            "JPY",
            "SGD",
            "ZAR",
        ]
        | None
    ) = Field(
        default=None,
        description="""
The currency used for all monetary values for entities under this profile.
|Region|`countryCode`|Country Name|`currencyCode`|
|-----|------|------|------|
|NA|BR|Brazil|BRL|
|NA|CA|Canada|CAD|
|NA|MX|Mexico|MXN|
|NA|US|United States|USD|
|EU|AE|United Arab Emirates|AED|
|EU|BE|Belgium|EUR|
|EU|DE|Germany|EUR|
|EU|EG|Egypt|EGP|
|EU|ES|Spain|EUR|
|EU|FR|France|EUR|
|EU|IE|Ireland|EUR|
|EU|IN|India|INR|
|EU|IT|Italy|EUR|
|EU|NL|The Netherlands|EUR|
|EU|PL|Poland|PLN|
|EU|SA|Saudi Arabia|SAR|
|EU|SE|Sweden|SEK|
|EU|TR|Turkey|TRY|
|EU|UK|United Kingdom|GBP|
|EU|ZA| South Africa | ZAR|
|FE|AU|Australia|AUD|
|FE|JP|Japan|JPY|
|FE|SG|Singapore|SGD|
""",
    )
    dailyBudget: float | None = Field(
        default=None,
        description="Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts.",
    )
    timezone: (
        Literal[
            "Africa/Cairo",
            "America/Sao_Paulo",
            "America/Los_Angeles",
            "Asia/Dubai",
            "Asia/Kolkata",
            "Asia/Riyadh",
            "Asia/Singapore",
            "Asia/Tokyo",
            "Australia/Sydney",
            "Europe/Amsterdam",
            "Europe/Dublin",
            "Europe/Istanbul",
            "Europe/London",
            "Europe/Paris",
            "Europe/Stockholm",
            "Europe/Warsaw",
            "Europe/Brussels",
            "Africa/Johannesburg",
        ]
        | None
    ) = Field(
        default=None,
        description="""
The time zone used for all date-based campaign management and reporting.
|Region|`countryCode`|Country Name|`timezone`|
|------|-----|-----|------|
|NA|BR|Brazil|America/Sao_Paulo|
|NA|CA|Canada|America/Los_Angeles|
|NA|MX|Mexico|America/Los_Angeles|
|NA|US|United States|America/Los_Angeles|
|EU|AE|United Arab Emirates|Asia/Dubai|
|EU|BE|Belgium|Europe/Brussels|
|EU|DE|Germany|Europe/Paris|
|EU|EG|Egypt|Africa/Cairo|
|EU|ES|Spain|Europe/Paris|
|EU|FR|France|Europe/Paris|
|EU|IE|Ireland|Europe/Dublin|
|EU|IN|India|Asia/Kolkata|
|EU|IT|Italy|Europe/Paris|
|EU|NL|The Netherlands|Europe/Amsterdam|
|EU|PL|Poland|Europe/Warsaw|
|EU|SA|Saudi Arabia|Asia/Riyadh|
|EU|SE|Sweden|Europe/Stockholm|
|EU|TR|Turkey|Europe/Istanbul|
|EU|UK|United Kingdom|Europe/London|
|EU|ZA| South Africa | Africa/Johannesburg |
|FE|AU|Australia|Australia/Sydney|
|FE|JP|Japan|Asia/Tokyo|
|FE|SG|Singapore|Asia/Singapore|
""",
    )
    accountInfo: AccountInfo | None = Field(default=None)


class ProfileOut(LenientModel):
    profileId: int | None = Field(default=None)
    countryCode: CountryCode | str | None = Field(default=None)
    currencyCode: (
        Literal[
            "BRL",
            "CAD",
            "MXN",
            "USD",
            "AED",
            "EUR",
            "EGP",
            "INR",
            "PLN",
            "SAR",
            "SEK",
            "TRY",
            "GBP",
            "AUD",
            "JPY",
            "SGD",
            "ZAR",
        ]
        | str
        | None
    ) = Field(
        default=None,
        description="""
The currency used for all monetary values for entities under this profile.
|Region|`countryCode`|Country Name|`currencyCode`|
|-----|------|------|------|
|NA|BR|Brazil|BRL|
|NA|CA|Canada|CAD|
|NA|MX|Mexico|MXN|
|NA|US|United States|USD|
|EU|AE|United Arab Emirates|AED|
|EU|BE|Belgium|EUR|
|EU|DE|Germany|EUR|
|EU|EG|Egypt|EGP|
|EU|ES|Spain|EUR|
|EU|FR|France|EUR|
|EU|IE|Ireland|EUR|
|EU|IN|India|INR|
|EU|IT|Italy|EUR|
|EU|NL|The Netherlands|EUR|
|EU|PL|Poland|PLN|
|EU|SA|Saudi Arabia|SAR|
|EU|SE|Sweden|SEK|
|EU|TR|Turkey|TRY|
|EU|UK|United Kingdom|GBP|
|EU|ZA| South Africa | ZAR|
|FE|AU|Australia|AUD|
|FE|JP|Japan|JPY|
|FE|SG|Singapore|SGD|
""",
    )
    dailyBudget: float | None = Field(
        default=None,
        description="Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts.",
    )
    timezone: (
        Literal[
            "Africa/Cairo",
            "America/Sao_Paulo",
            "America/Los_Angeles",
            "Asia/Dubai",
            "Asia/Kolkata",
            "Asia/Riyadh",
            "Asia/Singapore",
            "Asia/Tokyo",
            "Australia/Sydney",
            "Europe/Amsterdam",
            "Europe/Dublin",
            "Europe/Istanbul",
            "Europe/London",
            "Europe/Paris",
            "Europe/Stockholm",
            "Europe/Warsaw",
            "Europe/Brussels",
            "Africa/Johannesburg",
        ]
        | str
        | None
    ) = Field(
        default=None,
        description="""
The time zone used for all date-based campaign management and reporting.
|Region|`countryCode`|Country Name|`timezone`|
|------|-----|-----|------|
|NA|BR|Brazil|America/Sao_Paulo|
|NA|CA|Canada|America/Los_Angeles|
|NA|MX|Mexico|America/Los_Angeles|
|NA|US|United States|America/Los_Angeles|
|EU|AE|United Arab Emirates|Asia/Dubai|
|EU|BE|Belgium|Europe/Brussels|
|EU|DE|Germany|Europe/Paris|
|EU|EG|Egypt|Africa/Cairo|
|EU|ES|Spain|Europe/Paris|
|EU|FR|France|Europe/Paris|
|EU|IE|Ireland|Europe/Dublin|
|EU|IN|India|Asia/Kolkata|
|EU|IT|Italy|Europe/Paris|
|EU|NL|The Netherlands|Europe/Amsterdam|
|EU|PL|Poland|Europe/Warsaw|
|EU|SA|Saudi Arabia|Asia/Riyadh|
|EU|SE|Sweden|Europe/Stockholm|
|EU|TR|Turkey|Europe/Istanbul|
|EU|UK|United Kingdom|Europe/London|
|EU|ZA| South Africa | Africa/Johannesburg |
|FE|AU|Australia|Australia/Sydney|
|FE|JP|Japan|Asia/Tokyo|
|FE|SG|Singapore|Asia/Singapore|
""",
    )
    accountInfo: AccountInfoOut | None = Field(default=None)


class ProfileResult(LenientModel):
    profileId: int | None = Field(default=None)
    code: str | None = Field(default=None)
    details: str | None = Field(default=None)


__all__ = ["AccountInfo", "AccountInfoOut", "AccountType", "CountryCode", "Profile", "ProfileOut", "ProfileResult"]
