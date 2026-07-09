"""Generate Pydantic models for Profiles API (legacy/accounts).

Groups schemas by the `tags` field in the OpenAPI YAML spec.
  - tags=["Profiles"]  → profiles.py

Usage:
    uv run python scripts/generate_legacy_profiles_models.py
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from generate_file_structure import extract_refs  # type: ignore[import-untyped]
from generate_models import is_enum, _clean_description as _raw_clean  # type: ignore[import-untyped]

HERE = Path(__file__).parent
SPEC_PATH = HERE / "profiles_openapi.yaml"
OUTPUT_DIR = HERE.parent / "src" / "async_amazon_ads_api_v1" / "models" / "legacy" / "accounts"


MODULE_HEADER = '''"""Auto-generated Pydantic models for Profiles API."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum
'''


# ── Schema name → class name normalization ────────────────────────────


def to_pascal(name: str) -> str:
    """Ensure a schema name is PascalCase for use as a Python class name."""
    if name and name[0].islower():
        return name[0].upper() + name[1:]
    return name


def build_name_map(schemas: dict) -> dict[str, str]:
    """Build a mapping from schema key → PascalCase class name."""
    mapping: dict[str, str] = {}
    for key in schemas:
        mapping[key] = to_pascal(key)
    return mapping


def python_type_from_ref(ref_name: str, schemas: dict, name_map: dict[str, str]) -> str:
    """Resolve a $ref schema name to the Python type string, handling enums."""
    schema = schemas.get(ref_name, {})
    cls = name_map.get(ref_name, to_pascal(ref_name))
    if schema.get("enum"):
        return f"Annotated[{cls} | str, lenient_enum({cls})]"
    return cls


def resolve_type(fschema: dict, schemas: dict, name_map: dict[str, str]) -> str:
    """Convert an OpenAPI field schema to a Python type string."""
    if "$ref" in fschema:
        return python_type_from_ref(fschema["$ref"].split("/")[-1], schemas, name_map)

    t = fschema.get("type", "object")
    fmt = fschema.get("format", "")
    if t == "array":
        inner = resolve_type(fschema.get("items", {}), schemas, name_map)
        return f"list[{inner}]"
    if t == "object":
        if fschema.get("additionalProperties"):
            val = resolve_type(fschema["additionalProperties"], schemas, name_map)
            return f"dict[str, {val}]"
        return "dict[str, Any]"
    if t == "string":
        return "datetime" if fmt == "date-time" else "date" if fmt == "date" else "str"
    return {"integer": "int", "number": "float", "boolean": "bool"}.get(t, "Any")


# ── Tag-based schema grouping ──────────────────────────────────────────


def to_snake_filename(tag: str) -> str:
    s = tag.lower().replace(" ", "_").replace("-", "_")
    s = re.sub(r"[^a-z0-9_]", "", s)
    return s + ".py"


def tag_group_schemas(spec: dict) -> dict[str, list[str]]:
    schemas = spec["components"]["schemas"]
    paths = spec.get("paths", {})
    all_names = set(schemas.keys())

    fwd: dict[str, set[str]] = {}
    for n in all_names:
        all_refs = extract_refs(schemas[n])
        fwd[n] = {r for r in all_refs if r in all_names}

    tag_entries: dict[str, set[str]] = defaultdict(set)

    for p, pitem in paths.items():
        for method in ("get", "post", "put", "patch", "delete"):
            op = pitem.get(method)
            if not op:
                continue
            tags: list[str] = op.get("tags", [])
            if not tags:
                continue
            tag = tags[0]

            for _, media in op.get("requestBody", {}).get("content", {}).items():
                s = media.get("schema", {})
                if s.get("type") == "array" and "$ref" in (s.get("items") or {}):
                    tag_entries[tag].add(s["items"]["$ref"].split("/")[-1])
                elif "$ref" in s:
                    tag_entries[tag].add(s["$ref"].split("/")[-1])

            for _, resp in op.get("responses", {}).items():
                for _, media in resp.get("content", {}).items():
                    s = media.get("schema", {})
                    if s.get("type") == "array" and "$ref" in (s.get("items") or {}):
                        tag_entries[tag].add(s["items"]["$ref"].split("/")[-1])
                    elif "$ref" in s:
                        tag_entries[tag].add(s["$ref"].split("/")[-1])

    tag_closure: dict[str, set[str]] = {}
    for tag, entries in tag_entries.items():
        closure = set(entries)
        q = list(entries)
        while q:
            node = q.pop(0)
            for dep in fwd.get(node, set()):
                if dep not in closure:
                    closure.add(dep)
                    q.append(dep)
        tag_closure[tag] = closure

    assigned: dict[str, str] = {}
    for tag, closure in tag_closure.items():
        for s in sorted(closure):
            if s not in assigned:
                assigned[s] = tag

    result: dict[str, list[str]] = defaultdict(list)
    for s, tag in sorted(assigned.items()):
        result[tag].append(s)
    return dict(result)


# ── Model generation (Field(description=...) style) ───────────────────


def clean_desc(raw: str) -> str:
    """Clean and strip trailing whitespace from description lines."""
    cleaned = _raw_clean(raw) if raw else ""
    # Remove trailing whitespace from each line, then strip overall
    return " ".join(line.rstrip() for line in cleaned.splitlines()).strip()


def field_kwargs(fschema: dict, *, is_required: bool, desc: str) -> list[str]:
    kwargs: list[str] = []
    if not is_required:
        kwargs.append("default=None")
    if desc:
        kwargs.append(f'description="{desc.replace(chr(34), chr(92) + chr(34))}"')
    if fschema.get("minLength") is not None:
        kwargs.append(f"min_length={fschema['minLength']}")
    if fschema.get("maxLength") is not None:
        kwargs.append(f"max_length={fschema['maxLength']}")
    if fschema.get("minimum") is not None:
        kwargs.append(f"ge={fschema['minimum']}")
    if fschema.get("maximum") is not None:
        kwargs.append(f"le={fschema['maximum']}")
    if fschema.get("minItems") is not None:
        kwargs.append(f"min_length={fschema['minItems']}")
    if fschema.get("maxItems") is not None:
        kwargs.append(f"max_length={fschema['maxItems']}")
    return kwargs


def build_field_line(fname: str, fschema: dict, schemas: dict, name_map: dict[str, str], required: set[str]) -> str:
    typ = resolve_type(fschema, schemas, name_map)
    is_required = fname in required
    if not is_required and typ not in ("Any",):
        typ = f"{typ} | None"
    desc = clean_desc(fschema.get("description", "") or "")
    kwargs = field_kwargs(fschema, is_required=is_required, desc=desc)

    if not kwargs:
        default = "" if is_required else " = None"
        return f"    {fname}: {typ}{default}"

    indent = " " * (len(fname) + len(typ) + 2)
    lhs = f"    {fname}: {typ} = Field("

    if len(kwargs) == 1 and len(lhs) + len(kwargs[0]) < 88:
        return f"{lhs}{kwargs[0]})"

    args_block = f",\n{indent}".join(kwargs)
    return f"{lhs}\n{indent}{args_block},\n{indent})"


def generate_model(name: str, schema: dict, schemas: dict, name_map: dict[str, str]) -> str:
    doc = schema.get("description", "")
    required: set[str] = set(schema.get("required", []))
    docstring = f'\n    """{doc}"""' if doc else ""

    if not schema.get("properties") and schema.get("oneOf"):
        fields: list[str] = []
        for variant in schema["oneOf"]:
            if variant.get("type") == "object" and variant.get("properties"):
                for fname, fschema in variant["properties"].items():
                    fields.append(build_field_line(fname, fschema, schemas, name_map, required | set()))
        field_block = "\n".join(fields) if fields else "    pass"
        return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="forbid")

{field_block}
"""

    props = schema.get("properties", {})
    if not props:
        return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="forbid")
"""

    fields = [build_field_line(fname, fschema, schemas, name_map, required) for fname, fschema in props.items()]
    return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="forbid")

{chr(10).join(fields)}
"""


def generate_enum(name: str, schema: dict) -> str:
    doc = clean_desc(schema.get("description", "") or "")
    values = schema.get("enum", [])
    members = "\n    ".join(f'{v} = "{v}"' for v in values)
    docstring = f'\n    """{doc}"""' if doc else ""
    return f"""class {name}(StrEnum):{docstring}
    {members}
"""


def emit(schema: dict, name: str, schemas: dict, name_map: dict[str, str]) -> str:
    if is_enum(schema) and schema.get("enum"):
        return generate_enum(name, schema)
    return generate_model(name, schema, schemas, name_map)


# ── File writer ───────────────────────────────────────────────────────


def generate_file(
    tag: str,
    schema_names: list[str],
    schemas: dict,
    name_map: dict[str, str],
    *,
    extra_models: list[str] | None = None,
) -> str:
    has_enums = any(is_enum(schemas[n]) and schemas[n].get("enum") for n in schema_names)

    header_parts = [MODULE_HEADER.rstrip()]
    if has_enums:
        header_parts.append("from enum import StrEnum")
    header_parts.append("")
    header = "\n".join(header_parts)

    parts = [emit(schemas[n], name_map.get(n, to_pascal(n)), schemas, name_map) for n in schema_names]
    if extra_models:
        parts.extend(extra_models)
    return f"{header}{chr(10).join(parts)}\n"


def main() -> None:
    with open(SPEC_PATH) as f:
        data = yaml.safe_load(f)
    schemas = data["components"]["schemas"]
    name_map = build_name_map(schemas)

    print("Schema → class name mapping:")
    for key, cls in sorted(name_map.items()):
        if key != cls:
            print(f"  {key} → {cls}")

    groups = tag_group_schemas(data)

    print("\nTag groups:")
    for tag, names in sorted(groups.items()):
        print(f"  {tag}: {len(names)} schemas → {to_snake_filename(tag)}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Wrapper models for bare-array responses (needed by self._response)
    extra_models = [
        """class ListProfilesResponseContent(BaseModel):
    \"\"\"Wrapper for listProfiles response (bare array → dict).\"\"\"
    model_config = ConfigDict(extra="forbid")

    profiles: list[Profile]
""",
        """class UpdateProfilesResponseContent(BaseModel):
    \"\"\"Wrapper for updateProfiles response (bare array → dict).\"\"\"
    model_config = ConfigDict(extra="forbid")

    results: list[ProfileResponse]
""",
    ]

    for tag in sorted(groups):
        fname = to_snake_filename(tag)
        content = generate_file(tag, groups[tag], schemas, name_map, extra_models=extra_models)
        (OUTPUT_DIR / fname).write_text(content)
        print(f"Wrote {OUTPUT_DIR / fname}")


if __name__ == "__main__":
    main()
