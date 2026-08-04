"""Profiles resource operations.

Generated from OpenAPI spec (tag: Profiles).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.profiles.profiles import (
    Profile,
    ProfileOut,
    ProfileResult,
)


class Profiles(BaseResource):

    async def list_profiles(
        self,
        api_program: str | None = None,
        access_level: str | None = None,
        profile_type_filter: str | None = None,
        valid_payment_method_filter: str | None = None,
    ) -> list[ProfileOut]:
        """Note that this operation does not return a response unless the current account has created at least one campaign using the advertising console.

        Parameters
        ----------
        api_program : str
            Filters response to include profiles that have permissions for the specified Advertising API program only. Setting `apiProgram=billing` filters the response to include only profiles to which the user and application associated with the access token have permission to view or edit billing information.
        access_level : str
            Filters response to include profiles that have specified permissions for the specified Advertising API program only. Currently, the only supported access level is `view` and `edit`. Setting `accessLevel=view` filters the response to include only profiles to which the user and application associated with the access token have view permission to the provided api program.
        profile_type_filter : str
            Filters response to include profiles that are of the specified types in the comma-delimited list. Default is all types. Note that this filter performs an inclusive AND operation on the types.
        valid_payment_method_filter : str
            Filter response to include profiles that have valid payment methods. Default is to include all profiles. Setting this filter to `true` returns only profiles with either no `validPaymentMethod` field, or the `validPaymentMethod` field set to `true`.  Setting this to `false` returns profiles with the `validPaymentMethod` field set to `false` only.
        """

        params = {
            "apiProgram": api_program,
            "accessLevel": access_level,
            "profileTypeFilter": profile_type_filter,
            "validPaymentMethodFilter": valid_payment_method_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/v2/profiles", params=params)
        return self._response_list(ProfileOut, resp)

    async def update_profiles(self, body: list[Profile]) -> list[ProfileResult]:
        """Note that this operation is only used for Sellers using Sponsored Products. This operation is not enabled for vendor type accounts."""

        resp = await self._request(
            "PUT",
            "/v2/profiles",
            json=[x.model_dump(mode="json", exclude_none=True) for x in body],
        )
        return self._response_list(ProfileResult, resp)

    async def get_profile_by_id(self, profile_id: int) -> ProfileOut:
        """This operation does not return a response unless the current account has created at least one campaign using the advertising console."""

        resp = await self._request("GET", f"/v2/profiles/{profile_id}")
        return self._response(ProfileOut, resp)
