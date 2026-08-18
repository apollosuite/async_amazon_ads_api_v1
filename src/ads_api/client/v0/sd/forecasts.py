"""Forecasts resource operations.

Generated from OpenAPI spec (tag: Forecasts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.forecasts import (
    SDForecastRequest,
    SDForecastResponse,
)


class Forecasts(BaseResource):

    @overload
    async def create_sd_forecast(
        self, body: SDForecastRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDForecastResponse: ...
    @overload
    async def create_sd_forecast(self, body: SDForecastRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_sd_forecast(self, body: SDForecastRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_sd_forecast(
        self, body: SDForecastRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDForecastResponse | dict[str, Any] | httpx.Response:
        """Returns forecasts for a given ad group specified in SD forecast request."""

        resp = await self._request(
            "POST",
            "/sd/forecasts",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sdforecasts.v3.1+json",
                "Accept": "application/vnd.sdforecasts.v3.1+json",
            },
        )
        return self._response(SDForecastResponse, resp, mode=mode)
