"""AdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sp.ad_groups import (
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPCreateAdGroupRequest,
    SPDeleteAdGroupRequest,
    SPQueryAdGroupRequest,
    SPUpdateAdGroupRequest,
)


class AdGroups(BaseResource):

    async def sp_create_ad_group(self, body: SPCreateAdGroupRequest) -> SPAdGroupMultiStatusResponse:
        """Create ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)

    async def sp_delete_ad_group(self, body: SPDeleteAdGroupRequest) -> SPAdGroupMultiStatusResponse:
        """Delete ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)

    async def sp_query_ad_group(self, body: SPQueryAdGroupRequest) -> SPAdGroupSuccessResponse:
        """List ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdGroupSuccessResponse, resp)

    async def sp_update_ad_group(self, body: SPUpdateAdGroupRequest) -> SPAdGroupMultiStatusResponse:
        """Update ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)
