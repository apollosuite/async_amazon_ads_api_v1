"""SPCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.sp import (
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCreateCampaignRequest,
    SPDeleteCampaignRequest,
    SPQueryCampaignRequest,
    SPUpdateCampaignRequest,
)


class SPCampaigns(BaseResource):

    @overload
    def create_campaign(self, body: SPCreateCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_campaign(
        self, body: SPCreateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SPCampaignMultiStatusResponse: ...
    @overload
    def create_campaign(self, body: SPCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_campaign(
        self, body: SPCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(SPCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_campaign(self, body: SPDeleteCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_campaign(
        self, body: SPDeleteCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SPCampaignMultiStatusResponse: ...
    @overload
    def delete_campaign(self, body: SPDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_campaign(
        self, body: SPDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = self._request("POST", "/adsApi/v1/delete/campaigns", json=self.dump_json(body))
        return self._response(SPCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    def query_campaign(self, body: SPQueryCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_campaign(
        self, body: SPQueryCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SPCampaignSuccessResponse: ...
    @overload
    def query_campaign(self, body: SPQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_campaign(
        self, body: SPQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(SPCampaignSuccessResponse, resp, mode=mode)

    @overload
    def update_campaign(self, body: SPUpdateCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_campaign(
        self, body: SPUpdateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SPCampaignMultiStatusResponse: ...
    @overload
    def update_campaign(self, body: SPUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_campaign(
        self, body: SPUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(SPCampaignMultiStatusResponse, resp, mode=mode)
