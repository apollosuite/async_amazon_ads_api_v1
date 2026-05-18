"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from amazon_ads_sdk.models.base import SafeStrEnum

if TYPE_CHECKING:
    from amazon_ads_sdk.errors import ErrorsIndex
    from .enums import (
        SBAdProduct,
        SBCreateState,
        SBCurrencyCode,
        SBMarketplace,
        SBMarketplaceScope,
        SBState,
        SBUpdateState,
    )
    from .shared import SBCreateTag, SBStatus, SBTag


class SBAudienceBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid adjustment settings.


class SBAutoCreationSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    autoCreateTargets: bool | None = (
        None  # Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.
    )


class SBBidAdjustments(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    audienceBidAdjustments: list[SBAudienceBidAdjustment] | None = (
        None  # Bid Adjustments based on the audiences
    )
    placementBidAdjustments: list[SBPlacementBidAdjustment] | None = (
        None  # Bid adjustments based on ad placements.
    )
    shopperSegmentBidAdjustments: list[SBShopperSegmentBidAdjustment] | None = (
        None  # Legacy SB field (marked for deprecation)
    )


class SBBidSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    bidAdjustments: SBBidAdjustments | None = None
    bidStrategy: SBBidStrategy | None = None


class SBBidStrategy(SafeStrEnum):
    """| BidStrategy | Description |
    |------|------|
    | `MANUAL` | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding. |
    | `SALES_UP_AND_DOWN` | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale. |
    """

    MANUAL = "MANUAL"
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"


class SBBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    budgetType: SBBudgetType
    budgetValue: SBBudgetValue
    recurrenceTimePeriod: SBRecurrence


class SBBudgetType(SafeStrEnum):
    """| BudgetType | Description |
    |------|------|
    | `MONETARY` |  |
    """

    MONETARY = "MONETARY"


class SBBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    monetaryBudgetValue: SBMonetaryBudgetValue | None = None


class SBCampaign(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adProduct: SBAdProduct
    autoCreationSettings: SBAutoCreationSettings | None = None
    brandId: str | None = None  # This is the ID of the brand that the campaign is associated with.
    budgets: list[
        SBBudget
    ]  # The object containing budget details for the campaign (for campaigns that support multiple budgets).
    campaignId: str  # A unique identifier for a campaign.
    costType: SBCostType
    countries: list[SBCountryCode] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.
    )
    creationDateTime: datetime  # The date time that the campaign was created.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    isMultiAdGroupsEnabled: (
        bool  # A read-only field that indicates whether a campaign supports multiple adGroups.
    )
    lastUpdatedDateTime: datetime  # The date time that the campaign was last updated.
    marketplaceScope: SBMarketplaceScope
    marketplaces: list[SBMarketplace] | None = (
        None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc, that represent a country that an Amazon customer can shop.
    )
    name: str  # The name of the campaign.
    optimizations: SBCampaignOptimizations | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    salesChannel: SBSalesChannel | None = None
    siteRestrictions: list[SBSiteRestriction] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime  # The start date time for the campaign.
    state: SBState
    status: SBStatus | None = None
    tags: list[SBTag] | None = (
        None  # Open ended labels with a key value pair applied to the campaign
    )
    targetedPGDealId: str | None = None  # DealId associated with the campaign.


class SBCampaignAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[
        SBAdProduct
    ]  # AdProduct Description `SPONSORED_BRANDS` Sponsored Brands ad product.


class SBCampaignCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]


class SBCampaignCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adProduct: SBAdProduct
    autoCreationSettings: SBCreateAutoCreationSettings | None = None
    brandId: str | None = None  # This is the ID of the brand that the campaign is associated with.
    budgets: list[
        SBCreateBudget
    ]  # The object containing budget details for the campaign (for campaigns that support multiple budgets).
    costType: SBCostType
    countries: list[SBCountryCode] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.
    )
    endDateTime: datetime | None = None  # The end date time for the campaign.
    marketplaceScope: SBMarketplaceScope
    marketplaces: list[SBMarketplace] | None = (
        None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc, that represent a country that an Amazon customer can shop.
    )
    name: str  # The name of the campaign.
    optimizations: SBCreateCampaignOptimizations | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    salesChannel: SBSalesChannel | None = None
    siteRestrictions: list[SBSiteRestriction] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime  # The start date time for the campaign.
    state: SBCreateState
    tags: list[SBCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the campaign
    )
    targetedPGDealId: str | None = None  # DealId associated with the campaign.


class SBCampaignGoalFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[
        SBGoal
    ]  # Goal Description `AWARENESS` Indicates a goal of driving awareness. `CONSIDERATION` Indicates a goal of driving consideration. `CONVERSIONS` Indicates a goal of driving conversions.


class SBCampaignMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = None
    success: list[SBCampaignMultiStatusSuccess] | None = None


class SBCampaignMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    campaign: SBCampaign
    index: int


class SBCampaignNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]
    queryTermMatchType: SBCampaignNameFilterType


class SBCampaignNameFilterType(SafeStrEnum):
    """| CampaignNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    bidSettings: SBBidSettings | None = None
    goalSettings: SBGoalSettings | None = None


class SBCampaignPortfolioIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[str]


class SBCampaignStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    include: list[
        SBState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SBCampaignSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    campaigns: list[SBCampaign] | None = None
    nextToken: str | None = None


class SBCampaignUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    budgets: list[SBCreateBudget] | None = (
        None  # The object containing budget details for the campaign (for campaigns that support multiple budgets).
    )
    campaignId: str  # A unique identifier for a campaign.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    name: str | None = None  # The name of the campaign.
    optimizations: SBUpdateCampaignOptimizations | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    startDateTime: datetime | None = None  # The start date time for the campaign.
    state: SBUpdateState | None = None
    tags: list[SBCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the campaign
    )
    targetedPGDealId: str | None = None  # DealId associated with the campaign.


class SBCostType(SafeStrEnum):
    """| CostType | Description |
    |------|------|
    | `CPC` | Cost per click. |
    | `FIXED_PRICE` | Sale price for a specific ad placement regardless of auction performance. |
    | `VCPM` | Cost per thousand views. |
    """

    CPC = "CPC"
    FIXED_PRICE = "FIXED_PRICE"
    VCPM = "VCPM"


class SBCountryCode(SafeStrEnum):
    """| CountryCode | Description |
    |------|------|
    | `AE` |  |
    | `AU` |  |
    | `BE` |  |
    | `BR` |  |
    | `CA` |  |
    | `DE` |  |
    | `EG` |  |
    | `ES` |  |
    | `FR` |  |
    | `GB` |  |
    | `IE` |  |
    | `IN` |  |
    | `IT` |  |
    | `JP` |  |
    | `MX` |  |
    | `NL` |  |
    | `PL` |  |
    | `SA` |  |
    | `SE` |  |
    | `SG` |  |
    | `TR` |  |
    | `US` |  |
    | `ZA` |  |
    """

    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IE = "IE"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"
    ZA = "ZA"


class SBCreateAudienceBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid adjustment settings.


class SBCreateAutoCreationSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    autoCreateTargets: bool | None = (
        None  # Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.
    )


class SBCreateBidAdjustments(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    audienceBidAdjustments: list[SBCreateAudienceBidAdjustment] | None = (
        None  # Bid Adjustments based on the audiences
    )
    placementBidAdjustments: list[SBCreatePlacementBidAdjustment] | None = (
        None  # Bid adjustments based on ad placements.
    )
    shopperSegmentBidAdjustments: list[SBCreateShopperSegmentBidAdjustment] | None = (
        None  # Legacy SB field (marked for deprecation)
    )


class SBCreateBidSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    bidAdjustments: SBCreateBidAdjustments | None = None
    bidStrategy: SBBidStrategy | None = None


class SBCreateBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    budgetType: SBBudgetType
    budgetValue: SBCreateBudgetValue
    recurrenceTimePeriod: SBRecurrence


class SBCreateBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    monetaryBudgetValue: SBCreateMonetaryBudgetValue | None = None


class SBCreateCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    bidSettings: SBCreateBidSettings | None = None
    goalSettings: SBCreateGoalSettings | None = None


class SBCreateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    campaigns: list[SBCampaignCreate] | None = None


class SBCreateGoalSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    kpi: SBKPI


class SBCreateMonetaryBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    value: float  # The monetary amount of the budget cap in the given currency.


class SBCreateMonetaryBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    monetaryBudget: SBCreateMonetaryBudget


class SBCreatePlacementBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    percentage: int  # The selection of the percentage change associated with a given placement and bid adjustment settings.
    placement: SBPlacement


class SBCreateShopperSegmentBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")


class SBDeleteCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    campaignIds: list[str] | None = None


class SBGoal(SafeStrEnum):
    """| Goal | Description |
    |------|------|
    | `AWARENESS` | Indicates a goal of driving awareness. |
    | `CONSIDERATION` | Indicates a goal of driving consideration. |
    | `CONVERSIONS` | Indicates a goal of driving conversions. |
    """

    AWARENESS = "AWARENESS"
    CONSIDERATION = "CONSIDERATION"
    CONVERSIONS = "CONVERSIONS"


class SBGoalSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    goal: SBGoal
    kpi: SBKPI


class SBKPI(SafeStrEnum):
    """| KPI | Description |
    |------|------|
    | `CLICKS` | Indicates a goal of driving clicks. |
    | `TOP_OF_SEARCH_IMPRESSION_SHARE` | Indicates a goal of maximizing impression for top search placement. |
    """

    CLICKS = "CLICKS"
    TOP_OF_SEARCH_IMPRESSION_SHARE = "TOP_OF_SEARCH_IMPRESSION_SHARE"


class SBMonetaryBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    currencyCode: SBCurrencyCode
    ruleValue: float | None = (
        None  # The monetary amount of the budget when a budget rule is applied.
    )
    value: float  # The monetary amount of the budget cap in the given currency.


class SBMonetaryBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    monetaryBudget: SBMonetaryBudget


class SBPlacement(SafeStrEnum):
    """| Placement | Description |
    |------|------|
    | `HOME_PAGE` | Home page. |
    | `PRODUCT_PAGE` | Placements on the product detail page, and all nonsearch placements such as the add-to-cart page. |
    | `REST_OF_SEARCH` | Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond. |
    | `TOP_OF_SEARCH` | Placements on the top row of the first-page search results. |
    """

    HOME_PAGE = "HOME_PAGE"
    PRODUCT_PAGE = "PRODUCT_PAGE"
    REST_OF_SEARCH = "REST_OF_SEARCH"
    TOP_OF_SEARCH = "TOP_OF_SEARCH"


class SBPlacementBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    percentage: int  # The selection of the percentage change associated with a given placement and bid adjustment settings.
    placement: SBPlacement


class SBQueryCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    adProductFilter: SBCampaignAdProductFilter
    campaignIdFilter: SBCampaignCampaignIdFilter | None = None
    goalFilter: SBCampaignGoalFilter | None = None
    maxResults: int | None = None
    nameFilter: SBCampaignNameFilter | None = None
    nextToken: str | None = None
    portfolioIdFilter: SBCampaignPortfolioIdFilter | None = None
    stateFilter: SBCampaignStateFilter | None = None


class SBRecurrence(SafeStrEnum):
    """| Recurrence | Description |
    |------|------|
    | `DAILY` |  |
    | `LIFETIME` |  |
    """

    DAILY = "DAILY"
    LIFETIME = "LIFETIME"


class SBSalesChannel(SafeStrEnum):
    """| SalesChannel | Description |
    |------|------|
    | `AMAZON` | A product sold on Amazon-owned sites. |
    | `OFF_AMAZON` | A product sold on a site not owned by Amazon. |
    """

    AMAZON = "AMAZON"
    OFF_AMAZON = "OFF_AMAZON"


class SBShopperSegment(SafeStrEnum):
    """| ShopperSegment | Description |
    |------|------|
    | `NEW_TO_BRAND` |  |
    """

    NEW_TO_BRAND = "NEW_TO_BRAND"


class SBShopperSegmentBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    percentage: int  # The selection of the percentage change associated with a given shopper segment and bid adjustment settings.
    shopperSegment: SBShopperSegment


class SBSiteRestriction(SafeStrEnum):
    """| SiteRestriction | Description |
    |------|------|
    | `AMAZON_BUSINESS` | Restrict the ad to only show on Amazon Business. |
    """

    AMAZON_BUSINESS = "AMAZON_BUSINESS"


class SBUpdateBidAdjustments(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    audienceBidAdjustments: list[SBCreateAudienceBidAdjustment] | None = (
        None  # Bid Adjustments based on the audiences
    )
    placementBidAdjustments: list[SBCreatePlacementBidAdjustment] | None = (
        None  # Bid adjustments based on ad placements.
    )
    shopperSegmentBidAdjustments: list[SBCreateShopperSegmentBidAdjustment] | None = (
        None  # Legacy SB field (marked for deprecation)
    )


class SBUpdateBidSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    bidAdjustments: SBUpdateBidAdjustments | None = None
    bidStrategy: SBBidStrategy | None = None


class SBUpdateCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    bidSettings: SBUpdateBidSettings | None = None


class SBUpdateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    campaigns: list[SBCampaignUpdate] | None = None
