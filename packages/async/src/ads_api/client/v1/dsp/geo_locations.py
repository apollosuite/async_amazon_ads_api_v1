"""DSPGeoLocations resource operations.

Generated from OpenAPI spec (tag: GeoLocations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.geo_locations.dsp import (
    DSPCreateGeoLocationRequest,
    DSPGeoLocationMultiStatusResponse,
)


class DSPGeoLocations(BaseResource):

    @overload
    async def create_geo_location(
        self, body: DSPCreateGeoLocationRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_geo_location(
        self, body: DSPCreateGeoLocationRequest, *, mode: Literal["pydantic"]
    ) -> DSPGeoLocationMultiStatusResponse: ...
    @overload
    async def create_geo_location(
        self, body: DSPCreateGeoLocationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_geo_location(
        self, body: DSPCreateGeoLocationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPGeoLocationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create geo location targeting definitions. Supports smart locations, which target users based on their percentile rank within a Smart Location Index, and radius locations, which target users within a specified distance of an address or coordinate. Note: radius locations are currently in beta."""

        resp = await self._request("POST", "/adsApi/v1/create/geoLocations", json=self.dump_json(body))
        return self._response(DSPGeoLocationMultiStatusResponse, resp, mode=mode)
