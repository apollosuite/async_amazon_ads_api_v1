"""Pure async Amazon Ads API v1 client — Sponsored Products, Sponsored Brands, Sponsored Display."""

from async_amazon_ads_api_v1.client.sb import SBClient
from async_amazon_ads_api_v1.client.sd import SDClient
from async_amazon_ads_api_v1.client.sp import SPClient
from async_amazon_ads_api_v1.config.region import Region
from async_amazon_ads_api_v1.config.settings import AmazonAdsConfig

__all__ = ["AmazonAdsConfig", "Region", "SPClient", "SBClient", "SDClient"]
__version__ = "0.3.0"
