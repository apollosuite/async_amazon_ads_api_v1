"""StoreInsights resource operations.

Generated from OpenAPI spec (tag: Stores Analytics).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.reporting.store_insights import (
    GetAsinEngagementForStoreRequest,
    GetAsinEngagementForStoreResponse,
    GetInsightsForStoreRequest,
    GetInsightsForStoreResponse,
)


class StoreInsights(BaseResource):

    @overload
    async def get_asin_engagement_for_store(
        self, brand_entity_id: str, body: GetAsinEngagementForStoreRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_asin_engagement_for_store(
        self, brand_entity_id: str, body: GetAsinEngagementForStoreRequest, *, mode: Literal["pydantic"]
    ) -> GetAsinEngagementForStoreResponse: ...
    @overload
    async def get_asin_engagement_for_store(
        self, brand_entity_id: str, body: GetAsinEngagementForStoreRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_asin_engagement_for_store(
        self,
        brand_entity_id: str,
        body: GetAsinEngagementForStoreRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> GetAsinEngagementForStoreResponse | dict[str, Any] | httpx.Response:
        """Store asin metrics provides information about your store asin performance, including rendered impressions, viewed impressions, clicks and sales. You can access Stores insights through this API."""

        resp = await self._request(
            "POST",
            f"/stores/{brand_entity_id}/asinMetrics",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.GetAsinEngagementForStoreRequest.v1+json",
                "Accept": "application/vnd.GetAsinEngagementForStoreRequest.v1+json",
            },
        )
        return self._response(GetAsinEngagementForStoreResponse, resp, mode=mode)

    @overload
    async def get_insights_for_store_api(
        self, brand_entity_id: str, body: GetInsightsForStoreRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_insights_for_store_api(
        self, brand_entity_id: str, body: GetInsightsForStoreRequest, *, mode: Literal["pydantic"]
    ) -> GetInsightsForStoreResponse: ...
    @overload
    async def get_insights_for_store_api(
        self, brand_entity_id: str, body: GetInsightsForStoreRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_insights_for_store_api(
        self,
        brand_entity_id: str,
        body: GetInsightsForStoreRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> GetInsightsForStoreResponse | dict[str, Any] | httpx.Response:
        """Stores insights provides information about your store's performance, including traffic and sales. You can access Stores insights through this API."""

        resp = await self._request(
            "POST",
            f"/stores/{brand_entity_id}/insights",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.GetInsightsForStoreRequest.v1+json",
                "Accept": "application/vnd.GetInsightsForStoreRequest.v1+json",
            },
        )
        return self._response(GetInsightsForStoreResponse, resp, mode=mode)
