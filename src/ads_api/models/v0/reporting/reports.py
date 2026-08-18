"""Auto-generated models for Asynchronous Reports from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class AsyncReportAdProduct(StrEnum):
    """
    The advertising product.
    """

    ALL = "ALL"
    DEMAND_SIDE_PLATFORM = "DEMAND_SIDE_PLATFORM"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_TELEVISION = "SPONSORED_TELEVISION"


class AsyncReportConfigurationFormat(StrEnum):
    """
    The report file format.
    """

    GZIP_JSON = "GZIP_JSON"


class AsyncReportConfigurationTimeUnit(StrEnum):
    """
    The aggregation level of report data. If the timeUnit is set to `SUMMARY`, the report data is aggregated at the time period specified. The availability
    of time unit breakdowns depends on the selection of reportTypeId.
    """

    DAILY = "DAILY"
    SUMMARY = "SUMMARY"


class AsyncReportStatus(StrEnum):
    """
    The build status of the report.
      - `PENDING` - Report is created and awaiting processing.
      - `PROCESSING` - Report is processing. Please wait.
      - `COMPLETED` - Report has completed.  Check the `url` for the output file.
      - `FAILED` - Report generation failed.  Check the `failureReason` for details.
    """

    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"


class AsyncReport(LenientModel):
    configuration: AsyncReportConfigurationOut
    createdAt: str = Field(description="The date at which the report was created in ISO 8601 date time format.")
    endDate: str = Field(description="The end date for the reporting period in YYYY-mm-dd format.")
    failureReason: str | None = Field(
        default=None, description="Present for failed reports only. The reason why a report failed to generate."
    )
    fileSize: float | None = Field(default=None, description="The size of the report file, in bytes.")
    generatedAt: str | None = Field(
        default=None, description="The date at which the report was generated in ISO 8601 date time format."
    )
    name: str | None = Field(default=None, description="Optional. The name of the generated report.")
    reportId: str = Field(description="The identifier of the requested report.")
    startDate: str = Field(description="The start date for the reporting period in YYYY-mm-dd format.")
    status: Annotated[AsyncReportStatus | str, lenient_enum(AsyncReportStatus)] = Field(description="""
The build status of the report.
  - `PENDING` - Report is created and awaiting processing.
  - `PROCESSING` - Report is processing. Please wait.
  - `COMPLETED` - Report has completed.  Check the `url` for the output file.
  - `FAILED` - Report generation failed.  Check the `failureReason` for details.
""")
    updatedAt: str = Field(description="The date at which the report was last updated in ISO 8601 date time format.")
    url: str | None = Field(default=None, description="URL of the generated report.")
    urlExpiresAt: str | None = Field(
        default=None,
        description="The date at which the download URL for the generated report expires. urlExpires at this time defaults to 3600 seconds but may vary in the future.",
    )


class AsyncReportConfiguration(StrictModel):
    adProduct: Annotated[AsyncReportAdProduct | str, lenient_enum(AsyncReportAdProduct)]
    columns: list[str] = Field(description="""
The list of columns to be used for report. The availability of
columns depends on the selection of reportTypeId. This list cannot be null or empty.
""")
    filters: list[AsyncReportFilter] | None = Field(
        default=None,
        description="The list of filters supported by a report type. The availability of filters fields depends on the selection of reportTypeId.",
    )
    format: Annotated[AsyncReportConfigurationFormat | str, lenient_enum(AsyncReportConfigurationFormat)] = Field(
        description="The report file format."
    )
    groupBy: list[str] = Field(description="""
This field determines the aggregation level of the report data and also makes additional fields available
for selection. This field cannot be null or empty.
""")
    reportTypeId: str = Field(description="The identifier of the Report Type to be generated.")
    timeUnit: Annotated[AsyncReportConfigurationTimeUnit | str, lenient_enum(AsyncReportConfigurationTimeUnit)] = Field(
        description="""
The aggregation level of report data. If the timeUnit is set to `SUMMARY`, the report data is aggregated at the time period specified. The availability
of time unit breakdowns depends on the selection of reportTypeId.
"""
    )


class AsyncReportConfigurationOut(LenientModel):
    adProduct: Annotated[AsyncReportAdProduct | str, lenient_enum(AsyncReportAdProduct)]
    columns: list[str] = Field(description="""
The list of columns to be used for report. The availability of
columns depends on the selection of reportTypeId. This list cannot be null or empty.
""")
    filters: list[AsyncReportFilterOut] | None = Field(
        default=None,
        description="The list of filters supported by a report type. The availability of filters fields depends on the selection of reportTypeId.",
    )
    format: Annotated[AsyncReportConfigurationFormat | str, lenient_enum(AsyncReportConfigurationFormat)] = Field(
        description="The report file format."
    )
    groupBy: list[str] = Field(description="""
This field determines the aggregation level of the report data and also makes additional fields available
for selection. This field cannot be null or empty.
""")
    reportTypeId: str = Field(description="The identifier of the Report Type to be generated.")
    timeUnit: Annotated[AsyncReportConfigurationTimeUnit | str, lenient_enum(AsyncReportConfigurationTimeUnit)] = Field(
        description="""
The aggregation level of report data. If the timeUnit is set to `SUMMARY`, the report data is aggregated at the time period specified. The availability
of time unit breakdowns depends on the selection of reportTypeId.
"""
    )


class AsyncReportFilter(StrictModel):
    field: str | None = Field(default=None, description="The field name of the filter")
    values: list[str] | None = Field(default=None, description="The values to be filtered by")


class AsyncReportFilterOut(LenientModel):
    field: str | None = Field(default=None, description="The field name of the filter")
    values: list[str] | None = Field(default=None, description="The values to be filtered by")


class CreateAsyncReportRequest(StrictModel):
    configuration: AsyncReportConfiguration
    endDate: str = Field(
        description="YYYY-MM-DD format. The maximum lookback window supported depends on the selection of reportTypeId. Most report types support `95 days` as lookback window."
    )
    name: str | None = Field(default=None, description="The name of the report.")
    startDate: str = Field(
        description="YYYY-MM-DD format. The maximum lookback window supported depends on the selection of reportTypeId. Most report types support `95 days` as lookback window."
    )


class DeleteAsyncReportResponse(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    detail: str | None = Field(default=None, description="A human-readable description of the response.")
    reportId: str | None = Field(default=None, description="The identifier of the report.")


__all__ = [
    "AsyncReport",
    "AsyncReportAdProduct",
    "AsyncReportConfiguration",
    "AsyncReportConfigurationFormat",
    "AsyncReportConfigurationOut",
    "AsyncReportConfigurationTimeUnit",
    "AsyncReportFilter",
    "AsyncReportFilterOut",
    "AsyncReportStatus",
    "CreateAsyncReportRequest",
    "DeleteAsyncReportResponse",
]
