"""Auto-generated models for AdvertisingDeals from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBAdvertisingDealPriceType,
)

type SBAdvertisingDealNameFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `BROAD_MATCH`: Filter by broad match.
- `EXACT_MATCH`: Filter by exact match.
"""


type SBAdvertisingDealState = Literal["DRAFT", "PROPOSED"]


type SBAdvertisingDealStatusEnum = Literal["DRAFT", "MODERATION_APPROVED", "PROPOSED"]
"""
Supported values:
- `DRAFT`: The deal has not been submitted yet.
- `MODERATION_APPROVED`: The deal has passed moderation.
- `PROPOSED`: The deal has been submitted for moderation.
"""


type SBCurrencyCode = Literal[
    "AED",
    "AUD",
    "BRL",
    "CAD",
    "CHF",
    "CNY",
    "DKK",
    "EGP",
    "EUR",
    "GBP",
    "INR",
    "JPY",
    "MXN",
    "MXP",
    "NGN",
    "NOK",
    "NZD",
    "PLN",
    "SAR",
    "SEK",
    "SGD",
    "TRY",
    "USD",
    "ZAR",
]
"""
Supported values:
- `AED`: United Arab Emirates Dirham
- `AUD`: Australian Dollar
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `CHF`: Swiss Franc
- `CNY`: Chinese Yuan
- `DKK`: Danish Krone
- `EGP`: Egyptian Pound
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `INR`: Indian Rupee
- `JPY`: Japanese Yen
- `MXN`: Mexican Peso
- `MXP`: Mexican Peso
- `NGN`: Nigerian Naira
- `NOK`: Norwegian Krone
- `NZD`: New Zealand Dollar
- `PLN`: Polish Złoty
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `TRY`: Turkish Lira
- `USD`: United States Dollar
- `ZAR`: South African Rand
"""


type SBErrorCode = Literal[
    "BAD_REQUEST",
    "CONTENT_TOO_LARGE",
    "DATE_CANNOT_BE_IN_PAST",
    "DATE_CANNOT_BE_NULL",
    "DATE_TOO_SOON",
    "DUPLICATE_FIELD_VALUE_FOUND",
    "DUPLICATE_RESOURCE_ID_FOUND",
    "DURATION_TOO_SHORT",
    "FEATURE_DISCONTINUED",
    "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT",
    "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT",
    "FIELD_SIZE_IS_OUT_OF_RANGE",
    "FIELD_VALUE_CANNOT_EDIT",
    "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS",
    "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS",
    "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT",
    "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT",
    "FIELD_VALUE_IS_EMPTY",
    "FIELD_VALUE_IS_INVALID",
    "FIELD_VALUE_IS_NULL",
    "FIELD_VALUE_IS_OUT_OF_RANGE",
    "FIELD_VALUE_MISMATCH",
    "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL",
    "FIELD_VALUE_NOT_FOUND",
    "FIELD_VALUE_NOT_UNIQUE",
    "FORBIDDEN",
    "INTERNAL_ERROR",
    "NOT_FOUND",
    "PAYMENT_ISSUE",
    "PRODUCT_INELIGIBLE",
    "RESOURCE_DOES_NOT_BELONG_TO_PARENT",
    "RESOURCE_ID_NOT_FOUND",
    "RESOURCE_IS_EMPTY",
    "RESOURCE_IS_IN_TERMINAL_STATE",
    "RESOURCE_IS_NULL",
    "TOO_MANY_REQUESTS",
    "TOTAL_RESOURCE_LIMIT_EXCEEDED",
    "UNAUTHORIZED",
    "UNSUPPORTED_MARKETPLACE",
]
"""
Supported values:
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `DATE_CANNOT_BE_IN_PAST`: Update the date to be in the future.
- `DATE_CANNOT_BE_NULL`: Update the date.
- `DATE_TOO_SOON`: Update the date to be further in the future.
- `DUPLICATE_FIELD_VALUE_FOUND`: Multiple resources share the non-unique field values. Remove the non-unique field value.
- `DUPLICATE_RESOURCE_ID_FOUND`: Multiple resources share the same ID. Remove the duplicate ID.
- `DURATION_TOO_SHORT`: Update the length to be within the required range.
- `FEATURE_DISCONTINUED`: Feature has been discontinued.
- `FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_SIZE_IS_OUT_OF_RANGE`: Update the value to be within the required range.
- `FIELD_VALUE_CANNOT_EDIT`: Field value cannot be edited.
- `FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS`: Update the request with the required information for this resource.
- `FIELD_VALUE_CONTAINS_INVALID_CHARACTERS`: Remove the invalid characters and try again.
- `FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_VALUE_IS_EMPTY`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_INVALID`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_NULL`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_OUT_OF_RANGE`: Update the value to be within the required range.
- `FIELD_VALUE_MISMATCH`: Mismatch among resource field values.
- `FIELD_VALUE_MUST_BE_EMPTY_OR_NULL`: Update the request with the required information for this resource.
- `FIELD_VALUE_NOT_FOUND`: Resource specified in the field value not found. Try again with valid value.
- `FIELD_VALUE_NOT_UNIQUE`: Resource field value conflicts with existing resource. Try again with an unique field value.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `PAYMENT_ISSUE`: Payment failed.
- `PRODUCT_INELIGIBLE`: Product is not eligible for advertising. Try again with a valid product.
- `RESOURCE_DOES_NOT_BELONG_TO_PARENT`: Resource does not belong to the specified parent. Try again with a valid parent ID.
- `RESOURCE_ID_NOT_FOUND`: Resource ID not found. Try again with valid ID.
- `RESOURCE_IS_EMPTY`: Update the request with the required information for this resource.
- `RESOURCE_IS_IN_TERMINAL_STATE`: Resource is in terminal state.
- `RESOURCE_IS_NULL`: Update the request with the required information for this resource.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `TOTAL_RESOURCE_LIMIT_EXCEEDED`: Too many resources. Remove resources and try again.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
- `UNSUPPORTED_MARKETPLACE`: Marketplace not supported. Try again with a supported marketplace.
"""


class SBAdvertisingDeal(LenientModel):
    advertisingDealId: str = Field(description="A unique identifier for a deal.")
    endDateTime: datetime = Field(description="The end date time for the deal.")
    name: str = Field(description="The name of the deal.")
    price: SBAdvertisingDealPrice | None = Field(default=None)
    replacingDealId: str | None = Field(
        default=None, description="The ID of an advertising deal that this deal intends to replace."
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")
    state: SBAdvertisingDealState | str | None = Field(default=None)
    status: SBAdvertisingDealStatus


class SBAdvertisingDealAdvertisingDealIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBAdvertisingDealCreate(StrictModel):
    endDateTime: datetime = Field(description="The end date time for the deal.")
    name: str = Field(description="The name of the deal.")
    price: SBCreateAdvertisingDealPrice | None = Field(default=None)
    replacingDealId: str | None = Field(
        default=None, description="The ID of an advertising deal that this deal intends to replace."
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")
    state: SBAdvertisingDealState | None = Field(default=None)


class SBAdvertisingDealMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBAdvertisingDealMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBAdvertisingDealMultiStatusSuccess(LenientModel):
    advertisingDeal: SBAdvertisingDeal
    index: int = Field(ge=0, le=9)


class SBAdvertisingDealNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)
    queryTermMatchType: SBAdvertisingDealNameFilterType


class SBAdvertisingDealPrice(LenientModel):
    currencyCode: SBCurrencyCode | str
    priceType: SBAdvertisingDealPriceType | str
    value: float = Field(description="The monetary amount of the price in the given currency.")


class SBAdvertisingDealStatus(LenientModel):
    status: SBAdvertisingDealStatusEnum | str


class SBAdvertisingDealSuccessResponse(LenientModel):
    advertisingDeals: list[SBAdvertisingDeal] | None = Field(default=None, min_length=0, max_length=50)
    nextToken: str | None = Field(default=None)


class SBAdvertisingDealUpdate(StrictModel):
    advertisingDealId: str = Field(description="A unique identifier for a deal.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the deal.")
    name: str | None = Field(default=None, description="The name of the deal.")
    price: SBUpdateAdvertisingDealPrice | None = Field(default=None)
    replacingDealId: str | None = Field(
        default=None, description="The ID of an advertising deal that this deal intends to replace."
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the deal.")
    state: SBAdvertisingDealState | None = Field(default=None)


class SBCreateAdvertisingDealPrice(StrictModel):
    priceType: SBAdvertisingDealPriceType
    value: float = Field(description="The monetary amount of the price in the given currency.")


class SBCreateAdvertisingDealRequest(StrictModel):
    advertisingDeals: list[SBAdvertisingDealCreate] | None = Field(default=None, min_length=1, max_length=10)


class SBDeleteAdvertisingDealRequest(StrictModel):
    advertisingDealIds: list[str] | None = Field(default=None, min_length=1, max_length=10)


class SBError(LenientModel):
    code: SBErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class SBErrorsIndex(LenientModel):
    errors: list[SBError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SBQueryAdvertisingDealRequest(StrictModel):
    advertisingDealIdFilter: SBAdvertisingDealAdvertisingDealIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=10, ge=1, le=50)
    nameFilter: SBAdvertisingDealNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)


class SBUpdateAdvertisingDealPrice(StrictModel):
    priceType: SBAdvertisingDealPriceType | None = Field(default=None)
    value: float | None = Field(default=None, description="The monetary amount of the price in the given currency.")


class SBUpdateAdvertisingDealRequest(StrictModel):
    advertisingDeals: list[SBAdvertisingDealUpdate] | None = Field(default=None, min_length=1, max_length=10)


__all__ = [
    "SBAdvertisingDeal",
    "SBAdvertisingDealAdvertisingDealIdFilter",
    "SBAdvertisingDealCreate",
    "SBAdvertisingDealMultiStatusResponse",
    "SBAdvertisingDealMultiStatusSuccess",
    "SBAdvertisingDealNameFilter",
    "SBAdvertisingDealNameFilterType",
    "SBAdvertisingDealPrice",
    "SBAdvertisingDealPriceType",
    "SBAdvertisingDealState",
    "SBAdvertisingDealStatus",
    "SBAdvertisingDealStatusEnum",
    "SBAdvertisingDealSuccessResponse",
    "SBAdvertisingDealUpdate",
    "SBCreateAdvertisingDealPrice",
    "SBCreateAdvertisingDealRequest",
    "SBCurrencyCode",
    "SBDeleteAdvertisingDealRequest",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBQueryAdvertisingDealRequest",
    "SBUpdateAdvertisingDealPrice",
    "SBUpdateAdvertisingDealRequest",
]
