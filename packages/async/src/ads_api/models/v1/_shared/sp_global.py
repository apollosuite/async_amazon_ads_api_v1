"""Shared sp_global models reused across entities."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type SPGlobalAdProduct = Literal["SPONSORED_PRODUCTS"]
"""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
"""


type SPGlobalCreateState = Literal["ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


type SPGlobalCurrencyCode = Literal[
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


type SPGlobalDeliveryReason = Literal[
    "ADVERTISER_ARCHIVED",
    "ADVERTISER_OUT_OF_BUDGET",
    "ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT",
    "ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET",
    "ADVERTISER_OUT_OF_PREPAY_BALANCE",
    "ADVERTISER_PAUSED",
    "ADVERTISER_PAYMENT_FAILURE",
    "ADVERTISER_POLICING_PENDING_REVIEW",
    "ADVERTISER_POLICING_SUSPENDED",
    "AD_ARCHIVED",
    "AD_CREATION_FAILED",
    "AD_CREATION_IN_PROGRESS",
    "AD_GROUP_ARCHIVED",
    "AD_GROUP_INCOMPLETE",
    "AD_GROUP_LOW_BID",
    "AD_GROUP_PAUSED",
    "AD_GROUP_PENDING_REVIEW",
    "AD_GROUP_POLICING_PENDING_REVIEW",
    "AD_GROUP_REJECTED",
    "AD_INELIGIBLE",
    "AD_MISSING_DECORATION",
    "AD_MISSING_IMAGE",
    "AD_NOT_DELIVERING",
    "AD_PAUSED",
    "AD_POLICING_PENDING_REVIEW",
    "AD_POLICING_SUSPENDED",
    "BRAND_INELIGIBLE",
    "CAMPAIGN_ARCHIVED",
    "CAMPAIGN_END_DATE_REACHED",
    "CAMPAIGN_INCOMPLETE",
    "CAMPAIGN_OUT_OF_BUDGET",
    "CAMPAIGN_PAUSED",
    "CAMPAIGN_PENDING_REVIEW",
    "CAMPAIGN_PENDING_START_DATE",
    "CAMPAIGN_REJECTED",
    "CREATIVE_MISSING_ASSET",
    "CREATIVE_PENDING_REVIEW",
    "CREATIVE_REJECTED",
    "LANDING_PAGE_INELIGIBLE",
    "LANDING_PAGE_NOT_AVAILABLE",
    "MODERATION_ADULT_NOVELTY_POLICY_VIOLATION",
    "MODERATION_ADULT_PRODUCT_POLICY_VIOLATION",
    "MODERATION_ADULT_SOFTLINES_POLICY_VIOLATION",
    "MODERATION_CLAIM_WEIGHTLOSS_POLICY_VIOLATION",
    "MODERATION_CONTENT_NUDITY_POLICY_VIOLATION",
    "MODERATION_CONTENT_PROVOCATIVE_POLICY_VIOLATION",
    "MODERATION_CONTENT_SMOKING_POLICY_VIOLATION",
    "MODERATION_CRITICAL_EVENTS_POLICY_VIOLATION",
    "MODERATION_ERROR_404",
    "MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION",
    "MODERATION_HFSS_PRODUCT_POLICY_VIOLATION",
    "MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION",
    "MODERATION_NOT_COMPLIANT_TO_AD_POLICY",
    "MODERATION_SMOKING_RELATED_POLICY_VIOLATION",
    "NOT_BUYABLE",
    "NOT_IN_BUYBOX",
    "NOT_IN_POLICY",
    "NO_INVENTORY",
    "NO_PURCHASABLE_OFFER",
    "OTHER",
    "OUT_OF_REWARD_BUDGET",
    "OUT_OF_STOCK",
    "PIR_RULE_EXCLUDED",
    "PORTFOLIO_ARCHIVED",
    "PORTFOLIO_END_DATE_REACHED",
    "PORTFOLIO_OUT_OF_BUDGET",
    "PORTFOLIO_PAUSED",
    "PORTFOLIO_PENDING_START_DATE",
    "SECURITY_SCAN_PENDING_REVIEW",
    "SECURITY_SCAN_REJECTED",
    "SPEND_LIMIT_EXCEEDED",
    "STATUS_UNAVAILABLE",
    "TARGET_ARCHIVED",
    "TARGET_BLOCKED",
    "TARGET_PAUSED",
    "TARGET_POLICING_SUSPENDED",
]
"""
Supported values:
- `ADVERTISER_OUT_OF_BUDGET`: Indicates that an advertiser is out of budget for Sponsored Products campaigns for sellers.
- `ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT`: Indicates that a postpay advertiser is out of credit limit for all Sponsored Ads campaigns.
- `ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET`: Indicates that a postpay advertiser is out of monthly budget for all Sponsored Ads campaigns.
- `ADVERTISER_OUT_OF_PREPAY_BALANCE`: Indicates that a prepay advertiser is out of prepay balance for all Sponsored Ads campaigns.
"""


type SPGlobalDeliveryStatus = Literal["DELIVERING", "LIMITED", "NOT_DELIVERING", "UNAVAILABLE"]
"""
Supported values:
- `DELIVERING`: Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
- `LIMITED`: Represents partial delivery status, applicable to global resources that have different delivery status across marketplaces
- `NOT_DELIVERING`: Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
- `UNAVAILABLE`: Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces
"""


type SPGlobalErrorCode = Literal[
    "ACTION_NOT_SUPPORTED",
    "ACTIVE_RESOURCE_LIMIT_EXCEEDED",
    "ARCHIVED_PARENT_CANNOT_CREATE",
    "ARCHIVED_PARENT_CANNOT_EDIT",
    "ARCHIVED_RESOURCE_CANNOT_EDIT",
    "AUTOCREATED_ENTITY_CANNOT_EDIT",
    "BAD_REQUEST",
    "CONFLICT",
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


type SPGlobalErrorMarketplace = Literal[
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
]


type SPGlobalMarketplace = Literal[
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
]
"""
A list of country codes representing Amazon marketplaces
"""


type SPGlobalMarketplaceScope = Literal["GLOBAL"]


type SPGlobalProductIdType = Literal["ASIN", "SKU"]
"""
Supported values:
- `ASIN`: ASIN identifier type.
- `SKU`: SKU identifier type.
"""


type SPGlobalState = Literal["ARCHIVED", "ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


type SPGlobalUpdateState = Literal["ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


class SPGlobalCreateTag(StrictModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SPGlobalError(LenientModel):
    code: SPGlobalErrorCode | str
    fieldLocation: str | None = Field(default=None)
    marketplace: SPGlobalErrorMarketplace | str | None = Field(default=None)
    message: str


class SPGlobalErrorsIndex(LenientModel):
    errors: list[SPGlobalError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=4999)


class SPGlobalStatus(LenientModel):
    deliveryReasons: list[SPGlobalDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: SPGlobalDeliveryStatus | str
    marketplaceSettings: list[SPGlobalStatusMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace level delivery status and reasons of global resources, for all the marketplaces the global resource is applicable in.",
    )


class SPGlobalStatusMarketplaceSetting(LenientModel):
    deliveryReasons: list[SPGlobalDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: SPGlobalDeliveryStatus | str
    marketplace: SPGlobalMarketplace | str


class SPGlobalTag(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


__all__ = [
    "SPGlobalAdProduct",
    "SPGlobalCreateState",
    "SPGlobalCreateTag",
    "SPGlobalCurrencyCode",
    "SPGlobalDeliveryReason",
    "SPGlobalDeliveryStatus",
    "SPGlobalError",
    "SPGlobalErrorCode",
    "SPGlobalErrorMarketplace",
    "SPGlobalErrorsIndex",
    "SPGlobalMarketplace",
    "SPGlobalMarketplaceScope",
    "SPGlobalProductIdType",
    "SPGlobalState",
    "SPGlobalStatus",
    "SPGlobalStatusMarketplaceSetting",
    "SPGlobalTag",
    "SPGlobalUpdateState",
]
