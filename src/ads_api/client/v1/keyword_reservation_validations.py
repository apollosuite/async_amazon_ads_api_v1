"""KeywordReservationValidations resource operations.

Generated from OpenAPI spec (tag: KeywordReservationValidations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.keyword_reservation_validations.general import (
    SBCreateKeywordReservationValidationRequest,
    SBKeywordReservationValidationMultiStatusResponse,
)


class KeywordReservationValidations(BaseResource):

    @overload
    async def create_keyword_reservation_validation(
        self, body: SBCreateKeywordReservationValidationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBKeywordReservationValidationMultiStatusResponse: ...
    @overload
    async def create_keyword_reservation_validation(
        self, body: SBCreateKeywordReservationValidationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_keyword_reservation_validation(
        self, body: SBCreateKeywordReservationValidationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_keyword_reservation_validation(
        self,
        body: SBCreateKeywordReservationValidationRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SBKeywordReservationValidationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Validate keyword reservation"""

        resp = await self._request(
            "POST", "/adsApi/v1/create/keywordReservationValidations/sb", json=self.dump_json(body)
        )
        return self._response(SBKeywordReservationValidationMultiStatusResponse, resp, mode=mode)
