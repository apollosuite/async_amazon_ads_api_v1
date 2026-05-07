"""campaign models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class SPCampaign(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProduct: dict[str, Any]
    autoCreationSettings: dict[str, Any]
    autoScaleGlobalCampaign: dict[str, Any] | None = None
    budgets: list[
        dict[str, Any]
    ]  # The object containing budget details for the campaign (for campaigns that suppor
    campaignId: str  # A unique identifier for a campaign.
    countries: list[dict[str, Any]] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sp
    )
    creationDateTime: datetime  # The date time that the campaign was created.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    globalCampaignId: str | None = (
        None  # The global campaign identifier that manages this marketplace campaign.
    )
    lastUpdatedDateTime: datetime  # The date time that the campaign was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]] | None = (
        None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc,
    )
    name: str  # The name of the campaign.
    optimizations: dict[str, Any] | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    siteRestrictions: list[dict[str, Any]] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime  # The start date time for the campaign.
    state: dict[str, Any]
    status: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = (
        None  # Open ended labels with a key value pair applied to the campaign
    )


class SPCampaignCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProduct: dict[str, Any]
    autoCreationSettings: dict[str, Any]
    budgets: list[
        dict[str, Any]
    ]  # The object containing budget details for the campaign (for campaigns that suppor
    countries: list[dict[str, Any]] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sp
    )
    endDateTime: datetime | None = None  # The end date time for the campaign.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]] | None = (
        None  # This represent retail domains such as Amazon.com, Amazon.co.uk, Amazon.mx, etc,
    )
    name: str  # The name of the campaign.
    optimizations: dict[str, Any] | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    siteRestrictions: list[dict[str, Any]] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime  # The start date time for the campaign.
    state: dict[str, Any]
    tags: list[dict[str, Any]] | None = (
        None  # Open ended labels with a key value pair applied to the campaign
    )


class SPCampaignMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaign: dict[str, Any]
    index: int


class SPCampaignOptimizations(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidSettings: dict[str, Any] | None = None
    budgetSettings: dict[str, Any] | None = None


class SPCampaignUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    budgets: list[dict[str, Any]] | None = (
        None  # The object containing budget details for the campaign (for campaigns that suppor
    )
    campaignId: str  # A unique identifier for a campaign.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    name: str | None = None  # The name of the campaign.
    optimizations: dict[str, Any] | None = None
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    siteRestrictions: list[dict[str, Any]] | None = None  # Restrict the ad to a particular site
    startDateTime: datetime | None = None  # The start date time for the campaign.
    state: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = (
        None  # Open ended labels with a key value pair applied to the campaign
    )
