"""Amazon Ads API v1 async client."""

from __future__ import annotations

from typing import Any, overload

from ads_api.base import ClientContext
from ads_api.client.v1.ad_associations import AdAssociations
from ads_api.client.v1.advertiser_accounts import AdvertiserAccounts
from ads_api.client.v1.advertising_deal_targets import AdvertisingDealTargets
from ads_api.client.v1.advertising_deals import AdvertisingDeals
from ads_api.client.v1.brand_store_edition_publish_versions import BrandStoreEditionPublishVersions
from ads_api.client.v1.brand_store_editions import BrandStoreEditions
from ads_api.client.v1.brand_store_pages import BrandStorePages
from ads_api.client.v1.brand_stores import BrandStores
from ads_api.client.v1.branded_keywords_pricings import BrandedKeywordsPricings
from ads_api.client.v1.campaign_forecasts import CampaignForecasts
from ads_api.client.v1.commitment_spends import CommitmentSpends
from ads_api.client.v1.commitments import Commitments
from ads_api.client.v1.deal_preferences import DealPreferences
from ads_api.client.v1.dsp import DSP
from ads_api.client.v1.geo_locations import GeoLocations
from ads_api.client.v1.keyword_reservation_validations import KeywordReservationValidations
from ads_api.client.v1.location_indexes import LocationIndexes
from ads_api.client.v1.manager_accounts import ManagerAccounts
from ads_api.client.v1.recommendation_types import RecommendationTypes
from ads_api.client.v1.recommendations import Recommendations
from ads_api.client.v1.reserved_target_pricings import ReservedTargetPricings
from ads_api.client.v1.sb import SB
from ads_api.client.v1.sd import SD
from ads_api.client.v1.selling_accounts import SellingAccounts
from ads_api.client.v1.sp import SP
from ads_api.client.v1.sp_global import SPGlobal
from ads_api.client.v1.st import ST
from ads_api.client.v1.supplier_ad_product_prices import SupplierAdProductPrices
from ads_api.client.v1.supplier_ad_products import SupplierAdProducts
from ads_api.client.v1.supplier_proposal_destinations import SupplierProposalDestinations
from ads_api.client.v1.supplier_proposals import SupplierProposals
from ads_api.client.v1.supplier_proposed_deal_forecasts import SupplierProposedDealForecasts
from ads_api.client.v1.supplier_proposed_deal_historical_versions import SupplierProposedDealHistoricalVersions
from ads_api.client.v1.supplier_proposed_deal_revisions import SupplierProposedDealRevisions
from ads_api.client.v1.supplier_proposed_deals import SupplierProposedDeals
from ads_api.client.v1.supplier_publishers import SupplierPublishers
from ads_api.client.v1.supplier_target_items import SupplierTargetItems
from ads_api.config.settings import AmazonAdsConfig
from ads_api.errors import MissingConfigError


class AdsClientV1:
    """Async client for Amazon Ads API v1.

    Ad products are nested; unscoped APIs hang off the client:

        async with AdsClientV1(config) as ads:
            await ads.sp.campaigns.create_campaign(body)
            await ads.selling_accounts.query_selling_account(body)
    """

    @overload
    def __init__(self, config: AmazonAdsConfig) -> None: ...

    @overload
    def __init__(self, *, ctx: ClientContext) -> None: ...

    def __init__(
        self,
        config: AmazonAdsConfig | None = None,
        *,
        ctx: ClientContext | None = None,
    ) -> None:
        if ctx is not None:
            self._ctx = ctx
            self._owns_ctx = False
        elif config is not None:
            self._ctx = ClientContext(config)
            self._owns_ctx = True
        else:
            raise MissingConfigError()
        self.__sp: SP | None = None
        self.__sp_global: SPGlobal | None = None
        self.__sb: SB | None = None
        self.__sd: SD | None = None
        self.__dsp: DSP | None = None
        self.__st: ST | None = None
        self.__ad_associations: AdAssociations | None = None
        self.__advertiser_accounts: AdvertiserAccounts | None = None
        self.__advertising_deal_targets: AdvertisingDealTargets | None = None
        self.__advertising_deals: AdvertisingDeals | None = None
        self.__brand_store_edition_publish_versions: BrandStoreEditionPublishVersions | None = None
        self.__brand_store_editions: BrandStoreEditions | None = None
        self.__brand_store_pages: BrandStorePages | None = None
        self.__brand_stores: BrandStores | None = None
        self.__branded_keywords_pricings: BrandedKeywordsPricings | None = None
        self.__campaign_forecasts: CampaignForecasts | None = None
        self.__commitment_spends: CommitmentSpends | None = None
        self.__commitments: Commitments | None = None
        self.__deal_preferences: DealPreferences | None = None
        self.__geo_locations: GeoLocations | None = None
        self.__keyword_reservation_validations: KeywordReservationValidations | None = None
        self.__location_indexes: LocationIndexes | None = None
        self.__manager_accounts: ManagerAccounts | None = None
        self.__recommendation_types: RecommendationTypes | None = None
        self.__recommendations: Recommendations | None = None
        self.__reserved_target_pricings: ReservedTargetPricings | None = None
        self.__selling_accounts: SellingAccounts | None = None
        self.__supplier_ad_product_prices: SupplierAdProductPrices | None = None
        self.__supplier_ad_products: SupplierAdProducts | None = None
        self.__supplier_proposal_destinations: SupplierProposalDestinations | None = None
        self.__supplier_proposals: SupplierProposals | None = None
        self.__supplier_proposed_deal_forecasts: SupplierProposedDealForecasts | None = None
        self.__supplier_proposed_deal_historical_versions: SupplierProposedDealHistoricalVersions | None = None
        self.__supplier_proposed_deal_revisions: SupplierProposedDealRevisions | None = None
        self.__supplier_proposed_deals: SupplierProposedDeals | None = None
        self.__supplier_publishers: SupplierPublishers | None = None
        self.__supplier_target_items: SupplierTargetItems | None = None

    async def __aenter__(self) -> AdsClientV1:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        if self._owns_ctx:
            await self._ctx.close()

    @property
    def sp(self) -> SP:
        if self.__sp is None:
            self.__sp = SP(self._ctx)
        return self.__sp

    @property
    def sp_global(self) -> SPGlobal:
        if self.__sp_global is None:
            self.__sp_global = SPGlobal(self._ctx)
        return self.__sp_global

    @property
    def sb(self) -> SB:
        if self.__sb is None:
            self.__sb = SB(self._ctx)
        return self.__sb

    @property
    def sd(self) -> SD:
        if self.__sd is None:
            self.__sd = SD(self._ctx)
        return self.__sd

    @property
    def dsp(self) -> DSP:
        if self.__dsp is None:
            self.__dsp = DSP(self._ctx)
        return self.__dsp

    @property
    def st(self) -> ST:
        if self.__st is None:
            self.__st = ST(self._ctx)
        return self.__st

    @property
    def ad_associations(self) -> AdAssociations:
        if self.__ad_associations is None:
            self.__ad_associations = AdAssociations(self._ctx)
        return self.__ad_associations

    @property
    def advertiser_accounts(self) -> AdvertiserAccounts:
        if self.__advertiser_accounts is None:
            self.__advertiser_accounts = AdvertiserAccounts(self._ctx)
        return self.__advertiser_accounts

    @property
    def advertising_deal_targets(self) -> AdvertisingDealTargets:
        if self.__advertising_deal_targets is None:
            self.__advertising_deal_targets = AdvertisingDealTargets(self._ctx)
        return self.__advertising_deal_targets

    @property
    def advertising_deals(self) -> AdvertisingDeals:
        if self.__advertising_deals is None:
            self.__advertising_deals = AdvertisingDeals(self._ctx)
        return self.__advertising_deals

    @property
    def brand_store_edition_publish_versions(self) -> BrandStoreEditionPublishVersions:
        if self.__brand_store_edition_publish_versions is None:
            self.__brand_store_edition_publish_versions = BrandStoreEditionPublishVersions(self._ctx)
        return self.__brand_store_edition_publish_versions

    @property
    def brand_store_editions(self) -> BrandStoreEditions:
        if self.__brand_store_editions is None:
            self.__brand_store_editions = BrandStoreEditions(self._ctx)
        return self.__brand_store_editions

    @property
    def brand_store_pages(self) -> BrandStorePages:
        if self.__brand_store_pages is None:
            self.__brand_store_pages = BrandStorePages(self._ctx)
        return self.__brand_store_pages

    @property
    def brand_stores(self) -> BrandStores:
        if self.__brand_stores is None:
            self.__brand_stores = BrandStores(self._ctx)
        return self.__brand_stores

    @property
    def branded_keywords_pricings(self) -> BrandedKeywordsPricings:
        if self.__branded_keywords_pricings is None:
            self.__branded_keywords_pricings = BrandedKeywordsPricings(self._ctx)
        return self.__branded_keywords_pricings

    @property
    def campaign_forecasts(self) -> CampaignForecasts:
        if self.__campaign_forecasts is None:
            self.__campaign_forecasts = CampaignForecasts(self._ctx)
        return self.__campaign_forecasts

    @property
    def commitment_spends(self) -> CommitmentSpends:
        if self.__commitment_spends is None:
            self.__commitment_spends = CommitmentSpends(self._ctx)
        return self.__commitment_spends

    @property
    def commitments(self) -> Commitments:
        if self.__commitments is None:
            self.__commitments = Commitments(self._ctx)
        return self.__commitments

    @property
    def deal_preferences(self) -> DealPreferences:
        if self.__deal_preferences is None:
            self.__deal_preferences = DealPreferences(self._ctx)
        return self.__deal_preferences

    @property
    def geo_locations(self) -> GeoLocations:
        if self.__geo_locations is None:
            self.__geo_locations = GeoLocations(self._ctx)
        return self.__geo_locations

    @property
    def keyword_reservation_validations(self) -> KeywordReservationValidations:
        if self.__keyword_reservation_validations is None:
            self.__keyword_reservation_validations = KeywordReservationValidations(self._ctx)
        return self.__keyword_reservation_validations

    @property
    def location_indexes(self) -> LocationIndexes:
        if self.__location_indexes is None:
            self.__location_indexes = LocationIndexes(self._ctx)
        return self.__location_indexes

    @property
    def manager_accounts(self) -> ManagerAccounts:
        if self.__manager_accounts is None:
            self.__manager_accounts = ManagerAccounts(self._ctx)
        return self.__manager_accounts

    @property
    def recommendation_types(self) -> RecommendationTypes:
        if self.__recommendation_types is None:
            self.__recommendation_types = RecommendationTypes(self._ctx)
        return self.__recommendation_types

    @property
    def recommendations(self) -> Recommendations:
        if self.__recommendations is None:
            self.__recommendations = Recommendations(self._ctx)
        return self.__recommendations

    @property
    def reserved_target_pricings(self) -> ReservedTargetPricings:
        if self.__reserved_target_pricings is None:
            self.__reserved_target_pricings = ReservedTargetPricings(self._ctx)
        return self.__reserved_target_pricings

    @property
    def selling_accounts(self) -> SellingAccounts:
        if self.__selling_accounts is None:
            self.__selling_accounts = SellingAccounts(self._ctx)
        return self.__selling_accounts

    @property
    def supplier_ad_product_prices(self) -> SupplierAdProductPrices:
        if self.__supplier_ad_product_prices is None:
            self.__supplier_ad_product_prices = SupplierAdProductPrices(self._ctx)
        return self.__supplier_ad_product_prices

    @property
    def supplier_ad_products(self) -> SupplierAdProducts:
        if self.__supplier_ad_products is None:
            self.__supplier_ad_products = SupplierAdProducts(self._ctx)
        return self.__supplier_ad_products

    @property
    def supplier_proposal_destinations(self) -> SupplierProposalDestinations:
        if self.__supplier_proposal_destinations is None:
            self.__supplier_proposal_destinations = SupplierProposalDestinations(self._ctx)
        return self.__supplier_proposal_destinations

    @property
    def supplier_proposals(self) -> SupplierProposals:
        if self.__supplier_proposals is None:
            self.__supplier_proposals = SupplierProposals(self._ctx)
        return self.__supplier_proposals

    @property
    def supplier_proposed_deal_forecasts(self) -> SupplierProposedDealForecasts:
        if self.__supplier_proposed_deal_forecasts is None:
            self.__supplier_proposed_deal_forecasts = SupplierProposedDealForecasts(self._ctx)
        return self.__supplier_proposed_deal_forecasts

    @property
    def supplier_proposed_deal_historical_versions(self) -> SupplierProposedDealHistoricalVersions:
        if self.__supplier_proposed_deal_historical_versions is None:
            self.__supplier_proposed_deal_historical_versions = SupplierProposedDealHistoricalVersions(self._ctx)
        return self.__supplier_proposed_deal_historical_versions

    @property
    def supplier_proposed_deal_revisions(self) -> SupplierProposedDealRevisions:
        if self.__supplier_proposed_deal_revisions is None:
            self.__supplier_proposed_deal_revisions = SupplierProposedDealRevisions(self._ctx)
        return self.__supplier_proposed_deal_revisions

    @property
    def supplier_proposed_deals(self) -> SupplierProposedDeals:
        if self.__supplier_proposed_deals is None:
            self.__supplier_proposed_deals = SupplierProposedDeals(self._ctx)
        return self.__supplier_proposed_deals

    @property
    def supplier_publishers(self) -> SupplierPublishers:
        if self.__supplier_publishers is None:
            self.__supplier_publishers = SupplierPublishers(self._ctx)
        return self.__supplier_publishers

    @property
    def supplier_target_items(self) -> SupplierTargetItems:
        if self.__supplier_target_items is None:
            self.__supplier_target_items = SupplierTargetItems(self._ctx)
        return self.__supplier_target_items
