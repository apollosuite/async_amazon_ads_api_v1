"""Terms Token resource operations — from AdvertisingAccounts_prod_3p.json."""

from __future__ import annotations

from async_amazon_ads_api_v1.client.legacy.accounts._base import _AccountsAPIBase
from async_amazon_ads_api_v1.models.legacy.accounts.terms_token import (
    CreateTermsTokenRequestContent,
    CreateTermsTokenResponseContent,
    GetTermsTokenResponseContent,
)


class TermsToken(_AccountsAPIBase):
    """Terms Token API — 条款令牌创建与状态查询。"""

    async def create(
        self,
        request: CreateTermsTokenRequestContent,
    ) -> CreateTermsTokenResponseContent:
        """创建条款令牌，供客户接受广告条款。"""
        resp = await self._request(
            "POST",
            "/termsTokens",
            json=request.model_dump(),
            headers=self._client_id_header(),
        )
        return self._response(CreateTermsTokenResponseContent, resp)

    async def get_status(
        self,
        terms_token: str,
    ) -> GetTermsTokenResponseContent:
        """查询条款令牌的状态。"""
        resp = await self._request(
            "GET",
            f"/termsTokens/{terms_token}",
            headers=self._client_id_header(),
        )
        return self._response(GetTermsTokenResponseContent, resp)
