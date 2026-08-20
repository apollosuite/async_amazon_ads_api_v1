"""Auto-generated models for Recommendations from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type ErrorCode = Literal[
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


type SBAlternateBrandIdType = Literal["BRAND_REGISTRY"]
"""
The type of identifier for the alternate brand identifier.

Supported values:
- `BRAND_REGISTRY`: Previous version of brand identifier retrieved from BrandRegistry. Identifiers of this type are returned by the GET /brands operation.
"""


class Error(LenientModel):
    code: ErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SBBrandAlternateId(LenientModel):
    """Other types of brand identifiers for a brand that are used with other operations."""

    alternateBrandId: str = Field(description="The alternative brand identifier for the brandId.")
    alternateBrandIdType: SBAlternateBrandIdType | str


class SBBrandedKeyword(LenientModel):
    brandAlternateId: SBBrandAlternateId
    keyword: str = Field(description="Branded keyword")


class SBBrandedKeywordList(LenientModel):
    associatedBrandIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Brand IDs associated with the branded keyword list"
    )
    brandedKeyword: list[SBBrandedKeyword] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="Branded keywords are specific words or phrases that include a company's brand name or a registered trademark of a brand",
    )


class SBBrandedKeywordRecommendationTypeDetails(LenientModel):
    brandAlternateId: list[SBBrandAlternateId] = Field(min_length=1, max_length=1)
    brandIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The brand ID to scope branded keyword recommendations for",
    )


class SBCreateBrandAlternateId(StrictModel):
    """Other types of brand identifiers for a brand that are used with other operations."""

    alternateBrandId: str = Field(description="The alternative brand identifier for the brandId.")
    alternateBrandIdType: SBAlternateBrandIdType


class SBCreateBrandedKeywordRecommendationTypeDetails(StrictModel):
    brandAlternateId: list[SBCreateBrandAlternateId] = Field(min_length=1, max_length=1)
    brandIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The brand ID to scope branded keyword recommendations for",
    )


class SBCreateRecommendationRequest(StrictModel):
    recommendations: list[SBRecommendationCreate] | None = Field(default=None, min_length=1, max_length=1)


class SBCreateRecommendationTypeDetails(StrictModel):
    brandedKeywordRecommendationTypeDetails: SBCreateBrandedKeywordRecommendationTypeDetails


class SBObjectSettings(LenientModel):
    brandedKeywordList: SBBrandedKeywordList


class SBRecommendation(LenientModel):
    recommendationId: str = Field(description="The identifier of the recommendation")
    recommendationType: str = Field(
        description="A unique value to indicate similar recommendations, used for internal purposes only"
    )
    recommendationTypeDetails: SBRecommendationTypeDetails | None = Field(default=None)
    recommendedObjects: list[SBRecommendedObject] = Field(
        min_length=1, max_length=10, description="The target objects of the recommendation"
    )


class SBRecommendationCreate(StrictModel):
    recommendationType: str = Field(
        description="A unique value to indicate similar recommendations, used for internal purposes only"
    )
    recommendationTypeDetails: SBCreateRecommendationTypeDetails | None = Field(default=None)


class SBRecommendationMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1)
    success: list[SBRecommendationMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1)


class SBRecommendationMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=0)
    recommendation: SBRecommendation


class SBRecommendationTypeDetails(LenientModel):
    brandedKeywordRecommendationTypeDetails: SBBrandedKeywordRecommendationTypeDetails


class SBRecommendedObject(LenientModel):
    """Details of the recommended object"""

    recommendedObjectSettings: SBObjectSettings | None = Field(default=None)


__all__ = [
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "SBAlternateBrandIdType",
    "SBBrandAlternateId",
    "SBBrandedKeyword",
    "SBBrandedKeywordList",
    "SBBrandedKeywordRecommendationTypeDetails",
    "SBCreateBrandAlternateId",
    "SBCreateBrandedKeywordRecommendationTypeDetails",
    "SBCreateRecommendationRequest",
    "SBCreateRecommendationTypeDetails",
    "SBObjectSettings",
    "SBRecommendation",
    "SBRecommendationCreate",
    "SBRecommendationMultiStatusResponse",
    "SBRecommendationMultiStatusSuccess",
    "SBRecommendationTypeDetails",
    "SBRecommendedObject",
]
