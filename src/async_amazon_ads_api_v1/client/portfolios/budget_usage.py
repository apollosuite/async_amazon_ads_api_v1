"""PortfolioBudgetUsage resource operations.

Generated from OpenAPI spec (tag: Budget Usage).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.portfolios.budget_usage import (
    BudgetUsagePortfolioRequest,
    BudgetUsagePortfolioResponse,
)


class PortfolioBudgetUsage(BaseResource):

    @overload
    async def portfolio_budget_usage(
        self, body: BudgetUsagePortfolioRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> BudgetUsagePortfolioResponse: ...
    @overload
    async def portfolio_budget_usage(
        self, body: BudgetUsagePortfolioRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def portfolio_budget_usage(
        self, body: BudgetUsagePortfolioRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def portfolio_budget_usage(
        self, body: BudgetUsagePortfolioRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> BudgetUsagePortfolioResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/portfolios/budget/usage",
            json=body.model_dump(mode="json", exclude_unset=True),
            headers={
                "Content-Type": "application/vnd.portfoliobudgetusage.v1+json",
                "Accept": "application/vnd.portfoliobudgetusage.v1+json",
            },
        )
        return self._response(BudgetUsagePortfolioResponse, resp, mode=mode)
