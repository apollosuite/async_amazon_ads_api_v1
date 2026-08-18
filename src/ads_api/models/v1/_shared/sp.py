"""Shared sp models reused across entities."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type SPAdProduct = Literal["SPONSORED_PRODUCTS",]  # Sponsored Products ad product.
"""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
"""


type SPCreateState = Literal[
    "ENABLED",  # The object is set active by user and eligible for delivery.
    "PAUSED",  # The object is stopped by user and not eligible for delivery.
]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


type SPCurrencyCode = Literal[
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


type SPDeliveryReason = Literal[
    "ADVERTISER_ARCHIVED",
    "ADVERTISER_OUT_OF_BUDGET",  # Indicates that an advertiser is out of budget for Sponsored Products campaigns for sellers.
    "ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT",  # Indicates that a postpay advertiser is out of credit limit for all Sponsored Ads campaigns.
    "ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET",  # Indicates that a postpay advertiser is out of monthly budget for all Sponsored Ads campaigns.
    "ADVERTISER_OUT_OF_PREPAY_BALANCE",  # Indicates that a prepay advertiser is out of prepay balance for all Sponsored Ads campaigns.
    "ADVERTISER_PAUSED",
    "ADVERTISER_PAYMENT_FAILURE",
    "ADVERTISER_POLICING_PENDING_REVIEW",
    "ADVERTISER_POLICING_SUSPENDED",
    "AD_ARCHIVED",
    "AD_CREATION_FAILED",
    "AD_CREATION_IN_PROGRESS",
    "AD_EXTENSION_ARCHIVED",
    "AD_EXTENSION_PAUSED",
    "AD_EXTENSION_POLICING_PENDING_REVIEW",
    "AD_EXTENSION_POLICING_SUSPENDED",
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


type SPDeliveryStatus = Literal[
    "DELIVERING",  # Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
    "NOT_DELIVERING",  # Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
    "UNAVAILABLE",  # Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces
]
"""
Supported values:
- `DELIVERING`: Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
- `NOT_DELIVERING`: Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
- `UNAVAILABLE`: Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces
"""


type SPErrorCode = Literal[
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
    "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO",  # The campaign is associated with a global campaign. Portfolio association cannot be updated on a child campaign. Please perform operation on the global campaign.
    "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE",  # The campaign is associated with a global campaign. The state on child campaign cannot be set to archived. Please perform operation on global campaign.
    "GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT",  # The campaign is associated with a global campaign. Only one ad group can be created under this campaign.
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
- `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO`: The campaign is associated with a global campaign. Portfolio association cannot be updated on a child campaign. Please perform operation on the global campaign.
- `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE`: The campaign is associated with a global campaign. The state on child campaign cannot be set to archived. Please perform operation on global campaign.
- `GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT`: The campaign is associated with a global campaign. Only one ad group can be created under this campaign.
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


type SPMarketplaceScope = Literal["SINGLE_MARKETPLACE"]


type SPProductIdType = Literal[
    "ASIN",  # ASIN identifier type.
    "SKU",  # SKU identifier type.
]
"""
Supported values:
- `ASIN`: ASIN identifier type.
- `SKU`: SKU identifier type.
"""


type SPState = Literal[
    "ARCHIVED",  # The object is permanently stopped and cannot be reactivated. Terminal end state.
    "ENABLED",  # The object is set active by user and eligible for delivery.
    "PAUSED",  # The object is stopped by user and not eligible for delivery.
]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


type SPUpdateState = Literal[
    "ENABLED",  # The object is set active by user and eligible for delivery.
    "PAUSED",  # The object is stopped by user and not eligible for delivery.
]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
"""


class SPCreateTag(StrictModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SPError(LenientModel):
    code: SPErrorCode | str = Field(description="""
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
- `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO`: The campaign is associated with a global campaign. Portfolio association cannot be updated on a child campaign. Please perform operation on the global campaign.
- `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE`: The campaign is associated with a global campaign. The state on child campaign cannot be set to archived. Please perform operation on global campaign.
- `GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT`: The campaign is associated with a global campaign. Only one ad group can be created under this campaign.
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


class SPErrorsIndex(LenientModel):
    errors: list[SPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SPStatus(LenientModel):
    deliveryReasons: list[SPDeliveryReason | str] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="""
This is the list of reasons behind the delivery status.

Supported values:
- `ADVERTISER_OUT_OF_BUDGET`: Indicates that an advertiser is out of budget for Sponsored Products campaigns for sellers.
- `ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT`: Indicates that a postpay advertiser is out of credit limit for all Sponsored Ads campaigns.
- `ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET`: Indicates that a postpay advertiser is out of monthly budget for all Sponsored Ads campaigns.
- `ADVERTISER_OUT_OF_PREPAY_BALANCE`: Indicates that a prepay advertiser is out of prepay balance for all Sponsored Ads campaigns.
""",
    )
    deliveryStatus: SPDeliveryStatus | str = Field(description="""
Supported values:
- `DELIVERING`: Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
- `NOT_DELIVERING`: Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
- `UNAVAILABLE`: Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces
""")


class SPTag(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


__all__ = [
    "SPAdProduct",
    "SPCreateState",
    "SPCreateTag",
    "SPCurrencyCode",
    "SPDeliveryReason",
    "SPDeliveryStatus",
    "SPError",
    "SPErrorCode",
    "SPErrorsIndex",
    "SPMarketplaceScope",
    "SPProductIdType",
    "SPState",
    "SPStatus",
    "SPTag",
    "SPUpdateState",
]
