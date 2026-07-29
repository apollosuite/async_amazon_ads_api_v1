"""AdExtension resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sp.ad_extensions import (
    SPAdExtensionCreate,
    SPAdExtensionSuccessResponse,
    SPAdExtensionUpdate,
    SPQueryAdExtensionRequest,
)


class AdExtensions(_ResourceBase):
    """AdExtension 广告扩展资源操作。"""

    async def create(self, ad_extensions: list[SPAdExtensionCreate]) -> SPAdExtensionSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json={"adExtensions": self._dump(ad_extensions)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPAdExtensionSuccessResponse, resp)

    async def query(self, body: SPQueryAdExtensionRequest) -> SPAdExtensionSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adExtensions",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SPAdExtensionSuccessResponse, resp)

    async def update(self, ad_extensions: list[SPAdExtensionUpdate]) -> SPAdExtensionSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json={"adExtensions": self._dump(ad_extensions)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPAdExtensionSuccessResponse, resp)
