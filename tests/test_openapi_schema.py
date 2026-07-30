"""Tests for role-driven schema naming."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from _schema_roles import (
    SchemaNamingCollisionError,
    SchemaRole,
    build_python_name,
    discover_role_emissions,
    is_mutation_result_schema,
    prefixed_enum_name,
    prefixed_shared_model_name,
)


def _sb_rename(name: str) -> str:
    if name.startswith("SB"):
        return name
    return "SB" + name


def test_build_python_name_request_primary() -> None:
    assert (
        build_python_name("SBBudgetRule", SchemaRole.INPUT, stem_rename=_sb_rename, shared_entities={"SBBudgetRule"})
        == "SBBudgetRule"
    )
    assert (
        build_python_name("SBBudgetRule", SchemaRole.OUTPUT, stem_rename=_sb_rename, shared_entities={"SBBudgetRule"})
        == "SBBudgetRuleOut"
    )
    assert (
        build_python_name(
            "BudgetRuleResponse", SchemaRole.MUTATION_RESULT, stem_rename=_sb_rename, shared_entities=set()
        )
        == "SBBudgetRuleResult"
    )


def test_is_mutation_result_schema() -> None:
    assert is_mutation_result_schema({"properties": {"code": {}, "details": {}, "ruleId": {}}})
    assert not is_mutation_result_schema({"properties": {"budgetRule": {}}})


def test_prefixed_enum_name() -> None:
    assert prefixed_enum_name("ErrorCode", "SP", lambda n: n) == "SPErrorCode"
    assert prefixed_enum_name("SPState", "SP", lambda n: n) == "SPState"
    assert prefixed_enum_name("CountryCode", "General", lambda n: n) == "GeneralCountryCode"


def test_prefixed_shared_model_name() -> None:
    assert prefixed_shared_model_name("Error", SchemaRole.OUTPUT, "SP", lambda n: n, set()) == "SPError"
    assert prefixed_shared_model_name("SPTag", SchemaRole.OUTPUT, "SP", lambda n: n, set()) == "SPTag"
    assert prefixed_shared_model_name("Error", SchemaRole.OUTPUT, "General", lambda n: n, set()) == "GeneralError"


def test_discover_role_emissions_splits_shared_entity() -> None:
    spec = {
        "paths": {
            "/items": {
                "get": {
                    "tags": ["T"],
                    "responses": {
                        "200": {"content": {"application/json": {"schema": {"$ref": "#/components/schemas/Widget"}}}}
                    },
                },
                "put": {
                    "tags": ["T"],
                    "requestBody": {
                        "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Widget"}}}
                    },
                    "responses": {
                        "200": {
                            "content": {"application/json": {"schema": {"$ref": "#/components/schemas/WidgetResult"}}}
                        }
                    },
                },
            }
        },
        "components": {
            "schemas": {
                "Widget": {"type": "object", "properties": {"id": {"type": "string"}}, "required": ["id"]},
                "WidgetResult": {
                    "type": "object",
                    "properties": {"code": {"type": "string"}, "details": {"type": "string"}},
                },
            }
        },
    }
    emitted, shared, _, _ = discover_role_emissions(
        spec,
        [("GET", "/items", spec["paths"]["/items"]["get"]), ("PUT", "/items", spec["paths"]["/items"]["put"])],
    )
    names = {e.python_name for e in emitted}
    assert shared == {"Widget"}
    assert "Widget" in names
    assert "WidgetOut" in names
    assert "WidgetResult" in names


def test_discover_role_emissions_raises_on_collision() -> None:
    spec = {
        "paths": {
            "/x": {
                "post": {
                    "tags": ["T"],
                    "requestBody": {"content": {"application/json": {"schema": {"$ref": "#/components/schemas/Foo"}}}},
                    "responses": {
                        "200": {"content": {"application/json": {"schema": {"$ref": "#/components/schemas/Bar"}}}}
                    },
                }
            }
        },
        "components": {"schemas": {"Foo": {"type": "object"}, "Bar": {"type": "object"}}},
    }

    def same(_: str) -> str:
        return "Same"

    with pytest.raises(SchemaNamingCollisionError):
        discover_role_emissions(spec, [("POST", "/x", spec["paths"]["/x"]["post"])], same)
