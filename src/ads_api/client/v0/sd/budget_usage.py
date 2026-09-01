"""BudgetUsage resource operations.

Generated from OpenAPI spec (tag: Budget Usage).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.budget_usage import (
    BudgetUsageCampaignRequest,
    BudgetUsageCampaignResponse,
)


class BudgetUsage(BaseResource):

    @overload
    async def sd_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def sd_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest | None = None, *, mode: Literal["pydantic"]
    ) -> BudgetUsageCampaignResponse: ...
    @overload
    async def sd_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sd_campaigns_budget_usage(
        self, body: BudgetUsageCampaignRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> BudgetUsageCampaignResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sd/campaigns/budget/usage",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sdcampaignbudgetusage.v1+json",
                "Accept": "application/vnd.sdcampaignbudgetusage.v1+json",
            },
        )
        return self._response(BudgetUsageCampaignResponse, resp, mode=mode)
