"""SDCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.sd import (
    SDCampaignMultiStatusResponse,
    SDCampaignSuccessResponse,
    SDCreateCampaignRequest,
    SDDeleteCampaignRequest,
    SDQueryCampaignRequest,
    SDUpdateCampaignRequest,
)


class SDCampaigns(BaseResource):

    @overload
    def create_campaign(self, body: SDCreateCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_campaign(
        self, body: SDCreateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SDCampaignMultiStatusResponse: ...
    @overload
    def create_campaign(self, body: SDCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_campaign(
        self, body: SDCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(SDCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_campaign(self, body: SDDeleteCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_campaign(
        self, body: SDDeleteCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SDCampaignMultiStatusResponse: ...
    @overload
    def delete_campaign(self, body: SDDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_campaign(
        self, body: SDDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = self._request("POST", "/adsApi/v1/delete/campaigns", json=self.dump_json(body))
        return self._response(SDCampaignMultiStatusResponse, resp, mode=mode)

    @overload
    def query_campaign(self, body: SDQueryCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_campaign(
        self, body: SDQueryCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SDCampaignSuccessResponse: ...
    @overload
    def query_campaign(self, body: SDQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_campaign(
        self, body: SDQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(SDCampaignSuccessResponse, resp, mode=mode)

    @overload
    def update_campaign(self, body: SDUpdateCampaignRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_campaign(
        self, body: SDUpdateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SDCampaignMultiStatusResponse: ...
    @overload
    def update_campaign(self, body: SDUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_campaign(
        self, body: SDUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDCampaignMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(SDCampaignMultiStatusResponse, resp, mode=mode)
