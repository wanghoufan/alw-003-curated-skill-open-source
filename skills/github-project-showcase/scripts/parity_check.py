#!/usr/bin/env python3
"""GitHub profile README bilingual list parity check (read-only).

只读脚本：只调用 GitHub 的 GET 接口读取两份 README，不创建、不修改、不删除任何远端资源。
依赖：已登录目标账号的 gh CLI（gh auth login）+ Python 3.9+ 标准库；
      已有本地副本时用 --readme / --readme-en，可完全不联网。

用法：
    python3 scripts/parity_check.py --owner <账号>
    python3 scripts/parity_check.py --owner <账号> --format json --out parity.json
    python3 scripts/parity_check.py --owner <账号> --readme zh.md --readme-en en.md

退出码：0 = PARITY-OK，1 = PARITY-DRIFT，2 = 取不到文件或解析失败。
Windows 上若 python3 不可用，改用 python。
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple

ITEM = re.compile(r"^- \[([^\]]+)\]\((https?://[^)\s]+)\)")
SECTION = re.compile(r"^### (.+?)\s*$")
SUB_COUNT = re.compile(r"[（(]\s*(\d+)\s*[）)]\s*$")
TOTAL = re.compile(r"(?:共\s*(\d+)\s*个|(\d+)\s*total)", re.I)
LINK_LINE = re.compile(r"\[中文\]\(README\.md\).*\[English\]\(README\.en\.md\)")


def run_gh(args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(["gh", "api"] + args, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def fetch_remote(owner: str, repo: str, name: str) -> Optional[str]:
    code, out, err = run_gh([f"repos/{owner}/{repo}/contents/{name}", "--jq", ".content"])
    if code != 0:
        return None
    try:
        return base64.b64decode(out).decode("utf-8", errors="replace")
    except Exception:
        return None


def repo_in(url: str, owner: str) -> Optional[str]:
    """只认指向本账号仓库的链接，取路径首段作仓库名；外部站点与站点地址忽略。"""
    m = re.match(r"https?://github\.com/([^/]+)/([^/?#]+)", url)
    if not m:
        return None
    login, name = m.group(1), m.group(2)
    if login.lower() != owner.lower():
        return None
    name = name[:-4] if name.lower().endswith(".git") else name
    return name.lower()


def repo_target(url: str, owner: str) -> Optional[Tuple[str, str]]:
    """Return the repository-relative GitHub path so tag/release links are compared too."""
    m = re.match(r"https?://github\.com/([^/]+)/([^/?#]+)(/[^?#]*)?", url)
    if not m or m.group(1).lower() != owner.lower():
        return None
    repo = m.group(2)
    if repo.lower().endswith(".git"):
        repo = repo[:-4]
    path = (m.group(3) or "").rstrip("/")
    return repo.lower(), path


def parse(text: str, owner: str) -> dict:
    sections: list[dict] = []
    current = None
    declared_total = None

    for line in text.splitlines():
        if line.startswith("## "):
            hit = TOTAL.search(line)
            if hit and declared_total is None:
                declared_total = int(hit.group(1) or hit.group(2))
            continue
        m = SECTION.match(line)
        if m:
            head = m.group(1)
            sub = SUB_COUNT.search(head)
            current = {
                "title": head,
                "emoji": head.split(" ")[0],
                "declared": int(sub.group(1)) if sub else None,
                "items": [],
            }
            sections.append(current)
            continue
        m = ITEM.match(line)
        if m and current is not None:
            current["items"].append({
                "label": m.group(1),
                "url": m.group(2),
                "repo": repo_in(m.group(2), owner),
                "target": repo_target(m.group(2), owner),
            })

    items = [i for s in sections for i in s["items"]]
    return {
        "declared_total": declared_total,
        "sections": sections,
        "items": items,
        "repos": [i["repo"] for i in items if i["repo"]],
        "non_github": [i["url"] for i in items if not i["repo"]],
        "link_line": bool(LINK_LINE.search(text)),
    }


def diff(zh: dict, en: dict) -> list[dict]:
    problems: list[dict] = []

    for tag, doc in (("zh", zh), ("en", en)):
        if doc["declared_total"] is None:
            problems.append({"kind": "TOTAL_MISSING", "file": tag})
        elif doc["declared_total"] != len(doc["items"]):
            problems.append({"kind": "TOTAL_WRONG", "file": tag,
                             "declared": doc["declared_total"], "actual": len(doc["items"])})
        for sec in doc["sections"]:
            if sec["declared"] is not None and sec["declared"] != len(sec["items"]):
                problems.append({"kind": "SECTION subtotal", "file": tag,
                                 "section": sec["title"],
                                 "declared": sec["declared"], "actual": len(sec["items"])})

    if len(zh["sections"]) != len(en["sections"]):
        problems.append({"kind": "SECTIONS_COUNT", "zh": len(zh["sections"]),
                         "en": len(en["sections"])})
    else:
        for a, b in zip(zh["sections"], en["sections"]):
            if a["emoji"] != b["emoji"]:
                problems.append({"kind": "SECTION_ORDER", "zh": a["title"], "en": b["title"]})
            if a["declared"] != b["declared"]:
                problems.append({"kind": "SECTION_COUNT_MISMATCH", "zh": a["title"],
                                 "en": b["title"], "zh_count": a["declared"],
                                 "en_count": b["declared"]})
            a_repos = [i["repo"] for i in a["items"] if i["repo"]]
            b_repos = [i["repo"] for i in b["items"] if i["repo"]]
            if a_repos != b_repos:
                problems.append({"kind": "SECTION_PROJECTS", "zh": a["title"],
                                 "en": b["title"], "zh_repos": a_repos,
                                 "en_repos": b_repos})

    zh_set, en_set = set(zh["repos"]), set(en["repos"])
    if zh["repos"] != en["repos"]:
        problems.append({"kind": "PROJECT_ORDER", "zh": zh["repos"], "en": en["repos"]})
    zh_targets = {i["repo"]: i["target"] for i in zh["items"] if i["repo"]}
    en_targets = {i["repo"]: i["target"] for i in en["items"] if i["repo"]}
    for repo in sorted(zh_set & en_set):
        if zh_targets.get(repo) != en_targets.get(repo):
            problems.append({"kind": "LINK_MISMATCH", "repo": repo,
                             "zh": zh_targets.get(repo), "en": en_targets.get(repo)})
    for repo in sorted(zh_set - en_set):
        problems.append({"kind": "MISSING_IN_EN", "repo": repo})
    for repo in sorted(en_set - zh_set):
        problems.append({"kind": "MISSING_IN_ZH", "repo": repo})
    for tag, doc in (("zh", zh), ("en", en)):
        dupes = {r for r in doc["repos"] if doc["repos"].count(r) > 1}
        for repo in sorted(dupes):
            problems.append({"kind": "DUPLICATE", "file": tag, "repo": repo})

    for tag, doc in (("zh", zh), ("en", en)):
        if not doc["link_line"]:
            problems.append({"kind": "CROSS_LINK", "file": tag})

    return problems


def render(owner: str, zh: dict, en: dict, problems: list[dict]) -> str:
    lines = [
        f"OWNER {owner}",
        f"ZH sections={len(zh['sections'])} items={len(zh['items'])} declared={zh['declared_total']}",
        f"EN sections={len(en['sections'])} items={len(en['items'])} declared={en['declared_total']}",
    ]
    for i, (a, b) in enumerate(zip(zh["sections"], en["sections"])):
        lines.append(f"SECTION {i + 1} zh={a['declared']}/{len(a['items'])} "
                     f"en={b['declared']}/{len(b['items'])} {a['emoji']}")
    if problems:
        lines.append(f"DRIFT count={len(problems)}")
        for p in problems:
            lines.append("  " + json.dumps(p, ensure_ascii=False, sort_keys=True))
    verdict = "PARITY-OK" if not problems else "PARITY-DRIFT"
    lines.append(f"VERDICT {verdict} zh={len(zh['items'])} en={len(en['items'])}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Bilingual profile README parity check (read-only)")
    parser.add_argument("--owner", required=True, help="GitHub 账号（主页仓库同名）")
    parser.add_argument("--repo", help="主页仓库名，默认与 --owner 同名")
    parser.add_argument("--zh", default="README.md", help="中文文件名，默认 README.md")
    parser.add_argument("--en", default="README.en.md", help="英文文件名，默认 README.en.md")
    parser.add_argument("--readme", help="本地中文 README 路径（给了就不联网）")
    parser.add_argument("--readme-en", help="本地英文 README 路径")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--out", help="把结果以 UTF-8 写入该文件（Windows 下别用 shell 重定向）")
    args = parser.parse_args()

    if args.readme:
        if not args.readme_en:
            print("ERROR: 用了 --readme 就必须同时给 --readme-en", file=sys.stderr)
            return 2
        try:
            zh_text = Path(args.readme).expanduser().read_text(encoding="utf-8")
            en_text = Path(args.readme_en).expanduser().read_text(encoding="utf-8")
        except OSError as exc:
            print(f"ERROR: 本地文件读取失败 {exc}", file=sys.stderr)
            return 2
    else:
        repo = args.repo or args.owner
        zh_text = fetch_remote(args.owner, repo, args.zh)
        en_text = fetch_remote(args.owner, repo, args.en)
        if zh_text is None or en_text is None:
            missing = args.zh if zh_text is None else args.en
            print(f"ERROR: 取不到 {missing}。若账号下确实没有英文版，本校验不适用，"
                  f"要不要开英文版请让用户拍板。", file=sys.stderr)
            return 2

    zh, en = parse(zh_text, args.owner), parse(en_text, args.owner)
    problems = diff(zh, en)

    if args.format == "json":
        text = json.dumps({"owner": args.owner, "zh": {
            "items": len(zh["items"]), "declared_total": zh["declared_total"],
            "sections": [{"title": s["title"], "declared": s["declared"],
                          "actual": len(s["items"])} for s in zh["sections"]]},
            "en": {"items": len(en["items"]), "declared_total": en["declared_total"],
                   "sections": [{"title": s["title"], "declared": s["declared"],
                                 "actual": len(s["items"])} for s in en["sections"]]},
            "verdict": "PARITY-OK" if not problems else "PARITY-DRIFT",
            "problems": problems}, ensure_ascii=False, indent=2)
    else:
        text = render(args.owner, zh, en, problems)

    if args.out:
        Path(args.out).expanduser().write_text(text + "\n", encoding="utf-8")
    else:
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
        print(text)

    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
