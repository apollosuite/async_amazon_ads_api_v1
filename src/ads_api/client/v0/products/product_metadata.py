"""ProductMetadata resource operations.

Generated from OpenAPI spec (tag: Product Selector).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.products.product_metadata import (
    ProductMetadataRequest,
    ProductMetadataResponse,
)


class ProductMetadata(BaseResource):

    @overload
    async def product_metadata(
        self, body: ProductMetadataRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def product_metadata(
        self, body: ProductMetadataRequest, *, mode: Literal["pydantic"]
    ) -> ProductMetadataResponse: ...
    @overload
    async def product_metadata(self, body: ProductMetadataRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def product_metadata(
        self, body: ProductMetadataRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ProductMetadataResponse | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "POST",
            "/product/metadata",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.productmetadatarequest.v1+json",
                "Accept": "application/vnd.productmetadatarequest.v1+json",
            },
        )
        return self._response(ProductMetadataResponse, resp, mode=mode)
