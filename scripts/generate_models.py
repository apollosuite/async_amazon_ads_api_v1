"""Code generator: generates Pydantic models from the OpenAPI schema JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from generate_file_structure import classify  # type: ignore[import-untyped]

HERE = Path(__file__).parent
PROJECT = HERE.parent / "src" / "async_amazon_ads_api_v1"

SPECS: dict[str, Path] = {
    "sp": HERE / "AmazonAdsAPISPMerged_prod_3p.json",
    "sb": HERE / "AmazonAdsAPISBMerged_prod_3p.json",
    "sd": HERE / "AmazonAdsAPISDMerged_prod_3p.json",
}

SHARED_ERROR_SCHEMAS: set[str] = {
    "BadGatewayResponseContent",
    "BadRequestResponseContent",
    "ContentTooLargeResponseContent",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "ForbiddenResponseContent",
    "GatewayTimeoutResponseContent",
    "InternalServerErrorResponseContent",
    "NotFoundResponseContent",
    "ServiceUnavailableErrorResponseContent",
    "TooManyRequestsResponseContent",
    "UnauthorizedResponseContent",
}

MODULE_HEADER = '''"""Auto-generated Pydantic models for {product} from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict
'''

ENUMS_HEADER = '''"""Auto-generated Pydantic models for {product} from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
'''

SHARED_HEADER = '''"""shared models for {product}."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict
'''


def _clean_description(desc: str) -> str:
    lines = desc.splitlines()
    result_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            content = stripped[1:-1]
            if all(cell.strip() in ("", "---") for cell in content.split("|")):
                continue
            cells = [c.strip() for c in content.split("|")]
            if cells:
                result_lines.append(" ".join(cells))
        else:
            result_lines.append(line)
    return " ".join(result_lines).strip()


def openapi_to_python_type(schema: dict, schemas: dict | None = None) -> str:
    if "$ref" in schema:
        ref_name = schema["$ref"].split("/")[-1]
        return ref_name

    t = schema.get("type", "object")
    fmt = schema.get("format", "")
    if t == "array":
        items = schema.get("items", {})
        inner = openapi_to_python_type(items, schemas)
        return f"list[{inner}]"
    if t == "object":
        if schema.get("additionalProperties"):
            val = openapi_to_python_type(schema["additionalProperties"], schemas)
            return f"dict[str, {val}]"
        return "dict[str, Any]"
    if t == "string":
        if fmt == "date-time":
            return "datetime"
        if fmt == "date":
            return "date"
        return "str"
    return {"integer": "int", "number": "float", "boolean": "bool"}.get(t, "Any")


def is_enum(schema: dict) -> bool:
    return bool(schema.get("enum")) or (not schema.get("properties") and not schema.get("type"))


def generate_enum(name: str, schema: dict) -> str:
    doc = schema.get("description", "")
    values = schema.get("enum", [])
    members = "\n    ".join(f'{v} = "{v}"' for v in values)
    return f'''class {name}(StrEnum):
    """{doc}"""
    {members}
'''


def generate_model(name: str, schema: dict, schemas: dict | None = None) -> str:
    doc = schema.get("description", "")
    required: set[str] = set(schema.get("required", []))

    if not schema.get("properties") and schema.get("oneOf"):
        fields = []
        for variant in schema["oneOf"]:
            if variant.get("type") == "object" and variant.get("properties"):
                for fname, fschema in variant["properties"].items():
                    typ = openapi_to_python_type(fschema, schemas)
                    desc = _clean_description(fschema.get("description", "")).strip().rstrip()
                    comment = f"  # {desc}" if desc else ""
                    fields.append(f"    {fname}: {typ} | None = None{comment}")
        field_block = "\n".join(fields) if fields else "    pass"
        return f'''class {name}(BaseModel):
    """{doc}"""
    model_config = ConfigDict(extra="forbid")

{field_block}
'''

    props = schema.get("properties", {})
    if not props:
        return f'''class {name}(BaseModel):
    """{doc}"""
    model_config = ConfigDict(extra="forbid")
'''
    fields = []
    for fname, fschema in props.items():
        typ = openapi_to_python_type(fschema, schemas)
        is_required = fname in required
        default = "" if is_required else " = None"
        if not is_required and typ not in ("Any",):
            typ = f"{typ} | None"
        desc = _clean_description(fschema.get("description", "")).strip().rstrip()
        comment = f"  # {desc}" if desc else ""
        fields.append(f"    {fname}: {typ}{default}{comment}")
    field_block = "\n".join(fields)
    return f'''class {name}(BaseModel):
    """{doc}"""
    model_config = ConfigDict(extra="forbid")

{field_block}
'''


def emit(schema: dict, name: str, schemas: dict | None = None) -> str:
    if is_enum(schema) and schema.get("enum"):
        return generate_enum(name, schema)
    return generate_model(name, schema, schemas)


def _ext_refs_from_schema(name: str, schema: dict, schemas: dict, schema_module: dict) -> set[str]:
    refs: set[str] = set()
    seen: set[str] = set()

    def walk(s: dict) -> None:
        if "$ref" in s:
            rname = s["$ref"].split("/")[-1]
            if (
                rname not in seen
                and schema_module.get(rname)
                and schema_module[rname] != schema_module[name]
            ):
                refs.add(rname)
            seen.add(rname)
        elif s.get("type") == "array":
            walk(s.get("items", {}))
        elif s.get("type") == "object" and s.get("additionalProperties"):
            walk(s["additionalProperties"])

    for fname, fschema in schema.get("properties", {}).items():
        walk(fschema)
    for variant in schema.get("oneOf", []):
        if variant.get("type") == "object" and variant.get("properties"):
            for fname, fschema in variant["properties"].items():
                walk(fschema)
    return refs


def _build_import_block(module_filename: str, refs: set[str], schema_module: dict) -> str:
    grouped: dict[str, list[str]] = {}
    for ref in sorted(refs):
        src = schema_module[ref]
        grouped.setdefault(src, []).append(ref)
    if not grouped:
        return ""
    lines: list[str] = ["if TYPE_CHECKING:"]
    for src in sorted(grouped):
        names = sorted(grouped[src])
        if src == "_core.errors":
            lines.append(f"    from async_amazon_ads_api_v1.errors import {', '.join(names)}")
        else:
            lines.append(f"    from .{src.removesuffix('.py')} import {', '.join(names)}")
    lines.append("del TYPE_CHECKING")
    return "\n".join(lines) + "\n\n"


def _strip_prefix(filename: str) -> str:
    """Remove leading underscore from filename."""
    if filename.startswith("_"):
        return filename[1:]
    return filename


def main(*, output_dir: Path | None = None, product: str | None = None) -> None:
    if product is None or product not in ("sp", "sb", "sd"):
        print("Error: --product must be 'sp', 'sb', or 'sd'", file=sys.stderr)
        sys.exit(1)
    assert output_dir is not None

    spec_path = SPECS[product]
    with open(spec_path) as f:
        data = json.load(f)
    schemas = data["components"]["schemas"]

    result = classify(data)
    groups: dict[str, list[str]] = result["files"]
    schema_module: dict[str, str] = result["classification"]

    # Map shared error schemas to _core.errors so TYPE_CHECKING imports resolve
    for name in SHARED_ERROR_SCHEMAS:
        if name in schema_module:
            schema_module[name] = "_core.errors"

    # Remap file names: strip _ prefix
    def _remap_filename(old: str) -> str:
        return _strip_prefix(old)

    groups = {_remap_filename(k): v for k, v in groups.items()}
    schema_module = {
        k: _remap_filename(v) if v != "_core.errors" else v for k, v in schema_module.items()
    }

    # Remove shared error schemas from all groups (after ref collection)
    for name in SHARED_ERROR_SCHEMAS:
        for mod in list(groups):
            if name in groups[mod]:
                groups[mod].remove(name)

    # Remove empty groups
    groups = {k: v for k, v in groups.items() if v}

    # First pass: collect external type refs per module
    ext_refs: dict[str, set[str]] = {}
    for mod, names in groups.items():
        mod_refs: set[str] = set()
        for n in names:
            refs = _ext_refs_from_schema(n, schemas[n], schemas, schema_module)
            mod_refs.update(refs)
        mod_refs = {r for r in mod_refs if schema_module.get(r) != mod}
        ext_refs[mod] = mod_refs

    # Write files
    output_dir.mkdir(parents=True, exist_ok=True)

    # Track model names per file for __all__
    file_model_names: dict[str, list[str]] = {mod: list(names) for mod, names in groups.items()}

    # __init__.py
    init_parts = [
        f'"""Auto-generated Pydantic models for {product.upper()} from Amazon Ads API schema."""',
        "",
        "from __future__ import annotations",
        "",
        "import sys",
        "import typing",
        "",
    ]
    for module_file in sorted(groups):
        mod = module_file.removesuffix(".py")
        init_parts.append(f"from .{mod} import *")
    init_parts.extend(
        [
            "",
            "# Include shared error types for forward reference resolution",
            "import async_amazon_ads_api_v1.errors as _core_errors",
            "",
            "# Resolve cross-module forward references",
            "_ns: dict[str, typing.Any] = dict(sys.modules[__name__].__dict__)",
            "_ns.update(vars(_core_errors))",
            "for _name, _obj in list(_ns.items()):",
            "    if (",
            "        isinstance(_obj, type)",
            "        and hasattr(_obj, 'model_rebuild')",
            "        and getattr(_obj, '__module__', '').startswith('async_amazon_ads_api_v1.models')",
            "    ):",
            "        _obj.model_rebuild(_types_namespace=_ns)",
        ]
    )
    (output_dir / "__init__.py").write_text("\n".join(init_parts) + "\n")
    print(f"Wrote {output_dir / '__init__.py'}")

    done: set[str] = set()

    def emit_to_file(buf: list[str], name: str) -> None:
        if name in done:
            return
        done.add(name)
        out = emit(schemas[name], name, schemas)
        if out:
            buf.append(out)

    for filename, names in sorted(groups.items()):
        # Determine header based on content
        if filename == "enums.py":
            header = ENUMS_HEADER.format(product=product)
        else:
            header = MODULE_HEADER.format(product=product)

        # Ensure StrEnum import if file contains enums
        if any(is_enum(schemas[n]) and schemas[n].get("enum") for n in names):
            if "StrEnum" not in header:
                header = header.rstrip() + "\nfrom enum import StrEnum\n"

        refs = ext_refs.get(filename, set())
        imports = _build_import_block(filename, refs, schema_module)
        if refs:
            if "TYPE_CHECKING" not in header:
                header = header.replace(
                    "from typing import Any", "from typing import TYPE_CHECKING, Any"
                )
        buf = [header, imports] if imports else [header]
        for n in names:
            emit_to_file(buf, n)
        # Add __all__ to prevent TYPE_CHECKING from being exported via star imports
        all_models = file_model_names.get(filename, [])
        if all_models:
            buf.append(f"\n__all__ = [{', '.join(repr(m) for m in all_models)}]\n")
        (output_dir / filename).write_text("".join(buf) + "\n")
        print(f"Wrote {output_dir / filename}  ({len(names)} models)")

    print(f"\nAll models written to {output_dir}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Pydantic models from OpenAPI schema.")
    parser.add_argument(
        "--product",
        required=True,
        choices=["sp", "sb", "sd"],
        help="Product type: sp (Sponsored Products) or sb (Sponsored Brands)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Output directory (e.g. src/async_amazon_ads_api_v1/models/sp)",
    )
    args = parser.parse_args()
    main(output_dir=args.output_dir, product=args.product)
