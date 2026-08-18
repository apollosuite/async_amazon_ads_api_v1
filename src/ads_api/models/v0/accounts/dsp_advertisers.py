"""Auto-generated models for Advertiser from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel

type DspCountryV1 = Literal[
    "US",
    "CA",
    "MX",
    "JP",
    "AU",
    "IN",
    "UK",
    "GB",
    "DE",
    "FR",
    "IT",
    "ES",
    "AT",
    "AE",
    "SA",
    "BR",
    "NL",
    "SE",
    "SG",
    "TR",
]
"""
The country code.
"""


type DspSupportedCurrencyV1 = Literal[
    "USD", "CAD", "JPY", "GBP", "EUR", "INR", "MXN", "AED", "SAR", "BRL", "AUD", "SEK", "SGD", "TRY"
]
"""
The supported currencies.
"""


class DspAdvertiserV1(LenientModel):
    """The DSP Advertiser object"""

    advertiserId: str | None = Field(default=None, description="The advertiser identifier.")
    name: str | None = Field(default=None, description="The advertiser name.")
    currency: DspSupportedCurrencyV1 | str | None = Field(default=None)
    url: str | None = Field(default=None, description="The URL of the advertiser’s website.")
    country: DspCountryV1 | str | None = Field(default=None)
    timezone: DspTimezoneV1 | None = Field(default=None)
    isRegional: bool | None = Field(
        default=None, description="Set to `true` if account is associated with a Global Advertiser Account."
    )


class DspAdvertisersV1(LenientModel):
    """List of advertisers along with total number of advertisers which satisfy the filtering criteria."""

    totalResults: int | None = Field(
        default=None,
        description="Total number of advertisers which satisfy the filtering criteria. This number is given to support pagination and tell the client if there are more advertisers to be fetched.",
    )
    response: list[DspAdvertiserV1] | None = Field(
        default=None, description="List of advertisers with complete information."
    )


type DspTimezoneV1 = str

__all__ = ["DspAdvertiserV1", "DspAdvertisersV1", "DspCountryV1", "DspSupportedCurrencyV1", "DspTimezoneV1"]
