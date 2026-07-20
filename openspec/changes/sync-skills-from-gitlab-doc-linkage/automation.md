# 自动化：同步技能变更与文档联动

## 目标

把当前“固定来源 -> `doc/update.md` -> `docs/skills-detailed-update-log.mdx`”的流程从手工整理升级为可执行脚本。

## 脚本入口

- `doc/scripts/generate_skill_update.py`

## 固定输入

1. `clis/`
   - 扫描 `/home/maptex/Code/xcsmartdatabase/clis/*` 下带 `.git` 的子仓库
   - 直接读取 Git log
2. `gisagent/`
   - 读取 `/home/maptex/Code/xcsmartdatabase/gisagent` 的 Git log
   - 不再以 `gisagent/CHANGELOG.md` 作为固定事实源
3. `skills/`
   - 读取 `/home/maptex/Code/xcsmartdatabase/skills` 的 Git log

## 固定输出

1. `/home/maptex/Code/xcsmartdatabase/doc/update.md`
2. `/home/maptex/Code/xcsmartdatabase/doc/docs/skills-detailed-update-log.mdx`

## 执行命令

```bash
python3 /home/maptex/Code/xcsmartdatabase/doc/scripts/generate_skill_update.py
```

如需指定时间范围：

```bash
python3 /home/maptex/Code/xcsmartdatabase/doc/scripts/generate_skill_update.py \
  --since 2026-06-10 \
  --until 2026-07-20
```

## 当前边界

- 自动化来源仍然是固定三类 Git 来源，不扫描整个工作机所有仓库
- 自动生成的是统一汇总稿和文档页，不为每个 `SKILL.md` 单独生成 changelog
- 脚本目前按提交直接整理，不做复杂语义聚类
