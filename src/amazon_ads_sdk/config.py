"""Client configuration — regions and auth."""

from __future__ import annotations

import os
from enum import StrEnum


class Region(StrEnum):
    """Amazon Ads API region endpoints."""

    NA = "https://advertising-api.amazon.com"
    EU = "https://advertising-api-eu.amazon.com"
    FE = "https://advertising-api-fe.amazon.com"


class AmazonAdsConfig:
    """Holds authentication and client-level settings.

    Parameters
    ----------
    access_token : str
        OAuth 2.0 bearer token obtained via the Amazon Ads authorization flow.
    client_id : str
        Client identifier associated with a 'Login with Amazon' account.
        Sent as the ``Amazon-Ads-ClientId`` header.
    region : Region
        Which regional endpoint to target. Defaults to NA.
    profile_id : str | None
        Optional profile ID (for multi-profile accounts).
        Sent as the ``Amazon-Advertising-API-Scope`` header.
    timeout : float
        Request timeout in seconds. Defaults to 60.
    max_retries : int
        Number of automatic retries on transient errors (429 / 5xx).
    """

    def __init__(
        self,
        access_token: str,
        client_id: str,
        region: Region = Region.NA,
        *,
        profile_id: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 3,
    ) -> None:
        if not access_token:
            raise ValueError("access_token is required and cannot be empty")
        if not client_id:
            raise ValueError("client_id is required and cannot be empty")
        if timeout <= 0:
            raise ValueError("timeout must be a positive number")
        if max_retries < 0:
            raise ValueError("max_retries cannot be negative")
        self.access_token = access_token
        self.client_id = client_id
        self.region = region
        self.profile_id = profile_id
        self.timeout = timeout
        self.max_retries = max_retries

    @classmethod
    def from_env(cls) -> AmazonAdsConfig:
        access_token = os.environ.get("AMAZON_ACCESS_TOKEN")
        if not access_token:
            raise OSError("AMAZON_ACCESS_TOKEN environment variable is not set")
        client_id = os.environ.get("AMAZON_CLIENT_ID")
        if not client_id:
            raise OSError("AMAZON_CLIENT_ID environment variable is not set")
        region_str = os.environ.get("AMAZON_REGION", "na").lower()
        region_map = {"na": Region.NA, "eu": Region.EU, "fe": Region.FE}
        region = region_map.get(region_str)
        if region is None:
            raise ValueError(
                f"Unsupported AMAZON_REGION: {region_str!r}. Expected one of: {', '.join(region_map)}"
            )
        profile_id = os.environ.get("AMAZON_PROFILE_ID")
        return cls(
            access_token=access_token,
            client_id=client_id,
            region=region,
            profile_id=profile_id,
        )
