"""Advertising Accounts resource operations — from AdvertisingAccounts_prod_3p.json."""

from __future__ import annotations

from async_amazon_ads_api_v1.client.legacy.accounts._base import _AccountsAPIBase
from async_amazon_ads_api_v1.models.legacy.accounts.account import (
    GetAccountResponseContent,
    ListAdsAccountsRequestContent,
    ListAdsAccountsResponseContent,
    RegisterAdsAccountRequestContent,
    RegisterAdsAccountResponseContent,
)


class Accounts(_AccountsAPIBase):
    """Advertising Accounts API — 广告账户注册、列表与查询。"""

    async def register(
        self,
        request: RegisterAdsAccountRequestContent,
    ) -> RegisterAdsAccountResponseContent:
        """注册一个新的广告账户。"""
        resp = await self._request(
            "POST",
            "/adsAccounts",
            json=request.model_dump(),
            headers=self._client_id_header(),
        )
        return self._response(RegisterAdsAccountResponseContent, resp)

    async def list_accounts(
        self,
        request: ListAdsAccountsRequestContent | None = None,
    ) -> ListAdsAccountsResponseContent:
        """列出当前用户的所有广告账户。"""
        body = request.model_dump(exclude_none=True) if request else {}
        resp = await self._request("POST", "/adsAccounts/list", json=body, headers=self._client_id_header())
        return self._response(ListAdsAccountsResponseContent, resp)

    async def get(
        self,
        advertising_account_id: str,
    ) -> GetAccountResponseContent:
        """获取指定广告账户的详细信息。"""
        resp = await self._request(
            "GET",
            f"/adsAccounts/{advertising_account_id}",
            headers=self._client_id_header(),
        )
        return self._response(GetAccountResponseContent, resp)
