from __future__ import annotations

from collections.abc import AsyncGenerator
from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest
import pytest_asyncio

from async_amazon_ads_api_v1._base import ClientContext
from async_amazon_ads_api_v1.config.region import Region
from async_amazon_ads_api_v1.config.settings import AmazonAdsConfig


@pytest.fixture
def config() -> AmazonAdsConfig:
    return AmazonAdsConfig(access_token="test-token", client_id="test-client-id", region=Region.NA)


@pytest_asyncio.fixture
async def ctx(config: AmazonAdsConfig) -> AsyncGenerator[ClientContext]:
    context = ClientContext(config)
    yield context
    if context._client is not None:
        await context._client.aclose()


@pytest.fixture
def mock_async_client() -> MagicMock:
    client = MagicMock(spec=httpx.AsyncClient)
    client.request = AsyncMock()
    return client


@pytest.fixture
def mock_response() -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = 200
    resp.content = b'{"dummy": "ok"}'
    return resp


def make_config(
    access_token: str = "test-token",
    client_id: str = "test-client-id",
    region: Region = Region.NA,
    *,
    profile_id: str | None = None,
    timeout: float = 60.0,
    max_retries: int = 3,
) -> AmazonAdsConfig:
    return AmazonAdsConfig(
        access_token=access_token,
        client_id=client_id,
        region=region,
        profile_id=profile_id,
        timeout=timeout,
        max_retries=max_retries,
    )
