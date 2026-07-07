"""AdExtension resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sp.ad_extensions import (
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

    async def create(self, ad_extensions: list[SPAdExtensionCreate]) -> SPAdExtensionSuccessResponse:
        return await self._create(ad_extensions, self._spec, SPAdExtensionSuccessResponse)

    async def query(self, body: SPQueryAdExtensionRequest) -> SPAdExtensionSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/adExtensions", SPAdExtensionSuccessResponse)

    async def update(self, ad_extensions: list[SPAdExtensionUpdate]) -> SPAdExtensionSuccessResponse:
        return await self._update(ad_extensions, self._spec, SPAdExtensionSuccessResponse)
