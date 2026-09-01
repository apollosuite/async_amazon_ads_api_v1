"""UserPermissions resource operations.

Generated from OpenAPI spec (tag: user_permissions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.accounts.user_permissions import (
    DeleteUserPermissionsRequestContent,
    DeleteUserPermissionsResponseContent,
    ListUsersRequestContent,
    ListUsersResponseContent,
    QueryUserPermissionsRequestContent,
    QueryUserPermissionsResponseContent,
    QueryUserRolesRequestContent,
    QueryUserRolesResponseContent,
    UpdateUserPermissionsRequestContent,
    UpdateUserPermissionsResponseContent,
)


class UserPermissions(BaseResource):

    @overload
    async def delete_user_permissions(
        self, body: DeleteUserPermissionsRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_user_permissions(
        self, body: DeleteUserPermissionsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> DeleteUserPermissionsResponseContent: ...
    @overload
    async def delete_user_permissions(
        self, body: DeleteUserPermissionsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_user_permissions(
        self,
        body: DeleteUserPermissionsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> DeleteUserPermissionsResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "POST",
            "/userPermissions/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.MinosAuthorizationNativeServicePublicAPI.DeleteUserPermissionsResource.v1+json",
                "Accept": "application/vnd.MinosAuthorizationNativeServicePublicAPI.DeleteUserPermissionsResource.v1+json",
            },
        )
        return self._response(DeleteUserPermissionsResponseContent, resp, mode=mode)

    @overload
    async def list_users(
        self, body: ListUsersRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def list_users(
        self, body: ListUsersRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> ListUsersResponseContent: ...
    @overload
    async def list_users(
        self, body: ListUsersRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_users(
        self, body: ListUsersRequestContent | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ListUsersResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "POST",
            "/users/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.listusers.v1+json",
                "Accept": "application/vnd.listusers.v1+json",
            },
        )
        return self._response(ListUsersResponseContent, resp, mode=mode)

    @overload
    async def query_user_permissions(
        self, body: QueryUserPermissionsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_user_permissions(
        self, body: QueryUserPermissionsRequestContent, *, mode: Literal["pydantic"]
    ) -> QueryUserPermissionsResponseContent: ...
    @overload
    async def query_user_permissions(
        self, body: QueryUserPermissionsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_user_permissions(
        self, body: QueryUserPermissionsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> QueryUserPermissionsResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "POST",
            "/userPermissions/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.queryuserpermissions.v1+json",
                "Accept": "application/vnd.queryuserpermissions.v1+json",
            },
        )
        return self._response(QueryUserPermissionsResponseContent, resp, mode=mode)

    @overload
    async def query_user_roles(
        self, body: QueryUserRolesRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_user_roles(
        self, body: QueryUserRolesRequestContent, *, mode: Literal["pydantic"]
    ) -> QueryUserRolesResponseContent: ...
    @overload
    async def query_user_roles(self, body: QueryUserRolesRequestContent, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_user_roles(
        self, body: QueryUserRolesRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> QueryUserRolesResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "POST",
            "/userRoles/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.queryuserroles.v1+json",
                "Accept": "application/vnd.queryuserroles.v1+json",
            },
        )
        return self._response(QueryUserRolesResponseContent, resp, mode=mode)

    @overload
    async def update_user_permissions(
        self, body: UpdateUserPermissionsRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_user_permissions(
        self, body: UpdateUserPermissionsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> UpdateUserPermissionsResponseContent: ...
    @overload
    async def update_user_permissions(
        self, body: UpdateUserPermissionsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_user_permissions(
        self,
        body: UpdateUserPermissionsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> UpdateUserPermissionsResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "PUT",
            "/userPermissions",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.MinosAuthorizationNativeServicePublicAPI.UpdateUserPermissionsResource.v1+json",
                "Accept": "application/vnd.MinosAuthorizationNativeServicePublicAPI.UpdateUserPermissionsResource.v1+json",
            },
        )
        return self._response(UpdateUserPermissionsResponseContent, resp, mode=mode)
