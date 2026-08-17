"""DSPAdAssociations resource operations.

Generated from OpenAPI spec (tag: AdAssociations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_associations.dsp import (
    DSPAdAssociationMultiStatusResponse,
    DSPAdAssociationSuccessResponse,
    DSPCreateAdAssociationRequest,
    DSPDeleteAdAssociationRequest,
    DSPQueryAdAssociationRequest,
    DSPUpdateAdAssociationRequest,
)


class DSPAdAssociations(BaseResource):

    @overload
    async def create_ad_association(
        self, body: DSPCreateAdAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPAdAssociationMultiStatusResponse: ...
    @overload
    async def create_ad_association(
        self, body: DSPCreateAdAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_ad_association(
        self, body: DSPCreateAdAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_ad_association(
        self, body: DSPCreateAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPAdAssociationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create Ad Association"""

        resp = await self._request("POST", "/adsApi/v1/create/adAssociations", json=self.dump_json(body))
        return self._response(DSPAdAssociationMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_ad_association(
        self, body: DSPDeleteAdAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPAdAssociationMultiStatusResponse: ...
    @overload
    async def delete_ad_association(
        self, body: DSPDeleteAdAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def delete_ad_association(
        self, body: DSPDeleteAdAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_ad_association(
        self, body: DSPDeleteAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPAdAssociationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete Ad Association"""

        resp = await self._request("POST", "/adsApi/v1/delete/adAssociations", json=self.dump_json(body))
        return self._response(DSPAdAssociationMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_ad_association(
        self, body: DSPQueryAdAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPAdAssociationSuccessResponse: ...
    @overload
    async def query_ad_association(
        self, body: DSPQueryAdAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_ad_association(
        self, body: DSPQueryAdAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_ad_association(
        self, body: DSPQueryAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPAdAssociationSuccessResponse | dict[str, Any] | httpx.Response:
        """Query Ad Association"""

        resp = await self._request("POST", "/adsApi/v1/query/adAssociations", json=self.dump_json(body))
        return self._response(DSPAdAssociationSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad_association(
        self, body: DSPUpdateAdAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPAdAssociationMultiStatusResponse: ...
    @overload
    async def update_ad_association(
        self, body: DSPUpdateAdAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_ad_association(
        self, body: DSPUpdateAdAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_ad_association(
        self, body: DSPUpdateAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPAdAssociationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update Ad Association"""

        resp = await self._request("POST", "/adsApi/v1/update/adAssociations", json=self.dump_json(body))
        return self._response(DSPAdAssociationMultiStatusResponse, resp, mode=mode)
