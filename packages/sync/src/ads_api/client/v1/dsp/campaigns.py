"""DSPCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.dsp import (
    DSPCampaignMultiStatusResponse,
    DSPCampaignSuccessResponse,
    DSPCreateCampaignRequest,
    DSPQueryCampaignRequest,
    DSPUpdateCampaignRequest,
)


class DSPCampaigns(BaseResource):

    @overload
    def create_campaign(self, body: DSPCreateCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_campaign(
        self, body: DSPCreateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> DSPCampaignMultiStatusResponse: ...
    @overload
    def create_campaign(self, body: DSPCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_campaign(
        self, body: DSPCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(DSPCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    def query_campaign(self, body: DSPQueryCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_campaign(
        self, body: DSPQueryCampaignRequest, *, mode: Literal["pydantic"]
    ) -> DSPCampaignSuccessResponse: ...
    @overload
    def query_campaign(self, body: DSPQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_campaign(
        self, body: DSPQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(DSPCampaignSuccessResponse, resp, mode=mode)

    @overload
    def update_campaign(self, body: DSPUpdateCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_campaign(
        self, body: DSPUpdateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> DSPCampaignMultiStatusResponse: ...
    @overload
    def update_campaign(self, body: DSPUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_campaign(
        self, body: DSPUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(DSPCampaignMultiStatusResponse, resp, mode=mode)
