"""BrandMetrics resource operations.

Generated from OpenAPI spec (tag: Report).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.reporting.brand_metrics import (
    BrandMetricsGenerateReportRequest,
    BrandMetricsGenerateReportResponse,
    BrandMetricsGetReportByIdResponse,
)


class BrandMetrics(BaseResource):

    @overload
    async def generate_brand_metrics_report(
        self, body: BrandMetricsGenerateReportRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def generate_brand_metrics_report(
        self, body: BrandMetricsGenerateReportRequest | None = None, *, mode: Literal["pydantic"]
    ) -> BrandMetricsGenerateReportResponse: ...
    @overload
    async def generate_brand_metrics_report(
        self, body: BrandMetricsGenerateReportRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def generate_brand_metrics_report(
        self,
        body: BrandMetricsGenerateReportRequest | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> BrandMetricsGenerateReportResponse | dict[str, Any] | httpx.Response:
        """Generates the Brand Metrics report in CSV or JSON format. Customize the report by passing a specific categoryTreeName, categoryPath, brandName, reportStartDate, reportEndDate, lookbackPeriod, format or a list of metrics from the available metrics in the metrics field. If an empty request body is passed, report for the latest available report date in JSON format will get generated with all the available brands and metrics for an advertiser. The report may or may not contain the Brand Metrics data for one or more brands depending on data availability."""

        resp = await self._request(
            "POST",
            "/insights/brandMetrics/report",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.insightsbrandmetrics.v1+json",
                "Accept": "application/vnd.insightsbrandmetrics.v1+json",
            },
        )
        return self._response(BrandMetricsGenerateReportResponse, resp, mode=mode)

    @overload
    async def get_brand_metrics_report(
        self,
        report_id: str,
        *,
        accept: Literal[
            "application/vnd.insightsbrandmetrics.v1+json", "application/vnd.insightsbrandmetrics.v1.1+json"
        ] = "application/vnd.insightsbrandmetrics.v1+json",
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def get_brand_metrics_report(
        self,
        report_id: str,
        *,
        accept: Literal[
            "application/vnd.insightsbrandmetrics.v1+json", "application/vnd.insightsbrandmetrics.v1.1+json"
        ] = "application/vnd.insightsbrandmetrics.v1+json",
        mode: Literal["pydantic"],
    ) -> BrandMetricsGetReportByIdResponse: ...
    @overload
    async def get_brand_metrics_report(
        self,
        report_id: str,
        *,
        accept: Literal[
            "application/vnd.insightsbrandmetrics.v1+json", "application/vnd.insightsbrandmetrics.v1.1+json"
        ] = "application/vnd.insightsbrandmetrics.v1+json",
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def get_brand_metrics_report(
        self,
        report_id: str,
        *,
        accept: Literal[
            "application/vnd.insightsbrandmetrics.v1+json", "application/vnd.insightsbrandmetrics.v1.1+json"
        ] = "application/vnd.insightsbrandmetrics.v1+json",
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> BrandMetricsGetReportByIdResponse | dict[str, Any] | httpx.Response:
        """Fetch the location and status of the report for the brands for which the metrics are available. The URL to the report is only available when the status of the report is SUCCESSFUL."""

        headers = {}
        headers["Accept"] = accept
        resp = await self._request("GET", f"/insights/brandMetrics/report/{report_id}", headers=headers)
        return self._response(BrandMetricsGetReportByIdResponse, resp, mode=mode)
