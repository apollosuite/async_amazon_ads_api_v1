"""Auto-generated models for SellingAccounts from Amazon Ads API v1."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.general import (
    CountryCode,
    SellingProgram,
)


class Portal(StrEnum):
    AUTHOR_CENTRAL = "AUTHOR_CENTRAL"
    GROCERY_CENTRAL = "GROCERY_CENTRAL"
    KDP_CENTRAL = "KDP_CENTRAL"
    MERCH = "MERCH"
    SELLER_CENTRAL = "SELLER_CENTRAL"
    VENDOR_CENTRAL = "VENDOR_CENTRAL"


class QuerySellingAccountRequest(StrictModel):
    maxResults: int | None = Field(default=100, ge=10, le=100)
    nextToken: str | None = Field(default=None)
    sellingAccountLinkTokenFilter: SellingAccountSellingAccountLinkTokenFilter | None = Field(default=None)
    sellingProgramFilter: SellingAccountSellingProgramFilter | None = Field(default=None)


class SellingAccount(LenientModel):
    business: SellingAccountBusiness | None = Field(default=None)
    countryCodes: list[Annotated[CountryCode | str, lenient_enum(CountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The countries of the selling account user can advertise in.",
    )
    displayName: str | None = Field(default=None, description="Display name for the selling account.")
    portals: list[Annotated[Portal | str, lenient_enum(Portal)]] = Field(
        min_length=1, max_length=6, description="The portal(s) used to access the selling account."
    )
    sellingAccountLinkToken: str = Field(description="The token to locate a selling account.")
    sellingProgram: Annotated[SellingProgram | str, lenient_enum(SellingProgram)]


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
    include: list[Annotated[SellingProgram | str, lenient_enum(SellingProgram)]] = Field(min_length=1, max_length=1)


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
