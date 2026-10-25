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
SKILLS_MANIFEST = (
    WORKSPACE_ROOT
    / "openspec"
    / "changes"
    / "sync-skills-from-gitlab"
    / "known-skills.manifest"
)

UPDATE_MD = DOC_ROOT / "update.md"
UPDATE_MDX = DOC_ROOT / "docs" / "skills-detailed-update-log.mdx"


@dataclass
class Commit:
    repo: str
    full_hash: str
    short_hash: str
    commit_date: str
    subject: str


def since_bound(since: str) -> str:
    """Pin a bare ``--since=<date>`` to that day's midnight.

    Git's approxidate fills the missing time-of-day from *now*, so
    ``--since=2026-06-10`` slides forward as the day goes on and silently drops
    commits made earlier on the boundary day.
    """
    if "T" in since or " " in since.strip():
        return since
    return f"{since}T00:00:00"


def until_bound(until: str) -> str:
    """Make ``--until=<date>`` inclusive of that whole day.

    ``git log --until=2026-10-23`` is parsed as ``2026-10-23 00:00:00`` and
    silently drops every commit made later that day.
    """
    if "T" in until or " " in until.strip():
        return until
    return f"{until}T23:59:59"


def git_log(repo_path: Path, since: str, until: str) -> list[Commit]:
    fmt = "%H%x1f%h%x1f%ad%x1f%s"
    cmd = [
        "git",
        "-C",
        str(repo_path),
        "log",
        f"--since={since_bound(since)}",
        f"--until={until_bound(until)}",
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


def load_skill_manifest() -> set[str]:
    """Active skill names of the GitLab ``xcsmartdatabase/skills`` subgroup."""
    if not SKILLS_MANIFEST.exists():
        return set()
    names = SKILLS_MANIFEST.read_text(encoding="utf-8").splitlines()
    return {name.strip() for name in names if name.strip()}


def discover_skill_repos() -> tuple[list[Path], list[str]]:
    """Split ``skills/`` into per-skill GitLab checkouts and local-only caches.

    Only directories listed in ``known-skills.manifest`` are fact sources for
    the subgroup. Everything else (no independent Git repo, or a Git repo
    outside the manifest such as ``ui-ux-pro-max-skill``) is a local cache and
    must not be counted as a skill release.
    """
    manifest = load_skill_manifest()
    repos: list[Path] = []
    local_only: list[str] = []
    for path in sorted(SKILLS_ROOT.iterdir()):
        if not path.is_dir():
            continue
        is_manifest_skill = not manifest or path.name in manifest
        if (path / ".git").exists() and is_manifest_skill:
            repos.append(path)
        else:
            local_only.append(path.name)
    return repos, local_only


def load_skills_commits(since: str, until: str) -> dict[str, list[Commit]]:
    repos, _ = discover_skill_repos()
    data: dict[str, list[Commit]] = {}
    for repo_path in repos:
        commits = git_log(repo_path, since, until)
        if commits:
            data[repo_path.name] = commits
    return data


def latest_commit_date(commits: list[Commit]) -> str:
    """Newest date across possibly several repositories (not the list tail)."""
    return max((commit.commit_date for commit in commits), default="无")


def first_commit_date(commits: list[Commit]) -> str:
    """Oldest date across possibly several repositories (not the list head)."""
    return min((commit.commit_date for commit in commits), default="无")


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


def manifest_total_line(updated: int) -> str:
    total = len(load_skill_manifest())
    if not total:
        return "- subgroup 清单不可用，未做总数校验"
    return f"- subgroup 清单共 `{total}` 个技能，其余 `{total - updated}` 个在区间内无提交"


def render_skills_section(
    skills_data: dict[str, list[Commit]],
    local_only: list[str],
    since: str,
    until: str,
) -> str:
    all_commits = [commit for commits in skills_data.values() for commit in commits]
    lines = [
        "## skills/",
        "",
        "### 本轮状态",
        "",
        f"- 来源：`{SKILLS_ROOT}` 下各技能独立仓库 Git log（GitLab `xcsmartdatabase/skills` subgroup 清单：`{SKILLS_MANIFEST.name}`）",
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
            f"- 本轮共有 `{len(skills_data)}` 个技能仓库发生更新，累计 `{len(all_commits)}` 条提交",
            manifest_total_line(len(skills_data)),
            f"- 最近更新日期：`{latest_commit_date(all_commits)}`",
            f"- 重点仓库：`{top_repo_names(skills_data)}`",
        ]
    )
    if local_only:
        listed = "、".join(f"`{name}`" for name in local_only)
        lines.append(f"- 不在 subgroup 清单内的本地缓存目录（不计入统计，不参与 `skillpacks/mapviz-skills/` 提升）：{listed}")
    lines.append("")
    for repo_name, commits in sorted(skills_data.items(), key=lambda item: latest_commit_date(item[1]), reverse=True):
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


def render_overview(
    clis_data: dict[str, list[Commit]],
    gisagent_commits: list[Commit],
    skills_data: dict[str, list[Commit]],
) -> list[str]:
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
    skills_commits = [commit for commits in skills_data.values() for commit in commits]
    if skills_commits:
        lines.append(
            f"- **`skills/` 逐技能仓库持续演进**：`{len(skills_data)}` 个技能仓库新增 `{len(skills_commits)}` 条提交，最近更新到 `{latest_commit_date(skills_commits)}`。"
        )
    else:
        lines.append("- **`skills/` 本轮无新增**：统计区间内没有新提交。")
    return lines


def render_update_md(
    since: str,
    until: str,
    clis_data: dict[str, list[Commit]],
    gisagent_commits: list[Commit],
    skills_data: dict[str, list[Commit]],
    local_only: list[str],
) -> str:
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
        f"  - `{SKILLS_ROOT}` 下各技能独立仓库 Git log（以 `{SKILLS_MANIFEST.name}` 为 subgroup 清单）",
        "- 说明：",
        "  - 本文件由 `doc/scripts/generate_skill_update.py` 自动生成。",
        "  - 汇总范围固定为 `clis/`、`gisagent/` 与 `skills/`。",
        "  - 这不是逐个 `SKILL.md` 自动生成的全量 changelog，而是对固定来源 Git 提交的统一汇总。",
        "  - `skills/` 的 subgroup 口径与同步结论以 `config/openspecs/changes/docker-sync-skills/README.md` 索引的 `openspec/changes/sync-skills-from-gitlab/` 记录为准。",
        "",
    ]
    sections.extend(render_overview(clis_data, gisagent_commits, skills_data))
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
            render_skills_section(skills_data, local_only, since, until),
        ]
    )
    return "\n".join(sections).rstrip() + "\n"


def render_update_mdx(
    since: str,
    until: str,
    clis_data: dict[str, list[Commit]],
    gisagent_commits: list[Commit],
    skills_data: dict[str, list[Commit]],
    local_only: list[str],
) -> str:
    body = render_update_md(since, until, clis_data, gisagent_commits, skills_data, local_only)
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
        "> 最近一周新增／改名／内容更新的技能见 [本周新增技能](/docs/skills-new-this-week)。",
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
    skills_data = load_skills_commits(args.since, args.until)
    _, local_only = discover_skill_repos()

    UPDATE_MD.write_text(
        render_update_md(args.since, args.until, clis_data, gisagent_commits, skills_data, local_only),
        encoding="utf-8",
    )
    UPDATE_MDX.write_text(
        render_update_mdx(args.since, args.until, clis_data, gisagent_commits, skills_data, local_only),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
