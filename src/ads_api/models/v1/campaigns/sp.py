"""Auto-generated models for Campaigns from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.sp import (
    SPAdProduct,
    SPCreateState,
    SPCreateTag,
    SPCurrencyCode,
    SPDeliveryReason,
    SPDeliveryStatus,
    SPError,
    SPErrorCode,
    SPErrorsIndex,
    SPMarketplaceScope,
    SPState,
    SPStatus,
    SPTag,
    SPUpdateState,
)


class SPAutoScaleGlobalCampaignSetting(StrEnum):
    AUTO = "AUTO"  # Auto scale global campaign to new marketplaces
    MANUAL = "MANUAL"  # Manually scale global campaign to new marketplaces


class SPBidStrategy(StrEnum):
    MANUAL = (
        "MANUAL"  # Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
    )
    RULE_BASED = "RULE_BASED"  # Applies bidding rules defined by the advertiser.
    SALES_DOWN_ONLY = "SALES_DOWN_ONLY"  # Decreases your bids in real time when your ad is less likely to convert to a sale. Bids will never increase beyond your set bid.
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"  # Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.


class SPBudgetType(StrEnum):
    MONETARY = "MONETARY"


class SPCampaignNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SPCountryCode(StrEnum):
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


class SPCreativeBidAdjustmentType(StrEnum):
    SPOTLIGHT = "SPOTLIGHT"  # SPOTLIGHT Video Asset.


class SPMarketplace(StrEnum):
    """
    A list of country codes representing Amazon marketplaces
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


class SPMarketplaceBudgetAllocation(StrEnum):
    AUTO = "AUTO"  # Auto distribute global budget to marketplaces in global campaign
    MANUAL = "MANUAL"  # Manually distribute global budget to marketplaces in global campaign


class SPOffAmazonBudgetControlStrategy(StrEnum):
    MAXIMIZE_REACH = "MAXIMIZE_REACH"  # Maximize the reach of off-Amazon inventory within the budget.
    MINIMIZE_SPEND = "MINIMIZE_SPEND"  # Minimize spend on off-Amazon inventory while maintaining delivery.


class SPPlacement(StrEnum):
    PRODUCT_PAGE = "PRODUCT_PAGE"  # Placements on the product detail page, and all nonsearch placements such as the add-to-cart page.
    REST_OF_SEARCH = "REST_OF_SEARCH"  # Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond.
    SITE_AMAZON_BUSINESS = "SITE_AMAZON_BUSINESS"  # Amazon Business site placements.
    TOP_OF_SEARCH = "TOP_OF_SEARCH"  # Placements on the top row of the first-page search results.


class SPRecurrence(StrEnum):
    DAILY = "DAILY"


class SPSiteRestriction(StrEnum):
    AMAZON_BUSINESS = "AMAZON_BUSINESS"  # Restrict the ad to only show on Amazon Business.
    AMAZON_HAUL = "AMAZON_HAUL"  # Restrict the ad to only show on Amazon Haul.


class SPAudienceBidAdjustment(LenientModel):
    audienceId: str = Field(description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(
        description="The selection of the percentage change associated with a given audience and bid adjustment settings."
    )


class SPAutoCreationSettings(LenientModel):
    autoCreateTargets: bool = Field(
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised."
    )
    autoManageCampaign: bool | None = Field(
        default=None, description="Flag that allows Amazon to manage the lifecycle of your Campaign."
    )


class SPBidAdjustments(LenientModel):
    audienceBidAdjustments: list[SPAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    creativeBidAdjustments: list[SPCreativeBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900",
    )
    placementBidAdjustments: list[SPPlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )


class SPBidSettings(LenientModel):
    bidAdjustments: SPBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SPBidStrategy | str, lenient_enum(SPBidStrategy)] | None = Field(default=None)


class SPBudget(LenientModel):
    budgetType: Annotated[SPBudgetType | str, lenient_enum(SPBudgetType)]
    budgetValue: SPBudgetValue
    recurrenceTimePeriod: Annotated[SPRecurrence | str, lenient_enum(SPRecurrence)]


class SPBudgetSettings(LenientModel):
    marketplaceBudgetAllocation: (
        Annotated[SPMarketplaceBudgetAllocation | str, lenient_enum(SPMarketplaceBudgetAllocation)] | None
    ) = Field(default=None)
    offAmazonBudgetControlStrategy: (
        Annotated[SPOffAmazonBudgetControlStrategy | str, lenient_enum(SPOffAmazonBudgetControlStrategy)] | None
    ) = Field(default=None)


class SPBudgetValue(LenientModel):
    monetaryBudgetValue: SPMonetaryBudgetValue


class SPCampaign(LenientModel):
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    autoCreationSettings: SPAutoCreationSettings
    autoScaleGlobalCampaign: (
        Annotated[SPAutoScaleGlobalCampaignSetting | str, lenient_enum(SPAutoScaleGlobalCampaignSetting)] | None
    ) = Field(default=None)
    budgets: list[SPBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    countries: list[Annotated[SPCountryCode | str, lenient_enum(SPCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime = Field(description="The date time that the campaign was created.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    globalCampaignId: str | None = Field(
        default=None, description="The global campaign identifier that manages this marketplace campaign."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the campaign was last updated.")
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SPCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    siteRestrictions: list[Annotated[SPSiteRestriction | str, lenient_enum(SPSiteRestriction)]] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SPState | str, lenient_enum(SPState)]
    status: SPStatus | None = Field(default=None)
    tags: list[SPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPCampaignAdProductFilter(StrictModel):
    include: list[Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]] = Field(min_length=1, max_length=1)


class SPCampaignCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class SPCampaignCreate(StrictModel):
    adProduct: Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]
    autoCreationSettings: SPCreateAutoCreationSettings
    budgets: list[SPCreateBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    countries: list[Annotated[SPCountryCode | str, lenient_enum(SPCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaceScope: Annotated[SPMarketplaceScope | str, lenient_enum(SPMarketplaceScope)]
    marketplaces: list[Annotated[SPMarketplace | str, lenient_enum(SPMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SPCreateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    siteRestrictions: list[Annotated[SPSiteRestriction | str, lenient_enum(SPSiteRestriction)]] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SPCreateState | str, lenient_enum(SPCreateState)]
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPCampaignMultiStatusResponse(LenientModel):
    error: list[SPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPCampaignMultiStatusSuccess(LenientModel):
    campaign: SPCampaign
    index: int = Field(ge=0, le=999)


class SPCampaignNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SPCampaignNameFilterType | str, lenient_enum(SPCampaignNameFilterType)]


class SPCampaignOptimizations(LenientModel):
    bidSettings: SPBidSettings | None = Field(default=None)
    budgetSettings: SPBudgetSettings | None = Field(default=None)


class SPCampaignPortfolioIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPCampaignStateFilter(StrictModel):
    include: list[Annotated[SPState | str, lenient_enum(SPState)]] = Field(min_length=1, max_length=3)


class SPCampaignSuccessResponse(LenientModel):
    campaigns: list[SPCampaign] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPCampaignUpdate(StrictModel):
    budgets: list[SPCreateBudget] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: SPUpdateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    siteRestrictions: list[Annotated[SPSiteRestriction | str, lenient_enum(SPSiteRestriction)]] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: Annotated[SPUpdateState | str, lenient_enum(SPUpdateState)] | None = Field(default=None)
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPCreateAudienceBidAdjustment(StrictModel):
    audienceId: str = Field(description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(
        description="The selection of the percentage change associated with a given audience and bid adjustment settings."
    )


class SPCreateAutoCreationSettings(StrictModel):
    autoCreateTargets: bool = Field(
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised."
    )
    autoManageCampaign: bool | None = Field(
        default=None, description="Flag that allows Amazon to manage the lifecycle of your Campaign."
    )


class SPCreateBidAdjustments(StrictModel):
    audienceBidAdjustments: list[SPCreateAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    creativeBidAdjustments: list[SPCreateCreativeBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900",
    )
    placementBidAdjustments: list[SPCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )


class SPCreateBidSettings(StrictModel):
    bidAdjustments: SPCreateBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SPBidStrategy | str, lenient_enum(SPBidStrategy)] | None = Field(default=None)


class SPCreateBudget(StrictModel):
    budgetType: Annotated[SPBudgetType | str, lenient_enum(SPBudgetType)]
    budgetValue: SPCreateBudgetValue
    recurrenceTimePeriod: Annotated[SPRecurrence | str, lenient_enum(SPRecurrence)]


class SPCreateBudgetSettings(StrictModel):
    offAmazonBudgetControlStrategy: (
        Annotated[SPOffAmazonBudgetControlStrategy | str, lenient_enum(SPOffAmazonBudgetControlStrategy)] | None
    ) = Field(default=None)


class SPCreateBudgetValue(StrictModel):
    monetaryBudgetValue: SPCreateMonetaryBudgetValue


class SPCreateCampaignOptimizations(StrictModel):
    bidSettings: SPCreateBidSettings | None = Field(default=None)
    budgetSettings: SPCreateBudgetSettings | None = Field(default=None)


class SPCreateCampaignRequest(StrictModel):
    campaigns: list[SPCampaignCreate] = Field(min_length=1, max_length=1000)


class SPCreateCreativeBidAdjustment(StrictModel):
    creativeType: Annotated[SPCreativeBidAdjustmentType | str, lenient_enum(SPCreativeBidAdjustmentType)] | None = (
        Field(default=None)
    )
    percentage: int = Field(
        description="The selection of the percentage change associated with the creative type and bid adjustment settings."
    )


class SPCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SPCreateMonetaryBudgetValue(StrictModel):
    monetaryBudget: SPCreateMonetaryBudget


class SPCreatePlacementBidAdjustment(StrictModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: Annotated[SPPlacement | str, lenient_enum(SPPlacement)]


class SPCreativeBidAdjustment(LenientModel):
    creativeType: Annotated[SPCreativeBidAdjustmentType | str, lenient_enum(SPCreativeBidAdjustmentType)] | None = (
        Field(default=None)
    )
    percentage: int = Field(
        description="The selection of the percentage change associated with the creative type and bid adjustment settings."
    )


class SPDeleteCampaignRequest(StrictModel):
    campaignIds: list[str] = Field(min_length=1, max_length=1000)


class SPMonetaryBudget(LenientModel):
    currencyCode: Annotated[SPCurrencyCode | str, lenient_enum(SPCurrencyCode)]
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SPMonetaryBudgetValue(LenientModel):
    monetaryBudget: SPMonetaryBudget


class SPPlacementBidAdjustment(LenientModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: Annotated[SPPlacement | str, lenient_enum(SPPlacement)]


class SPQueryCampaignRequest(StrictModel):
    adProductFilter: SPCampaignAdProductFilter
    campaignIdFilter: SPCampaignCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nameFilter: SPCampaignNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    portfolioIdFilter: SPCampaignPortfolioIdFilter | None = Field(default=None)
    stateFilter: SPCampaignStateFilter | None = Field(default=None)


class SPUpdateBidAdjustments(StrictModel):
    audienceBidAdjustments: list[SPCreateAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    creativeBidAdjustments: list[SPCreateCreativeBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900",
    )
    placementBidAdjustments: list[SPCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )


class SPUpdateBidSettings(StrictModel):
    bidAdjustments: SPUpdateBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SPBidStrategy | str, lenient_enum(SPBidStrategy)] | None = Field(default=None)


class SPUpdateBudgetSettings(StrictModel):
    offAmazonBudgetControlStrategy: (
        Annotated[SPOffAmazonBudgetControlStrategy | str, lenient_enum(SPOffAmazonBudgetControlStrategy)] | None
    ) = Field(default=None)


class SPUpdateCampaignOptimizations(StrictModel):
    bidSettings: SPUpdateBidSettings | None = Field(default=None)
    budgetSettings: SPUpdateBudgetSettings | None = Field(default=None)


class SPUpdateCampaignRequest(StrictModel):
    campaigns: list[SPCampaignUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SPAdProduct",
    "SPAudienceBidAdjustment",
    "SPAutoCreationSettings",
    "SPAutoScaleGlobalCampaignSetting",
    "SPBidAdjustments",
    "SPBidSettings",
    "SPBidStrategy",
    "SPBudget",
    "SPBudgetSettings",
    "SPBudgetType",
    "SPBudgetValue",
    "SPCampaign",
    "SPCampaignAdProductFilter",
    "SPCampaignCampaignIdFilter",
    "SPCampaignCreate",
    "SPCampaignMultiStatusResponse",
    "SPCampaignMultiStatusSuccess",
    "SPCampaignNameFilter",
    "SPCampaignNameFilterType",
    "SPCampaignOptimizations",
    "SPCampaignPortfolioIdFilter",
    "SPCampaignStateFilter",
    "SPCampaignSuccessResponse",
    "SPCampaignUpdate",
    "SPCountryCode",
    "SPCreateAudienceBidAdjustment",
    "SPCreateAutoCreationSettings",
    "SPCreateBidAdjustments",
    "SPCreateBidSettings",
    "SPCreateBudget",
    "SPCreateBudgetSettings",
    "SPCreateBudgetValue",
    "SPCreateCampaignOptimizations",
    "SPCreateCampaignRequest",
    "SPCreateCreativeBidAdjustment",
    "SPCreateMonetaryBudget",
    "SPCreateMonetaryBudgetValue",
    "SPCreatePlacementBidAdjustment",
    "SPCreateState",
    "SPCreateTag",
    "SPCreativeBidAdjustment",
    "SPCreativeBidAdjustmentType",
    "SPCurrencyCode",
    "SPDeleteCampaignRequest",
    "SPDeliveryReason",
    "SPDeliveryStatus",
    "SPError",
    "SPErrorCode",
    "SPErrorsIndex",
    "SPMarketplace",
    "SPMarketplaceBudgetAllocation",
    "SPMarketplaceScope",
    "SPMonetaryBudget",
    "SPMonetaryBudgetValue",
    "SPOffAmazonBudgetControlStrategy",
    "SPPlacement",
    "SPPlacementBidAdjustment",
    "SPQueryCampaignRequest",
    "SPRecurrence",
    "SPSiteRestriction",
    "SPState",
    "SPStatus",
    "SPTag",
    "SPUpdateBidAdjustments",
    "SPUpdateBidSettings",
    "SPUpdateBudgetSettings",
    "SPUpdateCampaignOptimizations",
    "SPUpdateCampaignRequest",
    "SPUpdateState",
]
