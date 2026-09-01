"""Exports resource operations.

Generated from OpenAPI spec (tag: Exports).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.exports.exports import (
    BaseUniversalApiExportRequest,
    TargetsUniversalApiExportRequest,
    UniversalApiExportResponse,
)


class Exports(BaseResource):

    @overload
    async def ad_export(
        self, body: BaseUniversalApiExportRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def ad_export(
        self, body: BaseUniversalApiExportRequest, *, mode: Literal["pydantic"]
    ) -> UniversalApiExportResponse: ...
    @overload
    async def ad_export(self, body: BaseUniversalApiExportRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def ad_export(
        self, body: BaseUniversalApiExportRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> UniversalApiExportResponse | dict[str, Any] | httpx.Response:
        """Creates a file-based export of Ads in the account satisfying the filtering criteria."""

        resp = await self._request(
            "POST",
            "/ads/export",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.adsexport.v1+json",
                "Accept": "application/vnd.adsexport.v1+json",
            },
        )
        return self._response(UniversalApiExportResponse, resp, mode=mode)

    @overload
    async def ad_group_export(
        self, body: BaseUniversalApiExportRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def ad_group_export(
        self, body: BaseUniversalApiExportRequest, *, mode: Literal["pydantic"]
    ) -> UniversalApiExportResponse: ...
    @overload
    async def ad_group_export(self, body: BaseUniversalApiExportRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def ad_group_export(
        self, body: BaseUniversalApiExportRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> UniversalApiExportResponse | dict[str, Any] | httpx.Response:
        """Creates a file-based export of Ad Groups in the account satisfying the filtering criteria."""

        resp = await self._request(
            "POST",
            "/adGroups/export",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.adgroupsexport.v1+json",
                "Accept": "application/vnd.adgroupsexport.v1+json",
            },
        )
        return self._response(UniversalApiExportResponse, resp, mode=mode)

    @overload
    async def campaign_export(
        self, body: BaseUniversalApiExportRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def campaign_export(
        self, body: BaseUniversalApiExportRequest, *, mode: Literal["pydantic"]
    ) -> UniversalApiExportResponse: ...
    @overload
    async def campaign_export(self, body: BaseUniversalApiExportRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def campaign_export(
        self, body: BaseUniversalApiExportRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> UniversalApiExportResponse | dict[str, Any] | httpx.Response:
        """Creates a file-based export of Campaigns in the account satisfying the filtering criteria."""

        resp = await self._request(
            "POST",
            "/campaigns/export",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.campaignsexport.v1+json",
                "Accept": "application/vnd.campaignsexport.v1+json",
            },
        )
        return self._response(UniversalApiExportResponse, resp, mode=mode)

    @overload
    async def get_export(
        self,
        export_id: str,
        *,
        accept: Literal[
            "application/vnd.adgroupsexport.v1+json",
            "application/vnd.adsexport.v1+json",
            "application/vnd.campaignsexport.v1+json",
            "application/vnd.targetsexport.v1+json",
        ],
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def get_export(
        self,
        export_id: str,
        *,
        accept: Literal[
            "application/vnd.adgroupsexport.v1+json",
            "application/vnd.adsexport.v1+json",
            "application/vnd.campaignsexport.v1+json",
            "application/vnd.targetsexport.v1+json",
        ],
        mode: Literal["pydantic"],
    ) -> UniversalApiExportResponse: ...
    @overload
    async def get_export(
        self,
        export_id: str,
        *,
        accept: Literal[
            "application/vnd.adgroupsexport.v1+json",
            "application/vnd.adsexport.v1+json",
            "application/vnd.campaignsexport.v1+json",
            "application/vnd.targetsexport.v1+json",
        ],
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def get_export(
        self,
        export_id: str,
        *,
        accept: Literal[
            "application/vnd.adgroupsexport.v1+json",
            "application/vnd.adsexport.v1+json",
            "application/vnd.campaignsexport.v1+json",
            "application/vnd.targetsexport.v1+json",
        ],
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> UniversalApiExportResponse | dict[str, Any] | httpx.Response:
        """This API will return a status of the specified export."""

        headers = {}
        headers["Accept"] = accept
        resp = await self._request("GET", f"/exports/{export_id}", headers=headers)
        return self._response(UniversalApiExportResponse, resp, mode=mode)

    @overload
    async def target_export(
        self, body: TargetsUniversalApiExportRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def target_export(
        self, body: TargetsUniversalApiExportRequest, *, mode: Literal["pydantic"]
    ) -> UniversalApiExportResponse: ...
    @overload
    async def target_export(
        self, body: TargetsUniversalApiExportRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def target_export(
        self, body: TargetsUniversalApiExportRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> UniversalApiExportResponse | dict[str, Any] | httpx.Response:
        """Creates a file-based export of Targets in the account satisfying the filtering criteria."""

        resp = await self._request(
            "POST",
            "/targets/export",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.targetsexport.v1+json",
                "Accept": "application/vnd.targetsexport.v1+json",
            },
        )
        return self._response(UniversalApiExportResponse, resp, mode=mode)
