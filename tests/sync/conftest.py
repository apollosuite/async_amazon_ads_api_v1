from __future__ import annotations

from unittest.mock import MagicMock

import httpx
import pytest


@pytest.fixture
def sync_config():
    from ads_api.config.region import Region
    from ads_api.config.settings import AmazonAdsConfig

    return AmazonAdsConfig(
        access_token="test-token",
        client_id="test-client-id",
        region=Region.NA,
        profile_id="123456",
        account_id="amzn1.ads-account.test",
    )


@pytest.fixture
def mock_sync_client() -> MagicMock:
    client = MagicMock(spec=httpx.Client)
    client.request = MagicMock()
    return client


@pytest.fixture
def mock_response() -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = 200
    resp.is_error = False
    resp.content = b'{"dummy": "ok"}'
    resp.text = '{"dummy": "ok"}'
    resp.json.return_value = {"dummy": "ok"}
    return resp
