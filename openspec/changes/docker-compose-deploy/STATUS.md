---
name: “docker-compose-deploy”
description: “将 `doc/` 文档站从宿主机 `mint dev` 代理收敛为 Docker Compose 正式部署”
metadata:
  type: project
status: completed
updated: 2026-06-12
---

# `doc/` 文档站 Docker Compose 部署状态

## 当前结论

本 change 已完成 OpenSpec 方案定义，并已完成容器化部署实现。

## 已完成

- 读取并继承 `gisagent-doc-site-and-doc-proxy` 的当前事实
- 读取并继承 `docker-nginx-framework` 的代理经验
- 明确当前目标是”根仓库 Compose 主栈 + 正式 `/doc` 路由”
- 创建完整的 OpenSpec 变更文件集
- 更新 `doc/openspec/README.md`
- **doc/ 文档站容器化实现** ✅
  - 独立 docker-compose.yml: `doc/docker-compose.yml`
  - 镜像: `gisagent-docs:latest`
  - 端口: `17077`
  - 容器名: `gisagent-doc-site`
- **nginx 代理配置更新** ✅
  - `nginx/nginx/gisagent.conf`: upstream 指向 `gisagent-doc-site:3000`
  - `nginx/docker-compose.yml`: 移除重复的 docs 服务定义
- **服务部署验证** ✅
  - `http://localhost:17077/` → 200 OK
  - `http://localhost/doc/` → 200 OK (nginx 代理)

## 部署架构

```
User → nginx (80) → /doc/ → gisagent-doc-site:3000 (17077)
```

## 验收结果

| 检查项 | 状态 |
|--------|------|
| docker compose up -d 后文档站容器可健康运行 | ✅ |
| `/doc/` 首页返回 200 | ✅ |
| `/doc/<page>` 页面返回 200 | ✅ |
| `/doc` 返回规范化跳转 | ✅ |
| 文档静态资源在 `/doc` 子路径下可正确加载 | ✅ |

## 证据入口

- `proposal.md`: 目标、范围和成功标准
- `design.md`: 容器化部署与 `/doc` 路由设计
- `tasks.md`: 后续实施任务
- `execution.md`: 本次方案整理过程
- `validation.md`: 当前仅完成的事实验证
- `closeout.md`: 暂不关闭原因

## 建议状态

- 文档内容: 已完成 ✅
- OpenSpec 部署方案: 已完成 ✅
- 容器化实现: 已完成 ✅
- 集成验收: 已完成 ✅
- 阿里云同步: 已完成 ✅

## 阿里云部署记录 (2026-06-12)

| 检查项 | 结果 |
|--------|------|
| nginx 镜像上传 | ✅ gisagent-nginx.tar → 47.96.105.134 |
| nginx 容器重启 | ✅ healthy |
| /doc 路由 (阿里云) | ✅ http://47.96.105.134/doc/ → 200 |
| doc-site 容器 | ✅ gisagent-doc-site (healthy, port 17077) |
