"""SP resource namespace — entity-specific clients."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_extensions import SPAdExtensions
from .ad_groups import SPAdGroups
from .ads import SPAds
from .campaigns import SPCampaigns
from .targets import SPTargets


class SP:
    """Lazy entity-specific SP resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_extensions: SPAdExtensions | None = None
        self.__ad_groups: SPAdGroups | None = None
        self.__ads: SPAds | None = None
        self.__campaigns: SPCampaigns | None = None
        self.__targets: SPTargets | None = None

    @property
    def ad_extensions(self) -> SPAdExtensions:
        if self.__ad_extensions is None:
            self.__ad_extensions = SPAdExtensions(self._ctx)
        return self.__ad_extensions

    @property
    def ad_groups(self) -> SPAdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = SPAdGroups(self._ctx)
        return self.__ad_groups

    @property
    def ads(self) -> SPAds:
        if self.__ads is None:
            self.__ads = SPAds(self._ctx)
        return self.__ads

    @property
    def campaigns(self) -> SPCampaigns:
        if self.__campaigns is None:
            self.__campaigns = SPCampaigns(self._ctx)
        return self.__campaigns

    @property
    def targets(self) -> SPTargets:
        if self.__targets is None:
            self.__targets = SPTargets(self._ctx)
        return self.__targets
