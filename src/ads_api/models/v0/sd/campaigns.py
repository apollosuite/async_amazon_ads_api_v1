"""Auto-generated models for Campaigns from Amazon Ads API v0."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    BaseCampaign,
    CampaignId,
    Tactic,
)


class BaseCampaignOut(LenientModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: str | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: str | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: str | None = Field(default=None, description="The state of the campaign.")
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )


class Campaign(LenientModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: str | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: str | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: str | None = Field(default=None, description="The state of the campaign.")
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )
    campaignId: CampaignId | None = Field(default=None)
    tactic: Annotated[Tactic | str, lenient_enum(Tactic)] | None = Field(default=None)
    deliveryProfile: str | None = Field(default=None)
    ruleBasedBudget: RuleBasedBudget | None = Field(default=None)


class CampaignResponse(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    campaignId: CampaignId | None = Field(default=None)


class CampaignResponseEx(LenientModel):
    campaignId: float | None = Field(default=None, description="The identifier of the campaign.")
    name: str | None = Field(default=None, description="The name of the campaign.")
    tactic: Annotated[Tactic | str, lenient_enum(Tactic)] | None = Field(default=None)
    budgetType: str | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    state: str | None = Field(default=None, description="The state of the campaign.")
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )
    servingStatus: str | None = Field(default=None, description="The status of the campaign.")
    costType: str | None = Field(default=None, description="Determines how the campaign will bid and charge.")
    creationDate: int | None = Field(default=None, description="Epoch date the campaign was created.")
    lastUpdatedDate: int | None = Field(
        default=None, description="Epoch date of the last update to any property associated with the campaign."
    )
    ruleBasedBudget: RuleBasedBudget | None = Field(default=None)


class CreateCampaign(StrictModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: str | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: str | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: str | None = Field(default=None, description="The state of the campaign.")
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )
    tactic: Annotated[Tactic, lenient_enum(Tactic)] | None = Field(default=None)


class RuleBasedBudget(LenientModel):
    isProcessing: bool | None = Field(default=None)
    applicableRuleName: str | None = Field(default=None)
    value: float | None = Field(default=None)
    applicableRuleId: str | None = Field(default=None)


class UpdateCampaign(StrictModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: str | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: str | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: str | None = Field(default=None, description="The state of the campaign.")
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )
    campaignId: CampaignId


__all__ = [
    "BaseCampaign",
    "BaseCampaignOut",
    "Campaign",
    "CampaignId",
    "CampaignResponse",
    "CampaignResponseEx",
    "CreateCampaign",
    "RuleBasedBudget",
    "Tactic",
    "UpdateCampaign",
]
