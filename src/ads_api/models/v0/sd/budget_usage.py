"""Auto-generated models for Budget Usage from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class BudgetUsageCampaign(LenientModel):
    budgetUsagePercent: float | None = Field(
        default=None, description="Budget usage percentage (spend / available budget) for the given budget policy."
    )
    campaignId: str | None = Field(default=None, description="ID of requested resource")
    usageUpdatedTimestamp: datetime | None = Field(default=None, description="Last evaluation time for budget usage")
    index: float | None = Field(default=None, description="An index to maintain order of the campaignIds")
    budget: float | None = Field(default=None, description="Budget amount of resource requested")


class BudgetUsageCampaignBatchErrorResult(LenientModel):
    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    campaignId: str | None = Field(default=None, description="ID of requested resource")
    index: float | None = Field(default=None, description="An index to maintain order of the campaignIds")
    details: str | None = Field(default=None, description="A human-readable description of the response.")


class BudgetUsageCampaignRequest(StrictModel):
    campaignIds: list[str] | None = Field(
        default=None, min_length=1, max_length=100, description="A list of campaign IDs"
    )


class BudgetUsageCampaignResponse(LenientModel):
    success: list[BudgetUsageCampaign] | None = Field(
        default=None, description="List of budget usage percentages that were successfully pulled"
    )
    error: list[BudgetUsageCampaignBatchErrorResult] | None = Field(
        default=None, description="List of budget usage percentages that failed to pull"
    )


__all__ = [
    "BudgetUsageCampaign",
    "BudgetUsageCampaignBatchErrorResult",
    "BudgetUsageCampaignRequest",
    "BudgetUsageCampaignResponse",
]
