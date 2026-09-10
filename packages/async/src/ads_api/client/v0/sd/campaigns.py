"""Campaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.campaigns import (
    Campaign,
    CampaignResponse,
    CampaignResponseEx,
    CreateCampaign,
    UpdateCampaign,
)


class Campaigns(BaseResource):

    @overload
    async def archive_campaign(self, campaign_id: int, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def archive_campaign(self, campaign_id: int, *, mode: Literal["pydantic"]) -> CampaignResponse: ...
    @overload
    async def archive_campaign(self, campaign_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def archive_campaign(
        self, campaign_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CampaignResponse | dict[str, Any] | httpx.Response:
        """This operation is equivalent to an update operation that sets the status field to 'archived'. Note that setting the status field to 'archived' is permanent and can't be undone. See [Developer Notes](https://advertising.amazon.com/API/docs/en-us/info/developer-notes#archiving) for more information."""

        resp = await self._request("DELETE", f"/sd/campaigns/{campaign_id}")
        return self._response(CampaignResponse, resp, mode=mode)

    @overload
    async def create_campaigns(
        self, body: list[CreateCampaign] | None = None, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_campaigns(
        self, body: list[CreateCampaign] | None = None, *, mode: Literal["pydantic"]
    ) -> list[CampaignResponse]: ...
    @overload
    async def create_campaigns(
        self, body: list[CreateCampaign] | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_campaigns(
        self, body: list[CreateCampaign] | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> list[CampaignResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("POST", "/sd/campaigns", json=self.dump_json(body))
        return self._response_list(CampaignResponse, resp, mode=mode)

    @overload
    async def get_campaign(self, campaign_id: int, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def get_campaign(self, campaign_id: int, *, mode: Literal["pydantic"]) -> Campaign: ...
    @overload
    async def get_campaign(self, campaign_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_campaign(
        self, campaign_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> Campaign | dict[str, Any] | httpx.Response:
        """Returns a Campaign object for a requested campaign. Note that the Campaign object is designed for performance, with a small set of commonly used campaign fields to reduce size. If the extended set of fields is required, use the campaign operations that return the CampaignResponseEx object."""

        resp = await self._request("GET", f"/sd/campaigns/{campaign_id}")
        return self._response(Campaign, resp, mode=mode)

    @overload
    async def get_campaign_response_ex(self, campaign_id: int, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def get_campaign_response_ex(self, campaign_id: int, *, mode: Literal["pydantic"]) -> CampaignResponseEx: ...
    @overload
    async def get_campaign_response_ex(self, campaign_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_campaign_response_ex(
        self, campaign_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CampaignResponseEx | dict[str, Any] | httpx.Response:
        """Returns a CampaignResponseEx object for a requested campaign. The CampaignResponseEx includes the extended set of available fields."""

        resp = await self._request("GET", f"/sd/campaigns/extended/{campaign_id}")
        return self._response(CampaignResponseEx, resp, mode=mode)

    @overload
    async def list_campaigns(
        self,
        *,
        mode: Literal["dict"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        name: str | None = None,
        campaign_id_filter: str | None = None,
        portfolio_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_campaigns(
        self,
        *,
        mode: Literal["pydantic"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        name: str | None = None,
        campaign_id_filter: str | None = None,
        portfolio_id_filter: str | None = None,
    ) -> list[Campaign]: ...
    @overload
    async def list_campaigns(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        name: str | None = None,
        campaign_id_filter: str | None = None,
        portfolio_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_campaigns(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        name: str | None = None,
        campaign_id_filter: str | None = None,
        portfolio_id_filter: str | None = None,
    ) -> list[Campaign] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of Campaign objects for a requested set of Sponsored Display campaigns. Note that the Campaign object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use the campaign operations that return the CampaignResponseEx object."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "campaignIdFilter": campaign_id_filter,
            "portfolioIdFilter": portfolio_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/campaigns", params=params)
        return self._response_list(Campaign, resp, mode=mode)

    @overload
    async def list_campaigns_ex(
        self,
        *,
        mode: Literal["dict"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        name: str | None = None,
        campaign_id_filter: str | None = None,
        portfolio_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_campaigns_ex(
        self,
        *,
        mode: Literal["pydantic"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        name: str | None = None,
        campaign_id_filter: str | None = None,
        portfolio_id_filter: str | None = None,
    ) -> list[CampaignResponseEx]: ...
    @overload
    async def list_campaigns_ex(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        name: str | None = None,
        campaign_id_filter: str | None = None,
        portfolio_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_campaigns_ex(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        name: str | None = None,
        campaign_id_filter: str | None = None,
        portfolio_id_filter: str | None = None,
    ) -> list[CampaignResponseEx] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of CampaignResponseEx objects for a set of requested campaigns."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "campaignIdFilter": campaign_id_filter,
            "portfolioIdFilter": portfolio_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/campaigns/extended", params=params)
        return self._response_list(CampaignResponseEx, resp, mode=mode)

    @overload
    async def update_campaigns(
        self, body: list[UpdateCampaign] | None = None, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def update_campaigns(
        self, body: list[UpdateCampaign] | None = None, *, mode: Literal["pydantic"]
    ) -> list[CampaignResponse]: ...
    @overload
    async def update_campaigns(
        self, body: list[UpdateCampaign] | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_campaigns(
        self, body: list[UpdateCampaign] | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> list[CampaignResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("PUT", "/sd/campaigns", json=self.dump_json(body))
        return self._response_list(CampaignResponse, resp, mode=mode)
