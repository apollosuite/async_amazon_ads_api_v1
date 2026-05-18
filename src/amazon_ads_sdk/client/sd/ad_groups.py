"""SD AdGroup resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sd import (
    SDAdGroupCreate,
    SDAdGroupMultiStatusResponse,
    SDAdGroupSuccessResponse,
    SDAdGroupUpdate,
    SDQueryAdGroupRequest,
)


class AdGroups(_ResourceBase):
    _spec = _ResourceSpec(
        name="adGroups",
        create_model=SDAdGroupCreate,
        update_model=SDAdGroupUpdate,
        query_model=SDQueryAdGroupRequest,
        delete_key="adGroupIds",
    )

    async def create(
        self, ad_groups: list[dict[str, Any] | SDAdGroupCreate]
    ) -> SDAdGroupSuccessResponse:
        return await self._create(ad_groups, self._spec, SDAdGroupSuccessResponse)

    async def query(self, body: dict[str, Any] | SDQueryAdGroupRequest) -> SDAdGroupSuccessResponse:
        return await self._query(body, self._spec, SDAdGroupSuccessResponse)

    async def update(
        self, ad_groups: list[dict[str, Any] | SDAdGroupUpdate]
    ) -> SDAdGroupMultiStatusResponse:
        return await self._update(ad_groups, self._spec, SDAdGroupMultiStatusResponse)

    async def delete(self, ad_group_ids: list[str]) -> SDAdGroupMultiStatusResponse:
        return await self._delete(ad_group_ids, self._spec, SDAdGroupMultiStatusResponse)
