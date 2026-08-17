"""SPCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.sp import (
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCreateCampaignRequest,
    SPDeleteCampaignRequest,
    SPQueryCampaignRequest,
    SPUpdateCampaignRequest,
)


class SPCampaigns(BaseResource):

    @overload
    async def create_campaign(
        self, body: SPCreateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse: ...
    @overload
    async def create_campaign(self, body: SPCreateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_campaign(self, body: SPCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_campaign(
        self, body: SPCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = await self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(SPCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_campaign(
        self, body: SPDeleteCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse: ...
    @overload
    async def delete_campaign(self, body: SPDeleteCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def delete_campaign(self, body: SPDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_campaign(
        self, body: SPDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = await self._request("POST", "/adsApi/v1/delete/campaigns", json=self.dump_json(body))
        return self._response(SPCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_campaign(
        self, body: SPQueryCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCampaignSuccessResponse: ...
    @overload
    async def query_campaign(self, body: SPQueryCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_campaign(self, body: SPQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_campaign(
        self, body: SPQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = await self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(SPCampaignSuccessResponse, resp, mode=mode)

    @overload
    async def update_campaign(
        self, body: SPUpdateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse: ...
    @overload
    async def update_campaign(self, body: SPUpdateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def update_campaign(self, body: SPUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_campaign(
        self, body: SPUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = await self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(SPCampaignMultiStatusResponse, resp, mode=mode)
