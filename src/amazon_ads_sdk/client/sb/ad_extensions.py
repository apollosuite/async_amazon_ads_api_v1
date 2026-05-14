"""SB AdExtension resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sb import (
    SBAdExtensionCreate,
    SBAdExtensionMultiStatusResponse,
    SBAdExtensionSuccessResponse,
    SBAdExtensionUpdate,
)


class AdExtensions(_ResourceBase):
    _spec = _ResourceSpec(
        name="adExtensions",
        create_model=SBAdExtensionCreate,
        update_model=SBAdExtensionUpdate,
    )

    async def create(
        self, ad_extensions: list[dict[str, Any] | SBAdExtensionCreate]
    ) -> SBAdExtensionSuccessResponse:
        return await self._create(ad_extensions, self._spec, SBAdExtensionSuccessResponse)

    async def query(self, body: dict[str, Any]) -> SBAdExtensionSuccessResponse:
        return await self._query(body, self._spec, SBAdExtensionSuccessResponse)

    async def update(
        self, ad_extensions: list[dict[str, Any] | SBAdExtensionUpdate]
    ) -> SBAdExtensionMultiStatusResponse:
        return await self._update(ad_extensions, self._spec, SBAdExtensionMultiStatusResponse)
