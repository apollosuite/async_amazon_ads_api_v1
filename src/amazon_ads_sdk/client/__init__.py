"""Async HTTP client wrapping httpx."""

from __future__ import annotations

from typing import Any

import httpx

from amazon_ads_sdk.config import AmazonAdsConfig

from ._ad_extensions import AdExtensions
from ._ad_groups import AdGroups
from ._ads import Ads
from ._base import _AmazonAdsClientBase
from ._campaigns import Campaigns
from ._targets import Targets


class AmazonAdsClient(_AmazonAdsClientBase):
    """Async HTTP client for the Amazon Ads API.

    Parameters
    ----------
    config : AmazonAdsConfig
        Client configuration (auth, region, timeouts, retries).

    示例
    ----
    >>> config = AmazonAdsConfig(access_token="...", region=Region.NA)
    >>> async with AmazonAdsClient(config) as client:
    ...     result = await client.campaign.query({"stateFilter": {"include": ["enabled"]}})
    ...     for campaign in result.campaigns:
    ...         print(campaign.get("campaignId"))
    """

    def __init__(self, config: AmazonAdsConfig) -> None:
        self.config = config
        self._client: httpx.AsyncClient | None = None
        self._cached_profile_header: dict[str, str] | None = None
        self.__campaign: Campaigns | None = None
        self.__ad_group: AdGroups | None = None
        self.__ad: Ads | None = None
        self.__target: Targets | None = None
        self.__ad_extension: AdExtensions | None = None

    async def __aenter__(self) -> AmazonAdsClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    @property
    def campaign(self) -> Campaigns:
        """广告活动资源。"""
        if self.__campaign is None:
            self.__campaign = Campaigns(self)
        return self.__campaign

    @property
    def ad_group(self) -> AdGroups:
        """广告组资源。"""
        if self.__ad_group is None:
            self.__ad_group = AdGroups(self)
        return self.__ad_group

    @property
    def ad(self) -> Ads:
        """广告资源。"""
        if self.__ad is None:
            self.__ad = Ads(self)
        return self.__ad

    @property
    def target(self) -> Targets:
        """投放目标资源。"""
        if self.__target is None:
            self.__target = Targets(self)
        return self.__target

    @property
    def ad_extension(self) -> AdExtensions:
        """广告扩展资源。"""
        if self.__ad_extension is None:
            self.__ad_extension = AdExtensions(self)
        return self.__ad_extension
