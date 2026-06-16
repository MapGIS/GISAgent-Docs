# Closeout 状态：`doc/` 文档站 Docker Compose 部署

## 当前状态

本 change 已完成，可以标记为最终 closeout。

## 完成项

1. 文档站容器化实现 ✅
   - 独立 docker-compose.yml: `doc/docker-compose.yml`
   - 镜像: `gisagent-docs:latest`
   - 容器名: `gisagent-doc-site`
   - 端口: 17077

2. nginx 代理配置更新 ✅
   - `nginx/nginx/gisagent.conf`: upstream 指向 `gisagent-doc-site:3000`
   - `nginx/docker-compose.yml`: 移除重复的 docs 服务定义

3. 本机验收 ✅
   - `http://localhost:17077/` → 200 OK
   - `http://localhost/doc/` → 200 OK

4. 公网验收 ✅
   - `https://server.maptex.top/doc/` → 已代理

## 部署架构

```
独立部署文件: doc/docker-compose.yml
┌─────────────┐     ┌─────────────────────┐
│   nginx     │────▶│  gisagent-doc-site  │
│   (port 80) │     │     (port 17077)    │
└─────────────┘     └─────────────────────┘
     /doc/          upstream: docs_backend
```

## 结论

所有 OpenSpec 定义的目标均已实现并通过验证。

## 阿里云同步

### 2026-06-12 阿里云 nginx 配置同步

**目标服务器**: 47.96.105.134
**目标路径**: `/opt/nginx/nginx-20260602_164043`

| 检查项 | 结果 |
|--------|------|
| nginx 镜像上传 | ✅ gisagent-nginx.tar (48M) |
| nginx 容器重启 | ✅ healthy |
| /doc 路由 | ✅ http://47.96.105.134/doc/ → 200 OK |
| doc-site 容器 | ✅ gisagent-doc-site (healthy, port 17077) |

### 阿里云部署架构

```
阿里云: 47.96.105.134
┌─────────────────┐     ┌─────────────────────┐
│  gisagent-nginx │────▶│  gisagent-doc-site  │
│    (port 80)    │     │    (port 17077)     │
└─────────────────┘     └─────────────────────┘
      /doc/              upstream: docs_backend
```

---

**Closeout 时间**: 2026-06-12
**验证状态**: 已完成（本机 + 阿里云）