"""Profiles resource operations — from profiles_openapi.yaml."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1.client.legacy.accounts._base import _AccountsAPIBase
from async_amazon_ads_api_v1.models.legacy.accounts.profiles import Profile, ProfileOut, ProfileResult


class Profiles(_AccountsAPIBase):
    """Profiles API — 广告账户资料（profile）列表、更新与查询。"""

    async def list_profiles(
        self,
        *,
        api_program: str | None = None,
        access_level: str | None = None,
        profile_type_filter: str | None = None,
        valid_payment_method_filter: str | None = None,
    ) -> list[ProfileOut]:
        """获取所有 profile 列表。

        Args:
            api_program: 按 API 程序筛选（billing / campaign / paymentMethod / …）。
            access_level: 按访问级别筛选（view / edit）。
            profile_type_filter: 按账户类型筛选（seller / vendor / agency）。
            valid_payment_method_filter: 按有效支付方式筛选（true / false）。
        """
        params: dict[str, Any] = {}
        if api_program is not None:
            params["apiProgram"] = api_program
        if access_level is not None:
            params["accessLevel"] = access_level
        if profile_type_filter is not None:
            params["profileTypeFilter"] = profile_type_filter
        if valid_payment_method_filter is not None:
            params["validPaymentMethodFilter"] = valid_payment_method_filter

        resp = await self._request(
            "GET",
            "/v2/profiles",
            params=params or None,
            headers=self._client_id_header(),
        )
        return self._response_list(ProfileOut, resp)

    async def update(
        self,
        profiles: list[Profile],
    ) -> list[ProfileResult]:
        """批量更新 profile 的每日预算。

        Args:
            profiles: 待更新的 Profile 列表（需含 profileId 和 dailyBudget）。
        """
        resp = await self._request(
            "PUT",
            "/v2/profiles",
            json=[p.model_dump(exclude_none=True) for p in profiles],
            headers=self._client_id_header(),
        )
        return self._response_list(ProfileResult, resp)

    async def get(
        self,
        profile_id: int,
    ) -> ProfileOut:
        """获取指定 profile 的详细信息。"""
        resp = await self._request(
            "GET",
            f"/v2/profiles/{profile_id}",
            headers=self._client_id_header(),
        )
        return self._response(ProfileOut, resp)
