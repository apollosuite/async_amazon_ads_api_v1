"""Auto-generated models for Campaigns from Amazon Ads API v0."""

from __future__ import annotations

from datetime import date, datetime
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
    SponsoredProductsTags,
    SponsoredProductsTargetingType,
    SponsoredProductsThrottledError,
    SponsoredProductsThrottledErrorReason,
    SponsoredProductsValueLimitErrorReason,
)


class SponsoredProductsAudienceSegmentType(StrEnum):
    """
    DEPRECATED: This field is no longer used and any provided value will be ignored. The audience type is automatically determined via the Discovery API [ListTargetableEntities](https://advertising.amazon.com/API/docs/en-us/targetable-entities#operation/ListTargetableEntities) by examining the Audience path. Audience IDs are guaranteed to be unique across all audience types, enabling this inference.
    """

    BEHAVIOR_DYNAMIC = "BEHAVIOR_DYNAMIC"  # This type refers to the Audience Segments created by Amazon for Sponsored Ads. The Audience Ids can be retrieved using the Discovery API [ListTargetableEntities](https://advertising.amazon.com/API/docs/en-us/targetable-entities#operation/ListTargetableEntities) with parameters; `adProduct`=`SPONSORED_PRODUCTS`, `targetTypeFilter`=`AUDIENCE` and `pathsFilter` = `[["Audience Category", "Custom-built", "Product"]]`. Only the audiences retrieved using these filters are usable.
    SPONSORED_ADS_AMC = "SPONSORED_ADS_AMC"  # This type refers to the Audience Segments created in AMC for Sponsored Ads. See [AMC API](https://advertising.amazon.com/API/docs/en-us/amc-rba#tag/Rule-based-audience) for details on how to create AMC Audiences. Once the AMC Audiences are created, the Audience Ids can be retrieved using the Discovery API [ListTargetableEntities](https://advertising.amazon.com/API/docs/en-us/targetable-entities#operation/ListTargetableEntities) with parameters; `adProduct`=`SPONSORED_PRODUCTS`, `targetTypeFilter`=`AUDIENCE` and `pathsFilter` = `[["Audience Category", "Custom-built", "AMC"]]`. Only the audiences retrieved using these filters are usable.


class SponsoredProductsBiddingStrategy(StrEnum):
    """
    The bidding strategy.
    """

    AUTO_FOR_SALES = "AUTO_FOR_SALES"  # Dynamic bids - up and down | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.
    LEGACY_FOR_SALES = "LEGACY_FOR_SALES"  # Dynamic bids - down only | Lowers your bids in real time when your ad may be less likely to convert to a sale. Campaigns created before the release of the bidding controls feature used this setting by default.
    MANUAL = "MANUAL"  # Fixed bid | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
    OTHER = "OTHER"
    RULE_BASED = "RULE_BASED"  # Rule based bidding | See Rule based bidding documentation https://advertising.amazon.com/API/docs/en-us/sponsored-products/rule-based-bidding/overview


class SponsoredProductsBudgetErrorReason(StrEnum):
    BUDGETING_POLICY_INVALID = "BUDGETING_POLICY_INVALID"
    BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS = "BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS"
    BUDGET_LT_DEFAULT_BIDS = "BUDGET_LT_DEFAULT_BIDS"
    BUDGET_LT_KEYWORD_BIDS = "BUDGET_LT_KEYWORD_BIDS"
    BUDGET_LT_PREDEFINED_TARGET_BIDS = "BUDGET_LT_PREDEFINED_TARGET_BIDS"
    BUDGET_OUT_OF_MARKET_PLACE_RANGE = "BUDGET_OUT_OF_MARKET_PLACE_RANGE"
    BUDGET_TOO_HIGH = "BUDGET_TOO_HIGH"
    BUDGET_TOO_LOW = "BUDGET_TOO_LOW"
    MISSING_BUDGETING_POLICY = "MISSING_BUDGETING_POLICY"
    MISSING_IN_BUDGET_FLAG = "MISSING_IN_BUDGET_FLAG"


class SponsoredProductsBudgetType(StrEnum):
    DAILY = "DAILY"
    OTHER = "OTHER"


class SponsoredProductsCampaignServingStatus(StrEnum):
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
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


class SponsoredProductsCampaignServingStatusReason(StrEnum):
    ACCOUNT_OUT_OF_BUDGET_DETAIL = "ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL = "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    ADVERTISER_POLICING_PENDING_REVIEW_DETAIL = "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL"
    ADVERTISER_POLICING_SUSPENDED_DETAIL = "ADVERTISER_POLICING_SUSPENDED_DETAIL"
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


class SponsoredProductsCreateOrUpdateBiddingStrategy(StrEnum):
    """
    The bidding strategy.
    `strategy` is required for create requests if dynamicBidding is provided, but is optional for update requests.
    """

    AUTO_FOR_SALES = "AUTO_FOR_SALES"  # Dynamic bids - up and down | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.
    LEGACY_FOR_SALES = "LEGACY_FOR_SALES"  # Dynamic bids - down only | Lowers your bids in real time when your ad may be less likely to convert to a sale. Campaigns created before the release of the bidding controls feature used this setting by default.
    MANUAL = "MANUAL"  # Fixed bid | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
    RULE_BASED = "RULE_BASED"  # Rule based bidding | See Rule based bidding documentation https://advertising.amazon.com/API/docs/en-us/sponsored-products/rule-based-bidding/overview


class SponsoredProductsCreateOrUpdateBudgetType(StrEnum):
    DAILY = "DAILY"


class SponsoredProductsCreateOrUpdateOffAmazonBudgetControlStrategy(StrEnum):
    """
    The budget control strategy for ads served off Amazon . `OffAmazonBudgetControlStrategy` is optional for create and update requests.
    Value |  Description |
    """

    MAXIMIZE_REACH = "MAXIMIZE_REACH"  # Prioritize more reach using your target settings. This setting may result in more impressions and opportunities for sales off Amazon.
    MINIMIZE_SPEND = "MINIMIZE_SPEND"  # Optimize ad delivery to minimize spending. This setting may result in fewer impressions off Amazon, but it can help control spend.


class SponsoredProductsCurrencyErrorReason(StrEnum):
    CANNOT_UPDATE_CURRENCY = "CANNOT_UPDATE_CURRENCY"
    CURRENCY_NOT_MATCHING_PREFERRED_CURRENCY = "CURRENCY_NOT_MATCHING_PREFERRED_CURRENCY"
    CURRENCY_NOT_SUPPORTED = "CURRENCY_NOT_SUPPORTED"
    PREFERRED_CURRENCY_NOT_SET = "PREFERRED_CURRENCY_NOT_SET"


class SponsoredProductsDateErrorReason(StrEnum):
    END_DATE_EARLIER_THAN_TODAY = "END_DATE_EARLIER_THAN_TODAY"
    END_DATE_LATER_THAN_MAXIMUM = "END_DATE_LATER_THAN_MAXIMUM"
    INVALID_DATE = "INVALID_DATE"
    START_DATE_AFTER_END_DATE = "START_DATE_AFTER_END_DATE"
    START_DATE_EARLIER_THAN_TODAY = "START_DATE_EARLIER_THAN_TODAY"
    START_DATE_LATER_THAN_MAXIMUM = "START_DATE_LATER_THAN_MAXIMUM"
    UPDATING_ENDED_CAMPAIGN_WITHOUT_EXTENSION = "UPDATING_ENDED_CAMPAIGN_WITHOUT_EXTENSION"
    UPDATING_READ_ONLY_END_DATE = "UPDATING_READ_ONLY_END_DATE"
    UPDATING_READ_ONLY_START_DATE = "UPDATING_READ_ONLY_START_DATE"


class SponsoredProductsMarketplaceBudgetAllocation(StrEnum):
    """
    Setting for distribution of global budget into marketplaces in global campaign.
    """

    AUTO = "AUTO"  # Auto distribute global budget to marketplaces in global campaign. Budget updates for marketplaces are not allowed for AUTO campaigns. The budget can only be updated in global campaign for AUTO campaigns.
    MANUAL = "MANUAL"  # Manually distribute global budget to marketplaces in global campaign.


class SponsoredProductsOffAmazonBudgetControlStrategy(StrEnum):
    MAXIMIZE_REACH = "MAXIMIZE_REACH"
    MINIMIZE_SPEND = "MINIMIZE_SPEND"


class SponsoredProductsPlacement(StrEnum):
    """
    You can enable controls to adjust your bid based on the placement location. Specify a location where you want to use bid controls. The percentage value set is the percentage of the original bid for which you want to have your bid adjustment increased. For example, a 50% Top of Search adjustment on a $1.00 bid would increase the bid to $1.50 for the opportunity to win a Top of Search placement. A further 100% Amazon Business adjustment would increase the bid to $3.00 for the Amazon Business Top of Search placement and to $2.00 for all other Amazon Business placements.
    The Amazon Business Bid Adjustment and Reporting for Sponsored Products will be coming soon to Bulksheets.
    """

    PLACEMENT_PRODUCT_PAGE = "PLACEMENT_PRODUCT_PAGE"  # Product pages
    PLACEMENT_REST_OF_SEARCH = "PLACEMENT_REST_OF_SEARCH"  # Rest of the search
    PLACEMENT_TOP = "PLACEMENT_TOP"  # Top of search (first page)
    SITE_AMAZON_BUSINESS = "SITE_AMAZON_BUSINESS"  # Site Amazon Business


class SponsoredProductsShopperCohortType(StrEnum):
    """
    This field specifies the type of shopper cohort used to apply bid adjustments. `AUDIENCE_SEGMENT` is the only supported type currently.
    """

    AUDIENCE_SEGMENT = "AUDIENCE_SEGMENT"  # A predefined list of the shopper ids.


class SponsoredProductsSiteRestriction(StrEnum):
    """
    Restrict the ad to a particular site.
    If the value is absent (ie null), it means no site restrictions and defaults to current Sponsored Products campaign behavior.
    This field is coming up and is not ready for use at the moment.
    """

    AMAZON_BUSINESS = "AMAZON_BUSINESS"  # Restrict the ad to only show on Amazon Business.
    AMAZON_HAUL = "AMAZON_HAUL"  # Restrict the ad to only show on Amazon Haul.


class SponsoredProductsAudienceSegment(StrictModel):
    audienceId: str = Field(
        min_length=1, max_length=20, description="`audienceId` is specified based on the `audienceSegmentType` used."
    )
    audienceSegmentType: (
        Annotated[SponsoredProductsAudienceSegmentType | str, lenient_enum(SponsoredProductsAudienceSegmentType)] | None
    ) = Field(default=None)


class SponsoredProductsAudienceSegmentOut(LenientModel):
    audienceId: str = Field(
        min_length=1, max_length=20, description="`audienceId` is specified based on the `audienceSegmentType` used."
    )
    audienceSegmentType: (
        Annotated[SponsoredProductsAudienceSegmentType | str, lenient_enum(SponsoredProductsAudienceSegmentType)] | None
    ) = Field(default=None)


class SponsoredProductsBudget(LenientModel):
    budget: float = Field(description="Monetary value")
    budgetType: Annotated[SponsoredProductsBudgetType | str, lenient_enum(SponsoredProductsBudgetType)]
    effectiveBudget: float | None = Field(default=None, description="Monetary value")


class SponsoredProductsBudgetError(LenientModel):
    cause: SponsoredProductsErrorCause | None = Field(default=None)
    lowerLimit: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[SponsoredProductsBudgetErrorReason | str, lenient_enum(SponsoredProductsBudgetErrorReason)]
    upperLimit: str | None = Field(default=None)


class SponsoredProductsBulkCampaignOperationResponse(LenientModel):
    error: list[SponsoredProductsCampaignMutationFailureResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    success: list[SponsoredProductsCampaignMutationSuccessResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SponsoredProductsCampaign(LenientModel):
    autoManageCampaign: bool | None = Field(default=None)
    budget: SponsoredProductsBudget
    campaignId: str = Field(description="The identifier of the campaign.")
    dynamicBidding: SponsoredProductsDynamicBidding | None = Field(default=None)
    endDate: date | None = Field(default=None, description="The format of the date is YYYY-MM-DD.")
    extendedData: SponsoredProductsCampaignExtendedData | None = Field(default=None)
    globalCampaignId: str | None = Field(
        default=None, description="The global campaign identifier that manages this marketplace campaign."
    )
    marketplaceBudgetAllocation: (
        Annotated[
            SponsoredProductsMarketplaceBudgetAllocation | str,
            lenient_enum(SponsoredProductsMarketplaceBudgetAllocation),
        ]
        | None
    ) = Field(default=None)
    name: str = Field(description="The name of the campaign.")
    offAmazonSettings: SponsoredProductsOffAmazonSettings | None = Field(default=None)
    portfolioId: str | None = Field(
        default=None, description="The identifier of an existing portfolio to which the campaign is associated."
    )
    siteRestrictions: (
        list[Annotated[SponsoredProductsSiteRestriction | str, lenient_enum(SponsoredProductsSiteRestriction)]] | None
    ) = Field(default=None, min_length=1, max_length=1)
    startDate: date = Field(description="The format of the date is YYYY-MM-DD.")
    state: Annotated[SponsoredProductsEntityState | str, lenient_enum(SponsoredProductsEntityState)]
    tags: SponsoredProductsTagsOut | None = Field(default=None)
    targetingType: Annotated[SponsoredProductsTargetingType | str, lenient_enum(SponsoredProductsTargetingType)]


class SponsoredProductsCampaignExtendedData(LenientModel):
    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Last updated date in ISO 8601.")
    servingStatus: (
        Annotated[SponsoredProductsCampaignServingStatus | str, lenient_enum(SponsoredProductsCampaignServingStatus)]
        | None
    ) = Field(default=None)
    servingStatusDetails: list[SponsoredProductsCampaignServingStatusDetail] | None = Field(
        default=None, description="The serving status reasons of the Campaign"
    )


class SponsoredProductsCampaignMutationError(LenientModel):
    errorType: str = Field(description="The type of the error")
    errorValue: SponsoredProductsCampaignMutationErrorSelector


class SponsoredProductsCampaignMutationErrorSelector(LenientModel):
    biddingError: SponsoredProductsBiddingError | None = Field(default=None)
    billingError: SponsoredProductsBillingError | None = Field(default=None)
    budgetError: SponsoredProductsBudgetError | None = Field(default=None)
    currencyError: SponsoredProductsCurrencyError | None = Field(default=None)
    dateError: SponsoredProductsDateError | None = Field(default=None)
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


class SponsoredProductsCampaignMutationFailureResponseItem(LenientModel):
    errors: list[SponsoredProductsCampaignMutationError] | None = Field(
        default=None, description="A list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the campaign in the array from the request body")


class SponsoredProductsCampaignMutationSuccessResponseItem(LenientModel):
    campaign: SponsoredProductsCampaign | None = Field(default=None)
    campaignId: str | None = Field(default=None, description="the campaign ID")
    index: int = Field(ge=0, description="the index of the campaign in the array from the request body")


class SponsoredProductsCampaignServingStatusDetail(LenientModel):
    helpUrl: str | None = Field(
        default=None, description="A URL with additional information about the status identifier."
    )
    message: str | None = Field(
        default=None, description="A human-readable description of the status identifier specified in the name field."
    )
    name: (
        Annotated[
            SponsoredProductsCampaignServingStatusReason | str,
            lenient_enum(SponsoredProductsCampaignServingStatusReason),
        ]
        | None
    ) = Field(default=None)


class SponsoredProductsCreateCampaign(StrictModel):
    autoManageCampaign: bool | None = Field(default=None)
    budget: SponsoredProductsCreateOrUpdateBudget
    dynamicBidding: SponsoredProductsCreateOrUpdateDynamicBidding | None = Field(default=None)
    endDate: date | None = Field(default=None, description="The format of the date is YYYY-MM-DD.")
    name: str = Field(description="The name of the campaign.")
    offAmazonSettings: SponsoredProductsCreateOrUpdateOffAmazonSettings | None = Field(default=None)
    portfolioId: str | None = Field(
        default=None, description="The identifier of an existing portfolio to which the campaign is associated."
    )
    siteRestrictions: (
        list[Annotated[SponsoredProductsSiteRestriction | str, lenient_enum(SponsoredProductsSiteRestriction)]] | None
    ) = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
Restrict the ad to a particular site. siteRestrictions is an optional field.
If this field is not set, ads from the campaign will appear on Amazon - including both Amazon retail and Amazon Business - as well as select sites and apps off Amazon.
Please note that: 1) AMAZON_BUSINESS option is only available for Amazon Business operated marketplaces (US, CA, MX, UK, DE, FR, IT, ES, IN, JP, AU), and AMAZON_HAUL option is only available in US;
2) siteRestrictions cannot be changed post campaign creation;
3) siteRestrictions don’t support shopperCohortBidding setting, SITE_AMAZON_BUSINESS placementBidding setting and offAmazonSettings;
4) Only AMAZON_BUSINESS option is ready for use at the moment.
""",
    )
    startDate: date | None = Field(
        default=None, description="Default: today's date. The format of the date is YYYY-MM-DD."
    )
    state: Annotated[
        SponsoredProductsCreateOrUpdateEntityState | str, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
    ]
    tags: SponsoredProductsTags | None = Field(default=None)
    targetingType: Annotated[SponsoredProductsTargetingType | str, lenient_enum(SponsoredProductsTargetingType)]


class SponsoredProductsCreateOrUpdateBudget(StrictModel):
    budget: float = Field(description="Monetary value")
    budgetType: Annotated[
        SponsoredProductsCreateOrUpdateBudgetType | str, lenient_enum(SponsoredProductsCreateOrUpdateBudgetType)
    ]


class SponsoredProductsCreateOrUpdateDynamicBidding(StrictModel):
    """Specifies bidding controls. DynamicBidding is optional for both Create and Update requests.
    For Create Campaign requests, if you don't specify dynamicBidding, default strategy of `LEGACY_FOR_SALES` will be applied.
    """

    placementBidding: list[SponsoredProductsPlacementBidding] | None = Field(default=None)
    shopperCohortBidding: list[SponsoredProductsShopperCohortBidding] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="""
Specifies Shopper Cohorts based bid adjustment controls. `shopperCohortBidding` is optional for both Create and Update requests.
You can enable this control to adjust your bid based on the shopper cohorts. The percentage value set is the percentage of the original bid including any other bid adjustments such as `placementBidding`. For example, a `placementBidding` with 50% adjustment on a $1.00 bid would increase the bid to $1.50, and a `shopperCohortBidding` with 100% adjustment would further increase the bid to $3.00.
""",
    )
    strategy: (
        Annotated[
            SponsoredProductsCreateOrUpdateBiddingStrategy | str,
            lenient_enum(SponsoredProductsCreateOrUpdateBiddingStrategy),
        ]
        | None
    ) = Field(default=None)


class SponsoredProductsCreateOrUpdateOffAmazonSettings(StrictModel):
    """Settings that apply to ads served off Amazon. `OffAmazonSettings` is optional for both Create and Update requests.
    This field is upcoming and is not ready for use."""

    offAmazonBudgetControlStrategy: (
        Annotated[
            SponsoredProductsCreateOrUpdateOffAmazonBudgetControlStrategy | str,
            lenient_enum(SponsoredProductsCreateOrUpdateOffAmazonBudgetControlStrategy),
        ]
        | None
    ) = Field(default=None)


class SponsoredProductsCreateSponsoredProductsCampaignsRequestContent(StrictModel):
    campaigns: list[SponsoredProductsCreateCampaign] = Field(
        min_length=0, max_length=1000, description="An array of campaigns."
    )


class SponsoredProductsCreateSponsoredProductsCampaignsResponseContent(LenientModel):
    campaigns: SponsoredProductsBulkCampaignOperationResponse


class SponsoredProductsCurrencyError(LenientModel):
    """Errors related to currency"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[SponsoredProductsCurrencyErrorReason | str, lenient_enum(SponsoredProductsCurrencyErrorReason)]


class SponsoredProductsDateError(LenientModel):
    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[SponsoredProductsDateErrorReason | str, lenient_enum(SponsoredProductsDateErrorReason)]


class SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent(StrictModel):
    campaignIdFilter: SponsoredProductsObjectIdFilter


class SponsoredProductsDeleteSponsoredProductsCampaignsResponseContent(LenientModel):
    campaigns: SponsoredProductsBulkCampaignOperationResponse


class SponsoredProductsDynamicBidding(LenientModel):
    placementBidding: list[SponsoredProductsPlacementBiddingOut] | None = Field(default=None)
    shopperCohortBidding: list[SponsoredProductsShopperCohortBiddingOut] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="""
Specifies Shopper Cohorts based bid adjustment controls. `shopperCohortBidding` is optional for both Create and Update requests.
You can enable this control to adjust your bid based on the shopper cohorts. The percentage value set is the percentage of the original bid including any other bid adjustments such as `placementBidding`. For example, a `placementBidding` with 50% adjustment on a $1.00 bid would increase the bid to $1.50, and a `shopperCohortBidding` with 100% adjustment would further increase the bid to $3.00.
""",
    )
    strategy: Annotated[SponsoredProductsBiddingStrategy | str, lenient_enum(SponsoredProductsBiddingStrategy)]


class SponsoredProductsListSponsoredProductsCampaignsRequestContent(StrictModel):
    campaignIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus",
    )
    marketplaceBudgetAllocationFilter: SponsoredProductsMarketplaceBudgetAllocationFilter | None = Field(default=None)
    maxResults: int | None = Field(
        default=None,
        description="Number of records to include in the paginated response. Defaults to max page size for given API",
    )
    nameFilter: SponsoredProductsNameFilter | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    portfolioIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    stateFilter: SponsoredProductsEntityStateFilter | None = Field(default=None)


class SponsoredProductsListSponsoredProductsCampaignsResponseContent(LenientModel):
    campaigns: list[SponsoredProductsCampaign] | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    totalResults: int | None = Field(default=None, description="The total number of entities")


class SponsoredProductsMarketplaceBudgetAllocationFilter(StrictModel):
    """Filter campaigns by MarketplaceBudgetAllocation setting. By default, only MANUAL campaigns are returned. This filter is not functional yet, will be functional soon."""

    include: list[
        Annotated[
            SponsoredProductsMarketplaceBudgetAllocation | str,
            lenient_enum(SponsoredProductsMarketplaceBudgetAllocation),
        ]
    ] = Field(min_length=0, max_length=2)


class SponsoredProductsOffAmazonSettings(LenientModel):
    offAmazonBudgetControlStrategy: (
        Annotated[
            SponsoredProductsOffAmazonBudgetControlStrategy | str,
            lenient_enum(SponsoredProductsOffAmazonBudgetControlStrategy),
        ]
        | None
    ) = Field(default=None)


class SponsoredProductsPlacementBidding(StrictModel):
    percentage: int | None = Field(default=None, ge=0, le=900)
    placement: Annotated[SponsoredProductsPlacement | str, lenient_enum(SponsoredProductsPlacement)] | None = Field(
        default=None
    )


class SponsoredProductsPlacementBiddingOut(LenientModel):
    percentage: int | None = Field(default=None, ge=0, le=900)
    placement: Annotated[SponsoredProductsPlacement | str, lenient_enum(SponsoredProductsPlacement)] | None = Field(
        default=None
    )


class SponsoredProductsShopperCohortBidding(StrictModel):
    audienceSegments: list[SponsoredProductsAudienceSegment] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description='A list of Audience Segments. Shoppers belonging to these segments will be selected for applying the bid adjustments. This is a required field when using "AUDIENCE_SEGMENT" option for `shopperCohortType`.',
    )
    percentage: int | None = Field(default=None, ge=0, le=900)
    shopperCohortType: Annotated[
        SponsoredProductsShopperCohortType | str, lenient_enum(SponsoredProductsShopperCohortType)
    ]


class SponsoredProductsShopperCohortBiddingOut(LenientModel):
    audienceSegments: list[SponsoredProductsAudienceSegmentOut] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description='A list of Audience Segments. Shoppers belonging to these segments will be selected for applying the bid adjustments. This is a required field when using "AUDIENCE_SEGMENT" option for `shopperCohortType`.',
    )
    percentage: int | None = Field(default=None, ge=0, le=900)
    shopperCohortType: Annotated[
        SponsoredProductsShopperCohortType | str, lenient_enum(SponsoredProductsShopperCohortType)
    ]


class SponsoredProductsTagsOut(LenientModel):
    """A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You can specify a maximum of 50 identifiers."""

    pass


class SponsoredProductsUpdateCampaign(StrictModel):
    budget: SponsoredProductsCreateOrUpdateBudget | None = Field(default=None)
    campaignId: str = Field(description="The identifier of the campaign.")
    dynamicBidding: SponsoredProductsCreateOrUpdateDynamicBidding | None = Field(default=None)
    endDate: date | None = Field(default=None, description="The format of the date is YYYY-MM-DD.")
    name: str | None = Field(default=None, description="The name of the campaign.")
    offAmazonSettings: SponsoredProductsCreateOrUpdateOffAmazonSettings | None = Field(default=None)
    portfolioId: str | None = Field(
        default=None, description="The identifier of an existing portfolio to which the campaign is associated."
    )
    siteRestrictions: (
        list[Annotated[SponsoredProductsSiteRestriction | str, lenient_enum(SponsoredProductsSiteRestriction)]] | None
    ) = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
Restrict the ad to a particular site. siteRestrictions is an optional field.
If this field is not set, ads from the campaign will appear on Amazon - including both Amazon retail and Amazon Business - as well as select sites and apps off Amazon.
Please note that: 1) AMAZON_BUSINESS option is only available for Amazon Business operated marketplaces (US, CA, MX, UK, DE, FR, IT, ES, IN, JP, AU), and AMAZON_HAUL option is only available in US;
2) siteRestrictions cannot be changed post campaign creation;
3) siteRestrictions don’t support shopperCohortBidding setting, SITE_AMAZON_BUSINESS placementBidding setting and offAmazonSettings;
4) Only AMAZON_BUSINESS option is ready for use at the moment.
""",
    )
    startDate: date | None = Field(default=None, description="The format of the date is YYYY-MM-DD.")
    state: (
        Annotated[
            SponsoredProductsCreateOrUpdateEntityState | str, lenient_enum(SponsoredProductsCreateOrUpdateEntityState)
        ]
        | None
    ) = Field(default=None)
    tags: SponsoredProductsTags | None = Field(default=None)
    targetingType: (
        Annotated[SponsoredProductsTargetingType | str, lenient_enum(SponsoredProductsTargetingType)] | None
    ) = Field(default=None)


class SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent(StrictModel):
    campaigns: list[SponsoredProductsUpdateCampaign] = Field(
        min_length=0,
        max_length=1000,
        description="An array of campaigns with updated values. Note: targetingType cannot be updated",
    )


class SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent(LenientModel):
    campaigns: SponsoredProductsBulkCampaignOperationResponse


__all__ = [
    "SponsoredProductsAudienceSegment",
    "SponsoredProductsAudienceSegmentOut",
    "SponsoredProductsAudienceSegmentType",
    "SponsoredProductsBiddingError",
    "SponsoredProductsBiddingErrorReason",
    "SponsoredProductsBiddingStrategy",
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsBudget",
    "SponsoredProductsBudgetError",
    "SponsoredProductsBudgetErrorReason",
    "SponsoredProductsBudgetType",
    "SponsoredProductsBulkCampaignOperationResponse",
    "SponsoredProductsCampaign",
    "SponsoredProductsCampaignExtendedData",
    "SponsoredProductsCampaignMutationError",
    "SponsoredProductsCampaignMutationErrorSelector",
    "SponsoredProductsCampaignMutationFailureResponseItem",
    "SponsoredProductsCampaignMutationSuccessResponseItem",
    "SponsoredProductsCampaignServingStatus",
    "SponsoredProductsCampaignServingStatusDetail",
    "SponsoredProductsCampaignServingStatusReason",
    "SponsoredProductsCreateCampaign",
    "SponsoredProductsCreateOrUpdateBiddingStrategy",
    "SponsoredProductsCreateOrUpdateBudget",
    "SponsoredProductsCreateOrUpdateBudgetType",
    "SponsoredProductsCreateOrUpdateDynamicBidding",
    "SponsoredProductsCreateOrUpdateEntityState",
    "SponsoredProductsCreateOrUpdateOffAmazonBudgetControlStrategy",
    "SponsoredProductsCreateOrUpdateOffAmazonSettings",
    "SponsoredProductsCreateSponsoredProductsCampaignsRequestContent",
    "SponsoredProductsCreateSponsoredProductsCampaignsResponseContent",
    "SponsoredProductsCurrencyError",
    "SponsoredProductsCurrencyErrorReason",
    "SponsoredProductsDateError",
    "SponsoredProductsDateErrorReason",
    "SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent",
    "SponsoredProductsDeleteSponsoredProductsCampaignsResponseContent",
    "SponsoredProductsDuplicateValueError",
    "SponsoredProductsDuplicateValueErrorReason",
    "SponsoredProductsDynamicBidding",
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
    "SponsoredProductsListSponsoredProductsCampaignsRequestContent",
    "SponsoredProductsListSponsoredProductsCampaignsResponseContent",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMarketplaceBudgetAllocation",
    "SponsoredProductsMarketplaceBudgetAllocationFilter",
    "SponsoredProductsMissingValueError",
    "SponsoredProductsMissingValueErrorReason",
    "SponsoredProductsNameFilter",
    "SponsoredProductsObjectIdFilter",
    "SponsoredProductsOffAmazonBudgetControlStrategy",
    "SponsoredProductsOffAmazonSettings",
    "SponsoredProductsOtherError",
    "SponsoredProductsOtherErrorReason",
    "SponsoredProductsParentEntityError",
    "SponsoredProductsParentEntityErrorReason",
    "SponsoredProductsPlacement",
    "SponsoredProductsPlacementBidding",
    "SponsoredProductsPlacementBiddingOut",
    "SponsoredProductsQueryTermMatchType",
    "SponsoredProductsQuotaErrorReason",
    "SponsoredProductsQuotaScope",
    "SponsoredProductsRangeError",
    "SponsoredProductsReducedObjectIdFilter",
    "SponsoredProductsShopperCohortBidding",
    "SponsoredProductsShopperCohortBiddingOut",
    "SponsoredProductsShopperCohortType",
    "SponsoredProductsSiteRestriction",
    "SponsoredProductsTags",
    "SponsoredProductsTagsOut",
    "SponsoredProductsTargetingType",
    "SponsoredProductsThrottledError",
    "SponsoredProductsThrottledErrorReason",
    "SponsoredProductsUpdateCampaign",
    "SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent",
    "SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent",
    "SponsoredProductsValueLimitErrorReason",
]
