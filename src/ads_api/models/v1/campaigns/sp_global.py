"""Auto-generated models for Campaigns from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
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


class SPGlobalAutoScaleGlobalCampaignSetting(StrEnum):
    AUTO = "AUTO"  # Auto scale global campaign to new marketplaces
    MANUAL = "MANUAL"  # Manually scale global campaign to new marketplaces


class SPGlobalBidStrategy(StrEnum):
    MANUAL = (
        "MANUAL"  # Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
    )
    NEW_TO_BRAND = "NEW_TO_BRAND"  # Optimizes bidding to maximize new-to-brand customer acquisitions.
    RULE_BASED = "RULE_BASED"  # Applies bidding rules defined by the advertiser.
    SALES_DOWN_ONLY = "SALES_DOWN_ONLY"  # Decreases your bids in real time when your ad is less likely to convert to a sale. Bids will never increase beyond your set bid.
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"  # Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.


class SPGlobalBudgetType(StrEnum):
    MONETARY = "MONETARY"


class SPGlobalCampaignNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SPGlobalCountryCode(StrEnum):
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
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MK = "MK"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"


class SPGlobalMarketplace(StrEnum):
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


class SPGlobalPlacement(StrEnum):
    PRODUCT_PAGE = "PRODUCT_PAGE"  # Placements on the product detail page, and all nonsearch placements such as the add-to-cart page.
    REST_OF_SEARCH = "REST_OF_SEARCH"  # Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond.
    TOP_OF_SEARCH = "TOP_OF_SEARCH"  # Placements on the top row of the first-page search results.


class SPGlobalRecurrence(StrEnum):
    DAILY = "DAILY"


class SPGlobalSiteRestriction(StrEnum):
    AMAZON_BUSINESS = "AMAZON_BUSINESS"  # Restrict the ad to only show on Amazon Business.
    AMAZON_HAUL = "AMAZON_HAUL"  # Restrict the ad to only show on Amazon Haul.


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
    bidStrategy: Annotated[SPGlobalBidStrategy | str, lenient_enum(SPGlobalBidStrategy)] | None = Field(default=None)


class SPGlobalBudget(LenientModel):
    budgetType: Annotated[SPGlobalBudgetType | str, lenient_enum(SPGlobalBudgetType)]
    budgetValue: SPGlobalBudgetValue
    recurrenceTimePeriod: Annotated[SPGlobalRecurrence | str, lenient_enum(SPGlobalRecurrence)]


class SPGlobalBudgetValue(LenientModel):
    monetaryBudgetValue: SPGlobalMonetaryBudgetValue


class SPGlobalCampaign(LenientModel):
    adProduct: Annotated[SPGlobalAdProduct | str, lenient_enum(SPGlobalAdProduct)]
    autoCreationSettings: SPGlobalAutoCreationSettings
    autoScaleGlobalCampaign: (
        Annotated[SPGlobalAutoScaleGlobalCampaignSetting | str, lenient_enum(SPGlobalAutoScaleGlobalCampaignSetting)]
        | None
    ) = Field(default=None)
    budgets: list[SPGlobalBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    countries: list[Annotated[SPGlobalCountryCode | str, lenient_enum(SPGlobalCountryCode)]] | None = Field(
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
    marketplaceScope: Annotated[SPGlobalMarketplaceScope | str, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SPGlobalCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    siteRestrictions: list[Annotated[SPGlobalSiteRestriction | str, lenient_enum(SPGlobalSiteRestriction)]] | None = (
        Field(default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site")
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)]
    status: SPGlobalStatus | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPGlobalCampaignAdProductFilter(StrictModel):
    include: list[Annotated[SPGlobalAdProduct, lenient_enum(SPGlobalAdProduct)]] = Field(min_length=1, max_length=1)


class SPGlobalCampaignCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalCampaignCreate(StrictModel):
    adProduct: Annotated[SPGlobalAdProduct, lenient_enum(SPGlobalAdProduct)]
    autoCreationSettings: SPGlobalCreateAutoCreationSettings
    budgets: list[SPGlobalCreateBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    countries: list[Annotated[SPGlobalCountryCode, lenient_enum(SPGlobalCountryCode)]] | None = Field(
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
    marketplaceScope: Annotated[SPGlobalMarketplaceScope, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SPGlobalCreateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    siteRestrictions: list[Annotated[SPGlobalSiteRestriction, lenient_enum(SPGlobalSiteRestriction)]] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SPGlobalCreateState, lenient_enum(SPGlobalCreateState)]
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPGlobalCampaignMarketplaceScopeFilter(StrictModel):
    include: list[Annotated[SPGlobalMarketplaceScope, lenient_enum(SPGlobalMarketplaceScope)]] = Field(
        min_length=1, max_length=1
    )


class SPGlobalCampaignMultiStatusResponseWithPartialErrors(LenientModel):
    error: list[SPGlobalErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    partialSuccess: list[SPGlobalCampaignPartialIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPGlobalCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPGlobalCampaignMultiStatusSuccess(LenientModel):
    campaign: SPGlobalCampaign
    index: int = Field(ge=0, le=999)


class SPGlobalCampaignNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SPGlobalCampaignNameFilterType, lenient_enum(SPGlobalCampaignNameFilterType)]


class SPGlobalCampaignOptimizations(LenientModel):
    bidSettings: SPGlobalBidSettings | None = Field(default=None)


class SPGlobalCampaignPartialIndex(LenientModel):
    campaign: SPGlobalCampaign
    errors: list[SPGlobalError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SPGlobalCampaignPortfolioIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalCampaignStateFilter(StrictModel):
    include: list[Annotated[SPGlobalState, lenient_enum(SPGlobalState)]] = Field(min_length=1, max_length=3)


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
    countries: list[Annotated[SPGlobalCountryCode, lenient_enum(SPGlobalCountryCode)]] | None = Field(
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
    marketplaces: list[Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: SPGlobalUpdateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    siteRestrictions: list[Annotated[SPGlobalSiteRestriction, lenient_enum(SPGlobalSiteRestriction)]] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: Annotated[SPGlobalUpdateState, lenient_enum(SPGlobalUpdateState)] | None = Field(default=None)
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
    bidStrategy: Annotated[SPGlobalBidStrategy, lenient_enum(SPGlobalBidStrategy)] | None = Field(default=None)


class SPGlobalCreateBudget(StrictModel):
    budgetType: Annotated[SPGlobalBudgetType, lenient_enum(SPGlobalBudgetType)]
    budgetValue: SPGlobalCreateBudgetValue
    recurrenceTimePeriod: Annotated[SPGlobalRecurrence, lenient_enum(SPGlobalRecurrence)]


class SPGlobalCreateBudgetValue(StrictModel):
    monetaryBudgetValue: SPGlobalCreateMonetaryBudgetValue


class SPGlobalCreateCampaignOptimizations(StrictModel):
    bidSettings: SPGlobalCreateBidSettings | None = Field(default=None)


class SPGlobalCreateCampaignRequest(StrictModel):
    campaigns: list[SPGlobalCampaignCreate] = Field(min_length=1, max_length=1000)


class SPGlobalCreateMarketplaceCampaignConfigurations(StrictModel):
    marketplace: Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]
    overrides: SPGlobalCreateMarketplaceCampaignFieldOverrides


class SPGlobalCreateMarketplaceCampaignFieldOverrides(StrictModel):
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign")
    name: str | None = Field(default=None, description="The name of the campaign")
    optimizations: SPGlobalCreateCampaignOptimizations | None = Field(default=None)
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign")
    state: Annotated[SPGlobalState, lenient_enum(SPGlobalState)] | None = Field(default=None)
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPGlobalCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SPGlobalCreateMonetaryBudgetMarketplaceSetting(StrictModel):
    marketplace: Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]
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
    placement: Annotated[SPGlobalPlacement, lenient_enum(SPGlobalPlacement)]


class SPGlobalDeleteCampaignRequest(StrictModel):
    campaignIds: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalMarketplaceCampaignConfigurations(LenientModel):
    campaignId: str = Field(
        description="Represents marketplace campaign id (Ex: campaignId-US) associated to global campaign (Ex: campaignId-Global)"
    )
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
    overrides: SPGlobalMarketplaceCampaignFieldOverrides


class SPGlobalMarketplaceCampaignFieldOverrides(LenientModel):
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign")
    name: str | None = Field(default=None, description="The name of the campaign")
    optimizations: SPGlobalCampaignOptimizations | None = Field(default=None)
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign")
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)] | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SPGlobalMonetaryBudget(LenientModel):
    currencyCode: Annotated[SPGlobalCurrencyCode | str, lenient_enum(SPGlobalCurrencyCode)]
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SPGlobalMonetaryBudgetMarketplaceSetting(LenientModel):
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
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
    placement: Annotated[SPGlobalPlacement | str, lenient_enum(SPGlobalPlacement)]


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
    deliveryReasons: list[Annotated[SPGlobalDeliveryReason | str, lenient_enum(SPGlobalDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SPGlobalDeliveryStatus | str, lenient_enum(SPGlobalDeliveryStatus)]
    marketplaceSettings: list[SPGlobalStatusMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace level delivery status and reasons of global resources, for all the marketplaces the global resource is applicable in.",
    )


class SPGlobalStatusMarketplaceSetting(LenientModel):
    deliveryReasons: list[Annotated[SPGlobalDeliveryReason | str, lenient_enum(SPGlobalDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SPGlobalDeliveryStatus | str, lenient_enum(SPGlobalDeliveryStatus)]
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]


class SPGlobalUpdateBidAdjustments(StrictModel):
    placementBidAdjustments: list[SPGlobalCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )


class SPGlobalUpdateBidSettings(StrictModel):
    bidAdjustments: SPGlobalUpdateBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SPGlobalBidStrategy, lenient_enum(SPGlobalBidStrategy)] | None = Field(default=None)


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
