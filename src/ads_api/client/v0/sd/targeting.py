"""Targeting resource operations.

Generated from OpenAPI spec (tag: Targeting).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.targeting import (
    CreateTargetingClause,
    TargetingClause,
    TargetingClauseEx,
    TargetResponse,
    UpdateTargetingClause,
)


class Targeting(BaseResource):

    @overload
    async def archive_targeting_clause(
        self, target_id: int, *, mode: Literal["pydantic"] = "pydantic"
    ) -> TargetResponse: ...
    @overload
    async def archive_targeting_clause(self, target_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def archive_targeting_clause(self, target_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def archive_targeting_clause(
        self, target_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> TargetResponse | dict[str, Any] | httpx.Response:
        """Equivalent to using the `updateTargetingClauses` operation to set the `state` property of a targeting clause to `archived`. See [Developer"""

        resp = await self._request("DELETE", f"/sd/targets/{target_id}")
        return self._response(TargetResponse, resp, mode=mode)

    @overload
    async def create_targeting_clauses(
        self, body: list[CreateTargetingClause], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[TargetResponse]: ...
    @overload
    async def create_targeting_clauses(
        self, body: list[CreateTargetingClause], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_targeting_clauses(
        self, body: list[CreateTargetingClause], *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_targeting_clauses(
        self, body: list[CreateTargetingClause], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[TargetResponse] | list[dict[str, Any]] | httpx.Response:
        """Successfully created targeting clauses are assigned a unique `targetId` value."""

        resp = await self._request("POST", "/sd/targets", json=[self.dump_json(x) for x in body])
        return self._response_list(TargetResponse, resp, mode=mode)

    @overload
    async def get_targets(self, target_id: int, *, mode: Literal["pydantic"] = "pydantic") -> TargetingClause: ...
    @overload
    async def get_targets(self, target_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_targets(self, target_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_targets(
        self, target_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> TargetingClause | dict[str, Any] | httpx.Response:
        """This call returns the minimal set of targeting clause fields."""

        resp = await self._request("GET", f"/sd/targets/{target_id}")
        return self._response(TargetingClause, resp, mode=mode)

    @overload
    async def get_targets_ex(self, target_id: int, *, mode: Literal["pydantic"] = "pydantic") -> TargetingClauseEx: ...
    @overload
    async def get_targets_ex(self, target_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_targets_ex(self, target_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_targets_ex(
        self, target_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> TargetingClauseEx | dict[str, Any] | httpx.Response:
        """Gets a targeting clause object with extended fields. Note that this call returns the full set of targeting clause extended fields, but is less efficient than getTarget."""

        resp = await self._request("GET", f"/sd/targets/extended/{target_id}")
        return self._response(TargetingClauseEx, resp, mode=mode)

    @overload
    async def list_targeting_clauses(
        self,
        *,
        mode: Literal["pydantic"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[TargetingClause]: ...
    @overload
    async def list_targeting_clauses(
        self,
        *,
        mode: Literal["dict"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_targeting_clauses(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_targeting_clauses(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[TargetingClause] | list[dict[str, Any]] | httpx.Response:
        """Gets a list of targeting clauses objects for a requested set of Sponsored Display targets. Note that the Targeting Clause object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use the target operations that return the TargetingClauseEx object."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "targetIdFilter": target_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/targets", params=params)
        return self._response_list(TargetingClause, resp, mode=mode)

    @overload
    async def list_targeting_clauses_ex(
        self,
        *,
        mode: Literal["pydantic"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[TargetingClauseEx]: ...
    @overload
    async def list_targeting_clauses_ex(
        self,
        *,
        mode: Literal["dict"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_targeting_clauses_ex(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_targeting_clauses_ex(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[TargetingClauseEx] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of TargetingClauseEx objects for a set of requested targets. Note that this call returns the full set of targeting clause extended fields, but is less efficient than getTargets."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "targetIdFilter": target_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/targets/extended", params=params)
        return self._response_list(TargetingClauseEx, resp, mode=mode)

    @overload
    async def update_targeting_clauses(
        self, body: list[UpdateTargetingClause], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[TargetResponse]: ...
    @overload
    async def update_targeting_clauses(
        self, body: list[UpdateTargetingClause], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def update_targeting_clauses(
        self, body: list[UpdateTargetingClause], *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_targeting_clauses(
        self, body: list[UpdateTargetingClause], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[TargetResponse] | list[dict[str, Any]] | httpx.Response:
        """Updates one or more targeting clauses. Targeting clauses are identified using their targetId. The mutable fields are `bid` and `state`. Maximum length of the array is 100 objects."""

        resp = await self._request("PUT", "/sd/targets", json=[self.dump_json(x) for x in body])
        return self._response_list(TargetResponse, resp, mode=mode)
