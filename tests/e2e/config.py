from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class E2ESettings:
    base_url: str
    client_id: str
    client_secret: str
    refresh_token: str
    profile_id: str
    other_profile_id: str
    marketplace: str
    expected_currency_code: str
    timeout: float

    @property
    def token_url(self) -> str:
        return f"{self.base_url}/auth/o2/token"


def _env(name: str, default: str) -> str:
    return os.environ.get(name, default)


def load_settings() -> E2ESettings:
    return E2ESettings(
        base_url=_env("ADS_V1_E2E_BASE_URL", "http://127.0.0.1:8000").rstrip("/"),
        client_id=_env("ADS_V1_E2E_CLIENT_ID", "amzn1.application-oa2-client.seedclient00001"),
        client_secret=_env("ADS_V1_E2E_CLIENT_SECRET", "84fde1783fd1492b9ef761f771bb823e"),
        refresh_token=_env("ADS_V1_E2E_REFRESH_TOKEN", "Atzr|seed_refresh_token_002"),
        profile_id=_env("ADS_V1_E2E_PROFILE_ID", "111111115"),
        other_profile_id=_env("ADS_V1_E2E_OTHER_PROFILE_ID", "111111116"),
        marketplace=_env("ADS_V1_E2E_MARKETPLACE", "GB"),
        expected_currency_code=_env("ADS_V1_E2E_EXPECTED_CURRENCY", "GBP"),
        timeout=float(_env("ADS_V1_E2E_TIMEOUT", "10")),
    )
