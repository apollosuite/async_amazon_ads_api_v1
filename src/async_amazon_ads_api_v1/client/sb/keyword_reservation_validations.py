"""KeywordReservationValidations resource operations.

Generated from OpenAPI spec (tag: KeywordReservationValidations).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.keyword_reservation_validations import (
    SBCreateKeywordReservationValidationRequest,
    SBKeywordReservationValidationMultiStatusResponse,
)


class KeywordReservationValidations(BaseResource):

    async def sb_create_keyword_reservation_validation(
        self, body: SBCreateKeywordReservationValidationRequest
    ) -> SBKeywordReservationValidationMultiStatusResponse:
        """Validate keyword reservation"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/keywordReservationValidations/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBKeywordReservationValidationMultiStatusResponse, resp)
