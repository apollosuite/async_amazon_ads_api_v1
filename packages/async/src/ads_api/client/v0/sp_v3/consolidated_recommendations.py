"""ConsolidatedRecommendations resource operations.

Generated from OpenAPI spec (tag: Consolidated Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.consolidated_recommendations import (
    GetCampaignRecommendationsRequestV2,
    GetCampaignRecommendationsResponse,
    GetCampaignRecommendationsResponseV2,
)


class ConsolidatedRecommendations(BaseResource):

    @overload
    async def fetch_campaign_recommendations(
        self, body: GetCampaignRecommendationsRequestV2 | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def fetch_campaign_recommendations(
        self, body: GetCampaignRecommendationsRequestV2 | None = None, *, mode: Literal["pydantic"]
    ) -> GetCampaignRecommendationsResponseV2: ...
    @overload
    async def fetch_campaign_recommendations(
        self, body: GetCampaignRecommendationsRequestV2 | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def fetch_campaign_recommendations(
        self,
        body: GetCampaignRecommendationsRequestV2 | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> GetCampaignRecommendationsResponseV2 | dict[str, Any] | httpx.Response:
        """Gets the top consolidated recommendations across bid, budget, targeting for SP campaigns given an advertiser profile id. The recommendations are refreshed everyday."""

        resp = await self._request(
            "POST",
            "/sp/campaign/recommendations",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spgetcampaignrecommendationsrequest.v2+json",
                "Accept": "application/vnd.spgetcampaignrecommendationsrequest.v2+json",
            },
        )
        return self._response(GetCampaignRecommendationsResponseV2, resp, mode=mode)

    @overload
    async def get_campaign_recommendations(
        self,
        *,
        mode: Literal["dict"] = "dict",
        campaign_ids: list[str] | None = None,
        next_token: str | None = None,
        max_results: str | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def get_campaign_recommendations(
        self,
        *,
        mode: Literal["pydantic"],
        campaign_ids: list[str] | None = None,
        next_token: str | None = None,
        max_results: str | None = None,
    ) -> GetCampaignRecommendationsResponse: ...
    @overload
    async def get_campaign_recommendations(
        self,
        *,
        mode: Literal["raw"],
        campaign_ids: list[str] | None = None,
        next_token: str | None = None,
        max_results: str | None = None,
    ) -> httpx.Response: ...
    async def get_campaign_recommendations(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        campaign_ids: list[str] | None = None,
        next_token: str | None = None,
        max_results: str | None = None,
    ) -> GetCampaignRecommendationsResponse | dict[str, Any] | httpx.Response:
        """Gets the top consolidated recommendations across bid, budget, targeting for SP campaigns given an advertiser profile id. The recommendations are refreshed everyday."""

        params = {
            "campaignIds": campaign_ids,
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request(
            "GET",
            "/sp/campaign/recommendations",
            params=params,
            headers={"Accept": "application/vnd.spgetcampaignrecommendationsresponse.v1+json"},
        )
        return self._response(GetCampaignRecommendationsResponse, resp, mode=mode)
