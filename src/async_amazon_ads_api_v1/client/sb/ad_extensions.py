"""SB AdExtension resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.ad_extensions import (
    SBAdExtensionCreate,
    SBAdExtensionMultiStatusResponse,
    SBAdExtensionSuccessResponse,
    SBAdExtensionUpdate,
    SBQueryAdExtensionRequest,
)


class AdExtensions(_ResourceBase):

    async def create(self, ad_extensions: list[SBAdExtensionCreate]) -> SBAdExtensionSuccessResponse:
        return await self._create(
            "/adsApi/v1/create/adExtensions",
            SBAdExtensionSuccessResponse,
            json={"adExtensions": self._validate(ad_extensions)},
        )

    async def query(self, body: SBQueryAdExtensionRequest) -> SBAdExtensionSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/adExtensions", SBAdExtensionSuccessResponse)

    async def update(self, ad_extensions: list[SBAdExtensionUpdate]) -> SBAdExtensionMultiStatusResponse:
        return await self._update(
            "/adsApi/v1/update/adExtensions",
            SBAdExtensionMultiStatusResponse,
            json={"adExtensions": self._validate(ad_extensions)},
        )
