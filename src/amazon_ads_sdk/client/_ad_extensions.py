"""AdExtension resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPAdExtensionCreate,
    SPAdExtensionSuccessResponse,
    SPAdExtensionUpdate,
)

from ._base import _RequestMethod, _ResponseMethod


class AdExtensions:
    """AdExtension 广告扩展资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    async def create(
        self, ad_extensions: list[dict[str, Any] | SPAdExtensionCreate]
    ) -> SPAdExtensionSuccessResponse:
        """创建广告扩展（Prompts、Video 等类型）。

        参数
        -----
        ad_extensions : list[dict | SPAdExtensionCreate]
            广告扩展列表，每项包含 adExtensionType、adExtensionSettings 等字段。
        """
        validated = [
            (
                e.model_dump()
                if isinstance(e, SPAdExtensionCreate)
                else SPAdExtensionCreate(**e).model_dump()
            )
            for e in ad_extensions
        ]
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json={"adExtensions": validated},
        )
        return self._response(SPAdExtensionSuccessResponse, resp)  # type: ignore[return-value]

    async def query(self, body: dict[str, Any]) -> SPAdExtensionSuccessResponse:
        """查询广告扩展。

        参数
        -----
        body : dict
            查询条件，包含 adExtensionIdFilter、adExtensionTypeFilter 等。
            支持 nextToken 分页。
        """
        resp = await self._request("POST", "/adsApi/v1/query/adExtensions", json=body)
        return self._response(SPAdExtensionSuccessResponse, resp)  # type: ignore[return-value]

    async def update(
        self, ad_extensions: list[dict[str, Any] | SPAdExtensionUpdate]
    ) -> SPAdExtensionSuccessResponse:
        """更新广告扩展。

        参数
        -----
        ad_extensions : list[dict | SPAdExtensionUpdate]
            广告扩展更新列表，每项需包含 adExtensionId。
        """
        validated = [
            (
                e.model_dump()
                if isinstance(e, SPAdExtensionUpdate)
                else SPAdExtensionUpdate(**e).model_dump()
            )
            for e in ad_extensions
        ]
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json={"adExtensions": validated},
        )
        return self._response(SPAdExtensionSuccessResponse, resp)  # type: ignore[return-value]
