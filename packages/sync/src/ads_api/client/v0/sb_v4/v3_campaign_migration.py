"""V3CampaignMigration resource operations.

Generated from OpenAPI spec (tag: V3 Campaign Migration).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.v3_campaign_migration import (
    MigrationJobResultsRequestContent,
    MigrationJobResultsResponseContent,
    MigrationJobStatusRequestContent,
    MigrationJobStatusResponseContent,
    MigrationResultsRequestContent,
    MigrationResultsResponseContent,
    StartMigrationJobRequestContent,
    StartMigrationJobResponseContent,
)


class V3CampaignMigration(BaseResource):

    @overload
    def migration_job_results(
        self, body: MigrationJobResultsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def migration_job_results(
        self, body: MigrationJobResultsRequestContent, *, mode: Literal["pydantic"]
    ) -> MigrationJobResultsResponseContent: ...
    @overload
    def migration_job_results(
        self, body: MigrationJobResultsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def migration_job_results(
        self, body: MigrationJobResultsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> MigrationJobResultsResponseContent | dict[str, Any] | httpx.Response:
        """List Migration Results of all Campaign."""

        resp = self._request(
            "POST",
            "/sb/v4/legacyCampaigns/migrationJob/results",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
                "Accept": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
            },
        )
        return self._response(MigrationJobResultsResponseContent, resp, mode=mode)

    @overload
    def migration_job_status(
        self, body: MigrationJobStatusRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def migration_job_status(
        self, body: MigrationJobStatusRequestContent, *, mode: Literal["pydantic"]
    ) -> MigrationJobStatusResponseContent: ...
    @overload
    def migration_job_status(
        self, body: MigrationJobStatusRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def migration_job_status(
        self, body: MigrationJobStatusRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> MigrationJobStatusResponseContent | dict[str, Any] | httpx.Response:
        """List Migration Job Status."""

        resp = self._request(
            "POST",
            "/sb/v4/legacyCampaigns/migrationJob/status",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
                "Accept": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
            },
        )
        return self._response(MigrationJobStatusResponseContent, resp, mode=mode)

    @overload
    def migration_results(
        self, body: MigrationResultsRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def migration_results(
        self, body: MigrationResultsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> MigrationResultsResponseContent: ...
    @overload
    def migration_results(
        self, body: MigrationResultsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def migration_results(
        self, body: MigrationResultsRequestContent | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> MigrationResultsResponseContent | dict[str, Any] | httpx.Response:
        """Lists all Campaign Migration results for an advertiser"""

        resp = self._request(
            "POST",
            "/sb/v4/legacyCampaigns/overallMigrationResults",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
                "Accept": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
            },
        )
        return self._response(MigrationResultsResponseContent, resp, mode=mode)

    @overload
    def start_migration_job(
        self, body: StartMigrationJobRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def start_migration_job(
        self, body: StartMigrationJobRequestContent, *, mode: Literal["pydantic"]
    ) -> StartMigrationJobResponseContent: ...
    @overload
    def start_migration_job(self, body: StartMigrationJobRequestContent, *, mode: Literal["raw"]) -> httpx.Response: ...
    def start_migration_job(
        self, body: StartMigrationJobRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> StartMigrationJobResponseContent | dict[str, Any] | httpx.Response:
        """Creates Migration Job for V3 campaigns."""

        resp = self._request(
            "POST",
            "/sb/v4/legacyCampaigns/migrationJob",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
                "Accept": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
            },
        )
        return self._response(StartMigrationJobResponseContent, resp, mode=mode)
