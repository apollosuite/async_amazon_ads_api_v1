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
        assert __version__ == "0.6.13"

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


class TestAdsApiExports:
    def test_version(self) -> None:
        import ads_api

        assert ads_api.__version__ == "0.1.0"

    def test_all(self) -> None:
        import ads_api

        assert set(ads_api.__all__) == {
            "AdsClient",
            "AdsClientV0",
            "AdsClientV1",
            "AmazonAdsConfig",
            "BaseTokenCache",
            "ClientContext",
            "FileTokenCache",
            "RedisTokenCache",
            "Region",
            "TokenCredentials",
            "TokenManager",
        }

    def test_imports(self) -> None:
        import ads_api

        assert ads_api.AdsClient is not None
        assert ads_api.AmazonAdsConfig is not None
        assert ads_api.Region is not None
        assert ads_api.TokenManager is not None
