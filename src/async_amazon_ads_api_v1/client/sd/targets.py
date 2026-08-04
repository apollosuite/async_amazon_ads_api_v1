"""Targets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sd.targets import (
    SDCreateTargetRequest,
    SDDeleteTargetRequest,
    SDQueryTargetRequest,
    SDTargetMultiStatusResponse,
    SDTargetSuccessResponse,
    SDUpdateTargetRequest,
)


class Targets(BaseResource):

    async def sd_create_target(self, body: SDCreateTargetRequest) -> SDTargetMultiStatusResponse:
        """Create target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDTargetMultiStatusResponse, resp)

    async def sd_delete_target(self, body: SDDeleteTargetRequest) -> SDTargetMultiStatusResponse:
        """Delete target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDTargetMultiStatusResponse, resp)

    async def sd_query_target(self, body: SDQueryTargetRequest) -> SDTargetSuccessResponse:
        """List target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDTargetSuccessResponse, resp)

    async def sd_update_target(self, body: SDUpdateTargetRequest) -> SDTargetMultiStatusResponse:
        """Update target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDTargetMultiStatusResponse, resp)
