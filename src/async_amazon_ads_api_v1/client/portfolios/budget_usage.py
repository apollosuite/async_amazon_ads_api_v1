"""PortfolioBudgetUsage resource operations.

Generated from OpenAPI spec (tag: Budget Usage).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.portfolios.budget_usage import (
    BudgetUsagePortfolioRequest,
    BudgetUsagePortfolioResponse,
)


class PortfolioBudgetUsage(BaseResource):

    async def portfolio_budget_usage(self, body: BudgetUsagePortfolioRequest) -> BudgetUsagePortfolioResponse:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/portfolios/budget/usage",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.portfoliobudgetusage.v1+json",
                "Accept": "application/vnd.portfoliobudgetusage.v1+json",
            },
        )
        return self._response(BudgetUsagePortfolioResponse, resp)
