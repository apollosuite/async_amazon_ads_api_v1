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
    build_schema_renames,
    camel_to_snake,
    collect_class_names,
    discover_known_schemas,
    discover_schema_sets,
    find_endpoints_by_tag,
    rename_schema,
)
from _pydantic_emit import emit_model, is_enum, split_types


@dataclass(frozen=True)
class GenerationProject:
    """Output paths and import settings for a generation run."""

    spec_path: Path
    model_dir: Path
    models_package: str
    client_dir: Path | None
    known_schemas_prefix: str | None = None

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

    def resolved_schema_renames(self, spec: dict) -> dict[str, str]:
        if self.schema_renames:
            return dict(self.schema_renames)
        if self.rename_fn:
            return build_schema_renames(spec, self.tag, self.rename_fn)
        return {}

    def rename(self, name: str, renames: dict[str, str]) -> str:
        return rename_schema(name, renames)


def _resolve_tag_spec(spec: dict, tag: TagSpec) -> TagSpec:
    renames = tag.resolved_schema_renames(spec)
    if renames == tag.schema_renames:
        return tag
    return TagSpec(
        tag=tag.tag,
        snake_name=tag.snake_name,
        schema_renames=renames,
        client=tag.client,
    )


def generate_models_for_tag(
    spec: dict,
    tag: TagSpec,
    known_schemas: dict[str, str],
    *,
    model_dir: Path,
    models_package: str,
) -> tuple[set[str], list[tuple[str, str, dict]], dict[str, Any]] | None:
    """Generate a Pydantic model file for a single tag."""
    schema_renames = tag.schema_renames
    snake_name = tag.resolved_snake_name()

    def rename(n: str) -> str:
        return tag.rename(n, schema_renames)

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

    request_schemas, response_schemas, needed = discover_schema_sets(spec, endpoints)
    print(f"  Referenced schemas: {len(needed)} " f"(request={len(request_schemas)}, response={len(response_schemas)})")

    schemas_for_resolution: dict[str, Any] = dict(needed)
    for name, schema in needed.items():
        renamed = rename(name)
        if renamed != name:
            schemas_for_resolution[renamed] = schema

    renamed_from = {rename(k): k for k in needed if rename(k) != k}
    if renamed_from:
        for new, old in renamed_from.items():
            print(f"  Renamed schema: {old} → {new}")

    response_schema_names = {rename(n) for n in response_schemas}
    request_schema_names = {rename(n) for n in request_schemas}
    shared_schema_names = sorted(request_schema_names & response_schema_names)
    if shared_schema_names:
        print(f"  Shared schemas (request ∩ response): {len(shared_schema_names)}")
        for name in shared_schema_names:
            schema = needed.get(name) or next(
                (needed[k] for k in needed if rename(k) == name),
                {},
            )
            kind = "enum" if is_enum(schema) and schema.get("enum") else "model"
            print(f"    {name} ({kind})")

    to_import: dict[str, str] = {}
    to_generate: dict[str, Any] = {}
    current_module = f"{models_package}.{snake_name}"
    for name, schema in needed.items():
        renamed = rename(name)
        if renamed in known_schemas and known_schemas[renamed] != current_module:
            to_import[renamed] = known_schemas[renamed]
        else:
            to_generate[renamed] = schema

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
        if source == "errors":
            import_lines.append(f"from async_amazon_ads_api_v1.errors import {', '.join(sorted(names))}")
        else:
            prefix = f"{models_package}."
            if source.startswith(prefix):
                module = source[len(prefix) :]
                import_lines.append(f"from .{module} import {', '.join(sorted(names))}")
            else:
                import_lines.append(
                    f"from async_amazon_ads_api_v1.{source} import {', '.join(sorted(names))}"
                )

    enums, regular_models, composition_models = split_types(to_generate)
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

    all_models = list(regular_models) + list(composition_models)
    buf = "\n".join(header)
    for name, schema in enums:
        buf += emit_model(name, schema, schemas_for_resolution, schema_renames) + "\n\n"
    for name, schema in regular_models:
        extra = "allow" if name in response_schema_names else "forbid"
        buf += emit_model(name, schema, schemas_for_resolution, schema_renames, extra=extra) + "\n\n"
    for name, schema in composition_models:
        extra = "allow" if name in response_schema_names else "forbid"
        buf += emit_model(name, schema, schemas_for_resolution, schema_renames, extra=extra) + "\n\n"

    all_names = [n for n, _ in (enums + all_models)]
    if all_names:
        buf += f"__all__ = [{', '.join(repr(n) for n in all_names)}]\n"

    model_path.write_text(buf)
    print(f"\n  Wrote model file: {model_path}")

    return set(shared_schema_names), endpoints, schemas_for_resolution


def generate_for_tag(
    spec: dict,
    tag: TagSpec,
    known_schemas: dict[str, str],
    *,
    model_dir: Path,
    models_package: str,
    client_dir: Path,
) -> set[str]:
    """Generate model + client files for a single tag."""
    result = generate_models_for_tag(
        spec,
        tag,
        known_schemas,
        model_dir=model_dir,
        models_package=models_package,
    )
    if result is None:
        return set()

    shared_schema_names, endpoints, schemas_for_resolution = result
    client_dir.mkdir(parents=True, exist_ok=True)

    client_config = tag.client or ClientGenerationConfig(resource_name=tag.resolved_resource_name())
    client_content = generate_client_file(
        spec=spec,
        tag=tag.tag,
        resource_name=tag.resolved_resource_name(),
        snake_name=tag.resolved_snake_name(),
        models_package=models_package,
        endpoints=endpoints,
        schemas_for_resolution=schemas_for_resolution,
        schema_renames=tag.schema_renames,
        client_config=client_config,
    )
    client_path = client_dir / f"{tag.resolved_snake_name()}.py"
    client_path.write_text(client_content)
    print(f"  Wrote client file: {client_path}")
    return shared_schema_names


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
        print(f"No shared schemas (request ∩ response){suffix}.")
        return
    print("Shared schemas summary (request ∩ response)")
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

    known_schemas = discover_known_schemas(package_prefix=project.known_schemas_prefix)
    print(f"Discovered {len(known_schemas)} already-defined schemas in the project")
    print(f"  errors.py: {sum(1 for v in known_schemas.values() if v == 'errors')}")
    print(f"  model files: {sum(1 for v in known_schemas.values() if v != 'errors')}")

    spec = load_spec(project.spec_path)

    all_shared: dict[str, list[str]] = {}
    for raw_tag in tags:
        tag = _resolve_tag_spec(spec, raw_tag)
        if project.models_only:
            result = generate_models_for_tag(
                spec,
                tag,
                known_schemas,
                model_dir=project.model_dir,
                models_package=project.models_package,
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
