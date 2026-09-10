"""SharingRules resource operations.

Generated from OpenAPI spec (tag: Sharing Rules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.ads_data_manager.sharing_rules import (
    CreateSharingRuleRequestContent,
    CreateSharingRuleResponseContent,
    ListSharingRulesRequestContent,
    ListSharingRulesResponseContent,
)


class SharingRules(BaseResource):

    @overload
    def create_sharing_rule(
        self, body: CreateSharingRuleRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_sharing_rule(
        self, body: CreateSharingRuleRequestContent, *, mode: Literal["pydantic"]
    ) -> CreateSharingRuleResponseContent: ...
    @overload
    def create_sharing_rule(self, body: CreateSharingRuleRequestContent, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_sharing_rule(
        self, body: CreateSharingRuleRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CreateSharingRuleResponseContent | dict[str, Any] | httpx.Response:
        """Create a new Sharing Rule in ADM."""

        resp = self._request("POST", "/adm/sharingRules", json=self.dump_json(body))
        return self._response(CreateSharingRuleResponseContent, resp, mode=mode)

    @overload
    def list_sharing_rules(
        self, body: ListSharingRulesRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def list_sharing_rules(
        self, body: ListSharingRulesRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> ListSharingRulesResponseContent: ...
    @overload
    def list_sharing_rules(
        self, body: ListSharingRulesRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def list_sharing_rules(
        self, body: ListSharingRulesRequestContent | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ListSharingRulesResponseContent | dict[str, Any] | httpx.Response:
        """List a set of sharing rules belonging to an account."""

        resp = self._request("POST", "/adm/sharingRules/list", json=self.dump_json(body))
        return self._response(ListSharingRulesResponseContent, resp, mode=mode)

    @overload
    def revoke_sharing_rule(self, sharing_rule_id: str, *, mode: Literal["dict"] = "dict") -> Any: ...
    @overload
    def revoke_sharing_rule(self, sharing_rule_id: str, *, mode: Literal["pydantic"]) -> Any: ...
    @overload
    def revoke_sharing_rule(self, sharing_rule_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    def revoke_sharing_rule(self, sharing_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict") -> Any:
        """Revoke an existing Sharing Rule in ADM."""

        resp = self._request("PATCH", f"/adm/sharingRules/{sharing_rule_id}/revoke")
        if mode == "raw":
            return resp
        return resp.json()
