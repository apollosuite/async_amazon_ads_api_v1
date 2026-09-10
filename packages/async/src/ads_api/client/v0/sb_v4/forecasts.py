"""Forecasts resource operations.

Generated from OpenAPI spec (tag: Forecasts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.forecasts import (
    SBCampaignPerformanceForecastsRequestContent,
    SBCampaignPerformanceForecastsResponseContent,
)


class Forecasts(BaseResource):

    @overload
    async def campaign_performance_forecasts(
        self, body: SBCampaignPerformanceForecastsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def campaign_performance_forecasts(
        self, body: SBCampaignPerformanceForecastsRequestContent, *, mode: Literal["pydantic"]
    ) -> SBCampaignPerformanceForecastsResponseContent: ...
    @overload
    async def campaign_performance_forecasts(
        self, body: SBCampaignPerformanceForecastsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def campaign_performance_forecasts(
        self, body: SBCampaignPerformanceForecastsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBCampaignPerformanceForecastsResponseContent | dict[str, Any] | httpx.Response:
        """Returns forecasts for a list of new campaigns specified in SB forecast request. Currently only one new campaign is supported."""

        resp = await self._request(
            "POST",
            "/sb/forecasts",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbforecasting.v4+json",
                "Accept": "application/vnd.sbforecasting.v4+json",
            },
        )
        return self._response(SBCampaignPerformanceForecastsResponseContent, resp, mode=mode)
