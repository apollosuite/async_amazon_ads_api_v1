"""DSP resource namespace — entity-specific clients."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_groups import DSPAdGroups
from .ads import DSPAds
from .campaigns import DSPCampaigns
from .targets import DSPTargets


class DSP:
    """Lazy entity-specific DSP resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_groups: DSPAdGroups | None = None
        self.__ads: DSPAds | None = None
        self.__campaigns: DSPCampaigns | None = None
        self.__targets: DSPTargets | None = None

    @property
    def ad_groups(self) -> DSPAdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = DSPAdGroups(self._ctx)
        return self.__ad_groups

    @property
    def ads(self) -> DSPAds:
        if self.__ads is None:
            self.__ads = DSPAds(self._ctx)
        return self.__ads

    @property
    def campaigns(self) -> DSPCampaigns:
        if self.__campaigns is None:
            self.__campaigns = DSPCampaigns(self._ctx)
        return self.__campaigns

    @property
    def targets(self) -> DSPTargets:
        if self.__targets is None:
            self.__targets = DSPTargets(self._ctx)
        return self.__targets
