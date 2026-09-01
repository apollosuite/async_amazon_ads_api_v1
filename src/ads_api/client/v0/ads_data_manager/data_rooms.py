"""DataRooms resource operations.

Generated from OpenAPI spec (tag: Data rooms).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.ads_data_manager.data_rooms import (
    CreateDataroomResponseContent,
    GetDataroomMetadataResponseContent,
    GetDataroomResponseContent,
)


class DataRooms(BaseResource):

    @overload
    async def create_dataroom(self, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def create_dataroom(self, *, mode: Literal["pydantic"]) -> CreateDataroomResponseContent: ...
    @overload
    async def create_dataroom(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_dataroom(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CreateDataroomResponseContent | dict[str, Any] | httpx.Response:
        """Create a dataroom"""

        resp = await self._request("POST", "/adm/datarooms")
        return self._response(CreateDataroomResponseContent, resp, mode=mode)

    @overload
    async def get_dataroom(self, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def get_dataroom(self, *, mode: Literal["pydantic"]) -> GetDataroomResponseContent: ...
    @overload
    async def get_dataroom(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_dataroom(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> GetDataroomResponseContent | dict[str, Any] | httpx.Response:
        """Get a data room"""

        resp = await self._request("GET", "/adm/datarooms")
        return self._response(GetDataroomResponseContent, resp, mode=mode)

    @overload
    async def get_dataroom_metadata(self, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def get_dataroom_metadata(self, *, mode: Literal["pydantic"]) -> GetDataroomMetadataResponseContent: ...
    @overload
    async def get_dataroom_metadata(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_dataroom_metadata(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> GetDataroomMetadataResponseContent | dict[str, Any] | httpx.Response:
        """Gets dataset metadata including linked datasets, active dest., etc"""

        resp = await self._request(
            "GET", "/adm/datarooms/metadata", headers={"Accept": "application/vnd.admmetrics.v1+json"}
        )
        return self._response(GetDataroomMetadataResponseContent, resp, mode=mode)
