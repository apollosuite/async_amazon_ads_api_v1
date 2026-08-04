"""GeoLocations resource operations.

Generated from OpenAPI spec (tag: GeoLocations).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.general.geo_locations import (
    CreateGeoLocationRequest,
    GeoLocationMultiStatusResponse,
)


class GeoLocations(BaseResource):

    async def create_geo_location(self, body: CreateGeoLocationRequest) -> GeoLocationMultiStatusResponse:
        """Create geo location targeting definitions. Supports smart locations, which target users based on their percentile rank within a Smart Location Index, and radius locations, which target users within a specified distance of an address or coordinate. Note: radius locations are currently in beta."""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/geoLocations",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(GeoLocationMultiStatusResponse, resp)
