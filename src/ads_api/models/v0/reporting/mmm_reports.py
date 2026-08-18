"""Auto-generated models for Reports from Amazon Ads API v0."""

from __future__ import annotations

from datetime import date, datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel
from ads_api.models._core.lenient_enum import lenient_enum


class MmmReportConfigurationGeoDimension(StrEnum):
    """
    Geographic granularity of the report.
    |Value|Description|
    |---|---|
    |COUNTRY|Aggregate metrics by country.|
    |POSTAL_CODE|Aggregate metrics by postal code, e.g. ZIP Code. Valid only in select countries.|
    |DMA|Aggregate metrics by DMA® (Designated Market Area) region. Valid only in the US.|
    """

    COUNTRY = "COUNTRY"
    DMA = "DMA"
    POSTAL_CODE = "POSTAL_CODE"


class MmmReportConfigurationMetricsType(StrEnum):
    """
    The type of metrics to include in the report.
    |Value|Description|
    |---|---|
    |MEDIA_ONLY|Core advertising metrics only.|
    |MEDIA_AND_SALES|Advertising and retail metrics.|
    """

    MEDIA_AND_SALES = "MEDIA_AND_SALES"
    MEDIA_ONLY = "MEDIA_ONLY"


class MmmReportConfigurationTimeUnit(StrEnum):
    """
    Time granularity of the report.
    |Value|Description|
    |---|---|
    |DAILY|Aggregate metrics with daily granularity.|
    |WEEKLY|Aggregate metrics with weekly granularity.|
    """

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class MmmReportStatus(StrEnum):
    """
    The report generation status.
    |Value|Description|
    |---|---|
    |PENDING|Report is created and awaiting processing.|
    |PROCESSING|Report is processing.|
    |SUCCEEDED|Report is completed. Check `urls` for the output files.|
    |FAILED|Report processing failed. Check the `failureCode` and `failureMessage` for details.|
    |CANCELED|Report is canceled. Contact <mmm-support@amazon.com> if this is unexpected.|
    """

    CANCELED = "CANCELED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SUCCEEDED = "SUCCEEDED"


class MmmReport(LenientModel):
    configuration: MmmReportConfiguration | None = Field(default=None)
    createdAt: datetime | None = Field(default=None, description="The date and time when the report was created.")
    description: str | None = Field(default=None, description="A description of the report.")
    dueDate: date | None = Field(default=None, description="The due date of the report.")
    endDate: date | None = Field(default=None, description="Inclusive end of the reporting period.")
    failureCode: str | None = Field(
        default=None, description="An error code indicating why the report failed. Present when the status is `FAILED`."
    )
    failureMessage: str | None = Field(
        default=None,
        description="A human-readable message providing more information about the failure. Present when the status is `FAILED`.",
    )
    reportId: str | None = Field(default=None, description="The unique identifier of the report.")
    reportName: str | None = Field(default=None, description="The display name of the report.")
    startDate: date | None = Field(default=None, description="Inclusive start of the reporting period.")
    status: Annotated[MmmReportStatus | str, lenient_enum(MmmReportStatus)] | None = Field(
        default=None,
        description="""
The report generation status.
|Value|Description|
|---|---|
|PENDING|Report is created and awaiting processing.|
|PROCESSING|Report is processing.|
|SUCCEEDED|Report is completed. Check `urls` for the output files.|
|FAILED|Report processing failed. Check the `failureCode` and `failureMessage` for details.|
|CANCELED|Report is canceled. Contact <mmm-support@amazon.com> if this is unexpected.|
""",
    )
    urls: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=20,
        description="The URLs for downloading output files. Present when the status is `SUCCEEDED`.",
    )
    urlsExpireAt: datetime | None = Field(
        default=None, description="The expiration date of the download URLs. Present when the status is `SUCCEEDED`."
    )


class MmmReportConfiguration(LenientModel):
    brandGroupId: str = Field(description="Identifies the brand group being reported on.")
    geoDimension: Annotated[
        MmmReportConfigurationGeoDimension | str, lenient_enum(MmmReportConfigurationGeoDimension)
    ] = Field(
        description="""
Geographic granularity of the report.
|Value|Description|
|---|---|
|COUNTRY|Aggregate metrics by country.|
|POSTAL_CODE|Aggregate metrics by postal code, e.g. ZIP Code. Valid only in select countries.|
|DMA|Aggregate metrics by DMA® (Designated Market Area) region. Valid only in the US.|
"""
    )
    metricsType: Annotated[MmmReportConfigurationMetricsType | str, lenient_enum(MmmReportConfigurationMetricsType)] = (
        Field(description="""
The type of metrics to include in the report.
|Value|Description|
|---|---|
|MEDIA_ONLY|Core advertising metrics only.|
|MEDIA_AND_SALES|Advertising and retail metrics.|
""")
    )
    timeUnit: Annotated[MmmReportConfigurationTimeUnit | str, lenient_enum(MmmReportConfigurationTimeUnit)] = Field(
        description="""
Time granularity of the report.
|Value|Description|
|---|---|
|DAILY|Aggregate metrics with daily granularity.|
|WEEKLY|Aggregate metrics with weekly granularity.|
"""
    )


__all__ = [
    "MmmReport",
    "MmmReportConfiguration",
    "MmmReportConfigurationGeoDimension",
    "MmmReportConfigurationMetricsType",
    "MmmReportConfigurationTimeUnit",
    "MmmReportStatus",
]
