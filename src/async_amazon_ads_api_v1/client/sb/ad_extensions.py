"""SB AdExtension resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb import (
    SBAdExtensionCreate,
    SBAdExtensionMultiStatusResponse,
    SBAdExtensionSuccessResponse,
    SBAdExtensionUpdate,
    SBQueryAdExtensionRequest,
)


class AdExtensions(_ResourceBase):
    _spec = _ResourceSpec(
        name="adExtensions",
        create_model=SBAdExtensionCreate,
        update_model=SBAdExtensionUpdate,
    )

    async def create(self, ad_extensions: list[SBAdExtensionCreate]) -> SBAdExtensionSuccessResponse:
        return await self._create(ad_extensions, self._spec, SBAdExtensionSuccessResponse)

    async def query(self, body: SBQueryAdExtensionRequest) -> SBAdExtensionSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/adExtensions", SBAdExtensionSuccessResponse)

    async def update(self, ad_extensions: list[SBAdExtensionUpdate]) -> SBAdExtensionMultiStatusResponse:
        return await self._update(ad_extensions, self._spec, SBAdExtensionMultiStatusResponse)
