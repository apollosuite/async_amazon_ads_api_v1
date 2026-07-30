"""Auto-generated models for Budget Usage from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class BudgetUsagePortfolio(BaseModel):
    model_config = ConfigDict(extra="allow")

    budget: int | None = Field(default=None, description="Budget amount of resource requested")
    budgetUsagePercent: int | None = Field(
        default=None, description="Budget usage percentage (spend / available budget) for the given budget policy."
    )
    index: int | None = Field(default=None, description="An index to maintain order of the portfolioIds")
    portfolioId: str | None = Field(default=None, description="ID of requested resource")
    usageUpdatedTimestamp: datetime | None = Field(default=None, description="Last evaluation time for budget usage")


class BudgetUsagePortfolioBatchErrorResult(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")
    index: int | None = Field(default=None, description="An index to maintain order of the portfolioIds")
    portfolioId: str | None = Field(default=None, description="ID of requested resource")


class BudgetUsagePortfolioRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    portfolioIds: list[str] | None = Field(
        default=None, min_length=1, max_length=100, description="A list of portfolio IDs."
    )


class BudgetUsagePortfolioResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[BudgetUsagePortfolioBatchErrorResult] | None = Field(
        default=None, description="List of budget usage percentages that failed to pull"
    )
    success: list[BudgetUsagePortfolio] | None = Field(
        default=None, description="List of budget usage percentages that were successfully pulled"
    )


__all__ = ["BudgetUsagePortfolioRequest"]
