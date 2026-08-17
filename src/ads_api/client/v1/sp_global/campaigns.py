"""SPGlobalCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.sp_global import (
    SPGlobalCampaignMultiStatusResponseWithPartialErrors,
    SPGlobalCampaignSuccessResponse,
    SPGlobalCreateCampaignRequest,
    SPGlobalDeleteCampaignRequest,
    SPGlobalQueryCampaignRequest,
    SPGlobalUpdateCampaignRequest,
)


class SPGlobalCampaigns(BaseResource):

    @overload
    async def create_campaign(
        self, body: SPGlobalCreateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors: ...
    @overload
    async def create_campaign(
        self, body: SPGlobalCreateCampaignRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_campaign(self, body: SPGlobalCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_campaign(
        self, body: SPGlobalCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = await self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(SPGlobalCampaignMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    async def delete_campaign(
        self, body: SPGlobalDeleteCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors: ...
    @overload
    async def delete_campaign(
        self, body: SPGlobalDeleteCampaignRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def delete_campaign(self, body: SPGlobalDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_campaign(
        self, body: SPGlobalDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = await self._request("POST", "/adsApi/v1/delete/campaigns", json=self.dump_json(body))
        return self._response(SPGlobalCampaignMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    async def query_campaign(
        self, body: SPGlobalQueryCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalCampaignSuccessResponse: ...
    @overload
    async def query_campaign(self, body: SPGlobalQueryCampaignRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_campaign(self, body: SPGlobalQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_campaign(
        self, body: SPGlobalQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = await self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(SPGlobalCampaignSuccessResponse, resp, mode=mode)

    @overload
    async def update_campaign(
        self, body: SPGlobalUpdateCampaignRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors: ...
    @overload
    async def update_campaign(
        self, body: SPGlobalUpdateCampaignRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_campaign(self, body: SPGlobalUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_campaign(
        self, body: SPGlobalUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = await self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(SPGlobalCampaignMultiStatusResponseWithPartialErrors, resp, mode=mode)
