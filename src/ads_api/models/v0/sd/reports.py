"""Auto-generated models for Reports from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class ReportResponseRecordType(StrEnum):
    """
    The type of report requested.
    """

    CAMPAIGN = "CAMPAIGN"
    AD_GROUP = "AD_GROUP"
    PRODUCT_AD = "PRODUCT_AD"


class ReportResponseStatus(StrEnum):
    """
    The build status of the report.
    """

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class Segment(StrEnum):
    """
    Optional. A dimension used to further segment certain types of reports.

    Note: matchedTarget reports only return targets that have generated at least one click.
    | Dimension | Report types | Tactics | Metrics | Description |
    |---------|------------------|-------------|-------------|------------|
    | matchedTarget | campaigns, adGroups, targets | T00020, T00030 | Existing metrics for each report type are accepted. |  Segments a report based on the ASIN of the product page where the ad appeared.|
    """

    matchedTarget = "matchedTarget"


class TacticReport(StrEnum):
    """
    The advertising tactic associated with the campaign. The following table lists available tactic names:
    |Tactic Name|Type|Description|
    |-----------|-----|-----------|
    |T00020     |Contextual targeting | Choose individual products to show your ads in placements related to those products.<br> Choose individual categories to show your ads in placements related to those categories on and off Amazon.|
    |T00030     |Audiences or Contextual Targeting | Select individual products, categories, refined categories, or audiences to show your ads.|
    """

    T00020 = "T00020"
    T00030 = "T00030"


class ReportRequest(StrictModel):
    reportDate: str | None = Field(
        default=None,
        description="Date in YYYYMMDD format. The report contains only metrics generated on the specified date. Note that the time zone used for date calculation is the one associated with the profile used to make the request.",
    )
    tactic: Annotated[TacticReport | str, lenient_enum(TacticReport)] | None = Field(default=None)
    segment: Annotated[Segment | str, lenient_enum(Segment)] | None = Field(default=None)
    metrics: str | None = Field(
        default=None,
        description="""
A comma-separated list of the metrics to be included in the report.

Each report type supports different metrics. **To understand supported metrics for each report type, see [Report types](/API/docs/en-us/guides/reporting/v2/report-types).**

**Note**: Campaigns with vCPM costType should use view+click based metrics (viewAttributedConversions14d, viewAttributedDetailPageView14d, viewAttributedSales14d, viewAttributedUnitsOrdered14d, viewImpressions).

**Note**: Detail page view metrics (attributedDetailPageView14d, viewAttributedDetailPageView14d) have an SLA of 3 days.

**Tip**: Use new-to-brand (NTB) metrics to calculate how efficient your campaigns are at driving new shoppers:

  1. Percentage of NTB orders = attributedOrdersNewToBrand14d / attributedConversions14d
  2. Percentage NTB sales = attributedSalesNewToBrand14d / attributedSales14d
  3. Percentage NTB units = attributedUnitsOrderedNewToBrand14d / attributedUnitsOrdered14d
  4. NTB order rate = attributedOrdersNewToBrand14 / impressions
""",
    )


class ReportResponse(LenientModel):
    reportId: str | None = Field(default=None, description="The identifier of the report.")
    recordType: Annotated[ReportResponseRecordType | str, lenient_enum(ReportResponseRecordType)] | None = Field(
        default=None, description="The type of report requested."
    )
    status: Annotated[ReportResponseStatus | str, lenient_enum(ReportResponseStatus)] | None = Field(
        default=None, description="The build status of the report."
    )
    statusDetails: str | None = Field(default=None, description="A human-readable description of the current status.")
    location: str | None = Field(default=None, description="The URI location of the report.")
    fileSize: int | None = Field(default=None, description="The size of the report file, in bytes.")
    expiration: int | None = Field(
        default=None, description="Epoch date of the expiration of the URI in the `location` property."
    )


__all__ = [
    "ReportRequest",
    "ReportResponse",
    "ReportResponseRecordType",
    "ReportResponseStatus",
    "Segment",
    "TacticReport",
]
