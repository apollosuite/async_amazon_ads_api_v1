"""STCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.st import (
    STCampaignMultiStatusResponse,
    STCampaignSuccessResponse,
    STCreateCampaignRequest,
    STQueryCampaignRequest,
    STUpdateCampaignRequest,
)


class STCampaigns(BaseResource):

    @overload
    async def create_campaign(
        self, body: STCreateCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_campaign(
        self, body: STCreateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> STCampaignMultiStatusResponse: ...
    @overload
    async def create_campaign(self, body: STCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_campaign(
        self, body: STCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = await self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(STCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_campaign(
        self, body: STQueryCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_campaign(
        self, body: STQueryCampaignRequest, *, mode: Literal["pydantic"]
    ) -> STCampaignSuccessResponse: ...
    @overload
    async def query_campaign(self, body: STQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_campaign(
        self, body: STQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = await self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(STCampaignSuccessResponse, resp, mode=mode)

    @overload
    async def update_campaign(
        self, body: STUpdateCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_campaign(
        self, body: STUpdateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> STCampaignMultiStatusResponse: ...
    @overload
    async def update_campaign(self, body: STUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_campaign(
        self, body: STUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = await self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(STCampaignMultiStatusResponse, resp, mode=mode)
