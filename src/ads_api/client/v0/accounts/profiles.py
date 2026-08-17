"""Profiles resource operations.

Generated from OpenAPI spec (tag: Profiles).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.accounts.profiles import (
    Profile,
    ProfileOut,
    ProfileResult,
)


class Profiles(BaseResource):

    @overload
    async def get_profile_by_id(self, profile_id: int, *, mode: Literal["pydantic"] = "pydantic") -> ProfileOut: ...
    @overload
    async def get_profile_by_id(self, profile_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_profile_by_id(self, profile_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_profile_by_id(
        self, profile_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ProfileOut | dict[str, Any] | httpx.Response:
        """This operation does not return a response unless the current account has created at least one campaign using the advertising console."""

        resp = await self._request("GET", f"/v2/profiles/{profile_id}")
        return self._response(ProfileOut, resp, mode=mode)

    @overload
    async def list_profiles(
        self,
        *,
        mode: Literal["pydantic"] = "pydantic",
        api_program: str | None = None,
        access_level: str | None = None,
        profile_type_filter: str | None = None,
        valid_payment_method_filter: str | None = None,
    ) -> list[ProfileOut]: ...
    @overload
    async def list_profiles(
        self,
        *,
        mode: Literal["dict"],
        api_program: str | None = None,
        access_level: str | None = None,
        profile_type_filter: str | None = None,
        valid_payment_method_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_profiles(
        self,
        *,
        mode: Literal["raw"],
        api_program: str | None = None,
        access_level: str | None = None,
        profile_type_filter: str | None = None,
        valid_payment_method_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_profiles(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        api_program: str | None = None,
        access_level: str | None = None,
        profile_type_filter: str | None = None,
        valid_payment_method_filter: str | None = None,
    ) -> list[ProfileOut] | list[dict[str, Any]] | httpx.Response:
        """Note that this operation does not return a response unless the current account has created at least one campaign using the advertising console."""

        params = {
            "apiProgram": api_program,
            "accessLevel": access_level,
            "profileTypeFilter": profile_type_filter,
            "validPaymentMethodFilter": valid_payment_method_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/v2/profiles", params=params)
        return self._response_list(ProfileOut, resp, mode=mode)

    @overload
    async def update_profiles(
        self, body: list[Profile], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[ProfileResult]: ...
    @overload
    async def update_profiles(self, body: list[Profile], *, mode: Literal["dict"]) -> list[dict[str, Any]]: ...
    @overload
    async def update_profiles(self, body: list[Profile], *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_profiles(
        self, body: list[Profile], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[ProfileResult] | list[dict[str, Any]] | httpx.Response:
        """Note that this operation is only used for Sellers using Sponsored Products. This operation is not enabled for vendor type accounts."""

        resp = await self._request("PUT", "/v2/profiles", json=[self.dump_json(x) for x in body])
        return self._response_list(ProfileResult, resp, mode=mode)
