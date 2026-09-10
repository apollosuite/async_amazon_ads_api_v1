"""Reports resource operations.

Generated from OpenAPI spec (tag: Asynchronous Reports).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.reporting.reports import (
    AsyncReport,
    CreateAsyncReportRequest,
    DeleteAsyncReportResponse,
)


class Reports(BaseResource):

    @overload
    def create_async_report(
        self, body: CreateAsyncReportRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_async_report(
        self, body: CreateAsyncReportRequest | None = None, *, mode: Literal["pydantic"]
    ) -> AsyncReport: ...
    @overload
    def create_async_report(
        self, body: CreateAsyncReportRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_async_report(
        self, body: CreateAsyncReportRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> AsyncReport | dict[str, Any] | httpx.Response:
        """Creates a report request. Use this operation to request the creation of a new report for Amazon Advertising Products. Use `adProduct` to specify the Advertising Product of the report."""

        resp = self._request(
            "POST",
            "/reporting/reports",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.createasyncreportrequest.v3+json",
                "Accept": "application/vnd.createasyncreportrequest.v3+json",
            },
        )
        return self._response(AsyncReport, resp, mode=mode)

    @overload
    def delete_async_report(self, report_id: str, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_async_report(self, report_id: str, *, mode: Literal["pydantic"]) -> DeleteAsyncReportResponse: ...
    @overload
    def delete_async_report(self, report_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_async_report(
        self, report_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DeleteAsyncReportResponse | dict[str, Any] | httpx.Response:
        """Deletes a report by id. Use this operation to cancel a report in a `PENDING` status."""

        resp = self._request(
            "DELETE",
            f"/reporting/reports/{report_id}",
            headers={"Accept": "application/vnd.deleteasyncreportresponse.v3+json"},
        )
        return self._response(DeleteAsyncReportResponse, resp, mode=mode)

    @overload
    def get_async_report(self, report_id: str, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def get_async_report(self, report_id: str, *, mode: Literal["pydantic"]) -> AsyncReport: ...
    @overload
    def get_async_report(self, report_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    def get_async_report(
        self, report_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> AsyncReport | dict[str, Any] | httpx.Response:
        """Gets a generation status of a report by id. Uses the `reportId` value from"""

        resp = self._request(
            "GET",
            f"/reporting/reports/{report_id}",
            headers={"Accept": "application/vnd.getasyncreportresponse.v3+json"},
        )
        return self._response(AsyncReport, resp, mode=mode)
