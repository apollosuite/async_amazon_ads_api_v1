"""Auto-generated models for Campaigns from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import (
    SPAdProduct,
    SPCreateState,
    SPCurrencyCode,
    SPDeliveryReason,
    SPDeliveryStatus,
    SPErrorCode,
    SPMarketplace,
    SPMarketplaceScope,
    SPState,
    SPUpdateState,
)
from .shared import SPCreateTag, SPErrorsIndex, SPStatus, SPTag


class SPAutoScaleGlobalCampaignSetting(StrEnum):
    """
    **AutoScaleGlobalCampaignSetting Enum:**

    | AutoScaleGlobalCampaignSetting | Description |
    |------|------|
    | `AUTO` | Auto scale global campaign to new marketplaces |
    | `MANUAL` | Manually scale global campaign to new marketplaces |
    """

    AUTO = "AUTO"
    MANUAL = "MANUAL"


class SPBidStrategy(StrEnum):
    """
    **BidStrategy Enum:**

    | BidStrategy | Description |
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


class SPBudgetType(StrEnum):
    MONETARY = "MONETARY"


class SPCampaignNameFilterType(StrEnum):
    """
    **CampaignNameFilterType Enum:**
    | CampaignNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


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
    """
    **CreativeBidAdjustmentType Enum:**

    | CreativeBidAdjustmentType | Description |
    |------|------|
    | `SPOTLIGHT` | SPOTLIGHT Video Asset. |
    """

    SPOTLIGHT = "SPOTLIGHT"


class SPMarketplaceBudgetAllocation(StrEnum):
    """
    **MarketplaceBudgetAllocation Enum:**

    | MarketplaceBudgetAllocation | Description |
    |------|------|
    | `AUTO` | Auto distribute global budget to marketplaces in global campaign |
    | `MANUAL` | Manually distribute global budget to marketplaces in global campaign |
    """

    AUTO = "AUTO"
    MANUAL = "MANUAL"


class SPOffAmazonBudgetControlStrategy(StrEnum):
    """
    **OffAmazonBudgetControlStrategy Enum:**

    | OffAmazonBudgetControlStrategy | Description |
    |------|------|
    | `MAXIMIZE_REACH` | Maximize the reach of off-Amazon inventory within the budget. |
    | `MINIMIZE_SPEND` | Minimize spend on off-Amazon inventory while maintaining delivery. |
    """

    MAXIMIZE_REACH = "MAXIMIZE_REACH"
    MINIMIZE_SPEND = "MINIMIZE_SPEND"


class SPPlacement(StrEnum):
    """
    **Placement Enum:**

    | Placement | Description |
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


class SPRecurrence(StrEnum):
    DAILY = "DAILY"


class SPSiteRestriction(StrEnum):
    """
    **SiteRestriction Enum:**

    | SiteRestriction | Description |
    |------|------|
    | `AMAZON_BUSINESS` | Restrict the ad to only show on Amazon Business. |
    | `AMAZON_HAUL` | Restrict the ad to only show on Amazon Haul. |
    """

    AMAZON_BUSINESS = "AMAZON_BUSINESS"
    AMAZON_HAUL = "AMAZON_HAUL"


class SPAudienceBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="allow")

    audienceId: str = Field(description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(
        description="The selection of the percentage change associated with a given audience and bid adjustment settings."
    )


class SPAutoCreationSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    autoCreateTargets: bool = Field(
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised."
    )
    autoManageCampaign: bool | None = Field(
        default=None, description="Flag that allows Amazon to manage the lifecycle of your Campaign."
    )


class SPBidAdjustments(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SPBidSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    bidAdjustments: SPBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SPBidStrategy | str, lenient_enum(SPBidStrategy)] | None = Field(default=None)


class SPBudget(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetType: Annotated[SPBudgetType | str, lenient_enum(SPBudgetType)]
    budgetValue: SPBudgetValue
    recurrenceTimePeriod: Annotated[SPRecurrence | str, lenient_enum(SPRecurrence)]


class SPBudgetSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    marketplaceBudgetAllocation: (
        Annotated[SPMarketplaceBudgetAllocation | str, lenient_enum(SPMarketplaceBudgetAllocation)] | None
    ) = Field(default=None)
    offAmazonBudgetControlStrategy: (
        Annotated[SPOffAmazonBudgetControlStrategy | str, lenient_enum(SPOffAmazonBudgetControlStrategy)] | None
    ) = Field(default=None)


class SPBudgetValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    monetaryBudgetValue: SPMonetaryBudgetValue | None = None


class SPCampaign(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SPCampaignAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPAdProduct | str, lenient_enum(SPAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_PRODUCTS` | Sponsored Products ad product. |
""",
    )


class SPCampaignCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=1000)


class SPCampaignCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

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


class SPCampaignMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[SPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPCampaignMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaign: SPCampaign
    index: int = Field(ge=0, le=999)


class SPCampaignNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SPCampaignNameFilterType | str, lenient_enum(SPCampaignNameFilterType)]


class SPCampaignOptimizations(BaseModel):
    model_config = ConfigDict(extra="allow")

    bidSettings: SPBidSettings | None = Field(default=None)
    budgetSettings: SPBudgetSettings | None = Field(default=None)


class SPCampaignPortfolioIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SPCampaignStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SPState | str, lenient_enum(SPState)]] = Field(
        min_length=1,
        max_length=3,
        description="""
**State Enum:**
| State | Description |
| --- | --- |
| `ENABLED` | The object is set active by user and eligible for delivery. |
| `PAUSED` | The object is stopped by user and not eligible for delivery. |
| `ARCHIVED` | The object is permanently stopped and cannot be reactivated. Terminal end state. |
""",
    )


class SPCampaignSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaigns: list[SPCampaign] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPCampaignUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

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


class SPCreateAudienceBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    audienceId: str = Field(description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(
        description="The selection of the percentage change associated with a given audience and bid adjustment settings."
    )


class SPCreateAutoCreationSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool = Field(
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised."
    )
    autoManageCampaign: bool | None = Field(
        default=None, description="Flag that allows Amazon to manage the lifecycle of your Campaign."
    )


class SPCreateBidAdjustments(BaseModel):
    model_config = ConfigDict(extra="forbid")

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


class SPCreateBidSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SPCreateBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SPBidStrategy | str, lenient_enum(SPBidStrategy)] | None = Field(default=None)


class SPCreateBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetType: Annotated[SPBudgetType | str, lenient_enum(SPBudgetType)]
    budgetValue: SPCreateBudgetValue
    recurrenceTimePeriod: Annotated[SPRecurrence | str, lenient_enum(SPRecurrence)]


class SPCreateBudgetSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: (
        Annotated[SPOffAmazonBudgetControlStrategy | str, lenient_enum(SPOffAmazonBudgetControlStrategy)] | None
    ) = Field(default=None)


class SPCreateBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SPCreateMonetaryBudgetValue | None = None


class SPCreateCampaignOptimizations(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bidSettings: SPCreateBidSettings | None = Field(default=None)
    budgetSettings: SPCreateBudgetSettings | None = Field(default=None)


class SPCreateCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaignCreate] = Field(min_length=1, max_length=1000)


class SPCreateCreativeBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    creativeType: Annotated[SPCreativeBidAdjustmentType | str, lenient_enum(SPCreativeBidAdjustmentType)] | None = (
        Field(default=None)
    )
    percentage: int = Field(
        description="The selection of the percentage change associated with the creative type and bid adjustment settings."
    )


class SPCreateMonetaryBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SPCreateMonetaryBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SPCreateMonetaryBudget


class SPCreatePlacementBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: Annotated[SPPlacement | str, lenient_enum(SPPlacement)]


class SPCreativeBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="allow")

    creativeType: Annotated[SPCreativeBidAdjustmentType | str, lenient_enum(SPCreativeBidAdjustmentType)] | None = (
        Field(default=None)
    )
    percentage: int = Field(
        description="The selection of the percentage change associated with the creative type and bid adjustment settings."
    )


class SPDeleteCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaignIds: list[str] = Field(min_length=1, max_length=1000)


class SPMonetaryBudget(BaseModel):
    model_config = ConfigDict(extra="allow")

    currencyCode: Annotated[SPCurrencyCode | str, lenient_enum(SPCurrencyCode)]
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SPMonetaryBudgetValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    monetaryBudget: SPMonetaryBudget


class SPPlacementBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="allow")

    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: Annotated[SPPlacement | str, lenient_enum(SPPlacement)]


class SPQueryCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProductFilter: SPCampaignAdProductFilter
    campaignIdFilter: SPCampaignCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nameFilter: SPCampaignNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    portfolioIdFilter: SPCampaignPortfolioIdFilter | None = Field(default=None)
    stateFilter: SPCampaignStateFilter | None = Field(default=None)


class SPUpdateBidAdjustments(BaseModel):
    model_config = ConfigDict(extra="forbid")

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


class SPUpdateBidSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SPUpdateBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SPBidStrategy | str, lenient_enum(SPBidStrategy)] | None = Field(default=None)


class SPUpdateBudgetSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: (
        Annotated[SPOffAmazonBudgetControlStrategy | str, lenient_enum(SPOffAmazonBudgetControlStrategy)] | None
    ) = Field(default=None)


class SPUpdateCampaignOptimizations(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bidSettings: SPUpdateBidSettings | None = Field(default=None)
    budgetSettings: SPUpdateBudgetSettings | None = Field(default=None)


class SPUpdateCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaignUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SPAdProduct",
    "SPAutoScaleGlobalCampaignSetting",
    "SPBidStrategy",
    "SPBudgetType",
    "SPCampaignAdProductFilter",
    "SPCampaignCampaignIdFilter",
    "SPCampaignCreate",
    "SPCampaignNameFilter",
    "SPCampaignNameFilterType",
    "SPCampaignPortfolioIdFilter",
    "SPCampaignStateFilter",
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
    "SPCreativeBidAdjustmentType",
    "SPCurrencyCode",
    "SPDeleteCampaignRequest",
    "SPDeliveryReason",
    "SPDeliveryStatus",
    "SPErrorCode",
    "SPMarketplace",
    "SPMarketplaceBudgetAllocation",
    "SPMarketplaceScope",
    "SPOffAmazonBudgetControlStrategy",
    "SPPlacement",
    "SPQueryCampaignRequest",
    "SPRecurrence",
    "SPSiteRestriction",
    "SPState",
    "SPUpdateBidAdjustments",
    "SPUpdateBidSettings",
    "SPUpdateBudgetSettings",
    "SPUpdateCampaignOptimizations",
    "SPUpdateCampaignRequest",
    "SPUpdateState",
]
