"""DSPCommitments resource operations.

Generated from OpenAPI spec (tag: Commitments).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.commitments.dsp import (
    DSPCommitmentMultiStatusResponse,
    DSPCommitmentSuccessResponse,
    DSPCreateCommitmentRequest,
    DSPQueryCommitmentRequest,
    DSPRetrieveCommitmentRequest,
    DSPUpdateCommitmentRequest,
)


class DSPCommitments(BaseResource):

    @overload
    async def create_commitment(
        self, body: DSPCreateCommitmentRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPCommitmentMultiStatusResponse: ...
    @overload
    async def create_commitment(self, body: DSPCreateCommitmentRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_commitment(self, body: DSPCreateCommitmentRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_commitment(
        self, body: DSPCreateCommitmentRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPCommitmentMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create commitments"""

        resp = await self._request("POST", "/adsApi/v1/create/commitments", json=self.dump_json(body))
        return self._response(DSPCommitmentMultiStatusResponse, resp, mode=mode)

    @overload
    async def list_commitment(
        self, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None, max_results: int | None = None
    ) -> DSPCommitmentSuccessResponse: ...
    @overload
    async def list_commitment(
        self, *, mode: Literal["dict"], next_token: str | None = None, max_results: int | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def list_commitment(
        self, *, mode: Literal["raw"], next_token: str | None = None, max_results: int | None = None
    ) -> httpx.Response: ...
    async def list_commitment(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> DSPCommitmentSuccessResponse | dict[str, Any] | httpx.Response:
        """List commitments"""

        params = {
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/adsApi/v1/commitments", params=params)
        return self._response(DSPCommitmentSuccessResponse, resp, mode=mode)

    @overload
    async def query_commitment(
        self, body: DSPQueryCommitmentRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPCommitmentSuccessResponse: ...
    @overload
    async def query_commitment(self, body: DSPQueryCommitmentRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_commitment(self, body: DSPQueryCommitmentRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_commitment(
        self, body: DSPQueryCommitmentRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPCommitmentSuccessResponse | dict[str, Any] | httpx.Response:
        """Query commitments with filters"""

        resp = await self._request("POST", "/adsApi/v1/query/commitments", json=self.dump_json(body))
        return self._response(DSPCommitmentSuccessResponse, resp, mode=mode)

    @overload
    async def retrieve_commitment(
        self, body: DSPRetrieveCommitmentRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPCommitmentMultiStatusResponse: ...
    @overload
    async def retrieve_commitment(
        self, body: DSPRetrieveCommitmentRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def retrieve_commitment(
        self, body: DSPRetrieveCommitmentRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def retrieve_commitment(
        self, body: DSPRetrieveCommitmentRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPCommitmentMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Get Commitments"""

        resp = await self._request("POST", "/adsApi/v1/retrieve/commitments", json=self.dump_json(body))
        return self._response(DSPCommitmentMultiStatusResponse, resp, mode=mode)

    @overload
    async def update_commitment(
        self, body: DSPUpdateCommitmentRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPCommitmentMultiStatusResponse: ...
    @overload
    async def update_commitment(self, body: DSPUpdateCommitmentRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def update_commitment(self, body: DSPUpdateCommitmentRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_commitment(
        self, body: DSPUpdateCommitmentRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPCommitmentMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update commitments"""

        resp = await self._request("POST", "/adsApi/v1/update/commitments", json=self.dump_json(body))
        return self._response(DSPCommitmentMultiStatusResponse, resp, mode=mode)
