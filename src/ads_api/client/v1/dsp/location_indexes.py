"""DSPLocationIndexes resource operations.

Generated from OpenAPI spec (tag: LocationIndexes).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.location_indexes.dsp import (
    DSPCreateLocationIndexRequest,
    DSPLocationIndexMultiStatusResponse,
    DSPLocationIndexSuccessResponse,
    DSPRetrieveLocationIndexRequest,
    DSPUpdateLocationIndexRequest,
)


class DSPLocationIndexes(BaseResource):

    @overload
    async def create_location_index(
        self, body: DSPCreateLocationIndexRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPLocationIndexMultiStatusResponse: ...
    @overload
    async def create_location_index(
        self, body: DSPCreateLocationIndexRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_location_index(
        self, body: DSPCreateLocationIndexRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_location_index(
        self, body: DSPCreateLocationIndexRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPLocationIndexMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create a Smart Location Index. A Smart Location Index is a named dataset that maps postal codes to index values representing relative audience quality or sales potential for a given advertiser. Index data is processed asynchronously; the index status will transition from PENDING to ENABLED once processing is complete."""

        resp = await self._request("POST", "/adsApi/v1/create/locationIndexes", json=self.dump_json(body))
        return self._response(DSPLocationIndexMultiStatusResponse, resp, mode=mode)

    @overload
    async def list_location_index(
        self, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None, max_results: int | None = None
    ) -> DSPLocationIndexSuccessResponse: ...
    @overload
    async def list_location_index(
        self, *, mode: Literal["dict"], next_token: str | None = None, max_results: int | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def list_location_index(
        self, *, mode: Literal["raw"], next_token: str | None = None, max_results: int | None = None
    ) -> httpx.Response: ...
    async def list_location_index(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> DSPLocationIndexSuccessResponse | dict[str, Any] | httpx.Response:
        """List all Smart Location Indexes for the authenticated advertiser. Returns a paginated collection of indexes including their current processing status. Use the nextToken from the response to retrieve subsequent pages."""

        params = {
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/adsApi/v1/locationIndexes", params=params)
        return self._response(DSPLocationIndexSuccessResponse, resp, mode=mode)

    @overload
    async def retrieve_location_index(
        self, body: DSPRetrieveLocationIndexRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPLocationIndexMultiStatusResponse: ...
    @overload
    async def retrieve_location_index(
        self, body: DSPRetrieveLocationIndexRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def retrieve_location_index(
        self, body: DSPRetrieveLocationIndexRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def retrieve_location_index(
        self, body: DSPRetrieveLocationIndexRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPLocationIndexMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Retrieve one or more Smart Location Indexes by ID. Returns the current metadata and processing status for each requested index. An index with status PENDING is still being processed and is not yet available for use in smart location targeting."""

        resp = await self._request("POST", "/adsApi/v1/retrieve/locationIndexes", json=self.dump_json(body))
        return self._response(DSPLocationIndexMultiStatusResponse, resp, mode=mode)

    @overload
    async def update_location_index(
        self, body: DSPUpdateLocationIndexRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPLocationIndexMultiStatusResponse: ...
    @overload
    async def update_location_index(
        self, body: DSPUpdateLocationIndexRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_location_index(
        self, body: DSPUpdateLocationIndexRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_location_index(
        self, body: DSPUpdateLocationIndexRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPLocationIndexMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update the data for an existing Smart Location Index. Replaces the index's postal code values with the provided dataset. The update is processed asynchronously; the index status will return to PENDING until the new data has been fully processed."""

        resp = await self._request("POST", "/adsApi/v1/update/locationIndexes", json=self.dump_json(body))
        return self._response(DSPLocationIndexMultiStatusResponse, resp, mode=mode)
