"""LocationIndexes resource operations.

Generated from OpenAPI spec (tag: LocationIndexes).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.general.location_indexes import (
    CreateLocationIndexRequest,
    LocationIndexMultiStatusResponse,
    LocationIndexSuccessResponse,
    RetrieveLocationIndexRequest,
    UpdateLocationIndexRequest,
)


class LocationIndexes(_ResourceBase):

    async def create_location_index(self, body: CreateLocationIndexRequest) -> LocationIndexMultiStatusResponse:
        """Create a Smart Location Index.

        A Smart Location Index is a named dataset that maps postal codes to index values representing relative audience
        quality or sales potential for a given advertiser. Index data is processed asynchronously; the index status will
        transition from PENDING to ENABLED once processing is complete.
        """
        return await self._query(body, "/adsApi/v1/create/locationIndexes", LocationIndexMultiStatusResponse)

    async def list_location_index(
        self, next_token: str | None = None, max_results: int | None = None
    ) -> LocationIndexSuccessResponse:
        """List all Smart Location Indexes for the authenticated advertiser.

        Returns a paginated collection of indexes including their current processing status. Use the nextToken from the
        response to retrieve subsequent pages.
        """
        params = {
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/adsApi/v1/locationIndexes", params=params)
        return self._response(LocationIndexSuccessResponse, resp)

    async def retrieve_location_index(self, body: RetrieveLocationIndexRequest) -> LocationIndexMultiStatusResponse:
        """Retrieve one or more Smart Location Indexes by ID.

        Returns the current metadata and processing status for each requested index. An index with status PENDING is
        still being processed and is not yet available for use in smart location targeting.
        """
        return await self._query(body, "/adsApi/v1/retrieve/locationIndexes", LocationIndexMultiStatusResponse)

    async def update_location_index(self, body: UpdateLocationIndexRequest) -> LocationIndexMultiStatusResponse:
        """Update the data for an existing Smart Location Index.

        Replaces the index's postal code values with the provided dataset. The update is processed asynchronously; the
        index status will return to PENDING until the new data has been fully processed.
        """
        return await self._query(body, "/adsApi/v1/update/locationIndexes", LocationIndexMultiStatusResponse)
