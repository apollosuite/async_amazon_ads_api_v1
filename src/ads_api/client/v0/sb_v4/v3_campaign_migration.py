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
    async def migration_job_results(
        self, body: MigrationJobResultsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> MigrationJobResultsResponseContent: ...
    @overload
    async def migration_job_results(
        self, body: MigrationJobResultsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def migration_job_results(
        self, body: MigrationJobResultsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def migration_job_results(
        self, body: MigrationJobResultsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> MigrationJobResultsResponseContent | dict[str, Any] | httpx.Response:
        """List Migration Results of all Campaign."""

        resp = await self._request(
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
    async def migration_job_status(
        self, body: MigrationJobStatusRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> MigrationJobStatusResponseContent: ...
    @overload
    async def migration_job_status(
        self, body: MigrationJobStatusRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def migration_job_status(
        self, body: MigrationJobStatusRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def migration_job_status(
        self, body: MigrationJobStatusRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> MigrationJobStatusResponseContent | dict[str, Any] | httpx.Response:
        """List Migration Job Status."""

        resp = await self._request(
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
    async def migration_results(
        self, body: MigrationResultsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> MigrationResultsResponseContent: ...
    @overload
    async def migration_results(
        self, body: MigrationResultsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def migration_results(
        self, body: MigrationResultsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def migration_results(
        self, body: MigrationResultsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> MigrationResultsResponseContent | dict[str, Any] | httpx.Response:
        """Lists all Campaign Migration results for an advertiser"""

        resp = await self._request(
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
    async def start_migration_job(
        self, body: StartMigrationJobRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> StartMigrationJobResponseContent: ...
    @overload
    async def start_migration_job(
        self, body: StartMigrationJobRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def start_migration_job(
        self, body: StartMigrationJobRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def start_migration_job(
        self, body: StartMigrationJobRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> StartMigrationJobResponseContent | dict[str, Any] | httpx.Response:
        """Creates Migration Job for V3 campaigns."""

        resp = await self._request(
            "POST",
            "/sb/v4/legacyCampaigns/migrationJob",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
                "Accept": "application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json",
            },
        )
        return self._response(StartMigrationJobResponseContent, resp, mode=mode)
