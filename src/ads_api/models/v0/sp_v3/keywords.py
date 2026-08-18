"""Auto-generated models for Keywords from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
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
    SponsoredProductsInternalServerError,
    SponsoredProductsInternalServerErrorReason,
    SponsoredProductsKeywordServingStatus,
    SponsoredProductsKeywordServingStatusDetail,
    SponsoredProductsKeywordServingStatusReason,
    SponsoredProductsKeywordTextFilter,
    SponsoredProductsLocaleError,
    SponsoredProductsLocaleErrorReason,
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

type SponsoredProductsCreateOrUpdateMatchType = Literal["BROAD", "EXACT", "PHRASE"]


type SponsoredProductsMatchType = Literal[
    "BROAD",
    "EXACT",
    "OTHER",
    "PHRASE",
]


class SponsoredProductsBulkKeywordOperationResponse(LenientModel):
    error: list[SponsoredProductsKeywordFailureResponseItem] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SponsoredProductsKeywordSuccessResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SponsoredProductsCreateKeyword(StrictModel):
    adGroupId: str = Field(description="The identifier of the ad group to which this keyword is associated.")
    bid: float | None = Field(
        default=None,
        description="Bid associated with this keyword. Applicable to biddable match types only. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    campaignId: str = Field(description="The identifer of the campaign to which the keyword is associated.")
    keywordText: str = Field(description="The keyword text.")
    matchType: SponsoredProductsCreateOrUpdateMatchType
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: str | None = Field(
        default=None,
        description="The locale preference of the advertiser. For example, if the advertiser’s preferred language is Simplified Chinese, set the locale to zh_CN. Supported locales include: Simplified Chinese (locale: zh_CN) for US, UK and CA. English (locale: en_GB) for DE, FR, IT and ES.",
    )
    state: SponsoredProductsCreateOrUpdateEntityState


class SponsoredProductsCreateSponsoredProductsKeywordsRequestContent(StrictModel):
    keywords: list[SponsoredProductsCreateKeyword] = Field(
        min_length=0, max_length=1000, description="An array of keywords."
    )


class SponsoredProductsCreateSponsoredProductsKeywordsResponseContent(LenientModel):
    keywords: SponsoredProductsBulkKeywordOperationResponse


class SponsoredProductsDeleteSponsoredProductsKeywordsRequestContent(StrictModel):
    keywordIdFilter: SponsoredProductsObjectIdFilter


class SponsoredProductsDeleteSponsoredProductsKeywordsResponseContent(LenientModel):
    keywords: SponsoredProductsBulkKeywordOperationResponse


class SponsoredProductsKeyword(LenientModel):
    adGroupId: str = Field(description="The identifier of the ad group to which this keyword is associated.")
    bid: float | None = Field(
        default=None,
        description="Bid associated with this keyword. Applicable to biddable match types only. Keywords that do not have bid values in listKeywords will inherit the defaultBid from the adGroup level. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    campaignId: str = Field(description="The identifier of the campaign to which the keyword is associated.")
    extendedData: SponsoredProductsKeywordExtendedData | None = Field(default=None)
    globalKeywordId: str | None = Field(
        default=None, description="The global keyword identifier that manages this marketplace keyword."
    )
    keywordId: str = Field(description="The identifier of the keyword.")
    keywordText: str = Field(description="The keyword text.")
    matchType: SponsoredProductsMatchType | str
    nativeLanguageKeyword: str | None = Field(
        default=None, description="The unlocalized keyword text in the preferred locale of the advertiser."
    )
    nativeLanguageLocale: str | None = Field(
        default=None,
        description="The locale preference of the advertiser. For example, if the advertiser’s preferred language is Simplified Chinese, set the locale to zh_CN. Supported locales include: Simplified Chinese (locale: zh_CN) for US, UK and CA. English (locale: en_GB) for DE, FR, IT and ES.",
    )
    state: SponsoredProductsEntityState | str = Field(description="""
Supported values:
- `ENABLED`: Enabled State
- `PAUSED`: Paused State
- `PROPOSED`: Proposed State (Upcoming Feature)
- `ARCHIVED`: ARCHIVED State
- `ENABLING`: State for Draft Entity Only
- `USER_DELETED`: State for Draft Entity Only
- `OTHER`: Read Only
""")


class SponsoredProductsKeywordExtendedData(LenientModel):
    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Last updated date in ISO 8601.")
    servingStatus: SponsoredProductsKeywordServingStatus | str | None = Field(default=None)
    servingStatusDetails: list[SponsoredProductsKeywordServingStatusDetail] | None = Field(
        default=None, description="The serving status reasons of the Keyword"
    )


class SponsoredProductsKeywordFailureResponseItem(LenientModel):
    errors: list[SponsoredProductsKeywordMutationError] | None = Field(
        default=None, description="A list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the keyword in the array from the request body")


class SponsoredProductsKeywordMutationError(LenientModel):
    errorType: str = Field(description="The type of the error")
    errorValue: SponsoredProductsKeywordMutationErrorSelector


class SponsoredProductsKeywordMutationErrorSelector(LenientModel):
    biddingError: SponsoredProductsBiddingError | None = Field(default=None)
    billingError: SponsoredProductsBillingError | None = Field(default=None)
    duplicateValueError: SponsoredProductsDuplicateValueError | None = Field(default=None)
    entityNotFoundError: SponsoredProductsEntityNotFoundError | None = Field(default=None)
    entityQuotaError: SponsoredProductsEntityQuotaError | None = Field(default=None)
    entityStateError: SponsoredProductsEntityStateError | None = Field(default=None)
    internalServerError: SponsoredProductsInternalServerError | None = Field(default=None)
    localeError: SponsoredProductsLocaleError | None = Field(default=None)
    malformedValueError: SponsoredProductsMalformedValueError | None = Field(default=None)
    missingValueError: SponsoredProductsMissingValueError | None = Field(default=None)
    otherError: SponsoredProductsOtherError | None = Field(default=None)
    parentEntityError: SponsoredProductsParentEntityError | None = Field(default=None)
    rangeError: SponsoredProductsRangeError | None = Field(default=None)
    targetingClauseSetupError: SponsoredProductsTargetingClauseSetupError | None = Field(default=None)
    throttledError: SponsoredProductsThrottledError | None = Field(default=None)


class SponsoredProductsKeywordSuccessResponseItem(LenientModel):
    index: int = Field(ge=0, description="the index of the keyword in the array from the request body")
    keyword: SponsoredProductsKeyword | None = Field(default=None)
    keywordId: str | None = Field(default=None, description="the keyword ID")


class SponsoredProductsListSponsoredProductsKeywordsRequestContent(StrictModel):
    adGroupIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    campaignIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus",
    )
    keywordIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    keywordTextFilter: SponsoredProductsKeywordTextFilter | None = Field(default=None)
    locale: str | None = Field(default=None, description="Restricts results to keywords associated with locale")
    matchTypeFilter: list[SponsoredProductsMatchType | str] | None = Field(
        default=None, description="Only the keyword with match type that is in this list will be listed"
    )
    maxResults: int | None = Field(
        default=None,
        description="Number of records to include in the paginated response. Defaults to max page size for given API",
    )
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    stateFilter: SponsoredProductsEntityStateFilter | None = Field(default=None)


class SponsoredProductsListSponsoredProductsKeywordsResponseContent(LenientModel):
    keywords: list[SponsoredProductsKeyword] | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    totalResults: int | None = Field(default=None, description="The total number of entities")


class SponsoredProductsUpdateKeyword(StrictModel):
    bid: float | None = Field(
        default=None,
        description="Bid associated with this keyword. Applicable to biddable match types only. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    keywordId: str = Field(description="The identifier of the keyword.")
    state: SponsoredProductsCreateOrUpdateEntityState | None = Field(default=None)


class SponsoredProductsUpdateSponsoredProductsKeywordsRequestContent(StrictModel):
    keywords: list[SponsoredProductsUpdateKeyword] = Field(
        min_length=0, max_length=1000, description="An array of keywords with updated values."
    )


class SponsoredProductsUpdateSponsoredProductsKeywordsResponseContent(LenientModel):
    keywords: SponsoredProductsBulkKeywordOperationResponse


__all__ = [
    "SponsoredProductsBiddingError",
    "SponsoredProductsBiddingErrorReason",
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsBulkKeywordOperationResponse",
    "SponsoredProductsCreateKeyword",
    "SponsoredProductsCreateOrUpdateEntityState",
    "SponsoredProductsCreateOrUpdateMatchType",
    "SponsoredProductsCreateSponsoredProductsKeywordsRequestContent",
    "SponsoredProductsCreateSponsoredProductsKeywordsResponseContent",
    "SponsoredProductsDeleteSponsoredProductsKeywordsRequestContent",
    "SponsoredProductsDeleteSponsoredProductsKeywordsResponseContent",
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
    "SponsoredProductsKeyword",
    "SponsoredProductsKeywordExtendedData",
    "SponsoredProductsKeywordFailureResponseItem",
    "SponsoredProductsKeywordMutationError",
    "SponsoredProductsKeywordMutationErrorSelector",
    "SponsoredProductsKeywordServingStatus",
    "SponsoredProductsKeywordServingStatusDetail",
    "SponsoredProductsKeywordServingStatusReason",
    "SponsoredProductsKeywordSuccessResponseItem",
    "SponsoredProductsKeywordTextFilter",
    "SponsoredProductsListSponsoredProductsKeywordsRequestContent",
    "SponsoredProductsListSponsoredProductsKeywordsResponseContent",
    "SponsoredProductsLocaleError",
    "SponsoredProductsLocaleErrorReason",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMatchType",
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
    "SponsoredProductsTargetingClauseSetupError",
    "SponsoredProductsTargetingClauseSetupErrorReason",
    "SponsoredProductsThrottledError",
    "SponsoredProductsThrottledErrorReason",
    "SponsoredProductsUpdateKeyword",
    "SponsoredProductsUpdateSponsoredProductsKeywordsRequestContent",
    "SponsoredProductsUpdateSponsoredProductsKeywordsResponseContent",
    "SponsoredProductsValueLimitErrorReason",
]
