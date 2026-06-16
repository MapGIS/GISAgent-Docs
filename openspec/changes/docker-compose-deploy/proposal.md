# 提案：`doc/` 文档站的 Docker Compose 部署

## 背景

当前 `doc/` 下的 `GIS Agent` 文档站已经可本地运行，且 `server.maptex.top/doc/` 的本机访问链路已经打通。

但当前有效方式仍然是：

1. 宿主机手工启动 `mint dev`
2. Nginx 将 `/doc` 代理到宿主机 `3000` 端口

这意味着文档站还没有进入当前工程统一的容器化部署体系，也没有形成稳定的 `docker compose` 运维方式。

同时，仓库中已经存在两类相关基础：

1. 根目录 `docker-compose.yml`，用于当前 GIS / agent / gateway 主栈
2. `openspec/changes/docker-nginx-framework`，用于记录容器化 Nginx 代理的既有经验

因此下一步需要把 `doc/` 的部署方式正式收敛到 Docker Compose，并将 `/doc` 路由纳入仓库内的可交付部署方案。

## 问题陈述

当前缺少以下正式能力：

- 缺少文档站自己的容器化运行方式
- 缺少把文档站纳入现有 Compose 栈的设计记录
- 缺少 `/doc` 路由在 Docker Nginx 中的正式部署边界
- 缺少对“历史 `docker-nginx-framework` 方案”和“当前主 Compose 栈”之间关系的统一说明

## 目标

本 change 的目标是：

1. 为 `doc/` 文档站定义 Docker 化运行方案
2. 为当前工程定义可落地的 `docker compose` 部署拓扑
3. 将 `/doc` 入口从“宿主机开发预览代理”收敛为“Compose 内正式服务路由”
4. 复用 `docker-nginx-framework` 的 Nginx 经验，但不再维护割裂的独立部署认知
5. 明确部署后 `server.maptex.top` / `gisagent.smaryun.com` 的路由职责与验收范围

## 范围内

- `doc/` 文档站容器化部署方案
- 根目录 `docker-compose.yml` 的扩展方向
- `nginx/` 中 `/doc` 路由的正式配置方向
- `docker-nginx-framework` 与当前部署方案的关系梳理
- 部署、验证、回滚的 OpenSpec 记录

## 范围外

- 重新设计文档站内容结构
- 恢复或依赖已废弃的 `xcsmartdatabase-service`
- 将 `doc/` 并入 `opencode` 容器内部运行
- 直接在本 change 中完成阿里云全量上线验收

## 成功标准

1. `doc/openspec/changes/docker-compose-deploy` 下存在完整变更记录
2. 方案明确指出文档站将由 Docker 容器承载，而不是宿主机常驻 `mint dev`
3. 方案明确指出 `/doc` 将由 Compose 中的 Nginx 正式代理
4. 方案明确说明与 `docker-nginx-framework` 的继承关系和替代边界
5. 后续实施时可直接按本 change 落地配置与验收
