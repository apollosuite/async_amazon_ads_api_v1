"""MmmBrandGroupOverrides resource operations.

Generated from OpenAPI spec (tag: Brand Group Overrides).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource


class MmmBrandGroupOverrides(BaseResource):

    @overload
    async def create_mmm_brand_group_overrides(self, *, mode: Literal["pydantic"] = "pydantic") -> Any: ...
    @overload
    async def create_mmm_brand_group_overrides(self, *, mode: Literal["dict"]) -> Any: ...
    @overload
    async def create_mmm_brand_group_overrides(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_mmm_brand_group_overrides(self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic") -> Any:
        """Create overrides for brand groups. An override forces a brand group to include or exclude a specific product or campaign in reports. The products in a brand group can be listed in `GET /mmm/v1/brandGroups/{brandGroupId}/products`. The campaigns in a brand group can be listed in `GET /mmm/v1/brandGroups/{brandGroupId}/campaigns`. Some overrides require Amazon review before they are applied. If a brand group has an override that is `PENDING_REVIEW`, new reports for that brand group will not process until the review is completed. Overrides that are not permitted for the brand group will immediately return a 403 error code. Contact <mmm-support@amazon.com> if this is unexpected."""

        resp = await self._request("POST", "/mmm/v1/brandGroupOverrides")
        if mode == "raw":
            return resp
        return resp.json()

    @overload
    async def delete_mmm_brand_group_overrides(self, *, mode: Literal["pydantic"] = "pydantic") -> Any: ...
    @overload
    async def delete_mmm_brand_group_overrides(self, *, mode: Literal["dict"]) -> Any: ...
    @overload
    async def delete_mmm_brand_group_overrides(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_mmm_brand_group_overrides(self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic") -> Any:
        """Delete overrides for brand groups. If this operation deletes all the overrides in a brand group that are `PENDING_REVIEW`, any reports waiting on those reviews will be processed."""

        resp = await self._request("POST", "/mmm/v1/brandGroupOverrides/delete")
        if mode == "raw":
            return resp
        return resp.json()

    @overload
    async def list_mmm_brand_group_overrides(self, *, mode: Literal["pydantic"] = "pydantic") -> Any: ...
    @overload
    async def list_mmm_brand_group_overrides(self, *, mode: Literal["dict"]) -> Any: ...
    @overload
    async def list_mmm_brand_group_overrides(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def list_mmm_brand_group_overrides(self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic") -> Any:
        """List overrides for brand groups."""

        resp = await self._request("POST", "/mmm/v1/brandGroupOverrides/list")
        if mode == "raw":
            return resp
        return resp.json()
