"""DSPCommitmentSpends resource operations.

Generated from OpenAPI spec (tag: CommitmentSpends).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.commitment_spends.dsp import (
    DSPCommitmentSpendMultiStatusResponse,
    DSPRetrieveCommitmentSpendRequest,
)


class DSPCommitmentSpends(BaseResource):

    @overload
    async def retrieve_commitment_spend(
        self, body: DSPRetrieveCommitmentSpendRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPCommitmentSpendMultiStatusResponse: ...
    @overload
    async def retrieve_commitment_spend(
        self, body: DSPRetrieveCommitmentSpendRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def retrieve_commitment_spend(
        self, body: DSPRetrieveCommitmentSpendRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def retrieve_commitment_spend(
        self, body: DSPRetrieveCommitmentSpendRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPCommitmentSpendMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Retrieve commitment spend"""

        resp = await self._request("POST", "/adsApi/v1/retrieve/commitmentSpends", json=self.dump_json(body))
        return self._response(DSPCommitmentSpendMultiStatusResponse, resp, mode=mode)
