"""Auto-generated Pydantic models from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict

# ── Enums ──
class ErrorCode(StrEnum):
    """| ErrorCode | Description |
|------|------|
| `ACTION_NOT_SUPPORTED` | The request is not supported. |
| `ACTIVE_RESOURCE_LIMIT_EXCEEDED` | Too many live resources. Remove resources and try again. |
| `ARCHIVED_PARENT_CANNOT_CREATE` | New resources cannot be created within an archived parent. |
| `ARCHIVED_PARENT_CANNOT_EDIT` | Resources within an archived parent cannot be edited. |
| `ARCHIVED_RESOURCE_CANNOT_EDIT` | Archived resources cannot be edited. |
| `AUTOCREATED_ENTITY_CANNOT_EDIT` | Autocreated entities cannot be edited. To complete this action, create the resource manually. |
| `BAD_REQUEST` | The request is not valid considering the documented schema. |
| `CONFLICT` | Operation could not be completed due to a conflict. Please retry your request. |
| `CONTENT_TOO_LARGE` | The request is too large. Consider splitting it into multiple requests. |
| `DATE_CANNOT_BE_IN_PAST` | Update the date to be in the future. |
| `DATE_CANNOT_BE_NULL` | Update the date. |
| `DATE_TOO_SOON` | Update the date to be further in the future. |
| `DUPLICATE_FIELD_VALUE_FOUND` | Multiple resources share the non-unique field values. Remove the non-unique field value. |
| `DUPLICATE_RESOURCE_ID_FOUND` | Multiple resources share the same ID. Remove the duplicate ID. |
| `DURATION_TOO_SHORT` | Update the length to be within the required range. |
| `FEATURE_DISCONTINUED` | Feature has been discontinued. |
| `FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT` | Update the value to be within the required range. |
| `FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT` | Update the value to be within the required range. |
| `FIELD_SIZE_IS_OUT_OF_RANGE` | Update the value to be within the required range. |
| `FIELD_VALUE_CANNOT_EDIT` | Field value cannot be edited. |
| `FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS` | Update the request with the required information for this resource. |
| `FIELD_VALUE_CONTAINS_INVALID_CHARACTERS` | Remove the invalid characters and try again. |
| `FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT` | Update the value to be within the required range. |
| `FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT` | Update the value to be within the required range. |
| `FIELD_VALUE_IS_EMPTY` | Update the request with the required information for this resource. |
| `FIELD_VALUE_IS_INVALID` | Update the request with the required information for this resource. |
| `FIELD_VALUE_IS_NULL` | Update the request with the required information for this resource. |
| `FIELD_VALUE_IS_OUT_OF_RANGE` | Update the value to be within the required range. |
| `FIELD_VALUE_MISMATCH` | Mismatch among resource field values. |
| `FIELD_VALUE_MUST_BE_EMPTY_OR_NULL` | Update the request with the required information for this resource. |
| `FIELD_VALUE_NOT_FOUND` | Resource specified in the field value not found. Try again with valid value. |
| `FIELD_VALUE_NOT_UNIQUE` | Resource field value conflicts with existing resource. Try again with an unique field value. |
| `FORBIDDEN` | The caller is not authorized to make the given request. |
| `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO` | The campaign is associated with a global campaign. Portfolio association cannot be updated on a child campaign. Please perform operation on the global campaign. |
| `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE` | The campaign is associated with a global campaign. The state on child campaign cannot be set to archived. Please perform operation on global campaign. |
| `GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT` | The campaign is associated with a global campaign. Only one ad group can be created under this campaign. |
| `INTERNAL_ERROR` | The server encountered an unexpected condition that prevented it from fulfilling the request. |
| `NOT_FOUND` | The requested resource does not exist. |
| `PAYMENT_ISSUE` | Payment failed. |
| `PRODUCT_INELIGIBLE` | Product is not eligible for advertising. Try again with a valid product. |
| `RESOURCE_DOES_NOT_BELONG_TO_PARENT` | Resource does not belong to the specified parent. Try again with a valid parent ID. |
| `RESOURCE_ID_NOT_FOUND` | Resource ID not found. Try again with valid ID. |
| `RESOURCE_IS_EMPTY` | Update the request with the required information for this resource. |
| `RESOURCE_IS_IN_TERMINAL_STATE` | Resource is in terminal state. |
| `RESOURCE_IS_NULL` | Update the request with the required information for this resource. |
| `TOO_MANY_REQUESTS` | There have been too many requests, please slow down your call rate. |
| `TOTAL_RESOURCE_LIMIT_EXCEEDED` | Too many resources. Remove resources and try again. |
| `UNAUTHORIZED` | The request lacks the necessary credentials. |
| `UNSUPPORTED_MARKETPLACE` | Marketplace not supported. Try again with a supported marketplace. |
"""
    ACTION_NOT_SUPPORTED = "ACTION_NOT_SUPPORTED"
    ACTIVE_RESOURCE_LIMIT_EXCEEDED = "ACTIVE_RESOURCE_LIMIT_EXCEEDED"
    ARCHIVED_PARENT_CANNOT_CREATE = "ARCHIVED_PARENT_CANNOT_CREATE"
    ARCHIVED_PARENT_CANNOT_EDIT = "ARCHIVED_PARENT_CANNOT_EDIT"
    ARCHIVED_RESOURCE_CANNOT_EDIT = "ARCHIVED_RESOURCE_CANNOT_EDIT"
    AUTOCREATED_ENTITY_CANNOT_EDIT = "AUTOCREATED_ENTITY_CANNOT_EDIT"
    BAD_REQUEST = "BAD_REQUEST"
    CONFLICT = "CONFLICT"
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"
    DATE_CANNOT_BE_IN_PAST = "DATE_CANNOT_BE_IN_PAST"
    DATE_CANNOT_BE_NULL = "DATE_CANNOT_BE_NULL"
    DATE_TOO_SOON = "DATE_TOO_SOON"
    DUPLICATE_FIELD_VALUE_FOUND = "DUPLICATE_FIELD_VALUE_FOUND"
    DUPLICATE_RESOURCE_ID_FOUND = "DUPLICATE_RESOURCE_ID_FOUND"
    DURATION_TOO_SHORT = "DURATION_TOO_SHORT"
    FEATURE_DISCONTINUED = "FEATURE_DISCONTINUED"
    FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT = "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT"
    FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT = "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT"
    FIELD_SIZE_IS_OUT_OF_RANGE = "FIELD_SIZE_IS_OUT_OF_RANGE"
    FIELD_VALUE_CANNOT_EDIT = "FIELD_VALUE_CANNOT_EDIT"
    FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS = "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS"
    FIELD_VALUE_CONTAINS_INVALID_CHARACTERS = "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS"
    FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT = "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT"
    FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT = "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT"
    FIELD_VALUE_IS_EMPTY = "FIELD_VALUE_IS_EMPTY"
    FIELD_VALUE_IS_INVALID = "FIELD_VALUE_IS_INVALID"
    FIELD_VALUE_IS_NULL = "FIELD_VALUE_IS_NULL"
    FIELD_VALUE_IS_OUT_OF_RANGE = "FIELD_VALUE_IS_OUT_OF_RANGE"
    FIELD_VALUE_MISMATCH = "FIELD_VALUE_MISMATCH"
    FIELD_VALUE_MUST_BE_EMPTY_OR_NULL = "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL"
    FIELD_VALUE_NOT_FOUND = "FIELD_VALUE_NOT_FOUND"
    FIELD_VALUE_NOT_UNIQUE = "FIELD_VALUE_NOT_UNIQUE"
    FORBIDDEN = "FORBIDDEN"
    GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO = "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO"
    GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE = "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE"
    GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT = "GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    NOT_FOUND = "NOT_FOUND"
    PAYMENT_ISSUE = "PAYMENT_ISSUE"
    PRODUCT_INELIGIBLE = "PRODUCT_INELIGIBLE"
    RESOURCE_DOES_NOT_BELONG_TO_PARENT = "RESOURCE_DOES_NOT_BELONG_TO_PARENT"
    RESOURCE_ID_NOT_FOUND = "RESOURCE_ID_NOT_FOUND"
    RESOURCE_IS_EMPTY = "RESOURCE_IS_EMPTY"
    RESOURCE_IS_IN_TERMINAL_STATE = "RESOURCE_IS_IN_TERMINAL_STATE"
    RESOURCE_IS_NULL = "RESOURCE_IS_NULL"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
    TOTAL_RESOURCE_LIMIT_EXCEEDED = "TOTAL_RESOURCE_LIMIT_EXCEEDED"
    UNAUTHORIZED = "UNAUTHORIZED"
    UNSUPPORTED_MARKETPLACE = "UNSUPPORTED_MARKETPLACE"

class SPAdExtensionStatus(StrEnum):
    """Ad Extension Status.

| AdExtensionStatus | Description |
|------|------|
| `OPTED_OUT` | If the advertiser has opted out of this Ad Extension. |
"""
    OPTED_OUT = "OPTED_OUT"

class SPAdExtensionType(StrEnum):
    """Ad Extension Type.

| AdExtensionType | Description |
|------|------|
| `PROMPTS` | Enables Prompt based Ad Extension. |
| `VIDEO` | Enables Video based Ad Extension. |
"""
    PROMPTS = "PROMPTS"
    VIDEO = "VIDEO"

class SPAdGroupNameFilterType(StrEnum):
    """| AdGroupNameFilterType | Description |
| --- | --- |
| `EXACT_MATCH` | Filter by exact match. |
| `BROAD_MATCH` | Filter by broad match. |"""
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"

class SPAdProduct(StrEnum):
    """| AdProduct | Description |
|------|------|
| `SPONSORED_PRODUCTS` | Sponsored Products ad product. |
"""
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"

class SPAdType(StrEnum):
    """| AdType | Description |
|------|------|
| `PRODUCT_AD` | A creative built based on a specified product. |
"""
    PRODUCT_AD = "PRODUCT_AD"

class SPAutoScaleGlobalCampaignSetting(StrEnum):
    """| AutoScaleGlobalCampaignSetting | Description |
|------|------|
| `AUTO` | Auto scale global campaign to new marketplaces |
| `MANUAL` | Manually scale global campaign to new marketplaces |
"""
    AUTO = "AUTO"
    MANUAL = "MANUAL"

class SPBidStrategy(StrEnum):
    """| BidStrategy | Description |
|------|------|
| `MANUAL` | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding. |
| `RULE_BASED` | Applies bidding rules defined by the advertiser. |
| `SALES_DOWN_ONLY` | Decreases your bids in real time when your ad is less likely to convert to a sale. Bids will never increase beyond your set bid. |
| `SALES_UP_AND_DOWN` | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale. |
"""
    MANUAL = "MANUAL"
    RULE_BASED = "RULE_BASED"
    SALES_DOWN_ONLY = "SALES_DOWN_ONLY"
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"

class SPBudgetType(StrEnum):
    """| BudgetType | Description |
|------|------|
| `MONETARY` |  |
"""
    MONETARY = "MONETARY"

class SPCampaignNameFilterType(StrEnum):
    """| CampaignNameFilterType | Description |
| --- | --- |
| `EXACT_MATCH` | Filter by exact match. |
| `BROAD_MATCH` | Filter by broad match. |"""
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"

class SPCountryCode(StrEnum):
    """| CountryCode | Description |
|------|------|
| `AE` |  |
| `AU` |  |
| `BE` |  |
| `BR` |  |
| `CA` |  |
| `DE` |  |
| `EG` |  |
| `ES` |  |
| `FR` |  |
| `GB` |  |
| `IE` |  |
| `IN` |  |
| `IT` |  |
| `JP` |  |
| `MX` |  |
| `NL` |  |
| `PL` |  |
| `SA` |  |
| `SE` |  |
| `SG` |  |
| `TR` |  |
| `US` |  |
| `ZA` |  |
"""
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IE = "IE"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"
    ZA = "ZA"

class SPCreateState(StrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

| CreateState | Description |
|------|------|
| `ENABLED` | The object is set active by user and eligible for delivery. |
| `PAUSED` | The object is stopped by user and not eligible for delivery. |
"""
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"

class SPCreativeBidAdjustmentType(StrEnum):
    """| CreativeBidAdjustmentType | Description |
|------|------|
| `SPOTLIGHT` | SPOTLIGHT Video Asset. |
"""
    SPOTLIGHT = "SPOTLIGHT"

class SPCurrencyCode(StrEnum):
    """| CurrencyCode | Description |
|------|------|
| `AED` | United Arab Emirates Dirham |
| `AUD` | Australian Dollar |
| `BRL` | Brazilian Real |
| `CAD` | Canadian Dollar |
| `CHF` | Swiss Franc |
| `CNY` | Chinese Yuan |
| `DKK` | Danish Krone |
| `EGP` | Egyptian Pound |
| `EUR` | Euro |
| `GBP` | British Pound Sterling |
| `INR` | Indian Rupee |
| `JPY` | Japanese Yen |
| `MXN` | Mexican Peso |
| `MXP` | Mexican Peso |
| `NGN` | Nigerian Naira |
| `NOK` | Norwegian Krone |
| `NZD` | New Zealand Dollar |
| `PLN` | Polish Złoty |
| `SAR` | Saudi Riyal |
| `SEK` | Swedish Krona |
| `SGD` | Singapore Dollar |
| `TRY` | Turkish Lira |
| `USD` | United States Dollar |
| `ZAR` | South African Rand |
"""
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CNY = "CNY"
    DKK = "DKK"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    MXP = "MXP"
    NGN = "NGN"
    NOK = "NOK"
    NZD = "NZD"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"

class SPDeliveryReason(StrEnum):
    """| DeliveryReason | Description |
|------|------|
| `ADVERTISER_ARCHIVED` |  |
| `ADVERTISER_OUT_OF_BUDGET` | Indicates that an advertiser is out of budget for Sponsored Products campaigns for sellers. |
| `ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT` | Indicates that a postpay advertiser is out of credit limit for all Sponsored Ads campaigns. |
| `ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET` | Indicates that a postpay advertiser is out of monthly budget for all Sponsored Ads campaigns. |
| `ADVERTISER_OUT_OF_PREPAY_BALANCE` | Indicates that a prepay advertiser is out of prepay balance for all Sponsored Ads campaigns. |
| `ADVERTISER_PAUSED` |  |
| `ADVERTISER_PAYMENT_FAILURE` |  |
| `ADVERTISER_POLICING_PENDING_REVIEW` |  |
| `ADVERTISER_POLICING_SUSPENDED` |  |
| `AD_ARCHIVED` |  |
| `AD_CREATION_FAILED` |  |
| `AD_CREATION_IN_PROGRESS` |  |
| `AD_EXTENSION_ARCHIVED` |  |
| `AD_EXTENSION_PAUSED` |  |
| `AD_EXTENSION_POLICING_PENDING_REVIEW` |  |
| `AD_EXTENSION_POLICING_SUSPENDED` |  |
| `AD_GROUP_ARCHIVED` |  |
| `AD_GROUP_INCOMPLETE` |  |
| `AD_GROUP_LOW_BID` |  |
| `AD_GROUP_PAUSED` |  |
| `AD_GROUP_PENDING_REVIEW` |  |
| `AD_GROUP_POLICING_PENDING_REVIEW` |  |
| `AD_GROUP_REJECTED` |  |
| `AD_INELIGIBLE` |  |
| `AD_MISSING_DECORATION` |  |
| `AD_MISSING_IMAGE` |  |
| `AD_NOT_DELIVERING` |  |
| `AD_PAUSED` |  |
| `AD_POLICING_PENDING_REVIEW` |  |
| `AD_POLICING_SUSPENDED` |  |
| `BRAND_INELIGIBLE` |  |
| `CAMPAIGN_ARCHIVED` |  |
| `CAMPAIGN_END_DATE_REACHED` |  |
| `CAMPAIGN_INCOMPLETE` |  |
| `CAMPAIGN_OUT_OF_BUDGET` |  |
| `CAMPAIGN_PAUSED` |  |
| `CAMPAIGN_PENDING_REVIEW` |  |
| `CAMPAIGN_PENDING_START_DATE` |  |
| `CAMPAIGN_REJECTED` |  |
| `CREATIVE_MISSING_ASSET` |  |
| `CREATIVE_PENDING_REVIEW` |  |
| `CREATIVE_REJECTED` |  |
| `LANDING_PAGE_INELIGIBLE` |  |
| `LANDING_PAGE_NOT_AVAILABLE` |  |
| `MODERATION_ADULT_NOVELTY_POLICY_VIOLATION` |  |
| `MODERATION_ADULT_PRODUCT_POLICY_VIOLATION` |  |
| `MODERATION_ADULT_SOFTLINES_POLICY_VIOLATION` |  |
| `MODERATION_CLAIM_WEIGHTLOSS_POLICY_VIOLATION` |  |
| `MODERATION_CONTENT_NUDITY_POLICY_VIOLATION` |  |
| `MODERATION_CONTENT_PROVOCATIVE_POLICY_VIOLATION` |  |
| `MODERATION_CONTENT_SMOKING_POLICY_VIOLATION` |  |
| `MODERATION_CRITICAL_EVENTS_POLICY_VIOLATION` |  |
| `MODERATION_ERROR_404` |  |
| `MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION` |  |
| `MODERATION_HFSS_PRODUCT_POLICY_VIOLATION` |  |
| `MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION` |  |
| `MODERATION_NOT_COMPLIANT_TO_AD_POLICY` |  |
| `MODERATION_SMOKING_RELATED_POLICY_VIOLATION` |  |
| `NOT_BUYABLE` |  |
| `NOT_IN_BUYBOX` |  |
| `NOT_IN_POLICY` |  |
| `NO_INVENTORY` |  |
| `NO_PURCHASABLE_OFFER` |  |
| `OTHER` |  |
| `OUT_OF_REWARD_BUDGET` |  |
| `OUT_OF_STOCK` |  |
| `PIR_RULE_EXCLUDED` |  |
| `PORTFOLIO_ARCHIVED` |  |
| `PORTFOLIO_END_DATE_REACHED` |  |
| `PORTFOLIO_OUT_OF_BUDGET` |  |
| `PORTFOLIO_PAUSED` |  |
| `PORTFOLIO_PENDING_START_DATE` |  |
| `SECURITY_SCAN_PENDING_REVIEW` |  |
| `SECURITY_SCAN_REJECTED` |  |
| `SPEND_LIMIT_EXCEEDED` |  |
| `STATUS_UNAVAILABLE` |  |
| `TARGET_ARCHIVED` |  |
| `TARGET_BLOCKED` |  |
| `TARGET_PAUSED` |  |
| `TARGET_POLICING_SUSPENDED` |  |
"""
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT = "ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT"
    ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET = "ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    AD_ARCHIVED = "AD_ARCHIVED"
    AD_CREATION_FAILED = "AD_CREATION_FAILED"
    AD_CREATION_IN_PROGRESS = "AD_CREATION_IN_PROGRESS"
    AD_EXTENSION_ARCHIVED = "AD_EXTENSION_ARCHIVED"
    AD_EXTENSION_PAUSED = "AD_EXTENSION_PAUSED"
    AD_EXTENSION_POLICING_PENDING_REVIEW = "AD_EXTENSION_POLICING_PENDING_REVIEW"
    AD_EXTENSION_POLICING_SUSPENDED = "AD_EXTENSION_POLICING_SUSPENDED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_PENDING_REVIEW = "AD_GROUP_PENDING_REVIEW"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_REJECTED = "AD_GROUP_REJECTED"
    AD_INELIGIBLE = "AD_INELIGIBLE"
    AD_MISSING_DECORATION = "AD_MISSING_DECORATION"
    AD_MISSING_IMAGE = "AD_MISSING_IMAGE"
    AD_NOT_DELIVERING = "AD_NOT_DELIVERING"
    AD_PAUSED = "AD_PAUSED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    BRAND_INELIGIBLE = "BRAND_INELIGIBLE"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_END_DATE_REACHED = "CAMPAIGN_END_DATE_REACHED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_REVIEW = "CAMPAIGN_PENDING_REVIEW"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    CAMPAIGN_REJECTED = "CAMPAIGN_REJECTED"
    CREATIVE_MISSING_ASSET = "CREATIVE_MISSING_ASSET"
    CREATIVE_PENDING_REVIEW = "CREATIVE_PENDING_REVIEW"
    CREATIVE_REJECTED = "CREATIVE_REJECTED"
    LANDING_PAGE_INELIGIBLE = "LANDING_PAGE_INELIGIBLE"
    LANDING_PAGE_NOT_AVAILABLE = "LANDING_PAGE_NOT_AVAILABLE"
    MODERATION_ADULT_NOVELTY_POLICY_VIOLATION = "MODERATION_ADULT_NOVELTY_POLICY_VIOLATION"
    MODERATION_ADULT_PRODUCT_POLICY_VIOLATION = "MODERATION_ADULT_PRODUCT_POLICY_VIOLATION"
    MODERATION_ADULT_SOFTLINES_POLICY_VIOLATION = "MODERATION_ADULT_SOFTLINES_POLICY_VIOLATION"
    MODERATION_CLAIM_WEIGHTLOSS_POLICY_VIOLATION = "MODERATION_CLAIM_WEIGHTLOSS_POLICY_VIOLATION"
    MODERATION_CONTENT_NUDITY_POLICY_VIOLATION = "MODERATION_CONTENT_NUDITY_POLICY_VIOLATION"
    MODERATION_CONTENT_PROVOCATIVE_POLICY_VIOLATION = "MODERATION_CONTENT_PROVOCATIVE_POLICY_VIOLATION"
    MODERATION_CONTENT_SMOKING_POLICY_VIOLATION = "MODERATION_CONTENT_SMOKING_POLICY_VIOLATION"
    MODERATION_CRITICAL_EVENTS_POLICY_VIOLATION = "MODERATION_CRITICAL_EVENTS_POLICY_VIOLATION"
    MODERATION_ERROR_404 = "MODERATION_ERROR_404"
    MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION = "MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION"
    MODERATION_HFSS_PRODUCT_POLICY_VIOLATION = "MODERATION_HFSS_PRODUCT_POLICY_VIOLATION"
    MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION = "MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION"
    MODERATION_NOT_COMPLIANT_TO_AD_POLICY = "MODERATION_NOT_COMPLIANT_TO_AD_POLICY"
    MODERATION_SMOKING_RELATED_POLICY_VIOLATION = "MODERATION_SMOKING_RELATED_POLICY_VIOLATION"
    NOT_BUYABLE = "NOT_BUYABLE"
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"
    NOT_IN_POLICY = "NOT_IN_POLICY"
    NO_INVENTORY = "NO_INVENTORY"
    NO_PURCHASABLE_OFFER = "NO_PURCHASABLE_OFFER"
    OTHER = "OTHER"
    OUT_OF_REWARD_BUDGET = "OUT_OF_REWARD_BUDGET"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PIR_RULE_EXCLUDED = "PIR_RULE_EXCLUDED"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_END_DATE_REACHED = "PORTFOLIO_END_DATE_REACHED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    SECURITY_SCAN_PENDING_REVIEW = "SECURITY_SCAN_PENDING_REVIEW"
    SECURITY_SCAN_REJECTED = "SECURITY_SCAN_REJECTED"
    SPEND_LIMIT_EXCEEDED = "SPEND_LIMIT_EXCEEDED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    TARGET_ARCHIVED = "TARGET_ARCHIVED"
    TARGET_BLOCKED = "TARGET_BLOCKED"
    TARGET_PAUSED = "TARGET_PAUSED"
    TARGET_POLICING_SUSPENDED = "TARGET_POLICING_SUSPENDED"

class SPDeliveryStatus(StrEnum):
    """| DeliveryStatus | Description |
|------|------|
| `DELIVERING` | Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces |
| `NOT_DELIVERING` | Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces |
| `UNAVAILABLE` | Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces |
"""
    DELIVERING = "DELIVERING"
    NOT_DELIVERING = "NOT_DELIVERING"
    UNAVAILABLE = "UNAVAILABLE"

class SPKeywordMatchType(StrEnum):
    """| KeywordMatchType | Description |
|------|------|
| `BROAD` | Broad match search terms. This expands matching on user intent beyond PHRASE. |
| `EXACT` | Exact match search terms. |
| `PHRASE` | Phrase match search terms. This expands matching on user intent beyond EXACT. |
"""
    BROAD = "BROAD"
    EXACT = "EXACT"
    PHRASE = "PHRASE"

class SPLanguageLocale(StrEnum):
    """A combination of ISO-639 standard for language code and ISO-3166 for country code.

| LanguageLocale | Description |
|------|------|
| `zh_CN` | Chinese (China). |
"""
    zh_CN = "zh_CN"

class SPMarketplace(StrEnum):
    """A list of country codes representing Amazon marketplaces

| Marketplace | Description |
|------|------|
| `AE` |  |
| `AU` |  |
| `BE` |  |
| `BR` |  |
| `CA` |  |
| `DE` |  |
| `EG` |  |
| `ES` |  |
| `FR` |  |
| `GB` |  |
| `IE` |  |
| `IN` |  |
| `IT` |  |
| `JP` |  |
| `MX` |  |
| `NL` |  |
| `PL` |  |
| `SA` |  |
| `SE` |  |
| `SG` |  |
| `TR` |  |
| `US` |  |
| `ZA` |  |
"""
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IE = "IE"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"
    ZA = "ZA"

class SPMarketplaceBudgetAllocation(StrEnum):
    """| MarketplaceBudgetAllocation | Description |
|------|------|
| `AUTO` | Auto distribute global budget to marketplaces in global campaign |
| `MANUAL` | Manually distribute global budget to marketplaces in global campaign |
"""
    AUTO = "AUTO"
    MANUAL = "MANUAL"

class SPMarketplaceScope(StrEnum):
    """| MarketplaceScope | Description |
|------|------|
| `SINGLE_MARKETPLACE` |  |
"""
    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"

class SPMatchType(StrEnum):
    """| MatchType | Description |
| --- | --- |
| `KEYWORDS_RELATED_TO_GIFTS` | Search terms related to gifts. |
| `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY` | Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically. |
| `PRODUCT_SIMILAR` | Products similar to the specified product. |
| `BROAD` | Broad match search terms. This expands matching on user intent beyond PHRASE.  |
| `EXACT` | Exact match search terms. |
| `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY` | Search terms shoppers often use to search for products in the same category as the products you're advertising. |
| `KEYWORDS_RELATED_TO_YOUR_BRAND` | Search terms related to your brand. |
| `PRODUCT_SUBSTITUTES` | Products that can be substituted for advertised product. |
| `KEYWORDS_LOOSE_MATCH` | Search terms loosely matching advertised product. |
| `PHRASE` | Phrase match search terms. This expands matching on user intent beyond EXACT. |
| `KEYWORDS_CLOSE_MATCH` | Search terms closely matching advertised product. |
| `PRODUCT_COMPLEMENTS` | Products that complement advertised product. |
| `PRODUCT_EXACT` | Products exactly matching the specified product. |
| `KEYWORDS_RELATED_TO_PRIME_DAY` | Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day. |"""
    BROAD = "BROAD"
    EXACT = "EXACT"
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"
    KEYWORDS_RELATED_TO_GIFTS = "KEYWORDS_RELATED_TO_GIFTS"
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"
    KEYWORDS_RELATED_TO_PRIME_DAY = "KEYWORDS_RELATED_TO_PRIME_DAY"
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"
    PHRASE = "PHRASE"
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"
    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"

class SPOffAmazonBudgetControlStrategy(StrEnum):
    """| OffAmazonBudgetControlStrategy | Description |
|------|------|
| `MAXIMIZE_REACH` | Maximize the reach of off-Amazon inventory within the budget. |
| `MINIMIZE_SPEND` | Minimize spend on off-Amazon inventory while maintaining delivery. |
"""
    MAXIMIZE_REACH = "MAXIMIZE_REACH"
    MINIMIZE_SPEND = "MINIMIZE_SPEND"

class SPPlacement(StrEnum):
    """| Placement | Description |
|------|------|
| `PRODUCT_PAGE` | Placements on the product detail page, and all nonsearch placements such as the add-to-cart page. |
| `REST_OF_SEARCH` | Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond. |
| `SITE_AMAZON_BUSINESS` | Amazon Business site placements. |
| `TOP_OF_SEARCH` | Placements on the top row of the first-page search results. |
"""
    PRODUCT_PAGE = "PRODUCT_PAGE"
    REST_OF_SEARCH = "REST_OF_SEARCH"
    SITE_AMAZON_BUSINESS = "SITE_AMAZON_BUSINESS"
    TOP_OF_SEARCH = "TOP_OF_SEARCH"

class SPProductIdType(StrEnum):
    """| ProductIdType | Description |
|------|------|
| `ASIN` | ASIN identifier type. |
| `SKU` | SKU identifier type. |
"""
    ASIN = "ASIN"
    SKU = "SKU"

class SPProductMatchType(StrEnum):
    """| ProductMatchType | Description |
|------|------|
| `PRODUCT_EXACT` | Products exactly matching the specified product. |
| `PRODUCT_SIMILAR` | Products similar to the specified product. |
"""
    PRODUCT_EXACT = "PRODUCT_EXACT"
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"

class SPRecurrence(StrEnum):
    """| Recurrence | Description |
|------|------|
| `DAILY` |  |
"""
    DAILY = "DAILY"

class SPSiteRestriction(StrEnum):
    """| SiteRestriction | Description |
|------|------|
| `AMAZON_BUSINESS` | Restrict the ad to only show on Amazon Business. |
| `AMAZON_HAUL` | Restrict the ad to only show on Amazon Haul. |
"""
    AMAZON_BUSINESS = "AMAZON_BUSINESS"
    AMAZON_HAUL = "AMAZON_HAUL"

class SPState(StrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

| State | Description |
|------|------|
| `ARCHIVED` | The object is permanently stopped and cannot be reactivated. Terminal end state. |
| `ENABLED` | The object is set active by user and eligible for delivery. |
| `PAUSED` | The object is stopped by user and not eligible for delivery. |
"""
    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"

class SPTargetKeywordFilterType(StrEnum):
    """| TargetKeywordFilterType | Description |
| --- | --- |
| `EXACT_MATCH` | Filter by exact match. |
| `BROAD_MATCH` | Filter by broad match. |"""
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"

class SPTargetLevel(StrEnum):
    """| TargetLevel | Description |
|------|------|
| `AD_GROUP` | Target applied at the ad group level. |
| `CAMPAIGN` | Target applied at the campaign level. |
"""
    AD_GROUP = "AD_GROUP"
    CAMPAIGN = "CAMPAIGN"

class SPTargetProductIdFilterType(StrEnum):
    """| TargetProductIdFilterType | Description |
| --- | --- |
| `EXACT_MATCH` | Filter by exact match. |
| `BROAD_MATCH` | Filter by broad match. |"""
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"

class SPTargetType(StrEnum):
    """| TargetType | Description |
|------|------|
| `KEYWORD` | Target based on customer search terms. |
| `LOCATION` | Target based on geographic location. |
| `PRODUCT_CATEGORY` | Target based on a product category. |
| `PRODUCT` | Target based on a specific product. |
| `THEME` | Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products. |
"""
    KEYWORD = "KEYWORD"
    LOCATION = "LOCATION"
    PRODUCT = "PRODUCT"
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"
    THEME = "THEME"

class SPThemeMatchType(StrEnum):
    """| ThemeMatchType | Description |
|------|------|
| `KEYWORDS_CLOSE_MATCH` | Search terms closely matching advertised product. |
| `KEYWORDS_LOOSE_MATCH` | Search terms loosely matching advertised product. |
| `KEYWORDS_RELATED_TO_GIFTS` | Search terms related to gifts. |
| `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY` | Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically. |
| `KEYWORDS_RELATED_TO_PRIME_DAY` | Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day. |
| `KEYWORDS_RELATED_TO_YOUR_BRAND` | Search terms related to your brand. |
| `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY` | Search terms shoppers often use to search for products in the same category as the products you're advertising. |
| `PRODUCT_COMPLEMENTS` | Products that complement advertised product. |
| `PRODUCT_SUBSTITUTES` | Products that can be substituted for advertised product. |
"""
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"
    KEYWORDS_RELATED_TO_GIFTS = "KEYWORDS_RELATED_TO_GIFTS"
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"
    KEYWORDS_RELATED_TO_PRIME_DAY = "KEYWORDS_RELATED_TO_PRIME_DAY"
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"

class SPUpdateState(StrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

| UpdateState | Description |
|------|------|
| `ENABLED` | The object is set active by user and eligible for delivery. |
| `PAUSED` | The object is stopped by user and not eligible for delivery. |
"""
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"

class SPVideoType(StrEnum):
    """Video Type: Video type of the asset added in the ad extension and its rendering form.

| VideoType | Description |
|------|------|
| `SPOTLIGHT` | SPOTLIGHT Video Asset. |
"""
    SPOTLIGHT = "SPOTLIGHT"


# ── Filters ──
class SPAdAdGroupIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPAdAdIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPAdAdProductFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.

class SPAdCampaignIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPAdExtensionAdExtensionIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPAdExtensionAdExtensionStatusFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # AdExtensionStatus Description `OPTED_OUT` If the advertiser has opted out of thi

class SPAdExtensionAdExtensionTypeFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # AdExtensionType Description `PROMPTS` Enables Prompt based Ad Extension. `VIDEO`

class SPAdExtensionAdGroupIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPAdExtensionAdIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPAdExtensionAdProductFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.

class SPAdExtensionStateFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # State Description `ENABLED` The object is set active by user and eligible for de

class SPAdGroupAdGroupIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPAdGroupAdProductFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.

class SPAdGroupCampaignIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPAdGroupNameFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: dict[str, Any]

class SPAdGroupStateFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # State Description `ENABLED` The object is set active by user and eligible for de

class SPAdStateFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # State Description `ENABLED` The object is set active by user and eligible for de

class SPCampaignAdProductFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.

class SPCampaignCampaignIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPCampaignNameFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: dict[str, Any]

class SPCampaignPortfolioIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPCampaignStateFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # State Description `ENABLED` The object is set active by user and eligible for de

class SPTargetAdGroupIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPTargetAdProductFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.

class SPTargetCampaignIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPTargetKeywordFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: dict[str, Any]

class SPTargetMatchTypeFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # MatchType Description `KEYWORDS_RELATED_TO_GIFTS` Search terms related to gifts.

class SPTargetNegativeFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[bool]

class SPTargetProductIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: dict[str, Any]

class SPTargetStateFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # State Description `ENABLED` The object is set active by user and eligible for de

class SPTargetTargetIdFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[str]

class SPTargetTargetTypeFilter(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    include: list[dict[str, Any]]  # TargetType Description `KEYWORD` Target based on customer search terms. `PRODUCT


# ── Entity Models ──
class SPAd(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adId: str  # The identifier of the ad.
    adProduct: dict[str, Any]
    adType: dict[str, Any]
    campaignId: str  # The campaign associated with the ad. It's a read-only field.
    creationDateTime: datetime  # The date time that the ad was created.
    creative: dict[str, Any]
    globalAdId: str | None = None  # The global ad identifier that manages this marketplace ad.
    lastUpdatedDateTime: datetime  # The date time that the ad was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]]  # The list of country codes representing amazon marketplaces in which the global a
    state: dict[str, Any]
    status: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the ad

class SPAdCreate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adProduct: dict[str, Any]
    adType: dict[str, Any]
    creative: dict[str, Any]
    state: dict[str, Any]
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the ad

class SPAdExtension(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    adExtensionSettings: dict[str, Any]
    adExtensionStatus: dict[str, Any] | None = None
    adExtensionType: dict[str, Any]
    adGroupId: str | None = None  # A unique identifier for the ad group associated with the ad_extension.
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: dict[str, Any]
    creationDateTime: datetime  # The date time the ad_extension was created.
    lastUpdatedDateTime: datetime  # The date time the ad_extension was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]]  # The list of marketplace in which the global ad_extension is applicable. The mark
    state: dict[str, Any]
    status: dict[str, Any] | None = None

class SPAdExtensionCreate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adExtensionSettings: dict[str, Any]
    adExtensionStatus: dict[str, Any] | None = None
    adExtensionType: dict[str, Any]
    adGroupId: str | None = None  # A unique identifier for the ad group associated with the ad_extension.
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: dict[str, Any]
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]]  # The list of marketplace in which the global ad_extension is applicable. The mark
    state: dict[str, Any]

class SPAdExtensionMultiStatusSuccess(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adExtension: dict[str, Any]
    index: int

class SPAdExtensionSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

class SPAdExtensionUpdate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    state: dict[str, Any] | None = None

class SPAdGroup(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    adProduct: dict[str, Any]
    bid: dict[str, Any]
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    creationDateTime: datetime  # The date time that the ad group was created.
    globalAdGroupId: str | None = None  # The global adGroup identifier that manages this marketplace adGroup.
    lastUpdatedDateTime: datetime  # The date time that the ad group was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]]  # The list of country codes representing amazon marketplaces in which the global a
    name: str  # The name of the ad group.
    state: dict[str, Any]
    status: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the ad group

class SPAdGroupBid(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    currencyCode: dict[str, Any]
    defaultBid: float  # The default maximum bid for ads and targets in the ad group. This is used in spo

class SPAdGroupCreate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adProduct: dict[str, Any]
    bid: dict[str, Any]
    campaignId: str  # The unique identifier of the campaign the ad group belongs to.
    name: str  # The name of the ad group.
    state: dict[str, Any]
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the ad group

class SPAdGroupMultiStatusSuccess(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroup: dict[str, Any]
    index: int

class SPAdGroupUpdate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The unique identifier of the ad group.
    bid: dict[str, Any] | None = None
    name: str | None = None  # The name of the ad group.
    state: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the ad group

class SPAdMultiStatusSuccess(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    ad: dict[str, Any]
    index: int

class SPAdUpdate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adId: str  # The identifier of the ad.
    creative: dict[str, Any] | None = None
    state: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the ad

class SPAdvertisedProducts(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    globalStoreSetting: dict[str, Any] | None = None
    productId: str  # The identifier of the advertised product.
    productIdType: dict[str, Any]
    resolvedProductId: str | None = None  # The identifier of product associated with the advertised product. It's a read-on
    resolvedProductIdType: dict[str, Any] | None = None

class SPAudienceBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid

class SPAutoCreationSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the camp
    autoManageCampaign: bool | None = None  # Flag that allows Amazon to manage the lifecycle of your Campaign.

class SPBidAdjustments(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on the audiences
    creativeBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment
    placementBidAdjustments: list[dict[str, Any]] | None = None  # Bid adjustments based on ad placements.

class SPBidSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: dict[str, Any] | None = None
    bidStrategy: dict[str, Any] | None = None

class SPBudget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    budgetType: dict[str, Any]
    budgetValue: dict[str, Any]
    recurrenceTimePeriod: dict[str, Any]

class SPBudgetSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    marketplaceBudgetAllocation: dict[str, Any] | None = None
    offAmazonBudgetControlStrategy: dict[str, Any] | None = None

class SPBudgetValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

class SPCampaign(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adProduct: dict[str, Any]
    autoCreationSettings: dict[str, Any]
    autoScaleGlobalCampaign: dict[str, Any] | None = None
    budgets: list[dict[str, Any]]  # The object containing budget details for the campaign (for campaigns that suppor
    campaignId: str  # A unique identifier for a campaign.
    countries: list[dict[str, Any]] | None = None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sp
    creationDateTime: datetime  # The date time that the campaign was created.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    globalCampaignId: str | None = None  # The global campaign identifier that manages this marketplace campaign.
    lastUpdatedDateTime: datetime  # The date time that the campaign was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]] | None = None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc,
    name: str  # The name of the campaign.
    optimizations: dict[str, Any] | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    siteRestrictions: list[dict[str, Any]] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime  # The start date time for the campaign.
    state: dict[str, Any]
    status: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the campaign

class SPCampaignCreate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adProduct: dict[str, Any]
    autoCreationSettings: dict[str, Any]
    budgets: list[dict[str, Any]]  # The object containing budget details for the campaign (for campaigns that suppor
    countries: list[dict[str, Any]] | None = None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sp
    endDateTime: datetime | None = None  # The end date time for the campaign.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]] | None = None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc,
    name: str  # The name of the campaign.
    optimizations: dict[str, Any] | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    siteRestrictions: list[dict[str, Any]] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime  # The start date time for the campaign.
    state: dict[str, Any]
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the campaign

class SPCampaignMultiStatusSuccess(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    campaign: dict[str, Any]
    index: int

class SPCampaignOptimizations(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidSettings: dict[str, Any] | None = None
    budgetSettings: dict[str, Any] | None = None

class SPCampaignUpdate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    budgets: list[dict[str, Any]] | None = None  # The object containing budget details for the campaign (for campaigns that suppor
    campaignId: str  # A unique identifier for a campaign.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    name: str | None = None  # The name of the campaign.
    optimizations: dict[str, Any] | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    siteRestrictions: list[dict[str, Any]] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime | None = None  # The start date time for the campaign.
    state: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the campaign

class SPCreateAdExtensionSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

class SPCreateAdGroupBid(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    defaultBid: float  # The default maximum bid for ads and targets in the ad group. This is used in spo

class SPCreateAdvertisedProducts(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    globalStoreSetting: dict[str, Any] | None = None
    productId: str  # The identifier of the advertised product.
    productIdType: dict[str, Any]

class SPCreateAudienceBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid

class SPCreateAutoCreationSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the camp
    autoManageCampaign: bool | None = None  # Flag that allows Amazon to manage the lifecycle of your Campaign.

class SPCreateBidAdjustments(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on the audiences
    creativeBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment
    placementBidAdjustments: list[dict[str, Any]] | None = None  # Bid adjustments based on ad placements.

class SPCreateBidSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: dict[str, Any] | None = None
    bidStrategy: dict[str, Any] | None = None

class SPCreateBudget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    budgetType: dict[str, Any]
    budgetValue: dict[str, Any]
    recurrenceTimePeriod: dict[str, Any]

class SPCreateBudgetSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: dict[str, Any] | None = None

class SPCreateBudgetValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

class SPCreateCampaignOptimizations(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidSettings: dict[str, Any] | None = None
    budgetSettings: dict[str, Any] | None = None

class SPCreateCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

class SPCreateCreativeBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    creativeType: dict[str, Any] | None = None
    percentage: int  # The selection of the percentage change associated with the creative type and bid

class SPCreateGlobalStoreSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: dict[str, Any] | None = None

class SPCreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""
    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target
    matchType: dict[str, Any]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: dict[str, Any] | None = None

class SPCreateLocationTarget(BaseModel):
    """Target based on geographic location."""
    model_config = ConfigDict(extra="forbid")

    locationId: str  # The ID of the geographic location to target.

class SPCreateMonetaryBudget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    value: float  # The monetary amount of the budget cap in the given currency.

class SPCreateMonetaryBudgetValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    monetaryBudget: dict[str, Any]

class SPCreatePlacementBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid
    placement: dict[str, Any]

class SPCreateProductCategoryRefinement(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productAgeRangeId: str | None = None  # The age range ID to target.
    productBrandId: str | None = None  # The brand ID to target.
    productCategoryId: str | None = None  # The product category ID to target.
    productGenreId: str | None = None  # The product genre ID to target.
    productPriceGreaterThan: float | None = None  # Refinement to target products with a price greater than the value within the pro
    productPriceLessThan: float | None = None  # Refinement to target products with a price less than the value within the produc
    productPrimeShippingEligible: bool | None = None  # Target based on if a product is Prime-shipping eligible.
    productRatingGreaterThan: float | None = None  # Refinement to target products with a rating greater than the value within the pr
    productRatingLessThan: float | None = None  # Refinement to target products with a rating less than the value within the produ

class SPCreateProductCategoryRefinementValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: dict[str, Any]

class SPCreateProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: dict[str, Any]

class SPCreateProductCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: dict[str, Any]

class SPCreateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""
    model_config = ConfigDict(extra="forbid")

    advertisedProduct: dict[str, Any]
    headline: str | None = None  # The headline/custom text associated with the ad creative.
    spotlightVideos: dict[str, Any] | None = None

class SPCreateProductTarget(BaseModel):
    """Targets a specific product."""
    model_config = ConfigDict(extra="forbid")

    matchType: dict[str, Any]
    product: dict[str, Any]
    productIdType: dict[str, Any]

class SPCreateProductValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productId: str  # The product identifier. Either the product id or the marketplace settings should

class SPCreatePromptExtension(BaseModel):
    """Prompts Ad Extension"""
    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads

class SPCreateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""
    model_config = ConfigDict(extra="forbid")

    optimizeText: bool  # If the advertiser wants text they provided to be optimized by Amazon or not.
    videos: list[dict[str, Any]]  # The video asset(s) to use for the Sponsored Product experience.

class SPCreateTag(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.

class SPCreateTargetBid(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.

class SPCreateTargetDetails(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

class SPCreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""
    model_config = ConfigDict(extra="forbid")

    matchType: dict[str, Any]

class SPCreateVideo(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.
    description: str | None = None  # The description of the video content.
    headline: str | None = None  # The headline/custom text associated with the video.

class SPCreateVideoExtension(BaseModel):
    """Video Ad Extension"""
    model_config = ConfigDict(extra="forbid")

class SPCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

class SPCreativeBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    creativeType: dict[str, Any] | None = None
    percentage: int  # The selection of the percentage change associated with the creative type and bid

class SPGlobalStoreSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: dict[str, Any] | None = None

class SPKeywordTarget(BaseModel):
    """Targets a specific customer search term."""
    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target
    matchType: dict[str, Any]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: dict[str, Any] | None = None

class SPLocationTarget(BaseModel):
    """Target based on geographic location."""
    model_config = ConfigDict(extra="forbid")

    locationId: str  # The ID of the geographic location to target.

class SPMonetaryBudget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    currencyCode: dict[str, Any]
    ruleValue: float | None = None  # The monetary amount of the budget when a budget rule is applied.
    value: float  # The monetary amount of the budget cap in the given currency.

class SPMonetaryBudgetValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    monetaryBudget: dict[str, Any]

class SPPlacementBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid
    placement: dict[str, Any]

class SPProductCategoryRefinement(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productAgeRangeId: str | None = None  # The age range ID to target.
    productAgeRangeIdResolved: str | None = None  # The resolved age range to target.
    productBrandId: str | None = None  # The brand ID to target.
    productBrandIdResolved: str | None = None  # The resolved name of the brand.
    productCategoryId: str | None = None  # The product category ID to target.
    productCategoryIdResolved: str | None = None  # The resolved product category.
    productGenreId: str | None = None  # The product genre ID to target.
    productGenreIdResolved: str | None = None  # The resolved product genre to target.
    productPriceGreaterThan: float | None = None  # Refinement to target products with a price greater than the value within the pro
    productPriceLessThan: float | None = None  # Refinement to target products with a price less than the value within the produc
    productPrimeShippingEligible: bool | None = None  # Target based on if a product is Prime-shipping eligible.
    productRatingGreaterThan: float | None = None  # Refinement to target products with a rating greater than the value within the pr
    productRatingLessThan: float | None = None  # Refinement to target products with a rating less than the value within the produ

class SPProductCategoryRefinementValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: dict[str, Any]

class SPProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: dict[str, Any]

class SPProductCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: dict[str, Any]

class SPProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""
    model_config = ConfigDict(extra="forbid")

    advertisedProduct: dict[str, Any]
    headline: str | None = None  # The headline/custom text associated with the ad creative.
    spotlightVideos: dict[str, Any] | None = None

class SPProductTarget(BaseModel):
    """Targets a specific product."""
    model_config = ConfigDict(extra="forbid")

    matchType: dict[str, Any]
    product: dict[str, Any]
    productIdType: dict[str, Any]

class SPProductValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productId: str  # The product identifier. Either the product id or the marketplace settings should

class SPPromptExtension(BaseModel):
    """Prompts Ad Extension"""
    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads

class SPSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""
    model_config = ConfigDict(extra="forbid")

    optimizeText: bool  # If the advertiser wants text they provided to be optimized by Amazon or not.
    videos: list[dict[str, Any]]  # The video asset(s) to use for the Sponsored Product experience.

class SPStatus(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    deliveryReasons: list[dict[str, Any]] | None = None  # This is the list of reasons behind the delivery status.
    deliveryStatus: dict[str, Any]

class SPTag(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.

class SPTarget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = None  # A unique identifier for the ad group associated with the target. Only used for a
    adProduct: dict[str, Any]
    bid: dict[str, Any] | None = None
    campaignId: str | None = None  # A unique identifier for the campaign associated with the target. Only used for c
    creationDateTime: datetime  # The date time the target was created.
    globalTargetId: str | None = None  # The global target identifier that manages this marketplace target.
    lastUpdatedDateTime: datetime  # The date time the target was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]]  # The list of marketplace in which the global target is applicable. The marketplac
    negative: bool  # Indicates whether the target is negative or not.
    state: dict[str, Any]
    status: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the target
    targetDetails: dict[str, Any]
    targetId: str  # A unique identifier for the target.
    targetLevel: dict[str, Any]
    targetType: dict[str, Any]

class SPTargetBid(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.
    currencyCode: dict[str, Any]

class SPTargetCreate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = None  # A unique identifier for the ad group associated with the target. Only used for a
    adProduct: dict[str, Any]
    bid: dict[str, Any] | None = None
    campaignId: str | None = None  # A unique identifier for the campaign associated with the target. Only used for c
    negative: bool  # Indicates whether the target is negative or not.
    state: dict[str, Any]
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the target
    targetDetails: dict[str, Any]
    targetType: dict[str, Any]

class SPTargetDetails(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

class SPTargetMultiStatusSuccess(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    index: int
    target: dict[str, Any]

class SPTargetUpdate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bid: dict[str, Any] | None = None
    state: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the target
    targetId: str  # A unique identifier for the target.

class SPThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""
    model_config = ConfigDict(extra="forbid")

    matchType: dict[str, Any]

class SPUpdateAdGroupBid(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    defaultBid: float | None = None  # The default maximum bid for ads and targets in the ad group. This is used in spo

class SPUpdateBidAdjustments(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on the audiences
    creativeBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment
    placementBidAdjustments: list[dict[str, Any]] | None = None  # Bid adjustments based on ad placements.

class SPUpdateBidSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: dict[str, Any] | None = None
    bidStrategy: dict[str, Any] | None = None

class SPUpdateBudgetSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: dict[str, Any] | None = None

class SPUpdateCampaignOptimizations(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidSettings: dict[str, Any] | None = None
    budgetSettings: dict[str, Any] | None = None

class SPUpdateCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

class SPUpdateProductCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: dict[str, Any] | None = None

class SPUpdateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""
    model_config = ConfigDict(extra="forbid")

    spotlightVideos: dict[str, Any] | None = None

class SPUpdateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""
    model_config = ConfigDict(extra="forbid")

    optimizeText: bool | None = None  # If the advertiser wants text they provided to be optimized by Amazon or not.
    videos: list[dict[str, Any]] | None = None  # The video asset(s) to use for the Sponsored Product experience.

class SPUpdateTargetBid(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.

class SPVideo(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    assetId: str  # The asset library ID associated with the video asset.
    assetVersion: str  # The asset library version associated with the video asset.
    description: str | None = None  # The description of the video content.
    headline: str | None = None  # The headline/custom text associated with the video.

class SPVideoExtension(BaseModel):
    """Video Ad Extension"""
    model_config = ConfigDict(extra="forbid")

    renderedAssetId: str | None = None  # The video asset ID rendered in the ad.
    renderedCoverImageUrl: str | None = None  # The image displayed over the video player before the video is played.
    videoType: dict[str, Any]


# ── Request Bodies ──
class BadRequestResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str

class SPCreateAdExtensionRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[dict[str, Any]] | None = None

class SPCreateAdGroupRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroups: list[dict[str, Any]] | None = None

class SPCreateAdRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    ads: list[dict[str, Any]] | None = None

class SPCreateCampaignRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    campaigns: list[dict[str, Any]] | None = None

class SPCreateTargetRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    targets: list[dict[str, Any]] | None = None

class SPDeleteAdGroupRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupIds: list[str] | None = None

class SPDeleteAdRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adIds: list[str] | None = None

class SPDeleteCampaignRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    campaignIds: list[str] | None = None

class SPDeleteTargetRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    targetIds: list[str] | None = None

class SPQueryAdExtensionRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adExtensionIdFilter: dict[str, Any] | None = None
    adExtensionStatusFilter: dict[str, Any] | None = None
    adExtensionTypeFilter: dict[str, Any] | None = None
    adGroupIdFilter: dict[str, Any] | None = None
    adIdFilter: dict[str, Any] | None = None
    adProductFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: dict[str, Any] | None = None

class SPQueryAdGroupRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: dict[str, Any] | None = None
    adProductFilter: dict[str, Any]
    campaignIdFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    nameFilter: dict[str, Any] | None = None
    nextToken: str | None = None
    stateFilter: dict[str, Any] | None = None

class SPQueryAdRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: dict[str, Any] | None = None
    adIdFilter: dict[str, Any] | None = None
    adProductFilter: dict[str, Any]
    campaignIdFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: dict[str, Any] | None = None

class SPQueryCampaignRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adProductFilter: dict[str, Any]
    campaignIdFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    nameFilter: dict[str, Any] | None = None
    nextToken: str | None = None
    portfolioIdFilter: dict[str, Any] | None = None
    stateFilter: dict[str, Any] | None = None

class SPQueryTargetRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: dict[str, Any] | None = None
    adProductFilter: dict[str, Any]
    campaignIdFilter: dict[str, Any] | None = None
    keywordFilter: dict[str, Any] | None = None
    matchTypeFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    negativeFilter: dict[str, Any] | None = None
    nextToken: str | None = None
    productIdFilter: dict[str, Any] | None = None
    stateFilter: dict[str, Any] | None = None
    targetIdFilter: dict[str, Any] | None = None
    targetTypeFilter: dict[str, Any] | None = None

class SPUpdateAdExtensionRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[dict[str, Any]] | None = None

class SPUpdateAdGroupRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroups: list[dict[str, Any]] | None = None

class SPUpdateAdRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    ads: list[dict[str, Any]] | None = None

class SPUpdateCampaignRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    campaigns: list[dict[str, Any]] | None = None

class SPUpdateTargetRequest(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    targets: list[dict[str, Any]] | None = None

class TooManyRequestsResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str


# ── Response Bodies ──
class BadGatewayResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: str
    message: str

class ContentTooLargeResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str

class ForbiddenResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str

class GatewayTimeoutResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: str
    message: str

class InternalServerErrorResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: str
    message: str

class NotFoundResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str

class SPAdExtensionMultiStatusResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None

class SPAdExtensionSuccessResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adExtensions: list[dict[str, Any]] | None = None
    nextToken: str | None = None

class SPAdGroupMultiStatusResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None

class SPAdGroupSuccessResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroups: list[dict[str, Any]] | None = None
    nextToken: str | None = None

class SPAdMultiStatusResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None

class SPAdSuccessResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    ads: list[dict[str, Any]] | None = None
    nextToken: str | None = None

class SPCampaignMultiStatusResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None

class SPCampaignSuccessResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    campaigns: list[dict[str, Any]] | None = None
    nextToken: str | None = None

class SPTargetMultiStatusResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None

class SPTargetSuccessResponse(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    nextToken: str | None = None
    targets: list[dict[str, Any]] | None = None

class ServiceUnavailableErrorResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: str
    message: str

class UnauthorizedResponseContent(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str


# ── Other Schemas ──
class Error(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    fieldLocation: str | None = None
    message: str

class ErrorsIndex(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    errors: list[dict[str, Any]]
    index: int

