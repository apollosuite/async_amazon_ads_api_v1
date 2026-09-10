"""SBCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.sb import (
    SBCampaignMultiStatusResponse,
    SBCampaignSuccessResponse,
    SBCreateCampaignRequest,
    SBDeleteCampaignRequest,
    SBQueryCampaignRequest,
    SBUpdateCampaignRequest,
)


class SBCampaigns(BaseResource):

    @overload
    async def create_campaign(
        self, body: SBCreateCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_campaign(
        self, body: SBCreateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SBCampaignMultiStatusResponse: ...
    @overload
    async def create_campaign(self, body: SBCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_campaign(
        self, body: SBCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = await self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(SBCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_campaign(
        self, body: SBDeleteCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_campaign(
        self, body: SBDeleteCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SBCampaignMultiStatusResponse: ...
    @overload
    async def delete_campaign(self, body: SBDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_campaign(
        self, body: SBDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = await self._request("POST", "/adsApi/v1/delete/campaigns", json=self.dump_json(body))
        return self._response(SBCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_campaign(
        self, body: SBQueryCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_campaign(
        self, body: SBQueryCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SBCampaignSuccessResponse: ...
    @overload
    async def query_campaign(self, body: SBQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_campaign(
        self, body: SBQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = await self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(SBCampaignSuccessResponse, resp, mode=mode)

    @overload
    async def update_campaign(
        self, body: SBUpdateCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_campaign(
        self, body: SBUpdateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SBCampaignMultiStatusResponse: ...
    @overload
    async def update_campaign(self, body: SBUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_campaign(
        self, body: SBUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = await self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(SBCampaignMultiStatusResponse, resp, mode=mode)
