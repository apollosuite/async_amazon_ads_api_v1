from __future__ import annotations

import inspect
from unittest.mock import MagicMock, patch

import httpx

from ads_api import AdsClient, AdsClientV0, AdsClientV1, AmazonAdsConfig
from ads_api.base import BaseResource, ClientContext
from ads_api.models.v1.campaigns.sp import SPCampaignSuccessResponse, SPQueryCampaignRequest


def test_methods_are_not_coroutines(sync_config: AmazonAdsConfig) -> None:
    """Verify that resource methods in the sync package are synchronous functions."""
    with AdsClient(sync_config) as ads:
        assert not inspect.iscoroutinefunction(ads.v1.sp.campaigns.query_campaign)
        assert not inspect.iscoroutinefunction(ads.v0.accounts.profiles.list_profiles)
        assert not inspect.iscoroutinefunction(ads.close)


def test_sync_client_context_manager(sync_config: AmazonAdsConfig) -> None:
    """Verify synchronous context manager protocol."""
    with AdsClient(sync_config) as ads:
        assert ads.config == sync_config
        assert ads.account_id == "amzn1.ads-account.test"
        assert ads.profile_id == "123456"
        assert not ads.is_seller
        assert not ads.is_vendor
        assert not ads.is_agency


def test_sync_client_standalone_v1(sync_config: AmazonAdsConfig) -> None:
    with AdsClientV1(sync_config) as ads:
        assert ads.sp is not None
        assert ads.sb is not None
        assert ads.sd is not None
        assert ads.dsp is not None


def test_sync_client_standalone_v0(sync_config: AmazonAdsConfig) -> None:
    with AdsClientV0(sync_config) as ads:
        assert ads.accounts is not None
        assert ads.reporting is not None
        assert ads.sp_v3 is not None


def test_sync_v1_sp_query_campaign(sync_config: AmazonAdsConfig) -> None:
    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 200
    mock_resp.is_error = False
    mock_resp.text = '{"campaigns": []}'
    mock_resp.json.return_value = {"campaigns": []}

    with patch.object(BaseResource, "_request", return_value=mock_resp) as mock_req:
        with AdsClient(sync_config) as ads:
            body = SPQueryCampaignRequest(
                adProductFilter={"include": ["SPONSORED_PRODUCTS"]},
            )
            resp = ads.v1.sp.campaigns.query_campaign(body)
            assert resp == {"campaigns": []}
            mock_req.assert_called_once()

            # Test mode="pydantic"
            resp_model = ads.v1.sp.campaigns.query_campaign(body, mode="pydantic")
            assert isinstance(resp_model, SPCampaignSuccessResponse)


def test_sync_v0_profiles_list(sync_config: AmazonAdsConfig) -> None:
    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 200
    mock_resp.is_error = False
    mock_resp.text = (
        '[{"profileId": 12345, "countryCode": "US", "currencyCode": "USD", "timezone": "America/Los_Angeles", '
        '"accountInfo": {"marketplaceStringId": "ATVPDKIKX0DER", "id": "acc-1", "type": "seller"}}]'
    )
    mock_resp.json.return_value = [
        {
            "profileId": 12345,
            "countryCode": "US",
            "currencyCode": "USD",
            "timezone": "America/Los_Angeles",
            "accountInfo": {"marketplaceStringId": "ATVPDKIKX0DER", "id": "acc-1", "type": "seller"},
        }
    ]

    with patch.object(BaseResource, "_request", return_value=mock_resp) as mock_req:
        with AdsClient(sync_config) as ads:
            profiles = ads.v0.accounts.profiles.list_profiles()
            assert len(profiles) == 1
            assert profiles[0]["profileId"] == 12345
            mock_req.assert_called_once()


def test_sync_retry_on_rate_limit(sync_config: AmazonAdsConfig) -> None:
    resp_429 = MagicMock(spec=httpx.Response)
    resp_429.status_code = 429
    resp_429.is_error = True
    resp_429.headers = {"Retry-After": "0"}

    resp_200 = MagicMock(spec=httpx.Response)
    resp_200.status_code = 200
    resp_200.is_error = False
    resp_200.text = "{}"
    resp_200.json.return_value = {}

    ctx = ClientContext(sync_config)
    client_mock = MagicMock(spec=httpx.Client)
    client_mock.request.side_effect = [resp_429, resp_200]
    ctx._client = client_mock

    resource = BaseResource(ctx)
    with patch("time.sleep") as mock_sleep:
        resp = resource._request("GET", "/test")
        assert resp == resp_200
        mock_sleep.assert_called_once()
