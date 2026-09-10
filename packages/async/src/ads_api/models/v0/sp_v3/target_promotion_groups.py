"""Auto-generated models for TargetPromotionGroups from Amazon Ads API v0."""

from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    SponsoredProductsBiddingError,
    SponsoredProductsBiddingErrorReason,
    SponsoredProductsBillingError,
    SponsoredProductsBillingErrorReason,
    SponsoredProductsDuplicateValueError,
    SponsoredProductsDuplicateValueErrorReason,
    SponsoredProductsEntityNotFoundError,
    SponsoredProductsEntityNotFoundErrorReason,
    SponsoredProductsEntityQuotaError,
    SponsoredProductsEntityStateError,
    SponsoredProductsEntityStateErrorReason,
    SponsoredProductsEntityType,
    SponsoredProductsErrorCause,
    SponsoredProductsExpressionTypeError,
    SponsoredProductsExpressionTypeErrorReason,
    SponsoredProductsInternalServerError,
    SponsoredProductsInternalServerErrorReason,
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
    SponsoredProductsQuotaErrorReason,
    SponsoredProductsQuotaScope,
    SponsoredProductsRangeError,
    SponsoredProductsTags,
    SponsoredProductsTargetingClauseSetupError,
    SponsoredProductsTargetingClauseSetupErrorReason,
    SponsoredProductsThrottledError,
    SponsoredProductsThrottledErrorReason,
    SponsoredProductsValueLimitErrorReason,
)

type SponsoredProductsInvalidInputErrorReason = Literal["INVALID_TOKEN"]


type SponsoredProductsKeywordMatchType = Literal["BROAD", "EXACT", "PHRASE"]


type SponsoredProductsTargetType = Literal["ASIN", "KEYWORD"]
"""
Indicates if the recommendation target is a Keyword or ASIN
"""


type SponsoredProductsTargetingExpressionMatchType = Literal["PRODUCT_EXACT", "PRODUCT_SIMILAR"]


class SponsoredProductsCreateKeywordTarget(StrictModel):
    """A keyword target."""

    bid: float | None = Field(
        default=None,
        ge=0,
        description="Bid associated with the target. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    keyword: str = Field(description="The keyword text.")
    matchType: SponsoredProductsKeywordMatchType


class SponsoredProductsCreateProductTarget(StrictModel):
    """A product target."""

    bid: float | None = Field(
        default=None,
        ge=0,
        description="Bid associated with the target. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    matchType: SponsoredProductsTargetingExpressionMatchType
    target: str = Field(description="The product ASIN of the target.")


class SponsoredProductsCreateTarget(LenientModel):
    """Target created in the target promotion group."""

    manualTargetingAdGroupId: str | None = Field(
        default=None, description="The adGroupId of the manual-targeting campaign where the target belongs."
    )
    targetId: str | None = Field(default=None, description="The id of the target that got created.")
    targetPromotionGroupId: str | None = Field(default=None, description="The id of the target promotion group.")


class SponsoredProductsCreateTargetError(LenientModel):
    """Response object of failed target promotion group target."""

    errorType: str | None = Field(default=None, description="The type of the error.")
    errorValue: SponsoredProductsCreateTargetErrorSelector | None = Field(default=None)


class SponsoredProductsCreateTargetErrorSelectorBiddingError(LenientModel):
    biddingError: SponsoredProductsBiddingError


class SponsoredProductsCreateTargetErrorSelectorBillingError(LenientModel):
    billingError: SponsoredProductsBillingError


class SponsoredProductsCreateTargetErrorSelectorDuplicateValueError(LenientModel):
    duplicateValueError: SponsoredProductsDuplicateValueError


class SponsoredProductsCreateTargetErrorSelectorEntityNotFoundError(LenientModel):
    entityNotFoundError: SponsoredProductsEntityNotFoundError


class SponsoredProductsCreateTargetErrorSelectorEntityQuotaError(LenientModel):
    entityQuotaError: SponsoredProductsEntityQuotaError


class SponsoredProductsCreateTargetErrorSelectorEntityStateError(LenientModel):
    entityStateError: SponsoredProductsEntityStateError


class SponsoredProductsCreateTargetErrorSelectorExpressionTypeError(LenientModel):
    expressionTypeError: SponsoredProductsExpressionTypeError


class SponsoredProductsCreateTargetErrorSelectorLocaleError(LenientModel):
    localeError: SponsoredProductsLocaleError


class SponsoredProductsCreateTargetErrorSelectorMalformedValueError(LenientModel):
    malformedValueError: SponsoredProductsMalformedValueError


class SponsoredProductsCreateTargetErrorSelectorMissingValueError(LenientModel):
    missingValueError: SponsoredProductsMissingValueError


class SponsoredProductsCreateTargetErrorSelectorParentEntityError(LenientModel):
    parentEntityError: SponsoredProductsParentEntityError


class SponsoredProductsCreateTargetErrorSelectorRangeError(LenientModel):
    rangeError: SponsoredProductsRangeError


class SponsoredProductsCreateTargetErrorSelectorOtherError(LenientModel):
    otherError: SponsoredProductsOtherError


class SponsoredProductsCreateTargetErrorSelectorInternalServerError(LenientModel):
    internalServerError: SponsoredProductsInternalServerError


class SponsoredProductsCreateTargetErrorSelectorInvalidInputError(LenientModel):
    invalidInputError: SponsoredProductsInvalidInputError


class SponsoredProductsCreateTargetErrorSelectorThrottledError(LenientModel):
    throttledError: SponsoredProductsThrottledError


class SponsoredProductsCreateTargetErrorSelectorTargetingClauseSetupError(LenientModel):
    targetingClauseSetupError: SponsoredProductsTargetingClauseSetupError


type SponsoredProductsCreateTargetErrorSelector = SponsoredProductsCreateTargetErrorSelectorBiddingError | SponsoredProductsCreateTargetErrorSelectorBillingError | SponsoredProductsCreateTargetErrorSelectorDuplicateValueError | SponsoredProductsCreateTargetErrorSelectorEntityNotFoundError | SponsoredProductsCreateTargetErrorSelectorEntityQuotaError | SponsoredProductsCreateTargetErrorSelectorEntityStateError | SponsoredProductsCreateTargetErrorSelectorExpressionTypeError | SponsoredProductsCreateTargetErrorSelectorLocaleError | SponsoredProductsCreateTargetErrorSelectorMalformedValueError | SponsoredProductsCreateTargetErrorSelectorMissingValueError | SponsoredProductsCreateTargetErrorSelectorParentEntityError | SponsoredProductsCreateTargetErrorSelectorRangeError | SponsoredProductsCreateTargetErrorSelectorOtherError | SponsoredProductsCreateTargetErrorSelectorInternalServerError | SponsoredProductsCreateTargetErrorSelectorInvalidInputError | SponsoredProductsCreateTargetErrorSelectorThrottledError | SponsoredProductsCreateTargetErrorSelectorTargetingClauseSetupError


class SponsoredProductsCreateTargetPromotionGroupTargetsBatchError(LenientModel):
    """Response object of failed target promotion group target."""

    index: str | None = Field(default=None, description="index of the item in the request.")
    subErrors: list[SponsoredProductsError] | None = Field(
        default=None, min_length=1, max_length=100, description="A list of the errors encountered."
    )


class SponsoredProductsCreateTargetPromotionGroupTargetsBatchSuccess(LenientModel):
    """Response object of successfully created target promotion group target."""

    index: str | None = Field(default=None, description="index of the item in the request.")
    targetDetails: SponsoredProductsTargetPromotionGroupTargetDetails | None = Field(default=None)


class SponsoredProductsCreateTargetPromotionGroupTargetsFailureResponseItem(LenientModel):
    """Response object of failed target promotion group target."""

    errors: list[SponsoredProductsCreateTargetError] | None = Field(
        default=None,
        min_length=0,
        max_length=10000,
        description="Response object of failed target promotion group target.",
    )
    expressionType: str | None = Field(
        default=None, description="The expression type of the target that was requested to be created."
    )
    target: str | None = Field(default=None, description="The target that was requested to be created.")


class SponsoredProductsCreateTargetPromotionGroupTargetsRequestContent(StrictModel):
    """Request object for creating target promotion group targets in a target promotion group."""

    targetPromotionGroupId: str = Field(
        description="The id of the target promotion group where the targets are being added."
    )
    targets: list[SponsoredProductsCreateTargetRequest] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="List of targets to be added to the target promotion group.",
    )


class SponsoredProductsCreateTargetPromotionGroupTargetsResponseContent(LenientModel):
    """Response object for creating target promotion group targets."""

    errors: list[SponsoredProductsCreateTargetPromotionGroupTargetsFailureResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of targets that failed to create."
    )
    success: list[SponsoredProductsCreateTargetPromotionGroupTargetsSuccessResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of successfully created targets."
    )


class SponsoredProductsCreateTargetPromotionGroupTargetsSuccessResponseItem(LenientModel):
    """Response object of successfully created target promotion group target."""

    expressionType: str | None = Field(
        default=None, description="The expression type of the target that was requested to be created."
    )
    target: str | None = Field(default=None, description="The target that was requested to be created.")
    targetDetails: SponsoredProductsCreateTarget | None = Field(default=None)


class SponsoredProductsCreateTargetPromotionGroupTargetsV2RequestContent(StrictModel):
    """Request object for creating target promotion group targets in a target promotion group."""

    targetPromotionGroupId: str = Field(
        description="The id of the target promotion group where the targets are being added."
    )
    targets: list[SponsoredProductsCreateTargetRequestV2] | None = Field(
        default=None,
        min_length=1,
        max_length=1000,
        description="List of targets to be added to the target promotion group.",
    )


class SponsoredProductsCreateTargetPromotionGroupTargetsV2ResponseContent(LenientModel):
    """Response object for creating target promotion group targets."""

    error: list[SponsoredProductsCreateTargetPromotionGroupTargetsBatchError] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    success: list[SponsoredProductsCreateTargetPromotionGroupTargetsBatchSuccess] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SponsoredProductsCreateTargetPromotionGroupsRequestContent(StrictModel):
    """Request object for creating a Target Promotion Group."""

    adGroupId: str = Field(
        description="The adGroupId of the Ad Group of an Auto-Targeting campaign that will be part of the Target Promotion Group."
    )
    adIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1000,
        description="""
The list of adIds (optional) of the Ad Group of the Auto-Targeting campaign, that will be part of the Target Promotion Group. If this
    list is empty, all the Product Ads under the Ad Group will be part of the Target Promotion Group.
""",
    )
    existingCampaignDetails: SponsoredProductsExistingCampaignDetails | None = Field(default=None)
    newCampaignDetails: SponsoredProductsNewCampaignDetails | None = Field(default=None)


class SponsoredProductsCreateTargetPromotionGroupsResponseContent(LenientModel):
    """Response object for creating a target promotion group."""

    targetPromotionGroup: SponsoredProductsTargetPromotionGroup | None = Field(default=None)


class SponsoredProductsCreateTargetPromotionGroupsV2RequestContent(StrictModel):
    """Request object for creating a Target Promotion Group."""

    adGroupId: str = Field(
        description="The adGroupId of the source Ad Group that will be part of the Target Promotion Group."
    )
    adIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="""
The list of adIds (optional) of the source Ad Group, that will be part of the Target Promotion Group. If this
    list is not provided, all the Product Ads under the source Ad Group will be part of the Target Promotion Group.
""",
    )
    existingCampaignDetails: list[SponsoredProductsExistingAdGroup] | None = Field(
        default=None,
        min_length=1,
        max_length=2,
        description="""
List of existing manual campaign ad groups to be added in the Target Promotion Group. It must contain one keyword ad group, or one
    product ad group, or both. The request will fail if this field is provided alongside newCampaignDetails.
""",
    )
    newCampaignDetails: list[SponsoredProductsNewCampaign] | None = Field(
        default=None,
        min_length=1,
        max_length=2,
        description="""
List of new destination manual campaigns to be created as part of the Target Promotion Group. It must contain setting for the creation of
     one keyword ad group, or one product ad group, or both. The request will fail if this field is provided alongside existingCampaignDetails.
""",
    )
    targetPromotionGroupName: str = Field(description="The name of the target promotion group that will be created.")


class SponsoredProductsCreateTargetPromotionGroupsV2ResponseContent(LenientModel):
    """Response object for creating a target promotion group."""

    targetPromotionGroup: SponsoredProductsTargetPromotionGroupV2 | None = Field(default=None)


class SponsoredProductsCreateTargetRequest(StrictModel):
    """Request object for the target promotion group's target."""

    bid: float | None = Field(
        default=None,
        ge=0,
        description="Bid associated with the target. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    expressionType: str = Field(description="""
The match type (for KEYWORDs) or the expression type (for PRODUCT). One of QUERY_BROAD_MATCHES,
    QUERY_EXACT_MATCHES, QUERY_PHRASE_MATCHES, ASIN_SAME_AS, ASIN_EXPANDED_FROM
""")
    target: str = Field(description="The keyword or the product ASIN to be targeted.")


class SponsoredProductsCreateTargetRequestV2KeywordTarget(StrictModel):
    keywordTarget: SponsoredProductsCreateKeywordTarget


class SponsoredProductsCreateTargetRequestV2ProductTarget(StrictModel):
    productTarget: SponsoredProductsCreateProductTarget


type SponsoredProductsCreateTargetRequestV2 = SponsoredProductsCreateTargetRequestV2KeywordTarget | SponsoredProductsCreateTargetRequestV2ProductTarget


class SponsoredProductsError(LenientModel):
    errorCode: str | None = Field(default=None)
    errorMessage: str | None = Field(default=None)


class SponsoredProductsExistingAdGroup(StrictModel):
    adGroupId: str = Field(description="The id of the Ad Group.")


class SponsoredProductsExistingCampaignDetails(StrictModel):
    """The request object for creating a new target promotion group with existing campaigns. Please note that the adGroupIds provided need to
    contain the same Ad ASINs/SKUs combination as the Auto-Targeting adGroup for the target promotion group."""

    keywordCampaignAdGroupIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
AdGroupIds of existing manual campaigns to be used as part of the Target Promotion Group for
    promoting keyword targets.
""",
    )
    productCampaignAdGroupIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
AdGroupIds of existing manual campaigns to be used as part of the Target Promotion Group for
    promoting product targets.
""",
    )


class SponsoredProductsGetTargetPromotionGroupsRecommendationsRequestContent(StrictModel):
    adGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    adIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    campaignIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    maxResults: int | None = Field(
        default=None,
        ge=1,
        le=1000,
        description="Number of records to include in the paginated response. Defaults to 1000.",
    )
    nextToken: str | None = Field(default=None, description="Token for fetching the next page")


class SponsoredProductsGetTargetPromotionGroupsRecommendationsResponseContent(LenientModel):
    nextToken: str | None = Field(default=None, description="Token for fetching the next page")
    targets: list[SponsoredProductsRecommendedTarget] = Field(
        min_length=0,
        max_length=1000,
        description="List of optimized targets for the request, as recommended by Amazon heuristics",
    )
    totalResults: int = Field(description="Total number of records available")


class SponsoredProductsInvalidInputError(LenientModel):
    """Errors related to ad eligibility"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsInvalidInputErrorReason | str


class SponsoredProductsKeywordTargetV2(LenientModel):
    """A keyword target."""

    destinationAdGroupId: str | None = Field(
        default=None, description="The adGroupId of the destination manual-targeting adGroup where the target belongs."
    )
    keywordId: str | None = Field(default=None, description="The id of the keyword target.")
    keywordText: str | None = Field(default=None, description="The keyword text.")
    matchType: str | None = Field(
        default=None, description="The match type (for KEYWORDs). One of EXACT, PHRASE, BROAD"
    )
    targetPromotionGroupId: str | None = Field(default=None, description="The id of the target promotion group.")


class SponsoredProductsListTargetPromotionGroupTargetsRequestContent(StrictModel):
    """Request object for querying target promotion group targets."""

    adGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000, description="The maximum number of results requested.")
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next or previous response page"
    )
    targetPromotionGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)


class SponsoredProductsListTargetPromotionGroupTargetsResponseContent(LenientModel):
    """Response object for querying target promotion group targets."""

    nextToken: str | None = Field(
        default=None,
        description="""
To retrieve the next page of results, call the same operation and specify this token in the
    request. If the nextToken field is empty, there are no further results.
""",
    )
    targets: list[SponsoredProductsTarget] | None = Field(default=None, min_length=0, max_length=1000)
    totalResults: int | None = Field(default=None, description="The total number of results available.")


class SponsoredProductsListTargetPromotionGroupTargetsV2RequestContent(StrictModel):
    """Request object for querying target promotion group targets."""

    adGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000, description="The maximum number of results requested.")
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next or previous response page"
    )
    targetPromotionGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)


class SponsoredProductsListTargetPromotionGroupTargetsV2ResponseContent(LenientModel):
    """Response object for querying target promotion group targets."""

    nextToken: str | None = Field(
        default=None,
        description="""
To retrieve the next page of results, call the same operation and specify this token in the
    request. If the nextToken field is empty, there are no further results.
""",
    )
    targets: list[SponsoredProductsTargetPromotionGroupTargetDetails] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    totalResults: int | None = Field(default=None, description="The total number of results available.")


class SponsoredProductsListTargetPromotionGroupsRequestContent(StrictModel):
    """Request object for querying target promotion groups."""

    adGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000, description="The maximum number of results requested.")
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next or previous response page"
    )
    targetPromotionGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)


class SponsoredProductsListTargetPromotionGroupsResponseContent(LenientModel):
    """Response object for querying target promotion groups."""

    nextToken: str | None = Field(
        default=None,
        description="""
To retrieve the next page of results, call the same operation and specify this token in the
    request. If the nextToken field is empty, there are no further results.
""",
    )
    targetPromotionGroups: list[SponsoredProductsTargetPromotionGroup] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    totalResults: int | None = Field(default=None, description="The total number of results available.")


class SponsoredProductsListTargetPromotionGroupsV2RequestContent(StrictModel):
    """Request object for querying target promotion groups."""

    destinationAdGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000, description="The maximum number of results requested.")
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next or previous response page"
    )
    sourceAdGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    targetPromotionGroupIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)


class SponsoredProductsListTargetPromotionGroupsV2ResponseContent(LenientModel):
    """Response object for querying target promotion groups."""

    nextToken: str | None = Field(
        default=None,
        description="""
To retrieve the next page of results, call the same operation and specify this token in the
    request. If the nextToken field is empty, there are no further results.
""",
    )
    targetPromotionGroups: list[SponsoredProductsTargetPromotionGroupV2] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    totalResults: int | None = Field(default=None, description="The total number of results available.")


class SponsoredProductsNewAdGroup(StrictModel):
    adGroupName: str = Field(description="The name of the new ad group.")
    defaultBid: float = Field(
        ge=0,
        description="""
The default bid value that gets applied if no bid is provided for the target. For more information about bid constraints by marketplace,
    see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    targetingTypes: list[str] = Field(
        min_length=1,
        max_length=1,
        description="List of targeting types to be used for targets in the ad group. Supported types are KEYWORD and PRODUCT.",
    )


class SponsoredProductsNewCampaign(StrictModel):
    adGroups: list[SponsoredProductsNewAdGroup] = Field(
        min_length=1, max_length=1, description="List of ad groups to be created inside the new campaign."
    )
    budget: SponsoredProductsNewCampaignBudget
    campaignName: str = Field(description="The campaign name.")
    dynamicBidding: SponsoredProductsNewCampaignDynamicBidding | None = Field(default=None)
    endDate: date | None = Field(
        default=None,
        description="The end date of the new target promotion group entities. The format of the date is YYYY-MM-DD.",
    )
    startDate: date | None = Field(
        default=None,
        description="The start date of the new target promotion group entities. Default is today's date. The format of the date is YYYY-MM-DD.",
    )
    tags: SponsoredProductsTags | None = Field(default=None)


class SponsoredProductsNewCampaignBudget(StrictModel):
    """The budget for the campaigns in the target promotion group."""

    budget: float = Field(ge=0, description="The value of the budget.")
    budgetType: str = Field(description="DAILY.")


class SponsoredProductsNewCampaignDetails(StrictModel):
    """The request object for creating a new target promotion group with new campaigns."""

    budget: SponsoredProductsNewCampaignBudget
    defaultBid: float = Field(
        ge=0,
        description="The default bid value that gets applied if no bid is provided for the target. For more information about bid constraints by marketplace, see [bid limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).",
    )
    dynamicBidding: SponsoredProductsNewCampaignDynamicBidding | None = Field(default=None)
    endDate: date | None = Field(
        default=None,
        description="The end date of the new target promotion group entities. The format of the date is YYYY-MM-DD.",
    )
    namePrefix: str = Field(description="""
The name prefix to be used for the entities under the target promotion group. e.g. if the namePrefix
    is ABC, we will create a keyword campaign with the name 'ABC-ManualKeywordTargeting-Campaign-AutoGenerated'
""")
    startDate: date | None = Field(
        default=None,
        description="The start date of the new target promotion group entities. Default is today's date. The format of the date is YYYY-MM-DD.",
    )
    tags: SponsoredProductsTags | None = Field(default=None)


class SponsoredProductsNewCampaignDynamicBidding(StrictModel):
    """Specifies bidding controls."""

    placementBidding: list[SponsoredProductsNewCampaignPlacementBidding] | None = Field(
        default=None, min_length=0, max_length=3, description="The product placement."
    )
    strategy: str = Field(description="One of LEGACY_FOR_SALES, AUTO_FOR_SALES, MANUAL, RULE_BASED.")


class SponsoredProductsNewCampaignPlacementBidding(StrictModel):
    """The product placement."""

    percentage: int = Field(description="The bidding placement percentage.")
    placement: str = Field(
        description="The bidding placement. One of PLACEMENT_TOP, PLACEMENT_PRODUCT_PAGE, PLACEMENT_REST_OF_SEARCH."
    )


class SponsoredProductsProductTargetV2(LenientModel):
    """A product target."""

    destinationAdGroupId: str | None = Field(
        default=None, description="The adGroupId of the destination manual-targeting adGroup where the target belongs."
    )
    expressionType: str | None = Field(
        default=None, description="The the expression type (for PRODUCT). One of PRODUCT_EXACT, PRODUCT_SIMILAR"
    )
    target: str | None = Field(default=None, description="The product ASIN of the target.")
    targetId: str | None = Field(default=None, description="The id of the product target.")
    targetPromotionGroupId: str | None = Field(default=None, description="The id of the target promotion group.")


class SponsoredProductsRecommendationReason(LenientModel):
    """Provides a reason for why this target is being recommended for harvesting"""

    data: str | None = Field(default=None, description="The data supporting the recommendation reason")
    reason: str | None = Field(default=None, description="The reason for the recommendation")


class SponsoredProductsRecommendedTarget(LenientModel):
    adAsin: str | None = Field(default=None, description="The ASIN of the product being advertised")
    adGroupId: str | None = Field(
        default=None, description="The ID of an ad group for which the targets are recommended"
    )
    adId: str | None = Field(default=None, description="The ID of an ad for which the targets are recommended")
    campaignId: str | None = Field(
        default=None, description="The ID of a campaign for which the targets are recommended"
    )
    recommendationReasons: list[SponsoredProductsRecommendationReason] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="Provides a list of reasons for why this target is being recommended for harvesting",
    )
    recommendedTarget: str | None = Field(default=None, description="The keyword or ASIN that is being targeted")
    targetType: SponsoredProductsTargetType | str | None = Field(default=None)


class SponsoredProductsResponseAdGroup(LenientModel):
    """Ad groups where targets can be promoted."""

    adGroupId: str | None = Field(default=None, description="The id of the ad group in the campaign.")


class SponsoredProductsTarget(LenientModel):
    """Target promotion group's target."""

    expressionType: str | None = Field(
        default=None,
        description="""
The match type (for KEYWORDs) or the expression type (for PRODUCT). One of QUERY_BROAD_MATCHES,
    QUERY_EXACT_MATCHES, QUERY_PHRASE_MATCHES, ASIN_SAME_AS, ASIN_EXPANDED_FROM
""",
    )
    manualTargetingAdGroupId: str | None = Field(
        default=None, description="The adGroupId of the manual-targeting campaign where the target belongs."
    )
    target: str | None = Field(default=None, description="The keyword text or the product ASIN of the target.")
    targetId: str | None = Field(default=None, description="The id of the target.")
    targetPromotionGroupId: str | None = Field(default=None, description="The id of the target promotion group.")


class SponsoredProductsTargetPromotionGroup(LenientModel):
    """A Target Promotion Group that groups an Auto-Targeting Campaign/AdGroup with a Manual-Targeting Keyword Campaign/AdGroup, and a
    Manual-Targeting Product Campaign/AdGroup"""

    autoTargetingCampaignAdGroupId: str | None = Field(
        default=None, description="The Id of the auto-targeting AdGroup associated with the target promotion group"
    )
    autoTargetingCampaignAdIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="The list of Product Ad Ids in the Auto-Targeting campaign's Ad Group that's tied to the Target Promotion Group.",
    )
    keywordCampaignAdGroupIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The Ids of the manual keyword-targeting AdGroups associated with the target promotion group",
    )
    productCampaignAdGroupIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The Ids of the manual product-targeting AdGroups associated with the target promotion group",
    )
    state: str | None = Field(default=None, description="The state of the target promotion group.")
    targetPromotionGroupId: str | None = Field(default=None, description="The id of the target promotion group.")
    targetPromotionGroupName: str | None = Field(default=None, description="The name of the target promotion group.")


class SponsoredProductsTargetPromotionGroupTargetDetailsKeywordTargetDetailsV2(LenientModel):
    keywordTargetDetailsV2: SponsoredProductsKeywordTargetV2


class SponsoredProductsTargetPromotionGroupTargetDetailsProductTargetDetailsV2(LenientModel):
    productTargetDetailsV2: SponsoredProductsProductTargetV2


type SponsoredProductsTargetPromotionGroupTargetDetails = SponsoredProductsTargetPromotionGroupTargetDetailsKeywordTargetDetailsV2 | SponsoredProductsTargetPromotionGroupTargetDetailsProductTargetDetailsV2


class SponsoredProductsTargetPromotionGroupV2(LenientModel):
    """A Target Promotion Group that groups a source AdGroup with one or more destination Manual Keyword/Product Targeting AdGroup(s)"""

    adIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="The list of Product Ad Ids in the source Ad Group that's tied to the Target Promotion Group.",
    )
    destinationAdGroups: list[SponsoredProductsResponseAdGroup] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="The destination manual targeting AdGroups associated with the target promotion group.",
    )
    sourceAdGroupId: str | None = Field(
        default=None, description="The Id of the source AdGroup associated with the target promotion group"
    )
    sourceCampaignId: str | None = Field(
        default=None, description="The campaign Id of the source AdGroup associated with the target promotion group"
    )
    state: str | None = Field(default=None, description="The state of the target promotion group.")
    targetPromotionGroupId: str | None = Field(default=None, description="The id of the target promotion group.")
    targetPromotionGroupName: str | None = Field(default=None, description="The name of the target promotion group.")


__all__ = [
    "SponsoredProductsBiddingError",
    "SponsoredProductsBiddingErrorReason",
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsCreateKeywordTarget",
    "SponsoredProductsCreateProductTarget",
    "SponsoredProductsCreateTarget",
    "SponsoredProductsCreateTargetError",
    "SponsoredProductsCreateTargetErrorSelector",
    "SponsoredProductsCreateTargetPromotionGroupTargetsBatchError",
    "SponsoredProductsCreateTargetPromotionGroupTargetsBatchSuccess",
    "SponsoredProductsCreateTargetPromotionGroupTargetsFailureResponseItem",
    "SponsoredProductsCreateTargetPromotionGroupTargetsRequestContent",
    "SponsoredProductsCreateTargetPromotionGroupTargetsResponseContent",
    "SponsoredProductsCreateTargetPromotionGroupTargetsSuccessResponseItem",
    "SponsoredProductsCreateTargetPromotionGroupTargetsV2RequestContent",
    "SponsoredProductsCreateTargetPromotionGroupTargetsV2ResponseContent",
    "SponsoredProductsCreateTargetPromotionGroupsRequestContent",
    "SponsoredProductsCreateTargetPromotionGroupsResponseContent",
    "SponsoredProductsCreateTargetPromotionGroupsV2RequestContent",
    "SponsoredProductsCreateTargetPromotionGroupsV2ResponseContent",
    "SponsoredProductsCreateTargetRequest",
    "SponsoredProductsCreateTargetRequestV2",
    "SponsoredProductsDuplicateValueError",
    "SponsoredProductsDuplicateValueErrorReason",
    "SponsoredProductsEntityNotFoundError",
    "SponsoredProductsEntityNotFoundErrorReason",
    "SponsoredProductsEntityQuotaError",
    "SponsoredProductsEntityStateError",
    "SponsoredProductsEntityStateErrorReason",
    "SponsoredProductsEntityType",
    "SponsoredProductsError",
    "SponsoredProductsErrorCause",
    "SponsoredProductsExistingAdGroup",
    "SponsoredProductsExistingCampaignDetails",
    "SponsoredProductsExpressionTypeError",
    "SponsoredProductsExpressionTypeErrorReason",
    "SponsoredProductsGetTargetPromotionGroupsRecommendationsRequestContent",
    "SponsoredProductsGetTargetPromotionGroupsRecommendationsResponseContent",
    "SponsoredProductsInternalServerError",
    "SponsoredProductsInternalServerErrorReason",
    "SponsoredProductsInvalidInputError",
    "SponsoredProductsInvalidInputErrorReason",
    "SponsoredProductsKeywordMatchType",
    "SponsoredProductsKeywordTargetV2",
    "SponsoredProductsListTargetPromotionGroupTargetsRequestContent",
    "SponsoredProductsListTargetPromotionGroupTargetsResponseContent",
    "SponsoredProductsListTargetPromotionGroupTargetsV2RequestContent",
    "SponsoredProductsListTargetPromotionGroupTargetsV2ResponseContent",
    "SponsoredProductsListTargetPromotionGroupsRequestContent",
    "SponsoredProductsListTargetPromotionGroupsResponseContent",
    "SponsoredProductsListTargetPromotionGroupsV2RequestContent",
    "SponsoredProductsListTargetPromotionGroupsV2ResponseContent",
    "SponsoredProductsLocaleError",
    "SponsoredProductsLocaleErrorReason",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMissingValueError",
    "SponsoredProductsMissingValueErrorReason",
    "SponsoredProductsNewAdGroup",
    "SponsoredProductsNewCampaign",
    "SponsoredProductsNewCampaignBudget",
    "SponsoredProductsNewCampaignDetails",
    "SponsoredProductsNewCampaignDynamicBidding",
    "SponsoredProductsNewCampaignPlacementBidding",
    "SponsoredProductsObjectIdFilter",
    "SponsoredProductsOtherError",
    "SponsoredProductsOtherErrorReason",
    "SponsoredProductsParentEntityError",
    "SponsoredProductsParentEntityErrorReason",
    "SponsoredProductsProductTargetV2",
    "SponsoredProductsQuotaErrorReason",
    "SponsoredProductsQuotaScope",
    "SponsoredProductsRangeError",
    "SponsoredProductsRecommendationReason",
    "SponsoredProductsRecommendedTarget",
    "SponsoredProductsResponseAdGroup",
    "SponsoredProductsTags",
    "SponsoredProductsTarget",
    "SponsoredProductsTargetPromotionGroup",
    "SponsoredProductsTargetPromotionGroupTargetDetails",
    "SponsoredProductsTargetPromotionGroupV2",
    "SponsoredProductsTargetType",
    "SponsoredProductsTargetingClauseSetupError",
    "SponsoredProductsTargetingClauseSetupErrorReason",
    "SponsoredProductsTargetingExpressionMatchType",
    "SponsoredProductsThrottledError",
    "SponsoredProductsThrottledErrorReason",
    "SponsoredProductsValueLimitErrorReason",
]
