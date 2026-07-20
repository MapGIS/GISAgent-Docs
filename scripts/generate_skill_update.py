#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path


WORKSPACE_ROOT = Path("/home/maptex/Code/xcsmartdatabase")
DOC_ROOT = WORKSPACE_ROOT / "doc"
CLIS_ROOT = WORKSPACE_ROOT / "clis"
GISAGENT_ROOT = WORKSPACE_ROOT / "gisagent"
SKILLS_ROOT = WORKSPACE_ROOT / "skills"

UPDATE_MD = DOC_ROOT / "update.md"
UPDATE_MDX = DOC_ROOT / "docs" / "skills-detailed-update-log.mdx"


@dataclass
class Commit:
    repo: str
    full_hash: str
    short_hash: str
    commit_date: str
    subject: str


def git_log(repo_path: Path, since: str, until: str) -> list[Commit]:
    fmt = "%H%x1f%h%x1f%ad%x1f%s"
    cmd = [
        "git",
        "-C",
        str(repo_path),
        "log",
        f"--since={since}",
        f"--until={until}",
        "--date=short",
        f"--pretty=format:{fmt}",
        "--reverse",
    ]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    commits: list[Commit] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        full_hash, short_hash, commit_date, subject = line.split("\x1f", 3)
        commits.append(
            Commit(
                repo=repo_path.name,
                full_hash=full_hash,
                short_hash=short_hash,
                commit_date=commit_date,
                subject=subject.strip(),
            )
        )
    return commits


def discover_clis_repos() -> list[Path]:
    repos = []
    for path in sorted(CLIS_ROOT.iterdir()):
        if path.is_dir() and (path / ".git").exists():
            repos.append(path)
    return repos


def load_clis_commits(since: str, until: str) -> dict[str, list[Commit]]:
    data: dict[str, list[Commit]] = {}
    for repo_path in discover_clis_repos():
        commits = git_log(repo_path, since, until)
        if commits:
            data[repo_path.name] = commits
    return data


def latest_commit_date(commits: list[Commit]) -> str:
    return commits[-1].commit_date if commits else "无"


def first_commit_date(commits: list[Commit]) -> str:
    return commits[0].commit_date if commits else "无"


def top_repo_names(data: dict[str, list[Commit]], limit: int = 3) -> str:
    if not data:
        return "无"
    ordered = sorted(data.items(), key=lambda item: (-len(item[1]), item[0]))
    return "、".join(name for name, _ in ordered[:limit])


def render_commit_bullets(commits: list[Commit]) -> list[str]:
    return [f"- `{c.commit_date}` `{c.short_hash}` {c.subject}" for c in commits]


def render_clis_section(data: dict[str, list[Commit]], since: str, until: str) -> str:
    all_commits = [commit for commits in data.values() for commit in commits]
    lines = [
        "## clis/",
        "",
        "### 本轮状态",
        "",
        f"- 来源：`{CLIS_ROOT}` 下各子仓库 Git log",
        f"- 统计区间：{since} 至 {until}",
    ]
    if not all_commits:
        lines.extend(
            [
                "- 截至当前，本轮无新增条目",
                "",
                "本轮无新增条目。",
            ]
        )
        return "\n".join(lines)

    lines.extend(
        [
            f"- 本轮共有 `{len(data)}` 个子仓库发生更新，累计 `{len(all_commits)}` 条提交",
            f"- 最近更新日期：`{latest_commit_date(all_commits)}`",
            f"- 重点仓库：`{top_repo_names(data)}`",
            "",
        ]
    )
    for repo_name, commits in sorted(data.items(), key=lambda item: latest_commit_date(item[1]), reverse=True):
        lines.append(f"### `{repo_name}`")
        lines.append("")
        lines.append(
            f"- 提交数：`{len(commits)}`，区间：`{first_commit_date(commits)}` 至 `{latest_commit_date(commits)}`"
        )
        lines.extend(render_commit_bullets(commits))
        lines.append("")
    return "\n".join(lines).rstrip()


def render_single_repo_section(title: str, repo_path: Path, commits: list[Commit], since: str, until: str) -> str:
    lines = [
        f"## {title}",
        "",
        "### 本轮状态",
        "",
        f"- 来源：`{repo_path}` Git log",
        f"- 统计区间：{since} 至 {until}",
    ]
    if not commits:
        lines.extend(
            [
                "- 截至当前，本轮无新增条目",
                "",
                "本轮无新增条目。",
            ]
        )
        return "\n".join(lines)

    lines.extend(
        [
            f"- 本轮累计 `{len(commits)}` 条提交",
            f"- 最近更新日期：`{latest_commit_date(commits)}`",
            "",
            "### 提交列表",
            "",
        ]
    )
    lines.extend(render_commit_bullets(commits))
    return "\n".join(lines)


def render_overview(clis_data: dict[str, list[Commit]], gisagent_commits: list[Commit], skills_commits: list[Commit]) -> list[str]:
    clis_count = sum(len(commits) for commits in clis_data.values())
    lines = ["## 更新概览", ""]
    if clis_count:
        lines.append(
            f"- **`clis/` 持续演进**：`{len(clis_data)}` 个子仓库新增 `{clis_count}` 条提交，重点集中在 `{top_repo_names(clis_data)}`。"
        )
    else:
        lines.append("- **`clis/` 本轮无新增**：固定子仓库在统计区间内没有新提交。")
    if gisagent_commits:
        lines.append(
            f"- **`gisagent/` 继续迭代**：累计 `{len(gisagent_commits)}` 条提交，最近更新到 `{latest_commit_date(gisagent_commits)}`。"
        )
    else:
        lines.append("- **`gisagent/` 本轮无新增**：统计区间内没有新提交。")
    if skills_commits:
        lines.append(
            f"- **`skills/` 工作区继续收敛**：累计 `{len(skills_commits)}` 条提交，最近更新到 `{latest_commit_date(skills_commits)}`。"
        )
    else:
        lines.append("- **`skills/` 本轮无新增**：统计区间内没有新提交。")
    return lines


def render_update_md(since: str, until: str, clis_data: dict[str, list[Commit]], gisagent_commits: list[Commit], skills_commits: list[Commit]) -> str:
    sections = [
        "# 统一更新日志",
        "",
        "## 汇总说明",
        "",
        f"- 汇总日期：{date.today().isoformat()}",
        f"- 状态截止：{until}",
        "- 来源文件：",
        f"  - `{CLIS_ROOT}` 下各子仓库 Git log",
        f"  - `{GISAGENT_ROOT}` Git log",
        f"  - `{SKILLS_ROOT}` Git log",
        "- 说明：",
        "  - 本文件由 `doc/scripts/generate_skill_update.py` 自动生成。",
        "  - 汇总范围固定为 `clis/`、`gisagent/` 与 `skills/`。",
        "  - 这不是逐个 `SKILL.md` 自动生成的全量 changelog，而是对固定来源 Git 提交的统一汇总。",
        "",
    ]
    sections.extend(render_overview(clis_data, gisagent_commits, skills_commits))
    sections.extend(
        [
            "",
            "---",
            "",
            render_clis_section(clis_data, since, until),
            "",
            "",
            render_single_repo_section("gisagent/", GISAGENT_ROOT, gisagent_commits, since, until),
            "",
            "",
            render_single_repo_section("skills/", SKILLS_ROOT, skills_commits, since, until),
        ]
    )
    return "\n".join(sections).rstrip() + "\n"


def render_update_mdx(since: str, until: str, clis_data: dict[str, list[Commit]], gisagent_commits: list[Commit], skills_commits: list[Commit]) -> str:
    body = render_update_md(since, until, clis_data, gisagent_commits, skills_commits)
    body_lines = body.splitlines()
    # Drop the leading H1 in MDX body to avoid duplicate heading under frontmatter title.
    if body_lines and body_lines[0].startswith("# "):
        body_lines = body_lines[2:]
    frontmatter = [
        "---",
        "title: 技能详细更新日志",
        f'description: 基于固定 Git 来源自动汇总 {since} 至 {until} 的技能迭代与工程更新。',
        "---",
        "",
        "> 本页由 `doc/scripts/generate_skill_update.py` 自动生成。",
        "",
    ]
    return "\n".join(frontmatter + body_lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate doc/update.md and docs/skills-detailed-update-log.mdx from fixed git sources.")
    parser.add_argument("--since", default="2026-06-10", help="inclusive git log lower bound")
    parser.add_argument("--until", default=date.today().isoformat(), help="inclusive git log upper bound")
    args = parser.parse_args()

    clis_data = load_clis_commits(args.since, args.until)
    gisagent_commits = git_log(GISAGENT_ROOT, args.since, args.until)
    skills_commits = git_log(SKILLS_ROOT, args.since, args.until)

    UPDATE_MD.write_text(
        render_update_md(args.since, args.until, clis_data, gisagent_commits, skills_commits),
        encoding="utf-8",
    )
    UPDATE_MDX.write_text(
        render_update_mdx(args.since, args.until, clis_data, gisagent_commits, skills_commits),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
