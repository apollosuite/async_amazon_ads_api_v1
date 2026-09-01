"""BrandStoreEditions resource operations.

Generated from OpenAPI spec (tag: BrandStoreEditions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.brand_store_editions.general import (
    BrandStoreEditionSuccessResponse,
)


class BrandStoreEditions(BaseResource):

    @overload
    async def list_brand_store_edition(
        self,
        brand_store_id: str,
        *,
        mode: Literal["dict"] = "dict",
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def list_brand_store_edition(
        self,
        brand_store_id: str,
        *,
        mode: Literal["pydantic"],
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> BrandStoreEditionSuccessResponse: ...
    @overload
    async def list_brand_store_edition(
        self,
        brand_store_id: str,
        *,
        mode: Literal["raw"],
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> httpx.Response: ...
    async def list_brand_store_edition(
        self,
        brand_store_id: str,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> BrandStoreEditionSuccessResponse | dict[str, Any] | httpx.Response:
        """Retrieve brand store page content"""

        params = {
            "brandStoreId": brand_store_id,
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/adsApi/v1/brandStoreEditions", params=params)
        return self._response(BrandStoreEditionSuccessResponse, resp, mode=mode)
