"""campaign models."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import (
        SPAdProduct,
        SPAutoScaleGlobalCampaignSetting,
        SPCampaignNameFilterType,
        SPCountryCode,
        SPCreateState,
        SPMarketplace,
        SPMarketplaceScope,
        SPSiteRestriction,
        SPState,
        SPUpdateState,
    )
    from ._shared import (
        ErrorsIndex,
        SPAutoCreationSettings,
        SPBidSettings,
        SPBudget,
        SPBudgetSettings,
        SPCreateAutoCreationSettings,
        SPCreateBidSettings,
        SPCreateBudget,
        SPCreateBudgetSettings,
        SPCreateTag,
        SPStatus,
        SPTag,
        SPUpdateBidSettings,
        SPUpdateBudgetSettings,
    )


class SPAdCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


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


class SPCreateCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidSettings: SPCreateBidSettings | None = None
    budgetSettings: SPCreateBudgetSettings | None = None


class SPCreateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaignCreate] | None = None


class SPDeleteCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaignIds: list[str] | None = None


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


class SPTargetCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPUpdateCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidSettings: SPUpdateBidSettings | None = None
    budgetSettings: SPUpdateBudgetSettings | None = None


class SPUpdateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaignUpdate] | None = None
