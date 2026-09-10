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
    def retrieve_commitment_spend(
        self, body: DSPRetrieveCommitmentSpendRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def retrieve_commitment_spend(
        self, body: DSPRetrieveCommitmentSpendRequest, *, mode: Literal["pydantic"]
    ) -> DSPCommitmentSpendMultiStatusResponse: ...
    @overload
    def retrieve_commitment_spend(
        self, body: DSPRetrieveCommitmentSpendRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def retrieve_commitment_spend(
        self, body: DSPRetrieveCommitmentSpendRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPCommitmentSpendMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Retrieve commitment spend"""

        resp = self._request("POST", "/adsApi/v1/retrieve/commitmentSpends", json=self.dump_json(body))
        return self._response(DSPCommitmentSpendMultiStatusResponse, resp, mode=mode)
