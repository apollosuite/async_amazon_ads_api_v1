"""SBCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.sb import (
    SBCampaignMultiStatusResponse,
    SBCampaignSuccessResponse,
    SBCreateCampaignRequest,
    SBDeleteCampaignRequest,
    SBQueryCampaignRequest,
    SBUpdateCampaignRequest,
)


class SBCampaigns(BaseResource):

    @overload
    def create_campaign(self, body: SBCreateCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_campaign(
        self, body: SBCreateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SBCampaignMultiStatusResponse: ...
    @overload
    def create_campaign(self, body: SBCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_campaign(
        self, body: SBCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(SBCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_campaign(self, body: SBDeleteCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_campaign(
        self, body: SBDeleteCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SBCampaignMultiStatusResponse: ...
    @overload
    def delete_campaign(self, body: SBDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_campaign(
        self, body: SBDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = self._request("POST", "/adsApi/v1/delete/campaigns", json=self.dump_json(body))
        return self._response(SBCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    def query_campaign(self, body: SBQueryCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_campaign(
        self, body: SBQueryCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SBCampaignSuccessResponse: ...
    @overload
    def query_campaign(self, body: SBQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_campaign(
        self, body: SBQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(SBCampaignSuccessResponse, resp, mode=mode)

    @overload
    def update_campaign(self, body: SBUpdateCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_campaign(
        self, body: SBUpdateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SBCampaignMultiStatusResponse: ...
    @overload
    def update_campaign(self, body: SBUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_campaign(
        self, body: SBUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(SBCampaignMultiStatusResponse, resp, mode=mode)
