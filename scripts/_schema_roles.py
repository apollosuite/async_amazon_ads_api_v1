"""Role-driven OpenAPI schema → Python model naming."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Literal

from _openapi_schema import discover_schema_sets, is_enum, is_type_alias

ExtraMode = Literal["forbid", "allow"]

_ENTITY_FIELDS = frozenset(
    {
        "ruleDetails",
        "accountInfo",
        "countryCode",
        "currencyCode",
        "timezone",
        "dailyBudget",
        "budgetRulesDetails",
        "associatedRules",
        "budgetRule",
    }
)


class SchemaRole(StrEnum):
    """How an OpenAPI schema is used when emitting a Pydantic model."""

    INPUT = "input"
    OUTPUT = "output"
    MUTATION_RESULT = "mutation_result"
    NEUTRAL = "neutral"


@dataclass(frozen=True)
class SchemaKey:
    openapi_name: str
    role: SchemaRole


@dataclass(frozen=True)
class EmittedModel:
    key: SchemaKey
    python_name: str
    schema: dict[str, Any]
    extra: ExtraMode
    public: bool


class RoleNameMap:
    """Resolve OpenAPI ``$ref`` targets to Python class names by usage role."""

    def __init__(
        self,
        *,
        by_key: dict[SchemaKey, str],
        shared_entities: set[str],
        neutral: set[str],
        known_schemas: dict[str, str] | None = None,
    ) -> None:
        self._by_key = by_key
        self._shared_entities = shared_entities
        self._neutral = neutral
        self._known_schemas = known_schemas or {}
        self._by_openapi: dict[str, dict[SchemaRole, str]] = {}
        for key, python_name in by_key.items():
            self._by_openapi.setdefault(key.openapi_name, {})[key.role] = python_name

    @classmethod
    def from_emitted(
        cls, emitted: list[EmittedModel], shared_entities: set[str], known_schemas: dict[str, str] | None = None
    ) -> RoleNameMap:
        neutral = {e.key.openapi_name for e in emitted if e.key.role == SchemaRole.NEUTRAL}
        return cls(
            by_key={e.key: e.python_name for e in emitted},
            shared_entities=shared_entities,
            neutral=neutral,
            known_schemas=known_schemas,
        )

    def is_neutral(self, openapi_name: str) -> bool:
        return openapi_name in self._neutral

    def is_shared(self, openapi_name: str) -> bool:
        return openapi_name in self._shared_entities

    def python_name(self, openapi_name: str, role: SchemaRole) -> str:
        key = SchemaKey(openapi_name, role)
        if key in self._by_key:
            return self._by_key[key]
        raise KeyError(f"No emitted model for {openapi_name!r} with role {role!r}")

    def resolve_ref(self, openapi_name: str, context_role: SchemaRole) -> str:
        if openapi_name in self._neutral:
            return self.python_name(openapi_name, SchemaRole.NEUTRAL)

        for role in (context_role, SchemaRole.OUTPUT, SchemaRole.INPUT, SchemaRole.NEUTRAL, SchemaRole.MUTATION_RESULT):
            names = self._by_openapi.get(openapi_name, {})
            if role in names:
                return names[role]

        return openapi_name

    def resolve_request_ref(self, openapi_name: str) -> str:
        if openapi_name in self._neutral:
            return self.python_name(openapi_name, SchemaRole.NEUTRAL)
        return self.python_name(openapi_name, SchemaRole.INPUT)

    def resolve_response_ref(self, openapi_name: str, schema: dict[str, Any]) -> str:
        if openapi_name in self._neutral:
            return self.python_name(openapi_name, SchemaRole.NEUTRAL)
        if is_mutation_result_schema(schema):
            return self.python_name(openapi_name, SchemaRole.MUTATION_RESULT)
        if openapi_name in self._shared_entities:
            return self.python_name(openapi_name, SchemaRole.OUTPUT)
        return self.python_name(openapi_name, SchemaRole.OUTPUT)

    def legacy_flat_map(self) -> dict[str, str]:
        """Best-effort OpenAPI name → Python name (for logging)."""
        result: dict[str, str] = {}
        for openapi_name, roles in self._by_openapi.items():
            if SchemaRole.INPUT in roles:
                result[openapi_name] = roles[SchemaRole.INPUT]
            elif SchemaRole.NEUTRAL in roles:
                result[openapi_name] = roles[SchemaRole.NEUTRAL]
            else:
                result[openapi_name] = next(iter(roles.values()))
        return result


class SchemaNamingCollisionError(RuntimeError):
    def __init__(self, collisions: dict[str, list[SchemaKey]]) -> None:
        self.collisions = collisions
        details = "; ".join(
            f"{target} ← {', '.join(f'{k.openapi_name}[{k.role}]' for k in keys)}"
            for target, keys in sorted(collisions.items())
        )
        super().__init__(f"Schema naming collisions: {details}")


def is_mutation_result_schema(schema: dict[str, Any]) -> bool:
    props = set(schema.get("properties", {}))
    if "code" not in props or "details" not in props:
        return False
    return not bool(props & _ENTITY_FIELDS)


def _stem_for_mutation_result(openapi_name: str) -> str:
    if openapi_name.endswith("Response"):
        return openapi_name[: -len("Response")]
    return openapi_name


def build_python_name(
    openapi_name: str,
    role: SchemaRole,
    *,
    stem_rename: Callable[[str], str],
    shared_entities: set[str],
) -> str:
    if role == SchemaRole.NEUTRAL:
        return stem_rename(openapi_name)

    base = stem_rename(openapi_name)

    if role == SchemaRole.INPUT:
        return base

    if role == SchemaRole.MUTATION_RESULT:
        if openapi_name.endswith("Result"):
            return stem_rename(openapi_name)
        return f"{stem_rename(_stem_for_mutation_result(openapi_name))}Result"

    if role == SchemaRole.OUTPUT:
        if openapi_name in shared_entities:
            return f"{base}Out"
        return base

    raise ValueError(f"Unknown role: {role}")


def prefixed_enum_name(openapi_name: str, prefix: str, stem_rename: Callable[[str], str]) -> str:
    """Apply product prefix to a cross-tag shared enum (skip if already prefixed)."""
    base = stem_rename(openapi_name)
    if prefix and not base.startswith(prefix):
        return f"{prefix}{base}"
    return base


def prefixed_shared_model_name(
    openapi_name: str,
    role: SchemaRole,
    prefix: str,
    stem_rename: Callable[[str], str],
    shared_entities: set[str],
) -> str:
    """Apply product prefix to a cross-tag shared model (skip if already prefixed)."""
    base = build_python_name(
        openapi_name,
        role,
        stem_rename=stem_rename,
        shared_entities=shared_entities,
    )
    if prefix and not base.startswith(prefix):
        return f"{prefix}{base}"
    return base


def discover_role_emissions(
    spec: dict,
    endpoints: list[tuple[str, str, dict]],
    stem_rename: Callable[[str], str] | None = None,
    *,
    schema_renames: dict[str, str] | None = None,
    shared_enum_names: dict[str, str] | None = None,
    shared_model_names: dict[SchemaKey, str] | None = None,
) -> tuple[list[EmittedModel], set[str], set[str], set[str]]:
    """Discover emitted models with roles for a tag's endpoints."""
    overrides = schema_renames or {}

    def rename(openapi_name: str) -> str:
        if openapi_name in overrides:
            return overrides[openapi_name]
        if stem_rename:
            return stem_rename(openapi_name)
        return openapi_name

    all_schemas = spec.get("components", {}).get("schemas", {})
    request_schemas, response_schemas, _ = discover_schema_sets(spec, endpoints)
    request_names = set(request_schemas)
    response_names = set(response_schemas)
    shared_entities = request_names & response_names

    keys_to_emit: list[SchemaKey] = []

    for name in sorted(request_names | response_names):
        schema = all_schemas.get(name, {})
        if not schema:
            continue

        if (is_enum(schema) and schema.get("enum")) or is_type_alias(schema):
            keys_to_emit.append(SchemaKey(name, SchemaRole.NEUTRAL))
            continue

        if name in request_names:
            keys_to_emit.append(SchemaKey(name, SchemaRole.INPUT))

        if name in response_names:
            role = SchemaRole.MUTATION_RESULT if is_mutation_result_schema(schema) else SchemaRole.OUTPUT
            keys_to_emit.append(SchemaKey(name, role))

    emitted: list[EmittedModel] = []
    by_python: dict[str, list[SchemaKey]] = {}

    for key in keys_to_emit:
        schema = all_schemas[key.openapi_name]
        if shared_model_names and key in shared_model_names:
            python_name = shared_model_names[key]
        elif key.role == SchemaRole.NEUTRAL and shared_enum_names and key.openapi_name in shared_enum_names:
            python_name = shared_enum_names[key.openapi_name]
        else:
            python_name = build_python_name(
                key.openapi_name,
                key.role,
                stem_rename=rename,
                shared_entities=shared_entities,
            )
        extra: ExtraMode = "forbid" if key.role == SchemaRole.INPUT else "allow"
        public = key.role in (SchemaRole.INPUT, SchemaRole.NEUTRAL)
        emitted.append(
            EmittedModel(
                key=key,
                python_name=python_name,
                schema=schema,
                extra=extra,
                public=public,
            )
        )
        by_python.setdefault(python_name, []).append(key)

    collisions = {name: keys for name, keys in by_python.items() if len(keys) > 1}
    if collisions:
        raise SchemaNamingCollisionError(collisions)

    return emitted, shared_entities, request_names, response_names


def schemas_for_resolution(emitted: list[EmittedModel]) -> dict[str, Any]:
    return {item.python_name: item.schema for item in emitted}
