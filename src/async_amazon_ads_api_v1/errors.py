"""Shared HTTP error response models (used by all product APIs)."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class ErrorCode(StrEnum):
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


class Error(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    fieldLocation: str | None = None
    message: str


class ErrorsIndex(BaseModel):
    model_config = ConfigDict(extra="forbid")

    errors: list[Error]
    index: int


class BadGatewayResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class BadRequestResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class ContentTooLargeResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class ForbiddenResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class GatewayTimeoutResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class InternalServerErrorResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class NotFoundResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class ServiceUnavailableErrorResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class TooManyRequestsResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class UnauthorizedResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str
