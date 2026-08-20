"""AdAssociations resource operations.

Generated from OpenAPI spec (tag: AdAssociations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_associations.general import (
    AdAssociationMultiStatusResponse,
    AdAssociationSuccessResponse,
    CreateAdAssociationRequest,
    DeleteAdAssociationRequest,
    QueryAdAssociationRequest,
    UpdateAdAssociationRequest,
)


class AdAssociations(BaseResource):

    @overload
    async def create_ad_association(
        self, body: CreateAdAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdAssociationMultiStatusResponse: ...
    @overload
    async def create_ad_association(
        self, body: CreateAdAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_ad_association(
        self, body: CreateAdAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_ad_association(
        self, body: CreateAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdAssociationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create Ad Association"""

        resp = await self._request("POST", "/adsApi/v1/create/adAssociations", json=self.dump_json(body))
        return self._response(AdAssociationMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_ad_association(
        self, body: DeleteAdAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdAssociationMultiStatusResponse: ...
    @overload
    async def delete_ad_association(
        self, body: DeleteAdAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def delete_ad_association(
        self, body: DeleteAdAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_ad_association(
        self, body: DeleteAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdAssociationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete Ad Association"""

        resp = await self._request("POST", "/adsApi/v1/delete/adAssociations", json=self.dump_json(body))
        return self._response(AdAssociationMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_ad_association(
        self, body: QueryAdAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdAssociationSuccessResponse: ...
    @overload
    async def query_ad_association(
        self, body: QueryAdAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_ad_association(
        self, body: QueryAdAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_ad_association(
        self, body: QueryAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdAssociationSuccessResponse | dict[str, Any] | httpx.Response:
        """Query Ad Association"""

        resp = await self._request("POST", "/adsApi/v1/query/adAssociations", json=self.dump_json(body))
        return self._response(AdAssociationSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad_association(
        self, body: UpdateAdAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdAssociationMultiStatusResponse: ...
    @overload
    async def update_ad_association(
        self, body: UpdateAdAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_ad_association(
        self, body: UpdateAdAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_ad_association(
        self, body: UpdateAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdAssociationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update Ad Association"""

        resp = await self._request("POST", "/adsApi/v1/update/adAssociations", json=self.dump_json(body))
        return self._response(AdAssociationMultiStatusResponse, resp, mode=mode)
