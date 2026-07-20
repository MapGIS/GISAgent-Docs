# 提案：同步技能变更与 Mintlify 文档联动

## 背景

`openspec/changes/sync-skills-from-gitlab` 已经补充了：

- `clis-daily-git-update-log.md`
- `clis-new-skill-capability-log.md`
- `clis-frontend-and-bugfix-log.md`

这些文件适合做工程事实记录，但不直接满足 `doc/` 文档站的发布要求。

当前 `doc/` 使用 Mintlify，正式发布链路实际包含两层产物：

1. `doc/update.md`
   - 统一汇总稿
   - 固定汇总 `clis/` 与 `gisagent/`
2. `doc/docs/skills-detailed-update-log.mdx`
   - Mintlify 对外阅读页
   - 通过 `docs.json` 导航暴露

## 问题陈述

当前存在两层内容，但没有联动：

1. `openspec/changes/sync-skills-from-gitlab` 中的工程记录
2. `doc/update.md` 统一汇总稿
3. `doc/` 文档站中可被 Mintlify 直接消费的页面

这会导致：

- 工程侧、汇总稿、文档页三者容易漂移
- 文档站若单独补写，又缺少与原始 change 的追踪关系

## 目标

本 change 的目标是：

1. 将这轮技能更新收敛为 1 个统一汇总稿 `doc/update.md`
2. 将统一汇总稿镜像为 1 个 Mintlify 可访问页面 `doc/docs/skills-detailed-update-log.mdx`
3. 在 `doc/docs.json` 中加入可访问入口
4. 在 `doc/openspec/changes` 下记录这次联动关系
5. 回链到原始 `openspec/changes/sync-skills-from-gitlab`

## 范围内

- `doc/update.md`
- `doc/docs/skills-detailed-update-log.mdx`
- `doc/docs.json`
- `doc/openspec/changes/sync-skills-from-gitlab-doc-linkage/*`
- `doc/openspec/README.md`
- 原始 `openspec/changes/sync-skills-from-gitlab/tasks.md` 中的回链说明

## 范围外

- 重写原始 `openspec` 执行日报
- 修改 Git 同步流程本身
- 调整 Mintlify 部署方式

## 成功标准

1. `doc/update.md` 存在且明确标注固定来源
2. 文档站存在 1 个新的技能迭代页面 `docs/skills-detailed-update-log.mdx`
3. 页面为 Mintlify `.mdx` 格式
4. `docs.json` 中存在可访问导航入口
5. `doc/openspec/changes` 中存在本次联动 change
6. 原始 openspec change 能回链到文档侧页面与联动 change
