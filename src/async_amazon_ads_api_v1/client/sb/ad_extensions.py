"""SB AdExtension resource operations."""

from __future__ import annotations

from typing import Any

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

    async def create(
        self, ad_extensions: list[dict[str, Any] | SBAdExtensionCreate]
    ) -> SBAdExtensionSuccessResponse | dict[str, Any]:
        return await self._create(ad_extensions, self._spec, SBAdExtensionSuccessResponse)

    async def query(
        self, body: dict[str, Any] | SBQueryAdExtensionRequest
    ) -> SBAdExtensionSuccessResponse | dict[str, Any]:
        if isinstance(body, dict):
            body = SBQueryAdExtensionRequest(**body)
        return await self._query(body, "/adsApi/v1/query/adExtensions", SBAdExtensionSuccessResponse)

    async def update(
        self, ad_extensions: list[dict[str, Any] | SBAdExtensionUpdate]
    ) -> SBAdExtensionMultiStatusResponse | dict[str, Any]:
        return await self._update(ad_extensions, self._spec, SBAdExtensionMultiStatusResponse)
