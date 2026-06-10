from __future__ import annotations

import os
import time
from pathlib import Path

import pytest
import pytest_asyncio

from async_amazon_ads_api_v1.config.token_cache import (
    BaseTokenCache,
    FileTokenCache,
    RedisTokenCache,
    _redis_clients,
    _TokenData,
)

REDIS_URL = os.environ.get("TEST_REDIS_URL", "redis://localhost:6379/0")
HAS_REDIS = os.environ.get("TEST_REDIS_URL") is not None


@pytest.fixture
def token_data() -> _TokenData:
    return _TokenData(
        access_token="test-access-token",
        expires_at=time.time() + 3600,
        refresh_token="test-refresh-token",
    )


@pytest.fixture
def file_cache(tmp_path: Path) -> FileTokenCache:
    return FileTokenCache(
        cache_dir=tmp_path,
        client_id="test-client",
        refresh_token="test-refresh",
    )


@pytest_asyncio.fixture
async def redis_cache() -> RedisTokenCache:
    # Clear global pool to avoid event loop conflicts
    _redis_clients.clear()
    cache = RedisTokenCache(
        redis_url=REDIS_URL,
        client_id="test-client",
        refresh_token="test-refresh",
    )
    await cache._client.flushdb()
    yield cache
    await cache._client.aclose()
    _redis_clients.clear()


@pytest.mark.asyncio
class TestFileTokenCache:
    async def test_read_empty_cache(self, file_cache: FileTokenCache) -> None:
        result = await file_cache.read()
        assert result is None

    async def test_write_and_read(self, file_cache: FileTokenCache, token_data: _TokenData) -> None:
        await file_cache.write(token_data)
        result = await file_cache.read()
        assert result is not None
        assert result.access_token == token_data.access_token
        assert result.expires_at == token_data.expires_at
        assert result.refresh_token == token_data.refresh_token

    async def test_overwrite(self, file_cache: FileTokenCache) -> None:
        data1 = _TokenData(access_token="token-1", expires_at=time.time() + 100, refresh_token="rt1")
        data2 = _TokenData(access_token="token-2", expires_at=time.time() + 200, refresh_token="rt2")

        await file_cache.write(data1)
        await file_cache.write(data2)

        result = await file_cache.read()
        assert result is not None
        assert result.access_token == "token-2"

    async def test_corrupted_file_returns_none(self, file_cache: FileTokenCache) -> None:
        file_cache._cache_file.parent.mkdir(parents=True, exist_ok=True)
        file_cache._cache_file.write_text("not valid json", encoding="utf-8")
        result = await file_cache.read()
        assert result is None

    async def test_missing_fields_returns_none(self, file_cache: FileTokenCache) -> None:
        import json

        file_cache._cache_file.parent.mkdir(parents=True, exist_ok=True)
        file_cache._cache_file.write_text(json.dumps({"foo": "bar"}), encoding="utf-8")
        result = await file_cache.read()
        assert result is None

    async def test_different_credentials_different_files(self, tmp_path: Path) -> None:
        cache1 = FileTokenCache(cache_dir=tmp_path, client_id="client1", refresh_token="rt1")
        cache2 = FileTokenCache(cache_dir=tmp_path, client_id="client2", refresh_token="rt2")

        data = _TokenData(access_token="tok", expires_at=time.time() + 100, refresh_token="rt")
        await cache1.write(data)

        assert await cache1.read() is not None
        assert await cache2.read() is None


@pytest.mark.asyncio
@pytest.mark.skipif(not HAS_REDIS, reason="TEST_REDIS_URL not set")
class TestRedisTokenCache:
    async def test_read_empty_cache(self, redis_cache: RedisTokenCache) -> None:
        result = await redis_cache.read()
        assert result is None

    async def test_write_and_read(self, redis_cache: RedisTokenCache, token_data: _TokenData) -> None:
        await redis_cache.write(token_data)
        result = await redis_cache.read()
        assert result is not None
        assert result.access_token == token_data.access_token
        assert result.expires_at == token_data.expires_at
        assert result.refresh_token == token_data.refresh_token

    async def test_ttl_based_on_expires_at(self, redis_cache: RedisTokenCache) -> None:
        data = _TokenData(
            access_token="tok",
            expires_at=time.time() + 60,
            refresh_token="rt",
        )
        await redis_cache.write(data)
        ttl = await redis_cache._client.ttl(redis_cache._key)
        assert 50 <= ttl <= 60

    async def test_expired_token_not_written(self, redis_cache: RedisTokenCache) -> None:
        data = _TokenData(
            access_token="tok",
            expires_at=time.time() - 10,
            refresh_token="rt",
        )
        await redis_cache.write(data)
        result = await redis_cache.read()
        assert result is None

    async def test_overwrite(self, redis_cache: RedisTokenCache) -> None:
        data1 = _TokenData(access_token="token-1", expires_at=time.time() + 100, refresh_token="rt1")
        data2 = _TokenData(access_token="token-2", expires_at=time.time() + 200, refresh_token="rt2")

        await redis_cache.write(data1)
        await redis_cache.write(data2)

        result = await redis_cache.read()
        assert result is not None
        assert result.access_token == "token-2"

    async def test_different_credentials_different_keys(self, redis_cache: RedisTokenCache) -> None:
        cache2 = RedisTokenCache(redis_url=REDIS_URL, client_id="c2", refresh_token="rt2")

        data = _TokenData(access_token="tok", expires_at=time.time() + 100, refresh_token="rt")
        await redis_cache.write(data)

        assert await redis_cache.read() is not None
        assert await cache2.read() is None

    async def test_shared_connection(self, redis_cache: RedisTokenCache) -> None:
        """Multiple instances with same URL share the same Redis client."""
        cache2 = RedisTokenCache(redis_url=REDIS_URL, client_id="c2", refresh_token="rt2")
        assert redis_cache._client is cache2._client


class TestBaseTokenCache:
    def test_cannot_instantiate_abstract(self) -> None:
        with pytest.raises(TypeError):
            BaseTokenCache()  # type: ignore[abstract]
