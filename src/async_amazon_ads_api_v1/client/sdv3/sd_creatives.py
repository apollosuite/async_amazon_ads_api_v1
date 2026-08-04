"""SDCreatives resource operations.

Generated from OpenAPI spec (tag: Creatives).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sdv3.sd_creatives import (
    Locale,
    SDCreateCreative,
    SDCreative,
    SDCreativeModeration,
    SDCreativePreviewRequest,
    SDCreativePreviewResponse,
    SDCreativeResponse,
    SDCreativeUpdate,
)


class SDCreatives(BaseResource):

    async def list_creatives(
        self,
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[SDCreative]:
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
        """

        params = {
            "startIndex": start_index,
            "count": count,
            "adGroupIdFilter": ad_group_id_filter,
            "creativeIdFilter": creative_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/creatives", params=params)
        return self._response_list(SDCreative, resp)

    async def update_creatives(self, body: list[SDCreativeUpdate]) -> list[SDCreativeResponse]:
        """ """

        resp = await self._request(
            "PUT",
            "/sd/creatives",
            json=[x.model_dump(exclude_none=True) for x in body],
        )
        return self._response_list(SDCreativeResponse, resp)

    async def create_creatives(self, body: list[SDCreateCreative]) -> list[SDCreativeResponse]:
        """ """

        resp = await self._request(
            "POST",
            "/sd/creatives",
            json=[x.model_dump(exclude_none=True) for x in body],
        )
        return self._response_list(SDCreativeResponse, resp)

    async def post_creative_preview(self, body: SDCreativePreviewRequest) -> SDCreativePreviewResponse:
        """ """

        resp = await self._request(
            "POST",
            "/sd/creatives/preview",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SDCreativePreviewResponse, resp)

    async def list_creative_moderations(
        self,
        language: Locale,
        start_index: int | None = None,
        count: int | None = None,
        ad_group_id_filter: str | None = None,
        creative_id_filter: str | None = None,
    ) -> list[SDCreativeModeration]:
        """

        Parameters
        ----------
        language : Locale
            The language of the returned creative moderation metadata.
        start_index : int
            Sets a cursor into the requested set of creative moderations. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0.
        count : int
            Sets the number of creative objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten creative moderations set `startIndex=0` and `count=10`. To return the next ten creative moderations, set `startIndex=10` and `count=10`, and so on. Defaults to max page size.
        ad_group_id_filter : str
            The returned array includes only creative moderations associated with ad group identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `creativeIdFilter` parameter.
        creative_id_filter : str
            The returned array includes only creative moderations with creative identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `adGroupIdFilter` parameter.
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
        return self._response_list(SDCreativeModeration, resp)
