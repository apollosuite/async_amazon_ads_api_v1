from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import httpx
import pytest

from ads_api.config.settings import AmazonAdsConfig
from ads_api.config.token_cache import FileTokenCache, TokenData
from ads_api.config.token_manager import TokenCredentials, TokenManager
from ads_api.errors import InvalidGrantError, TokenRefreshError


def test_file_token_cache_sync() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        cache = FileTokenCache(Path(tmp_dir), "client_1", "refresh_1")
        assert cache.read() is None

        data = TokenData(access_token="token_abc", expires_at=9999999999.0)
        cache.write(data)

        loaded = cache.read()
        assert loaded is not None
        assert loaded.access_token == "token_abc"
        assert loaded.expires_at == 9999999999.0
        cache.close()


def test_sync_token_manager_refresh_success() -> None:
    creds = TokenCredentials(
        client_id="test_client",
        client_secret="test_secret",
        refresh_token="test_refresh",
    )
    manager = TokenManager(credentials=creds)

    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 200
    mock_resp.is_error = False
    mock_resp.json.return_value = {
        "access_token": "new_access_token",
        "expires_in": 3600,
    }

    with patch("httpx.Client.post", return_value=mock_resp):
        token = manager.get_access_token(force=True)
        assert token == "new_access_token"
        assert manager.access_token == "new_access_token"

        # Second call should use in-memory cached token without HTTP request
        with patch("httpx.Client.post") as post_again:
            cached = manager.get_access_token()
            assert cached == "new_access_token"
            post_again.assert_not_called()


def test_sync_token_manager_invalid_grant() -> None:
    creds = TokenCredentials(
        client_id="test_client",
        client_secret="test_secret",
        refresh_token="revoked_token",
    )
    manager = TokenManager(credentials=creds)

    mock_resp = httpx.Response(
        status_code=400,
        json={
            "error": "invalid_grant",
            "error_description": "The request has an invalid grant parameter : refresh_token.",
        },
        request=httpx.Request("POST", "https://api.amazon.com/auth/o2/token"),
    )

    err_400 = httpx.HTTPStatusError("400", request=mock_resp.request, response=mock_resp)
    with patch("httpx.Client.post", side_effect=err_400):
        with pytest.raises(InvalidGrantError) as exc_info:
            manager.get_access_token(force=True)
        assert exc_info.value.status_code == 400
        assert exc_info.value.error_code == "invalid_grant"


def test_sync_token_manager_other_error() -> None:
    creds = TokenCredentials(
        client_id="test_client",
        client_secret="test_secret",
        refresh_token="test_token",
    )
    manager = TokenManager(credentials=creds)

    mock_resp = httpx.Response(
        status_code=500,
        text="Internal Server Error",
        request=httpx.Request("POST", "https://api.amazon.com/auth/o2/token"),
    )

    err_500 = httpx.HTTPStatusError("500", request=mock_resp.request, response=mock_resp)
    with patch("httpx.Client.post", side_effect=err_500):
        with pytest.raises(TokenRefreshError) as exc_info:
            manager.get_access_token(force=True)
        assert exc_info.value.status_code == 500


def test_sync_config_refresh_access_token() -> None:
    config = AmazonAdsConfig(
        client_id="test-client-id",
        refresh_token="test-refresh-token",
        client_secret="test-client-secret",
    )
    assert config._token_manager is not None

    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 200
    mock_resp.is_error = False
    mock_resp.json.return_value = {
        "access_token": "token_from_refresh",
        "expires_in": 3600,
    }

    with patch("httpx.Client.post", return_value=mock_resp):
        token = config.refresh_access_token()
        assert token == "token_from_refresh"
        assert config.access_token == "token_from_refresh"
