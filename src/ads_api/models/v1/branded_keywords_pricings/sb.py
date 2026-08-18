"""Auto-generated models for BrandedKeywordsPricings from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBAdvertisingDealPriceType,
)

type SBCurrencyCode = Literal[
    "AED",  # United Arab Emirates Dirham
    "AUD",  # Australian Dollar
    "BRL",  # Brazilian Real
    "CAD",  # Canadian Dollar
    "CHF",  # Swiss Franc
    "CNY",  # Chinese Yuan
    "DKK",  # Danish Krone
    "EGP",  # Egyptian Pound
    "EUR",  # Euro
    "GBP",  # British Pound Sterling
    "INR",  # Indian Rupee
    "JPY",  # Japanese Yen
    "MXN",  # Mexican Peso
    "MXP",  # Mexican Peso
    "NGN",  # Nigerian Naira
    "NOK",  # Norwegian Krone
    "NZD",  # New Zealand Dollar
    "PLN",  # Polish Złoty
    "SAR",  # Saudi Riyal
    "SEK",  # Swedish Krona
    "SGD",  # Singapore Dollar
    "TRY",  # Turkish Lira
    "USD",  # United States Dollar
    "ZAR",  # South African Rand
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
    "BAD_REQUEST",  # The request is not valid considering the documented schema.
    "CONTENT_TOO_LARGE",  # The request is too large. Consider splitting it into multiple requests.
    "DATE_CANNOT_BE_IN_PAST",  # Update the date to be in the future.
    "DATE_CANNOT_BE_NULL",  # Update the date.
    "DATE_TOO_SOON",  # Update the date to be further in the future.
    "DUPLICATE_FIELD_VALUE_FOUND",  # Multiple resources share the non-unique field values. Remove the non-unique field value.
    "DUPLICATE_RESOURCE_ID_FOUND",  # Multiple resources share the same ID. Remove the duplicate ID.
    "DURATION_TOO_SHORT",  # Update the length to be within the required range.
    "FEATURE_DISCONTINUED",  # Feature has been discontinued.
    "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT",  # Update the value to be within the required range.
    "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT",  # Update the value to be within the required range.
    "FIELD_SIZE_IS_OUT_OF_RANGE",  # Update the value to be within the required range.
    "FIELD_VALUE_CANNOT_EDIT",  # Field value cannot be edited.
    "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS",  # Update the request with the required information for this resource.
    "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS",  # Remove the invalid characters and try again.
    "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT",  # Update the value to be within the required range.
    "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT",  # Update the value to be within the required range.
    "FIELD_VALUE_IS_EMPTY",  # Update the request with the required information for this resource.
    "FIELD_VALUE_IS_INVALID",  # Update the request with the required information for this resource.
    "FIELD_VALUE_IS_NULL",  # Update the request with the required information for this resource.
    "FIELD_VALUE_IS_OUT_OF_RANGE",  # Update the value to be within the required range.
    "FIELD_VALUE_MISMATCH",  # Mismatch among resource field values.
    "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL",  # Update the request with the required information for this resource.
    "FIELD_VALUE_NOT_FOUND",  # Resource specified in the field value not found. Try again with valid value.
    "FIELD_VALUE_NOT_UNIQUE",  # Resource field value conflicts with existing resource. Try again with an unique field value.
    "FORBIDDEN",  # The caller is not authorized to make the given request.
    "INTERNAL_ERROR",  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    "NOT_FOUND",  # The requested resource does not exist.
    "PAYMENT_ISSUE",  # Payment failed.
    "PRODUCT_INELIGIBLE",  # Product is not eligible for advertising. Try again with a valid product.
    "RESOURCE_DOES_NOT_BELONG_TO_PARENT",  # Resource does not belong to the specified parent. Try again with a valid parent ID.
    "RESOURCE_ID_NOT_FOUND",  # Resource ID not found. Try again with valid ID.
    "RESOURCE_IS_EMPTY",  # Update the request with the required information for this resource.
    "RESOURCE_IS_IN_TERMINAL_STATE",  # Resource is in terminal state.
    "RESOURCE_IS_NULL",  # Update the request with the required information for this resource.
    "TOO_MANY_REQUESTS",  # There have been too many requests, please slow down your call rate.
    "TOTAL_RESOURCE_LIMIT_EXCEEDED",  # Too many resources. Remove resources and try again.
    "UNAUTHORIZED",  # The request lacks the necessary credentials.
    "UNSUPPORTED_MARKETPLACE",  # Marketplace not supported. Try again with a supported marketplace.
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


class SBAdvertisingDealPrice(LenientModel):
    currencyCode: SBCurrencyCode | str = Field(description="""
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
""")
    priceType: SBAdvertisingDealPriceType | str = Field(description="""
Supported values:
- `FIXED_PRICE`: Sale price for a specific ad placement regardless of auction performance.
""")
    value: float = Field(description="The monetary amount of the price in the given currency.")


class SBBrandedKeywordsPricing(LenientModel):
    advertisingDealId: str | None = Field(
        default=None, description="Identifier of the existing deal to price. Omit when pricing a new deal."
    )
    brandedKeywordsPricingId: str = Field(description="A unique identifier for the branded keywords pricing.")
    endDateTime: datetime = Field(description="The end date time for the deal.")
    keywords: list[str] = Field(
        min_length=1, max_length=1000, description="The list of branded keywords advertiser wants to reserve."
    )
    keywordsPricing: SBKeywordsPricing | None = Field(default=None)
    rejectedKeywords: list[SBRejectedKeyword] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="The list of branded keywords rejected for reservation by this advertiser.",
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")


class SBBrandedKeywordsPricingCreate(StrictModel):
    advertisingDealId: str | None = Field(
        default=None, description="Identifier of the existing deal to price. Omit when pricing a new deal."
    )
    endDateTime: datetime = Field(description="The end date time for the deal.")
    keywords: list[str] = Field(
        min_length=1, max_length=1000, description="The list of branded keywords advertiser wants to reserve."
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")


class SBBrandedKeywordsPricingMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBBrandedKeywordsPricingMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBBrandedKeywordsPricingMultiStatusSuccess(LenientModel):
    brandedKeywordsPricing: SBBrandedKeywordsPricing
    index: int = Field(ge=0, le=9)


class SBCreateBrandedKeywordsPricingRequest(StrictModel):
    brandedKeywordsPricings: list[SBBrandedKeywordsPricingCreate] | None = Field(
        default=None, min_length=1, max_length=10
    )


class SBError(LenientModel):
    code: SBErrorCode | str = Field(description="""
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
""")
    fieldLocation: str | None = Field(default=None)
    message: str


class SBErrorsIndex(LenientModel):
    errors: list[SBError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SBKeywordsPricing(LenientModel):
    """The detail of keywords pricing."""

    price: SBAdvertisingDealPrice
    validKeywords: list[str] = Field(min_length=1, max_length=1000, description="List of valid keywords.")


class SBRejectedKeyword(LenientModel):
    """The detail of a rejected keyword."""

    keyword: str = Field(description="The keyword that has been rejected.")
    reason: str = Field(description="The reason keyword has been rejected for this advertiser.")


__all__ = [
    "SBAdvertisingDealPrice",
    "SBAdvertisingDealPriceType",
    "SBBrandedKeywordsPricing",
    "SBBrandedKeywordsPricingCreate",
    "SBBrandedKeywordsPricingMultiStatusResponse",
    "SBBrandedKeywordsPricingMultiStatusSuccess",
    "SBCreateBrandedKeywordsPricingRequest",
    "SBCurrencyCode",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBKeywordsPricing",
    "SBRejectedKeyword",
]
