"""SB KeywordReservationValidation resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.keyword_reservation_validations import (
    SBKeywordReservationValidationCreate,
    SBKeywordReservationValidationMultiStatusResponse,
)


class KeywordReservationValidations(_ResourceBase):

    async def create(
        self, items: list[SBKeywordReservationValidationCreate]
    ) -> SBKeywordReservationValidationMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/keywordReservationValidations/sb",
            json={"keywordReservationValidations": self._validate(items)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBKeywordReservationValidationMultiStatusResponse, resp)
