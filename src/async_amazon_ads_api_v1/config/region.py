"""Region enum and endpoint mapping."""

from __future__ import annotations

from enum import StrEnum


class Region(StrEnum):
    """Amazon Ads API region identifiers."""

    NA = "na"
    EU = "eu"
    FE = "fe"


ENDPOINT_MAP: dict[str, str] = {
    "na": "https://advertising-api.amazon.com",
    "eu": "https://advertising-api-eu.amazon.com",
    "fe": "https://advertising-api-fe.amazon.com",
}
