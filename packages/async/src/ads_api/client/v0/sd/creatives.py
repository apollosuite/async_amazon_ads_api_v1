"""Creatives resource operations.

Generated from OpenAPI spec (tag: Creatives).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.creatives import (
    CreateCreative,
    Creative,
    CreativeModeration,
    CreativePreviewRequest,
    CreativePreviewResponse,
    CreativeResponse,
    CreativeUpdate,
    Locale,
)


class Creatives(BaseResource):

    @overload
    async def create_creatives(
        self, body: list[CreateCreative] | None = None, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_creatives(
        self, body: list[CreateCreative] | None = None, *, mode: Literal["pydantic"]
    ) -> list[CreativeResponse]: ...
    @overload
    async def create_creatives(
        self, body: list[CreateCreative] | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_creatives(
        self, body: list[CreateCreative] | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> list[CreativeResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("POST", "/sd/creatives", json=self.dump_json(body))
        return self._response_list(CreativeResponse, resp, mode=mode)

    @overload
    async def list_creative_moderations(
        self,
        language: Locale | str,
        *,
        mode: Literal["dict"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_creative_moderations(
        self,
        language: Locale | str,
        *,
        mode: Literal["pydantic"],
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[CreativeModeration]: ...
    @overload
    async def list_creative_moderations(
        self,
        language: Locale | str,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_creative_moderations(
        self,
        language: Locale | str,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[CreativeModeration] | list[dict[str, Any]] | httpx.Response:
        """"""

        params = {
            "language": language,
            "startIndex": start_index,
            "count": count,
            "adGroupIdFilter": ad_group_id_filter,
            "creativeIdFilter": creative_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/moderation/creatives", params=params)
        return self._response_list(CreativeModeration, resp, mode=mode)

    @overload
    async def list_creatives(
        self,
        *,
        mode: Literal["dict"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_creatives(
        self,
        *,
        mode: Literal["pydantic"],
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[Creative]: ...
    @overload
    async def list_creatives(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_creatives(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[Creative] | list[dict[str, Any]] | httpx.Response:
        """"""

        params = {
            "startIndex": start_index,
            "count": count,
            "adGroupIdFilter": ad_group_id_filter,
            "creativeIdFilter": creative_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/creatives", params=params)
        return self._response_list(Creative, resp, mode=mode)

    @overload
    async def post_creative_preview(
        self, body: CreativePreviewRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def post_creative_preview(
        self, body: CreativePreviewRequest | None = None, *, mode: Literal["pydantic"]
    ) -> CreativePreviewResponse: ...
    @overload
    async def post_creative_preview(
        self, body: CreativePreviewRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def post_creative_preview(
        self, body: CreativePreviewRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CreativePreviewResponse | dict[str, Any] | httpx.Response:
        """"""

        resp = await self._request("POST", "/sd/creatives/preview", json=self.dump_json(body))
        return self._response(CreativePreviewResponse, resp, mode=mode)

    @overload
    async def update_creatives(
        self, body: list[CreativeUpdate] | None = None, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def update_creatives(
        self, body: list[CreativeUpdate] | None = None, *, mode: Literal["pydantic"]
    ) -> list[CreativeResponse]: ...
    @overload
    async def update_creatives(
        self, body: list[CreativeUpdate] | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_creatives(
        self, body: list[CreativeUpdate] | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> list[CreativeResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("PUT", "/sd/creatives", json=self.dump_json(body))
        return self._response_list(CreativeResponse, resp, mode=mode)
