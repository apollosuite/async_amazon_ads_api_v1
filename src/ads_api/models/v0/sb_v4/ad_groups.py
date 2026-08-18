"""Auto-generated models for Ad groups from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    BiddingError,
    CreateOrUpdateEntityState,
    DateError,
    EntityState,
    EntityStateFilter,
    ErrorCause,
    NameFilter,
    ObjectIdFilter,
    OtherError,
    QueryTermMatchType,
    RangeError,
)


class AdGroupServingStatus(StrEnum):
    """
    `Notice: the servingStatus enums have not been finalized yet.`
    The ad group serving status determined by system.
    - AD_GROUP_STATUS_ENABLED - Ad group's status is enabled.
    - AD_GROUP_PAUSED - Ad group's status is paused.
    - AD_GROUP_ARCHIVED - Ad group's status is archived.
    - AD_GROUP_INCOMPLETE - Ad group does not contain any ads or targeting clauses.
    - AD_GROUP_POLICING_PENDING_REVIEW - Ad group is pending review because of policing reason
    - AD_GROUP_POLICING_CREATIVE_REJECTED - Ad group is rejected due to creative because of policing reason
    - AD_GROUP_LOW_BID - Ad group is less than the minimum allowed bid in its marketplace

    - ADVERTISER_STATUS_ENABLED - Advertiser's status is enabled
    - ADVERTISER_POLICING_PENDING_REVIEW - Avertiser is pending review because of policing reason
    - ADVERTISER_POLICING_SUSPENDED - Advertiser's status is suspended because of policing reason
    - ADVERTISER_PAUSED - Advertiser's status is paused
    - ADVERTISER_ARCHIVED - Advertiser's status is archived
    - ADVERTISER_PAYMENT_FAILURE - Advertiser's internal status is suspended
    - ADVERTISER_ACCOUNT_OUT_OF_BUDGET - Advertiser is out of budget for all Sponsored Ads campaigns
    - ADVERTISER_OUT_OF_PREPAY_BALANCE - Advertiser is out of prepay balance for all Sponsored Ads campaigns
    - ADVERTISER_EXCEED_SPENDS_LIMIT - Advertiser spends over the daily limit

    - CAMPAIGN_STATUS_ENABLED - Campaign's (parent) status is enabled.
    - CAMPAIGN_PAUSED - Campaign's (parent) status is paused.
    - CAMPAIGN_ARCHIVED - Campaign's (parent) status is archived.
    - CAMPAIGN_INCOMPLETE - Campaign (parent) does not contain any ads or targeting clauses.
    - CAMPAIGN_OUT_OF_BUDGET - Campaign (parent) is out of budget.

    - PORTFOLIO_STATUS_ENABLED - Portfolio's (parent) status is enabled
    - PORTFOLIO_PAUSED - Portfolio's (parent) status is paused
    - PORTFOLIO_ARCHIVED - Portfolio's (parent) status is archived
    - PORTFOLIO_OUT_OF_BUDGET - Portfolio (parent) is out of budget
    - PORTFOLIO_PENDING_START_DATE - Portfolio's (parent) start date is in the future
    - PORTFOLIO_ENDED - Portfolio's (parent) end date is in the past.

    - INELIGIBLE - Ad group is ineligible.
    - ELIGIBLE - Ad group is eligible.
    - ENDED - Campaign's (parent) end date is in the past.
    - PENDING_REVIEW - Campaign (parent) is pending review.
    - PENDING_START_DATE - Campaign's (parent) start date is in the future.
    - REJECTED - Campaign (parent) is rejected by moderation process.
    - UNKNOWN - Serving status is unknown. Please contact us for support.
    """

    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    INELIGIBLE = "INELIGIBLE"
    ELIGIBLE = "ELIGIBLE"
    ENDED = "ENDED"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    REJECTED = "REJECTED"
    UNKNOWN = "UNKNOWN"


class AdGroup(LenientModel):
    campaignId: str = Field(description="The identifier of the campaign to which the keyword is associated.")
    name: str = Field(min_length=1, max_length=255, description="The name of the ad group.")
    state: Annotated[EntityState | str, lenient_enum(EntityState)]
    adGroupId: str = Field(description="The identifier of the keyword.")
    extendedData: AdGroupExtendedData | None = Field(default=None)


class AdGroupExtendedData(LenientModel):
    servingStatus: Annotated[AdGroupServingStatus | str, lenient_enum(AdGroupServingStatus)] | None = Field(
        default=None
    )
    lastUpdateDate: float | None = Field(default=None, description="Date of last update in epoch time.")
    servingStatusDetails: list[str] | None = Field(
        default=None, min_length=0, max_length=100, description="The serving status reasons of the Ad Group."
    )
    creationDate: float | None = Field(default=None, description="Creation date in epoch time.")


class AdGroupFailureResponseItem(LenientModel):
    index: float = Field(ge=0, le=10, description="the index of the adGroup in the array from the request body.")
    errors: list[AdGroupMutationError] | None = Field(
        default=None, min_length=0, max_length=100, description="A list of validation errors."
    )


class AdGroupMutationError(LenientModel):
    errorType: str = Field(description="The type of the error.")
    errorValue: AdGroupMutationErrorSelector


class AdGroupMutationErrorSelector(LenientModel):
    dateError: DateError | None = Field(default=None)
    biddingError: BiddingError | None = Field(default=None)
    rangeError: RangeError | None = Field(default=None)
    otherError: OtherError | None = Field(default=None)


class AdGroupSuccessResponseItem(LenientModel):
    adGroup: AdGroup | None = Field(default=None)
    index: float = Field(ge=0, le=10, description="the index of the adGroup in the array from the request body.")
    adGroupId: str | None = Field(default=None, description="the adGroup ID.")


class BulkAdGroupOperationResponse(LenientModel):
    success: list[AdGroupSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    error: list[AdGroupFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class CreateAdGroup(StrictModel):
    campaignId: str = Field(description="The identifier of the campaign to which the keyword is associated.")
    name: str = Field(min_length=1, max_length=255, description="The name of the ad group.")
    state: Annotated[CreateOrUpdateEntityState | str, lenient_enum(CreateOrUpdateEntityState)]


class CreateSponsoredBrandsAdGroupsRequestContent(StrictModel):
    adGroups: list[CreateAdGroup] = Field(min_length=1, max_length=10)


class CreateSponsoredBrandsAdGroupsResponseContent(LenientModel):
    adGroups: BulkAdGroupOperationResponse | None = Field(default=None)


class DeleteSponsoredBrandsAdGroupsRequestContent(StrictModel):
    adGroupIdFilter: ObjectIdFilter | None = Field(default=None)


class DeleteSponsoredBrandsAdGroupsResponseContent(LenientModel):
    adGroups: BulkAdGroupOperationResponse | None = Field(default=None)


class ListSponsoredBrandsAdGroupsRequestContent(StrictModel):
    campaignIdFilter: ObjectIdFilter | None = Field(default=None)
    stateFilter: EntityStateFilter | None = Field(default=None)
    maxResults: float | None = Field(
        default=None,
        ge=1,
        le=100,
        description="Number of records to include in the paginated response. Defaults to max page size for given API.",
    )
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    adGroupIdFilter: ObjectIdFilter | None = Field(default=None)
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="Setting to true will slow down performance because the API needs to retrieve extra information for each campaign.",
    )
    nameFilter: NameFilter | None = Field(default=None)


class ListSponsoredBrandsAdGroupsResponseContent(LenientModel):
    totalResults: float | None = Field(default=None, description="The total number of entities.")
    adGroups: list[AdGroup] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )


class UpdateAdGroup(StrictModel):
    name: str | None = Field(default=None, min_length=1, max_length=255, description="The name of the ad group.")
    state: Annotated[CreateOrUpdateEntityState | str, lenient_enum(CreateOrUpdateEntityState)] | None = Field(
        default=None
    )
    adGroupId: str = Field(description="The identifier of the keyword.")


class UpdateSponsoredBrandsAdGroupsRequestContent(StrictModel):
    adGroups: list[UpdateAdGroup] = Field(min_length=1, max_length=10)


class UpdateSponsoredBrandsAdGroupsResponseContent(LenientModel):
    adGroups: BulkAdGroupOperationResponse | None = Field(default=None)


__all__ = [
    "AdGroup",
    "AdGroupExtendedData",
    "AdGroupFailureResponseItem",
    "AdGroupMutationError",
    "AdGroupMutationErrorSelector",
    "AdGroupServingStatus",
    "AdGroupSuccessResponseItem",
    "BiddingError",
    "BulkAdGroupOperationResponse",
    "CreateAdGroup",
    "CreateOrUpdateEntityState",
    "CreateSponsoredBrandsAdGroupsRequestContent",
    "CreateSponsoredBrandsAdGroupsResponseContent",
    "DateError",
    "DeleteSponsoredBrandsAdGroupsRequestContent",
    "DeleteSponsoredBrandsAdGroupsResponseContent",
    "EntityState",
    "EntityStateFilter",
    "ErrorCause",
    "ListSponsoredBrandsAdGroupsRequestContent",
    "ListSponsoredBrandsAdGroupsResponseContent",
    "NameFilter",
    "ObjectIdFilter",
    "OtherError",
    "QueryTermMatchType",
    "RangeError",
    "UpdateAdGroup",
    "UpdateSponsoredBrandsAdGroupsRequestContent",
    "UpdateSponsoredBrandsAdGroupsResponseContent",
]
