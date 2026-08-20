"""CampaignForecasts resource operations.

Generated from OpenAPI spec (tag: CampaignForecasts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.campaign_forecasts.general import (
    DSPCampaignForecastMultiStatusResponse,
    DSPRetrieveCampaignForecastRequest,
)


class CampaignForecasts(BaseResource):

    @overload
    async def retrieve_campaign_forecast(
        self, body: DSPRetrieveCampaignForecastRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPCampaignForecastMultiStatusResponse: ...
    @overload
    async def retrieve_campaign_forecast(
        self, body: DSPRetrieveCampaignForecastRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def retrieve_campaign_forecast(
        self, body: DSPRetrieveCampaignForecastRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def retrieve_campaign_forecast(
        self, body: DSPRetrieveCampaignForecastRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPCampaignForecastMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Retrieve campaign forecast"""

        resp = await self._request("POST", "/adsApi/v1/retrieve/campaignForecasts/dsp", json=self.dump_json(body))
        return self._response(DSPCampaignForecastMultiStatusResponse, resp, mode=mode)
