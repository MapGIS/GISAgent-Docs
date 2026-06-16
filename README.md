# GIS Agent 文档站

## 部署说明

### 目录结构

```
doc/
├── docker-compose.yml   # 独立部署配置
├── Dockerfile           # 镜像构建文件 (nginx:1.27-alpine)
├── package.sh           # 离线打包脚本
├── docs.json            # Mintlify 配置
├── export-site/         # 静态网站文件
├── scripts/
│   ├── build-docker.sh  # 构建脚本
│   └── nginx-doc.conf   # nginx 配置模板
└── openspec/            # OpenSpec 变更记录
```

### 快速部署

```bash
# 1. 构建 Mintlify 导出（如果需要更新内容）
npx mint@latest export --output export.zip
python3 -m zipfile -e export.zip export-site

# 2. 构建镜像
docker build -f Dockerfile -t gisagent-docs:latest .

# 3. 启动服务
docker compose up -d

# 4. 验证
curl http://localhost:17077/
```

### 离线打包

```bash
# 生成离线部署包
./package.sh

# 输出到 packages/gisagent-docs-bundle-*.tar.gz (~46M)
```

### 部署包内容

| 文件 | 说明 |
|------|------|
| docker-compose.yml | Docker Compose 配置 |
| Dockerfile | 镜像构建文件 |
| images/docker-images.tar | Docker 镜像归档 |
| export-site/ | 静态网站文件 |
| deploy.sh | 目标机部署脚本 |
| README.md | 部署说明 |

### 目标机部署

```bash
# 1. 解压
tar -xzf gisagent-docs-bundle-*.tar.gz
cd gisagent-docs-bundle-*

# 2. 执行部署脚本
./deploy.sh

# 3. 验证
curl http://localhost:17077/
```

### nginx 代理配置

文档站通过 nginx 反向代理对外提供 `/doc` 路径：

```nginx
upstream docs_backend {
    server gisagent-doc-site:3000;
    keepalive 16;
}

location = /doc {
    return 301 /doc/;
}

location ^~ /doc/ {
    proxy_pass http://docs_backend/;
    # ... 其他代理配置
}
```

### 访问地址

| 环境 | 地址 |
|------|------|
| 本机直接访问 | http://localhost:17077/ |
| 本机 nginx 代理 | http://localhost/doc/ |
| 阿里云直接访问 | http://47.96.105.134:17077/ |
| 阿里云 nginx 代理 | http://47.96.105.134/doc/ |

### 阿里云同步

nginx 配置更新后需同步到阿里云：

```bash
# 1. 本机构建 nginx 镜像
cd /home/maptex/Code/xcsmartdatabase/nginx
docker build -t gisagent-nginx:latest .
docker save -o /tmp/gisagent-nginx.tar gisagent-nginx:latest

# 2. 上传到阿里云
scp /tmp/gisagent-nginx.tar root@47.96.105.134:/tmp/

# 3. 阿里云加载并重启
ssh root@47.96.105.134
docker load -i /tmp/gisagent-nginx.tar
cd /opt/nginx/nginx-20260602_164043
docker compose up -d --force-recreate
```

### 相关链接

- OpenSpec 变更记录: `openspec/changes/docker-compose-deploy/`
- nginx 配置: `/home/maptex/Code/xcsmartdatabase/nginx/nginx/gisagent.conf`

---

**更新时间**: 2026-06-12
**部署状态**: 已完成 (本机 + 阿里云)
