"""Auto-generated models for Brand Benchmarks from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel


class AdvertiserReportMetadata(LenientModel):
    advertiserId: str | None = Field(default=None)
    indexDate: str | None = Field(default=None, pattern="^[0-9]{4}-(0*[1-9]|1[0-2])-(0*[1-9]|[1-2][0-9]|3[0-1])$")
    obfuscatedMarketplaceId: str | None = Field(default=None)
    reportType: str | None = Field(default=None)


class GetAdvertiserReportResponseContent(LenientModel):
    """The presigned S3 URL to allow clients to download the report."""

    downloadLink: str | None = Field(default=None)


class ListAdvertiserReportMetadataResponseContent(LenientModel):
    """The presigned S3 URL to allow clients to download the report."""

    nextToken: str | None = Field(default=None)
    reportsMetadata: list[AdvertiserReportMetadata] | None = Field(default=None, min_length=0, max_length=1000)


__all__ = [
    "AdvertiserReportMetadata",
    "GetAdvertiserReportResponseContent",
    "ListAdvertiserReportMetadataResponseContent",
]
