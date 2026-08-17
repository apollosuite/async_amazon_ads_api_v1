"""MmmReports resource operations.

Generated from OpenAPI spec (tag: Reports).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.reporting.mmm_reports import (
    MmmReport,
)


class MmmReports(BaseResource):

    @overload
    async def create_mmm_report(self, *, mode: Literal["pydantic"] = "pydantic") -> MmmReport: ...
    @overload
    async def create_mmm_report(self, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_mmm_report(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_mmm_report(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> MmmReport | dict[str, Any] | httpx.Response:
        """Creates a report. Each report requires the `brandGroupId` of a predefined brand group listed in `POST /mmm/v1/brandGroups/list`. The response will include a `reportId` that can be used to poll the status and results."""

        resp = await self._request("POST", "/mmm/v1/reports")
        return self._response(MmmReport, resp, mode=mode)

    @overload
    async def delete_mmm_report(self, *, mode: Literal["pydantic"] = "pydantic") -> Any: ...
    @overload
    async def delete_mmm_report(self, *, mode: Literal["dict"]) -> Any: ...
    @overload
    async def delete_mmm_report(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_mmm_report(self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic") -> Any:
        """Deletes a report by ID. Use this operation to cancel or clean up a report."""

        resp = await self._request("DELETE", "/mmm/v1/reports/{reportId}")
        if mode == "raw":
            return resp
        return resp.json()

    @overload
    async def get_mmm_report(self, *, mode: Literal["pydantic"] = "pydantic") -> MmmReport: ...
    @overload
    async def get_mmm_report(self, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_mmm_report(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_mmm_report(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> MmmReport | dict[str, Any] | httpx.Response:
        """Gets the generation status of a report by ID. The `reportId` is found in the response to creating a report using `POST /mmm/v1/reports`. When the `status` is `SUCCESSFUL` the output files will be available for download at `urls`. A report may take up to 24 hours to be processed. Repeated calls to check report status may generate a 429 response, indicating that your requests have been throttled. To retrieve reports programmatically, your application logic should institute a delay between requests."""

        resp = await self._request("GET", "/mmm/v1/reports/{reportId}")
        return self._response(MmmReport, resp, mode=mode)

    @overload
    async def list_mmm_reports(self, *, mode: Literal["pydantic"] = "pydantic") -> Any: ...
    @overload
    async def list_mmm_reports(self, *, mode: Literal["dict"]) -> Any: ...
    @overload
    async def list_mmm_reports(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def list_mmm_reports(self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic") -> Any:
        """Returns a list of reports and their generation status. When the `status` is `SUCCESSFUL` the output files will be available for download at `urls`. Each report may take up to 24 hours to be processed. Repeated calls to check report status may generate a 429 response, indicating that your requests have been throttled. To retrieve reports programmatically, your application logic should institute a delay between requests."""

        resp = await self._request("POST", "/mmm/v1/reports/list")
        if mode == "raw":
            return resp
        return resp.json()
