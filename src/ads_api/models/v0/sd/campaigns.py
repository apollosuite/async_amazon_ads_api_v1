"""Auto-generated models for Campaigns from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    BaseCampaign,
    BaseCampaignBudgetType,
    BaseCampaignCostType,
    BaseCampaignState,
    CampaignDeliveryProfile,
    CampaignId,
    Tactic,
)


class CampaignResponseExBudgetType(StrEnum):
    """
    The time period over which the amount specified in the `budget` property is allocated.
    """

    daily = "daily"


class CampaignResponseExCostType(StrEnum):
    """
    Determines how the campaign will bid and charge.
    |Name|Description|
    |----|----------|-----------|
    |cpc |[Default] The performance of this campaign is measured by the clicks triggered by the ad.|
    |vcpm|The performance of this campaign is measured by the viewed impressions triggered by the ad. $1 is the minimum bid for vCPM.|
    """

    cpc = "cpc"
    vcpm = "vcpm"


class CampaignResponseExServingStatus(StrEnum):
    """
    The status of the campaign.
    """

    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    PENDING_START_DATE = "PENDING_START_DATE"
    ENDED = "ENDED"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    INELIGIBLE = "INELIGIBLE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"


class CampaignResponseExState(StrEnum):
    """
    The state of the campaign.
    """

    enabled = "enabled"
    paused = "paused"
    archived = "archived"


class BaseCampaignOut(LenientModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: Annotated[BaseCampaignBudgetType | str, lenient_enum(BaseCampaignBudgetType)] | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: Annotated[BaseCampaignCostType | str, lenient_enum(BaseCampaignCostType)] | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
|Name|Description|
|----|----------|
|cpc |[Default] The performance of this campaign is measured by the clicks triggered by the ad.|
|vcpm |The performance of this campaign is measured by the viewed impressions triggered by the ad. |

To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: Annotated[BaseCampaignState | str, lenient_enum(BaseCampaignState)] | None = Field(
        default=None, description="The state of the campaign."
    )
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )


class Campaign(LenientModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: Annotated[BaseCampaignBudgetType | str, lenient_enum(BaseCampaignBudgetType)] | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: Annotated[BaseCampaignCostType | str, lenient_enum(BaseCampaignCostType)] | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
|Name|Description|
|----|----------|
|cpc |[Default] The performance of this campaign is measured by the clicks triggered by the ad.|
|vcpm |The performance of this campaign is measured by the viewed impressions triggered by the ad. |

To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: Annotated[BaseCampaignState | str, lenient_enum(BaseCampaignState)] | None = Field(
        default=None, description="The state of the campaign."
    )
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )
    campaignId: CampaignId | None = Field(default=None)
    tactic: Annotated[Tactic | str, lenient_enum(Tactic)] | None = Field(default=None)
    deliveryProfile: Annotated[CampaignDeliveryProfile | str, lenient_enum(CampaignDeliveryProfile)] | None = Field(
        default=None
    )
    ruleBasedBudget: RuleBasedBudget | None = Field(default=None)


class CampaignResponse(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    campaignId: CampaignId | None = Field(default=None)


class CampaignResponseEx(LenientModel):
    campaignId: float | None = Field(default=None, description="The identifier of the campaign.")
    name: str | None = Field(default=None, description="The name of the campaign.")
    tactic: Annotated[Tactic | str, lenient_enum(Tactic)] | None = Field(default=None)
    budgetType: Annotated[CampaignResponseExBudgetType | str, lenient_enum(CampaignResponseExBudgetType)] | None = (
        Field(
            default=None,
            description="The time period over which the amount specified in the `budget` property is allocated.",
        )
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    state: Annotated[CampaignResponseExState | str, lenient_enum(CampaignResponseExState)] | None = Field(
        default=None, description="The state of the campaign."
    )
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )
    servingStatus: (
        Annotated[CampaignResponseExServingStatus | str, lenient_enum(CampaignResponseExServingStatus)] | None
    ) = Field(default=None, description="The status of the campaign.")
    costType: Annotated[CampaignResponseExCostType | str, lenient_enum(CampaignResponseExCostType)] | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
|Name|Description|
|----|----------|-----------|
|cpc |[Default] The performance of this campaign is measured by the clicks triggered by the ad.|
|vcpm|The performance of this campaign is measured by the viewed impressions triggered by the ad. $1 is the minimum bid for vCPM.|
""",
    )
    creationDate: int | None = Field(default=None, description="Epoch date the campaign was created.")
    lastUpdatedDate: int | None = Field(
        default=None, description="Epoch date of the last update to any property associated with the campaign."
    )
    ruleBasedBudget: RuleBasedBudget | None = Field(default=None)


class CreateCampaign(StrictModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: Annotated[BaseCampaignBudgetType | str, lenient_enum(BaseCampaignBudgetType)] | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: Annotated[BaseCampaignCostType | str, lenient_enum(BaseCampaignCostType)] | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
|Name|Description|
|----|----------|
|cpc |[Default] The performance of this campaign is measured by the clicks triggered by the ad.|
|vcpm |The performance of this campaign is measured by the viewed impressions triggered by the ad. |

To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: Annotated[BaseCampaignState | str, lenient_enum(BaseCampaignState)] | None = Field(
        default=None, description="The state of the campaign."
    )
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )
    tactic: Annotated[Tactic | str, lenient_enum(Tactic)] | None = Field(default=None)


class RuleBasedBudget(LenientModel):
    isProcessing: bool | None = Field(default=None)
    applicableRuleName: str | None = Field(default=None)
    value: float | None = Field(default=None)
    applicableRuleId: str | None = Field(default=None)


class UpdateCampaign(StrictModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: Annotated[BaseCampaignBudgetType | str, lenient_enum(BaseCampaignBudgetType)] | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: Annotated[BaseCampaignCostType | str, lenient_enum(BaseCampaignCostType)] | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
|Name|Description|
|----|----------|
|cpc |[Default] The performance of this campaign is measured by the clicks triggered by the ad.|
|vcpm |The performance of this campaign is measured by the viewed impressions triggered by the ad. |

To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: Annotated[BaseCampaignState | str, lenient_enum(BaseCampaignState)] | None = Field(
        default=None, description="The state of the campaign."
    )
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )
    campaignId: CampaignId


__all__ = [
    "BaseCampaign",
    "BaseCampaignBudgetType",
    "BaseCampaignCostType",
    "BaseCampaignOut",
    "BaseCampaignState",
    "Campaign",
    "CampaignDeliveryProfile",
    "CampaignId",
    "CampaignResponse",
    "CampaignResponseEx",
    "CampaignResponseExBudgetType",
    "CampaignResponseExCostType",
    "CampaignResponseExServingStatus",
    "CampaignResponseExState",
    "CreateCampaign",
    "RuleBasedBudget",
    "Tactic",
    "UpdateCampaign",
]
