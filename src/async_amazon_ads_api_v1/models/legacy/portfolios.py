"""Portfolio Pydantic models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, RootModel


class Portfolio(BaseModel):
    """Individual portfolio."""

    model_config = ConfigDict(extra="ignore")

    portfolioId: str | None = None
    name: str | None = None
    budget: dict[str, Any] | None = None
    budgetType: str | None = None
    inBudget: bool | None = None
    state: str | None = None
    creationDate: int | None = None
    lastUpdatedDate: int | None = None
    budgetControls: dict[str, Any] | None = None


class PortfolioListRequest(BaseModel):
    """Request body for POST /portfolios/list."""

    model_config = ConfigDict(extra="ignore")

    includeExtendedDataFields: bool | None = None
    nextToken: str | None = None
    portfolioIdFilter: dict[str, list[str]] | None = None


PortfolioListResponse = RootModel[list[Portfolio]]


class PortfolioUpdateItem(BaseModel):
    """Individual item within a portfolio update multi-status response."""

    model_config = ConfigDict(extra="ignore")

    index: int
    errors: list[dict[str, Any]] = []


class PortfolioUpdateResponse(BaseModel):
    """Response for PUT /portfolios."""

    model_config = ConfigDict(extra="ignore")

    success: list[dict[str, Any]] = []
    error: list[PortfolioUpdateItem] = []


__all__ = [
    "Portfolio",
    "PortfolioListRequest",
    "PortfolioListResponse",
    "PortfolioUpdateItem",
    "PortfolioUpdateResponse",
]
