"""Targets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.targets import (
    SBCreateTargetRequest,
    SBDeleteTargetRequest,
    SBQueryTargetRequest,
    SBTargetMultiStatusResponse,
    SBTargetSuccessResponse,
    SBUpdateTargetRequest,
)


class Targets(BaseResource):

    async def sb_create_target(self, body: SBCreateTargetRequest) -> SBTargetMultiStatusResponse:
        """Create target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBTargetMultiStatusResponse, resp)

    async def sb_delete_target(self, body: SBDeleteTargetRequest) -> SBTargetMultiStatusResponse:
        """Delete target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBTargetMultiStatusResponse, resp)

    async def sb_query_target(self, body: SBQueryTargetRequest) -> SBTargetSuccessResponse:
        """List target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBTargetSuccessResponse, resp)

    async def sb_update_target(self, body: SBUpdateTargetRequest) -> SBTargetMultiStatusResponse:
        """Update target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBTargetMultiStatusResponse, resp)
