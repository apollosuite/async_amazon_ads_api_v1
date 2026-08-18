"""Auto-generated models for Negative keywords from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    SponsoredProductsBillingError,
    SponsoredProductsBillingErrorReason,
    SponsoredProductsCreateOrUpdateEntityState,
    SponsoredProductsCreateOrUpdateNegativeMatchType,
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
    SponsoredProductsKeywordTextFilter,
    SponsoredProductsMalformedValueError,
    SponsoredProductsMalformedValueErrorReason,
    SponsoredProductsMarketplace,
    SponsoredProductsMissingValueError,
    SponsoredProductsMissingValueErrorReason,
    SponsoredProductsNegativeMatchType,
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


class SponsoredProductsBulkNegativeKeywordOperationResponse(LenientModel):
    error: list[SponsoredProductsNegativeKeywordFailureResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    success: list[SponsoredProductsNegativeKeywordSuccessResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SponsoredProductsCreateNegativeKeyword(StrictModel):
    adGroupId: str = Field(description="The identifier of the ad group to which this keyword is associated.")
    campaignId: str = Field(description="The identifer of the campaign to which the keyword is associated.")
    keywordText: str = Field(description="The keyword text.")
    matchType: Annotated[
        SponsoredProductsCreateOrUpdateNegativeMatchType | str,
        lenient_enum(SponsoredProductsCreateOrUpdateNegativeMatchType),
    ]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser"
    )
    nativeLanguageLocale: str | None = Field(default=None, description="The locale preference of the advertiser.")
    state: Annotated[
        SponsoredProductsCreateOrUpdateEntityState | str, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
    ]


class SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent(StrictModel):
    negativeKeywords: list[SponsoredProductsCreateNegativeKeyword] = Field(
        min_length=0, max_length=1000, description="An array of negativeKeywords."
    )


class SponsoredProductsCreateSponsoredProductsNegativeKeywordsResponseContent(LenientModel):
    negativeKeywords: SponsoredProductsBulkNegativeKeywordOperationResponse


class SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent(StrictModel):
    negativeKeywordIdFilter: SponsoredProductsObjectIdFilter


class SponsoredProductsDeleteSponsoredProductsNegativeKeywordsResponseContent(LenientModel):
    negativeKeywords: SponsoredProductsBulkNegativeKeywordOperationResponse


class SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent(StrictModel):
    adGroupIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    campaignIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus",
    )
    locale: str | None = Field(
        default=None, description="Restricts results to negativeKeywords that match the specified locale."
    )
    matchTypeFilter: (
        list[Annotated[SponsoredProductsNegativeMatchType | str, lenient_enum(SponsoredProductsNegativeMatchType)]]
        | None
    ) = Field(
        default=None, description="Only the negativeKeyword with the match type that is in this list will be listed"
    )
    maxResults: int | None = Field(
        default=None,
        description="Number of records to include in the paginated response. Defaults to max page size for given API",
    )
    negativeKeywordIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    negativeKeywordTextFilter: SponsoredProductsKeywordTextFilter | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    stateFilter: SponsoredProductsEntityStateFilter | None = Field(default=None)


class SponsoredProductsListSponsoredProductsNegativeKeywordsResponseContent(LenientModel):
    negativeKeywords: list[SponsoredProductsNegativeKeyword] | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    totalResults: int | None = Field(default=None, description="The total number of entities")


class SponsoredProductsNegativeKeyword(LenientModel):
    adGroupId: str = Field(description="The identifier of the ad group to which this keyword is associated.")
    campaignId: str = Field(description="The identifier of the campaign to which the keyword is associated.")
    extendedData: SponsoredProductsNegativeKeywordExtendedData | None = Field(default=None)
    globalKeywordId: str | None = Field(
        default=None, description="The global keyword identifier that manages this marketplace keyword."
    )
    keywordId: str = Field(description="The identifier of the keyword.")
    keywordText: str = Field(description="The keyword text.")
    matchType: Annotated[SponsoredProductsNegativeMatchType | str, lenient_enum(SponsoredProductsNegativeMatchType)]
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser"
    )
    nativeLanguageLocale: str | None = Field(default=None, description="The locale preference of the advertiser.")
    state: Annotated[SponsoredProductsEntityState | str, lenient_enum(SponsoredProductsEntityState)]


class SponsoredProductsNegativeKeywordExtendedData(LenientModel):
    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Last updated date in ISO 8601.")
    servingStatus: (
        Annotated[SponsoredProductsKeywordServingStatus | str, lenient_enum(SponsoredProductsKeywordServingStatus)]
        | None
    ) = Field(default=None)
    servingStatusDetails: list[SponsoredProductsKeywordServingStatusDetail] | None = Field(
        default=None, description="The serving status reasons of the Keyword"
    )


class SponsoredProductsNegativeKeywordFailureResponseItem(LenientModel):
    errors: list[SponsoredProductsNegativeKeywordMutationError] | None = Field(
        default=None, description="A list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the negativeKeyword in the array from the request body")


class SponsoredProductsNegativeKeywordMutationError(LenientModel):
    errorType: str = Field(description="The type of the error")
    errorValue: SponsoredProductsNegativeKeywordMutationErrorSelector


class SponsoredProductsNegativeKeywordMutationErrorSelector(LenientModel):
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


class SponsoredProductsNegativeKeywordSuccessResponseItem(LenientModel):
    index: int = Field(ge=0, description="the index of the negativeKeyword in the array from the request body")
    negativeKeyword: SponsoredProductsNegativeKeyword | None = Field(default=None)
    negativeKeywordId: str | None = Field(default=None, description="the negativeKeyword ID")


class SponsoredProductsUpdateNegativeKeyword(StrictModel):
    keywordId: str = Field(description="The identifier of the keyword.")
    state: (
        Annotated[
            SponsoredProductsCreateOrUpdateEntityState | str, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
        ]
        | None
    ) = Field(default=None)


class SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent(StrictModel):
    negativeKeywords: list[SponsoredProductsUpdateNegativeKeyword] = Field(
        min_length=0, max_length=1000, description="An array of negativeKeywords with updated values."
    )


class SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent(LenientModel):
    negativeKeywords: SponsoredProductsBulkNegativeKeywordOperationResponse


__all__ = [
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsBulkNegativeKeywordOperationResponse",
    "SponsoredProductsCreateNegativeKeyword",
    "SponsoredProductsCreateOrUpdateEntityState",
    "SponsoredProductsCreateOrUpdateNegativeMatchType",
    "SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent",
    "SponsoredProductsCreateSponsoredProductsNegativeKeywordsResponseContent",
    "SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent",
    "SponsoredProductsDeleteSponsoredProductsNegativeKeywordsResponseContent",
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
    "SponsoredProductsKeywordTextFilter",
    "SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent",
    "SponsoredProductsListSponsoredProductsNegativeKeywordsResponseContent",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMissingValueError",
    "SponsoredProductsMissingValueErrorReason",
    "SponsoredProductsNegativeKeyword",
    "SponsoredProductsNegativeKeywordExtendedData",
    "SponsoredProductsNegativeKeywordFailureResponseItem",
    "SponsoredProductsNegativeKeywordMutationError",
    "SponsoredProductsNegativeKeywordMutationErrorSelector",
    "SponsoredProductsNegativeKeywordSuccessResponseItem",
    "SponsoredProductsNegativeMatchType",
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
    "SponsoredProductsUpdateNegativeKeyword",
    "SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent",
    "SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent",
    "SponsoredProductsValueLimitErrorReason",
]
