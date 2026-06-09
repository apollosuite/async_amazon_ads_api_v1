from __future__ import annotations

from collections.abc import AsyncGenerator
from uuid import uuid4

import httpx
import pytest
import pytest_asyncio

from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient

from .config import E2ESettings, load_settings


@pytest.fixture(scope="session")
def e2e_settings() -> E2ESettings:
    return load_settings()


@pytest.fixture(scope="session", autouse=True)
def require_ads_v1_server(e2e_settings: E2ESettings) -> None:
    try:
        resp = httpx.get(
            f"{e2e_settings.base_url}/health",
            timeout=e2e_settings.timeout,
            trust_env=False,
        )
    except httpx.HTTPError as exc:
        pytest.skip(f"ads_v1_server 不可用：{exc}")
    if resp.status_code != 200:
        pytest.skip(f"ads_v1_server /health 返回 {resp.status_code}: {resp.text}")


@pytest.fixture
def amazon_ads_config(e2e_settings: E2ESettings) -> AmazonAdsConfig:
    return AmazonAdsConfig(
        client_id=e2e_settings.client_id,
        client_secret=e2e_settings.client_secret,
        refresh_token=e2e_settings.refresh_token,
        profile_id=e2e_settings.profile_id,
        region=Region.NA,
        endpoints={"na": e2e_settings.base_url},
        token_url=e2e_settings.token_url,
        timeout=e2e_settings.timeout,
    )


@pytest_asyncio.fixture
async def sp_client(amazon_ads_config: AmazonAdsConfig) -> AsyncGenerator[SPClient]:
    async with SPClient(amazon_ads_config) as client:
        yield client


@pytest.fixture
def unique_name() -> str:
    return f"ads-v1-e2e-{uuid4()}"
