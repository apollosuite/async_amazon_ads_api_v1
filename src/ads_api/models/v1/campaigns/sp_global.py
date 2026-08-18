"""Auto-generated models for Campaigns from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sp_global import (
    SPGlobalAdProduct,
    SPGlobalCreateState,
    SPGlobalCreateTag,
    SPGlobalCurrencyCode,
    SPGlobalDeliveryReason,
    SPGlobalDeliveryStatus,
    SPGlobalError,
    SPGlobalErrorCode,
    SPGlobalErrorMarketplace,
    SPGlobalErrorsIndex,
    SPGlobalMarketplaceScope,
    SPGlobalState,
    SPGlobalTag,
    SPGlobalUpdateState,
)

type SPGlobalAutoScaleGlobalCampaignSetting = Literal["AUTO", "MANUAL"]
"""
Supported values:
- `AUTO`: Auto scale global campaign to new marketplaces
- `MANUAL`: Manually scale global campaign to new marketplaces
"""


type SPGlobalBidStrategy = Literal["MANUAL", "NEW_TO_BRAND", "RULE_BASED", "SALES_DOWN_ONLY", "SALES_UP_AND_DOWN"]
"""
Supported values:
- `MANUAL`: Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
- `NEW_TO_BRAND`: Optimizes bidding to maximize new-to-brand customer acquisitions.
- `RULE_BASED`: Applies bidding rules defined by the advertiser.
- `SALES_DOWN_ONLY`: Decreases your bids in real time when your ad is less likely to convert to a sale. Bids will never increase beyond your set bid.
- `SALES_UP_AND_DOWN`: Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.
"""


type SPGlobalBudgetType = Literal["MONETARY"]


type SPGlobalCampaignNameFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SPGlobalCountryCode = Literal[
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
    "IN",
    "IT",
    "JP",
    "MK",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "US",
]


type SPGlobalMarketplace = Literal[
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
]
"""
A list of country codes representing Amazon marketplaces
"""


type SPGlobalPlacement = Literal["PRODUCT_PAGE", "REST_OF_SEARCH", "TOP_OF_SEARCH"]
"""
Supported values:
- `PRODUCT_PAGE`: Placements on the product detail page, and all nonsearch placements such as the add-to-cart page.
- `REST_OF_SEARCH`: Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond.
- `TOP_OF_SEARCH`: Placements on the top row of the first-page search results.
"""


type SPGlobalRecurrence = Literal["DAILY"]


type SPGlobalSiteRestriction = Literal["AMAZON_BUSINESS", "AMAZON_HAUL"]
"""
Supported values:
- `AMAZON_BUSINESS`: Restrict the ad to only show on Amazon Business.
- `AMAZON_HAUL`: Restrict the ad to only show on Amazon Haul.
"""


class SPGlobalAutoCreationSettings(LenientModel):
    autoCreateTargets: bool = Field(
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised."
    )


class SPGlobalBidAdjustments(LenientModel):
    placementBidAdjustments: list[SPGlobalPlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )


class SPGlobalBidSettings(LenientModel):
    bidAdjustments: SPGlobalBidAdjustments | None = Field(default=None)
    bidStrategy: SPGlobalBidStrategy | str | None = Field(default=None)


class SPGlobalBudget(LenientModel):
    budgetType: SPGlobalBudgetType | str
    budgetValue: SPGlobalBudgetValue
    recurrenceTimePeriod: SPGlobalRecurrence | str


class SPGlobalBudgetValue(LenientModel):
    monetaryBudgetValue: SPGlobalMonetaryBudgetValue


class SPGlobalCampaign(LenientModel):
    adProduct: SPGlobalAdProduct | str
    autoCreationSettings: SPGlobalAutoCreationSettings
    autoScaleGlobalCampaign: SPGlobalAutoScaleGlobalCampaignSetting | str | None = Field(default=None)
    budgets: list[SPGlobalBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    countries: list[SPGlobalCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime = Field(description="The date time that the campaign was created.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    lastUpdatedDateTime: datetime = Field(description="The date time that the campaign was last updated.")
    marketplaceConfigurations: list[SPGlobalMarketplaceCampaignConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individual marketplace level. For example, if a global campaign is ENABLED and startDate '2024-06-01' but needs to be PAUSED in DE with startDateTime '2024-06-02' marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED, startDate: '2024-06-02'}}]. When a marketplace-specific override is not provided, the campaign's global value is applied to that marketplace.",
    )
    marketplaceScope: SPGlobalMarketplaceScope | str
    marketplaces: list[SPGlobalMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SPGlobalCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    siteRestrictions: list[SPGlobalSiteRestriction | str] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: SPGlobalState | str
    status: SPGlobalStatus | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPGlobalCampaignAdProductFilter(StrictModel):
    include: list[SPGlobalAdProduct] = Field(min_length=1, max_length=1)


class SPGlobalCampaignCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalCampaignCreate(StrictModel):
    adProduct: SPGlobalAdProduct
    autoCreationSettings: SPGlobalCreateAutoCreationSettings
    budgets: list[SPGlobalCreateBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    countries: list[SPGlobalCountryCode] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceCampaignConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individual marketplace level. For example, if a global campaign is ENABLED and startDate '2024-06-01' but needs to be PAUSED in DE with startDateTime '2024-06-02' marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED, startDate: '2024-06-02'}}]. When a marketplace-specific override is not provided, the campaign's global value is applied to that marketplace.",
    )
    marketplaceScope: SPGlobalMarketplaceScope
    marketplaces: list[SPGlobalMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SPGlobalCreateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    siteRestrictions: list[SPGlobalSiteRestriction] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: SPGlobalCreateState
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPGlobalCampaignMarketplaceScopeFilter(StrictModel):
    include: list[SPGlobalMarketplaceScope] = Field(min_length=1, max_length=1)


class SPGlobalCampaignMultiStatusResponseWithPartialErrors(LenientModel):
    error: list[SPGlobalErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    partialSuccess: list[SPGlobalCampaignPartialIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPGlobalCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPGlobalCampaignMultiStatusSuccess(LenientModel):
    campaign: SPGlobalCampaign
    index: int = Field(ge=0, le=999)


class SPGlobalCampaignNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: SPGlobalCampaignNameFilterType


class SPGlobalCampaignOptimizations(LenientModel):
    bidSettings: SPGlobalBidSettings | None = Field(default=None)


class SPGlobalCampaignPartialIndex(LenientModel):
    campaign: SPGlobalCampaign
    errors: list[SPGlobalError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SPGlobalCampaignPortfolioIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalCampaignStateFilter(StrictModel):
    include: list[SPGlobalState] = Field(min_length=1, max_length=3)


class SPGlobalCampaignSuccessResponse(LenientModel):
    campaigns: list[SPGlobalCampaign] | None = Field(default=None, min_length=0, max_length=5000)
    nextToken: str | None = Field(default=None)


class SPGlobalCampaignUpdate(StrictModel):
    budgets: list[SPGlobalCreateBudget] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    countries: list[SPGlobalCountryCode] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceCampaignConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individual marketplace level. For example, if a global campaign is ENABLED and startDate '2024-06-01' but needs to be PAUSED in DE with startDateTime '2024-06-02' marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED, startDate: '2024-06-02'}}]. When a marketplace-specific override is not provided, the campaign's global value is applied to that marketplace.",
    )
    marketplaces: list[SPGlobalMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: SPGlobalUpdateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    siteRestrictions: list[SPGlobalSiteRestriction] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: SPGlobalUpdateState | None = Field(default=None)
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPGlobalCreateAutoCreationSettings(StrictModel):
    autoCreateTargets: bool = Field(
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised."
    )


class SPGlobalCreateBidAdjustments(StrictModel):
    placementBidAdjustments: list[SPGlobalCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )


class SPGlobalCreateBidSettings(StrictModel):
    bidAdjustments: SPGlobalCreateBidAdjustments | None = Field(default=None)
    bidStrategy: SPGlobalBidStrategy | None = Field(default=None)


class SPGlobalCreateBudget(StrictModel):
    budgetType: SPGlobalBudgetType
    budgetValue: SPGlobalCreateBudgetValue
    recurrenceTimePeriod: SPGlobalRecurrence


class SPGlobalCreateBudgetValue(StrictModel):
    monetaryBudgetValue: SPGlobalCreateMonetaryBudgetValue


class SPGlobalCreateCampaignOptimizations(StrictModel):
    bidSettings: SPGlobalCreateBidSettings | None = Field(default=None)


class SPGlobalCreateCampaignRequest(StrictModel):
    campaigns: list[SPGlobalCampaignCreate] = Field(min_length=1, max_length=1000)


class SPGlobalCreateMarketplaceCampaignConfigurations(StrictModel):
    marketplace: SPGlobalMarketplace
    overrides: SPGlobalCreateMarketplaceCampaignFieldOverrides


class SPGlobalCreateMarketplaceCampaignFieldOverrides(StrictModel):
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign")
    name: str | None = Field(default=None, description="The name of the campaign")
    optimizations: SPGlobalCreateCampaignOptimizations | None = Field(default=None)
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign")
    state: SPGlobalState | None = Field(default=None)
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPGlobalCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SPGlobalCreateMonetaryBudgetMarketplaceSetting(StrictModel):
    marketplace: SPGlobalMarketplace
    monetaryBudget: SPGlobalCreateMonetaryBudget


class SPGlobalCreateMonetaryBudgetValue(StrictModel):
    marketplaceSettings: list[SPGlobalCreateMonetaryBudgetMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="List of Monetary Budget values selectively applied at the given marketplace level",
    )


class SPGlobalCreatePlacementBidAdjustment(StrictModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: SPGlobalPlacement


class SPGlobalDeleteCampaignRequest(StrictModel):
    campaignIds: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalMarketplaceCampaignConfigurations(LenientModel):
    campaignId: str = Field(
        description="Represents marketplace campaign id (Ex: campaignId-US) associated to global campaign (Ex: campaignId-Global)"
    )
    marketplace: SPGlobalMarketplace | str
    overrides: SPGlobalMarketplaceCampaignFieldOverrides


class SPGlobalMarketplaceCampaignFieldOverrides(LenientModel):
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign")
    name: str | None = Field(default=None, description="The name of the campaign")
    optimizations: SPGlobalCampaignOptimizations | None = Field(default=None)
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign")
    state: SPGlobalState | str | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPGlobalMonetaryBudget(LenientModel):
    currencyCode: SPGlobalCurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SPGlobalMonetaryBudgetMarketplaceSetting(LenientModel):
    marketplace: SPGlobalMarketplace | str
    monetaryBudget: SPGlobalMonetaryBudget


class SPGlobalMonetaryBudgetValue(LenientModel):
    marketplaceSettings: list[SPGlobalMonetaryBudgetMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="List of Monetary Budget values selectively applied at the given marketplace level",
    )


class SPGlobalPlacementBidAdjustment(LenientModel):
    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: SPGlobalPlacement | str


class SPGlobalQueryCampaignRequest(StrictModel):
    adProductFilter: SPGlobalCampaignAdProductFilter
    campaignIdFilter: SPGlobalCampaignCampaignIdFilter | None = Field(default=None)
    marketplaceScopeFilter: SPGlobalCampaignMarketplaceScopeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=5000, ge=1, le=5000)
    nameFilter: SPGlobalCampaignNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    portfolioIdFilter: SPGlobalCampaignPortfolioIdFilter | None = Field(default=None)
    stateFilter: SPGlobalCampaignStateFilter | None = Field(default=None)


class SPGlobalStatus(LenientModel):
    deliveryReasons: list[SPGlobalDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: SPGlobalDeliveryStatus | str
    marketplaceSettings: list[SPGlobalStatusMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace level delivery status and reasons of global resources, for all the marketplaces the global resource is applicable in.",
    )


class SPGlobalStatusMarketplaceSetting(LenientModel):
    deliveryReasons: list[SPGlobalDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: SPGlobalDeliveryStatus | str
    marketplace: SPGlobalMarketplace | str


class SPGlobalUpdateBidAdjustments(StrictModel):
    placementBidAdjustments: list[SPGlobalCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )


class SPGlobalUpdateBidSettings(StrictModel):
    bidAdjustments: SPGlobalUpdateBidAdjustments | None = Field(default=None)
    bidStrategy: SPGlobalBidStrategy | None = Field(default=None)


class SPGlobalUpdateCampaignOptimizations(StrictModel):
    bidSettings: SPGlobalUpdateBidSettings | None = Field(default=None)


class SPGlobalUpdateCampaignRequest(StrictModel):
    campaigns: list[SPGlobalCampaignUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SPGlobalAdProduct",
    "SPGlobalAutoCreationSettings",
    "SPGlobalAutoScaleGlobalCampaignSetting",
    "SPGlobalBidAdjustments",
    "SPGlobalBidSettings",
    "SPGlobalBidStrategy",
    "SPGlobalBudget",
    "SPGlobalBudgetType",
    "SPGlobalBudgetValue",
    "SPGlobalCampaign",
    "SPGlobalCampaignAdProductFilter",
    "SPGlobalCampaignCampaignIdFilter",
    "SPGlobalCampaignCreate",
    "SPGlobalCampaignMarketplaceScopeFilter",
    "SPGlobalCampaignMultiStatusResponseWithPartialErrors",
    "SPGlobalCampaignMultiStatusSuccess",
    "SPGlobalCampaignNameFilter",
    "SPGlobalCampaignNameFilterType",
    "SPGlobalCampaignOptimizations",
    "SPGlobalCampaignPartialIndex",
    "SPGlobalCampaignPortfolioIdFilter",
    "SPGlobalCampaignStateFilter",
    "SPGlobalCampaignSuccessResponse",
    "SPGlobalCampaignUpdate",
    "SPGlobalCountryCode",
    "SPGlobalCreateAutoCreationSettings",
    "SPGlobalCreateBidAdjustments",
    "SPGlobalCreateBidSettings",
    "SPGlobalCreateBudget",
    "SPGlobalCreateBudgetValue",
    "SPGlobalCreateCampaignOptimizations",
    "SPGlobalCreateCampaignRequest",
    "SPGlobalCreateMarketplaceCampaignConfigurations",
    "SPGlobalCreateMarketplaceCampaignFieldOverrides",
    "SPGlobalCreateMonetaryBudget",
    "SPGlobalCreateMonetaryBudgetMarketplaceSetting",
    "SPGlobalCreateMonetaryBudgetValue",
    "SPGlobalCreatePlacementBidAdjustment",
    "SPGlobalCreateState",
    "SPGlobalCreateTag",
    "SPGlobalCurrencyCode",
    "SPGlobalDeleteCampaignRequest",
    "SPGlobalDeliveryReason",
    "SPGlobalDeliveryStatus",
    "SPGlobalError",
    "SPGlobalErrorCode",
    "SPGlobalErrorMarketplace",
    "SPGlobalErrorsIndex",
    "SPGlobalMarketplace",
    "SPGlobalMarketplaceCampaignConfigurations",
    "SPGlobalMarketplaceCampaignFieldOverrides",
    "SPGlobalMarketplaceScope",
    "SPGlobalMonetaryBudget",
    "SPGlobalMonetaryBudgetMarketplaceSetting",
    "SPGlobalMonetaryBudgetValue",
    "SPGlobalPlacement",
    "SPGlobalPlacementBidAdjustment",
    "SPGlobalQueryCampaignRequest",
    "SPGlobalRecurrence",
    "SPGlobalSiteRestriction",
    "SPGlobalState",
    "SPGlobalStatus",
    "SPGlobalStatusMarketplaceSetting",
    "SPGlobalTag",
    "SPGlobalUpdateBidAdjustments",
    "SPGlobalUpdateBidSettings",
    "SPGlobalUpdateCampaignOptimizations",
    "SPGlobalUpdateCampaignRequest",
    "SPGlobalUpdateState",
]
