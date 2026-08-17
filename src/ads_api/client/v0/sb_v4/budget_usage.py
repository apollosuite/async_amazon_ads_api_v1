"""BudgetUsage resource operations.

Generated from OpenAPI spec (tag: Budget usage).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.budget_usage import (
    BudgetUsageCampaignRequest,
    BudgetUsageCampaignResponse,
)


class BudgetUsage(BaseResource):

    @overload
    async def sb_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> BudgetUsageCampaignResponse: ...
    @overload
    async def sb_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> BudgetUsageCampaignResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sb/campaigns/budget/usage",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbcampaignbudgetusage.v1+json",
                "Accept": "application/vnd.sbcampaignbudgetusage.v1+json",
            },
        )
        return self._response(BudgetUsageCampaignResponse, resp, mode=mode)
