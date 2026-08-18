"""Auto-generated models for Campaign negative keywords from Amazon Ads API v0."""

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
    SponsoredProductsThrottledError,
    SponsoredProductsThrottledErrorReason,
    SponsoredProductsValueLimitErrorReason,
)


class SponsoredProductsBulkCampaignNegativeKeywordOperationResponse(LenientModel):
    error: list[SponsoredProductsCampaignNegativeKeywordFailureResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    success: list[SponsoredProductsCampaignNegativeKeywordSuccessResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SponsoredProductsCampaignNegativeKeyword(LenientModel):
    campaignId: str = Field(description="The identifier of the campaign to which the keyword is associated.")
    extendedData: SponsoredProductsCampaignNegativeKeywordExtendedData | None = Field(default=None)
    globalKeywordId: str | None = Field(
        default=None, description="The global keyword identifier that manages this marketplace keyword."
    )
    keywordId: str = Field(description="The identifier of the keyword.")
    keywordText: str = Field(description="The keyword text.")
    matchType: Annotated[SponsoredProductsNegativeMatchType | str, lenient_enum(SponsoredProductsNegativeMatchType)]
    state: Annotated[SponsoredProductsEntityState | str, lenient_enum(SponsoredProductsEntityState)]


class SponsoredProductsCampaignNegativeKeywordExtendedData(LenientModel):
    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Last updated date in ISO 8601.")
    servingStatus: (
        Annotated[SponsoredProductsKeywordServingStatus | str, lenient_enum(SponsoredProductsKeywordServingStatus)]
        | None
    ) = Field(default=None)
    servingStatusDetails: list[SponsoredProductsKeywordServingStatusDetail] | None = Field(
        default=None, description="The serving status reasons of the Keyword"
    )


class SponsoredProductsCampaignNegativeKeywordFailureResponseItem(LenientModel):
    errors: list[SponsoredProductsCampaignNegativeKeywordMutationError] | None = Field(
        default=None, description="A list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the campaign in the array from the request body")


class SponsoredProductsCampaignNegativeKeywordMutationError(LenientModel):
    errorType: str = Field(description="The type of the error")
    errorValue: SponsoredProductsCampaignNegativeKeywordMutationErrorSelector


class SponsoredProductsCampaignNegativeKeywordMutationErrorSelector(LenientModel):
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
    throttledError: SponsoredProductsThrottledError | None = Field(default=None)


class SponsoredProductsCampaignNegativeKeywordSuccessResponseItem(LenientModel):
    campaignNegativeKeyword: SponsoredProductsCampaignNegativeKeyword | None = Field(default=None)
    campaignNegativeKeywordId: str | None = Field(default=None, description="the campaignNegativeKeyword ID")
    index: int = Field(ge=0, description="the index of the campaign in the array from the request body")


class SponsoredProductsCreateCampaignNegativeKeyword(StrictModel):
    campaignId: str = Field(description="The identifier of the campaign to which the keyword is associated.")
    keywordText: str = Field(description="The keyword text.")
    matchType: Annotated[
        SponsoredProductsCreateOrUpdateNegativeMatchType | str,
        lenient_enum(SponsoredProductsCreateOrUpdateNegativeMatchType),
    ]
    state: Annotated[
        SponsoredProductsCreateOrUpdateEntityState | str, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
    ]


class SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsRequestContent(StrictModel):
    campaignNegativeKeywords: list[SponsoredProductsCreateCampaignNegativeKeyword] = Field(
        min_length=0, max_length=1000, description="An array of campaignNegativeKeywords."
    )


class SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsResponseContent(LenientModel):
    campaignNegativeKeywords: SponsoredProductsBulkCampaignNegativeKeywordOperationResponse


class SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsRequestContent(StrictModel):
    campaignNegativeKeywordIdFilter: SponsoredProductsObjectIdFilter


class SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsResponseContent(LenientModel):
    campaignNegativeKeywords: SponsoredProductsBulkCampaignNegativeKeywordOperationResponse


class SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsRequestContent(StrictModel):
    campaignIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    campaignNegativeKeywordIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    campaignNegativeKeywordTextFilter: SponsoredProductsKeywordTextFilter | None = Field(default=None)
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus",
    )
    matchTypeFilter: (
        list[Annotated[SponsoredProductsNegativeMatchType | str, lenient_enum(SponsoredProductsNegativeMatchType)]]
        | None
    ) = Field(default=None, description="Restricts results to resources with the selected matchType")
    maxResults: int | None = Field(
        default=None,
        description="Number of records to include in the paginated response. Defaults to max page size for given API",
    )
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    stateFilter: SponsoredProductsEntityStateFilter | None = Field(default=None)


class SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsResponseContent(LenientModel):
    campaignNegativeKeywords: list[SponsoredProductsCampaignNegativeKeyword] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    totalResults: int | None = Field(default=None, description="The total number of entities")


class SponsoredProductsUpdateCampaignNegativeKeyword(StrictModel):
    keywordId: str = Field(description="The identifier of the keyword.")
    state: (
        Annotated[
            SponsoredProductsCreateOrUpdateEntityState | str, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
        ]
        | None
    ) = Field(default=None)


class SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsRequestContent(StrictModel):
    campaignNegativeKeywords: list[SponsoredProductsUpdateCampaignNegativeKeyword] = Field(
        min_length=0, max_length=1000, description="An array of campaignNegativeKeywords with updated values."
    )


class SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsResponseContent(LenientModel):
    campaignNegativeKeywords: SponsoredProductsBulkCampaignNegativeKeywordOperationResponse


__all__ = [
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsBulkCampaignNegativeKeywordOperationResponse",
    "SponsoredProductsCampaignNegativeKeyword",
    "SponsoredProductsCampaignNegativeKeywordExtendedData",
    "SponsoredProductsCampaignNegativeKeywordFailureResponseItem",
    "SponsoredProductsCampaignNegativeKeywordMutationError",
    "SponsoredProductsCampaignNegativeKeywordMutationErrorSelector",
    "SponsoredProductsCampaignNegativeKeywordSuccessResponseItem",
    "SponsoredProductsCreateCampaignNegativeKeyword",
    "SponsoredProductsCreateOrUpdateEntityState",
    "SponsoredProductsCreateOrUpdateNegativeMatchType",
    "SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsRequestContent",
    "SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsResponseContent",
    "SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsRequestContent",
    "SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsResponseContent",
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
    "SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsRequestContent",
    "SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsResponseContent",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMissingValueError",
    "SponsoredProductsMissingValueErrorReason",
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
    "SponsoredProductsThrottledError",
    "SponsoredProductsThrottledErrorReason",
    "SponsoredProductsUpdateCampaignNegativeKeyword",
    "SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsRequestContent",
    "SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsResponseContent",
    "SponsoredProductsValueLimitErrorReason",
]
