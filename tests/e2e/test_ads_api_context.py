from __future__ import annotations

import httpx
import pytest

from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient

from .config import E2ESettings


def _query_body() -> dict[str, object]:
    return {"adProductFilter": {"include": ["SPONSORED_PRODUCTS"]}}


def _config_with_access_token(
    e2e_settings: E2ESettings,
    access_token: str,
    *,
    client_id: str | None = None,
    profile_id: str | None = None,
) -> AmazonAdsConfig:
    return AmazonAdsConfig(
        access_token=access_token,
        client_id=client_id or e2e_settings.client_id,
        profile_id=profile_id or e2e_settings.profile_id,
        region=Region.NA,
        endpoints={"na": e2e_settings.base_url},
        token_url=e2e_settings.token_url,
        timeout=e2e_settings.timeout,
    )


@pytest.mark.asyncio
async def test_ads_api_rejects_missing_client_id_header(
    e2e_settings: E2ESettings,
    access_token: str,
) -> None:
    async with httpx.AsyncClient(
        base_url=e2e_settings.base_url,
        timeout=e2e_settings.timeout,
        trust_env=False,
    ) as client:
        resp = await client.post(
            "/adsApi/v1/query/campaigns",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Amazon-Advertising-API-Scope": e2e_settings.profile_id,
            },
            json=_query_body(),
        )

    assert resp.status_code == 400
    assert resp.json() == {
        "code": "BAD_REQUEST",
        "message": "Amazon-Ads-ClientId header is required",
    }


@pytest.mark.asyncio
async def test_sp_campaigns_reject_client_id_mismatch(
    e2e_settings: E2ESettings,
    access_token: str,
) -> None:
    bad_config = _config_with_access_token(
        e2e_settings,
        access_token,
        client_id=f"{e2e_settings.client_id}.mismatch",
    )

    async with SPClient(bad_config) as sp_client:
        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            await sp_client.campaigns.query(_query_body())

    resp = exc_info.value.response
    assert resp.status_code == 401
    assert resp.json() == {
        "code": "UNAUTHORIZED",
        "message": "Amazon-Ads-ClientId does not match the access token",
    }


@pytest.mark.asyncio
async def test_sp_campaigns_reject_non_numeric_profile_scope(
    e2e_settings: E2ESettings,
    access_token: str,
) -> None:
    bad_config = _config_with_access_token(
        e2e_settings,
        access_token,
        profile_id="not-a-profile-id",
    )

    async with SPClient(bad_config) as sp_client:
        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            await sp_client.campaigns.query(_query_body())

    resp = exc_info.value.response
    assert resp.status_code == 400
    assert resp.json() == {
        "code": "BAD_REQUEST",
        "message": "Amazon-Advertising-API-Scope must be a profileId",
    }
