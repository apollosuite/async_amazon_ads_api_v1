"""ProductEligibility resource operations.

Generated from OpenAPI spec (tag: product_eligibility).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.products.product_eligibility import (
    ProductEligibilityRequest,
    ProductEligibilityResponse,
    ProgramEligibilityRequestContent,
    ProgramEligibilityResponseContent,
)


class ProductEligibility(BaseResource):

    @overload
    async def product_eligibility(
        self, body: ProductEligibilityRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def product_eligibility(
        self, body: ProductEligibilityRequest, *, mode: Literal["pydantic"]
    ) -> ProductEligibilityResponse: ...
    @overload
    async def product_eligibility(self, body: ProductEligibilityRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def product_eligibility(
        self, body: ProductEligibilityRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ProductEligibilityResponse | dict[str, Any] | httpx.Response:
        """Gets a list of advertising eligibility objects for a set of products. Requests are permitted only for products sold by the merchant associated with the profile. Note that the request object is a list of ASINs, but multiple SKUs are returned if there is more than one SKU associated with an ASIN. If a product is not eligible for advertising, the response includes an object describing the reasons for ineligibility."""

        resp = await self._request("POST", "/eligibility/product/list", json=self.dump_json(body))
        return self._response(ProductEligibilityResponse, resp, mode=mode)

    @overload
    async def program_eligibility(
        self, body: ProgramEligibilityRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def program_eligibility(
        self, body: ProgramEligibilityRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> ProgramEligibilityResponseContent: ...
    @overload
    async def program_eligibility(
        self, body: ProgramEligibilityRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def program_eligibility(
        self, body: ProgramEligibilityRequestContent | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ProgramEligibilityResponseContent | dict[str, Any] | httpx.Response:
        """Checks the advertiser's eligibility to ad programs."""

        resp = await self._request(
            "POST",
            "/eligibility/programs",
            json=self.dump_json(body),
            headers={"Accept": "application/vnd.programeligibility.v2+json"},
        )
        return self._response(ProgramEligibilityResponseContent, resp, mode=mode)
