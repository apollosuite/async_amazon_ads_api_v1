"""Reports resource operations.

Generated from OpenAPI spec (tag: Reports).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.reports.general import (
    CreateReportRequest,
    DeleteReportRequest,
    ReportMultiStatusResponse,
    RetrieveReportRequest,
)


class Reports(BaseResource):

    @overload
    def create_report(self, body: CreateReportRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_report(self, body: CreateReportRequest, *, mode: Literal["pydantic"]) -> ReportMultiStatusResponse: ...
    @overload
    def create_report(self, body: CreateReportRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_report(
        self, body: CreateReportRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ReportMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create a report"""

        resp = self._request("POST", "/adsApi/v1/create/reports", json=self.dump_json(body))
        return self._response(ReportMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_report(self, body: DeleteReportRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_report(self, body: DeleteReportRequest, *, mode: Literal["pydantic"]) -> ReportMultiStatusResponse: ...
    @overload
    def delete_report(self, body: DeleteReportRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_report(
        self, body: DeleteReportRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ReportMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete a report by ID"""

        resp = self._request("POST", "/adsApi/v1/delete/reports", json=self.dump_json(body))
        return self._response(ReportMultiStatusResponse, resp, mode=mode)

    @overload
    def retrieve_report(self, body: RetrieveReportRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def retrieve_report(
        self, body: RetrieveReportRequest, *, mode: Literal["pydantic"]
    ) -> ReportMultiStatusResponse: ...
    @overload
    def retrieve_report(self, body: RetrieveReportRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def retrieve_report(
        self, body: RetrieveReportRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ReportMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Retrieve a report by ID"""

        resp = self._request("POST", "/adsApi/v1/retrieve/reports", json=self.dump_json(body))
        return self._response(ReportMultiStatusResponse, resp, mode=mode)
