"""Auto-generated Pydantic models from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum


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


class SPAdProduct(StrEnum):
    """| AdProduct | Description |
    |------|------|
    | `SPONSORED_PRODUCTS` | Sponsored Products ad product. |
    """

    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"


class SPCreateState(StrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

    | CreateState | Description |
    |------|------|
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    """

    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


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


class SPMarketplaceScope(StrEnum):
    """| MarketplaceScope | Description |
    |------|------|
    | `SINGLE_MARKETPLACE` |  |
    """

    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"


class SPProductIdType(StrEnum):
    """| ProductIdType | Description |
    |------|------|
    | `ASIN` | ASIN identifier type. |
    | `SKU` | SKU identifier type. |
    """

    ASIN = "ASIN"
    SKU = "SKU"


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


class SPUpdateState(StrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

    | UpdateState | Description |
    |------|------|
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    """

    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
