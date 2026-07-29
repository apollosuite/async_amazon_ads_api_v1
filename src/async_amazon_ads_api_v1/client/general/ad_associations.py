"""AdAssociations resource operations.

Generated from OpenAPI spec (tag: AdAssociations).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.general.ad_associations import (
    AdAssociationMultiStatusResponse,
    AdAssociationSuccessResponse,
    CreateAdAssociationRequest,
    DeleteAdAssociationRequest,
    QueryAdAssociationRequest,
    UpdateAdAssociationRequest,
)


class AdAssociations(BaseResource):

    async def create_ad_association(self, body: CreateAdAssociationRequest) -> AdAssociationMultiStatusResponse:
        """Create Ad Association"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adAssociations",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(AdAssociationMultiStatusResponse, resp)

    async def delete_ad_association(self, body: DeleteAdAssociationRequest) -> AdAssociationMultiStatusResponse:
        """Delete Ad Association"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adAssociations",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(AdAssociationMultiStatusResponse, resp)

    async def query_ad_association(self, body: QueryAdAssociationRequest) -> AdAssociationSuccessResponse:
        """Query Ad Association"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adAssociations",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(AdAssociationSuccessResponse, resp)

    async def update_ad_association(self, body: UpdateAdAssociationRequest) -> AdAssociationMultiStatusResponse:
        """Update Ad Association"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adAssociations",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(AdAssociationMultiStatusResponse, resp)
