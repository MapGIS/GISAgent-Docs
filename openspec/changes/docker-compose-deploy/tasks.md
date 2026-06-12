# 任务：`doc/` 文档站 Docker Compose 部署

## 1. 方案收敛

- [x] 盘点当前 `doc/` 文档站的本地运行方式
- [x] 盘点根目录 `docker-compose.yml` 的现有服务结构
- [x] 盘点 `docker-nginx-framework` 中可复用的代理经验
- [x] 明确本 change 的目标是"并入当前 Compose 主栈"

## 2. 文档站容器化设计

- [x] 确定 `doc/` 的正式容器运行方式（nginx + 静态文件）
- [x] 明确使用 Mintlify 导出的静态构建产物
- [x] 设计文档站容器的健康检查方式（wget + 30s interval）
- [x] 明确容器端口 17077、构建上下文和产物目录 export-site/

## 3. Compose 集成设计

- [x] 设计 `doc/docker-compose.yml` 独立部署文件
- [x] 明确该 service 所需网络 gisagent-network、无卷依赖
- [x] 创建 `doc/package.sh` 离线打包脚本

## 4. Nginx 集成设计

- [x] 将 `/doc` 正式并入仓库 `nginx/` 配置
- [x] 设计 `/doc` 到文档站容器的代理规则
- [x] 子路径改写由 Nginx sub_filter 处理
- [x] 说明与 `docker-nginx-framework` 的继承关系

## 5. 验证与部署

- [x] 本机 `docker compose` 验证（200 OK）
- [x] 公网入口验证（https://server.maptex.top/doc/）
- [x] 离线打包测试

## 6. OpenSpec 记录

- [x] 创建 `proposal.md`
- [x] 创建 `design.md`
- [x] 创建 `tasks.md`
- [x] 创建 `execution.md`
- [x] 创建 `validation.md`
- [x] 创建 `closeout.md`
- [x] 创建 `STATUS.md`

---

## 实施记录

### 2026-06-12 部署完成

| 项目 | 状态 | 详情 |
|------|------|------|
| docker-compose.yml | ✅ | `doc/docker-compose.yml` 端口 17077 |
| nginx 代理 | ✅ | `nginx/nginx/gisagent.conf` upstream docs_backend |
| 镜像构建 | ✅ | `gisagent-docs:latest` (nginx:1.27-alpine) |
| 服务验证 | ✅ | localhost:17077 → 200, localhost/doc/ → 200 |

### 2026-06-12 离线打包脚本

| 项目 | 详情 |
|------|------|
| 脚本路径 | `doc/package.sh` |
| 输出目录 | `doc/packages/` |
| 归档名称 | `gisagent-docs-bundle-<timestamp>.tar.gz` |
| 归档大小 | ~46M (含镜像) |
| 功能 | 导出镜像 + 静态文件 + 生成 deploy.sh |

**打包内容**:
- docker-compose.yml
- Dockerfile
- images/docker-images.tar (镜像归档)
- export-site/ (静态文件)
- deploy.sh (部署脚本)
- README.md (部署说明)

### 2026-06-12 阿里云 nginx 配置同步

| 项目 | 结果 |
|------|------|
| 目标服务器 | 47.96.105.134 |
| 目标路径 | `/opt/nginx/nginx-20260602_164043` |
| nginx 镜像上传 | ✅ |
| nginx 容器重启 | ✅ healthy |
| /doc 路由验证 | ✅ 200 OK |
| doc-site 容器 | ✅ healthy (port 17077) |

**同步步骤**:
```bash
# 1. 本机构建并导出镜像
cd /home/maptex/Code/xcsmartdatabase/nginx
docker build -t gisagent-nginx:latest .
docker save -o /tmp/gisagent-nginx.tar gisagent-nginx:latest

# 2. 上传并加载
scp /tmp/gisagent-nginx.tar root@47.96.105.134:/tmp/
ssh root@47.96.105.134 "docker load -i /tmp/gisagent-nginx.tar"
ssh root@47.96.105.134 "cd /opt/nginx/nginx-20260602_164043 && docker compose up -d --force-recreate"
```