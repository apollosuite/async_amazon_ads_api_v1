"""Auto-generated models for Reports from Amazon Ads API v0."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel


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
    status: str | None = Field(default=None, description="The report generation status.")
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
    geoDimension: str = Field(description="Geographic granularity of the report.")
    metricsType: str = Field(description="The type of metrics to include in the report.")
    timeUnit: str = Field(description="Time granularity of the report.")


__all__ = ["MmmReport", "MmmReportConfiguration"]
