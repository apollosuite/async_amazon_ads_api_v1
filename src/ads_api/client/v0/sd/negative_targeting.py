"""NegativeTargeting resource operations.

Generated from OpenAPI spec (tag: Negative Targeting).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.negative_targeting import (
    CreateNegativeTargetingClause,
    NegativeTargetingClause,
    NegativeTargetingClauseEx,
    TargetResponse,
    UpdateNegativeTargetingClause,
)


class NegativeTargeting(BaseResource):

    @overload
    async def archive_negative_targeting_clause(
        self, negative_target_id: int, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def archive_negative_targeting_clause(
        self, negative_target_id: int, *, mode: Literal["pydantic"]
    ) -> TargetResponse: ...
    @overload
    async def archive_negative_targeting_clause(
        self, negative_target_id: int, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def archive_negative_targeting_clause(
        self, negative_target_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> TargetResponse | dict[str, Any] | httpx.Response:
        """Equivalent to using the updateNegativeTargetingClauses operation to set the `state` property of a targeting clause to `archived`. See [Developer Notes](http://advertising.amazon.com/API/docs/guides/developer_notes#Archiving) for more information."""

        resp = await self._request("DELETE", f"/sd/negativeTargets/{negative_target_id}")
        return self._response(TargetResponse, resp, mode=mode)

    @overload
    async def create_negative_targeting_clauses(
        self, body: list[CreateNegativeTargetingClause] | None = None, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_negative_targeting_clauses(
        self, body: list[CreateNegativeTargetingClause] | None = None, *, mode: Literal["pydantic"]
    ) -> list[TargetResponse]: ...
    @overload
    async def create_negative_targeting_clauses(
        self, body: list[CreateNegativeTargetingClause] | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_negative_targeting_clauses(
        self,
        body: list[CreateNegativeTargetingClause] | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> list[TargetResponse] | list[dict[str, Any]] | httpx.Response:
        """Successfully created negative targeting clauses associated with an ad group are assigned a unique target identifier."""

        resp = await self._request("POST", "/sd/negativeTargets", json=self.dump_json(body))
        return self._response_list(TargetResponse, resp, mode=mode)

    @overload
    async def get_negative_targets(
        self, negative_target_id: int, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_negative_targets(
        self, negative_target_id: int, *, mode: Literal["pydantic"]
    ) -> NegativeTargetingClause: ...
    @overload
    async def get_negative_targets(self, negative_target_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_negative_targets(
        self, negative_target_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> NegativeTargetingClause | dict[str, Any] | httpx.Response:
        """This call returns the minimal set of negative targeting clause fields, but is more efficient than getNegativeTargetsEx."""

        resp = await self._request("GET", f"/sd/negativeTargets/{negative_target_id}")
        return self._response(NegativeTargetingClause, resp, mode=mode)

    @overload
    async def get_negative_targets_ex(
        self, negative_target_id: int, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_negative_targets_ex(
        self, negative_target_id: int, *, mode: Literal["pydantic"]
    ) -> NegativeTargetingClauseEx: ...
    @overload
    async def get_negative_targets_ex(self, negative_target_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_negative_targets_ex(
        self, negative_target_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> NegativeTargetingClauseEx | dict[str, Any] | httpx.Response:
        """Gets a negative targeting clause with extended fields. Note that this call returns the full set of negative targeting clause extended fields, but is less efficient than getNegativeTarget."""

        resp = await self._request("GET", f"/sd/negativeTargets/extended/{negative_target_id}")
        return self._response(NegativeTargetingClauseEx, resp, mode=mode)

    @overload
    async def list_negative_targeting_clauses(
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
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_negative_targeting_clauses(
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
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[NegativeTargetingClause]: ...
    @overload
    async def list_negative_targeting_clauses(
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
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_negative_targeting_clauses(
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
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[NegativeTargetingClause] | list[dict[str, Any]] | httpx.Response:
        """Gets a list of negative targeting clauses objects for a requested set of Sponsored Display negative targets. Note that the Negative Targeting Clause object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use the negative target operations that return the NegativeTargetingClauseEx object."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/negativeTargets", params=params)
        return self._response_list(NegativeTargetingClause, resp, mode=mode)

    @overload
    async def list_negative_targeting_clauses_ex(
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
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_negative_targeting_clauses_ex(
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
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[NegativeTargetingClauseEx]: ...
    @overload
    async def list_negative_targeting_clauses_ex(
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
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_negative_targeting_clauses_ex(
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
        target_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[NegativeTargetingClauseEx] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of NegativeTargetingClauseEx objects for a set of requested negative targets. Note that this call returns the full set of negative targeting clause extended fields, but is less efficient than getNegativeTargets."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "targetIdFilter": target_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/negativeTargets/extended", params=params)
        return self._response_list(NegativeTargetingClauseEx, resp, mode=mode)

    @overload
    async def update_negative_targeting_clauses(
        self, body: list[UpdateNegativeTargetingClause] | None = None, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def update_negative_targeting_clauses(
        self, body: list[UpdateNegativeTargetingClause] | None = None, *, mode: Literal["pydantic"]
    ) -> list[TargetResponse]: ...
    @overload
    async def update_negative_targeting_clauses(
        self, body: list[UpdateNegativeTargetingClause] | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_negative_targeting_clauses(
        self,
        body: list[UpdateNegativeTargetingClause] | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> list[TargetResponse] | list[dict[str, Any]] | httpx.Response:
        """Updates one or more negative targeting clauses. Negative targeting clauses are identified using their targetId. The mutable field is `state`. Maximum length of the array is 100 objects."""

        resp = await self._request("PUT", "/sd/negativeTargets", json=self.dump_json(body))
        return self._response_list(TargetResponse, resp, mode=mode)
