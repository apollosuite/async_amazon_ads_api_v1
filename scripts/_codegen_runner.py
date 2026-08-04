"""Orchestration for tag-based OpenAPI code generation."""

from __future__ import annotations

import json
import subprocess
import sys
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from _client_emit import ClientGenerationConfig, generate_client_file
from _openapi_schema import (
    PROJECT_ROOT,
    camel_to_snake,
    collect_class_names,
    discover_known_schemas,
    find_endpoints_by_tag,
)
from _pydantic_emit import emit_model, is_enum, split_types
from _schema_roles import (
    EmittedModel,
    RoleNameMap,
    SchemaKey,
    SchemaRole,
    discover_role_emissions,
    prefixed_enum_name,
    prefixed_shared_model_name,
    schemas_for_resolution,
)


@dataclass(frozen=True)
class GenerationProject:
    """Output paths and import settings for a generation run."""

    spec_path: Path
    model_dir: Path
    models_package: str
    client_dir: Path | None
    known_schemas_prefix: str | None = None
    enum_prefix: str = ""
    patch_spec: Callable[[dict], None] | None = None

    @property
    def models_only(self) -> bool:
        return self.client_dir is None


@dataclass(frozen=True)
class TagSpec:
    """Per-tag model (+ optional client) generation settings."""

    tag: str
    snake_name: str | None = None
    schema_renames: dict[str, str] = field(default_factory=dict)
    rename_fn: Callable[[str], str] | None = None
    client: ClientGenerationConfig | None = None

    def resolved_snake_name(self) -> str:
        if self.snake_name:
            return self.snake_name
        resource = self.client.resource_name if self.client and self.client.resource_name else self.tag
        return camel_to_snake(resource)

    def resolved_resource_name(self) -> str:
        if self.client and self.client.resource_name:
            return self.client.resource_name
        return self.tag

    def stem_rename(self) -> Callable[[str], str]:
        overrides = self.schema_renames

        def rename(openapi_name: str) -> str:
            if openapi_name in overrides:
                return overrides[openapi_name]
            if self.rename_fn:
                return self.rename_fn(openapi_name)
            return openapi_name

        return rename


def collect_cross_tag_enums(
    spec: dict,
    tags: list[TagSpec],
    enum_prefix: str,
) -> dict[str, tuple[dict[str, Any], str]]:
    """Return cross-tag shared enums as ``{openapi_name: (schema, python_name)}``."""
    all_schemas = spec.get("components", {}).get("schemas", {})
    enum_to_tags: dict[str, set[str]] = defaultdict(set)
    stem_rename = tags[0].stem_rename() if tags else (lambda n: n)

    for tag in tags:
        endpoints = find_endpoints_by_tag(spec, tag.tag)
        if not endpoints:
            continue
        emitted, _, _, _ = discover_role_emissions(
            spec,
            endpoints,
            tag.rename_fn,
            schema_renames=tag.schema_renames,
        )
        for item in emitted:
            if item.key.role == SchemaRole.NEUTRAL and is_enum(item.schema) and item.schema.get("enum"):
                enum_to_tags[item.key.openapi_name].add(tag.resolved_snake_name())

    result: dict[str, tuple[dict[str, Any], str]] = {}
    for openapi_name, tag_set in enum_to_tags.items():
        if len(tag_set) < 2:
            continue
        schema = all_schemas.get(openapi_name, {})
        if not schema:
            continue
        python_name = prefixed_enum_name(openapi_name, enum_prefix, stem_rename)
        result[openapi_name] = (schema, python_name)
    return result


def generate_enums_file(
    *,
    model_dir: Path,
    models_package: str,
    cross_tag_enums: dict[str, tuple[dict[str, Any], str]],
) -> None:
    """Write shared enums for a product package."""
    if not cross_tag_enums:
        return

    enums_by_python = {python_name: schema for _, (schema, python_name) in cross_tag_enums.items()}
    header = [
        '"""Auto-generated shared enums for cross-tag schemas."""',
        "",
        "from __future__ import annotations",
        "",
        "from enum import StrEnum",
        "",
    ]
    buf = "\n".join(header)
    empty_name_map = RoleNameMap(by_key={}, shared_entities=set(), neutral=set())
    for python_name in sorted(enums_by_python):
        buf += (
            emit_model(
                python_name,
                enums_by_python[python_name],
                {},
                empty_name_map,
                SchemaRole.NEUTRAL,
            )
            + "\n\n"
        )

    public_names = sorted(enums_by_python)
    buf += f"__all__ = [{', '.join(repr(n) for n in public_names)}]\n"

    model_dir.mkdir(parents=True, exist_ok=True)
    enums_path = model_dir / "enums.py"
    enums_path.write_text(buf)
    print(f"\n  Wrote shared enums: {enums_path} ({len(public_names)} enums)")


def collect_tag_emissions(
    spec: dict,
    tags: list[TagSpec],
    shared_enum_names: dict[str, str] | None,
    shared_model_names: dict[SchemaKey, str] | None = None,
) -> tuple[dict[str, list[EmittedModel]], list[EmittedModel], set[str]]:
    """Collect per-tag emissions and union metadata for shared file generation."""
    per_tag: dict[str, list[EmittedModel]] = {}
    all_emitted: list[EmittedModel] = []
    shared_entities: set[str] = set()

    for tag in tags:
        endpoints = find_endpoints_by_tag(spec, tag.tag)
        if not endpoints:
            continue
        emitted, tag_shared, _, _ = discover_role_emissions(
            spec,
            endpoints,
            tag.rename_fn,
            schema_renames=tag.schema_renames,
            shared_enum_names=shared_enum_names,
            shared_model_names=shared_model_names,
        )
        per_tag[tag.resolved_snake_name()] = emitted
        all_emitted.extend(emitted)
        shared_entities |= tag_shared

    return per_tag, all_emitted, shared_entities


def collect_cross_tag_models(
    per_tag_emissions: dict[str, list[EmittedModel]],
) -> dict[SchemaKey, EmittedModel]:
    """Return models (non-enum) emitted from two or more tags."""
    key_to_tags: dict[SchemaKey, set[str]] = defaultdict(set)
    key_to_item: dict[SchemaKey, EmittedModel] = {}

    for tag_name, emitted in per_tag_emissions.items():
        for item in emitted:
            if item.key.role == SchemaRole.NEUTRAL:
                continue
            key_to_tags[item.key].add(tag_name)
            key_to_item[item.key] = item

    return {key: key_to_item[key] for key, tag_set in key_to_tags.items() if len(tag_set) >= 2}


def apply_shared_model_prefixes(
    cross_tag_models: dict[SchemaKey, EmittedModel],
    prefix: str,
    stem_rename: Callable[[str], str],
    shared_entities: set[str],
) -> dict[SchemaKey, EmittedModel]:
    """Return cross-tag models with product-prefixed Python names."""
    return {
        key: EmittedModel(
            key=key,
            python_name=prefixed_shared_model_name(
                key.openapi_name,
                key.role,
                prefix,
                stem_rename,
                shared_entities,
            ),
            schema=item.schema,
            extra=item.extra,
            public=item.public,
        )
        for key, item in cross_tag_models.items()
    }


def _collect_openapi_refs(schema: Any) -> set[str]:
    refs: set[str] = set()
    if isinstance(schema, dict):
        if "$ref" in schema:
            refs.add(schema["$ref"].split("/")[-1])
        for value in schema.values():
            refs |= _collect_openapi_refs(value)
    elif isinstance(schema, list):
        for item in schema:
            refs |= _collect_openapi_refs(item)
    return refs


def generate_shared_file(
    *,
    model_dir: Path,
    cross_tag_models: dict[SchemaKey, EmittedModel],
    all_emitted: list[EmittedModel],
    shared_entities: set[str],
    shared_enum_names: dict[str, str],
) -> None:
    """Write cross-tag shared Pydantic models."""
    if not cross_tag_models:
        return

    resolution_schemas = schemas_for_resolution(all_emitted)
    name_map = RoleNameMap.from_emitted(all_emitted, shared_entities)

    models_by_name = {item.python_name: item for item in cross_tag_models.values()}
    generate_schemas = {name: item.schema for name, item in models_by_name.items()}
    _, regular_models, composition_models = split_types(generate_schemas)

    enum_imports: set[str] = set()
    for item in cross_tag_models.values():
        for ref in _collect_openapi_refs(item.schema):
            python_name = shared_enum_names.get(ref)
            if python_name:
                enum_imports.add(python_name)

    header = [
        '"""Auto-generated shared models for cross-tag schemas."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Annotated",
        "from datetime import date, datetime",
        "",
        "from pydantic import BaseModel, ConfigDict, Field",
        "",
        "from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum",
        "",
    ]
    if enum_imports:
        header.append(f"from .enums import {', '.join(sorted(enum_imports))}")
        header.append("")
    header.append("")

    buf = "\n".join(header)

    def _emit(name: str, schema: dict) -> str:
        item = models_by_name[name]
        return emit_model(
            name,
            schema,
            resolution_schemas,
            name_map,
            item.key.role,
            extra=item.extra,
        )

    for name, schema in regular_models:
        buf += _emit(name, schema) + "\n\n"
    for name, schema in composition_models:
        buf += _emit(name, schema) + "\n\n"

    public_names = sorted(item.python_name for item in cross_tag_models.values() if item.public)
    if public_names:
        buf += f"__all__ = [{', '.join(repr(n) for n in public_names)}]\n"

    model_dir.mkdir(parents=True, exist_ok=True)
    shared_path = model_dir / "shared.py"
    shared_path.write_text(buf)
    print(f"\n  Wrote shared models: {shared_path} ({len(models_by_name)} models)")


def generate_models_for_tag(
    spec: dict,
    tag: TagSpec,
    known_schemas: dict[str, str],
    *,
    model_dir: Path,
    models_package: str,
    shared_enum_names: dict[str, str] | None = None,
    shared_enum_openapi: set[str] | None = None,
    shared_model_names: dict[SchemaKey, str] | None = None,
    shared_model_keys: set[SchemaKey] | None = None,
) -> tuple[set[str], list[tuple[str, str, dict]], dict[str, Any], RoleNameMap] | None:
    """Generate a Pydantic model file for a single tag."""
    snake_name = tag.resolved_snake_name()

    endpoints = find_endpoints_by_tag(spec, tag.tag)
    if not endpoints:
        print(f"\n[SKIP] Tag '{tag.tag}' has no endpoints")
        return None

    print(f"\n{'=' * 60}")
    print(f"Tag: {tag.tag}")
    print(f"Endpoints: {len(endpoints)}")
    for method, path, op in endpoints:
        print(f"  {method:6s} {path}  ({op.get('operationId', '?')})")

    model_dir.mkdir(parents=True, exist_ok=True)

    emitted, shared_entities, request_names, response_names = discover_role_emissions(
        spec,
        endpoints,
        tag.rename_fn,
        schema_renames=tag.schema_renames,
        shared_enum_names=shared_enum_names,
        shared_model_names=shared_model_names,
    )
    name_map = RoleNameMap.from_emitted(emitted, shared_entities, known_schemas=known_schemas)
    resolution_schemas = schemas_for_resolution(emitted)

    print(
        f"  Emitted models: {len(emitted)} "
        f"(request={len(request_names)}, response={len(response_names)}, shared={len(shared_entities)})"
    )

    for item in emitted:
        if item.key.openapi_name != item.python_name or item.key.role.value != "input":
            print(f"  {item.key.openapi_name}[{item.key.role}] → {item.python_name}")

    if shared_entities:
        print(f"  Shared entities (input + output): {', '.join(sorted(shared_entities))}")

    to_import: dict[str, str] = {}
    to_generate: dict[str, EmittedModel] = {}
    current_module = f"{models_package}.{snake_name}"
    cross_tag_enums = shared_enum_openapi or set()
    cross_tag_models = shared_model_keys or set()
    enums_module = f"{models_package}.enums"
    shared_module = f"{models_package}.shared"
    for item in emitted:
        if item.python_name in known_schemas and known_schemas[item.python_name] != current_module:
            to_import[item.python_name] = known_schemas[item.python_name]
        elif item.key in cross_tag_models:
            to_import[item.python_name] = shared_module
        elif item.key.openapi_name in cross_tag_enums:
            to_import[item.python_name] = enums_module
        else:
            to_generate[item.python_name] = item

    if to_import:
        print(f"  Already known (will import): {len(to_import)}")
        for n in sorted(to_import):
            print(f"    {n} ← {to_import[n]}")

    model_path = model_dir / f"{snake_name}.py"
    model_imports: dict[str, list[str]] = defaultdict(list)
    for name, source in sorted(to_import.items()):
        model_imports[source].append(name)

    import_lines: list[str] = []
    for source, names in sorted(model_imports.items()):
        prefix = f"{models_package}."
        if source.startswith(prefix):
            module = source[len(prefix) :]
            import_lines.append(f"from .{module} import {', '.join(sorted(names))}")
        else:
            import_lines.append(f"from async_amazon_ads_api_v1.{source} import {', '.join(sorted(names))}")

    generate_schemas = {name: item.schema for name, item in to_generate.items()}
    enums, regular_models, composition_models = split_types(generate_schemas)

    header = [
        f'"""Auto-generated models for {tag.tag} from Amazon Ads API schema."""',
        "",
        "from __future__ import annotations",
        "",
    ]

    std_imports = set()
    if any(is_enum(s) for _, s in enums):
        std_imports.add("from enum import StrEnum")
    std_imports.add("from typing import Annotated, Any")
    std_imports.add("from datetime import date, datetime")

    header.extend(sorted(std_imports))
    if std_imports:
        header.append("")
    header.append("")
    header.append("from pydantic import BaseModel, ConfigDict, Field")
    header.append("")
    header.append("from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum")
    header.append("")
    header.extend(import_lines)
    header.append("")
    header.append("")

    emitted_by_name = {item.python_name: item for item in emitted}
    buf = "\n".join(header)

    def _emit(name: str, schema: dict) -> str:
        item = emitted_by_name[name]
        return emit_model(
            name,
            schema,
            resolution_schemas,
            name_map,
            item.key.role,
            extra=item.extra,
        )

    for name, schema in enums:
        buf += _emit(name, schema) + "\n\n"
    for name, schema in regular_models:
        buf += _emit(name, schema) + "\n\n"
    for name, schema in composition_models:
        buf += _emit(name, schema) + "\n\n"

    public_names = sorted(item.python_name for item in emitted if item.public)
    if public_names:
        buf += f"__all__ = [{', '.join(repr(n) for n in public_names)}]\n"

    model_path.write_text(buf)
    print(f"\n  Wrote model file: {model_path}")

    return shared_entities, endpoints, resolution_schemas, name_map


def generate_for_tag(
    spec: dict,
    tag: TagSpec,
    known_schemas: dict[str, str],
    *,
    model_dir: Path,
    models_package: str,
    client_dir: Path,
    shared_enum_names: dict[str, str] | None = None,
    shared_enum_openapi: set[str] | None = None,
    shared_model_names: dict[SchemaKey, str] | None = None,
    shared_model_keys: set[SchemaKey] | None = None,
) -> set[str]:
    """Generate model + client files for a single tag."""
    result = generate_models_for_tag(
        spec,
        tag,
        known_schemas,
        model_dir=model_dir,
        models_package=models_package,
        shared_enum_names=shared_enum_names,
        shared_enum_openapi=shared_enum_openapi,
        shared_model_names=shared_model_names,
        shared_model_keys=shared_model_keys,
    )
    if result is None:
        return set()

    shared_entities, endpoints, resolution_schemas, name_map = result
    client_dir.mkdir(parents=True, exist_ok=True)

    client_config = tag.client or ClientGenerationConfig(resource_name=tag.resolved_resource_name())
    client_content = generate_client_file(
        spec=spec,
        tag=tag.tag,
        resource_name=tag.resolved_resource_name(),
        snake_name=tag.resolved_snake_name(),
        models_package=models_package,
        endpoints=endpoints,
        schemas_for_resolution=resolution_schemas,
        name_map=name_map,
        client_config=client_config,
    )
    client_path = client_dir / f"{tag.resolved_snake_name()}.py"
    client_path.write_text(client_content)
    print(f"  Wrote client file: {client_path}")
    return shared_entities


def run_tool(cmd: list[str], label: str, *, cwd: Path = PROJECT_ROOT) -> None:
    print(f"\n── {label} {'─' * (56 - len(label))}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"  ⚠ {label} exited with code {result.returncode}")
    if result.stdout:
        for line in result.stdout.splitlines():
            print(f"  {line}")
    if result.stderr:
        for line in result.stderr.splitlines():
            print(f"  {line}")
    if result.returncode == 0:
        print(f"  ✓ {label} passed")


def run_post_processing() -> None:
    print("\n" + "=" * 60)
    print("Post-processing generated files...")
    run_tool(["uv", "run", "black", "src/"], "black")
    run_tool(["uv", "run", "ruff", "check", "--fix", "src/"], "ruff check --fix")


def print_shared_schemas_summary(all_shared: dict[str, list[str]], *, single_tag: bool = False) -> None:
    print("\n" + "=" * 60)
    if not all_shared:
        suffix = "" if single_tag else " across all tags"
        print(f"No shared entity schemas{suffix}.")
        return
    print("Shared entity schemas summary")
    for tag_name, names in all_shared.items():
        print(f"  {tag_name}: {', '.join(names)}")


def load_spec(spec_path: Path) -> dict:
    """Load an OpenAPI spec from JSON or YAML."""
    with open(spec_path) as f:
        if spec_path.suffix in {".yaml", ".yml"}:
            return yaml.safe_load(f)
        return json.load(f)


def run(project: GenerationProject, tags: list[TagSpec]) -> None:
    """Load spec, generate all tags, print summary, and post-process."""
    if not project.spec_path.exists():
        print(f"ERROR: {project.spec_path} not found", file=sys.stderr)
        sys.exit(1)

    known_schemas = discover_known_schemas(
        package_prefix=project.known_schemas_prefix or project.models_package,
    )
    print(f"Discovered {len(known_schemas)} already-defined schemas in the project")
    print(f"  model files: {len(known_schemas)}")

    spec = load_spec(project.spec_path)
    if project.patch_spec:
        project.patch_spec(spec)

    cross_tag_enums = collect_cross_tag_enums(spec, tags, project.enum_prefix)
    shared_enum_names = {openapi: python for openapi, (_, python) in cross_tag_enums.items()}
    shared_enum_openapi = set(cross_tag_enums)
    stem_rename = tags[0].stem_rename() if tags else (lambda n: n)

    per_tag_emissions, _, shared_entities = collect_tag_emissions(spec, tags, shared_enum_names or None)
    cross_tag_models = apply_shared_model_prefixes(
        collect_cross_tag_models(per_tag_emissions),
        project.enum_prefix,
        stem_rename,
        shared_entities,
    )
    shared_model_names = {key: item.python_name for key, item in cross_tag_models.items()}
    shared_model_keys = set(cross_tag_models)
    _, all_emitted, shared_entities = collect_tag_emissions(
        spec,
        tags,
        shared_enum_names or None,
        shared_model_names,
    )

    if cross_tag_enums:
        print(f"\nCross-tag shared enums: {len(cross_tag_enums)}")
        for openapi_name in sorted(cross_tag_enums):
            _, python_name = cross_tag_enums[openapi_name]
            print(f"  {openapi_name} → {python_name}")
        generate_enums_file(
            model_dir=project.model_dir,
            models_package=project.models_package,
            cross_tag_enums=cross_tag_enums,
        )
        enums_path = project.model_dir / "enums.py"
        for cls, _ in collect_class_names([enums_path]).items():
            known_schemas[cls] = f"{project.models_package}.enums"

    if cross_tag_models:
        print(f"\nCross-tag shared models: {len(cross_tag_models)}")
        for key, item in sorted(cross_tag_models.items(), key=lambda kv: kv[1].python_name):
            print(f"  {key.openapi_name}[{key.role}] → {item.python_name}")
        generate_shared_file(
            model_dir=project.model_dir,
            cross_tag_models=cross_tag_models,
            all_emitted=all_emitted,
            shared_entities=shared_entities,
            shared_enum_names=shared_enum_names,
        )
        shared_path = project.model_dir / "shared.py"
        for cls, _ in collect_class_names([shared_path]).items():
            known_schemas[cls] = f"{project.models_package}.shared"

    all_shared: dict[str, list[str]] = {}
    for tag in tags:
        if project.models_only:
            result = generate_models_for_tag(
                spec,
                tag,
                known_schemas,
                model_dir=project.model_dir,
                models_package=project.models_package,
                shared_enum_names=shared_enum_names,
                shared_enum_openapi=shared_enum_openapi,
                shared_model_names=shared_model_names,
                shared_model_keys=shared_model_keys,
            )
            shared = result[0] if result else set()
        else:
            assert project.client_dir is not None
            shared = generate_for_tag(
                spec,
                tag,
                known_schemas,
                model_dir=project.model_dir,
                models_package=project.models_package,
                client_dir=project.client_dir,
                shared_enum_names=shared_enum_names,
                shared_enum_openapi=shared_enum_openapi,
                shared_model_names=shared_model_names,
                shared_model_keys=shared_model_keys,
            )
        snake_name = tag.resolved_snake_name()
        model_path = project.model_dir / f"{snake_name}.py"
        if model_path.exists():
            for cls, stem in collect_class_names([model_path]).items():
                known_schemas[cls] = f"{project.models_package}.{stem}"
        if shared:
            all_shared[tag.tag] = sorted(shared)

    print_shared_schemas_summary(all_shared, single_tag=len(tags) == 1)
    run_post_processing()
    print(f"\n{'=' * 60}")
    print("Done.")
