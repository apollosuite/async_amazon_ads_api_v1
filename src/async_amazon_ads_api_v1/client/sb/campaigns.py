"""Campaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.campaigns import (
    SBCampaignMultiStatusResponse,
    SBCampaignSuccessResponse,
    SBCreateCampaignRequest,
    SBDeleteCampaignRequest,
    SBQueryCampaignRequest,
    SBUpdateCampaignRequest,
)


class Campaigns(BaseResource):

    @overload
    async def sb_create_campaign(
        self, body: SBCreateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBCampaignMultiStatusResponse: ...
    @overload
    async def sb_create_campaign(self, body: SBCreateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_create_campaign(self, body: SBCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_create_campaign(
        self, body: SBCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_delete_campaign(
        self, body: SBDeleteCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBCampaignMultiStatusResponse: ...
    @overload
    async def sb_delete_campaign(self, body: SBDeleteCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_delete_campaign(self, body: SBDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_delete_campaign(
        self, body: SBDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_query_campaign(
        self, body: SBQueryCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBCampaignSuccessResponse: ...
    @overload
    async def sb_query_campaign(self, body: SBQueryCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_query_campaign(self, body: SBQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_query_campaign(
        self, body: SBQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCampaignSuccessResponse, resp, mode=mode)

    @overload
    async def sb_update_campaign(
        self, body: SBUpdateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBCampaignMultiStatusResponse: ...
    @overload
    async def sb_update_campaign(self, body: SBUpdateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_update_campaign(self, body: SBUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_update_campaign(
        self, body: SBUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCampaignMultiStatusResponse, resp, mode=mode)
