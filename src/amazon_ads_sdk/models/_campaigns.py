"""campaign models."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import (
        SPAdProduct,
        SPAutoScaleGlobalCampaignSetting,
        SPCountryCode,
        SPCreateState,
        SPMarketplace,
        SPMarketplaceScope,
        SPSiteRestriction,
        SPState,
        SPUpdateState,
    )
    from ._shared import (
        SPAutoCreationSettings,
        SPBidSettings,
        SPBudget,
        SPBudgetSettings,
        SPCreateAutoCreationSettings,
        SPCreateBudget,
        SPCreateCampaignOptimizations,
        SPCreateTag,
        SPStatus,
        SPTag,
        SPUpdateCampaignOptimizations,
    )


class SPCampaign(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProduct: SPAdProduct
    autoCreationSettings: SPAutoCreationSettings
    autoScaleGlobalCampaign: SPAutoScaleGlobalCampaignSetting | None = None
    budgets: list[
        SPBudget
    ]  # The object containing budget details for the campaign (for campaigns that suppor
    campaignId: str  # A unique identifier for a campaign.
    countries: list[SPCountryCode] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sp
    )
    creationDateTime: datetime  # The date time that the campaign was created.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    globalCampaignId: str | None = (
        None  # The global campaign identifier that manages this marketplace campaign.
    )
    lastUpdatedDateTime: datetime  # The date time that the campaign was last updated.
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[SPMarketplace] | None = (
        None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc,
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


class SPCampaignCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProduct: SPAdProduct
    autoCreationSettings: SPCreateAutoCreationSettings
    budgets: list[
        SPCreateBudget
    ]  # The object containing budget details for the campaign (for campaigns that suppor
    countries: list[SPCountryCode] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sp
    )
    endDateTime: datetime | None = None  # The end date time for the campaign.
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[SPMarketplace] | None = (
        None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc,
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


class SPCampaignMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaign: SPCampaign
    index: int


class SPCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidSettings: SPBidSettings | None = None
    budgetSettings: SPBudgetSettings | None = None


class SPCampaignUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    budgets: list[SPCreateBudget] | None = (
        None  # The object containing budget details for the campaign (for campaigns that suppor
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
