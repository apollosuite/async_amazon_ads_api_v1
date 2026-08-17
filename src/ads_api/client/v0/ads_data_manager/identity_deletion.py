"""IdentityDeletion resource operations.

Generated from OpenAPI spec (tag: Identity Deletion).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.ads_data_manager.identity_deletion import (
    DeleteIdentityRequestContent,
)


class IdentityDeletion(BaseResource):

    @overload
    async def delete_identity(
        self, body: DeleteIdentityRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> Any: ...
    @overload
    async def delete_identity(self, body: DeleteIdentityRequestContent, *, mode: Literal["dict"]) -> Any: ...
    @overload
    async def delete_identity(self, body: DeleteIdentityRequestContent, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_identity(
        self, body: DeleteIdentityRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> Any:
        """Deletes matched list of users from your data room within 30 days."""

        resp = await self._request(
            "POST",
            "/adm/identities/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.admDataDeletion.v1+json",
                "Accept": "application/vnd.admDataDeletion.v1+json",
            },
        )
        if mode == "raw":
            return resp
        return resp.json()
