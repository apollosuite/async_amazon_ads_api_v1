"""Campaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sp.campaigns import (
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCreateCampaignRequest,
    SPDeleteCampaignRequest,
    SPQueryCampaignRequest,
    SPUpdateCampaignRequest,
)


class Campaigns(BaseResource):

    @overload
    async def sp_create_campaign(
        self, body: SPCreateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse: ...
    @overload
    async def sp_create_campaign(self, body: SPCreateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_create_campaign(self, body: SPCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_create_campaign(
        self, body: SPCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def sp_delete_campaign(
        self, body: SPDeleteCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse: ...
    @overload
    async def sp_delete_campaign(self, body: SPDeleteCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_delete_campaign(self, body: SPDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_delete_campaign(
        self, body: SPDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    async def sp_query_campaign(
        self, body: SPQueryCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCampaignSuccessResponse: ...
    @overload
    async def sp_query_campaign(self, body: SPQueryCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_query_campaign(self, body: SPQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_query_campaign(
        self, body: SPQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCampaignSuccessResponse, resp, mode=mode)

    @overload
    async def sp_update_campaign(
        self, body: SPUpdateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse: ...
    @overload
    async def sp_update_campaign(self, body: SPUpdateCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_update_campaign(self, body: SPUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_update_campaign(
        self, body: SPUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCampaignMultiStatusResponse, resp, mode=mode)
