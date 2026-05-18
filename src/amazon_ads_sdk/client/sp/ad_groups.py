"""AdGroup resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sp import (
    SPAdGroupCreate,
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPAdGroupUpdate,
    SPQueryAdGroupRequest,
)


class AdGroups(_ResourceBase):
    """AdGroup 广告组资源操作。"""

    _spec = _ResourceSpec(
        name="adGroups",
        create_model=SPAdGroupCreate,
        update_model=SPAdGroupUpdate,
        query_model=SPQueryAdGroupRequest,
        delete_key="adGroupIds",
    )

    async def create(
        self, ad_groups: list[dict[str, Any] | SPAdGroupCreate]
    ) -> SPAdGroupSuccessResponse:
        return await self._create(ad_groups, self._spec, SPAdGroupSuccessResponse)

    async def query(self, body: dict[str, Any] | SPQueryAdGroupRequest) -> SPAdGroupSuccessResponse:
        return await self._query(body, self._spec, SPAdGroupSuccessResponse)

    async def update(
        self, ad_groups: list[dict[str, Any] | SPAdGroupUpdate]
    ) -> SPAdGroupMultiStatusResponse:
        return await self._update(ad_groups, self._spec, SPAdGroupMultiStatusResponse)

    async def delete(self, ad_group_ids: list[str]) -> SPAdGroupMultiStatusResponse:
        return await self._delete(ad_group_ids, self._spec, SPAdGroupMultiStatusResponse)
