"""Auto-generated models for Targeting clauses from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    SponsoredProductsAsinFilter,
    SponsoredProductsBiddingError,
    SponsoredProductsBiddingErrorReason,
    SponsoredProductsBillingError,
    SponsoredProductsBillingErrorReason,
    SponsoredProductsCreateOrUpdateEntityState,
    SponsoredProductsDuplicateValueError,
    SponsoredProductsDuplicateValueErrorReason,
    SponsoredProductsEntityNotFoundError,
    SponsoredProductsEntityNotFoundErrorReason,
    SponsoredProductsEntityQuotaError,
    SponsoredProductsEntityState,
    SponsoredProductsEntityStateError,
    SponsoredProductsEntityStateErrorReason,
    SponsoredProductsEntityStateFilter,
    SponsoredProductsEntityType,
    SponsoredProductsErrorCause,
    SponsoredProductsExpressionTypeError,
    SponsoredProductsExpressionTypeErrorReason,
    SponsoredProductsInternalServerError,
    SponsoredProductsInternalServerErrorReason,
    SponsoredProductsKeywordServingStatus,
    SponsoredProductsKeywordServingStatusDetail,
    SponsoredProductsKeywordServingStatusReason,
    SponsoredProductsMalformedValueError,
    SponsoredProductsMalformedValueErrorReason,
    SponsoredProductsMarketplace,
    SponsoredProductsMissingValueError,
    SponsoredProductsMissingValueErrorReason,
    SponsoredProductsObjectIdFilter,
    SponsoredProductsOtherError,
    SponsoredProductsOtherErrorReason,
    SponsoredProductsParentEntityError,
    SponsoredProductsParentEntityErrorReason,
    SponsoredProductsQueryTermMatchType,
    SponsoredProductsQuotaErrorReason,
    SponsoredProductsQuotaScope,
    SponsoredProductsRangeError,
    SponsoredProductsReducedObjectIdFilter,
    SponsoredProductsTargetingClauseSetupError,
    SponsoredProductsTargetingClauseSetupErrorReason,
    SponsoredProductsThrottledError,
    SponsoredProductsThrottledErrorReason,
    SponsoredProductsValueLimitErrorReason,
)


class SponsoredProductsCreateExpressionType(StrEnum):
    MANUAL = "MANUAL"


class SponsoredProductsCreateTargetingExpressionPredicateType(StrEnum):
    """
    The type of targeting expression. You can specify values for the following predicates:
    """

    ASIN_AGE_RANGE_SAME_AS = "ASIN_AGE_RANGE_SAME_AS"  # Target an age range that is in the expressed range. This refinement can be applied for toys and games categories only.
    ASIN_BRAND_SAME_AS = "ASIN_BRAND_SAME_AS"  # Target the brand that is the same as the brand expressed.
    ASIN_CATEGORY_SAME_AS = "ASIN_CATEGORY_SAME_AS"  # Target the category that is the same as the category expressed.
    ASIN_EXPANDED_FROM = "ASIN_EXPANDED_FROM"  # Target products similar in performance to the ASIN expressed.
    ASIN_GENRE_SAME_AS = "ASIN_GENRE_SAME_AS"  # Target products related to the expressed genre. This refinement can be applied for Books and eBooks categories only.
    ASIN_IS_PRIME_SHIPPING_ELIGIBLE = "ASIN_IS_PRIME_SHIPPING_ELIGIBLE"  # Target products that are Prime Shipping Eligible. This refinement can be applied at a category or brand level only.
    ASIN_PRICE_BETWEEN = "ASIN_PRICE_BETWEEN"  # Target a price that is between the prices expressed.
    ASIN_PRICE_GREATER_THAN = "ASIN_PRICE_GREATER_THAN"  # Target a price that is greater than the price expressed.
    ASIN_PRICE_LESS_THAN = "ASIN_PRICE_LESS_THAN"  # Target a price that is less than the price expressed.
    ASIN_REVIEW_RATING_BETWEEN = (
        "ASIN_REVIEW_RATING_BETWEEN"  # Target a review rating that is between the review ratings expressed.
    )
    ASIN_REVIEW_RATING_GREATER_THAN = (
        "ASIN_REVIEW_RATING_GREATER_THAN"  # Target a review rating that is greater than the review rating expressed.
    )
    ASIN_REVIEW_RATING_LESS_THAN = (
        "ASIN_REVIEW_RATING_LESS_THAN"  # Target a review rating less than the review rating that is expressed.
    )
    ASIN_SAME_AS = "ASIN_SAME_AS"  # Target an ASIN that is the same as the ASIN expressed.
    KEYWORD_GROUP_SAME_AS = "KEYWORD_GROUP_SAME_AS"  # Target the keyword group that is the same as the keyword group expressed (Beta coming soon).


class SponsoredProductsExpressionType(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"
    OTHER = "OTHER"


class SponsoredProductsExpressionTypeWithoutOther(StrEnum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class SponsoredProductsTargetingExpressionPredicateType(StrEnum):
    """
    The type of targeting expression. You can specify values for the following predicates:
    """

    ASIN_ACCESSORY_RELATED = "ASIN_ACCESSORY_RELATED"  # Auto Targeting - cannot be manually created - corresponds to the `Complements` target type in the UI, this will show your ad to shoppers who view the detail pages of products that complement your product.
    ASIN_AGE_RANGE_SAME_AS = "ASIN_AGE_RANGE_SAME_AS"  # Target an age range that is in the expressed range. This refinement can be applied for toys and games categories only.
    ASIN_BRAND_SAME_AS = "ASIN_BRAND_SAME_AS"  # Target the brand that is the same as the brand expressed.
    ASIN_CATEGORY_SAME_AS = "ASIN_CATEGORY_SAME_AS"  # Target the category that is the same as the category expressed
    ASIN_EXPANDED_FROM = "ASIN_EXPANDED_FROM"  # Target products similar in performance to the ASIN expressed.
    ASIN_GENRE_SAME_AS = "ASIN_GENRE_SAME_AS"  # Target products related to the expressed genre. This refinement can be applied for Books and eBooks categories only.
    ASIN_IS_PRIME_SHIPPING_ELIGIBLE = "ASIN_IS_PRIME_SHIPPING_ELIGIBLE"  # Target products that are Prime Shipping Eligible. This refinement can be applied at a category or brand level only.
    ASIN_PRICE_BETWEEN = "ASIN_PRICE_BETWEEN"  # Target a price that is between the prices expressed.
    ASIN_PRICE_GREATER_THAN = "ASIN_PRICE_GREATER_THAN"  # Target a price that is greater than the price expressed.
    ASIN_PRICE_LESS_THAN = "ASIN_PRICE_LESS_THAN"  # Target a price that is less than the price expressed.
    ASIN_REVIEW_RATING_BETWEEN = (
        "ASIN_REVIEW_RATING_BETWEEN"  # Target a review rating that is between the review ratings expressed.
    )
    ASIN_REVIEW_RATING_GREATER_THAN = (
        "ASIN_REVIEW_RATING_GREATER_THAN"  # Target a review rating that is greater than the review rating expressed.
    )
    ASIN_REVIEW_RATING_LESS_THAN = (
        "ASIN_REVIEW_RATING_LESS_THAN"  # Target a review rating less than the review rating that is expressed.
    )
    ASIN_SAME_AS = "ASIN_SAME_AS"  # Target an ASIN that is the same as the ASIN expressed.
    ASIN_SUBSTITUTE_RELATED = "ASIN_SUBSTITUTE_RELATED"  # Auto Targeting - cannot be manually created - corresponds to the `Substitutes` target type in the UI, this will show your ad to shoppers who use detail pages of products similar to yours.
    KEYWORD_GROUP_SAME_AS = "KEYWORD_GROUP_SAME_AS"  # Target the keyword group that is the same as the keyword group expressed (Beta coming soon).
    OTHER = "OTHER"  # Other Type.
    QUERY_BROAD_REL_MATCHES = "QUERY_BROAD_REL_MATCHES"  # Auto Targeting - cannot be manually created - corresponds to the `Loose match` target type in the UI, this will show your ad to shoppers who use search terms loosely related to your products.
    QUERY_HIGH_REL_MATCHES = "QUERY_HIGH_REL_MATCHES"  # Auto Targeting - cannot be manually created - corresponds to the `Close match` target type in the UI, this will show your ad to shoppers who use search terms closely related to your products.


class SponsoredProductsTargetingExpressionPredicateTypeWithoutOther(StrEnum):
    """
    The type of targeting expression. You can specify values for the following predicates:
    """

    ASIN_ACCESSORY_RELATED = "ASIN_ACCESSORY_RELATED"  # Auto Targeting - cannot be manually created - corresponds to the `Complements` target type in the UI, this will show your ad to shoppers who view the detail pages of products that complement your product.
    ASIN_AGE_RANGE_SAME_AS = "ASIN_AGE_RANGE_SAME_AS"  # Target an age range that is in the expressed range. This refinement can be applied for toys and games categories only.
    ASIN_BRAND_SAME_AS = "ASIN_BRAND_SAME_AS"  # Target the brand that is the same as the brand expressed.
    ASIN_CATEGORY_SAME_AS = "ASIN_CATEGORY_SAME_AS"  # Target the category that is the same as the category expressed
    ASIN_EXPANDED_FROM = "ASIN_EXPANDED_FROM"  # Target products similar in performance to the ASIN expressed.
    ASIN_GENRE_SAME_AS = "ASIN_GENRE_SAME_AS"  # Target products related to the expressed genre. This refinement can be applied for Books and eBooks categories only.
    ASIN_IS_PRIME_SHIPPING_ELIGIBLE = "ASIN_IS_PRIME_SHIPPING_ELIGIBLE"  # Target products that are Prime Shipping Eligible. This refinement can be applied at a category or brand level only.
    ASIN_PRICE_BETWEEN = "ASIN_PRICE_BETWEEN"  # Target a price that is between the prices expressed.
    ASIN_PRICE_GREATER_THAN = "ASIN_PRICE_GREATER_THAN"  # Target a price that is greater than the price expressed.
    ASIN_PRICE_LESS_THAN = "ASIN_PRICE_LESS_THAN"  # Target a price that is less than the price expressed.
    ASIN_REVIEW_RATING_BETWEEN = (
        "ASIN_REVIEW_RATING_BETWEEN"  # Target a review rating that is between the review ratings expressed.
    )
    ASIN_REVIEW_RATING_GREATER_THAN = (
        "ASIN_REVIEW_RATING_GREATER_THAN"  # Target a review rating that is greater than the review rating expressed.
    )
    ASIN_REVIEW_RATING_LESS_THAN = (
        "ASIN_REVIEW_RATING_LESS_THAN"  # Target a review rating less than the review rating that is expressed.
    )
    ASIN_SAME_AS = "ASIN_SAME_AS"  # Target an ASIN that is the same as the ASIN expressed.
    ASIN_SUBSTITUTE_RELATED = "ASIN_SUBSTITUTE_RELATED"  # Auto Targeting - cannot be manually created - corresponds to the `Substitutes` target type in the UI, this will show your ad to shoppers who use detail pages of products similar to yours.
    KEYWORD_GROUP_SAME_AS = "KEYWORD_GROUP_SAME_AS"  # Target the keyword group that is the same as the keyword group expressed (Beta coming soon).
    QUERY_BROAD_REL_MATCHES = "QUERY_BROAD_REL_MATCHES"  # Auto Targeting - cannot be manually created - corresponds to the `Loose match` target type in the UI, this will show your ad to shoppers who use search terms loosely related to your products.
    QUERY_HIGH_REL_MATCHES = "QUERY_HIGH_REL_MATCHES"  # Auto Targeting - cannot be manually created - corresponds to the `Close match` target type in the UI, this will show your ad to shoppers who use search terms closely related to your products.


class SponsoredProductsBulkTargetingClauseOperationResponse(LenientModel):
    error: list[SponsoredProductsTargetingClauseFailureResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    success: list[SponsoredProductsTargetingClauseSuccessResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent(StrictModel):
    targetingClauses: list[SponsoredProductsCreateTargetingClause] = Field(
        min_length=0, max_length=1000, description="An array of targetingClauses."
    )


class SponsoredProductsCreateSponsoredProductsTargetingClausesResponseContent(LenientModel):
    targetingClauses: SponsoredProductsBulkTargetingClauseOperationResponse


class SponsoredProductsCreateTargetingClause(StrictModel):
    adGroupId: str = Field(description="The identifier of the ad group to which this target is associated.")
    bid: float | None = Field(
        default=None,
        description="The bid for ads sourced using the target. Targets that do not have bid values in listTargetingClauses will inherit the defaultBid from the adGroup level. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    campaignId: str = Field(description="The identifier of the campaign to which this target is associated.")
    expression: list[SponsoredProductsCreateTargetingExpressionPredicate] = Field(
        min_length=0, max_length=1000, description="The targeting expression."
    )
    expressionType: Annotated[
        SponsoredProductsCreateExpressionType | str, lenient_enum(SponsoredProductsCreateExpressionType)
    ]
    state: Annotated[
        SponsoredProductsCreateOrUpdateEntityState | str, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
    ]


class SponsoredProductsCreateTargetingExpressionPredicate(StrictModel):
    type: Annotated[
        SponsoredProductsCreateTargetingExpressionPredicateType | str,
        lenient_enum(SponsoredProductsCreateTargetingExpressionPredicateType),
    ]
    value: str | None = Field(default=None, description="The expression value")


class SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent(StrictModel):
    targetIdFilter: SponsoredProductsObjectIdFilter


class SponsoredProductsDeleteSponsoredProductsTargetingClausesResponseContent(LenientModel):
    targetingClauses: SponsoredProductsBulkTargetingClauseOperationResponse


class SponsoredProductsExpressionTypeFilter(StrictModel):
    """Filter entities by ExpressionType"""

    include: list[Annotated[SponsoredProductsExpressionType | str, lenient_enum(SponsoredProductsExpressionType)]] = (
        Field(min_length=0, max_length=2)
    )


class SponsoredProductsListSponsoredProductsTargetingClausesRequestContent(StrictModel):
    adGroupIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    asinFilter: SponsoredProductsAsinFilter | None = Field(default=None)
    campaignIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    expressionTypeFilter: SponsoredProductsExpressionTypeFilter | None = Field(default=None)
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus",
    )
    maxResults: int | None = Field(
        default=None,
        description="Number of records to include in the paginated response. Defaults to max page size for given API",
    )
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    stateFilter: SponsoredProductsEntityStateFilter | None = Field(default=None)
    targetIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)


class SponsoredProductsListSponsoredProductsTargetingClausesResponseContent(LenientModel):
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    targetingClauses: list[SponsoredProductsTargetingClause] | None = Field(default=None, min_length=0, max_length=1000)
    totalResults: int | None = Field(default=None, description="The total number of entities")


class SponsoredProductsTargetMutationError(LenientModel):
    errorType: str = Field(description="The type of the error")
    errorValue: SponsoredProductsTargetMutationErrorSelector


class SponsoredProductsTargetMutationErrorSelector(LenientModel):
    biddingError: SponsoredProductsBiddingError | None = Field(default=None)
    billingError: SponsoredProductsBillingError | None = Field(default=None)
    duplicateValueError: SponsoredProductsDuplicateValueError | None = Field(default=None)
    entityNotFoundError: SponsoredProductsEntityNotFoundError | None = Field(default=None)
    entityQuotaError: SponsoredProductsEntityQuotaError | None = Field(default=None)
    entityStateError: SponsoredProductsEntityStateError | None = Field(default=None)
    expressionTypeError: SponsoredProductsExpressionTypeError | None = Field(default=None)
    internalServerError: SponsoredProductsInternalServerError | None = Field(default=None)
    malformedValueError: SponsoredProductsMalformedValueError | None = Field(default=None)
    missingValueError: SponsoredProductsMissingValueError | None = Field(default=None)
    otherError: SponsoredProductsOtherError | None = Field(default=None)
    parentEntityError: SponsoredProductsParentEntityError | None = Field(default=None)
    rangeError: SponsoredProductsRangeError | None = Field(default=None)
    targetingClauseSetupError: SponsoredProductsTargetingClauseSetupError | None = Field(default=None)
    throttledError: SponsoredProductsThrottledError | None = Field(default=None)


class SponsoredProductsTargetingClause(LenientModel):
    adGroupId: str = Field(description="The identifier of the ad group to which this target is associated.")
    bid: float | None = Field(
        default=None,
        description="The bid for ads sourced using the target. Targets that do not have bid values in listTargetingClauses will inherit the defaultBid from the adGroup level. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    campaignId: str = Field(description="The identifier of the campaign to which this target is associated.")
    expression: list[SponsoredProductsTargetingExpressionPredicate] = Field(
        min_length=0, max_length=1000, description="The targeting expression."
    )
    expressionType: Annotated[SponsoredProductsExpressionType | str, lenient_enum(SponsoredProductsExpressionType)]
    extendedData: SponsoredProductsTargetingClauseExtendedData | None = Field(default=None)
    globalTargetId: str | None = Field(
        default=None, description="The global target identifier that manages this marketplace target."
    )
    resolvedExpression: list[SponsoredProductsTargetingExpressionPredicate] = Field(
        min_length=0, max_length=1000, description="The resolved targeting expression."
    )
    state: Annotated[SponsoredProductsEntityState | str, lenient_enum(SponsoredProductsEntityState)]
    targetId: str = Field(description="The target identifier")


class SponsoredProductsTargetingClauseExtendedData(LenientModel):
    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Last updated date in ISO 8601.")
    servingStatus: (
        Annotated[SponsoredProductsKeywordServingStatus | str, lenient_enum(SponsoredProductsKeywordServingStatus)]
        | None
    ) = Field(default=None)
    servingStatusDetails: list[SponsoredProductsKeywordServingStatusDetail] | None = Field(
        default=None, description="The serving status reasons of the TargetingClause"
    )


class SponsoredProductsTargetingClauseFailureResponseItem(LenientModel):
    errors: list[SponsoredProductsTargetMutationError] | None = Field(
        default=None, description="A list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the targetingClause in the array from the request body")


class SponsoredProductsTargetingClauseSuccessResponseItem(LenientModel):
    index: int = Field(ge=0, description="the index of the targetingClause in the array from the request body")
    targetId: str | None = Field(default=None, description="the targetingClause ID")
    targetingClause: SponsoredProductsTargetingClause | None = Field(default=None)


class SponsoredProductsTargetingExpressionPredicate(LenientModel):
    type: (
        Annotated[
            SponsoredProductsTargetingExpressionPredicateType | str,
            lenient_enum(SponsoredProductsTargetingExpressionPredicateType),
        ]
        | None
    ) = Field(default=None)
    value: str | None = Field(default=None, description="The expression value")


class SponsoredProductsTargetingExpressionPredicateWithoutOther(StrictModel):
    type: Annotated[
        SponsoredProductsTargetingExpressionPredicateTypeWithoutOther | str,
        lenient_enum(SponsoredProductsTargetingExpressionPredicateTypeWithoutOther),
    ]
    value: str | None = Field(default=None, description="The expression value")


class SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent(StrictModel):
    targetingClauses: list[SponsoredProductsUpdateTargetingClause] = Field(
        min_length=0, max_length=1000, description="An array of targetingClauses with updated values."
    )


class SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent(LenientModel):
    targetingClauses: SponsoredProductsBulkTargetingClauseOperationResponse


class SponsoredProductsUpdateTargetingClause(StrictModel):
    bid: float | None = Field(
        default=None,
        description="The bid for ads sourced using the target. Targets that do not have bid values in listTargetingClauses will inherit the defaultBid from the adGroup level. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    expression: list[SponsoredProductsTargetingExpressionPredicateWithoutOther] | None = Field(
        default=None, min_length=0, max_length=1000, description="The targeting expression."
    )
    expressionType: (
        Annotated[
            SponsoredProductsExpressionTypeWithoutOther | str, lenient_enum(SponsoredProductsExpressionTypeWithoutOther)
        ]
        | None
    ) = Field(default=None)
    state: (
        Annotated[
            SponsoredProductsCreateOrUpdateEntityState | str, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
        ]
        | None
    ) = Field(default=None)
    targetId: str = Field(description="The target identifier")


__all__ = [
    "SponsoredProductsAsinFilter",
    "SponsoredProductsBiddingError",
    "SponsoredProductsBiddingErrorReason",
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsBulkTargetingClauseOperationResponse",
    "SponsoredProductsCreateExpressionType",
    "SponsoredProductsCreateOrUpdateEntityState",
    "SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent",
    "SponsoredProductsCreateSponsoredProductsTargetingClausesResponseContent",
    "SponsoredProductsCreateTargetingClause",
    "SponsoredProductsCreateTargetingExpressionPredicate",
    "SponsoredProductsCreateTargetingExpressionPredicateType",
    "SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent",
    "SponsoredProductsDeleteSponsoredProductsTargetingClausesResponseContent",
    "SponsoredProductsDuplicateValueError",
    "SponsoredProductsDuplicateValueErrorReason",
    "SponsoredProductsEntityNotFoundError",
    "SponsoredProductsEntityNotFoundErrorReason",
    "SponsoredProductsEntityQuotaError",
    "SponsoredProductsEntityState",
    "SponsoredProductsEntityStateError",
    "SponsoredProductsEntityStateErrorReason",
    "SponsoredProductsEntityStateFilter",
    "SponsoredProductsEntityType",
    "SponsoredProductsErrorCause",
    "SponsoredProductsExpressionType",
    "SponsoredProductsExpressionTypeError",
    "SponsoredProductsExpressionTypeErrorReason",
    "SponsoredProductsExpressionTypeFilter",
    "SponsoredProductsExpressionTypeWithoutOther",
    "SponsoredProductsInternalServerError",
    "SponsoredProductsInternalServerErrorReason",
    "SponsoredProductsKeywordServingStatus",
    "SponsoredProductsKeywordServingStatusDetail",
    "SponsoredProductsKeywordServingStatusReason",
    "SponsoredProductsListSponsoredProductsTargetingClausesRequestContent",
    "SponsoredProductsListSponsoredProductsTargetingClausesResponseContent",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMissingValueError",
    "SponsoredProductsMissingValueErrorReason",
    "SponsoredProductsObjectIdFilter",
    "SponsoredProductsOtherError",
    "SponsoredProductsOtherErrorReason",
    "SponsoredProductsParentEntityError",
    "SponsoredProductsParentEntityErrorReason",
    "SponsoredProductsQueryTermMatchType",
    "SponsoredProductsQuotaErrorReason",
    "SponsoredProductsQuotaScope",
    "SponsoredProductsRangeError",
    "SponsoredProductsReducedObjectIdFilter",
    "SponsoredProductsTargetMutationError",
    "SponsoredProductsTargetMutationErrorSelector",
    "SponsoredProductsTargetingClause",
    "SponsoredProductsTargetingClauseExtendedData",
    "SponsoredProductsTargetingClauseFailureResponseItem",
    "SponsoredProductsTargetingClauseSetupError",
    "SponsoredProductsTargetingClauseSetupErrorReason",
    "SponsoredProductsTargetingClauseSuccessResponseItem",
    "SponsoredProductsTargetingExpressionPredicate",
    "SponsoredProductsTargetingExpressionPredicateType",
    "SponsoredProductsTargetingExpressionPredicateTypeWithoutOther",
    "SponsoredProductsTargetingExpressionPredicateWithoutOther",
    "SponsoredProductsThrottledError",
    "SponsoredProductsThrottledErrorReason",
    "SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent",
    "SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent",
    "SponsoredProductsUpdateTargetingClause",
    "SponsoredProductsValueLimitErrorReason",
]
