"""SB AdExtension resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.ad_extensions import (
    SBAdExtensionCreate,
    SBAdExtensionMultiStatusResponse,
    SBAdExtensionSuccessResponse,
    SBAdExtensionUpdate,
    SBQueryAdExtensionRequest,
)


class AdExtensions(BaseResource):

    async def create(self, ad_extensions: list[SBAdExtensionCreate]) -> SBAdExtensionSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json={"adExtensions": self._dump(ad_extensions)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdExtensionSuccessResponse, resp)

    async def query(self, body: SBQueryAdExtensionRequest) -> SBAdExtensionSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adExtensions",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SBAdExtensionSuccessResponse, resp)

    async def update(self, ad_extensions: list[SBAdExtensionUpdate]) -> SBAdExtensionMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json={"adExtensions": self._dump(ad_extensions)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdExtensionMultiStatusResponse, resp)
