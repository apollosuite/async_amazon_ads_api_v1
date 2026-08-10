"""SDCreatives resource operations.

Generated from OpenAPI spec (tag: Creatives).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sdv3.sd_creatives import (
    SDCreateCreative,
    SDCreative,
    SDCreativeModeration,
    SDCreativePreviewRequest,
    SDCreativePreviewResponse,
    SDCreativeResponse,
    SDCreativeUpdate,
    SDLocale,
)


class SDCreatives(BaseResource):

    @overload
    async def list_creatives(
        self,
        *,
        mode: Literal["pydantic"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[SDCreative]: ...
    @overload
    async def list_creatives(
        self,
        *,
        mode: Literal["dict"],
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
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
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[SDCreative] | list[dict[str, Any]] | httpx.Response:
        """

        Parameters
        ----------
        start_index : int
            Sets a cursor into the requested set of creatives. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0.
        count : int
            Sets the number of creative objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten creatives set `startIndex=0` and `count=10`. To return the next ten creatives, set `startIndex=10` and `count=10`, and so on. Defaults to max page size.
        ad_group_id_filter : str
            The returned array includes only creatives associated with ad group identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `creativeIdFilter` parameter.
        creative_id_filter : str
            The returned array includes only creatives with identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `adGroupIdFilter` parameter.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        params = {
            "startIndex": start_index,
            "count": count,
            "adGroupIdFilter": ad_group_id_filter,
            "creativeIdFilter": creative_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/creatives", params=params)
        return self._response_list(SDCreative, resp, mode=mode)

    @overload
    async def update_creatives(
        self, body: list[SDCreativeUpdate], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[SDCreativeResponse]: ...
    @overload
    async def update_creatives(
        self, body: list[SDCreativeUpdate], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def update_creatives(self, body: list[SDCreativeUpdate], *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_creatives(
        self, body: list[SDCreativeUpdate], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[SDCreativeResponse] | list[dict[str, Any]] | httpx.Response:
        """ """

        resp = await self._request(
            "PUT",
            "/sd/creatives",
            json=[self.dump_json(x) for x in body],
        )
        return self._response_list(SDCreativeResponse, resp, mode=mode)

    @overload
    async def create_creatives(
        self, body: list[SDCreateCreative], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[SDCreativeResponse]: ...
    @overload
    async def create_creatives(
        self, body: list[SDCreateCreative], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_creatives(self, body: list[SDCreateCreative], *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_creatives(
        self, body: list[SDCreateCreative], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[SDCreativeResponse] | list[dict[str, Any]] | httpx.Response:
        """ """

        resp = await self._request(
            "POST",
            "/sd/creatives",
            json=[self.dump_json(x) for x in body],
        )
        return self._response_list(SDCreativeResponse, resp, mode=mode)

    @overload
    async def post_creative_preview(
        self, body: SDCreativePreviewRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDCreativePreviewResponse: ...
    @overload
    async def post_creative_preview(
        self, body: SDCreativePreviewRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def post_creative_preview(
        self, body: SDCreativePreviewRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def post_creative_preview(
        self, body: SDCreativePreviewRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDCreativePreviewResponse | dict[str, Any] | httpx.Response:
        """ """

        resp = await self._request(
            "POST",
            "/sd/creatives/preview",
            json=self.dump_json(body),
        )
        return self._response(SDCreativePreviewResponse, resp, mode=mode)

    @overload
    async def list_creative_moderations(
        self,
        language: SDLocale,
        *,
        mode: Literal["pydantic"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[SDCreativeModeration]: ...
    @overload
    async def list_creative_moderations(
        self,
        language: SDLocale,
        *,
        mode: Literal["dict"],
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_creative_moderations(
        self,
        language: SDLocale,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_creative_moderations(
        self,
        language: SDLocale,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[SDCreativeModeration] | list[dict[str, Any]] | httpx.Response:
        """

        Parameters
        ----------
        language : SDLocale
            The language of the returned creative moderation metadata.
        start_index : int
            Sets a cursor into the requested set of creative moderations. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0.
        count : int
            Sets the number of creative objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten creative moderations set `startIndex=0` and `count=10`. To return the next ten creative moderations, set `startIndex=10` and `count=10`, and so on. Defaults to max page size.
        ad_group_id_filter : str
            The returned array includes only creative moderations associated with ad group identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `creativeIdFilter` parameter.
        creative_id_filter : str
            The returned array includes only creative moderations with creative identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `adGroupIdFilter` parameter.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        params = {
            "language": language,
            "startIndex": start_index,
            "count": count,
            "adGroupIdFilter": ad_group_id_filter,
            "creativeIdFilter": creative_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/moderation/creatives", params=params)
        return self._response_list(SDCreativeModeration, resp, mode=mode)
