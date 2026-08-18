"""Auto-generated models for Report from Amazon Ads API v0."""

from __future__ import annotations

from datetime import date
from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class BrandMetricsGenerateReportRequest(StrictModel):
    """Request object to generate the Brand Metrics Report."""

    brandName: str | None = Field(
        default=None,
        description="Optional. Brand Name. If no Brand Name is passed, then all data available for all brands belonging to the entity are retrieved.",
    )
    categoryPath: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="Optional. The hierarchical path that leads to a node starting with the root node. If no Category Node Name is passed, then all data available for all brands belonging to the entity are retrieved.",
    )
    categoryTreeName: str | None = Field(
        default=None, description="Optional. The node at the top of a browse tree. It is the start node of a tree."
    )
    format: Literal["CSV", "JSON"] | None = Field(default="JSON", description="Format of the report.")
    lookBackPeriod: Literal["1CM", "1M", "1W"] | None = Field(
        default="1W",
        description='Currently supported values: "1w" (one week), "1m" (one month) and  "1cm" (one calendar month). This defines the period of time used to determine the number of shoppers in the metrics computation.',
    )
    metrics: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="Optional. Specify an array of string of metrics field names to include in the report. If no metric field names are specified, all metrics are returned.",
    )
    reportEndDate: date | None = Field(
        default=None,
        description="Optional. Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The maximum allowed date range for report generation is 3 months. The date will be in the Coordinated Universal Time (UTC) timezone in YYYY-MM-DD format. If both reportStartDate and reportEndDate are passed and the range is greater than 3 months, the reportStartDate will be adjusted to a date 3 months from the reportEndDate. If no date is passed in reportEndDate, all available metrics till metricsComputationDate of 3 months after the reportStartDate will be provided. If no date is passed for either reportStartDate or reportEndDate, the metrics with the most recent metricsComputationDate will be returned.",
    )
    reportStartDate: date | None = Field(
        default=None,
        description="Optional. Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The maximum allowed date range for report generation is 3 months. The date will be in the Coordinated Universal Time (UTC) timezone in YYYY-MM-DD format. If both reportStartDate and reportEndDate are passed and the range is greater than 3 months, the reportStartDate will be adjusted to a date 3 months from the reportEndDate. If no date is passed in reportStartDate, all available metrics from metricsComputationDate of 3 months before the reportEndDate will be provided. If no date is passed for either reportStartDate or reportEndDate, the metrics with the most recent metricsComputationDate will be returned.",
    )


class BrandMetricsGenerateReportRequestV11(StrictModel):
    """Request object to generate the Brand Metrics Report."""

    brandName: str | None = Field(
        default=None,
        description="Optional. Brand Name. If no Brand Name is passed, then all data available for all brands belonging to the entity are retrieved.",
    )
    categoryPath: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="Optional. The hierarchical path that leads to a node starting with the root node. If no Category Node Name is passed, then all data available for all brands belonging to the entity are retrieved.",
    )
    categoryTreeName: str | None = Field(
        default=None, description="Optional. The node at the top of a browse tree. It is the start node of a tree."
    )
    format: Literal["CSV", "JSON"] | None = Field(default="JSON", description="Format of the report.")
    lookBackPeriod: Literal["1cm", "1m", "1w"] | None = Field(
        default="1w",
        description='Currently supported values: "1w" (one week), "1m" (one month) and  "1cm" (one calendar month). This defines the period of time used to determine the number of shoppers in the metrics computation.',
    )
    metrics: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=500,
        description="Optional. Specify an array of string of metrics field names to include in the report. If no metric field names are specified, all metrics are returned.",
    )
    reportEndDate: date | None = Field(
        default=None,
        description="Optional. Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The maximum allowed date range for report generation is 3 months. The date will be in the Coordinated Universal Time (UTC) timezone in YYYY-MM-DD format. If both reportStartDate and reportEndDate are passed and the range is greater than 3 months, the reportStartDate will be adjusted to a date 3 months from the reportEndDate. If no date is passed in reportEndDate, all available metrics till metricsComputationDate of 3 months after the reportStartDate will be provided. If no date is passed for either reportStartDate or reportEndDate, the metrics with the most recent metricsComputationDate will be returned.",
    )
    reportStartDate: date | None = Field(
        default=None,
        description="Optional. Retrieves metrics with metricsComputationDate between reportStartDate and reportEndDate (inclusive). The maximum allowed date range for report generation is 3 months. The date will be in the Coordinated Universal Time (UTC) timezone in YYYY-MM-DD format. If both reportStartDate and reportEndDate are passed and the range is greater than 3 months, the reportStartDate will be adjusted to a date 3 months from the reportEndDate. If no date is passed in reportStartDate, all available metrics from metricsComputationDate of 3 months before the reportEndDate will be provided. If no date is passed for either reportStartDate or reportEndDate, the metrics with the most recent metricsComputationDate will be returned.",
    )


class BrandMetricsGenerateReportResponse(LenientModel):
    """Response object containing Brand Metrics Report metadata."""

    expiration: int = Field(
        description="The expiration time of the URI in the location property in milliseconds. The expiration time is the interval between the time the response was generated and the time the URI expires."
    )
    format: Literal["CSV", "JSON"] | str = Field(description="Format of the report.")
    location: str | None = Field(default=None, description="The URI address of the report.")
    reportId: str = Field(description="The identifier of the report.")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCESSFUL"] | str = Field(description="The build status of the report.")
    statusDetails: str = Field(description="A human-readable description of the current status.")


class BrandMetricsGenerateReportResponseV11(LenientModel):
    """Response object containing Brand Metrics Report metadata."""

    expiration: int = Field(
        description="The expiration time of the URI in the location property in milliseconds. The expiration time is the interval between the time the response was generated and the time the URI expires."
    )
    format: Literal["CSV", "JSON"] | str = Field(description="Format of the report.")
    location: str | None = Field(default=None, description="The URI address of the report.")
    reportId: str = Field(description="The identifier of the report.")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCESSFUL"] | str = Field(description="The build status of the report.")
    statusDetails: str = Field(description="A human-readable description of the current status.")


class BrandMetricsGetReportByIdResponse(LenientModel):
    """Response object containing Brand Metrics Report status metadata."""

    brandsInfo: list[dict[str, Any]] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="List of first 200 brands for which the Brand Metrics report is generated. The report may contain more than 200 brands. This list is only populated with brands if the Brand Metrics are available for the brands that an advertiser has access to.",
    )
    expiration: int = Field(
        description="The expiration time of the URI in the location property in milliseconds. The expiration time is the interval between the time the response was generated and the time the URI expires."
    )
    format: Literal["CSV", "JSON"] | str = Field(description="Format of the report.")
    location: str | None = Field(
        default=None,
        description="The URI address of the report. Only available if the report is generated successfully. The location is empty if the Brand Metrics are not available or if the report is not generated successfully.",
    )
    reportId: str = Field(description="The identifier of the report.")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCESSFUL"] | str = Field(description="The build status of the report.")
    statusDetails: str = Field(description="A human-readable description of the current status.")


__all__ = [
    "BrandMetricsGenerateReportRequest",
    "BrandMetricsGenerateReportRequestV11",
    "BrandMetricsGenerateReportResponse",
    "BrandMetricsGenerateReportResponseV11",
    "BrandMetricsGetReportByIdResponse",
]
