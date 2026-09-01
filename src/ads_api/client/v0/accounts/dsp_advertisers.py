"""DSPAdvertisers resource operations.

Generated from OpenAPI spec (tag: Advertiser).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.accounts.dsp_advertisers import (
    DspAdvertisersV1,
    DspAdvertiserV1,
)


class DSPAdvertisers(BaseResource):

    @overload
    async def get_dsp_advertiser(self, advertiser_id: str, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def get_dsp_advertiser(self, advertiser_id: str, *, mode: Literal["pydantic"]) -> DspAdvertiserV1: ...
    @overload
    async def get_dsp_advertiser(self, advertiser_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_dsp_advertiser(
        self, advertiser_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DspAdvertiserV1 | dict[str, Any] | httpx.Response:
        """Returns advertiser information based on given advertiser id."""

        resp = await self._request("GET", f"/dsp/advertisers/{advertiser_id}")
        return self._response(DspAdvertiserV1, resp, mode=mode)

    @overload
    async def list_advertisers(
        self,
        *,
        mode: Literal["dict"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        advertiser_id_filter: str | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def list_advertisers(
        self,
        *,
        mode: Literal["pydantic"],
        start_index: int | None = None,
        count: int | None = None,
        advertiser_id_filter: str | None = None,
    ) -> DspAdvertisersV1: ...
    @overload
    async def list_advertisers(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        advertiser_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_advertisers(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        advertiser_id_filter: str | None = None,
    ) -> DspAdvertisersV1 | dict[str, Any] | httpx.Response:
        """Returns a list of advertisers with information which satisfy the filtering criteria."""

        params = {
            "startIndex": start_index,
            "count": count,
            "advertiserIdFilter": advertiser_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/dsp/advertisers", params=params)
        return self._response(DspAdvertisersV1, resp, mode=mode)
