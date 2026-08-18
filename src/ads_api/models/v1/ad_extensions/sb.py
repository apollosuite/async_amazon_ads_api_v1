"""Auto-generated models for AdExtensions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBAdProduct,
    SBCreateState,
    SBMarketplaceScope,
    SBState,
    SBUpdateState,
)

type SBAdExtensionStatus = Literal["OPTED_OUT",]  # If the advertiser has opted out of this Ad Extension.
"""
Ad Extension Status.

Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
"""


type SBAdExtensionType = Literal["PROMPTS",]  # Enables Prompt based Ad Extension.
"""
Ad Extension Type.

Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
"""


type SBErrorCode = Literal[
    "ACTION_NOT_SUPPORTED",  # The request is not supported.
    "ACTIVE_RESOURCE_LIMIT_EXCEEDED",  # Too many live resources. Remove resources and try again.
    "ARCHIVED_PARENT_CANNOT_CREATE",  # New resources cannot be created within an archived parent.
    "ARCHIVED_PARENT_CANNOT_EDIT",  # Resources within an archived parent cannot be edited.
    "ARCHIVED_RESOURCE_CANNOT_EDIT",  # Archived resources cannot be edited.
    "AUTOCREATED_ENTITY_CANNOT_EDIT",  # Autocreated entities cannot be edited. To complete this action, create the resource manually.
    "BAD_REQUEST",  # The request is not valid considering the documented schema.
    "CONFLICT",  # Operation could not be completed due to a conflict. Please retry your request.
    "CONTENT_TOO_LARGE",  # The request is too large. Consider splitting it into multiple requests.
    "DATE_CANNOT_BE_IN_PAST",  # Update the date to be in the future.
    "DATE_CANNOT_BE_NULL",  # Update the date.
    "DATE_TOO_SOON",  # Update the date to be further in the future.
    "DUPLICATE_FIELD_VALUE_FOUND",  # Multiple resources share the non-unique field values. Remove the non-unique field value.
    "DUPLICATE_RESOURCE_ID_FOUND",  # Multiple resources share the same ID. Remove the duplicate ID.
    "DURATION_TOO_SHORT",  # Update the length to be within the required range.
    "FEATURE_DISCONTINUED",  # Feature has been discontinued.
    "FEATURE_NOT_AVAILABLE",  # The requested feature is not available.
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
- `ACTION_NOT_SUPPORTED`: The request is not supported.
- `ACTIVE_RESOURCE_LIMIT_EXCEEDED`: Too many live resources. Remove resources and try again.
- `ARCHIVED_PARENT_CANNOT_CREATE`: New resources cannot be created within an archived parent.
- `ARCHIVED_PARENT_CANNOT_EDIT`: Resources within an archived parent cannot be edited.
- `ARCHIVED_RESOURCE_CANNOT_EDIT`: Archived resources cannot be edited.
- `AUTOCREATED_ENTITY_CANNOT_EDIT`: Autocreated entities cannot be edited. To complete this action, create the resource manually.
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `CONFLICT`: Operation could not be completed due to a conflict. Please retry your request.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `DATE_CANNOT_BE_IN_PAST`: Update the date to be in the future.
- `DATE_CANNOT_BE_NULL`: Update the date.
- `DATE_TOO_SOON`: Update the date to be further in the future.
- `DUPLICATE_FIELD_VALUE_FOUND`: Multiple resources share the non-unique field values. Remove the non-unique field value.
- `DUPLICATE_RESOURCE_ID_FOUND`: Multiple resources share the same ID. Remove the duplicate ID.
- `DURATION_TOO_SHORT`: Update the length to be within the required range.
- `FEATURE_DISCONTINUED`: Feature has been discontinued.
- `FEATURE_NOT_AVAILABLE`: The requested feature is not available.
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


type SBMarketplace = Literal[
    "AE",
    "AU",
    "BE",
    "BR",
    "CA",
    "DE",
    "EG",
    "ES",
    "FR",
    "GB",
    "IE",
    "IN",
    "IT",
    "JP",
    "MX",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "US",
    "ZA",
]
"""
A list of country codes representing Amazon marketplaces
"""


class SBAdExtension(LenientModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    adExtensionSettings: SBAdExtensionSettings
    adExtensionStatus: SBAdExtensionStatus | str | None = Field(
        default=None,
        description="""
Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
""",
    )
    adExtensionType: SBAdExtensionType | str = Field(description="""
Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
""")
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SBAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_BRANDS`: Sponsored Brands ad product.
""")
    creationDateTime: datetime = Field(description="The date time the ad_extension was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the ad_extension was last updated.")
    marketplaceScope: SBMarketplaceScope | str
    marketplaces: list[SBMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SBState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")


class SBAdExtensionAdExtensionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBAdExtensionAdExtensionStatusFilter(StrictModel):
    include: list[SBAdExtensionStatus | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
""",
    )


class SBAdExtensionAdExtensionTypeFilter(StrictModel):
    include: list[SBAdExtensionType | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
""",
    )


class SBAdExtensionAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBAdExtensionAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SBAdExtensionAdProductFilter(StrictModel):
    include: list[SBAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_BRANDS`: Sponsored Brands ad product.
""",
    )


class SBAdExtensionCreate(StrictModel):
    adExtensionSettings: SBCreateAdExtensionSettings
    adExtensionStatus: SBAdExtensionStatus | None = Field(
        default=None,
        description="""
Supported values:
- `OPTED_OUT`: If the advertiser has opted out of this Ad Extension.
""",
    )
    adExtensionType: SBAdExtensionType = Field(description="""
Supported values:
- `PROMPTS`: Enables Prompt based Ad Extension.
""")
    adGroupId: str | None = Field(
        default=None, description="A unique identifier for the ad group associated with the ad_extension."
    )
    adId: str | None = Field(
        default=None, description="A unique identifier for the ad associated with the ad_extension."
    )
    adProduct: SBAdProduct = Field(description="""
Supported values:
- `SPONSORED_BRANDS`: Sponsored Brands ad product.
""")
    marketplaceScope: SBMarketplaceScope
    marketplaces: list[SBMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of marketplace in which the global ad_extension is applicable. The marketplaces included should either be same as or subset of parent campaign/adGroup/ad",
    )
    state: SBCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")


class SBAdExtensionMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=50)
    success: list[SBAdExtensionMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=50)


class SBAdExtensionMultiStatusSuccess(LenientModel):
    adExtension: SBAdExtension
    index: int = Field(ge=0, le=49)


class SBAdExtensionSettings(LenientModel):
    promptExtension: SBPromptExtension


class SBAdExtensionStateFilter(StrictModel):
    include: list[SBState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SBAdExtensionSuccessResponse(LenientModel):
    adExtensions: list[SBAdExtension] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SBAdExtensionUpdate(StrictModel):
    adExtensionId: str = Field(description="A unique identifier for the ad_extension.")
    state: SBUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SBCreateAdExtensionRequest(StrictModel):
    adExtensions: list[SBAdExtensionCreate] = Field(min_length=1, max_length=50)


class SBCreateAdExtensionSettings(StrictModel):
    promptExtension: SBCreatePromptExtension


class SBCreatePromptExtension(StrictModel):
    """Prompts Ad Extension"""

    promptText: str = Field(description="The prompt text rendered in the ads")


class SBError(LenientModel):
    code: SBErrorCode | str = Field(description="""
Supported values:
- `ACTION_NOT_SUPPORTED`: The request is not supported.
- `ACTIVE_RESOURCE_LIMIT_EXCEEDED`: Too many live resources. Remove resources and try again.
- `ARCHIVED_PARENT_CANNOT_CREATE`: New resources cannot be created within an archived parent.
- `ARCHIVED_PARENT_CANNOT_EDIT`: Resources within an archived parent cannot be edited.
- `ARCHIVED_RESOURCE_CANNOT_EDIT`: Archived resources cannot be edited.
- `AUTOCREATED_ENTITY_CANNOT_EDIT`: Autocreated entities cannot be edited. To complete this action, create the resource manually.
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `CONFLICT`: Operation could not be completed due to a conflict. Please retry your request.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `DATE_CANNOT_BE_IN_PAST`: Update the date to be in the future.
- `DATE_CANNOT_BE_NULL`: Update the date.
- `DATE_TOO_SOON`: Update the date to be further in the future.
- `DUPLICATE_FIELD_VALUE_FOUND`: Multiple resources share the non-unique field values. Remove the non-unique field value.
- `DUPLICATE_RESOURCE_ID_FOUND`: Multiple resources share the same ID. Remove the duplicate ID.
- `DURATION_TOO_SHORT`: Update the length to be within the required range.
- `FEATURE_DISCONTINUED`: Feature has been discontinued.
- `FEATURE_NOT_AVAILABLE`: The requested feature is not available.
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
    index: int = Field(ge=0, le=4999)


class SBPromptExtension(LenientModel):
    """Prompts Ad Extension"""

    promptText: str = Field(description="The prompt text rendered in the ads")


class SBQueryAdExtensionRequest(StrictModel):
    adExtensionIdFilter: SBAdExtensionAdExtensionIdFilter | None = Field(default=None)
    adExtensionStatusFilter: SBAdExtensionAdExtensionStatusFilter | None = Field(default=None)
    adExtensionTypeFilter: SBAdExtensionAdExtensionTypeFilter | None = Field(default=None)
    adGroupIdFilter: SBAdExtensionAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SBAdExtensionAdIdFilter | None = Field(default=None)
    adProductFilter: SBAdExtensionAdProductFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: SBAdExtensionStateFilter | None = Field(default=None)


class SBUpdateAdExtensionRequest(StrictModel):
    adExtensions: list[SBAdExtensionUpdate] = Field(min_length=1, max_length=50)


__all__ = [
    "SBAdExtension",
    "SBAdExtensionAdExtensionIdFilter",
    "SBAdExtensionAdExtensionStatusFilter",
    "SBAdExtensionAdExtensionTypeFilter",
    "SBAdExtensionAdGroupIdFilter",
    "SBAdExtensionAdIdFilter",
    "SBAdExtensionAdProductFilter",
    "SBAdExtensionCreate",
    "SBAdExtensionMultiStatusResponse",
    "SBAdExtensionMultiStatusSuccess",
    "SBAdExtensionSettings",
    "SBAdExtensionStateFilter",
    "SBAdExtensionStatus",
    "SBAdExtensionSuccessResponse",
    "SBAdExtensionType",
    "SBAdExtensionUpdate",
    "SBAdProduct",
    "SBCreateAdExtensionRequest",
    "SBCreateAdExtensionSettings",
    "SBCreatePromptExtension",
    "SBCreateState",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBPromptExtension",
    "SBQueryAdExtensionRequest",
    "SBState",
    "SBUpdateAdExtensionRequest",
    "SBUpdateState",
]
