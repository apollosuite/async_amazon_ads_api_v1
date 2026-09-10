from __future__ import annotations

import os
import sys
from collections.abc import AsyncGenerator
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

_async_src = str(Path(__file__).resolve().parents[1] / "packages" / "async" / "src")
_sync_src = str(Path(__file__).resolve().parents[1] / "packages" / "sync" / "src")

if os.environ.get("TESTING_SYNC") == "1":
    if _async_src in sys.path:
        sys.path.remove(_async_src)
    if _sync_src in sys.path:
        sys.path.remove(_sync_src)
    sys.path.insert(0, _sync_src)
else:
    if _sync_src in sys.path:
        sys.path.remove(_sync_src)
    if _async_src in sys.path:
        sys.path.remove(_async_src)
    sys.path.insert(0, _async_src)

# Clear any cached ads_api modules to ensure clean import
for _mod in list(sys.modules.keys()):
    if _mod == "ads_api" or _mod.startswith("ads_api."):
        del sys.modules[_mod]

import httpx
import pytest
import pytest_asyncio

from ads_api.base import ClientContext
from ads_api.config.region import Region
from ads_api.config.settings import AmazonAdsConfig


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
