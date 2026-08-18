"""Auto-generated models for Report from Amazon Ads API v0."""

from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Annotated, Any

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class BrandMetricsGenerateReportRequestFormat(StrEnum):
    """
    Format of the report.
    """

    CSV = "CSV"
    JSON = "JSON"


class BrandMetricsGenerateReportRequestLookBackPeriod(StrEnum):
    """
    Currently supported values: "1w" (one week), "1m" (one month) and  "1cm" (one calendar month). This defines the period of time used to determine the number of shoppers in the metrics computation.
    """

    _1CM = "1CM"
    _1M = "1M"
    _1W = "1W"


class BrandMetricsGenerateReportRequestV11Format(StrEnum):
    """
    Format of the report.
    """

    CSV = "CSV"
    JSON = "JSON"


class BrandMetricsGenerateReportRequestV11LookBackPeriod(StrEnum):
    """
    Currently supported values: "1w" (one week), "1m" (one month) and  "1cm" (one calendar month). This defines the period of time used to determine the number of shoppers in the metrics computation.
    """

    _1cm = "1cm"
    _1m = "1m"
    _1w = "1w"


class BrandMetricsGenerateReportResponseFormat(StrEnum):
    """
    Format of the report.
    """

    CSV = "CSV"
    JSON = "JSON"


class BrandMetricsGenerateReportResponseStatus(StrEnum):
    """
    The build status of the report.
    """

    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"


class BrandMetricsGenerateReportResponseV11Format(StrEnum):
    """
    Format of the report.
    """

    CSV = "CSV"
    JSON = "JSON"


class BrandMetricsGenerateReportResponseV11Status(StrEnum):
    """
    The build status of the report.
    """

    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"


class BrandMetricsGetReportByIdResponseFormat(StrEnum):
    """
    Format of the report.
    """

    CSV = "CSV"
    JSON = "JSON"


class BrandMetricsGetReportByIdResponseStatus(StrEnum):
    """
    The build status of the report.
    """

    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"


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
    format: (
        Annotated[BrandMetricsGenerateReportRequestFormat | str, lenient_enum(BrandMetricsGenerateReportRequestFormat)]
        | None
    ) = Field(default="JSON", description="Format of the report.")
    lookBackPeriod: (
        Annotated[
            BrandMetricsGenerateReportRequestLookBackPeriod | str,
            lenient_enum(BrandMetricsGenerateReportRequestLookBackPeriod),
        ]
        | None
    ) = Field(
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
    format: (
        Annotated[
            BrandMetricsGenerateReportRequestV11Format | str, lenient_enum(BrandMetricsGenerateReportRequestV11Format)
        ]
        | None
    ) = Field(default="JSON", description="Format of the report.")
    lookBackPeriod: (
        Annotated[
            BrandMetricsGenerateReportRequestV11LookBackPeriod | str,
            lenient_enum(BrandMetricsGenerateReportRequestV11LookBackPeriod),
        ]
        | None
    ) = Field(
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
    format: Annotated[
        BrandMetricsGenerateReportResponseFormat | str, lenient_enum(BrandMetricsGenerateReportResponseFormat)
    ] = Field(description="Format of the report.")
    location: str | None = Field(default=None, description="The URI address of the report.")
    reportId: str = Field(description="The identifier of the report.")
    status: Annotated[
        BrandMetricsGenerateReportResponseStatus | str, lenient_enum(BrandMetricsGenerateReportResponseStatus)
    ] = Field(description="The build status of the report.")
    statusDetails: str = Field(description="A human-readable description of the current status.")


class BrandMetricsGenerateReportResponseV11(LenientModel):
    """Response object containing Brand Metrics Report metadata."""

    expiration: int = Field(
        description="The expiration time of the URI in the location property in milliseconds. The expiration time is the interval between the time the response was generated and the time the URI expires."
    )
    format: Annotated[
        BrandMetricsGenerateReportResponseV11Format | str, lenient_enum(BrandMetricsGenerateReportResponseV11Format)
    ] = Field(description="Format of the report.")
    location: str | None = Field(default=None, description="The URI address of the report.")
    reportId: str = Field(description="The identifier of the report.")
    status: Annotated[
        BrandMetricsGenerateReportResponseV11Status | str, lenient_enum(BrandMetricsGenerateReportResponseV11Status)
    ] = Field(description="The build status of the report.")
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
    format: Annotated[
        BrandMetricsGetReportByIdResponseFormat | str, lenient_enum(BrandMetricsGetReportByIdResponseFormat)
    ] = Field(description="Format of the report.")
    location: str | None = Field(
        default=None,
        description="The URI address of the report. Only available if the report is generated successfully. The location is empty if the Brand Metrics are not available or if the report is not generated successfully.",
    )
    reportId: str = Field(description="The identifier of the report.")
    status: Annotated[
        BrandMetricsGetReportByIdResponseStatus | str, lenient_enum(BrandMetricsGetReportByIdResponseStatus)
    ] = Field(description="The build status of the report.")
    statusDetails: str = Field(description="A human-readable description of the current status.")


__all__ = [
    "BrandMetricsGenerateReportRequest",
    "BrandMetricsGenerateReportRequestFormat",
    "BrandMetricsGenerateReportRequestLookBackPeriod",
    "BrandMetricsGenerateReportRequestV11",
    "BrandMetricsGenerateReportRequestV11Format",
    "BrandMetricsGenerateReportRequestV11LookBackPeriod",
    "BrandMetricsGenerateReportResponse",
    "BrandMetricsGenerateReportResponseFormat",
    "BrandMetricsGenerateReportResponseStatus",
    "BrandMetricsGenerateReportResponseV11",
    "BrandMetricsGenerateReportResponseV11Format",
    "BrandMetricsGenerateReportResponseV11Status",
    "BrandMetricsGetReportByIdResponse",
    "BrandMetricsGetReportByIdResponseFormat",
    "BrandMetricsGetReportByIdResponseStatus",
]
