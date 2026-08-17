"""Auto-generated models for Campaigns from Amazon Ads API v0."""

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


class AudienceSegmentType(StrEnum):
    """
    The audience segment type is required to specify the type of audience being used to apply bid adjustments.
    """

    SPONSORED_ADS_AMC = "SPONSORED_ADS_AMC"  # This type refers to the Audience Segments created in AMC for Sponsored Ads. See [AMC API](https://advertising.amazon.com/API/docs/en-us/amc-rba#tag/Rule-based-audience) for details on how to create AMC Audiences. Once the AMC Audiences are created, the Audience Ids can be retrieved using the Discovery API [ListTargetableEntities](https://advertising.amazon.com/API/docs/en-us/targetable-entities#operation/ListTargetableEntities) with parameters; `adProduct`=`SPONSORED_BRANDS`, `targetTypeFilter`=`AUDIENCE` and `pathsFilter` = `[["Audience Category", "Custom-built", "AMC"]]`. Only the audiences retrieved using these filters are usable.
    BEHAVIOR_DYNAMIC = "BEHAVIOR_DYNAMIC"  # This type refers to the Audience Segments created by Amazon for Sponsored Ads. The Audience Ids can be retrieved using the Discovery API [ListTargetableEntities](https://advertising.amazon.com/API/docs/en-us/targetable-entities#operation/ListTargetableEntities) with parameters; `adProduct`=`SPONSORED_BRANDS`, `targetTypeFilter`=`AUDIENCE` and `pathsFilter` = `[["Audience Category", "Custom-built", "Product"]]`. Only the audiences retrieved using these filters are usable.


class BudgetType(StrEnum):
    """
    For the lifetime budget type, `startDate` and `endDate` must be specified.
    """

    DAILY = "DAILY"
    LIFETIME = "LIFETIME"


class CampaignServingStatus(StrEnum):
    """
    `Notice: the servingStatus enums have not been finalized yet.`
    The campaign serving status determined by system.
    - ADVERTISER_STATUS_ENABLED - Advertiser's status is enabled
    - ADVERTISER_POLICING_PENDING_REVIEW - Avertiser is pending review because of policing reason
    - ADVERTISER_POLICING_SUSPENDED - Advertiser's status is suspended because of policing reason
    - ADVERTISER_PAUSED - Advertiser's status is paused
    - ADVERTISER_ARCHIVED - Advertiser's status is archived
    - ADVERTISER_PAYMENT_FAILURE - Advertiser's internal status is suspended
    - ADVERTISER_ACCOUNT_OUT_OF_BUDGET - Advertiser is out of budget for all Sponsored Ads campaigns
    - ADVERTISER_OUT_OF_PREPAY_BALANCE - Advertiser is out of prepay balance for all Sponsored Ads campaigns
    - ADVERTISER_EXCEED_SPENDS_LIMIT - Advertiser spends over the daily limit

    - CAMPAIGN_STATUS_ENABLED - Campaign's status is enabled.
    - CAMPAIGN_PAUSED - Campaign's status is paused.
    - CAMPAIGN_ARCHIVED - Campaign's status is archived.
    - CAMPAIGN_INCOMPLETE - Campaign does not contain any ads or targeting clauses.
    - CAMPAIGN_OUT_OF_BUDGET - Campaign is out of budget.

    - PORTFOLIO_STATUS_ENABLED - Portfolio's status is enabled
    - PORTFOLIO_PAUSED - Portfolio's status is paused
    - PORTFOLIO_ARCHIVED - Portfolio's status is archived
    - PORTFOLIO_OUT_OF_BUDGET - Portfolio is out of budget
    - PORTFOLIO_PENDING_START_DATE - Portfolio's start date is in the future
    - PORTFOLIO_ENDED - Portfolio's end date is in the past.

    - INELIGIBLE - Ad Offer is ineligible
    - ELIGIBLE - Ad Offer is eligible
    - ENDED - Campaign's end date is in the past.
    - PENDING_REVIEW - Campaign is pending review.
    - PENDING_START_DATE - Campaign's start date is in the future.
    - REJECTED - Campaign is rejected by moderation process.
    - UNKNOWN - Serving status is unknown. Please contact us for support.
    """

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


class Placement(StrEnum):
    """
    List of bid adjustments for placements.
    - HOME - The home page of the Amazon store.
    - DETAIL_PAGE - Product detail pages within the Amazon store.
    - OTHER - Other placement groups. Such as search pages in the Amazon Store.
    - TOP_OF_SEARCH - Top of search ads generally appear above the top search results.
    """

    HOME = "HOME"
    DETAIL_PAGE = "DETAIL_PAGE"
    OTHER = "OTHER"
    TOP_OF_SEARCH = "TOP_OF_SEARCH"


class ProductLocation(StrEnum):
    """
    The product location of the campaign.
    - SOLD_ON_AMAZON - For products sold on Amazon websites.
    - NOT_SOLD_ON_AMAZON - For products not sold on Amazon websites.
    - SOLD_ON_DTC - Deprecated (For products sold on DTC websites).
    """

    SOLD_ON_AMAZON = "SOLD_ON_AMAZON"
    NOT_SOLD_ON_AMAZON = "NOT_SOLD_ON_AMAZON"
    SOLD_ON_DTC = "SOLD_ON_DTC"


class ShopperCohortType(StrEnum):
    """
    The shopper cohort type. The shopperCohortType is required to specify the type of shopper cohort used to apply bid adjustments. Currently only "AUDIENCE_SEGMENT" is supported.
    """

    AUDIENCE_SEGMENT = "AUDIENCE_SEGMENT"


class SiteRestriction(StrEnum):
    AMAZON_BUSINESS = "AMAZON_BUSINESS"


class AudienceSegment(StrictModel):
    audienceId: str | None = Field(default=None)
    audienceSegmentType: Annotated[AudienceSegmentType, lenient_enum(AudienceSegmentType)] | None = Field(default=None)


class AudienceSegmentOut(LenientModel):
    audienceId: str | None = Field(default=None)
    audienceSegmentType: Annotated[AudienceSegmentType | str, lenient_enum(AudienceSegmentType)] | None = Field(
        default=None
    )


class BidAdjustmentByPlacement(StrictModel):
    percentage: float | None = Field(default=None, ge=-99, le=900)
    placement: Annotated[Placement, lenient_enum(Placement)] | None = Field(default=None)


class BidAdjustmentByPlacementOut(LenientModel):
    percentage: float | None = Field(default=None, ge=-99, le=900)
    placement: Annotated[Placement | str, lenient_enum(Placement)] | None = Field(default=None)


class Bidding(StrictModel):
    bidOptimization: bool | None = Field(
        default=None,
        description="""
Whether to use automatic placement level bid optimization. If set to true, Amazon will automatically set the right placement adjustment and the bidAdjustmentsByPlacement field is ignored. If set to false, the bidAdjustmentsByPlacement field will be used to adjust bid on different placements.
If this field is changed from false to true, the bidAdjustmentsByPlacement field will be reset to null.
""",
    )
    shopperCohortBidAdjustments: list[ShopperCohortBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Shopper cohort based bid adjustments."
    )
    bidAdjustmentsByPlacement: list[BidAdjustmentByPlacement] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="Placement level bid adjustment. Note that this field can only be set when 'bidOptimization' is set to false.",
    )


class BiddingOut(LenientModel):
    bidOptimization: bool | None = Field(
        default=None,
        description="""
Whether to use automatic placement level bid optimization. If set to true, Amazon will automatically set the right placement adjustment and the bidAdjustmentsByPlacement field is ignored. If set to false, the bidAdjustmentsByPlacement field will be used to adjust bid on different placements.
If this field is changed from false to true, the bidAdjustmentsByPlacement field will be reset to null.
""",
    )
    shopperCohortBidAdjustments: list[ShopperCohortBidAdjustmentOut] | None = Field(
        default=None, min_length=0, max_length=1, description="Shopper cohort based bid adjustments."
    )
    bidAdjustmentsByPlacement: list[BidAdjustmentByPlacementOut] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="Placement level bid adjustment. Note that this field can only be set when 'bidOptimization' is set to false.",
    )


class BillingError(LenientModel):
    """Errors related to billing."""

    reason: str = Field(description="Exact error reason.")
    cause: ErrorCause
    message: str = Field(description="Human readable error message.")


class BudgetError(LenientModel):
    reason: str
    cause: ErrorCause
    upperLimit: str | None = Field(default=None)
    lowerLimit: str | None = Field(default=None)
    message: str = Field(description="Human readable error message.")


class BulkCampaignOperationResponse(LenientModel):
    success: list[CampaignMutationSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    error: list[CampaignMutationFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class Campaign(LenientModel):
    budgetType: Annotated[BudgetType | str, lenient_enum(BudgetType)]
    ruleBasedBudget: RuleBasedBudget | None = Field(default=None)
    brandEntityId: str | None = Field(default=None)
    isMultiAdGroupsEnabled: bool | None = Field(default=None)
    goal: str | None = Field(
        default=None,
        description="""
Goal will allow you to set goal type to help drive your campaign performance. If no goal is selected then it will default to PAGE_VISIT.
The goal type of the campaign.
- BRAND_IMPRESSION_SHARE - This goal will allow you grown your brand impression share on top of search placements
- PAGE_VISIT [DEFAULT] - This goal drives traffic to your landing and detail pages through all placements
- ACQUIRE_NEW_CUSTOMERS - This property is a PREVIEW ONLY and cannot be used as part of a request or response. This goal drives new customer acquisition for your brands.
- AD_VIEWS - This property is a PREVIEW ONLY and cannot be used as part of a request or response. This goal maximizes view for your ads.
""",
    )
    bidding: BiddingOut | None = Field(default=None)
    endDate: str | None = Field(
        default=None,
        pattern="^20[1-9][0-9]-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$",
        description="The format of the date is YYYY-MM-DD.",
    )
    campaignId: str = Field(description="The identifier of the campaign.")
    productLocation: Annotated[ProductLocation | str, lenient_enum(ProductLocation)] | None = Field(default=None)
    tags: TagsOut | None = Field(default=None)
    portfolioId: str | None = Field(
        default=None, description="The identifier of an existing portfolio to which the campaign is associated."
    )
    costType: str | None = Field(
        default=None,
        description="""
The costType can be set to determines how the campaign will bid and charge. To view the bid maximums and minimums by geography and costType, see https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace
- CPC [Default] - Cost per click. The performance of this campaign is measured by the clicks triggered by the ad.
- VCPM - Cost per 1000 viewable impressions. The performance of this campaign is measured by the viewable impressions triggered by the ad.
- FIXED_PRICE - Sale price for a specific ad placement. It can only be used for campaign with a targetedPGDealId.
""",
    )
    smartDefault: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="""
The smartDefault specifies a list of the smart default options for the campaign.

`smartDefault` is optional for create campaign requests. `smartDefault` are applicable to all applicable child entities of the campaign and are not editable once the campaign is created. When using ["TARGETING"], targets will be automatically added based on the goal selected.  When ["MANUAL"] is selected, you will still be required to manually add targets.

If you don't specify `smartDefault`, default value will be applied based on `goal` . If campaign's `goal` is selected, `smartDefault` will be set to ["TARGETING"].  Otherwise, a campaign's `smartDefault` will be set to ["MANUAL"].

Each element in smartDefault can be set to determines which default strategy to be used
- MANUAL - Manual settings, no smart default be applied to the campaign, if MANUAL is added in the list, no other items are allowed in the list (the list must contains only one item)
- TARGETING - Smart Default Targeting creation, will automatically creating targetings when create ad group

Example: ["TARGETING"]
""",
    )
    siteRestrictions: list[Annotated[SiteRestriction | str, lenient_enum(SiteRestriction)]] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
Restrict the ad to a particular site. siteRestrictions is an optional field.  If this field is not set, ads from the campaign will appear on Amazon - including both Amazon retail and Amazon Business.
Please note that:
1) AMAZON_BUSINESS option is only available for Amazon Business operated marketplaces (US, CA, MX, UK, DE, FR, IT, ES, IN, JP, AU);
2) siteRestrictions cannot be changed post campaign creation;
3) siteRestrictions doesn't support shopperCohortBidding setting.
""",
    )
    name: str = Field(min_length=1, max_length=128, description="The name of the campaign.")
    state: Annotated[EntityState | str, lenient_enum(EntityState)]
    startDate: str | None = Field(
        default=None,
        pattern="^20[1-9][0-9]-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$",
        description="The format of the date is YYYY-MM-DD.",
    )
    budget: float
    extendedData: CampaignExtendedData | None = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId associated with the campaign. This field is immutable and cannot be changed after the campaign is created.",
    )


class CampaignExtendedData(LenientModel):
    """CampaignExtendedData can only be retrieved via the list API. It won't be available in the response during update/create."""

    servingStatus: Annotated[CampaignServingStatus | str, lenient_enum(CampaignServingStatus)] | None = Field(
        default=None
    )
    lastUpdateDate: float | None = Field(default=None, description="Date of last update in epoch time.")
    servingStatusDetails: list[str] | None = Field(
        default=None, min_length=0, max_length=100, description="The serving status reasons of the Campaign."
    )
    creationDate: float | None = Field(default=None, description="Creation date in epoch time.")


class CampaignMutationError(LenientModel):
    errorType: str = Field(description="The type of the error.")
    errorValue: CampaignMutationErrorSelector


class CampaignMutationErrorSelector(LenientModel):
    dateError: DateError | None = Field(default=None)
    biddingError: BiddingError | None = Field(default=None)
    budgetError: BudgetError | None = Field(default=None)
    billingError: BillingError | None = Field(default=None)
    rangeError: RangeError | None = Field(default=None)
    otherError: OtherError | None = Field(default=None)


class CampaignMutationFailureResponseItem(LenientModel):
    index: float = Field(ge=0, le=10, description="the index of the campaign in the array from the request body.")
    errors: list[CampaignMutationError] | None = Field(
        default=None, min_length=0, max_length=100, description="A list of validation errors."
    )


class CampaignMutationSuccessResponseItem(LenientModel):
    campaignId: str | None = Field(default=None, description="The campaign ID.")
    index: float = Field(ge=0, le=10, description="The index of the campaign in the array from the request body.")
    campaign: Campaign | None = Field(default=None)


class CreateCampaign(StrictModel):
    budgetType: Annotated[BudgetType, lenient_enum(BudgetType)]
    brandEntityId: str | None = Field(
        default=None,
        description="Please note that brandEntityId is only required for sellers. You can get the brandEntityId by calling the [GET /brands](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Brands/operation/getBrands) endpoint.",
    )
    goal: str | None = Field(
        default=None,
        description="""
Goal will allow you to set goal type to help drive your campaign performance. If no goal is selected then it will default to PAGE_VISIT.
The goal type of the campaign.
- BRAND_IMPRESSION_SHARE - This goal will allow you grown your brand impression share on top of search placement
- PAGE_VISIT [DEFAULT] - This goal drives traffic to your landing and detail pages through all placements.
""",
    )
    bidding: Bidding | None = Field(default=None)
    endDate: str | None = Field(
        default=None,
        pattern="^20[1-9][0-9]-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$",
        description="endDate is optional. If endDate is specified, startDate must be specified as well.",
    )
    productLocation: Annotated[ProductLocation, lenient_enum(ProductLocation)] | None = Field(default=None)
    tags: Tags | None = Field(default=None)
    portfolioId: str | None = Field(
        default=None, description="The identifier of an existing portfolio to which the campaign is associated."
    )
    costType: str | None = Field(
        default=None,
        description="""
The costType can be set to determines how the campaign will bid and charge. To view the bid maximums and minimums by geography and costType, see https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace
- CPC [Default] - Cost per click. The performance of this campaign is measured by the clicks triggered by the ad.
- VCPM - Cost per 1000 viewable impressions. The performance of this campaign is measured by the viewable impressions triggered by the ad.
- FIXED_PRICE - Sale price for a specific ad placement. It can only be used for campaign with a targetedPGDealId.
""",
    )
    smartDefault: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="""
The smartDefault specifies a list of the smart default options for the campaign.

`smartDefault` is optional for create campaign requests. `smartDefault` are applicable to all applicable child entities of the campaign and are not editable once the campaign is created. When using ["TARGETING"], targets will be automatically added based on the goal selected.  When ["MANUAL"] is selected, you will still be required to manually add targets.

If you don't specify `smartDefault`, default value will be applied based on `goal` . If campaign's `goal` is selected, `smartDefault` will be set to ["TARGETING"].  Otherwise, a campaign's `smartDefault` will be set to ["MANUAL"].

Each element in smartDefault can be set to determines which default strategy to be used
- MANUAL - Manual settings, no smart default be applied to the campaign, if MANUAL is added in the list, no other items are allowed in the list (the list must contains only one item)
- TARGETING - Smart Default Targeting creation, will automatically creating targetings when create ad group

Example: ["TARGETING"]
""",
    )
    name: str = Field(min_length=1, max_length=128, description="The name of the campaign.")
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)]
    startDate: str | None = Field(
        default=None,
        pattern="^20[1-9][0-9]-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$",
        description="startDate is optional. If startDate is not specified, current date will be used.",
    )
    budget: float = Field(description="The budget of the campaign.")
    siteRestrictions: list[Annotated[SiteRestriction, lenient_enum(SiteRestriction)]] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
Restrict the ad to a particular site. siteRestrictions is an optional field.  If this field is not set, ads from the campaign will appear on Amazon - including both Amazon retail and Amazon Business.
Please note that:
1) AMAZON_BUSINESS option is only available for Amazon Business operated marketplaces (US, CA, MX, UK, DE, FR, IT, ES, IN, JP, AU);
2) siteRestrictions cannot be changed post campaign creation;
3) siteRestrictions doesn't support shopperCohortBidding setting.
""",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class CreateSponsoredBrandsCampaignsRequestContent(StrictModel):
    campaigns: list[CreateCampaign] = Field(min_length=1, max_length=10)


class CreateSponsoredBrandsCampaignsResponseContent(LenientModel):
    campaigns: BulkCampaignOperationResponse | None = Field(default=None)


class DeleteSponsoredBrandsCampaignsRequestContent(StrictModel):
    campaignIdFilter: ObjectIdFilter | None = Field(default=None)


class DeleteSponsoredBrandsCampaignsResponseContent(LenientModel):
    campaigns: BulkCampaignOperationResponse | None = Field(default=None)


class GoalTypeFilter(StrictModel):
    """Filter entities by goal type."""

    include: list[str] | None = Field(default=None, min_length=0, max_length=100)


class ListSponsoredBrandsCampaignsRequestContent(StrictModel):
    campaignIdFilter: ObjectIdFilter | None = Field(default=None)
    portfolioIdFilter: ObjectIdFilter | None = Field(default=None)
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
    goalTypeFilter: GoalTypeFilter | None = Field(default=None)
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="Setting to true will slow down performance because the API needs to retrieve extra information for each campaign.",
    )
    nameFilter: NameFilter | None = Field(default=None)


class ListSponsoredBrandsCampaignsResponseContent(LenientModel):
    campaigns: list[Campaign] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    totalCount: float | None = Field(default=None, description="The total number of entities.")


class RuleBasedBudget(LenientModel):
    isProcessing: bool | None = Field(default=None)
    applicableRuleName: str | None = Field(default=None)
    value: float | None = Field(default=None)
    applicableRuleId: str | None = Field(default=None)


class ShopperCohortBidAdjustment(StrictModel):
    shopperCohortType: Annotated[ShopperCohortType, lenient_enum(ShopperCohortType)] | None = Field(default=None)
    percentage: float | None = Field(default=None, ge=0, le=900)
    audienceSegments: list[AudienceSegment] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description='Required when "AUDIENCE_SEGMENT" is used for shopperCohortType.',
    )


class ShopperCohortBidAdjustmentOut(LenientModel):
    shopperCohortType: Annotated[ShopperCohortType | str, lenient_enum(ShopperCohortType)] | None = Field(default=None)
    percentage: float | None = Field(default=None, ge=0, le=900)
    audienceSegments: list[AudienceSegmentOut] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description='Required when "AUDIENCE_SEGMENT" is used for shopperCohortType.',
    )


class Tags(StrictModel):
    """A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You can specify a maximum of 50 identifiers."""

    pass


class TagsOut(LenientModel):
    """A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You can specify a maximum of 50 identifiers."""

    pass


class UpdateCampaign(StrictModel):
    portfolioId: str | None = Field(
        default=None, description="The identifier of an existing portfolio to which the campaign is associated."
    )
    bidding: Bidding | None = Field(default=None)
    endDate: str | None = Field(
        default=None,
        pattern="^20[1-9][0-9]-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$",
        description="endDate is optional. If endDate is specified, startDate must be specified as well. Note: This property is nullable. If null is explicitly provided in a campaign update request, any existing endDate for the campaign will be removed.",
    )
    campaignId: str = Field(description="The identifier of the campaign.")
    name: str | None = Field(default=None, min_length=1, max_length=128, description="The name of the campaign.")
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)] | None = Field(default=None)
    startDate: str | None = Field(
        default=None,
        pattern="^20[1-9][0-9]-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$",
        description="startDate can only be changed if the current startDate is in the future.",
    )
    budget: float | None = Field(
        default=None,
        description="The budget of the campaign. See https://advertising.amazon.com/help?entityId=ENTITYJDATFOIA05Q7#GE5QEBS6QRJJAT3A",
    )
    tags: Tags | None = Field(default=None)


class UpdateSponsoredBrandsCampaignsRequestContent(StrictModel):
    campaigns: list[UpdateCampaign] = Field(min_length=1, max_length=10)


class UpdateSponsoredBrandsCampaignsResponseContent(LenientModel):
    campaigns: BulkCampaignOperationResponse | None = Field(default=None)


__all__ = [
    "AudienceSegment",
    "AudienceSegmentOut",
    "AudienceSegmentType",
    "BidAdjustmentByPlacement",
    "BidAdjustmentByPlacementOut",
    "Bidding",
    "BiddingError",
    "BiddingOut",
    "BillingError",
    "BudgetError",
    "BudgetType",
    "BulkCampaignOperationResponse",
    "Campaign",
    "CampaignExtendedData",
    "CampaignMutationError",
    "CampaignMutationErrorSelector",
    "CampaignMutationFailureResponseItem",
    "CampaignMutationSuccessResponseItem",
    "CampaignServingStatus",
    "CreateCampaign",
    "CreateOrUpdateEntityState",
    "CreateSponsoredBrandsCampaignsRequestContent",
    "CreateSponsoredBrandsCampaignsResponseContent",
    "DateError",
    "DeleteSponsoredBrandsCampaignsRequestContent",
    "DeleteSponsoredBrandsCampaignsResponseContent",
    "EntityState",
    "EntityStateFilter",
    "ErrorCause",
    "GoalTypeFilter",
    "ListSponsoredBrandsCampaignsRequestContent",
    "ListSponsoredBrandsCampaignsResponseContent",
    "NameFilter",
    "ObjectIdFilter",
    "OtherError",
    "Placement",
    "ProductLocation",
    "QueryTermMatchType",
    "RangeError",
    "RuleBasedBudget",
    "ShopperCohortBidAdjustment",
    "ShopperCohortBidAdjustmentOut",
    "ShopperCohortType",
    "SiteRestriction",
    "Tags",
    "TagsOut",
    "UpdateCampaign",
    "UpdateSponsoredBrandsCampaignsRequestContent",
    "UpdateSponsoredBrandsCampaignsResponseContent",
]
