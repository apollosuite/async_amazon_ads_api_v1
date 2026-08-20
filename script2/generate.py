"""Generate ads_api v1 models and clients from script2/data/api-spec-v1.

Usage:
    uv run python script2/generate.py
"""

from __future__ import annotations

import argparse
import copy
import shutil
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from codegen.emit import render_client_module, render_models_module, render_shared_module
from codegen.schema import EmittedModel, NameMap, discover_emissions, select_shared_models
from codegen.spec import (
    ALL,
    PRODUCT_ORDER,
    Product,
    apply_schema_prefix,
    camel_to_snake,
    drop_covered_operations,
    iter_operations,
    load_json,
    operation_keys,
    product_from_filename,
    unique_tags,
)

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
SPEC_ROOT = HERE / "data" / "api-spec-v1"
PACKAGE_ROOT = PROJECT / "src" / "ads_api"
CLIENT_ROOT = PACKAGE_ROOT / "client" / "v1"
MODELS_ROOT = PACKAGE_ROOT / "models" / "v1"


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path.relative_to(PROJECT)}")


def _ensure_pkg(path: Path) -> None:
    init = path / "__init__.py"
    if not init.exists():
        _write(init, "")


_PRODUCT_MODULES = {product.module for product in PRODUCT_ORDER}


def render_product_namespace(product: Product, entities: list[tuple[str, str]]) -> str:
    """entities: list of (entity_snake, resource_class)."""
    entities = sorted(entities)
    cls = product.prefix
    lines = [
        f'"""{product.prefix} resource namespace — entity-specific clients."""',
        "",
        "from __future__ import annotations",
        "",
        "from ads_api.base import ClientContext",
        "",
    ]
    for module, resource_cls in entities:
        lines.append(f"from .{module} import {resource_cls}")
    lines.append("")
    lines.append("")
    lines.append(f"class {cls}:")
    lines.append(f'    """Lazy entity-specific {product.prefix} resources."""')
    lines.append("")
    lines.append("    def __init__(self, ctx: ClientContext) -> None:")
    lines.append("        self._ctx = ctx")
    for module, resource_cls in entities:
        lines.append(f"        self.__{module}: {resource_cls} | None = None")
    lines.append("")
    for module, resource_cls in entities:
        lines.append("    @property")
        lines.append(f"    def {module}(self) -> {resource_cls}:")
        lines.append(f"        if self.__{module} is None:")
        lines.append(f"            self.__{module} = {resource_cls}(self._ctx)")
        lines.append(f"        return self.__{module}")
        lines.append("")
    return "\n".join(lines)


def _append_lazy_properties(lines: list[str], attrs: list[tuple[str, str]]) -> None:
    for name, cls in attrs:
        lines.append("    @property")
        lines.append(f"    def {name}(self) -> {cls}:")
        lines.append(f"        if self.__{name} is None:")
        lines.append(f"            self.__{name} = {cls}(self._ctx)")
        lines.append(f"        return self.__{name}")
        lines.append("")


def render_v1_client(products: list[Product], entities: list[tuple[str, str]]) -> str:
    """entities: top-level ALL resources as (module, resource_class)."""
    attrs = [(product.module, product.prefix) for product in products] + sorted(entities)
    lines = [
        '"""Amazon Ads API v1 async client."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, overload",
        "",
        "from ads_api.base import ClientContext",
        "from ads_api.config.settings import AmazonAdsConfig",
        "from ads_api.errors import MissingConfigError",
        "",
    ]
    for product in products:
        lines.append(f"from ads_api.client.v1.{product.module} import {product.prefix}")
    for module, cls in entities:
        lines.append(f"from ads_api.client.v1.{module} import {cls}")
    lines.append("")
    lines.append("")
    lines.append("class AdsClientV1:")
    lines.append('    """Async client for Amazon Ads API v1.')
    lines.append("")
    lines.append("    Ad products are nested; unscoped APIs hang off the client:")
    lines.append("")
    lines.append("        async with AdsClientV1(config) as ads:")
    lines.append("            await ads.sp.campaigns.create_campaign(body)")
    lines.append("            await ads.selling_accounts.query_selling_account(body)")
    lines.append('    """')
    lines.append("")
    lines.append("    @overload")
    lines.append("    def __init__(self, config: AmazonAdsConfig) -> None: ...")
    lines.append("")
    lines.append("    @overload")
    lines.append("    def __init__(self, *, ctx: ClientContext) -> None: ...")
    lines.append("")
    lines.append(
        "    def __init__(\n"
        "        self,\n"
        "        config: AmazonAdsConfig | None = None,\n"
        "        *,\n"
        "        ctx: ClientContext | None = None,\n"
        "    ) -> None:"
    )
    lines.append("        if ctx is not None:")
    lines.append("            self._ctx = ctx")
    lines.append("            self._owns_ctx = False")
    lines.append("        elif config is not None:")
    lines.append("            self._ctx = ClientContext(config)")
    lines.append("            self._owns_ctx = True")
    lines.append("        else:")
    lines.append("            raise MissingConfigError()")
    for name, cls in attrs:
        lines.append(f"        self.__{name}: {cls} | None = None")
    lines.append("")
    lines.append("    async def __aenter__(self) -> AdsClientV1:")
    lines.append("        return self")
    lines.append("")
    lines.append("    async def __aexit__(self, *args: Any) -> None:")
    lines.append("        await self.close()")
    lines.append("")
    lines.append("    async def close(self) -> None:")
    lines.append("        if self._owns_ctx:")
    lines.append("            await self._ctx.close()")
    lines.append("")
    _append_lazy_properties(lines, attrs)
    return "\n".join(lines)


@dataclass
class ProductWork:
    product: Product
    spec: dict[str, Any]
    endpoints: list[tuple[str, str, dict[str, Any]]]
    emitted: list[EmittedModel]
    name_map: NameMap
    resource_name: str


@dataclass
class EntityWork:
    entity: str
    tag: str
    entity_snake: str
    products: list[ProductWork]


def prepare_entity(entity: str) -> EntityWork:
    entity_dir = SPEC_ROOT / entity
    meta_path = entity_dir / "meta.json"
    if not meta_path.is_file():
        raise SystemExit(f"找不到 spec: {meta_path}")

    meta = load_json(meta_path)
    items = meta["items"]
    by_product = {product_from_filename(item["file"]): entity_dir / item["file"] for item in items}
    specs = {product: load_json(path) for product, path in by_product.items()}
    sample = next(iter(specs.values()))
    tags = unique_tags(sample)
    if len(tags) != 1:
        raise SystemExit(f"{entity}: 期望恰好 1 个 OpenAPI tag，实际 {tags}")
    tag = tags[0]
    entity_snake = camel_to_snake(tag)

    covered: set[tuple[str, str]] = set()
    for product, spec in specs.items():
        if product is not ALL:
            covered |= operation_keys(spec)

    model_dir = MODELS_ROOT / entity_snake
    products: list[ProductWork] = []
    print(f"\n=== {entity} (tag={tag}) ===")
    for product in PRODUCT_ORDER:
        if product not in specs:
            continue
        spec = copy.deepcopy(specs[product])
        if product is ALL:
            drop_covered_operations(spec, covered)
            remaining = iter_operations(spec)
            if not remaining:
                print("  skip ALL: 全部操作已被产品 spec 覆盖")
                for leftover in (
                    model_dir / "all.py",
                    model_dir / f"{ALL.module}.py",
                    CLIENT_ROOT / "all" / f"{entity_snake}.py",
                    CLIENT_ROOT / f"{entity_snake}.py",
                ):
                    if leftover.exists():
                        leftover.unlink()
                        print(f"  removed {leftover.relative_to(PROJECT)}")
                continue
            print(f"  {ALL.module}: 保留 {len(remaining)} 个独有操作")
        else:
            print(f"  {product.module}: {len(iter_operations(spec))} operations")

        if product.prefix:
            apply_schema_prefix(spec, product.prefix)
        endpoints = iter_operations(spec)
        emitted, name_map = discover_emissions(spec, endpoints)
        products.append(
            ProductWork(
                product=product,
                spec=spec,
                endpoints=endpoints,
                emitted=emitted,
                name_map=name_map,
                resource_name=f"{product.prefix}{tag}" if product.prefix else tag,
            )
        )

    if not products:
        raise SystemExit(f"{entity}: 没有生成任何产品模块")
    return EntityWork(entity=entity, tag=tag, entity_snake=entity_snake, products=products)


def _collect_shared(works: list[EntityWork]) -> dict[str, list[EmittedModel]]:
    groups: dict[str, list[list[EmittedModel]]] = defaultdict(list)
    for work in works:
        for product_work in work.products:
            groups[product_work.product.module].append(product_work.emitted)
    shared: dict[str, list[EmittedModel]] = {}
    for module, emitted_groups in groups.items():
        items = select_shared_models(emitted_groups)
        if items:
            shared[module] = items
            names = ", ".join(item.python_name for item in items)
            print(f"  shared {module}: {names}")
    return shared


def _write_shared(shared_by_product: dict[str, list[EmittedModel]], generated_modules: set[str]) -> None:
    shared_dir = MODELS_ROOT / "_shared"
    _ensure_pkg(MODELS_ROOT)
    _ensure_pkg(shared_dir)
    for module, items in shared_by_product.items():
        _write(shared_dir / f"{module}.py", render_shared_module(module, items, NameMap(items)))
    valid_modules = {product.module for product in PRODUCT_ORDER}
    for module in generated_modules:
        path = shared_dir / f"{module}.py"
        if module not in shared_by_product and path.exists():
            path.unlink()
            print(f"  removed {path.relative_to(PROJECT)}")
    for path in sorted(shared_dir.glob("*.py")):
        if path.name != "__init__.py" and path.stem not in valid_modules:
            path.unlink()
            print(f"  removed {path.relative_to(PROJECT)}")


def write_entity(work: EntityWork, shared_by_product: dict[str, list[EmittedModel]]) -> None:
    model_dir = MODELS_ROOT / work.entity_snake
    _ensure_pkg(MODELS_ROOT)
    _ensure_pkg(CLIENT_ROOT)
    _ensure_pkg(model_dir)

    generated_modules: set[str] = set()
    for product_work in work.products:
        module = product_work.product.module
        generated_modules.add(module)
        shared_items = shared_by_product.get(module, [])
        shared_names = {item.python_name for item in shared_items}
        models_import = f"ads_api.models.v1.{work.entity_snake}.{module}"
        _write(
            model_dir / f"{module}.py",
            render_models_module(
                work.tag,
                product_work.emitted,
                product_work.name_map,
                shared_names=shared_names,
                shared_module=module if shared_names else None,
            ),
        )
        if product_work.product is ALL:
            client_path = CLIENT_ROOT / f"{work.entity_snake}.py"
        else:
            client_dir = CLIENT_ROOT / module
            _ensure_pkg(client_dir)
            client_path = client_dir / f"{work.entity_snake}.py"
        _write(
            client_path,
            render_client_module(
                spec=product_work.spec,
                tag=work.tag,
                resource_name=product_work.resource_name,
                models_import=models_import,
                endpoints=product_work.endpoints,
                emitted=product_work.emitted,
                name_map=product_work.name_map,
            ),
        )

    _write(model_dir / "__init__.py", "")
    for path in sorted(model_dir.glob("*.py")):
        if path.name == "__init__.py" or path.stem in generated_modules:
            continue
        path.unlink()
        print(f"  removed {path.relative_to(PROJECT)}")


def _cleanup_legacy_entity_client_dirs() -> None:
    client_root = CLIENT_ROOT
    if not client_root.exists():
        return
    for path in sorted(client_root.iterdir()):
        if not path.is_dir() or path.name in _PRODUCT_MODULES or path.name == "__pycache__":
            continue
        shutil.rmtree(path)
        print(f"  removed {path.relative_to(PROJECT)}")


def _remove_empty_product_dirs(products: list[Product]) -> None:
    client_root = CLIENT_ROOT
    if not client_root.exists():
        return
    active_modules = {product.module for product in products}
    for product in PRODUCT_ORDER:
        if product is ALL or product.module in active_modules:
            continue
        product_dir = client_root / product.module
        if not product_dir.is_dir():
            continue
        shutil.rmtree(product_dir)
        print(f"  removed {product_dir.relative_to(PROJECT)}")


def write_client_namespaces(works: list[EntityWork]) -> None:
    product_entities: dict[Product, list[tuple[str, str]]] = defaultdict(list)
    top_level_entities: list[tuple[str, str]] = []
    for work in works:
        for product_work in work.products:
            entity = (work.entity_snake, product_work.resource_name)
            if product_work.product is ALL:
                top_level_entities.append(entity)
            else:
                product_entities[product_work.product].append(entity)

    products = [product for product in PRODUCT_ORDER if product in product_entities]
    _cleanup_legacy_entity_client_dirs()
    _remove_empty_product_dirs(products)
    for product in products:
        product_dir = CLIENT_ROOT / product.module
        expected_files = {f"{mod}.py" for mod, _ in product_entities[product]} | {"__init__.py"}
        for path in sorted(product_dir.glob("*.py")):
            if path.name not in expected_files:
                path.unlink()
                print(f"  removed {path.relative_to(PROJECT)}")
        _write(product_dir / "__init__.py", render_product_namespace(product, product_entities[product]))

    expected_top_level = {f"{mod}.py" for mod, _ in top_level_entities} | {"__init__.py"}
    for path in sorted(CLIENT_ROOT.glob("*.py")):
        if path.name not in expected_top_level:
            path.unlink()
            print(f"  removed {path.relative_to(PROJECT)}")

    _write(
        CLIENT_ROOT / "__init__.py",
        render_v1_client(products, top_level_entities),
    )


def generate_all() -> None:
    works = [prepare_entity(entity) for entity in list_entities()]
    shared_by_product = _collect_shared(works)
    generated_modules = {pw.product.module for work in works for pw in work.products}
    _write_shared(shared_by_product, generated_modules)
    for work in works:
        write_entity(work, shared_by_product)
    write_client_namespaces(works)


def list_entities() -> list[str]:
    return sorted(p.name for p in SPEC_ROOT.iterdir() if p.is_dir() and (p / "meta.json").is_file())


def run_format() -> None:
    src = str(PACKAGE_ROOT)
    scripts = str(HERE)
    for cmd, label in (
        (["uv", "run", "black", src, scripts], "black"),
        (["uv", "run", "ruff", "check", "--fix", src, scripts], "ruff"),
    ):
        print(f"\n── {label}")
        result = subprocess.run(cmd, cwd=PROJECT, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        if result.returncode != 0:
            raise SystemExit(result.returncode)
        print(f"  ✓ {label}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate ads_api v1 from per-entity OpenAPI specs")
    parser.add_argument("--no-format", action="store_true", help="跳过 black/ruff")
    args = parser.parse_args()

    generate_all()
    if not args.no_format:
        run_format()
    print("\nDone.")


if __name__ == "__main__":
    main()
