"""SPGlobalCampaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaigns.sp_global import (
    SPGlobalCampaignMultiStatusResponseWithPartialErrors,
    SPGlobalCampaignSuccessResponse,
    SPGlobalCreateCampaignRequest,
    SPGlobalDeleteCampaignRequest,
    SPGlobalQueryCampaignRequest,
    SPGlobalUpdateCampaignRequest,
)


class SPGlobalCampaigns(BaseResource):

    @overload
    def create_campaign(
        self, body: SPGlobalCreateCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_campaign(
        self, body: SPGlobalCreateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors: ...
    @overload
    def create_campaign(self, body: SPGlobalCreateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_campaign(
        self, body: SPGlobalCreateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = self._request("POST", "/adsApi/v1/create/campaigns", json=self.dump_json(body))
        return self._response(SPGlobalCampaignMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    def delete_campaign(
        self, body: SPGlobalDeleteCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def delete_campaign(
        self, body: SPGlobalDeleteCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors: ...
    @overload
    def delete_campaign(self, body: SPGlobalDeleteCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_campaign(
        self, body: SPGlobalDeleteCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = self._request("POST", "/adsApi/v1/delete/campaigns", json=self.dump_json(body))
        return self._response(SPGlobalCampaignMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    def query_campaign(
        self, body: SPGlobalQueryCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def query_campaign(
        self, body: SPGlobalQueryCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalCampaignSuccessResponse: ...
    @overload
    def query_campaign(self, body: SPGlobalQueryCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_campaign(
        self, body: SPGlobalQueryCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalCampaignSuccessResponse | dict[str, Any] | httpx.Response:
        """Query campaign"""

        resp = self._request("POST", "/adsApi/v1/query/campaigns", json=self.dump_json(body))
        return self._response(SPGlobalCampaignSuccessResponse, resp, mode=mode)

    @overload
    def update_campaign(
        self, body: SPGlobalUpdateCampaignRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def update_campaign(
        self, body: SPGlobalUpdateCampaignRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors: ...
    @overload
    def update_campaign(self, body: SPGlobalUpdateCampaignRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_campaign(
        self, body: SPGlobalUpdateCampaignRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalCampaignMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Update campaign"""

        resp = self._request("POST", "/adsApi/v1/update/campaigns", json=self.dump_json(body))
        return self._response(SPGlobalCampaignMultiStatusResponseWithPartialErrors, resp, mode=mode)
