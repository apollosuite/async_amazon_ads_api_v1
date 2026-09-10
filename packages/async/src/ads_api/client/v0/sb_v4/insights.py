"""Insights resource operations.

Generated from OpenAPI spec (tag: Insights).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.insights import (
    SBInsightsCampaignInsightsRequestContent,
    SBInsightsCampaignInsightsResponseContent,
)


class Insights(BaseResource):

    @overload
    async def insights_campaign_insights(
        self,
        body: SBInsightsCampaignInsightsRequestContent,
        *,
        mode: Literal["dict"] = "dict",
        next_token: str | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def insights_campaign_insights(
        self,
        body: SBInsightsCampaignInsightsRequestContent,
        *,
        mode: Literal["pydantic"],
        next_token: str | None = None,
    ) -> SBInsightsCampaignInsightsResponseContent: ...
    @overload
    async def insights_campaign_insights(
        self, body: SBInsightsCampaignInsightsRequestContent, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def insights_campaign_insights(
        self,
        body: SBInsightsCampaignInsightsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        next_token: str | None = None,
    ) -> SBInsightsCampaignInsightsResponseContent | dict[str, Any] | httpx.Response:
        """Creates campaign level insights. Insights will be provided for passed in campaign parameters."""

        params = {
            "nextToken": next_token,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request(
            "POST",
            "/sb/campaigns/insights",
            params=params,
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbinsights.v4+json",
                "Accept": "application/vnd.sbinsights.v4+json",
            },
        )
        return self._response(SBInsightsCampaignInsightsResponseContent, resp, mode=mode)
