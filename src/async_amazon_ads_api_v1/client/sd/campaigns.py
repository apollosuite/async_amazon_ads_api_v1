"""Campaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sd.campaigns import (
    SDCampaignMultiStatusResponse,
    SDCampaignSuccessResponse,
    SDCreateCampaignRequest,
    SDDeleteCampaignRequest,
    SDQueryCampaignRequest,
    SDUpdateCampaignRequest,
)


class Campaigns(BaseResource):

    @overload
    async def sd_create_campaign(
        self, body: SDCreateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDCampaignMultiStatusResponse: ...
    @overload
    async def sd_create_campaign(self, body: SDCreateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_create_campaign(self, body: SDCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_create_campaign(
        self, body: SDCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json=self.dump_json(body),
        )
        return self._response(SDCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def sd_delete_campaign(
        self, body: SDDeleteCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDCampaignMultiStatusResponse: ...
    @overload
    async def sd_delete_campaign(self, body: SDDeleteCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_delete_campaign(self, body: SDDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_delete_campaign(
        self, body: SDDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json=self.dump_json(body),
        )
        return self._response(SDCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def sd_query_campaign(
        self, body: SDQueryCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDCampaignSuccessResponse: ...
    @overload
    async def sd_query_campaign(self, body: SDQueryCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_query_campaign(self, body: SDQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_query_campaign(
        self, body: SDQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/campaigns",
            json=self.dump_json(body),
        )
        return self._response(SDCampaignSuccessResponse, resp, mode=mode)

    @overload
    async def sd_update_campaign(
        self, body: SDUpdateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDCampaignMultiStatusResponse: ...
    @overload
    async def sd_update_campaign(self, body: SDUpdateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_update_campaign(self, body: SDUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_update_campaign(
        self, body: SDUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json=self.dump_json(body),
        )
        return self._response(SDCampaignMultiStatusResponse, resp, mode=mode)
