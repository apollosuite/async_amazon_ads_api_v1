"""Auto-generated models for Reports from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type Segment = Literal["matchedTarget"]
"""
Optional. A dimension used to further segment certain types of reports.

Note: matchedTarget reports only return targets that have generated at least one click.
| Dimension | Report types | Tactics | Metrics | Description |
|---------|------------------|-------------|-------------|------------|
| matchedTarget | campaigns, adGroups, targets | T00020, T00030 | Existing metrics for each report type are accepted. |  Segments a report based on the ASIN of the product page where the ad appeared.|
"""


type TacticReport = Literal["T00020", "T00030"]
"""
The advertising tactic associated with the campaign. The following table lists available tactic names:
|Tactic Name|Type|Description|
|-----------|-----|-----------|
|T00020     |Contextual targeting | Choose individual products to show your ads in placements related to those products.<br> Choose individual categories to show your ads in placements related to those categories on and off Amazon.|
|T00030     |Audiences or Contextual Targeting | Select individual products, categories, refined categories, or audiences to show your ads.|
"""


class ReportRequest(StrictModel):
    reportDate: str | None = Field(
        default=None,
        description="Date in YYYYMMDD format. The report contains only metrics generated on the specified date. Note that the time zone used for date calculation is the one associated with the profile used to make the request.",
    )
    tactic: TacticReport | None = Field(default=None)
    segment: Segment | None = Field(default=None)
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
    recordType: Literal["CAMPAIGN", "AD_GROUP", "PRODUCT_AD"] | str | None = Field(
        default=None, description="The type of report requested."
    )
    status: Literal["IN_PROGRESS", "SUCCESS", "FAILURE"] | str | None = Field(
        default=None, description="The build status of the report."
    )
    statusDetails: str | None = Field(default=None, description="A human-readable description of the current status.")
    location: str | None = Field(default=None, description="The URI location of the report.")
    fileSize: int | None = Field(default=None, description="The size of the report file, in bytes.")
    expiration: int | None = Field(
        default=None, description="Epoch date of the expiration of the URI in the `location` property."
    )


__all__ = ["ReportRequest", "ReportResponse", "Segment", "TacticReport"]
