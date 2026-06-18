---
name: "mintlify-hosted-docs-subpath"
description: "GIS Agent 文档站接入 Mintlify 托管，并通过 `gisagent.smaryun.com/docs` 提供正式入口"
metadata:
  type: project
status: proposed
updated: 2026-06-17
---

# Mintlify 托管 `/docs` 子路径接入状态

## 当前结论

该 change 用于记录 `GIS Agent` 文档站从“本机 Mintlify 预览 / 本机静态导出”转向“Mintlify 托管 + 自定义域名 `/docs` 反向代理”的正式接入方案。

## 当前状态

- 方案已确认可行
- 当前文档仓库已接入 Mintlify 托管
- `https://mapgis.mintlify.app/` 已可访问当前仓库内容
- 本地与阿里云 `/docs -> mapgis.mintlify.dev/docs` 反代模板已同步
- `http://gisagent.smaryun.com/docs` 已完成公网反代验收
- `https://gisagent.smaryun.com/` 与 `https://gisagent.smaryun.com/docs` 当前可访问
- 已确认 `gisagent-nginx` 在后端容器重启后会缓存旧 IP，需执行 `nginx -s reload` 刷新上游解析
- 尚未完成搜索与 Assistant 的正式功能验收

## 目标结果

- GitHub 仓库接入 Mintlify 托管
- 通过 Mintlify 平台启用搜索与 Assistant
- `https://gisagent.smaryun.com/docs` 成为正式文档入口
