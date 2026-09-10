"""DSP resource namespace — entity-specific clients."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_associations import DSPAdAssociations
from .ad_groups import DSPAdGroups
from .ads import DSPAds
from .campaign_forecasts import DSPCampaignForecasts
from .campaigns import DSPCampaigns
from .commitment_spends import DSPCommitmentSpends
from .commitments import DSPCommitments
from .deal_preferences import DSPDealPreferences
from .geo_locations import DSPGeoLocations
from .location_indexes import DSPLocationIndexes
from .supplier_ad_product_prices import DSPSupplierAdProductPrices
from .supplier_ad_products import DSPSupplierAdProducts
from .supplier_proposal_destinations import DSPSupplierProposalDestinations
from .supplier_proposals import DSPSupplierProposals
from .supplier_proposed_deal_forecasts import DSPSupplierProposedDealForecasts
from .supplier_proposed_deal_historical_versions import DSPSupplierProposedDealHistoricalVersions
from .supplier_proposed_deal_revisions import DSPSupplierProposedDealRevisions
from .supplier_proposed_deals import DSPSupplierProposedDeals
from .supplier_publishers import DSPSupplierPublishers
from .supplier_target_items import DSPSupplierTargetItems
from .targets import DSPTargets


class DSP:
    """Lazy entity-specific DSP resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_associations: DSPAdAssociations | None = None
        self.__ad_groups: DSPAdGroups | None = None
        self.__ads: DSPAds | None = None
        self.__campaign_forecasts: DSPCampaignForecasts | None = None
        self.__campaigns: DSPCampaigns | None = None
        self.__commitment_spends: DSPCommitmentSpends | None = None
        self.__commitments: DSPCommitments | None = None
        self.__deal_preferences: DSPDealPreferences | None = None
        self.__geo_locations: DSPGeoLocations | None = None
        self.__location_indexes: DSPLocationIndexes | None = None
        self.__supplier_ad_product_prices: DSPSupplierAdProductPrices | None = None
        self.__supplier_ad_products: DSPSupplierAdProducts | None = None
        self.__supplier_proposal_destinations: DSPSupplierProposalDestinations | None = None
        self.__supplier_proposals: DSPSupplierProposals | None = None
        self.__supplier_proposed_deal_forecasts: DSPSupplierProposedDealForecasts | None = None
        self.__supplier_proposed_deal_historical_versions: DSPSupplierProposedDealHistoricalVersions | None = None
        self.__supplier_proposed_deal_revisions: DSPSupplierProposedDealRevisions | None = None
        self.__supplier_proposed_deals: DSPSupplierProposedDeals | None = None
        self.__supplier_publishers: DSPSupplierPublishers | None = None
        self.__supplier_target_items: DSPSupplierTargetItems | None = None
        self.__targets: DSPTargets | None = None

    @property
    def ad_associations(self) -> DSPAdAssociations:
        if self.__ad_associations is None:
            self.__ad_associations = DSPAdAssociations(self._ctx)
        return self.__ad_associations

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
    def campaign_forecasts(self) -> DSPCampaignForecasts:
        if self.__campaign_forecasts is None:
            self.__campaign_forecasts = DSPCampaignForecasts(self._ctx)
        return self.__campaign_forecasts

    @property
    def campaigns(self) -> DSPCampaigns:
        if self.__campaigns is None:
            self.__campaigns = DSPCampaigns(self._ctx)
        return self.__campaigns

    @property
    def commitment_spends(self) -> DSPCommitmentSpends:
        if self.__commitment_spends is None:
            self.__commitment_spends = DSPCommitmentSpends(self._ctx)
        return self.__commitment_spends

    @property
    def commitments(self) -> DSPCommitments:
        if self.__commitments is None:
            self.__commitments = DSPCommitments(self._ctx)
        return self.__commitments

    @property
    def deal_preferences(self) -> DSPDealPreferences:
        if self.__deal_preferences is None:
            self.__deal_preferences = DSPDealPreferences(self._ctx)
        return self.__deal_preferences

    @property
    def geo_locations(self) -> DSPGeoLocations:
        if self.__geo_locations is None:
            self.__geo_locations = DSPGeoLocations(self._ctx)
        return self.__geo_locations

    @property
    def location_indexes(self) -> DSPLocationIndexes:
        if self.__location_indexes is None:
            self.__location_indexes = DSPLocationIndexes(self._ctx)
        return self.__location_indexes

    @property
    def supplier_ad_product_prices(self) -> DSPSupplierAdProductPrices:
        if self.__supplier_ad_product_prices is None:
            self.__supplier_ad_product_prices = DSPSupplierAdProductPrices(self._ctx)
        return self.__supplier_ad_product_prices

    @property
    def supplier_ad_products(self) -> DSPSupplierAdProducts:
        if self.__supplier_ad_products is None:
            self.__supplier_ad_products = DSPSupplierAdProducts(self._ctx)
        return self.__supplier_ad_products

    @property
    def supplier_proposal_destinations(self) -> DSPSupplierProposalDestinations:
        if self.__supplier_proposal_destinations is None:
            self.__supplier_proposal_destinations = DSPSupplierProposalDestinations(self._ctx)
        return self.__supplier_proposal_destinations

    @property
    def supplier_proposals(self) -> DSPSupplierProposals:
        if self.__supplier_proposals is None:
            self.__supplier_proposals = DSPSupplierProposals(self._ctx)
        return self.__supplier_proposals

    @property
    def supplier_proposed_deal_forecasts(self) -> DSPSupplierProposedDealForecasts:
        if self.__supplier_proposed_deal_forecasts is None:
            self.__supplier_proposed_deal_forecasts = DSPSupplierProposedDealForecasts(self._ctx)
        return self.__supplier_proposed_deal_forecasts

    @property
    def supplier_proposed_deal_historical_versions(self) -> DSPSupplierProposedDealHistoricalVersions:
        if self.__supplier_proposed_deal_historical_versions is None:
            self.__supplier_proposed_deal_historical_versions = DSPSupplierProposedDealHistoricalVersions(self._ctx)
        return self.__supplier_proposed_deal_historical_versions

    @property
    def supplier_proposed_deal_revisions(self) -> DSPSupplierProposedDealRevisions:
        if self.__supplier_proposed_deal_revisions is None:
            self.__supplier_proposed_deal_revisions = DSPSupplierProposedDealRevisions(self._ctx)
        return self.__supplier_proposed_deal_revisions

    @property
    def supplier_proposed_deals(self) -> DSPSupplierProposedDeals:
        if self.__supplier_proposed_deals is None:
            self.__supplier_proposed_deals = DSPSupplierProposedDeals(self._ctx)
        return self.__supplier_proposed_deals

    @property
    def supplier_publishers(self) -> DSPSupplierPublishers:
        if self.__supplier_publishers is None:
            self.__supplier_publishers = DSPSupplierPublishers(self._ctx)
        return self.__supplier_publishers

    @property
    def supplier_target_items(self) -> DSPSupplierTargetItems:
        if self.__supplier_target_items is None:
            self.__supplier_target_items = DSPSupplierTargetItems(self._ctx)
        return self.__supplier_target_items

    @property
    def targets(self) -> DSPTargets:
        if self.__targets is None:
            self.__targets = DSPTargets(self._ctx)
        return self.__targets
