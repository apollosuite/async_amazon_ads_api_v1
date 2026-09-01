"""Portfolios resource operations.

Generated from OpenAPI spec (tag: portfolios).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.portfolios.portfolios import (
    BudgetUsagePortfolioRequest,
    BudgetUsagePortfolioResponse,
    CreatePortfoliosRequestContent,
    CreatePortfoliosResponseContent,
    ListPortfoliosRequestContent,
    ListPortfoliosResponseContent,
    UpdatePortfoliosRequestContent,
    UpdatePortfoliosResponseContent,
)


class Portfolios(BaseResource):

    @overload
    async def create_portfolios(
        self, body: CreatePortfoliosRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreatePortfoliosResponseContent: ...
    @overload
    async def create_portfolios(
        self, body: CreatePortfoliosRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_portfolios(
        self, body: CreatePortfoliosRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_portfolios(
        self, body: CreatePortfoliosRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> CreatePortfoliosResponseContent | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/portfolios",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spPortfolio.v3+json",
                "Accept": "application/vnd.spPortfolio.v3+json",
            },
        )
        return self._response(CreatePortfoliosResponseContent, resp, mode=mode)

    @overload
    async def list_portfolios(
        self, body: ListPortfoliosRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ListPortfoliosResponseContent: ...
    @overload
    async def list_portfolios(self, body: ListPortfoliosRequestContent, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def list_portfolios(self, body: ListPortfoliosRequestContent, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def list_portfolios(
        self, body: ListPortfoliosRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ListPortfoliosResponseContent | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/portfolios/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spPortfolio.v3+json",
                "Accept": "application/vnd.spPortfolio.v3+json",
            },
        )
        return self._response(ListPortfoliosResponseContent, resp, mode=mode)

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
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/portfolios/budget/usage",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.portfoliobudgetusage.v1+json",
                "Accept": "application/vnd.portfoliobudgetusage.v1+json",
            },
        )
        return self._response(BudgetUsagePortfolioResponse, resp, mode=mode)

    @overload
    async def update_portfolios(
        self, body: UpdatePortfoliosRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> UpdatePortfoliosResponseContent: ...
    @overload
    async def update_portfolios(
        self, body: UpdatePortfoliosRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_portfolios(
        self, body: UpdatePortfoliosRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_portfolios(
        self, body: UpdatePortfoliosRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> UpdatePortfoliosResponseContent | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "PUT",
            "/portfolios",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spPortfolio.v3+json",
                "Accept": "application/vnd.spPortfolio.v3+json",
            },
        )
        return self._response(UpdatePortfoliosResponseContent, resp, mode=mode)
