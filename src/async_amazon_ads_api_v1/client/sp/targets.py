"""Targets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sp.targets import (
    SPCreateTargetRequest,
    SPDeleteTargetRequest,
    SPQueryTargetRequest,
    SPTargetMultiStatusResponse,
    SPTargetSuccessResponse,
    SPUpdateTargetRequest,
)


class Targets(BaseResource):

    async def sp_create_target(self, body: SPCreateTargetRequest) -> SPTargetMultiStatusResponse:
        """Create target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPTargetMultiStatusResponse, resp)

    async def sp_delete_target(self, body: SPDeleteTargetRequest) -> SPTargetMultiStatusResponse:
        """Delete target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPTargetMultiStatusResponse, resp)

    async def sp_query_target(self, body: SPQueryTargetRequest) -> SPTargetSuccessResponse:
        """List target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPTargetSuccessResponse, resp)

    async def sp_update_target(self, body: SPUpdateTargetRequest) -> SPTargetMultiStatusResponse:
        """Update target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPTargetMultiStatusResponse, resp)
