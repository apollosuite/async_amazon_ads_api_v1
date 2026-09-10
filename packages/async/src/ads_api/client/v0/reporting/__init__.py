"""Reporting resource namespace — v0 Reporting APIs."""

from __future__ import annotations

from ads_api.base import ClientContext

from .brand_benchmarks import BrandBenchmarks
from .brand_metrics import BrandMetrics
from .mmm_brand_group_overrides import MmmBrandGroupOverrides
from .mmm_brand_groups import MmmBrandGroups
from .mmm_reports import MmmReports
from .reports import Reports
from .store_insights import StoreInsights


class Reporting:
    """Lazy Reporting resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__brand_benchmarks: BrandBenchmarks | None = None
        self.__brand_metrics: BrandMetrics | None = None
        self.__mmm_brand_group_overrides: MmmBrandGroupOverrides | None = None
        self.__mmm_brand_groups: MmmBrandGroups | None = None
        self.__mmm_reports: MmmReports | None = None
        self.__reports: Reports | None = None
        self.__store_insights: StoreInsights | None = None

    @property
    def brand_benchmarks(self) -> BrandBenchmarks:
        if self.__brand_benchmarks is None:
            self.__brand_benchmarks = BrandBenchmarks(self._ctx)
        return self.__brand_benchmarks

    @property
    def brand_metrics(self) -> BrandMetrics:
        if self.__brand_metrics is None:
            self.__brand_metrics = BrandMetrics(self._ctx)
        return self.__brand_metrics

    @property
    def mmm_brand_group_overrides(self) -> MmmBrandGroupOverrides:
        if self.__mmm_brand_group_overrides is None:
            self.__mmm_brand_group_overrides = MmmBrandGroupOverrides(self._ctx)
        return self.__mmm_brand_group_overrides

    @property
    def mmm_brand_groups(self) -> MmmBrandGroups:
        if self.__mmm_brand_groups is None:
            self.__mmm_brand_groups = MmmBrandGroups(self._ctx)
        return self.__mmm_brand_groups

    @property
    def mmm_reports(self) -> MmmReports:
        if self.__mmm_reports is None:
            self.__mmm_reports = MmmReports(self._ctx)
        return self.__mmm_reports

    @property
    def reports(self) -> Reports:
        if self.__reports is None:
            self.__reports = Reports(self._ctx)
        return self.__reports

    @property
    def store_insights(self) -> StoreInsights:
        if self.__store_insights is None:
            self.__store_insights = StoreInsights(self._ctx)
        return self.__store_insights
