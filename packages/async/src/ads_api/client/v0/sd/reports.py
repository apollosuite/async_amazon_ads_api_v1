"""Reports resource operations.

Generated from OpenAPI spec (tag: Reports).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.reports import (
    ReportRequest,
    ReportResponse,
)


class Reports(BaseResource):

    @overload
    async def download_report(self, report_id: str, *, mode: Literal["dict"] = "dict") -> Any: ...
    @overload
    async def download_report(self, report_id: str, *, mode: Literal["pydantic"]) -> Any: ...
    @overload
    async def download_report(self, report_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def download_report(self, report_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict") -> Any:
        """Gets a `307 Temporary Redirect` response that includes a `location` header with the value set to an AWS S3 path where the report is located. The path expires after 30 seconds. If the path expires before the report is downloaded, a new report request must be created."""

        resp = await self._request("GET", f"/v2/reports/{report_id}/download")
        if mode == "raw":
            return resp
        return resp.json()

    @overload
    async def get_report_status(self, report_id: str, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def get_report_status(self, report_id: str, *, mode: Literal["pydantic"]) -> ReportResponse: ...
    @overload
    async def get_report_status(self, report_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_report_status(
        self, report_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ReportResponse | dict[str, Any] | httpx.Response:
        """Uses the `reportId` value from the response of a report previously requested via `POST` method of the `/sd/{recordType}/report` operation."""

        resp = await self._request("GET", f"/v2/reports/{report_id}")
        return self._response(ReportResponse, resp, mode=mode)

    @overload
    async def request_report(
        self,
        record_type: Literal["campaigns", "adGroups", "productAds", "targets", "asins"] | str,
        body: ReportRequest | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def request_report(
        self,
        record_type: Literal["campaigns", "adGroups", "productAds", "targets", "asins"] | str,
        body: ReportRequest | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> ReportResponse: ...
    @overload
    async def request_report(
        self,
        record_type: Literal["campaigns", "adGroups", "productAds", "targets", "asins"] | str,
        body: ReportRequest | None = None,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def request_report(
        self,
        record_type: Literal["campaigns", "adGroups", "productAds", "targets", "asins"] | str,
        body: ReportRequest | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> ReportResponse | dict[str, Any] | httpx.Response:
        """**To understand the call flow for asynchronous reports, see [Getting started with sponsored ads reports](/API/docs/en-us/guides/reporting/v2/sponsored-ads-reports).**"""

        resp = await self._request("POST", f"/sd/{record_type}/report", json=self.dump_json(body))
        return self._response(ReportResponse, resp, mode=mode)
