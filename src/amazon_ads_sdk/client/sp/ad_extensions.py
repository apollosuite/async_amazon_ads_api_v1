"""AdExtension resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sp import (
    SPAdExtensionCreate,
    SPAdExtensionSuccessResponse,
    SPAdExtensionUpdate,
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
    ) -> SPAdExtensionSuccessResponse:
        return await self._create(ad_extensions, self._spec, SPAdExtensionSuccessResponse)

    async def query(self, body: dict[str, Any]) -> SPAdExtensionSuccessResponse:
        return await self._query(body, self._spec, SPAdExtensionSuccessResponse)

    async def update(
        self, ad_extensions: list[dict[str, Any] | SPAdExtensionUpdate]
    ) -> SPAdExtensionSuccessResponse:
        return await self._update(ad_extensions, self._spec, SPAdExtensionSuccessResponse)
