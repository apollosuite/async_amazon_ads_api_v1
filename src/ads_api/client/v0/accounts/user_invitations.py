"""UserInvitations resource operations.

Generated from OpenAPI spec (tag: user_invitations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.accounts.user_invitations import (
    CreateUserInvitationsRequestContent,
    CreateUserInvitationsResponseContent,
    GetUserInvitationResponseContent,
    ListUserInvitationsRequestContent,
    ListUserInvitationsResponseContent,
    RedeemUserInvitationRequestContent,
    UpdateUserInvitationsRequestContent,
    UpdateUserInvitationsResponseContent,
)


class UserInvitations(BaseResource):

    @overload
    async def create_user_invitations(
        self, body: CreateUserInvitationsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateUserInvitationsResponseContent: ...
    @overload
    async def create_user_invitations(
        self, body: CreateUserInvitationsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_user_invitations(
        self, body: CreateUserInvitationsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_user_invitations(
        self, body: CreateUserInvitationsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> CreateUserInvitationsResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "POST",
            "/user-invitations",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.CreateUserInvitations.v1+json",
                "Accept": "application/vnd.CreateUserInvitations.v1+json",
            },
        )
        return self._response(CreateUserInvitationsResponseContent, resp, mode=mode)

    @overload
    async def get_user_invitation(
        self, invitation_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GetUserInvitationResponseContent: ...
    @overload
    async def get_user_invitation(self, invitation_id: str, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_user_invitation(self, invitation_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_user_invitation(
        self, invitation_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> GetUserInvitationResponseContent | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "GET", f"/user-invitations/{invitation_id}", headers={"Accept": "application/vnd.GetUserInvitation.v1+json"}
        )
        return self._response(GetUserInvitationResponseContent, resp, mode=mode)

    @overload
    async def list_user_invitations(
        self, body: ListUserInvitationsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ListUserInvitationsResponseContent: ...
    @overload
    async def list_user_invitations(
        self, body: ListUserInvitationsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_user_invitations(
        self, body: ListUserInvitationsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_user_invitations(
        self, body: ListUserInvitationsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ListUserInvitationsResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "POST",
            "/user-invitations/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.ListUserInvitations.v1+json",
                "Accept": "application/vnd.ListUserInvitations.v1+json",
            },
        )
        return self._response(ListUserInvitationsResponseContent, resp, mode=mode)

    @overload
    async def redeem_user_invitation(
        self, body: RedeemUserInvitationRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> Any: ...
    @overload
    async def redeem_user_invitation(
        self, body: RedeemUserInvitationRequestContent, *, mode: Literal["dict"]
    ) -> Any: ...
    @overload
    async def redeem_user_invitation(
        self, body: RedeemUserInvitationRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def redeem_user_invitation(
        self, body: RedeemUserInvitationRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> Any:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "PUT",
            "/user-invitations/redeem",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.RedeemUserInvitation.v1+json",
                "Accept": "application/vnd.RedeemUserInvitation.v1+json",
            },
        )
        if mode == "raw":
            return resp
        return resp.json()

    @overload
    async def update_user_invitations(
        self, body: UpdateUserInvitationsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> UpdateUserInvitationsResponseContent: ...
    @overload
    async def update_user_invitations(
        self, body: UpdateUserInvitationsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_user_invitations(
        self, body: UpdateUserInvitationsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_user_invitations(
        self, body: UpdateUserInvitationsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> UpdateUserInvitationsResponseContent | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request(
            "PUT",
            "/user-invitations",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.UpdateUserInvitations.v1+json",
                "Accept": "application/vnd.UpdateUserInvitations.v1+json",
            },
        )
        return self._response(UpdateUserInvitationsResponseContent, resp, mode=mode)
