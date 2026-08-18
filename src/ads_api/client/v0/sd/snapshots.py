"""Snapshots resource operations.

Generated from OpenAPI spec (tag: Snapshots).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.snapshots import (
    SnapshotRequest,
    SnapshotResponse,
)


class Snapshots(BaseResource):

    @overload
    async def create_snapshot(
        self, record_type: str, body: SnapshotRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SnapshotResponse: ...
    @overload
    async def create_snapshot(
        self, record_type: str, body: SnapshotRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_snapshot(
        self, record_type: str, body: SnapshotRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_snapshot(
        self, record_type: str, body: SnapshotRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SnapshotResponse | dict[str, Any] | httpx.Response:
        """**Note: Snapshots APIs are deprecated and will be shut off on October 15, 2024. For replacement functionality, see the [exports](guides/exports/overview) API. To learn more, view the [migration guide](reference/migration-guides/snapshots-exports).**"""

        resp = await self._request("POST", f"/sd/{record_type}/snapshot", json=self.dump_json(body))
        return self._response(SnapshotResponse, resp, mode=mode)

    @overload
    async def download_snapshot(self, snapshot_id: str, *, mode: Literal["pydantic"] = "pydantic") -> Any: ...
    @overload
    async def download_snapshot(self, snapshot_id: str, *, mode: Literal["dict"]) -> Any: ...
    @overload
    async def download_snapshot(self, snapshot_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def download_snapshot(
        self, snapshot_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> Any:
        """**Note: Snapshots APIs are deprecated and will be shut off on October 15, 2024. For replacement functionality, see the [exports](guides/exports/overview) API. To learn more, view the [migration guide](reference/migration-guides/snapshots-exports).**"""

        resp = await self._request("GET", f"/sd/snapshots/{snapshot_id}/download")
        if mode == "raw":
            return resp
        return resp.json()

    @overload
    async def get_snapshot(self, snapshot_id: str, *, mode: Literal["pydantic"] = "pydantic") -> SnapshotResponse: ...
    @overload
    async def get_snapshot(self, snapshot_id: str, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_snapshot(self, snapshot_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_snapshot(
        self, snapshot_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SnapshotResponse | dict[str, Any] | httpx.Response:
        """**Note: Snapshots APIs are deprecated and will be shut off on October 15, 2024. For replacement functionality, see the [exports](guides/exports/overview) API. To learn more, view the [migration guide](reference/migration-guides/snapshots-exports).**"""

        resp = await self._request("GET", f"/sd/snapshots/{snapshot_id}")
        return self._response(SnapshotResponse, resp, mode=mode)
