from __future__ import annotations

from amazon_ads_sdk import (
    AmazonAdsConfig,
    Region,
    SBClient,
    SDClient,
    SPClient,
    __all__,
    __version__,
)


class TestExports:
    def test_version(self) -> None:
        assert __version__ == "0.3.0"

    def test_all(self) -> None:
        assert set(__all__) == {"AmazonAdsConfig", "Region", "SPClient", "SBClient", "SDClient"}

    def test_imports(self) -> None:
        assert AmazonAdsConfig is not None
        assert Region is not None
        assert SPClient is not None
        assert SBClient is not None
        assert SDClient is not None
