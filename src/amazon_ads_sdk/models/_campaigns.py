"""campaign models."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from enum import StrEnum

if TYPE_CHECKING:
    from ._enums import (
        SPAdProduct,
        SPCreateState,
        SPCurrencyCode,
        SPMarketplace,
        SPMarketplaceScope,
        SPState,
        SPUpdateState,
    )
    from ._shared import ErrorsIndex, SPCreateTag, SPStatus, SPTag


class SPAudienceBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid adjustment settings.


class SPAutoCreationSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.
    autoManageCampaign: bool | None = (
        None  # Flag that allows Amazon to manage the lifecycle of your Campaign.
    )


class SPAutoScaleGlobalCampaignSetting(StrEnum):
    """| AutoScaleGlobalCampaignSetting | Description |
    |------|------|
    | `AUTO` | Auto scale global campaign to new marketplaces |
    | `MANUAL` | Manually scale global campaign to new marketplaces |
    """

    AUTO = "AUTO"
    MANUAL = "MANUAL"


class SPBidAdjustments(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[SPAudienceBidAdjustment] | None = (
        None  # Bid Adjustments based on the audiences
    )
    creativeBidAdjustments: list[SPCreativeBidAdjustment] | None = (
        None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900
    )
    placementBidAdjustments: list[SPPlacementBidAdjustment] | None = (
        None  # Bid adjustments based on ad placements.
    )


class SPBidSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SPBidAdjustments | None = None
    bidStrategy: SPBidStrategy | None = None


class SPBidStrategy(StrEnum):
    """| BidStrategy | Description |
    |------|------|
    | `MANUAL` | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding. |
    | `RULE_BASED` | Applies bidding rules defined by the advertiser. |
    | `SALES_DOWN_ONLY` | Decreases your bids in real time when your ad is less likely to convert to a sale. Bids will never increase beyond your set bid. |
    | `SALES_UP_AND_DOWN` | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale. |
    """

    MANUAL = "MANUAL"
    RULE_BASED = "RULE_BASED"
    SALES_DOWN_ONLY = "SALES_DOWN_ONLY"
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"


class SPBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    budgetType: SPBudgetType
    budgetValue: SPBudgetValue
    recurrenceTimePeriod: SPRecurrence


class SPBudgetSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    marketplaceBudgetAllocation: SPMarketplaceBudgetAllocation | None = None
    offAmazonBudgetControlStrategy: SPOffAmazonBudgetControlStrategy | None = None


class SPBudgetType(StrEnum):
    """| BudgetType | Description |
    |------|------|
    | `MONETARY` |  |
    """

    MONETARY = "MONETARY"


class SPBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SPMonetaryBudgetValue | None = None


class SPCampaign(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProduct: SPAdProduct
    autoCreationSettings: SPAutoCreationSettings
    autoScaleGlobalCampaign: SPAutoScaleGlobalCampaignSetting | None = None
    budgets: list[
        SPBudget
    ]  # The object containing budget details for the campaign (for campaigns that support multiple budgets).
    campaignId: str  # A unique identifier for a campaign.
    countries: list[SPCountryCode] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.
    )
    creationDateTime: datetime  # The date time that the campaign was created.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    globalCampaignId: str | None = (
        None  # The global campaign identifier that manages this marketplace campaign.
    )
    lastUpdatedDateTime: datetime  # The date time that the campaign was last updated.
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[SPMarketplace] | None = (
        None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc, that represent a country that an Amazon customer can shop.
    )
    name: str  # The name of the campaign.
    optimizations: SPCampaignOptimizations | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    siteRestrictions: list[SPSiteRestriction] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime  # The start date time for the campaign.
    state: SPState
    status: SPStatus | None = None
    tags: list[SPTag] | None = (
        None  # Open ended labels with a key value pair applied to the campaign
    )


class SPCampaignAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdProduct
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPCampaignCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPCampaignCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProduct: SPAdProduct
    autoCreationSettings: SPCreateAutoCreationSettings
    budgets: list[
        SPCreateBudget
    ]  # The object containing budget details for the campaign (for campaigns that support multiple budgets).
    countries: list[SPCountryCode] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.
    )
    endDateTime: datetime | None = None  # The end date time for the campaign.
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[SPMarketplace] | None = (
        None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc, that represent a country that an Amazon customer can shop.
    )
    name: str  # The name of the campaign.
    optimizations: SPCreateCampaignOptimizations | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    siteRestrictions: list[SPSiteRestriction] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime  # The start date time for the campaign.
    state: SPCreateState
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the campaign
    )


class SPCampaignMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPCampaignMultiStatusSuccess] | None = None


class SPCampaignMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaign: SPCampaign
    index: int


class SPCampaignNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: SPCampaignNameFilterType


class SPCampaignNameFilterType(StrEnum):
    """| CampaignNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SPCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidSettings: SPBidSettings | None = None
    budgetSettings: SPBudgetSettings | None = None


class SPCampaignPortfolioIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPCampaignStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPCampaignSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaign] | None = None
    nextToken: str | None = None


class SPCampaignUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    budgets: list[SPCreateBudget] | None = (
        None  # The object containing budget details for the campaign (for campaigns that support multiple budgets).
    )
    campaignId: str  # A unique identifier for a campaign.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    name: str | None = None  # The name of the campaign.
    optimizations: SPUpdateCampaignOptimizations | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    siteRestrictions: list[SPSiteRestriction] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime | None = None  # The start date time for the campaign.
    state: SPUpdateState | None = None
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the campaign
    )


class SPCountryCode(StrEnum):
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


class SPCreateAudienceBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid adjustment settings.


class SPCreateAutoCreationSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.
    autoManageCampaign: bool | None = (
        None  # Flag that allows Amazon to manage the lifecycle of your Campaign.
    )


class SPCreateBidAdjustments(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[SPCreateAudienceBidAdjustment] | None = (
        None  # Bid Adjustments based on the audiences
    )
    creativeBidAdjustments: list[SPCreateCreativeBidAdjustment] | None = (
        None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900
    )
    placementBidAdjustments: list[SPCreatePlacementBidAdjustment] | None = (
        None  # Bid adjustments based on ad placements.
    )


class SPCreateBidSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SPCreateBidAdjustments | None = None
    bidStrategy: SPBidStrategy | None = None


class SPCreateBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    budgetType: SPBudgetType
    budgetValue: SPCreateBudgetValue
    recurrenceTimePeriod: SPRecurrence


class SPCreateBudgetSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: SPOffAmazonBudgetControlStrategy | None = None


class SPCreateBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SPCreateMonetaryBudgetValue | None = None


class SPCreateCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidSettings: SPCreateBidSettings | None = None
    budgetSettings: SPCreateBudgetSettings | None = None


class SPCreateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaignCreate] | None = None


class SPCreateCreativeBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    creativeType: SPCreativeBidAdjustmentType | None = None
    percentage: int  # The selection of the percentage change associated with the creative type and bid adjustment settings.


class SPCreateMonetaryBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    value: float  # The monetary amount of the budget cap in the given currency.


class SPCreateMonetaryBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SPCreateMonetaryBudget


class SPCreatePlacementBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid adjustment settings.
    placement: SPPlacement


class SPCreativeBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    creativeType: SPCreativeBidAdjustmentType | None = None
    percentage: int  # The selection of the percentage change associated with the creative type and bid adjustment settings.


class SPCreativeBidAdjustmentType(StrEnum):
    """| CreativeBidAdjustmentType | Description |
    |------|------|
    | `SPOTLIGHT` | SPOTLIGHT Video Asset. |
    """

    SPOTLIGHT = "SPOTLIGHT"


class SPDeleteCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaignIds: list[str] | None = None


class SPMarketplaceBudgetAllocation(StrEnum):
    """| MarketplaceBudgetAllocation | Description |
    |------|------|
    | `AUTO` | Auto distribute global budget to marketplaces in global campaign |
    | `MANUAL` | Manually distribute global budget to marketplaces in global campaign |
    """

    AUTO = "AUTO"
    MANUAL = "MANUAL"


class SPMonetaryBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    currencyCode: SPCurrencyCode
    ruleValue: float | None = (
        None  # The monetary amount of the budget when a budget rule is applied.
    )
    value: float  # The monetary amount of the budget cap in the given currency.


class SPMonetaryBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SPMonetaryBudget


class SPOffAmazonBudgetControlStrategy(StrEnum):
    """| OffAmazonBudgetControlStrategy | Description |
    |------|------|
    | `MAXIMIZE_REACH` | Maximize the reach of off-Amazon inventory within the budget. |
    | `MINIMIZE_SPEND` | Minimize spend on off-Amazon inventory while maintaining delivery. |
    """

    MAXIMIZE_REACH = "MAXIMIZE_REACH"
    MINIMIZE_SPEND = "MINIMIZE_SPEND"


class SPPlacement(StrEnum):
    """| Placement | Description |
    |------|------|
    | `PRODUCT_PAGE` | Placements on the product detail page, and all nonsearch placements such as the add-to-cart page. |
    | `REST_OF_SEARCH` | Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond. |
    | `SITE_AMAZON_BUSINESS` | Amazon Business site placements. |
    | `TOP_OF_SEARCH` | Placements on the top row of the first-page search results. |
    """

    PRODUCT_PAGE = "PRODUCT_PAGE"
    REST_OF_SEARCH = "REST_OF_SEARCH"
    SITE_AMAZON_BUSINESS = "SITE_AMAZON_BUSINESS"
    TOP_OF_SEARCH = "TOP_OF_SEARCH"


class SPPlacementBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid adjustment settings.
    placement: SPPlacement


class SPQueryCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProductFilter: SPCampaignAdProductFilter
    campaignIdFilter: SPCampaignCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SPCampaignNameFilter | None = None
    nextToken: str | None = None
    portfolioIdFilter: SPCampaignPortfolioIdFilter | None = None
    stateFilter: SPCampaignStateFilter | None = None


class SPRecurrence(StrEnum):
    """| Recurrence | Description |
    |------|------|
    | `DAILY` |  |
    """

    DAILY = "DAILY"


class SPSiteRestriction(StrEnum):
    """| SiteRestriction | Description |
    |------|------|
    | `AMAZON_BUSINESS` | Restrict the ad to only show on Amazon Business. |
    | `AMAZON_HAUL` | Restrict the ad to only show on Amazon Haul. |
    """

    AMAZON_BUSINESS = "AMAZON_BUSINESS"
    AMAZON_HAUL = "AMAZON_HAUL"


class SPUpdateBidAdjustments(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[SPCreateAudienceBidAdjustment] | None = (
        None  # Bid Adjustments based on the audiences
    )
    creativeBidAdjustments: list[SPCreateCreativeBidAdjustment] | None = (
        None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900
    )
    placementBidAdjustments: list[SPCreatePlacementBidAdjustment] | None = (
        None  # Bid adjustments based on ad placements.
    )


class SPUpdateBidSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SPUpdateBidAdjustments | None = None
    bidStrategy: SPBidStrategy | None = None


class SPUpdateBudgetSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: SPOffAmazonBudgetControlStrategy | None = None


class SPUpdateCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidSettings: SPUpdateBidSettings | None = None
    budgetSettings: SPUpdateBudgetSettings | None = None


class SPUpdateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaignUpdate] | None = None
