"""SB AdGroup resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb import (
    SBAdGroupCreate,
    SBAdGroupMultiStatusResponse,
    SBAdGroupSuccessResponse,
    SBAdGroupUpdate,
    SBQueryAdGroupRequest,
)


class AdGroups(_ResourceBase):
    _spec = _ResourceSpec(
        name="adGroups",
        create_model=SBAdGroupCreate,
        update_model=SBAdGroupUpdate,
        delete_key="adGroupIds",
    )

    async def create(
        self, ad_groups: list[dict[str, Any] | SBAdGroupCreate]
    ) -> SBAdGroupSuccessResponse | dict[str, Any]:
        return await self._create(ad_groups, self._spec, SBAdGroupSuccessResponse)

    async def query(
        self, body: dict[str, Any] | SBQueryAdGroupRequest
    ) -> SBAdGroupSuccessResponse | dict[str, Any]:
        if isinstance(body, dict):
            body = SBQueryAdGroupRequest(**body)
        return await self._query(body, "/adsApi/v1/query/adGroups", SBAdGroupSuccessResponse)

    async def update(
        self, ad_groups: list[dict[str, Any] | SBAdGroupUpdate]
    ) -> SBAdGroupMultiStatusResponse | dict[str, Any]:
        return await self._update(ad_groups, self._spec, SBAdGroupMultiStatusResponse)

    async def delete(
        self, ad_group_ids: list[str]
    ) -> SBAdGroupMultiStatusResponse | dict[str, Any]:
        return await self._delete(ad_group_ids, self._spec, SBAdGroupMultiStatusResponse)
