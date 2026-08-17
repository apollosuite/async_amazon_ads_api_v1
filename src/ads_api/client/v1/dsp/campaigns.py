"""DSPCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.dsp import (
    DSPCampaignMultiStatusResponse,
    DSPCampaignSuccessResponse,
    DSPCreateCampaignRequest,
    DSPQueryCampaignRequest,
    DSPUpdateCampaignRequest,
)


class DSPCampaigns(BaseResource):

    @overload
    async def create_campaign(
        self, body: DSPCreateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPCampaignMultiStatusResponse: ...
    @overload
    async def create_campaign(self, body: DSPCreateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_campaign(self, body: DSPCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_campaign(
        self, body: DSPCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = await self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(DSPCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_campaign(
        self, body: DSPQueryCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPCampaignSuccessResponse: ...
    @overload
    async def query_campaign(self, body: DSPQueryCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_campaign(self, body: DSPQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_campaign(
        self, body: DSPQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = await self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(DSPCampaignSuccessResponse, resp, mode=mode)

    @overload
    async def update_campaign(
        self, body: DSPUpdateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPCampaignMultiStatusResponse: ...
    @overload
    async def update_campaign(self, body: DSPUpdateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def update_campaign(self, body: DSPUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_campaign(
        self, body: DSPUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = await self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(DSPCampaignMultiStatusResponse, resp, mode=mode)
