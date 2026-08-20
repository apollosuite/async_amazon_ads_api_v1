"""Auto-generated models for SellingAccounts from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    SellingProgram,
)

type CountryCode = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AL",
    "AM",
    "AO",
    "AQ",
    "AR",
    "AS",
    "AT",
    "AU",
    "AW",
    "AX",
    "AZ",
    "BA",
    "BB",
    "BD",
    "BE",
    "BF",
    "BG",
    "BH",
    "BI",
    "BJ",
    "BL",
    "BM",
    "BN",
    "BO",
    "BQ",
    "BR",
    "BS",
    "BT",
    "BV",
    "BW",
    "BY",
    "BZ",
    "CA",
    "CC",
    "CD",
    "CF",
    "CG",
    "CH",
    "CI",
    "CK",
    "CL",
    "CM",
    "CN",
    "CO",
    "CR",
    "CU",
    "CV",
    "CW",
    "CX",
    "CY",
    "CZ",
    "DE",
    "DJ",
    "DK",
    "DM",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "EH",
    "ER",
    "ES",
    "ET",
    "FI",
    "FJ",
    "FK",
    "FM",
    "FO",
    "FR",
    "GA",
    "GB",
    "GD",
    "GE",
    "GF",
    "GG",
    "GH",
    "GI",
    "GL",
    "GM",
    "GN",
    "GP",
    "GQ",
    "GR",
    "GS",
    "GT",
    "GU",
    "GW",
    "GY",
    "HK",
    "HM",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IE",
    "IL",
    "IM",
    "IN",
    "IO",
    "IQ",
    "IR",
    "IS",
    "IT",
    "JE",
    "JM",
    "JO",
    "JP",
    "KE",
    "KG",
    "KH",
    "KI",
    "KM",
    "KN",
    "KP",
    "KR",
    "KW",
    "KY",
    "KZ",
    "LA",
    "LB",
    "LC",
    "LI",
    "LK",
    "LR",
    "LS",
    "LT",
    "LU",
    "LV",
    "LY",
    "MA",
    "MC",
    "MD",
    "ME",
    "MF",
    "MG",
    "MH",
    "MK",
    "ML",
    "MM",
    "MN",
    "MO",
    "MP",
    "MQ",
    "MR",
    "MS",
    "MT",
    "MU",
    "MV",
    "MW",
    "MX",
    "MY",
    "MZ",
    "NA",
    "NC",
    "NE",
    "NF",
    "NG",
    "NI",
    "NL",
    "NO",
    "NP",
    "NR",
    "NU",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PF",
    "PG",
    "PH",
    "PK",
    "PL",
    "PM",
    "PN",
    "PR",
    "PS",
    "PT",
    "PW",
    "PY",
    "QA",
    "RE",
    "RO",
    "RS",
    "RU",
    "RW",
    "SA",
    "SB",
    "SC",
    "SD",
    "SE",
    "SG",
    "SH",
    "SI",
    "SJ",
    "SK",
    "SL",
    "SM",
    "SN",
    "SO",
    "SR",
    "SS",
    "ST",
    "SV",
    "SX",
    "SY",
    "SZ",
    "TC",
    "TD",
    "TF",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TL",
    "TM",
    "TN",
    "TO",
    "TR",
    "TT",
    "TV",
    "TW",
    "TZ",
    "UA",
    "UG",
    "UM",
    "US",
    "UY",
    "UZ",
    "VA",
    "VC",
    "VE",
    "VG",
    "VI",
    "VN",
    "VU",
    "WF",
    "WS",
    "YE",
    "YT",
    "ZA",
    "ZM",
    "ZW",
]


type Portal = Literal["AUTHOR_CENTRAL", "GROCERY_CENTRAL", "KDP_CENTRAL", "MERCH", "SELLER_CENTRAL", "VENDOR_CENTRAL"]


class QuerySellingAccountRequest(StrictModel):
    maxResults: int | None = Field(default=100, ge=10, le=100)
    nextToken: str | None = Field(default=None)
    sellingAccountLinkTokenFilter: SellingAccountSellingAccountLinkTokenFilter | None = Field(default=None)
    sellingProgramFilter: SellingAccountSellingProgramFilter | None = Field(default=None)


class SellingAccount(LenientModel):
    business: SellingAccountBusiness | None = Field(default=None)
    countryCodes: list[CountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The countries of the selling account user can advertise in.",
    )
    displayName: str | None = Field(default=None, description="Display name for the selling account.")
    portals: list[Portal | str] = Field(
        min_length=1, max_length=6, description="The portal(s) used to access the selling account."
    )
    sellingAccountLinkToken: str = Field(description="The token to locate a selling account.")
    sellingProgram: SellingProgram | str


class SellingAccountAddress(LenientModel):
    """The business address of selling account."""

    addressLine1: str = Field(description="The address details - 1 of business.")
    addressLine2: str | None = Field(default=None, description="The address details - 2 of business.")
    addressToken: str = Field(description="The token to locate a business address.")
    businessName: str = Field(description="The name of business.")
    city: str = Field(description="The city where business is located.")
    countryCode: str = Field(description="The country where business is located.")
    phoneNumber: str | None = Field(default=None, description="The phone number of business.")
    state: str = Field(description="The city where business is located.")
    zipCode: str = Field(description="The zipCode where business is located.")


class SellingAccountBusiness(LenientModel):
    """The business details of selling account."""

    addresses: list[SellingAccountAddress] | None = Field(
        default=None, min_length=0, max_length=10, description="A list of business address the selling account has."
    )
    website: str | None = Field(default=None, description="The website of the business.")


class SellingAccountSellingAccountLinkTokenFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class SellingAccountSellingProgramFilter(StrictModel):
    include: list[SellingProgram] = Field(min_length=1, max_length=1)


class SellingAccountSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    sellingAccounts: list[SellingAccount] | None = Field(default=None, min_length=0, max_length=100)


__all__ = [
    "CountryCode",
    "Portal",
    "QuerySellingAccountRequest",
    "SellingAccount",
    "SellingAccountAddress",
    "SellingAccountBusiness",
    "SellingAccountSellingAccountLinkTokenFilter",
    "SellingAccountSellingProgramFilter",
    "SellingAccountSuccessResponse",
    "SellingProgram",
]
