# `doc/` OpenSpec 记录

本文档目录用于记录 `doc/` 目录下本次文档站建设与 `/doc` 代理接入工作的阶段性事实。

## 当前 change

- `gisagent-doc-site-and-doc-proxy`
- `docker-compose-deploy`

## 入口文件

- `gisagent-doc-site-and-doc-proxy/proposal.md`
- `gisagent-doc-site-and-doc-proxy/design.md`
- `gisagent-doc-site-and-doc-proxy/tasks.md`
- `gisagent-doc-site-and-doc-proxy/execution.md`
- `gisagent-doc-site-and-doc-proxy/validation.md`
- `gisagent-doc-site-and-doc-proxy/closeout.md`
- `gisagent-doc-site-and-doc-proxy/STATUS.md`
- `docker-compose-deploy/proposal.md`
- `docker-compose-deploy/design.md`
- `docker-compose-deploy/tasks.md`
- `docker-compose-deploy/execution.md`
- `docker-compose-deploy/validation.md`
- `docker-compose-deploy/closeout.md`
- `docker-compose-deploy/STATUS.md`

## 本次记录覆盖内容

- 基于最新 Mintlify `docs.json` 结构创建 `GisAgent` 文档站
- 将站点中文化，并把导航调整为多 Tab
- 统一标题、logo、favicon 与蓝色主色调
- 将 `AGENTS.md` 中的架构说明迁移到多页文档
- 记录仓库内 Nginx 预期配置变更
- 记录当前工作机本机 `/doc` 代理接入与验证结果
- 记录将文档站从本机 `mint dev` 代理切换到 `docker compose` 部署的目标方案

## 当前边界

- 这些记录已覆盖本次实际完成工作
- 公网 `http://gisagent.smaryun.com/doc` 的最终入口仍未完成真实链路验收
- 因此当前 change 只能视为“文档站完成 + 本机代理完成 + 公网入口待确认”
- 新增的 `docker-compose-deploy` 仍处于方案阶段，用于承接下一步容器化部署
