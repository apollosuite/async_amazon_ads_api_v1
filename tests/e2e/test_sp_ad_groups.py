from __future__ import annotations

import pytest

from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient
from async_amazon_ads_api_v1.models.sp import (
    SPAdGroupMultiStatusResponse,
    SPCampaignMultiStatusResponse,
)

from .config import E2ESettings
from .helpers import ad_group_payload, campaign_payload


def _config_for_profile(e2e_settings: E2ESettings, profile_id: str) -> AmazonAdsConfig:
    return AmazonAdsConfig(
        client_id=e2e_settings.client_id,
        client_secret=e2e_settings.client_secret,
        refresh_token=e2e_settings.refresh_token,
        profile_id=profile_id,
        region=Region.NA,
        endpoints={"na": e2e_settings.base_url},
        token_url=e2e_settings.token_url,
        timeout=e2e_settings.timeout,
    )


@pytest.mark.asyncio
async def test_sp_ad_groups_require_campaign_in_same_profile(
    e2e_settings: E2ESettings,
    unique_name: str,
) -> None:
    owner_config = _config_for_profile(e2e_settings, e2e_settings.profile_id)
    other_config = _config_for_profile(e2e_settings, e2e_settings.other_profile_id)

    async with SPClient(owner_config) as owner_client:
        missing_parent = await owner_client.ad_groups.create(
            [ad_group_payload(f"{unique_name}-missing-parent", "missing-campaign")]
        )
        assert isinstance(missing_parent, SPAdGroupMultiStatusResponse)
        assert missing_parent.success == []
        assert missing_parent.error is not None
        assert missing_parent.error[0].index == 0
        assert missing_parent.error[0].errors[0].code == "RESOURCE_DOES_NOT_BELONG_TO_PARENT"

        campaign_result = await owner_client.campaigns.create(
            [campaign_payload(f"{unique_name}-parent", e2e_settings.marketplace)]
        )
        assert isinstance(campaign_result, SPCampaignMultiStatusResponse)
        assert campaign_result.error == []
        assert campaign_result.success is not None
        campaign_id = campaign_result.success[0].campaign.campaignId

        try:
            async with SPClient(other_config) as other_client:
                cross_profile = await other_client.ad_groups.create(
                    [ad_group_payload(f"{unique_name}-cross-profile", campaign_id)]
                )
            assert isinstance(cross_profile, SPAdGroupMultiStatusResponse)
            assert cross_profile.success == []
            assert cross_profile.error is not None
            assert cross_profile.error[0].index == 0
            assert cross_profile.error[0].errors[0].code == "RESOURCE_DOES_NOT_BELONG_TO_PARENT"

            same_profile = await owner_client.ad_groups.create(
                [ad_group_payload(f"{unique_name}-same-profile", campaign_id)]
            )
            assert isinstance(same_profile, SPAdGroupMultiStatusResponse)
            assert same_profile.error == []
            assert same_profile.success is not None
            ad_group = same_profile.success[0].adGroup
            assert ad_group.campaignId == campaign_id
            assert ad_group.adProduct == "SPONSORED_PRODUCTS"
            assert ad_group.bid.currencyCode == e2e_settings.expected_currency_code
        finally:
            await owner_client.campaigns.delete([campaign_id])
