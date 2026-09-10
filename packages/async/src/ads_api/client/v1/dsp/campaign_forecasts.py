"""DSPCampaignForecasts resource operations.

Generated from OpenAPI spec (tag: CampaignForecasts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaign_forecasts.dsp import (
    DSPCampaignForecastMultiStatusResponse,
    DSPRetrieveCampaignForecastRequest,
)


class DSPCampaignForecasts(BaseResource):

    @overload
    async def retrieve_campaign_forecast(
        self, body: DSPRetrieveCampaignForecastRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def retrieve_campaign_forecast(
        self, body: DSPRetrieveCampaignForecastRequest, *, mode: Literal["pydantic"]
    ) -> DSPCampaignForecastMultiStatusResponse: ...
    @overload
    async def retrieve_campaign_forecast(
        self, body: DSPRetrieveCampaignForecastRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def retrieve_campaign_forecast(
        self, body: DSPRetrieveCampaignForecastRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPCampaignForecastMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Retrieve campaign forecast"""

        resp = await self._request("POST", "/adsApi/v1/retrieve/campaignForecasts/dsp", json=self.dump_json(body))
        return self._response(DSPCampaignForecastMultiStatusResponse, resp, mode=mode)
