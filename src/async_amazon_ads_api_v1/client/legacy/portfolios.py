"""Portfolios resource operations — from Portfolios_prod_3p.json."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy.portfolios import (
    BudgetUsagePortfolioRequest,
    BudgetUsagePortfolioResponse,
    CreatePortfoliosRequestContent,
    CreatePortfoliosResponseContent,
    ListPortfoliosRequestContent,
    ListPortfoliosResponseContent,
    UpdatePortfoliosRequestContent,
    UpdatePortfoliosResponseContent,
)


class Portfolios(_ResourceBase):
    """Portfolio Management API — 投资组合管理。"""

    async def list(
        self,
        request: ListPortfoliosRequestContent | None = None,
    ) -> ListPortfoliosResponseContent:
        """获取投资组合列表。"""
        body = request.model_dump(exclude_none=True) if request else {}
        resp = await self._request("POST", "/portfolios/list", json=body)
        return self._response(ListPortfoliosResponseContent, resp)

    async def create(
        self,
        request: CreatePortfoliosRequestContent,
    ) -> CreatePortfoliosResponseContent:
        """创建投资组合。"""
        resp = await self._request(
            "POST",
            "/portfolios",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(CreatePortfoliosResponseContent, resp)

    async def update(
        self,
        request: UpdatePortfoliosRequestContent,
    ) -> UpdatePortfoliosResponseContent:
        """批量更新投资组合。"""
        resp = await self._request(
            "PUT",
            "/portfolios",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(UpdatePortfoliosResponseContent, resp)

    async def get_budget_usage(
        self,
        request: BudgetUsagePortfolioRequest,
    ) -> BudgetUsagePortfolioResponse:
        """获取投资组合预算使用情况。"""
        resp = await self._request(
            "POST",
            "/portfolios/budget/usage",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(BudgetUsagePortfolioResponse, resp)
