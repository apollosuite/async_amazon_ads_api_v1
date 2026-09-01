"""BudgetUsage resource operations.

Generated from OpenAPI spec (tag: Budget Usage).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.budget_usage import (
    BudgetUsageCampaignRequest,
    BudgetUsageCampaignResponse,
)


class BudgetUsage(BaseResource):

    @overload
    async def sp_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def sp_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest, *, mode: Literal["pydantic"]
    ) -> BudgetUsageCampaignResponse: ...
    @overload
    async def sp_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sp_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> BudgetUsageCampaignResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/campaigns/budget/usage",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spcampaignbudgetusage.v1+json",
                "Accept": "application/vnd.spcampaignbudgetusage.v1+json",
            },
        )
        return self._response(BudgetUsageCampaignResponse, resp, mode=mode)
