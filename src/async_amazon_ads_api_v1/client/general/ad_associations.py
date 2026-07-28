"""AdAssociations resource operations.

Generated from OpenAPI spec (tag: AdAssociations).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.general.ad_associations import (
    AdAssociationMultiStatusResponse,
    AdAssociationSuccessResponse,
    CreateAdAssociationRequest,
    DeleteAdAssociationRequest,
    QueryAdAssociationRequest,
    UpdateAdAssociationRequest,
)


class AdAssociations(_ResourceBase):

    async def create_ad_association(self, body: CreateAdAssociationRequest) -> AdAssociationMultiStatusResponse:
        """Create Ad Association"""

        return await self._query(body, "/adsApi/v1/create/adAssociations", AdAssociationMultiStatusResponse)

    async def delete_ad_association(self, body: DeleteAdAssociationRequest) -> AdAssociationMultiStatusResponse:
        """Delete Ad Association"""

        return await self._query(body, "/adsApi/v1/delete/adAssociations", AdAssociationMultiStatusResponse)

    async def query_ad_association(self, body: QueryAdAssociationRequest) -> AdAssociationSuccessResponse:
        """Query Ad Association"""

        return await self._query(body, "/adsApi/v1/query/adAssociations", AdAssociationSuccessResponse)

    async def update_ad_association(self, body: UpdateAdAssociationRequest) -> AdAssociationMultiStatusResponse:
        """Update Ad Association"""

        return await self._query(body, "/adsApi/v1/update/adAssociations", AdAssociationMultiStatusResponse)
