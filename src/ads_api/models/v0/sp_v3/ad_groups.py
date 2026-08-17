"""Auto-generated models for Ad groups from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
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
    SponsoredProductsMalformedValueError,
    SponsoredProductsMalformedValueErrorReason,
    SponsoredProductsMarketplace,
    SponsoredProductsMissingValueError,
    SponsoredProductsMissingValueErrorReason,
    SponsoredProductsNameFilter,
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
    SponsoredProductsTargetingType,
    SponsoredProductsThrottledError,
    SponsoredProductsThrottledErrorReason,
    SponsoredProductsValueLimitErrorReason,
)


class SponsoredProductsAdGroupServingStatus(StrEnum):
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    ENDED = "ENDED"
    OTHER = "OTHER"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    REJECTED = "REJECTED"


class SponsoredProductsAdGroupServingStatusReason(StrEnum):
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL = "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
    AD_GROUP_ARCHIVED_DETAIL = "AD_GROUP_ARCHIVED_DETAIL"
    AD_GROUP_INCOMPLETE_DETAIL = "AD_GROUP_INCOMPLETE_DETAIL"
    AD_GROUP_LOW_BID_DETAIL = "AD_GROUP_LOW_BID_DETAIL"
    AD_GROUP_PAUSED_DETAIL = "AD_GROUP_PAUSED_DETAIL"
    AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL = "AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL"
    AD_GROUP_POLICING_PENDING_REVIEW_DETAIL = "AD_GROUP_POLICING_PENDING_REVIEW_DETAIL"
    AD_GROUP_STATUS_ENABLED_DETAIL = "AD_GROUP_STATUS_ENABLED_DETAIL"
    CAMPAIGN_ARCHIVED_DETAIL = "CAMPAIGN_ARCHIVED_DETAIL"
    CAMPAIGN_INCOMPLETE_DETAIL = "CAMPAIGN_INCOMPLETE_DETAIL"
    CAMPAIGN_OUT_OF_BUDGET_DETAIL = "CAMPAIGN_OUT_OF_BUDGET_DETAIL"
    CAMPAIGN_PAUSED_DETAIL = "CAMPAIGN_PAUSED_DETAIL"
    CAMPAIGN_STATUS_ENABLED_DETAIL = "CAMPAIGN_STATUS_ENABLED_DETAIL"
    ENDED_DETAIL = "ENDED_DETAIL"
    OTHER = "OTHER"
    PENDING_REVIEW_DETAIL = "PENDING_REVIEW_DETAIL"
    PENDING_START_DATE_DETAIL = "PENDING_START_DATE_DETAIL"
    PORTFOLIO_ARCHIVED_DETAIL = "PORTFOLIO_ARCHIVED_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PAUSED_DETAIL = "PORTFOLIO_PAUSED_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"
    REJECTED_DETAIL = "REJECTED_DETAIL"


class SponsoredProductsApplicableMarketplacesErrorReason(StrEnum):
    APPLICABLE_MARKETPLACES_MISMATCH_ERROR = "APPLICABLE_MARKETPLACES_MISMATCH_ERROR"


class SponsoredProductsAdGroup(LenientModel):
    adGroupId: str = Field(description="The identifier of the keyword.")
    campaignId: str = Field(description="The identifier of the campaign to which the keyword is associated.")
    defaultBid: float = Field(
        description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace)."
    )
    extendedData: SponsoredProductsAdGroupExtendedData | None = Field(default=None)
    globalAdGroupId: str | None = Field(
        default=None, description="The global adGroup identifier that manages this marketplace adGroup."
    )
    name: str = Field(description="The name of the ad group.")
    state: Annotated[SponsoredProductsEntityState | str, lenient_enum(SponsoredProductsEntityState)]


class SponsoredProductsAdGroupExtendedData(LenientModel):
    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Last updated date in ISO 8601.")
    servingStatus: (
        Annotated[SponsoredProductsAdGroupServingStatus | str, lenient_enum(SponsoredProductsAdGroupServingStatus)]
        | None
    ) = Field(default=None)
    servingStatusDetails: list[SponsoredProductsAdGroupServingStatusDetail] | None = Field(
        default=None, description="The serving status reasons of the AdGroup"
    )


class SponsoredProductsAdGroupFailureResponseItem(LenientModel):
    errors: list[SponsoredProductsAdGroupMutationError] | None = Field(
        default=None, description="A list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the adGroup in the array from the request body")


class SponsoredProductsAdGroupMutationError(LenientModel):
    errorType: str = Field(description="The type of the error")
    errorValue: SponsoredProductsAdGroupMutationErrorSelector


class SponsoredProductsAdGroupMutationErrorSelector(LenientModel):
    applicableMarketplacesError: SponsoredProductsApplicableMarketplacesError | None = Field(default=None)
    biddingError: SponsoredProductsBiddingError | None = Field(default=None)
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


class SponsoredProductsAdGroupServingStatusDetail(LenientModel):
    helpUrl: str | None = Field(
        default=None, description="A URL with additional information about the status identifier."
    )
    message: str | None = Field(
        default=None, description="A human-readable description of the status identifier specified in the name field."
    )
    name: (
        Annotated[
            SponsoredProductsAdGroupServingStatusReason | str, lenient_enum(SponsoredProductsAdGroupServingStatusReason)
        ]
        | None
    ) = Field(default=None)


class SponsoredProductsAdGroupSuccessResponseItem(LenientModel):
    adGroup: SponsoredProductsAdGroup | None = Field(default=None)
    adGroupId: str | None = Field(default=None, description="the adGroup ID")
    index: int = Field(ge=0, description="the index of the adGroup in the array from the request body")


class SponsoredProductsApplicableMarketplacesError(LenientModel):
    """Errors related to ad eligibility"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[
        SponsoredProductsApplicableMarketplacesErrorReason | str,
        lenient_enum(SponsoredProductsApplicableMarketplacesErrorReason),
    ]


class SponsoredProductsBulkAdGroupOperationResponse(LenientModel):
    error: list[SponsoredProductsAdGroupFailureResponseItem] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SponsoredProductsAdGroupSuccessResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SponsoredProductsCreateAdGroup(StrictModel):
    campaignId: str = Field(description="The identifier of the campaign to which the keyword is associated.")
    defaultBid: float = Field(
        description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace)."
    )
    name: str = Field(description="The name of the ad group.")
    state: Annotated[
        SponsoredProductsCreateOrUpdateEntityState, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
    ]


class SponsoredProductsCreateSponsoredProductsAdGroupsRequestContent(StrictModel):
    adGroups: list[SponsoredProductsCreateAdGroup] = Field(
        min_length=0, max_length=1000, description="An array of adGroups."
    )


class SponsoredProductsCreateSponsoredProductsAdGroupsResponseContent(LenientModel):
    adGroups: SponsoredProductsBulkAdGroupOperationResponse


class SponsoredProductsDeleteSponsoredProductsAdGroupsRequestContent(StrictModel):
    adGroupIdFilter: SponsoredProductsObjectIdFilter


class SponsoredProductsDeleteSponsoredProductsAdGroupsResponseContent(LenientModel):
    adGroups: SponsoredProductsBulkAdGroupOperationResponse


class SponsoredProductsListSponsoredProductsAdGroupsRequestContent(StrictModel):
    adGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    campaignIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    campaignTargetingTypeFilter: (
        Annotated[SponsoredProductsTargetingType, lenient_enum(SponsoredProductsTargetingType)] | None
    ) = Field(default=None)
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus",
    )
    maxResults: int | None = Field(
        default=None,
        description="Number of records to include in the paginated response. Defaults to max page size for given API",
    )
    nameFilter: SponsoredProductsNameFilter | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    stateFilter: SponsoredProductsEntityStateFilter | None = Field(default=None)


class SponsoredProductsListSponsoredProductsAdGroupsResponseContent(LenientModel):
    adGroups: list[SponsoredProductsAdGroup] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    totalResults: int | None = Field(default=None, description="The total number of entities")


class SponsoredProductsUpdateAdGroup(StrictModel):
    adGroupId: str = Field(description="The identifier of the keyword.")
    defaultBid: float | None = Field(
        default=None,
        description="A bid value for use when no bid is specified for keywords in the ad group. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: (
        Annotated[SponsoredProductsCreateOrUpdateEntityState, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)]
        | None
    ) = Field(default=None)


class SponsoredProductsUpdateSponsoredProductsAdGroupsRequestContent(StrictModel):
    adGroups: list[SponsoredProductsUpdateAdGroup] = Field(
        min_length=0, max_length=1000, description="An array of adGroups with updated values."
    )


class SponsoredProductsUpdateSponsoredProductsAdGroupsResponseContent(LenientModel):
    adGroups: SponsoredProductsBulkAdGroupOperationResponse


__all__ = [
    "SponsoredProductsAdGroup",
    "SponsoredProductsAdGroupExtendedData",
    "SponsoredProductsAdGroupFailureResponseItem",
    "SponsoredProductsAdGroupMutationError",
    "SponsoredProductsAdGroupMutationErrorSelector",
    "SponsoredProductsAdGroupServingStatus",
    "SponsoredProductsAdGroupServingStatusDetail",
    "SponsoredProductsAdGroupServingStatusReason",
    "SponsoredProductsAdGroupSuccessResponseItem",
    "SponsoredProductsApplicableMarketplacesError",
    "SponsoredProductsApplicableMarketplacesErrorReason",
    "SponsoredProductsBiddingError",
    "SponsoredProductsBiddingErrorReason",
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsBulkAdGroupOperationResponse",
    "SponsoredProductsCreateAdGroup",
    "SponsoredProductsCreateOrUpdateEntityState",
    "SponsoredProductsCreateSponsoredProductsAdGroupsRequestContent",
    "SponsoredProductsCreateSponsoredProductsAdGroupsResponseContent",
    "SponsoredProductsDeleteSponsoredProductsAdGroupsRequestContent",
    "SponsoredProductsDeleteSponsoredProductsAdGroupsResponseContent",
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
    "SponsoredProductsListSponsoredProductsAdGroupsRequestContent",
    "SponsoredProductsListSponsoredProductsAdGroupsResponseContent",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMissingValueError",
    "SponsoredProductsMissingValueErrorReason",
    "SponsoredProductsNameFilter",
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
    "SponsoredProductsTargetingType",
    "SponsoredProductsThrottledError",
    "SponsoredProductsThrottledErrorReason",
    "SponsoredProductsUpdateAdGroup",
    "SponsoredProductsUpdateSponsoredProductsAdGroupsRequestContent",
    "SponsoredProductsUpdateSponsoredProductsAdGroupsResponseContent",
    "SponsoredProductsValueLimitErrorReason",
]
