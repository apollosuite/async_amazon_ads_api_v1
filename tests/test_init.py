from __future__ import annotations

from async_amazon_ads_api_v1 import (
    AmazonAdsConfig,
    Region,
    SBClient,
    SDClient,
    SPClient,
    TokenCredentials,
    TokenManager,
    __all__,
    __version__,
)


class TestExports:
    def test_version(self) -> None:
        assert __version__ == "0.6.0"

    def test_all(self) -> None:
        assert set(__all__) == {
            "AmazonAdsConfig",
            "BaseTokenCache",
            "CacheBackend",
            "FileTokenCache",
            "RedisTokenCache",
            "Region",
            "SBClient",
            "SDClient",
            "SPClient",
            "TokenCredentials",
            "TokenManager",
            "close_all_redis",
        }

    def test_imports(self) -> None:
        assert AmazonAdsConfig is not None
        assert Region is not None
        assert SPClient is not None
        assert SBClient is not None
        assert SDClient is not None
        assert TokenManager is not None
        assert TokenCredentials is not None
