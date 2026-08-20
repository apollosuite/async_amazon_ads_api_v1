"""Auto-generated models for ManagerAccounts from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    Address,
    BusinessDetail,
    CreateAddress,
    CreateBusinessDetail,
    CurrencyCode,
    Error,
    ErrorCode,
    ErrorsIndex,
    IndustryVertical,
    TimeZoneIana,
)

type AccountUsageType = Literal["PRODUCTION", "TEST"]


class CreateManagerAccountRequest(StrictModel):
    managerAccounts: list[ManagerAccountCreate] = Field(min_length=1, max_length=10)


class ManagerAccount(LenientModel):
    accountUsageType: AccountUsageType | str | None = Field(default=None)
    businessDetails: BusinessDetail | None = Field(default=None)
    currencyCode: CurrencyCode | str | None = Field(default=None)
    industryVertical: IndustryVertical | str | None = Field(default=None)
    timeZoneIana: TimeZoneIana | str | None = Field(default=None)


class ManagerAccountCreate(StrictModel):
    accountUsageType: AccountUsageType | None = Field(default=None)
    businessDetails: CreateBusinessDetail | None = Field(default=None)
    currencyCode: CurrencyCode | None = Field(default=None)
    industryVertical: IndustryVertical | None = Field(default=None)
    timeZoneIana: TimeZoneIana | None = Field(default=None)


class ManagerAccountManagerAccountIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class ManagerAccountMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[ManagerAccountMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class ManagerAccountMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    managerAccount: ManagerAccount


class ManagerAccountSuccessResponse(LenientModel):
    managerAccounts: list[ManagerAccount] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class ManagerAccountUpdate(StrictModel):
    businessDetails: UpdateBusinessDetail | None = Field(default=None)
    currencyCode: CurrencyCode | None = Field(default=None)
    industryVertical: IndustryVertical | None = Field(default=None)
    managerAccountId: str | None = Field(default=None, description="The identifier of the manager account.")
    timeZoneIana: TimeZoneIana | None = Field(default=None)


class QueryManagerAccountRequest(StrictModel):
    managerAccountIdFilter: ManagerAccountManagerAccountIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=10, le=100)
    nextToken: str | None = Field(default=None)


class UpdateAddress(StrictModel):
    """The business address of advertising account."""

    addressLine1: str | None = Field(default=None, description="The address details - 1 of business.")
    addressLine2: str | None = Field(default=None, description="The address details - 2 of business.")
    businessName: str | None = Field(default=None, description="The name of business.")
    city: str | None = Field(default=None, description="The city where business is located.")
    countryCode: str | None = Field(default=None, description="The country where business is located.")
    phoneNumber: str | None = Field(default=None, description="The phone number of business.")
    state: str | None = Field(default=None, description="The city where business is located.")
    zipCode: str | None = Field(default=None, description="The zipCode where business is located.")


class UpdateBusinessDetail(StrictModel):
    """The business details of advertising account."""

    address: UpdateAddress | None = Field(default=None)
    addressToken: str | None = Field(default=None, description="The token of the business address being linked.")
    businessRegistrationNumber: str | None = Field(
        default=None, description="The business registration number of the business."
    )
    website: str | None = Field(default=None, description="The website of the business.")


class UpdateManagerAccountRequest(StrictModel):
    managerAccounts: list[ManagerAccountUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "AccountUsageType",
    "Address",
    "BusinessDetail",
    "CreateAddress",
    "CreateBusinessDetail",
    "CreateManagerAccountRequest",
    "CurrencyCode",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "IndustryVertical",
    "ManagerAccount",
    "ManagerAccountCreate",
    "ManagerAccountManagerAccountIdFilter",
    "ManagerAccountMultiStatusResponse",
    "ManagerAccountMultiStatusSuccess",
    "ManagerAccountSuccessResponse",
    "ManagerAccountUpdate",
    "QueryManagerAccountRequest",
    "TimeZoneIana",
    "UpdateAddress",
    "UpdateBusinessDetail",
    "UpdateManagerAccountRequest",
]
