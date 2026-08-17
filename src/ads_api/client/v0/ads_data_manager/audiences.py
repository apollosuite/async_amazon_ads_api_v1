"""Audiences resource operations.

Generated from OpenAPI spec (tag: Audiences).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.ads_data_manager.audiences import (
    AdsCdxSolCreateAudienceRequestContent,
    AdsCdxSolCreateAudienceResponseContent,
    AdsCdxSolGetAudienceResponseContent,
    AdsCdxSolListAudienceResponseContent,
    IngestAudiencesRequestContent,
    IngestAudiencesResponseContent,
)


class Audiences(BaseResource):

    @overload
    async def create_audience_dataset(
        self, body: AdsCdxSolCreateAudienceRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdsCdxSolCreateAudienceResponseContent: ...
    @overload
    async def create_audience_dataset(
        self, body: AdsCdxSolCreateAudienceRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_audience_dataset(
        self, body: AdsCdxSolCreateAudienceRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_audience_dataset(
        self, body: AdsCdxSolCreateAudienceRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdsCdxSolCreateAudienceResponseContent | dict[str, Any] | httpx.Response:
        """Creates an Audience DataSet."""

        resp = await self._request("POST", "/adm/audiences", json=self.dump_json(body))
        return self._response(AdsCdxSolCreateAudienceResponseContent, resp, mode=mode)

    @overload
    async def get_audience_dataset(
        self, data_set_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdsCdxSolGetAudienceResponseContent: ...
    @overload
    async def get_audience_dataset(self, data_set_id: str, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_audience_dataset(self, data_set_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_audience_dataset(
        self, data_set_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdsCdxSolGetAudienceResponseContent | dict[str, Any] | httpx.Response:
        """Gets an Audience DataSet."""

        resp = await self._request("GET", f"/adm/audiences/{data_set_id}")
        return self._response(AdsCdxSolGetAudienceResponseContent, resp, mode=mode)

    @overload
    async def ingest_audiences(
        self, data_set_id: str, body: IngestAudiencesRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> IngestAudiencesResponseContent: ...
    @overload
    async def ingest_audiences(
        self, data_set_id: str, body: IngestAudiencesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def ingest_audiences(
        self, data_set_id: str, body: IngestAudiencesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def ingest_audiences(
        self,
        data_set_id: str,
        body: IngestAudiencesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> IngestAudiencesResponseContent | dict[str, Any] | httpx.Response:
        """Posts audience members to an audience dataset."""

        resp = await self._request(
            "POST",
            f"/adm/audiences/{data_set_id}/members",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.admAudiences.v1+json",
                "Accept": "application/vnd.admAudiences.v1+json",
            },
        )
        return self._response(IngestAudiencesResponseContent, resp, mode=mode)

    @overload
    async def list_audience_datasets(
        self, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None, limit: float | None = None
    ) -> AdsCdxSolListAudienceResponseContent: ...
    @overload
    async def list_audience_datasets(
        self, *, mode: Literal["dict"], next_token: str | None = None, limit: float | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def list_audience_datasets(
        self, *, mode: Literal["raw"], next_token: str | None = None, limit: float | None = None
    ) -> httpx.Response: ...
    async def list_audience_datasets(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
        limit: float | None = None,
    ) -> AdsCdxSolListAudienceResponseContent | dict[str, Any] | httpx.Response:
        """Lists all Audience DataSets."""

        params = {
            "nextToken": next_token,
            "limit": limit,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/adm/audiences", params=params)
        return self._response(AdsCdxSolListAudienceResponseContent, resp, mode=mode)
