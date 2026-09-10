"""TargetableEntities resource operations.

Generated from OpenAPI spec (tag: targetable_entities).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.discovery.targetable_entities import (
    ListTargetableEntitiesRequestContent,
    ListTargetableEntitiesResponseContent,
    ListTargetableEntityPathsRequestContent,
    ListTargetableEntityPathsResponseContent,
)


class TargetableEntities(BaseResource):

    @overload
    async def list_targetable_entities(
        self, body: ListTargetableEntitiesRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def list_targetable_entities(
        self, body: ListTargetableEntitiesRequestContent, *, mode: Literal["pydantic"]
    ) -> ListTargetableEntitiesResponseContent: ...
    @overload
    async def list_targetable_entities(
        self, body: ListTargetableEntitiesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_targetable_entities(
        self, body: ListTargetableEntitiesRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ListTargetableEntitiesResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "POST",
            "/targetableEntities/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.Mindreader.TargetableEntitiesResource.v1+json",
                "Accept": "application/vnd.Mindreader.TargetableEntitiesResource.v1+json",
            },
        )
        return self._response(ListTargetableEntitiesResponseContent, resp, mode=mode)

    @overload
    async def list_targetable_entity_paths(
        self, body: ListTargetableEntityPathsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def list_targetable_entity_paths(
        self, body: ListTargetableEntityPathsRequestContent, *, mode: Literal["pydantic"]
    ) -> ListTargetableEntityPathsResponseContent: ...
    @overload
    async def list_targetable_entity_paths(
        self, body: ListTargetableEntityPathsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_targetable_entity_paths(
        self, body: ListTargetableEntityPathsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ListTargetableEntityPathsResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "POST",
            "/targetableEntities/paths/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.Mindreader.TargetableEntitiesResource.v1+json",
                "Accept": "application/vnd.Mindreader.TargetableEntitiesResource.v1+json",
            },
        )
        return self._response(ListTargetableEntityPathsResponseContent, resp, mode=mode)
