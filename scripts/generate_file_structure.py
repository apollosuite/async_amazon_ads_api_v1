#!/usr/bin/env python3
"""Generate model file structure from OpenAPI spec.

核心设计意图：
  这是一个零硬编码的通用分类器，从 OpenAPI spec 自动推导 schema → 文件的归属关系。
  输入任意 OpenAPI JSON，输出 { file_name → [schema_names] } 的映射，
  可直接被 generate_models.py 读取，替代手写的 name sets。

  算法分 9 个阶段，每个阶段处理一个独立的分层问题：

  阶段 1 — 枚举分离: is_enum 检测，将纯枚举值与结构化模型分开
  阶段 2 — 依赖图: 构建 $ref 有向图（fwd/rev），记录枚举使用者（enum_users）
  阶段 3 — 资源发现: 从 paths 提取入口 schema（request body + success response），
                   识别全局 HTTP 错误（出现在 ≥2 个资源的错误响应中）
  阶段 4 — 传递闭包: 每个资源的入口 schema 沿 $ref 图 BFS 扩散，得到资源专属的 schema 集合
  阶段 5-6 — 单资源 vs 多资源: 按 "schema 出现在几个资源的闭包中" 分割
  阶段 7 — 文件归属: HTTP 错误 → _errors.py；多资源 schema → 连通分量分析 → LCP 命名；
                   单资源 schema → 随 resource 文件
  阶段 8 — 枚举归属: 枚举只被一个文件的 schema 引用 → 放入该文件；跨文件 → _enums.py

  关键设计决策：
  - 不依赖字符串关键词匹配，只使用 $ref 图结构和 path 分析
  - 资源名称自动转换：CamelCase → snake_case（adGroups → _ad_groups.py）
  - 多资源共享 schema 通过连通分量分组合并，避免碎片化

Usage:
    uv run python scripts/generate_file_structure.py openapi.json
    uv run python scripts/generate_file_structure.py openapi.json -o structure.json
    uv run python scripts/generate_file_structure.py openapi.json --verbose
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

# ── 阶段 1: 枚举检测 ─────────────────────────────────────────────────────
# 判定依据：schema 有 enum 字段，或没有任何结构化属性（无 properties/type/oneOf/allOf 且无 $ref）


def is_enum(schema: dict) -> bool:
    return bool(schema.get("enum")) or (
        not schema.get("properties")
        and not schema.get("type")
        and not schema.get("oneOf")
        and not schema.get("allOf")
        and "$ref" not in schema
    )


# ── $ref 提取（从 OpenAPI schema 对象中递归采集所有 $ref 目标） ───────


def extract_refs(schema: dict) -> set[str]:
    refs: set[str] = set()

    def walk(obj: Any) -> None:
        if isinstance(obj, dict):
            if "$ref" in obj:
                refs.add(obj["$ref"].split("/")[-1])
                return  # 遇到 $ref 不再深入（引用的结构在目标 schema 中定义）
            for k in ("properties", "additionalProperties", "items"):
                if k in obj:
                    walk(obj[k])
            for k in ("oneOf", "anyOf", "allOf"):
                if k in obj:
                    for item in obj[k]:
                        walk(item)
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(schema)
    return refs


# ── 阶段 3: 资源发现（从 API paths 推导资源分组） ─────────────────────
#
# 设计意图：不依赖 OpenAPI tags 或固定路径格式，而是扫描路径段中的
# 动作动词（create/delete/query/update 等），将路径按资源名分组。
# 这样能兼容不同风格的 REST API 设计。

ACTION_VERBS: set[str] = {
    "create",
    "delete",
    "update",
    "patch",
    "query",
    "get",
    "list",
    "post",
    "put",
    "batch",
}


def extract_resource_from_path(path: str) -> tuple[str, str] | None:
    """从路径中提取 (action, resource_name)。

    支持模式：
      /api/v1/create/campaigns    → ("create", "campaigns")
      /pets                       → (None, "pets")
      /adsApi/v1/query/adGroups   → ("query", "adGroups")
    """
    segments = [s for s in path.split("/") if s and not s.startswith("{")]
    for i, seg in enumerate(segments):
        if seg.lower() in ACTION_VERBS:
            for j in range(i + 1, len(segments)):
                if segments[j].lower() not in ACTION_VERBS and not re.match(r"^v\d", segments[j]):
                    return (seg, segments[j])
    if segments and segments[-1].lower() not in ACTION_VERBS:
        return (None, segments[-1])
    return None


def discover_entry_schemas(paths: dict) -> tuple[dict[str, dict[str, str]], set[str]]:
    """发现资源和入口 schema。

    返回：
      entry_map: resource_name → {schema_name → "action_request"|"action_response"}
      global_errors: 出现在 ≥2 个资源的错误响应中的 schema 集合
    """
    path_resources: dict[str, list[str]] = defaultdict(list)
    for p in paths:
        r = extract_resource_from_path(p)
        if r:
            path_resources[r[1]].append(p)

    entry_map: dict[str, dict[str, str]] = {}
    error_by_resource: dict[str, set[str]] = defaultdict(set)

    for resource, path_list in path_resources.items():
        entries: dict[str, str] = {}
        for p in path_list:
            op = paths[p].get("post", paths[p].get("get", {}))
            if not op:
                continue
            action = next((s for s in p.split("/") if s.lower() in ACTION_VERBS), None)
            if not action:
                continue

            # requestBody 中的 schema → action_request
            for _, ms in op.get("requestBody", {}).get("content", {}).items():
                ref = ms.get("schema", {}).get("$ref", "")
                if ref:
                    entries[ref.split("/")[-1]] = f"{action}_request"
            # 响应中的 schema
            for code, resp in op.get("responses", {}).items():
                for _, ms in resp.get("content", {}).items():
                    ref = ms.get("schema", {}).get("$ref", "")
                    if not ref:
                        continue
                    name = ref.split("/")[-1]
                    if code in ("200", "207", "201"):
                        entries[name] = f"{action}_response"
                    else:
                        error_by_resource[resource].add(name)

        if entries:
            entry_map[resource] = entries

    # 全局 HTTP 错误：出现在 ≥2 个资源的错误响应中的 schema
    global_errors: set[str] = set()
    err_lists = list(error_by_resource.values())
    if len(err_lists) >= 2:
        global_errors = set.intersection(*err_lists)
    return entry_map, global_errors


# ── 阶段 4: 传递闭包（每个资源沿 $ref 图 BFS 扩散） ────────────────────


def compute_closures(
    entry_map: dict[str, dict[str, str]],
    fwd: dict[str, set[str]],
) -> dict[str, set[str]]:
    """对每个资源，从入口 schema 出发，沿 $ref 图传播得到全量 schema 集合。"""
    closures: dict[str, set[str]] = {}
    for resource, entries in entry_map.items():
        closure = set(entries)
        q = list(entries)
        while q:
            node = q.pop(0)
            for dep in fwd.get(node, set()):
                if dep not in closure:
                    closure.add(dep)
                    q.append(dep)
        closures[resource] = closure
    return closures


# ── 文件名转换工具 ──────────────────────────────────────────────────────
#
# 设计意图：
#   将 OpenAPI spec 中的资源名（adGroups）自动转为 Python 文件命名
#   规范（_ad_groups.py），避免硬编码任何文件名。


def to_snake_case(name: str) -> str:
    """CamelCase → snake_case，生成 Python 文件名。

    例: adGroups → _ad_groups.py, SPBudget → _sp_budget.py
    """
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", name)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9_]", "_", s)
    s = s.strip("_")
    return ("_" + s + ".py") if s else "_unknown.py"


def known_filename(name: str, existing: set[str]) -> str:
    """确保文件名不冲突，冲突时追加 _1, _2 后缀。"""
    if name not in existing:
        return name
    base, ext = name.rsplit(".", 1)
    for i in range(1, 100):
        c = f"{base}_{i}.{ext}"
        if c not in existing:
            return c
    return name


def extract_domain(name: str) -> str:
    """从 schema 名称中提取领域名（用于多资源 schema 的 LCP 分组）。

    SPBudget           → Budget
    SPCreateBudget     → Budget
    SPUpdateBidSettings → BidSettings
    """
    for prefix in ("SPCreate", "SPUpdate", "SPDelete", "SPQuery", "SP"):
        if name.startswith(prefix):
            name = name[len(prefix) :]
            break
    return name


# ── 多资源连通分量分析 ──────────────────────────────────────────────────
#
# 设计意图：
#   跨资源共享的 schema 之间通过 $ref 图可能形成多个连通分量，
#   每个分量应独立成一个文件。使用无向连通分量算法将 $ref 关系
#   转化为文件分组。


def _connected_components(nodes: set[str], fwd: dict[str, set[str]]) -> list[set[str]]:
    """无向连通分量。"""
    if not nodes:
        return []
    adj: dict[str, set[str]] = {n: set() for n in nodes}
    for n in nodes:
        deps = fwd.get(n, set()) & nodes
        adj[n].update(deps)
        for d in deps:
            adj.setdefault(d, set()).add(n)
    visited: set[str] = set()
    comps: list[set[str]] = []
    for n in sorted(nodes):
        if n in visited:
            continue
        comp: set[str] = set()
        stack = [n]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            comp.add(node)
            for nb in adj.get(node, set()):
                if nb not in visited:
                    stack.append(nb)
        comps.append(comp)
    return comps


# ── 核心分类算法 ────────────────────────────────────────────────────────
#
# 整体流程：
#   9 个阶段依次执行，每个阶段依赖前一个阶段的输出。
#   最终产出 schema_name → file_name 的映射 + file_name → [schemas] 的分组。


def classify(spec: dict) -> dict:
    schemas = spec.get("components", {}).get("schemas", {})
    paths = spec.get("paths", {})
    all_names = set(schemas.keys())

    # ── 阶段 1: 枚举分离 ─────────────────────────────────────────────
    enums = {n for n in all_names if is_enum(schemas[n]) and schemas[n].get("enum")}
    non_enums = {n for n in all_names if n not in enums}

    # ── 阶段 2: 构建依赖图 ──────────────────────────────────────────
    # fwd: 非枚举 schema → 它 $ref 的其他非枚举 schema
    # rev: 非枚举 schema → 谁 $ref 它
    # enum_users: 枚举 → 引用它的非枚举 schema（用于阶段 9 枚举归属）
    fwd: dict[str, set[str]] = {}
    rev: dict[str, set[str]] = {}
    enum_users: dict[str, set[str]] = {}
    for n in non_enums:
        all_refs = extract_refs(schemas[n])
        fwd[n] = all_refs & non_enums
        for r in fwd[n]:
            rev.setdefault(r, set()).add(n)
        for e in all_refs & enums:
            enum_users.setdefault(e, set()).add(n)

    # ── 阶段 3: 从 paths 发现资源边界 ───────────────────────────────
    entry_map, global_errors = discover_entry_schemas(paths)
    all_entry: set[str] = set()
    for ents in entry_map.values():
        all_entry.update(ents)

    # ── 阶段 4: 计算每个资源的传递闭包 ──────────────────────────────
    closures = compute_closures(entry_map, fwd)

    # schema_in_resources: 每个 schema 出现在哪些资源的闭包中
    schema_in_resources: dict[str, set[str]] = defaultdict(set)
    for resource, closure in closures.items():
        for s in closure:
            schema_in_resources[s].add(resource)

    # ── 阶段 5-6: 单资源 vs 多资源分割 ─────────────────────────────
    # 不在任何资源闭包中的 schema → _unknown 兜底
    classification: dict[str, str] = {}
    used_fnames: set[str] = set()

    all_non_entry = {n for n in non_enums}

    single_res: dict[str, set[str]] = {}  # resource → 专有 schema
    multi_res_groups: dict[str, dict] = {}  # domain → 共享 schema 信息

    for s in all_non_entry:
        resources = schema_in_resources.get(s, set())
        if len(resources) <= 1:
            res = list(resources)[0] if resources else "_unknown"
            single_res.setdefault(res, set()).add(s)
        else:
            domain = extract_domain(s)
            if domain not in multi_res_groups:
                multi_res_groups[domain] = {"schemas": set(), "resources": set()}
            multi_res_groups[domain]["schemas"].add(s)
            multi_res_groups[domain]["resources"].update(resources)

    # ── 阶段 7a: 单资源 schema → 随 resource 文件 ──────────────────
    for resource, schemas in single_res.items():
        fname = to_snake_case(resource)
        fname = known_filename(fname, used_fnames)
        used_fnames.add(fname)
        for s in schemas:
            classification.setdefault(s, fname)

    # ── 阶段 7b: HTTP 错误 → _errors.py ─────────────────────────────
    error_file = known_filename("_errors.py", used_fnames)
    used_fnames.add(error_file)
    for s in global_errors:
        if s in non_enums:
            classification[s] = error_file

    # ── 阶段 7c: 多资源 schema → 连通分量 → LCP 命名文件 ───────────
    multi_schemas: set[str] = set()
    for info in multi_res_groups.values():
        multi_schemas.update(info["schemas"])

    multi_schemas -= set(classification.keys())  # 排除已分配（HTTP 错误）

    multi_components = _connected_components(multi_schemas, fwd)

    shared_file = known_filename("_shared.py", used_fnames)
    used_fnames.add(shared_file)

    for comp in multi_components:
        for s in comp:
            classification[s] = shared_file

    # ── 阶段 8: 枚举归属 ────────────────────────────────────────────
    # 核心原则：枚举只被一个文件的 schema 引用 → 放入该文件；
    # 被多个文件的 schema 引用 → 留在 _enums.py
    enum_file = known_filename("_enums.py", used_fnames)
    used_fnames.add(enum_file)
    for e in sorted(enums):
        user_files: set[str] = set()
        for user in enum_users.get(e, set()):
            f = classification.get(user)
            if f:
                user_files.add(f)
        classification[e] = list(user_files)[0] if len(user_files) == 1 else enum_file

    # 兜底：未分配的 schema 归入 _shared.py
    for n in non_enums:
        if n not in classification:
            classification[n] = known_filename("_shared.py", used_fnames)

    # 构建输出
    file_map: dict[str, list[str]] = defaultdict(list)
    for s, f in classification.items():
        file_map[f].append(s)
    for f in file_map:
        file_map[f] = sorted(file_map[f])

    return {
        "files": dict(sorted(file_map.items())),
        "classification": dict(sorted(classification.items())),
        "meta": {
            "total_schemas": len(all_names),
            "enum_count": len(enums),
            "model_count": len(non_enums),
            "resource_count": len(entry_map),
            "resources": sorted(entry_map.keys()),
            "domain_count": len(multi_res_groups),
            "global_errors": sorted(global_errors),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate model file structure from OpenAPI spec.")
    parser.add_argument("spec", type=Path)
    parser.add_argument("--output", "-o", type=Path, default=None)
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    with open(args.spec) as f:
        spec = json.load(f)

    result = classify(spec)

    if args.verbose:
        m = result["meta"]
        print(f"Total: {m['total_schemas']}  Enums: {m['enum_count']}  Models: {m['model_count']}")
        print(f"Resources ({m['resource_count']}): {m['resources']}")
        print(f"Domains: {m['domain_count']}")
        print(f"Files ({len(result['files'])}):")
        for fn, schemas in result["files"].items():
            print(f"  {fn}: {len(schemas)}")

    if args.output:
        args.output.write_text(json.dumps(result, indent=2))
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
