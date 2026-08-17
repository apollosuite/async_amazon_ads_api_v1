"""BrandBenchmarks resource operations.

Generated from OpenAPI spec (tag: Brand Benchmarks).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.reporting.brand_benchmarks import (
    GetAdvertiserReportResponseContent,
    ListAdvertiserReportMetadataResponseContent,
)


class BrandBenchmarks(BaseResource):

    @overload
    async def get_advertiser_report(
        self, advertiser_id: str, index_date: str, report_type: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GetAdvertiserReportResponseContent: ...
    @overload
    async def get_advertiser_report(
        self, advertiser_id: str, index_date: str, report_type: str, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_advertiser_report(
        self, advertiser_id: str, index_date: str, report_type: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_advertiser_report(
        self,
        advertiser_id: str,
        index_date: str,
        report_type: str,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> GetAdvertiserReportResponseContent | dict[str, Any] | httpx.Response:
        """Gets the download link for an advertiser's metric report in the specified marketplace."""

        resp = await self._request(
            "GET",
            f"/insights/brandBenchmarks/advertisers/{advertiser_id}/reports/{report_type}/indexDates/{index_date}",
            headers={"Accept": "application/vnd.insightsAdvertiser.v1+json"},
        )
        return self._response(GetAdvertiserReportResponseContent, resp, mode=mode)

    @overload
    async def list_advertiser_report_metadata(
        self,
        advertiser_id: str,
        *,
        mode: Literal["pydantic"] = "pydantic",
        next_token: str | None = None,
        max_results: float | None = None,
        latest_only: bool | None = None,
    ) -> ListAdvertiserReportMetadataResponseContent: ...
    @overload
    async def list_advertiser_report_metadata(
        self,
        advertiser_id: str,
        *,
        mode: Literal["dict"],
        next_token: str | None = None,
        max_results: float | None = None,
        latest_only: bool | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def list_advertiser_report_metadata(
        self,
        advertiser_id: str,
        *,
        mode: Literal["raw"],
        next_token: str | None = None,
        max_results: float | None = None,
        latest_only: bool | None = None,
    ) -> httpx.Response: ...
    async def list_advertiser_report_metadata(
        self,
        advertiser_id: str,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
        max_results: float | None = None,
        latest_only: bool | None = None,
    ) -> ListAdvertiserReportMetadataResponseContent | dict[str, Any] | httpx.Response:
        """Gets all of the report metadata the specified advertiser at the specified marketplace."""

        params = {
            "nextToken": next_token,
            "maxResults": max_results,
            "latestOnly": latest_only,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request(
            "GET",
            f"/insights/brandBenchmarks/advertisers/{advertiser_id}/allReportMetadata",
            params=params,
            headers={"Accept": "application/vnd.insightsAdvertiser.v1+json"},
        )
        return self._response(ListAdvertiserReportMetadataResponseContent, resp, mode=mode)
