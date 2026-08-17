"""Auto-generated models for Campaign negative targeting clauses from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    SponsoredProductsAsinFilter,
    SponsoredProductsBillingError,
    SponsoredProductsBillingErrorReason,
    SponsoredProductsCreateOrUpdateEntityState,
    SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate,
    SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicateType,
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
    SponsoredProductsNegativeTargetingExpressionPredicate,
    SponsoredProductsNegativeTargetingExpressionPredicateType,
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


class SponsoredProductsBulkCampaignNegativeTargetingClauseOperationResponse(LenientModel):
    error: list[SponsoredProductsCampaignNegativeTargetingClauseFailureResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    success: list[SponsoredProductsCampaignNegativeTargetingClauseSuccessResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SponsoredProductsCampaignNegativeTargetingClause(LenientModel):
    campaignId: str = Field(description="The identifier of the campaign to which this target is associated.")
    expression: list[SponsoredProductsNegativeTargetingExpressionPredicate] = Field(
        min_length=0, max_length=1000, description="The CampaignNegativeTargetingClause expression."
    )
    extendedData: SponsoredProductsCampaignNegativeTargetingClauseExtendedData | None = Field(default=None)
    globalTargetId: str | None = Field(
        default=None, description="The global target identifier that manages this marketplace target."
    )
    resolvedExpression: list[SponsoredProductsNegativeTargetingExpressionPredicate] = Field(
        min_length=0, max_length=1000, description="The resolved CampaignNegativeTargetingClause expression."
    )
    state: Annotated[SponsoredProductsEntityState | str, lenient_enum(SponsoredProductsEntityState)]
    targetId: str = Field(description="The target identifier")


class SponsoredProductsCampaignNegativeTargetingClauseExtendedData(LenientModel):
    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Last updated date in ISO 8601.")
    servingStatus: (
        Annotated[SponsoredProductsKeywordServingStatus | str, lenient_enum(SponsoredProductsKeywordServingStatus)]
        | None
    ) = Field(default=None)
    servingStatusDetails: list[SponsoredProductsKeywordServingStatusDetail] | None = Field(
        default=None, description="The serving status reasons of the CampaignNegativeTargetingClause"
    )


class SponsoredProductsCampaignNegativeTargetingClauseFailureResponseItem(LenientModel):
    errors: list[SponsoredProductsCampaignNegativeTargetsMutationError] | None = Field(
        default=None, description="A list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the CampaignNegativeTargets in the array from the request body")


class SponsoredProductsCampaignNegativeTargetingClauseSuccessResponseItem(LenientModel):
    campaignNegativeTargetingClauseId: str | None = Field(default=None, description="the CampaignNegativeTargets ID")
    campaignNegativeTargetingClauses: SponsoredProductsCampaignNegativeTargetingClause | None = Field(default=None)
    index: int = Field(ge=0, description="the index of the CampaignNegativeTargets in the array from the request body")


class SponsoredProductsCampaignNegativeTargetsMutationError(LenientModel):
    errorType: str = Field(description="The type of the error")
    errorValue: SponsoredProductsCampaignNegativeTargetsMutationErrorSelector


class SponsoredProductsCampaignNegativeTargetsMutationErrorSelector(LenientModel):
    billingError: SponsoredProductsBillingError | None = Field(default=None)
    duplicateValueError: SponsoredProductsDuplicateValueError | None = Field(default=None)
    entityNotFoundError: SponsoredProductsEntityNotFoundError | None = Field(default=None)
    entityQuotaError: SponsoredProductsEntityQuotaError | None = Field(default=None)
    entityStateError: SponsoredProductsEntityStateError | None = Field(default=None)
    internalServerError: SponsoredProductsInternalServerError | None = Field(default=None)
    malformedValueError: SponsoredProductsMalformedValueError | None = Field(default=None)
    missingValueError: SponsoredProductsMissingValueError | None = Field(default=None)
    otherError: SponsoredProductsOtherError | None = Field(default=None)
    parentEntityError: SponsoredProductsParentEntityError | None = Field(default=None)
    rangeError: SponsoredProductsRangeError | None = Field(default=None)
    targetingClauseSetupError: SponsoredProductsTargetingClauseSetupError | None = Field(default=None)
    throttledError: SponsoredProductsThrottledError | None = Field(default=None)


class SponsoredProductsCreateCampaignNegativeTargetingClause(StrictModel):
    campaignId: str = Field(
        description="The identifier of the campaign to which this target is associated. CampaignNegativeTargetingClauses are only available for AUTO campaigns"
    )
    expression: list[SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate] = Field(
        min_length=0, max_length=1000, description="The NegativeTargeting expression."
    )
    state: Annotated[
        SponsoredProductsCreateOrUpdateEntityState, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
    ]


class SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesRequestContent(StrictModel):
    campaignNegativeTargetingClauses: list[SponsoredProductsCreateCampaignNegativeTargetingClause] = Field(
        min_length=0, max_length=1000, description="An array of Campaign Negative TargetingClauses."
    )


class SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesResponseContent(LenientModel):
    campaignNegativeTargetingClauses: SponsoredProductsBulkCampaignNegativeTargetingClauseOperationResponse


class SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent(StrictModel):
    campaignNegativeTargetIdFilter: SponsoredProductsObjectIdFilter


class SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesResponseContent(LenientModel):
    campaignNegativeTargetingClauses: SponsoredProductsBulkCampaignNegativeTargetingClauseOperationResponse


class SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesRequestContent(StrictModel):
    asinFilter: SponsoredProductsAsinFilter | None = Field(default=None)
    campaignIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    campaignNegativeTargetIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
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


class SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesResponseContent(LenientModel):
    campaignNegativeTargetingClauses: list[SponsoredProductsCampaignNegativeTargetingClause] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    totalResults: int | None = Field(default=None, description="The total number of entities")


class SponsoredProductsUpdateCampaignNegativeTargetingClause(StrictModel):
    expression: list[SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate] | None = Field(
        default=None, min_length=0, max_length=1000, description="The NegativeTargeting expression."
    )
    state: (
        Annotated[SponsoredProductsCreateOrUpdateEntityState, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)]
        | None
    ) = Field(default=None)
    targetId: str = Field(description="The target identifier")


class SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesRequestContent(StrictModel):
    campaignNegativeTargetingClauses: list[SponsoredProductsUpdateCampaignNegativeTargetingClause] = Field(
        min_length=0, max_length=1000, description="An array of Campaign Negative TargetingClauses with updated values."
    )


class SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesResponseContent(LenientModel):
    campaignNegativeTargetingClauses: SponsoredProductsBulkCampaignNegativeTargetingClauseOperationResponse


__all__ = [
    "SponsoredProductsAsinFilter",
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsBulkCampaignNegativeTargetingClauseOperationResponse",
    "SponsoredProductsCampaignNegativeTargetingClause",
    "SponsoredProductsCampaignNegativeTargetingClauseExtendedData",
    "SponsoredProductsCampaignNegativeTargetingClauseFailureResponseItem",
    "SponsoredProductsCampaignNegativeTargetingClauseSuccessResponseItem",
    "SponsoredProductsCampaignNegativeTargetsMutationError",
    "SponsoredProductsCampaignNegativeTargetsMutationErrorSelector",
    "SponsoredProductsCreateCampaignNegativeTargetingClause",
    "SponsoredProductsCreateOrUpdateEntityState",
    "SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate",
    "SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicateType",
    "SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesRequestContent",
    "SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesResponseContent",
    "SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent",
    "SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesResponseContent",
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
    "SponsoredProductsInternalServerError",
    "SponsoredProductsInternalServerErrorReason",
    "SponsoredProductsKeywordServingStatus",
    "SponsoredProductsKeywordServingStatusDetail",
    "SponsoredProductsKeywordServingStatusReason",
    "SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesRequestContent",
    "SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesResponseContent",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMissingValueError",
    "SponsoredProductsMissingValueErrorReason",
    "SponsoredProductsNegativeTargetingExpressionPredicate",
    "SponsoredProductsNegativeTargetingExpressionPredicateType",
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
    "SponsoredProductsTargetingClauseSetupError",
    "SponsoredProductsTargetingClauseSetupErrorReason",
    "SponsoredProductsThrottledError",
    "SponsoredProductsThrottledErrorReason",
    "SponsoredProductsUpdateCampaignNegativeTargetingClause",
    "SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesRequestContent",
    "SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesResponseContent",
    "SponsoredProductsValueLimitErrorReason",
]
