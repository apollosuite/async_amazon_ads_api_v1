"""Shared st models reused across entities."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel
from ads_api.models._core.lenient_enum import lenient_enum


class STAdProduct(StrEnum):
    SPONSORED_TELEVISION = "SPONSORED_TELEVISION"  # Sponsored Television ad product.


class STCreateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class STCurrencyCode(StrEnum):
    AED = "AED"  # United Arab Emirates Dirham
    AUD = "AUD"  # Australian Dollar
    BRL = "BRL"  # Brazilian Real
    CAD = "CAD"  # Canadian Dollar
    CHF = "CHF"  # Swiss Franc
    CNY = "CNY"  # Chinese Yuan
    DKK = "DKK"  # Danish Krone
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound Sterling
    INR = "INR"  # Indian Rupee
    JPY = "JPY"  # Japanese Yen
    MXN = "MXN"  # Mexican Peso
    NOK = "NOK"  # Norwegian Krone
    SAR = "SAR"  # Saudi Riyal
    SEK = "SEK"  # Swedish Krona
    SGD = "SGD"  # Singapore Dollar
    TRY = "TRY"  # Turkish Lira
    USD = "USD"  # United States Dollar


class STDeliveryReason(StrEnum):
    AD_CREATIVES_NOT_RUNNING = "AD_CREATIVES_NOT_RUNNING"
    AD_GROUPS_NOT_RUNNING = "AD_GROUPS_NOT_RUNNING"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_ENDED = "AD_GROUP_ENDED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_PENDING_START_DATE = "AD_GROUP_PENDING_START_DATE"
    AD_GROUP_POLICING_SUSPENDED = "AD_GROUP_POLICING_SUSPENDED"
    AD_NOT_APPROVED_FOR_ALL_AD_GROUPS = "AD_NOT_APPROVED_FOR_ALL_AD_GROUPS"
    AD_NOT_ASSOCIATED_WITH_AD_GROUP = "AD_NOT_ASSOCIATED_WITH_AD_GROUP"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_END_DATE_REACHED = "CAMPAIGN_END_DATE_REACHED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    CAMPAIGN_POLICING_SUSPENDED = "CAMPAIGN_POLICING_SUSPENDED"
    OTHER = "OTHER"


class STDeliveryStatus(StrEnum):
    DELIVERING = "DELIVERING"  # Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
    LIMITED = "LIMITED"  # Represents partial delivery status, applicable to global resources that have different delivery status across marketplaces
    NOT_DELIVERING = "NOT_DELIVERING"  # Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
    UNAVAILABLE = "UNAVAILABLE"  # Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces


class STErrorCode(StrEnum):
    ACTION_NOT_SUPPORTED = "ACTION_NOT_SUPPORTED"  # The request is not supported.
    ACTIVE_RESOURCE_LIMIT_EXCEEDED = (
        "ACTIVE_RESOURCE_LIMIT_EXCEEDED"  # Too many live resources. Remove resources and try again.
    )
    ARCHIVED_PARENT_CANNOT_CREATE = (
        "ARCHIVED_PARENT_CANNOT_CREATE"  # New resources cannot be created within an archived parent.
    )
    ARCHIVED_PARENT_CANNOT_EDIT = "ARCHIVED_PARENT_CANNOT_EDIT"  # Resources within an archived parent cannot be edited.
    ARCHIVED_RESOURCE_CANNOT_EDIT = "ARCHIVED_RESOURCE_CANNOT_EDIT"  # Archived resources cannot be edited.
    AUTOCREATED_ENTITY_CANNOT_EDIT = "AUTOCREATED_ENTITY_CANNOT_EDIT"  # Autocreated entities cannot be edited. To complete this action, create the resource manually.
    BAD_REQUEST = "BAD_REQUEST"  # The request is not valid considering the documented schema.
    CONFLICT = "CONFLICT"  # Operation could not be completed due to a conflict. Please retry your request.
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"  # The request is too large. Consider splitting it into multiple requests.
    DATE_CANNOT_BE_NULL = "DATE_CANNOT_BE_NULL"  # Update the date.
    DATE_TOO_SOON = "DATE_TOO_SOON"  # Update the date to be further in the future.
    DUPLICATE_FIELD_VALUE_FOUND = "DUPLICATE_FIELD_VALUE_FOUND"  # Multiple resources share the non-unique field values. Remove the non-unique field value.
    DUPLICATE_RESOURCE_ID_FOUND = (
        "DUPLICATE_RESOURCE_ID_FOUND"  # Multiple resources share the same ID. Remove the duplicate ID.
    )
    DURATION_TOO_SHORT = "DURATION_TOO_SHORT"  # Update the length to be within the required range.
    FEATURE_DISCONTINUED = "FEATURE_DISCONTINUED"  # Feature has been discontinued.
    FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_SIZE_IS_OUT_OF_RANGE = "FIELD_SIZE_IS_OUT_OF_RANGE"  # Update the value to be within the required range.
    FIELD_VALUE_CANNOT_EDIT = "FIELD_VALUE_CANNOT_EDIT"  # Field value cannot be edited.
    FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS = (
        "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_CONTAINS_INVALID_CHARACTERS = (
        "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS"  # Remove the invalid characters and try again.
    )
    FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_VALUE_IS_EMPTY = "FIELD_VALUE_IS_EMPTY"  # Update the request with the required information for this resource.
    FIELD_VALUE_IS_INVALID = (
        "FIELD_VALUE_IS_INVALID"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_IS_NULL = "FIELD_VALUE_IS_NULL"  # Update the request with the required information for this resource.
    FIELD_VALUE_IS_OUT_OF_RANGE = "FIELD_VALUE_IS_OUT_OF_RANGE"  # Update the value to be within the required range.
    FIELD_VALUE_MISMATCH = "FIELD_VALUE_MISMATCH"  # Mismatch among resource field values.
    FIELD_VALUE_MUST_BE_EMPTY_OR_NULL = (
        "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_NOT_FOUND = (
        "FIELD_VALUE_NOT_FOUND"  # Resource specified in the field value not found. Try again with valid value.
    )
    FIELD_VALUE_NOT_UNIQUE = "FIELD_VALUE_NOT_UNIQUE"  # Resource field value conflicts with existing resource. Try again with an unique field value.
    FORBIDDEN = "FORBIDDEN"  # The caller is not authorized to make the given request.
    INTERNAL_ERROR = "INTERNAL_ERROR"  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    NOT_FOUND = "NOT_FOUND"  # The requested resource does not exist.
    PAYMENT_ISSUE = "PAYMENT_ISSUE"  # Payment failed.
    PRODUCT_INELIGIBLE = (
        "PRODUCT_INELIGIBLE"  # Product is not eligible for advertising. Try again with a valid product.
    )
    RESOURCE_DOES_NOT_BELONG_TO_PARENT = "RESOURCE_DOES_NOT_BELONG_TO_PARENT"  # Resource does not belong to the specified parent. Try again with a valid parent ID.
    RESOURCE_ID_NOT_FOUND = "RESOURCE_ID_NOT_FOUND"  # Resource ID not found. Try again with valid ID.
    RESOURCE_IS_EMPTY = "RESOURCE_IS_EMPTY"  # Update the request with the required information for this resource.
    RESOURCE_IS_IN_TERMINAL_STATE = "RESOURCE_IS_IN_TERMINAL_STATE"  # Resource is in terminal state.
    RESOURCE_IS_NULL = "RESOURCE_IS_NULL"  # Update the request with the required information for this resource.
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"  # There have been too many requests, please slow down your call rate.
    TOTAL_RESOURCE_LIMIT_EXCEEDED = (
        "TOTAL_RESOURCE_LIMIT_EXCEEDED"  # Too many resources. Remove resources and try again.
    )
    UNAUTHORIZED = "UNAUTHORIZED"  # The request lacks the necessary credentials.
    UNSUPPORTED_MARKETPLACE = (
        "UNSUPPORTED_MARKETPLACE"  # Marketplace not supported. Try again with a supported marketplace.
    )


class STState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ARCHIVED = "ARCHIVED"  # The object is permanently stopped and cannot be reactivated. Terminal end state.
    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class STUpdateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class STError(LenientModel):
    code: Annotated[STErrorCode | str, lenient_enum(STErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class STErrorsIndex(LenientModel):
    errors: list[STError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class STStatus(LenientModel):
    deliveryReasons: list[Annotated[STDeliveryReason | str, lenient_enum(STDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[STDeliveryStatus | str, lenient_enum(STDeliveryStatus)]


__all__ = [
    "STAdProduct",
    "STCreateState",
    "STCurrencyCode",
    "STDeliveryReason",
    "STDeliveryStatus",
    "STError",
    "STErrorCode",
    "STErrorsIndex",
    "STState",
    "STStatus",
    "STUpdateState",
]
