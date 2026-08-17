"""KeywordTargets resource operations.

Generated from OpenAPI spec (tag: Keyword Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.keyword_targets import (
    GlobalRankedTargetWithThemedBidsResponse,
    KeywordTargetResponse,
)


class KeywordTargets(BaseResource):

    @overload
    async def get_global_ranked_keyword_recommendation(
        self, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GlobalRankedTargetWithThemedBidsResponse: ...
    @overload
    async def get_global_ranked_keyword_recommendation(self, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_global_ranked_keyword_recommendation(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_global_ranked_keyword_recommendation(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> GlobalRankedTargetWithThemedBidsResponse | dict[str, Any] | httpx.Response:
        """The <b> POST /sp/global/targets/keywords/recommendations/list </b> endpoint returns recommended keyword targets for a list of countries given either A) a list of ad ASINs per target country or B) a global campaign ID and ad group ID. Please use the recommendationType field to specify if you want to use option A or option B. This endpoint will also return recommended bids along with each recommendation keyword target.<br><br> <b> Asins</b> <br>Global API endpoint accepts <b>asins</b> array. Item is a <b>country asin map</b> Key is the 2-letter country code. Value is an asin.<br><br> <b> Targets</b> <br>Global API endpoint accepts <b>targets</b> array. Item is a <b>country target object</b> Object has two fields: matchType and countryKeywords. CountryKeywords is a map with a key as the 2-letter country code and value as a keyword object. <br/><br/>Each country will be processed in parallel according to rules of <a href='https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#tag/Keyword-Targets:~:text=keywords/localize%20endpoint.-,Version%205.0,-New%20Features'>version 5</a> recommendation API.<h3> Availability </h3> Global keyword recommendation API is available in all the marketplaces."""

        resp = await self._request(
            "POST",
            "/sp/global/targets/keywords/recommendations/list",
            headers={
                "Content-Type": "application/vnd.spkeywordsrecommendation.v5+json",
                "Accept": "application/vnd.spkeywordsrecommendation.v5+json",
            },
        )
        return self._response(GlobalRankedTargetWithThemedBidsResponse, resp, mode=mode)

    @overload
    async def get_ranked_keyword_recommendation(
        self, *, mode: Literal["pydantic"] = "pydantic"
    ) -> KeywordTargetResponse: ...
    @overload
    async def get_ranked_keyword_recommendation(self, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_ranked_keyword_recommendation(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_ranked_keyword_recommendation(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> KeywordTargetResponse | dict[str, Any] | httpx.Response:
        """The <b> POST /sp/targets/keywords/recommendations </b> endpoint returns recommended keyword targets given either A) a list of ad ASINs or B) a campaign ID and ad group ID. Please use the recommendationType field to specify if you want to use option A or option B. This endpoint will also return recommended bids along with each recommendation keyword target.<br><br> <b> Ranking </b> <br> The keyword recommendations will be ranked in descending order of clicks or impressions, depending on the <b>sortDimension</b> field provided by the user. You may also input your own keyword targets to be ranked alongside the keyword recommendations by using the <b>targets</b> array. <br><br> <b> Localization </b> <br> Use the <b> locale </b> field to get keywords in your specified locale. Supported marketplace to locale mappings can be found at the <a href='https://advertising.amazon.com/API/docs/en-us/localization/#/Keyword%20Localization'>POST /keywords/localize</a> endpoint. <h1> Version 5.0 </h1>  <h2> New Features </h2> Version 5.0 utilizes the new theme-based bid recommendations, which can be retrieved at the endpoint <b>/sp/targets/bid/recommendations</b>, to return improved bid recommendations for each keyword. Theme-based bid recommendations provide \\\'themes\\\' and \\\'impact metrics\\\' along with each bid suggestion to help you choose the right bid for your keyword target.<br><br><b>Themes</b><br> We now may return multiple bid suggestions for each keyword target. Each suggestion will have a theme to express the business objective of the bid. Available themes are: <ul> <li> CONVERSION_OPPORTUNITIES - The default theme which aims to maximize number of conversions. </li> <li> SPECIAL_DAYS - A theme available during high sales events such as Prime Day, to anticipate an increase in sales and competition.</li></ul><b>Impact Metrics</b><br>We have added impact metrics which provide insight on the number of clicks and conversions you will receive for targeting a keyword at a certain bid. <br><br><b>Bidding Strategy</b><br> You may now specify your bidding strategy in the KEYWORDS_BY_ASINS request to get bid suggestions tailored to your bidding strategy. For KEYWORDS_BY_ADGROUP requests, you will not specify a bidding strategy, because the bidding strategy of the ad group is used. The three bidding strategies are: <ul> <li> LEGACY_FOR_SALES - Dynamic bids (down only) </li> <li> AUTO_FOR_SALES - Dynamic bids (up and down) </li> <li> MANUAL - Fixed bids </li> </ul> <h3> Availability </h3> Version 5.0 is only available in the following marketplaces: US, CA, BR, MX, UK, DE, FR, ES, IN, IT, NL, AE, SA, TR, EG, BE, SE, PL, JP, AU, SG. <h1> Version 4.0 </h1> <h2> New features </h2> Version 4.0 allows users to retrieve recommended keyword targets which are sorted in descending order of clicks or conversions. The default sort dimension, if not specified, ranks recommendations by our interal ranking mechanism. We have also added search term metrics. <b> Search term impression share </b> indicates the percentage share of all ad-attributed impressions you received on that keyword in the last 30 days. This metric helps advertisers identify potential opportunities based on their share on relevant keywords. <b> Search term impression rank </b> indicates your ranking among all advertisers for the keyword by ad impressions in a marketplace. It tells an advertiser how many advertisers had higher share of ad impressions. <i> Search term information is only available for keywords the advertiser targeted with ad impressions. </i> <h3> Availability </h3> Version 4.0 is available in all marketplaces."""

        resp = await self._request(
            "POST",
            "/sp/targets/keywords/recommendations",
            headers={
                "Content-Type": "application/vnd.spkeywordsrecommendation.v3+json",
                "Accept": "application/vnd.spkeywordsrecommendation.v3+json",
            },
        )
        return self._response(KeywordTargetResponse, resp, mode=mode)
