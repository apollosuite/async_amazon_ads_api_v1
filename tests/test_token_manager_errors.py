"""Unit tests for TokenManager error handling and InvalidGrantError."""

from unittest.mock import AsyncMock, patch

import httpx
import pytest

from ads_api.config.token_manager import TokenCredentials, TokenManager
from ads_api.errors import InvalidGrantError, TokenRefreshError


@pytest.mark.asyncio
async def test_token_manager_refresh_invalid_grant():
    creds = TokenCredentials(
        client_id="test_client",
        client_secret="test_secret",
        refresh_token="revoked_token",
    )
    manager = TokenManager(credentials=creds)

    mock_response = httpx.Response(
        status_code=400,
        json={
            "error": "invalid_grant",
            "error_description": (
                "The request has an invalid grant parameter : refresh_token. "
                "User may have revoked or didn't grant the permission."
            ),
        },
        request=httpx.Request("POST", "https://api.amazon.com/auth/o2/token"),
    )

    with patch("httpx.AsyncClient.post", AsyncMock(return_value=mock_response)):
        with pytest.raises(InvalidGrantError) as exc_info:
            await manager.get_access_token(force=True)

        err = exc_info.value
        assert err.status_code == 400
        assert err.error_code == "invalid_grant"
        assert "invalid_grant" in str(err)
        assert isinstance(err, TokenRefreshError)


@pytest.mark.asyncio
async def test_token_manager_refresh_other_error():
    creds = TokenCredentials(
        client_id="test_client",
        client_secret="test_secret",
        refresh_token="test_token",
    )
    manager = TokenManager(credentials=creds)

    mock_response = httpx.Response(
        status_code=500,
        text="Internal Server Error",
        request=httpx.Request("POST", "https://api.amazon.com/auth/o2/token"),
    )

    with patch("httpx.AsyncClient.post", AsyncMock(return_value=mock_response)):
        with pytest.raises(TokenRefreshError) as exc_info:
            await manager.get_access_token(force=True)

        err = exc_info.value
        assert err.status_code == 500
        assert not isinstance(err, InvalidGrantError)
