"""从 reference_prod.json 下载各实体 OpenAPI 到 data/api-spec-v1/<entity>/。"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx
from _json_io import read_json, write_json

DATA_DIR = Path(__file__).resolve().parent / "data"
SPEC_V1_DIR = DATA_DIR / "api-spec-v1"
REF_PATH = SPEC_V1_DIR / "reference_prod.json"
ROUTE_PREFIX = "api-spec-v1-"


def filename_from_url(url: str) -> str:
    path = urlparse(url).path
    name = path.rsplit("/", 1)[-1]
    if not name:
        raise ValueError(f"无法从 URL 解析文件名: {url}")
    return name


def entity_from_route(route: str) -> str:
    if route.startswith(ROUTE_PREFIX):
        return route.removeprefix(ROUTE_PREFIX)
    return route


def item_by_url(meta: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["openapi"]: item for item in meta["items"]}


def load_meta(meta_path: Path) -> dict[str, Any]:
    if not meta_path.is_file():
        return {"route": "", "entity": "", "items": []}
    return read_json(meta_path)


def remove_stale_specs(out_dir: Path, filenames: set[str]) -> None:
    """Remove specs no longer listed for an entity by reference_prod.json."""
    for path in sorted(out_dir.iterdir()):
        if path.name == "meta.json" or path.name in filenames:
            continue
        if path.is_file():
            path.unlink()
            print(f"removed: {path.relative_to(SPEC_V1_DIR)}")


def remove_stale_entities(entities: set[str]) -> None:
    """Remove entity directories no longer present in reference_prod.json."""
    for path in sorted(SPEC_V1_DIR.iterdir()):
        if not path.is_dir() or path.name in entities:
            continue
        shutil.rmtree(path)
        print(f"removed: {path.relative_to(SPEC_V1_DIR)}")


def main() -> None:
    data = read_json(REF_PATH)
    active_entities: set[str] = set()

    with httpx.Client(timeout=60.0, follow_redirects=True) as client:
        for entry in data:
            for route_entry in entry["routes"]:
                route = route_entry["route"]
                entity = entity_from_route(route)
                active_entities.add(entity)
                out_dir = SPEC_V1_DIR / entity
                out_dir.mkdir(parents=True, exist_ok=True)

                meta_path = out_dir / "meta.json"
                prev = item_by_url(load_meta(meta_path))
                items_meta: list[dict[str, Any]] = []
                content_changed = False

                for item in route_entry["items"]:
                    url = item["openapi"]
                    name = item["name"]
                    filename = filename_from_url(url)
                    dest = out_dir / filename
                    old = prev[url] if url in prev else None

                    headers: dict[str, str] = {}
                    if dest.is_file() and old is not None and "etag" in old and old["etag"]:
                        headers["If-None-Match"] = old["etag"]

                    resp = client.get(url, headers=headers)

                    if resp.status_code == 304:
                        assert old is not None
                        print(f"skip(304): {entity}/{filename}")
                        items_meta.append(
                            {
                                "name": name,
                                "openapi": url,
                                "file": filename,
                                "etag": old["etag"],
                                "last_modified": old["last_modified"] if "last_modified" in old else None,
                                "size": dest.stat().st_size,
                            }
                        )
                        continue

                    resp.raise_for_status()
                    write_json(dest, resp.json())
                    content_changed = True
                    etag = resp.headers["etag"] if "etag" in resp.headers else None
                    last_modified = resp.headers["last-modified"] if "last-modified" in resp.headers else None
                    print(f"saved: {entity}/{filename} ({dest.stat().st_size} bytes)")
                    items_meta.append(
                        {
                            "name": name,
                            "openapi": url,
                            "file": filename,
                            "etag": etag,
                            "last_modified": last_modified,
                            "size": dest.stat().st_size,
                        }
                    )

                meta = {"route": route, "entity": entity, "items": items_meta}
                if content_changed or not meta_path.is_file() or read_json(meta_path) != meta:
                    write_json(meta_path, meta)
                remove_stale_specs(out_dir, {item["file"] for item in items_meta})

    remove_stale_entities(active_entities)


if __name__ == "__main__":
    main()
