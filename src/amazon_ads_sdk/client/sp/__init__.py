"""Sponsored Products async HTTP client."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import ClientContext
from amazon_ads_sdk.config import AmazonAdsConfig

from .ad_extensions import AdExtensions
from .ad_groups import AdGroups
from .ads import Ads
from .campaigns import Campaigns
from .targets import Targets


class SPClient:
    """Async HTTP client for Amazon Ads Sponsored Products API.

    Parameters
    ----------
    config : AmazonAdsConfig
        Client configuration (auth, region, timeouts, retries).
    """

    def __init__(self, config: AmazonAdsConfig) -> None:
        self._ctx = ClientContext(config)
        self.__campaign: Campaigns | None = None
        self.__ad_group: AdGroups | None = None
        self.__ad: Ads | None = None
        self.__target: Targets | None = None
        self.__ad_extension: AdExtensions | None = None

    async def __aenter__(self) -> SPClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        if self._ctx._client is not None:
            await self._ctx._client.aclose()
            self._ctx._client = None

    @property
    def campaigns(self) -> Campaigns:
        if self.__campaign is None:
            self.__campaign = Campaigns(self._ctx)
        return self.__campaign

    @property
    def ad_groups(self) -> AdGroups:
        if self.__ad_group is None:
            self.__ad_group = AdGroups(self._ctx)
        return self.__ad_group

    @property
    def ads(self) -> Ads:
        if self.__ad is None:
            self.__ad = Ads(self._ctx)
        return self.__ad

    @property
    def targets(self) -> Targets:
        if self.__target is None:
            self.__target = Targets(self._ctx)
        return self.__target

    @property
    def ad_extensions(self) -> AdExtensions:
        if self.__ad_extension is None:
            self.__ad_extension = AdExtensions(self._ctx)
        return self.__ad_extension
