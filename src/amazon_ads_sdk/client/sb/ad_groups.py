"""SB AdGroup resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sb import (
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
    ) -> SBAdGroupSuccessResponse:
        return await self._create(ad_groups, self._spec, SBAdGroupSuccessResponse)

    async def query(self, body: dict[str, Any] | SBQueryAdGroupRequest) -> SBAdGroupSuccessResponse:
        return await self._query(body, self._spec, SBAdGroupSuccessResponse)

    async def update(
        self, ad_groups: list[dict[str, Any] | SBAdGroupUpdate]
    ) -> SBAdGroupMultiStatusResponse:
        return await self._update(ad_groups, self._spec, SBAdGroupMultiStatusResponse)

    async def delete(self, ad_group_ids: list[str]) -> SBAdGroupMultiStatusResponse:
        return await self._delete(ad_group_ids, self._spec, SBAdGroupMultiStatusResponse)
