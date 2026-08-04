"""Portfolios resource operations.

Generated from OpenAPI spec (tag: Portfolios).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.portfolios.portfolios import (
    CreatePortfoliosRequestContent,
    CreatePortfoliosResponseContent,
    ListPortfoliosRequestContent,
    ListPortfoliosResponseContent,
    UpdatePortfoliosRequestContent,
    UpdatePortfoliosResponseContent,
)


class Portfolios(BaseResource):

    async def create_portfolios(self, body: CreatePortfoliosRequestContent) -> CreatePortfoliosResponseContent:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/portfolios",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.spPortfolio.v3+json",
                "Accept": "application/vnd.spPortfolio.v3+json",
            },
        )
        return self._response(CreatePortfoliosResponseContent, resp)

    async def update_portfolios(self, body: UpdatePortfoliosRequestContent) -> UpdatePortfoliosResponseContent:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "PUT",
            "/portfolios",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.spPortfolio.v3+json",
                "Accept": "application/vnd.spPortfolio.v3+json",
            },
        )
        return self._response(UpdatePortfoliosResponseContent, resp)

    async def list_portfolios(self, body: ListPortfoliosRequestContent) -> ListPortfoliosResponseContent:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/portfolios/list",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.spPortfolio.v3+json",
                "Accept": "application/vnd.spPortfolio.v3+json",
            },
        )
        return self._response(ListPortfoliosResponseContent, resp)
