"""Async HTTP client wrapping httpx."""

from __future__ import annotations

from typing import Any

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
    ...     resp = await client.campaign.query({"stateFilter": {"include": ["enabled"]}})
    ...     print(resp.json())
    """

    _campaign: Campaigns | None = None
    _ad_group: AdGroups | None = None
    _ad: Ads | None = None
    _target: Targets | None = None
    _ad_extension: AdExtensions | None = None

    def __init__(self, config: AmazonAdsConfig) -> None:
        self.config = config
        self._client: Any = None

    async def __aenter__(self) -> AmazonAdsClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    @property
    def campaign(self) -> Campaigns:
        """广告活动资源。"""
        if self._campaign is None:
            self._campaign = Campaigns(self._request)
        return self._campaign

    @property
    def ad_group(self) -> AdGroups:
        """广告组资源。"""
        if self._ad_group is None:
            self._ad_group = AdGroups(self._request)
        return self._ad_group

    @property
    def ad(self) -> Ads:
        """广告资源。"""
        if self._ad is None:
            self._ad = Ads(self._request)
        return self._ad

    @property
    def target(self) -> Targets:
        """投放目标资源。"""
        if self._target is None:
            self._target = Targets(self._request)
        return self._target

    @property
    def ad_extension(self) -> AdExtensions:
        """广告扩展资源。"""
        if self._ad_extension is None:
            self._ad_extension = AdExtensions(self._request)
        return self._ad_extension
