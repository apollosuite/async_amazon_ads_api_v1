"""Auto-generated models for Stores Analytics from Amazon Ads API v0."""

from __future__ import annotations

from datetime import date
from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type AsinEngagementDimension = Literal["ASIN"]
"""
User can use dimensions to aggregate the engagement metrics. Supported dimension types:
  * `ASIN` - Amazon Standard Identification Number.

  When *dimension* is omitted, user can retrieve select metrics aggregated at the store level. See *metrics* for details.
"""


type AsinEngagementMetric = Literal[
    "ADD_TO_CARTS",
    "AVERAGE_IN_STOCK_PRICE",
    "AVERAGE_SALE_PRICE",
    "CLICKS",
    "CLICK_RATE",
    "CONVERSION_RATE",
    "IN_STOCK_RATE",
    "IN_STOCK_VIEWS",
    "ORDERS",
    "RENDERS",
    "TOTAL_CLICKS",
    "TOTAL_VIEWS",
    "UNITS",
    "VIEWS",
]
"""
Store Metric Types: Metrics aggregated at the store level. To be used with *dimension* omitted, otherwise a 422 response is returned.
 * `TOTAL_VIEWS` - Total number of times customers viewed ASINs on the store’s pages. A view can happen once per store page visit.
 * `TOTAL_CLICKS` - Total count of times a customer clicked an ASIN related widget on the store’s pages.

 Asin Metric Types: Metrics aggregated at the ASIN level. To be used with a supported dimension type (see *dimension*), otherwise a 422 response is returned.
  * `RENDERS` - Number of times the asin rendered on a store page, this does not guarentee the customer saw the asin.
 * `VIEWS` - Number of times the a customer viewed an ASIN. Can happen once per page visit.
  * `ORDERS` - Estimated total orders placed by Store visitors on the day of the ASIN view.
 Orders can have one or more total units.
 * `UNITS` - Estimated units purchased by Store visitors during attributed orders for the ASIN.
 * `ADD_TO_CARTS` - Total number of times an asin was added to cart by a customer on a store page.
  * `IN_STOCK_VIEWS` - Total views of an asin on a store page while the asin was in stock. For asins with variations, the customer must have selected a variation which as in stock to be counted.
  * `AVERAGE_IN_STOCK_PRICE` - Average price in local currency the asin was viewed at by customers while it was in stock.
  *  `IN_STOCK_RATE` - Rate at which customers viewed an asin while it was in stock.
  *  `AVERAGE_SALE_PRICE` - Average price in local currency for which the asin sold for during the order.
  *  `CONVERSION_RATE` - Rate at which customers ordered a unit of the item over how many times customers clicked the item.
  *  `CLICKS` - Count of how many times a customer clicked an asin related widget on the store page.
  *  `CLICK_RATE` - Rate at which the asin was clicker per view. This ratio can be above one if the widget is interacted with on a widget with engaging features. (Product Showcase, Variation Selection in Product Grid, or Interactive Image)
"""


type InsightDimension = Literal[
    "DATE",
    "PAGE",
    "SOURCE",
    "STORE",
    "TAG",
]
"""
User can use dimensions to aggregate the insight metrics. Supported dimension types:
  * `DATE` - For aggregation by date.
  * `PAGE` - For aggregation by page.
  * `SOURCE` - For aggregation by source.
  * `TAG` - For aggregation by tag.
  * `STORE` - For aggregation by store. This dimension is only supported for "DWELL_TIME", "BOUNCE_RATE", "NEW_TO_STORE"

 Please check *metrics* for more detailsdetails.

<br><br> Not all InsightMetrics can be aggregated using above dimensions. Below is the supported metrics for each dimension,
<table>
  <tr>
    <th>InsightDimension</th>
    <th>Supported InsightMetrics</th>
  </tr>
  <tr>
    <th>DATE</th>
    <th>Either "VIEWS, ORDERS, UNITS, SALES, VISITS, DWELL_TIME, BOUNCE_RATE, NEW_TO_STORE" or "SCORE_LEVEL, RECOMMENDATIONS, CONTRIBUTORS, DWELL, PEER_DWELL, COMPLETED_RECOMMENDATIONS, ACTIONS_TAKEN_BY_PEERS" (Store Quality metrics)</th>
  </tr>
  <tr>
    <th>PAGE</th>
    <th>VIEWS, ORDERS, UNITS, SALES, VISITS,  DWELL_TIME, BOUNCE_RATE </th>
  </tr>
  <tr>
    <th>SOURCE</th>
    <th>VIEWS, ORDERS, UNITS, SALES, VISITS,  DWELL_TIME, BOUNCE_RATE </th>
  </tr>
  <tr>
    <th>TAG</th>
    <th>VIEWS, ORDERS, UNITS, SALES, VISITS,  DWELL_TIME, BOUNCE_RATE </th>
  </tr>
<tr>
    <th> STORE </th>
    <th> DWELL_TIME, BOUNCE_RATE, NEW_TO_STORE</th>
  </tr>
</table>
<br><br>
"""


type InsightMetric = Literal[
    "ACTIONS_TAKEN_BY_PEERS",
    "BOUNCE_RATE",
    "COMPLETED_RECOMMENDATIONS",
    "CONTRIBUTORS",
    "DWELL",
    "DWELL_TIME",
    "NEW_TO_STORE",
    "ORDERS",
    "PEER_DWELL",
    "PEER_SALES_LAST_60_DAYS",
    "RECOMMENDATIONS",
    "SALES",
    "SALES_LAST_60_DAYS",
    "SCORE_LEVEL",
    "UNITS",
    "VIDEO_10S_PLAYED",
    "VIDEO_25P_PLAYED",
    "VIDEO_50P_PLAYED",
    "VIDEO_75P_PLAYED",
    "VIDEO_COMPLETED",
    "VIDEO_STARTED",
    "VIEWS",
    "VISITORS",
    "VISITS",
]
"""
Insight Metric Type:
  * `VIEWS` - Number of page views. Data is available on a rolling 12-month window that updates based on the current date. <br> "VIEW" metric can be aggregated by all InsightDimensions.
  * `ORDERS` - Estimated total orders placed by Store visitors within 14 days of their visit. Orders contain one or more units sold. Data is available on a rolling 12-month window that updates based on the current date. <br> "ORDERS" metric can be aggregated by all the InsightDimensions.
  * `UNITS` - Estimated units purchased by Store visitors within 14 days of their last visit. Data is available on a rolling 12-month window that updates based on the current date. <br> "UNITS" metric can be aggregated by all the InsightDimensions.
  * `SALES` - Estimated total sales generated by Store visitors within 14 days of their last visit. Data is available on a rolling 12-month window that updates based on the current date. <br> "SALES" metric can be aggregated by all the InsightDimensions.
  * `VISITS` - Total visits to a page within a single day. Each visitor can visit more than one page, and they can visit your Store from more than one traffic source. Data is available on a rolling 12-month window that updates based on the current date. <br> "VISITS" metric can be aggregated by all the InsightDimensions.
  * `VISITORS` - Total visitors to your Store within the selected date range, calculated based on daily unique users or devices. One visitor can visit more than one page, and they can visit your Store from more than one traffic source. The total visitors by page or source may sum up to a value larger than the total visitors by day to the Store or to the page. Data is available on a rolling 12-month window that updates based on the current date. <br> "VISITORS" metric currently can only be aggregated by InsightDimension "Date". Users won't be able to get this metric when specifying other InsightDimensions. This is because number of visitors are measured at store level. This also means this metric won't be impacted by the InsightFilter.
  * `SCORE_LEVEL` This metric is the overall Store Quality rating calculated based on various factors defining the quality of a store. It can be `HIGH`, `MEDIUM` or `LOW`. This metric currently can only be aggregated by InsightDimension "DATE".
  * `RECOMMENDATIONS` This metric is an Array of Objects containing recommendation details. Each object includes fields like `recommendedAction` (description of recommendation), `observedAverageDwellTimeIncrease` (improvement in dwell time), and `observedAverageSalesIncrease` (improvement in sales).
  * `CONTRIBUTORS` This metric is the array of recommendations applied by the Store Owner which resulted in the improvement of overall store quality. This metric currently can only be aggregated by InsightDimension "DATE".
  * `DWELL` This metric is the time a customer spends on the store, on an average. This metric is specifically for the store quality and measures the time spent by a shopping customer on the store. This is calculated differently from "DWELL_TIME". This metric currently can only be aggregated by InsightDimension "DATE".
  * `SALES_LAST_60_DAYS` This metric represents the estimated sales performance of your stores by in last 60 days. This metric currently can only be aggregated by InsightDimension "DATE".
  * `PEER_DWELL` This metric is the average time customers spend on other similar (peer) stores. This metric currently can only be aggregated by InsightDimension "DATE".
  * `PEER_SALES_LAST_60_DAYS` This metric represents the estimated average sales performance of similar (peer) stores by looking back last 60 days. This metric currently can only be aggregated by InsightDimension "DATE".
  * `DWELL_TIME` This metric represents the average time a customer spends on the store, providing insights into user engagement by calculating the average duration of visits. <br> "DWELL_TIME" metric can be aggregated by all the InsightDimensions or at the store level. For aggregation at store level, *dimension* must be omitted from the request.
  * `BOUNCE_RATE` This metric provides insights into visitor engagement by measuring the ratio of total bounce visits(customer who landed on the store and left quickly without engaging) to total landing visits. It provides insights into user interaction, available at both page and store levels. <br> "BOUNCE_RATE" metric can be aggregated by all the InsightDimensions or at the store level. For aggregation at store level, *dimension* must be omitted from the request.
  * `NEW_TO_STORE` This metric reports the total count of unique visitors who are new to the store, providing valuable insights into the number of first-time shoppers. <br> "NEW_TO_STORE" metric currently can only be aggregated by InsightDimension "DATE" or at the store level. For aggregation at store level, *dimension* must be omitted from the request.
"""


type SortOrder = Literal["ASC", "DESC"]
"""
Describes whether a sort should be ascending (ASC) or descending (DESC).
"""


type TrafficSource = Literal["ADS", "ORGANIC", "OTHER"]
"""
Traffic Source Type:
  * `ADS` - Traffic from Sponsored Brands ads on Amazon.
  * `ORGANIC` - Traffic originating from your brand link on Amazon product detail pages.
  * `OTHER` - All other traffic sources not categorized.
"""


class AsinEngagementDetail(LenientModel):
    """A key-value pair map which contains the dimension and metric information. The key is either dimension name or metric name, while the value is the corresponding dimension value or metric value."""

    pass


class GetAsinEngagementForStoreRequest(StrictModel):
    dimension: AsinEngagementDimension | None = Field(default=None)
    endDate: date = Field(
        description="The end date (inclusive) in YYYY-MM-DD format for the time period from when to fetch the insights."
    )
    metrics: list[AsinEngagementMetric | str] = Field(
        min_length=0,
        max_length=12,
        description="List of the engagement metrics to be fetched. At least one metric should be specified.",
    )
    orderBy: SortOrder | None = Field(default=None)
    sortBy: dict[str, Any] | None = Field(
        default=None,
        description="Nullable metric to sort on. If a value is provided, it must also appear in the metrics list. If no value is provided, the result is not guaranteed to be sorted. This field is only valid when the dimension is ASIN.",
    )
    startDate: date = Field(
        description="The start date (inclusive) in YYYY-MM-DD format for the time period from when to fetch the insights."
    )


class GetAsinEngagementForStoreResponse(LenientModel):
    dimension: AsinEngagementDimension | str | None = Field(default=None)
    metricsDetails: list[AsinEngagementDetail] | None = Field(default=None, min_length=0, max_length=1500)


class GetInsightsForStoreRequest(StrictModel):
    dimension: InsightDimension
    endDate: date = Field(
        description="The end date (inclusive) in YYYY-MM-DD format for the time period from when to fetch the insights."
    )
    filter: dict[str, Any] | None = Field(default=None)
    language: str | None = Field(
        default=None,
        description="""
This parameter is only available for Insights Metrics request for Store Quality(SQS). The language parameter is to request RECOMMENDATIONS and CONTRIBUTORS metrics in the requested language. Currently, we support 35 languages. This parameter is optional and default value is 'en' English. Following are the values expected in `language` parameter.
 <table>
   <tr>
    <th>S no.</th>
    <th>Language Code</th>
    <th>Language description</th>
   </tr>
   <tr>
     <th>1</th>
     <th>French (Canada)</th>
     <th>fr-CA</th>
   </tr>
   <tr>
     <th>2</th>
     <th>French (France)</th>
     <th>fr-FR</th>
   </tr>
   <tr>
     <th>3</th>
     <th>German</th>
     <th>de-DE</th>
   </tr>
   <tr>
     <th>4</th>
     <th>Czech</th>
     <th>cs-CZ</th>
   </tr>
   <tr>
    <th>5</th>
    <th>Polish</th>
    <th>pl-PL</th>
  </tr>
  <tr>
    <th>6</th>
    <th>Turkish</th>
    <th>tr-TR</th>
  </tr>
  <tr>
    <th>7</th>
    <th>Dutch</th>
    <th>nl-NL</th>
  </tr>
  <tr>
    <th>8</th>
    <th>Italian</th>
    <th>it-IT</th>
  </tr><tr>
     <th>9</th>
     <th>Spanish (Spain)</th>
     <th>es-ES</th>
   </tr>
   <tr>
     <th>10</th>
     <th>Spanish (Mexico)</th>
     <th>es-MX</th>
   </tr>
 <tr>
     <th>11</th>
     <th>Spanish (Columbia)</th>
     <th>es-CO</th>
   </tr>
  <tr>
     <th>12</th>
     <th>Portugese (Brazil)</th>
     <th>pt-BR</th>
   </tr>
   <tr>
     <th>13</th>
     <th>Hindi (India)</th>
     <th>hi-IN</th>
   </tr><tr>
     <th>14</th>
     <th>Tamil (India)</th>
     <th>ta-IN</th>
   </tr>
   <tr>
     <th>15</th>
     <th>Telugu (India)</th>
     <th>te-IN</th>
   </tr>
   <tr>
     <th>16</th>
     <th>Kanada (India)</th>
     <th>kn-IN</th>
   </tr>
   <tr>
     <th>17</th>
     <th>Malyalam (India)</th>
     <th>ml-IN</th>
   </tr><tr>
     <th>18</th>
     <th>Bangla (India)</th>
     <th>bn-IN</th>
   </tr>
   <tr>
     <th>19</th>
     <th>Marathi (India)</th>
     <th>mr-IN</th>
   </tr>
   <tr>
     <th>20</th>
     <th>Japanese</th>
     <th>ja-JP</th>
   </tr>
   <tr>
     <th>21</th>
     <th>Simplified Chinese</th>
     <th>zh-CN</th>
   <tr>
<th>
22</th>
<th>
Chinese - TAIWAN</th>
<th>
zh-TW</th>
</tr>
<tr>
<th>
23</th>
<th>
Vietnamese</th>
<th>
vi-VN</th>
</tr>
<tr>
<th>
24</th>
<th>
Arabic (U.A.E.)</th>
<th>
ar-AE</th>
</tr>
<tr>
<th>
25</th>
<th>
Swedish (Sweden)</th>
<th>
sv-SE</th>
</tr>
<tr>
<th>
26</th>
<th>
Thai (Thailand)</th>
<th>
th-TH</th>
</tr>
<tr>
<th>
27</th>
<th>
Korean</th>
<th>
ko-KR</th>
</tr>
</tr><tr>
     <th>28</th>
     <th>English</th>
     <th>en</th>
   </tr>
<tr>
     <th>29</th>
     <th>English (US)</th>
     <th>en-US</th>
   </tr>
<tr>
     <th>30</th>
     <th>English (Canada)</th>
     <th>en-CA</th>
   </tr>
<tr>
     <th>31</th>
     <th>English (India)</th>
     <th>en-IN</th>
   </tr>
<tr>
     <th>32</th>
     <th>English (UK)</th>
     <th>en-GB</th>
   </tr>
<tr>
     <th>33</th>
     <th>English (UAE)</th>
     <th>en-AE</th>
   </tr>
<tr>
     <th>34</th>
     <th>English(Australia)</th>
     <th>en-AU</th>
   </tr>
<tr>
     <th>35</th>
     <th>English (Singapore)</th>
     <th>en-SG</th>
   </tr>
 </table>
 <br><br>
""",
    )
    maxResult: int | None = Field(
        default=None,
        ge=1,
        le=1500,
        description="The max number of result that will be returned in one response. The max allowed value will be 1500. If the parameter is not presented, it will be default to 1500.",
    )
    metrics: list[InsightMetric | str] = Field(
        min_length=1,
        max_length=20,
        description="List of the insight metrics to be fetched. Only one metric should be specified.",
    )
    paginationToken: str | None = Field(
        default=None,
        description="The token that last request returned. It will be used to fetch next page of response.",
    )
    startDate: date = Field(
        description="The start date (inclusive) in YYYY-MM-DD format for the time period from when to fetch the insights. The earliest date will be 2018-09-01, if the input is earlier, it will be default to 2018-09-01"
    )


class GetInsightsForStoreResponse(LenientModel):
    dimension: InsightDimension | str | None = Field(default=None)
    filter: InsightFilterOut | None = Field(default=None)
    metricsDetails: list[InsightMetricsDetail] | None = Field(default=None, min_length=0, max_length=1500)
    paginationToken: str | None = Field(
        default=None,
        description="The token can be directly used to fetch next page of the result. The token can only been used when the token is been created less than 24 hours and the request input is same as last request",
    )


class InsightFilter(StrictModel):
    """The filter to restrict the return data. Users can specifiy the pages/source/tags they feel interested in for the insights. The relationship between each field is 'AND'. E.g. The user can speficy {pageIds=[page1_id], sources=[source1]} to retrieve the related insights for page1 and source1. The user can specify {pageIds=[page1_id], tags=[tag1_name]} to retrieve related insights for page1 and tag1. <br><br> However, specifying both "sources" and "tags" is currently not supported. Users cannot retrieve insights for given sources and tags as all the tags belong to a specific source named "tagged"."""

    pageIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="List of pages to be fetched for insight metrics. Users can first make request to the API with the same parameters but without the filter to retrieve all the available page ids.",
    )
    sources: list[TrafficSource | str] | None = Field(
        default=None, min_length=0, max_length=200, description="List of sources to be fetched for insight metrics."
    )
    tags: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="List of tags to be fetched for insight metrics. Users can first make request to the API with the same parameters but without the filter to retrieve all the available tag names.",
    )


class InsightFilterOut(LenientModel):
    """The filter to restrict the return data. Users can specifiy the pages/source/tags they feel interested in for the insights. The relationship between each field is 'AND'. E.g. The user can speficy {pageIds=[page1_id], sources=[source1]} to retrieve the related insights for page1 and source1. The user can specify {pageIds=[page1_id], tags=[tag1_name]} to retrieve related insights for page1 and tag1. <br><br> However, specifying both "sources" and "tags" is currently not supported. Users cannot retrieve insights for given sources and tags as all the tags belong to a specific source named "tagged"."""

    pageIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="List of pages to be fetched for insight metrics. Users can first make request to the API with the same parameters but without the filter to retrieve all the available page ids.",
    )
    sources: list[TrafficSource | str] | None = Field(
        default=None, min_length=0, max_length=200, description="List of sources to be fetched for insight metrics."
    )
    tags: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="List of tags to be fetched for insight metrics. Users can first make request to the API with the same parameters but without the filter to retrieve all the available tag names.",
    )


class InsightMetricsDetail(LenientModel):
    """A key-value pair map which contains the dimension and metric information. The key is either dimension name or metric name, while the value is the corresponding dimension value or metric value. Addition of boolean,Array and Object is solely for the Store Quality metrics."""

    pass


class StoreQualityCompletedRecommendation(LenientModel):
    """The Object containing recommendations to improve store quality."""

    category: str | None = Field(
        default=None, description="The category in which the store owners could see improvment by this recommendation."
    )
    exampleLink: str | None = Field(
        default=None, description="Link to the example store with a sample to showcase a recommended action."
    )
    exampleText: str | None = Field(
        default=None, description="The text to describe the example to showcase the recommended action."
    )
    observedAverageDwellTimeIncrease: str | None = Field(
        default=None, description="The percentage by which store quality could improve by this recommendation."
    )
    recommendedAction: str | None = Field(default=None, description="description of the recommendation.")


class StoreQualityRecommendation(LenientModel):
    """The Object containing recommendations to improve store quality."""

    category: str | None = Field(
        default=None, description="The category in which the store owners could see improvment by this recommendation."
    )
    ctaLink: str | None = Field(
        default=None, description="Call to Action(CTA) link to take customer to the page where the changes can be made."
    )
    ctaText: str | None = Field(default=None, description="Text describing the Call to Action(CTA).")
    exampleLink: str | None = Field(
        default=None, description="Link to the example store with a sample to showcase a recommended action."
    )
    exampleText: str | None = Field(
        default=None, description="The text to describe the example to showcase the recommended action."
    )
    observedAveragSalesIncrease: str | None = Field(
        default=None, description="The percentage by which store's sales could improve by this recommendation."
    )
    observedAverageDwellTimeIncrease: str | None = Field(
        default=None, description="The percentage by which store quality could improve by this recommendation."
    )
    recommendedAction: str | None = Field(default=None, description="description of the recommendation.")


__all__ = [
    "AsinEngagementDetail",
    "AsinEngagementDimension",
    "AsinEngagementMetric",
    "GetAsinEngagementForStoreRequest",
    "GetAsinEngagementForStoreResponse",
    "GetInsightsForStoreRequest",
    "GetInsightsForStoreResponse",
    "InsightDimension",
    "InsightFilter",
    "InsightFilterOut",
    "InsightMetric",
    "InsightMetricsDetail",
    "SortOrder",
    "StoreQualityCompletedRecommendation",
    "StoreQualityRecommendation",
    "TrafficSource",
]
