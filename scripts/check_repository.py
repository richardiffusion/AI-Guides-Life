#!/usr/bin/env python3
"""Check the public framework surface; this is a heuristic, not a DLP guarantee."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


DOMAINS = (
    "01-daily-routine", "02-sleep", "03-nutrition", "04-hydration",
    "05-fitness", "06-commute", "07-reading", "08-travel", "09-social",
)
REQUIRED = {
    "README.md", "AGENTS.md", "CONTRIBUTING.md", ".gitignore",
    "docs/privacy.md", "docs/quick-start.md", "docs/methodology.md",
    "docs/cross-domain.md", "docs/automation.md", "docs/evidence.md",
    "docs/roadmap.md", "prompts/core.md", "prompts/planning.md",
    "prompts/review.md", "templates/personal-setup.md",
    "templates/daily-plan.md", "templates/weekly-review.md",
    "templates/experiment.md", "templates/automation-contract.md",
    "templates/source-check.md", "examples/fictional-walkthrough.md",
    "scripts/check_repository.py", ".github/workflows/check.yml",
} | {f"domains/{domain}/README.md" for domain in DOMAINS}
SPECIAL = {
    "README.md", "AGENTS.md", "CONTRIBUTING.md", ".gitignore",
    "scripts/check_repository.py", ".github/workflows/check.yml",
}
DOC_ROOTS = {"docs", "domains", "prompts", "templates", "examples"}
SECTION_LABELS = (
    "私有输入", "操作流程", "可复制提示词", "预期输出", "回退与复盘",
)
PATTERNS = (
    ("邮箱形式", re.compile(r"(?<![\w.+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?!\w)")),
    ("手机号码形式", re.compile(r"(?<![\w])(?:\+?86[- ]?)?1[3-9]\d{9}(?!\w)")),
    ("国际电话形式", re.compile(r"(?<!\w)\+\d(?:[ ()-]*\d){7,14}(?!\w)")),
    ("本机用户绝对路径", re.compile(r"/(?:Users|home)/[^\s<>\"']+|\b[A-Za-z]:\\(?:Users|Documents and Settings)\\[^\s<>\"']+")),
    ("私钥标记", re.compile(r"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----")),
    ("常见访问凭据形式", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|sk-(?:proj-)?[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16})\b")),
    ("带用户信息的链接", re.compile(r"https?://[^\s/]+@")),
)
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")


def allowed(relative: Path) -> bool:
    name = relative.as_posix()
    return name in SPECIAL or (
        relative.parts[0] in DOC_ROOTS
        and relative.suffix == ".md"
        and all(re.fullmatch(r"[A-Za-z0-9_.-]+", part) for part in relative.parts)
    )


def anchors(content: str) -> set[str]:
    result: set[str] = set()
    counts: dict[str, int] = {}
    in_code = False
    for line in content.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            slug = re.sub(r"[^\w -]", "", match.group(1).lower()).replace(" ", "-")
            count = counts.get(slug, 0)
            counts[slug] = count + 1
            result.add(f"{slug}-{count}" if count else slug)
    return result


def inspect(root: Path, forbidden: list[str]) -> tuple[list[str], int]:
    errors: list[str] = []
    texts: dict[Path, str] = {}
    seen: set[str] = set()

    def raise_walk_error(error: OSError) -> None:
        raise error

    for parent, directories, names in os.walk(root, followlinks=False, onerror=raise_walk_error):
        parent_path = Path(parent)
        # Git's internal database is outside the document scan. History needs a separate audit.
        if parent_path == root and ".git" in directories:
            directories.remove(".git")
        for directory in list(directories):
            location = parent_path / directory
            relative = location.relative_to(root)
            if location.is_symlink():
                errors.append("发现目录符号链接；路径省略，请人工检查。")
                directories.remove(directory)
            elif relative.parts[0] not in DOC_ROOTS | {"scripts", ".github"}:
                errors.append("发现非约定目录；路径省略，请人工检查。")
                directories.remove(directory)
        for name in names:
            path = parent_path / name
            relative = path.relative_to(root)
            rel = relative.as_posix()
            # A worktree may use a .git file instead of a directory.
            if relative.parts == (".git",):
                continue
            if path.is_symlink() or not allowed(relative):
                errors.append("发现非约定文件或符号链接；路径省略，请人工检查。")
                continue
            if any(value.casefold() in rel.casefold() for value in forbidden):
                errors.append("文件路径命中禁止词；路径与值省略。")
                continue
            seen.add(rel)
            try:
                content = path.read_text(encoding="utf-8")
            except (UnicodeError, OSError):
                errors.append(f"{rel}: 无法读取为 UTF-8 文本。")
                continue
            if "\x00" in content:
                errors.append(f"{rel}: 检测到非文本内容。")
                continue
            texts[path.resolve()] = content
            for number, line in enumerate(content.splitlines(), 1):
                for label, pattern in PATTERNS:
                    if pattern.search(line):
                        errors.append(f"{rel}:{number}: 命中{label}，值省略。")
                if any(value.casefold() in line.casefold() for value in forbidden):
                    errors.append(f"{rel}:{number}: 命中禁止词，值省略。")

    for missing in sorted(REQUIRED - seen):
        errors.append(f"{missing}: 缺少必要文件。")

    for path, content in texts.items():
        if path.suffix != ".md":
            continue
        rel = path.relative_to(root).as_posix()
        if not re.search(r"^#\s+\S", content, re.MULTILINE):
            errors.append(f"{rel}: 缺少一级标题。")
        if rel.startswith("domains/") and path.name == "README.md":
            for label in SECTION_LABELS:
                if f"## {label}" not in content:
                    errors.append(f"{rel}: 缺少必要章节 {label}。")
        for match in LINK.finditer(content):
            href = match.group(1).strip()
            if href.startswith("<") and href.endswith(">"):
                href = href[1:-1]
            try:
                parsed = urlsplit(href)
            except ValueError:
                errors.append(f"{rel}: 链接格式无效，值省略。")
                continue
            if parsed.scheme or parsed.netloc:
                if parsed.scheme not in {"https", "http"} or not parsed.hostname or parsed.username or parsed.password:
                    errors.append(f"{rel}: 外部链接协议或访问身份不符合公开引用规则，值省略。")
                # Remote availability and source validity require a separate, current review.
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(root) or target not in texts:
                errors.append(f"{rel}: 站内链接目标不存在、越界或不是已检查文本，值省略。")
            elif parsed.fragment and unquote(parsed.fragment) not in anchors(texts[target]):
                errors.append(f"{rel}: 站内链接锚点不存在，值省略。")
    return errors, len(texts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--forbid", action="append", default=[], help="Extra forbidden literal; values are never printed.")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print("FAIL: repository directory does not exist.", file=sys.stderr)
        return 1
    if any(not value.strip() for value in args.forbid):
        print("FAIL: forbidden values must be nonempty.", file=sys.stderr)
        return 1
    try:
        errors, count = inspect(root, args.forbid)
    except OSError:
        print("FAIL: filesystem scan could not complete; details omitted.", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        print(f"FAIL: {len(errors)} issue(s); no sensitive values printed.", file=sys.stderr)
        return 1
    print(f"PASS: {count} text files; structure, local links and common sensitive patterns checked.")
    print("Manual content and Git history/metadata review are still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
