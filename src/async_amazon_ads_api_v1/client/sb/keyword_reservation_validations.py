"""SB KeywordReservationValidation resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb import (
    SBKeywordReservationValidationCreate,
    SBKeywordReservationValidationMultiStatusResponse,
)


class KeywordReservationValidations(_ResourceBase):
    _spec = _ResourceSpec(
        name="keywordReservationValidations",
        create_model=SBKeywordReservationValidationCreate,
        path_suffix="/sb",
    )

    async def create(
        self, items: list[SBKeywordReservationValidationCreate]
    ) -> SBKeywordReservationValidationMultiStatusResponse:
        return await self._create(items, self._spec, SBKeywordReservationValidationMultiStatusResponse)
