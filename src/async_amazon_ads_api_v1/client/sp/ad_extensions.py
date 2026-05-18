"""AdExtension resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sp import (
    SPAdExtensionCreate,
    SPAdExtensionSuccessResponse,
    SPAdExtensionUpdate,
    SPQueryAdExtensionRequest,
)


class AdExtensions(_ResourceBase):
    """AdExtension 广告扩展资源操作。"""

    _spec = _ResourceSpec(
        name="adExtensions",
        create_model=SPAdExtensionCreate,
        update_model=SPAdExtensionUpdate,
    )

    async def create(
        self, ad_extensions: list[dict[str, Any] | SPAdExtensionCreate]
    ) -> SPAdExtensionSuccessResponse | dict[str, Any]:
        return await self._create(ad_extensions, self._spec, SPAdExtensionSuccessResponse)

    async def query(
        self, body: dict[str, Any] | SPQueryAdExtensionRequest
    ) -> SPAdExtensionSuccessResponse | dict[str, Any]:
        if isinstance(body, dict):
            body = SPQueryAdExtensionRequest(**body)
        return await self._query(
            body, "/adsApi/v1/query/adExtensions", SPAdExtensionSuccessResponse
        )

    async def update(
        self, ad_extensions: list[dict[str, Any] | SPAdExtensionUpdate]
    ) -> SPAdExtensionSuccessResponse | dict[str, Any]:
        return await self._update(ad_extensions, self._spec, SPAdExtensionSuccessResponse)
