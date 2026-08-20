"""Auto-generated models for Campaigns from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBAdProduct,
    SBCreateState,
    SBCreateTag,
    SBCurrencyCode,
    SBDeliveryReason,
    SBDeliveryStatus,
    SBError,
    SBErrorCode,
    SBErrorsIndex,
    SBMarketplace,
    SBMarketplaceScope,
    SBState,
    SBStatus,
    SBTag,
    SBUpdateState,
)

type SBBidStrategy = Literal["MANUAL", "SALES_UP_AND_DOWN"]
"""
Supported values:
- `MANUAL`: Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
- `SALES_UP_AND_DOWN`: Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.
"""


type SBBudgetType = Literal["MONETARY"]


type SBCampaignNameFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SBCostType = Literal["CPC", "CPM", "FIXED_PRICE", "VCPM"]
"""
Supported values:
- `CPC`: Cost per click.
- `CPM`: Cost per thousand impressions.
- `FIXED_PRICE`: Sale price for a specific ad placement regardless of auction performance.
- `VCPM`: Cost per thousand views.
"""


type SBCountryCode = Literal[
    "AE",
    "AU",
    "BE",
    "BR",
    "CA",
    "DE",
    "EG",
    "ES",
    "FR",
    "GB",
    "IE",
    "IN",
    "IT",
    "JP",
    "MX",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "US",
    "ZA",
]


type SBGoal = Literal["AWARENESS", "CONSIDERATION", "CONVERSIONS"]
"""
Supported values:
- `AWARENESS`: Indicates a goal of driving awareness.
- `CONSIDERATION`: Indicates a goal of driving consideration.
- `CONVERSIONS`: Indicates a goal of driving conversions.
"""


type SBKPI = Literal["CLICKS", "TOP_OF_SEARCH_IMPRESSION_SHARE"]
"""
Supported values:
- `CLICKS`: Indicates a goal of driving clicks.
- `TOP_OF_SEARCH_IMPRESSION_SHARE`: Indicates a goal of maximizing impression for top search placement.
"""


type SBPlacement = Literal["HOME_PAGE", "PRODUCT_PAGE", "REST_OF_SEARCH", "TOP_OF_SEARCH"]
"""
Supported values:
- `HOME_PAGE`: Home page.
- `PRODUCT_PAGE`: Placements on the product detail page, and all nonsearch placements such as the add-to-cart page.
- `REST_OF_SEARCH`: Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond.
- `TOP_OF_SEARCH`: Placements on the top row of the first-page search results.
"""


type SBRecurrence = Literal["DAILY", "LIFETIME"]


type SBSalesChannel = Literal["AMAZON", "OFF_AMAZON"]
"""
Supported values:
- `AMAZON`: A product sold on Amazon-owned sites.
- `OFF_AMAZON`: A product sold on a site not owned by Amazon.
"""


type SBShopperSegment = Literal["NEW_TO_BRAND"]


type SBSiteRestriction = Literal["AMAZON_BUSINESS"]
"""
Supported values:
- `AMAZON_BUSINESS`: Restrict the ad to only show on Amazon Business.
"""


class SBAudienceBidAdjustment(LenientModel):
    audienceId: str = Field(description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(
        description="The selection of the percentage change associated with a given audience and bid adjustment settings."
    )


class SBAutoCreationSettings(LenientModel):
    autoCreateTargets: bool | None = Field(
        default=None,
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.",
    )


class SBBidAdjustments(LenientModel):
    audienceBidAdjustments: list[SBAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    placementBidAdjustments: list[SBPlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )
    shopperSegmentBidAdjustments: list[SBShopperSegmentBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Legacy SB field (marked for deprecation)"
    )


class SBBidSettings(LenientModel):
    bidAdjustments: SBBidAdjustments | None = Field(default=None)
    bidStrategy: SBBidStrategy | str | None = Field(default=None)


class SBBudget(LenientModel):
    budgetType: SBBudgetType | str
    budgetValue: SBBudgetValue
    recurrenceTimePeriod: SBRecurrence | str


class SBBudgetValue(LenientModel):
    monetaryBudgetValue: SBMonetaryBudgetValue


class SBCampaign(LenientModel):
    adProduct: SBAdProduct | str
    autoCreationSettings: SBAutoCreationSettings | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[SBBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    costType: SBCostType | str
    countries: list[SBCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime = Field(description="The date time that the campaign was created.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    isMultiAdGroupsEnabled: bool = Field(
        description="A read-only field that indicates whether a campaign supports multiple adGroups."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the campaign was last updated.")
    marketplaceScope: SBMarketplaceScope | str
    marketplaces: list[SBMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SBCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    salesChannel: SBSalesChannel | str | None = Field(default=None)
    siteRestrictions: list[SBSiteRestriction | str] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: SBState | str
    status: SBStatus | None = Field(default=None)
    tags: list[SBTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class SBCampaignAdProductFilter(StrictModel):
    include: list[SBAdProduct] = Field(min_length=1, max_length=1)


class SBCampaignCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBCampaignCreate(StrictModel):
    adProduct: SBAdProduct
    autoCreationSettings: SBCreateAutoCreationSettings | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[SBCreateBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    costType: SBCostType
    countries: list[SBCountryCode] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaceScope: SBMarketplaceScope
    marketplaces: list[SBMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SBCreateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    salesChannel: SBSalesChannel | None = Field(default=None)
    siteRestrictions: list[SBSiteRestriction] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: SBCreateState
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class SBCampaignGoalFilter(StrictModel):
    include: list[SBGoal] = Field(min_length=1, max_length=3)


class SBCampaignMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBCampaignMultiStatusSuccess(LenientModel):
    campaign: SBCampaign
    index: int = Field(ge=0, le=9)


class SBCampaignNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: SBCampaignNameFilterType


class SBCampaignOptimizations(LenientModel):
    bidSettings: SBBidSettings | None = Field(default=None)
    goalSettings: SBGoalSettings | None = Field(default=None)


class SBCampaignPortfolioIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBCampaignStateFilter(StrictModel):
    include: list[SBState] = Field(min_length=1, max_length=3)


class SBCampaignSuccessResponse(LenientModel):
    campaigns: list[SBCampaign] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SBCampaignUpdate(StrictModel):
    budgets: list[SBCreateBudget] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: SBUpdateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: SBUpdateState | None = Field(default=None)
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class SBCreateAudienceBidAdjustment(StrictModel):
    audienceId: str = Field(description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(
        description="The selection of the percentage change associated with a given audience and bid adjustment settings."
    )


class SBCreateAutoCreationSettings(StrictModel):
    autoCreateTargets: bool | None = Field(
        default=None,
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.",
    )


class SBCreateBidAdjustments(StrictModel):
    audienceBidAdjustments: list[SBCreateAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    placementBidAdjustments: list[SBCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )
    shopperSegmentBidAdjustments: list[SBCreateShopperSegmentBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Legacy SB field (marked for deprecation)"
    )


class SBCreateBidSettings(StrictModel):
    bidAdjustments: SBCreateBidAdjustments | None = Field(default=None)
    bidStrategy: SBBidStrategy | None = Field(default=None)


class SBCreateBudget(StrictModel):
    budgetType: SBBudgetType
    budgetValue: SBCreateBudgetValue
    recurrenceTimePeriod: SBRecurrence


class SBCreateBudgetValue(StrictModel):
    monetaryBudgetValue: SBCreateMonetaryBudgetValue


class SBCreateCampaignOptimizations(StrictModel):
    bidSettings: SBCreateBidSettings | None = Field(default=None)
    goalSettings: SBCreateGoalSettings | None = Field(default=None)


class SBCreateCampaignRequest(StrictModel):
    campaigns: list[SBCampaignCreate] = Field(min_length=1, max_length=10)


class SBCreateGoalSettings(StrictModel):
    kpi: SBKPI


class SBCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SBCreateMonetaryBudgetValue(StrictModel):
    monetaryBudget: SBCreateMonetaryBudget


class SBCreatePlacementBidAdjustment(StrictModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: SBPlacement


class SBCreateShopperSegmentBidAdjustment(StrictModel):
    pass


class SBDeleteCampaignRequest(StrictModel):
    campaignIds: list[str] = Field(min_length=1, max_length=10)


class SBGoalSettings(LenientModel):
    goal: SBGoal | str
    kpi: SBKPI | str


class SBMonetaryBudget(LenientModel):
    currencyCode: SBCurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SBMonetaryBudgetValue(LenientModel):
    monetaryBudget: SBMonetaryBudget


class SBPlacementBidAdjustment(LenientModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: SBPlacement | str


class SBQueryCampaignRequest(StrictModel):
    adProductFilter: SBCampaignAdProductFilter
    campaignIdFilter: SBCampaignCampaignIdFilter | None = Field(default=None)
    goalFilter: SBCampaignGoalFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SBCampaignNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    portfolioIdFilter: SBCampaignPortfolioIdFilter | None = Field(default=None)
    stateFilter: SBCampaignStateFilter | None = Field(default=None)


class SBShopperSegmentBidAdjustment(LenientModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given shopper segment and bid adjustment settings."
    )
    shopperSegment: SBShopperSegment | str


class SBUpdateBidAdjustments(StrictModel):
    audienceBidAdjustments: list[SBCreateAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    placementBidAdjustments: list[SBCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )
    shopperSegmentBidAdjustments: list[SBCreateShopperSegmentBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Legacy SB field (marked for deprecation)"
    )


class SBUpdateBidSettings(StrictModel):
    bidAdjustments: SBUpdateBidAdjustments | None = Field(default=None)
    bidStrategy: SBBidStrategy | None = Field(default=None)


class SBUpdateCampaignOptimizations(StrictModel):
    bidSettings: SBUpdateBidSettings | None = Field(default=None)


class SBUpdateCampaignRequest(StrictModel):
    campaigns: list[SBCampaignUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "SBAdProduct",
    "SBAudienceBidAdjustment",
    "SBAutoCreationSettings",
    "SBBidAdjustments",
    "SBBidSettings",
    "SBBidStrategy",
    "SBBudget",
    "SBBudgetType",
    "SBBudgetValue",
    "SBCampaign",
    "SBCampaignAdProductFilter",
    "SBCampaignCampaignIdFilter",
    "SBCampaignCreate",
    "SBCampaignGoalFilter",
    "SBCampaignMultiStatusResponse",
    "SBCampaignMultiStatusSuccess",
    "SBCampaignNameFilter",
    "SBCampaignNameFilterType",
    "SBCampaignOptimizations",
    "SBCampaignPortfolioIdFilter",
    "SBCampaignStateFilter",
    "SBCampaignSuccessResponse",
    "SBCampaignUpdate",
    "SBCostType",
    "SBCountryCode",
    "SBCreateAudienceBidAdjustment",
    "SBCreateAutoCreationSettings",
    "SBCreateBidAdjustments",
    "SBCreateBidSettings",
    "SBCreateBudget",
    "SBCreateBudgetValue",
    "SBCreateCampaignOptimizations",
    "SBCreateCampaignRequest",
    "SBCreateGoalSettings",
    "SBCreateMonetaryBudget",
    "SBCreateMonetaryBudgetValue",
    "SBCreatePlacementBidAdjustment",
    "SBCreateShopperSegmentBidAdjustment",
    "SBCreateState",
    "SBCreateTag",
    "SBCurrencyCode",
    "SBDeleteCampaignRequest",
    "SBDeliveryReason",
    "SBDeliveryStatus",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBGoal",
    "SBGoalSettings",
    "SBKPI",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBMonetaryBudget",
    "SBMonetaryBudgetValue",
    "SBPlacement",
    "SBPlacementBidAdjustment",
    "SBQueryCampaignRequest",
    "SBRecurrence",
    "SBSalesChannel",
    "SBShopperSegment",
    "SBShopperSegmentBidAdjustment",
    "SBSiteRestriction",
    "SBState",
    "SBStatus",
    "SBTag",
    "SBUpdateBidAdjustments",
    "SBUpdateBidSettings",
    "SBUpdateCampaignOptimizations",
    "SBUpdateCampaignRequest",
    "SBUpdateState",
]
