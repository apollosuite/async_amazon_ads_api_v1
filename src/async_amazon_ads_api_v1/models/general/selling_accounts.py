"""Auto-generated models for SellingAccounts from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import GeneralCountryCode, GeneralSellingProgram


class Portal(StrEnum):
    AUTHOR_CENTRAL = "AUTHOR_CENTRAL"
    GROCERY_CENTRAL = "GROCERY_CENTRAL"
    KDP_CENTRAL = "KDP_CENTRAL"
    MERCH = "MERCH"
    SELLER_CENTRAL = "SELLER_CENTRAL"
    VENDOR_CENTRAL = "VENDOR_CENTRAL"


class QuerySellingAccountRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    maxResults: int | None = Field(default=100, ge=10, le=100)
    nextToken: str | None = Field(default=None)
    sellingAccountLinkTokenFilter: SellingAccountSellingAccountLinkTokenFilter | None = Field(default=None)
    sellingProgramFilter: SellingAccountSellingProgramFilter | None = Field(default=None)


class SellingAccount(BaseModel):
    model_config = ConfigDict(extra="allow")

    business: SellingAccountBusiness | None = Field(default=None)
    countryCodes: list[Annotated[GeneralCountryCode | str, lenient_enum(GeneralCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The countries of the selling account user can advertise in.",
    )
    displayName: str | None = Field(default=None, description="Display name for the selling account.")
    portals: list[Annotated[Portal | str, lenient_enum(Portal)]] | None = Field(
        default=None, min_length=1, max_length=6, description="The portal(s) used to access the selling account."
    )
    sellingAccountLinkToken: str | None = Field(default=None, description="The token to locate a selling account.")
    sellingProgram: Annotated[GeneralSellingProgram | str, lenient_enum(GeneralSellingProgram)] | None = Field(
        default=None
    )


class SellingAccountAddress(BaseModel):
    """The business address of selling account."""

    model_config = ConfigDict(extra="allow")

    addressLine1: str | None = Field(default=None, description="The address details - 1 of business.")
    addressLine2: str | None = Field(default=None, description="The address details - 2 of business.")
    addressToken: str | None = Field(default=None, description="The token to locate a business address.")
    businessName: str | None = Field(default=None, description="The name of business.")
    city: str | None = Field(default=None, description="The city where business is located.")
    countryCode: str | None = Field(default=None, description="The country where business is located.")
    phoneNumber: str | None = Field(default=None, description="The phone number of business.")
    state: str | None = Field(default=None, description="The city where business is located.")
    zipCode: str | None = Field(default=None, description="The zipCode where business is located.")


class SellingAccountBusiness(BaseModel):
    """The business details of selling account."""

    model_config = ConfigDict(extra="allow")

    addresses: list[SellingAccountAddress] | None = Field(
        default=None, min_length=0, max_length=10, description="A list of business address the selling account has."
    )
    website: str | None = Field(default=None, description="The website of the business.")


class SellingAccountSellingAccountLinkTokenFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=1)


class SellingAccountSellingProgramFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[GeneralSellingProgram | str, lenient_enum(GeneralSellingProgram)]] = Field(
        min_length=1, max_length=1
    )


class SellingAccountSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    nextToken: str | None = Field(default=None)
    sellingAccounts: list[SellingAccount] | None = Field(default=None, min_length=0, max_length=100)


__all__ = [
    "GeneralCountryCode",
    "GeneralSellingProgram",
    "Portal",
    "QuerySellingAccountRequest",
    "SellingAccountSellingAccountLinkTokenFilter",
    "SellingAccountSellingProgramFilter",
]
