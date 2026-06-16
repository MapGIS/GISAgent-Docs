#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_FILE="${ROOT_DIR}/docker-compose.yml"
OUTPUT_DIR="${ROOT_DIR}/packages"
PROJECT_NAME="gisagent-docs"
PACKAGE_NAME="gisagent-docs-bundle-$(date +%Y%m%d_%H%M%S)"
STAGE_DIR=""
ARCHIVE_PATH=""
INCLUDE_IMAGES=1
DRY_RUN=0

readonly EXTERNAL_NETWORKS=(
  "gisagent-network"
)

usage() {
  cat <<'EOF'
Usage: ./package.sh [options]

gisagent-docs 文档站离线打包脚本

Options:
  --output-dir <dir>   Output directory for generated bundle (default: ./packages)
  --name <name>        Bundle base name (default: gisagent-docs-bundle-<timestamp>)
  --no-images          Do not export Docker images
  --dry-run            Generate bundle structure and scripts, skip image export and final tar.gz
  -h, --help           Show this help

Default behavior:
  1. Export gisagent-docs:latest image
  2. Copy docker-compose.yml into a portable bundle
  3. Generate deploy.sh for target host restore
  4. Pack everything into one .tar.gz archive
EOF
}

log() {
  printf '[INFO] %s\n' "$*"
}

warn() {
  printf '[WARN] %s\n' "$*" >&2
}

fail() {
  printf '[ERROR] %s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || fail "Missing required command: $1"
}

parse_args() {
  while (($#)); do
    case "$1" in
      --output-dir)
        [[ $# -ge 2 ]] || fail "--output-dir requires a value"
        OUTPUT_DIR="$2"
        shift 2
        ;;
      --name)
        [[ $# -ge 2 ]] || fail "--name requires a value"
        PACKAGE_NAME="$2"
        shift 2
        ;;
      --no-images)
        INCLUDE_IMAGES=0
        shift
        ;;
      --dry-run)
        DRY_RUN=1
        shift
        ;;
      -h|--help)
        usage
        exit 0
        ;;
      *)
        fail "Unknown option: $1"
        ;;
    esac
  done
}

check_inputs() {
  require_command docker
  require_command tar

  [[ -f "$COMPOSE_FILE" ]] || fail "Compose file not found: $COMPOSE_FILE"
  [[ -f "${ROOT_DIR}/Dockerfile" ]] || fail "Dockerfile not found: ${ROOT_DIR}/Dockerfile"

  # 检查镜像是否存在
  docker image inspect "gisagent-docs:latest" >/dev/null 2>&1 || {
    warn "Image gisagent-docs:latest not found locally, building..."
    docker build -f "${ROOT_DIR}/Dockerfile" -t "gisagent-docs:latest" "${ROOT_DIR}"
  }
}

prepare_stage() {
  mkdir -p "$OUTPUT_DIR"
  STAGE_DIR="${OUTPUT_DIR}/${PACKAGE_NAME}"
  ARCHIVE_PATH="${OUTPUT_DIR}/${PACKAGE_NAME}.tar.gz"

  rm -rf "$STAGE_DIR"
  mkdir -p "$STAGE_DIR"/{images,scripts}
}

copy_bundle_files() {
  log "Copying deployment files"

  cp -a "${ROOT_DIR}/docker-compose.yml" "$STAGE_DIR/docker-compose.yml"
  cp -a "${ROOT_DIR}/Dockerfile" "$STAGE_DIR/Dockerfile"
  cp -a "${ROOT_DIR}/.dockerignore" "$STAGE_DIR/.dockerignore" 2>/dev/null || true

  # 复制 nginx 配置和静态文件
  mkdir -p "$STAGE_DIR/scripts"
  cp -a "${ROOT_DIR}/scripts/nginx-doc.conf" "$STAGE_DIR/scripts/" 2>/dev/null || true

  # 复制 export-site 静态文件
  if [[ -d "${ROOT_DIR}/export-site" ]]; then
    log "Copying export-site static files"
    mkdir -p "$STAGE_DIR/export-site"
    cp -a "${ROOT_DIR}/export-site"/* "$STAGE_DIR/export-site/"
  else
    fail "export-site directory not found. Please run 'npx mint@latest export' first."
  fi

  # 复制 Mintlify 配置（可选，用于重新构建）
  cp -a "${ROOT_DIR}/docs.json" "$STAGE_DIR/" 2>/dev/null || true
  cp -a "${ROOT_DIR}/favicon.svg" "$STAGE_DIR/" 2>/dev/null || true
  if [[ -d "${ROOT_DIR}/logo" ]]; then
    cp -a "${ROOT_DIR}/logo" "$STAGE_DIR/"
  fi
}

export_images() {
  (( INCLUDE_IMAGES == 1 )) || return 0

  log "Exporting gisagent-docs:latest image"
  docker save -o "${STAGE_DIR}/images/docker-images.tar" "gisagent-docs:latest"
}

generate_manifest() {
  log "Writing manifest"
  {
    printf 'PROJECT_NAME=%s\n' "$PROJECT_NAME"
    printf 'GENERATED_AT=%s\n' "$(date -Iseconds)"
    printf 'INCLUDE_IMAGES=%s\n' "$INCLUDE_IMAGES"
    printf 'IMAGE=gisagent-docs:latest\n'
    printf 'CONTAINER_NAME=gisagent-doc-site\n'
    printf 'PORT=17077\n'
    printf '\n[external_networks]\n'
    for network in "${EXTERNAL_NETWORKS[@]}"; do
      printf '%s\n' "$network"
    done
  } > "${STAGE_DIR}/manifest.txt"
}

generate_deploy_script() {
  log "Generating deploy.sh"

  cat > "${STAGE_DIR}/deploy.sh" <<'EOF'
#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_FILE="${ROOT_DIR}/docker-compose.yml"
PROJECT_NAME="gisagent-docs"
IMAGES_ARCHIVE="${ROOT_DIR}/images/docker-images.tar"

SKIP_IMAGES=0
SKIP_UP=0

readonly EXTERNAL_NETWORKS=(
  "gisagent-network"
)

usage() {
  cat <<'USAGE'
Usage: ./deploy.sh [options]

gisagent-docs 文档站部署脚本

Options:
  --skip-images   Skip docker load
  --skip-up       Skip docker compose up -d
  -h, --help      Show help

部署说明:
  1. 确保 gisagent-network 网络已创建（主服务栈应先部署）
  2. 文档站端口: 17077
  3. nginx 代理: /doc/ → gisagent-doc-site:3000
USAGE
}

parse_args() {
  while (($#)); do
    case "$1" in
      --skip-images)
        SKIP_IMAGES=1
        shift
        ;;
      --skip-up)
        SKIP_UP=1
        shift
        ;;
      -h|--help)
        usage
        exit 0
        ;;
      *)
        echo "[ERROR] Unknown option: $1" >&2
        exit 1
        ;;
    esac
  done
}

log() {
  printf '[INFO] %s\n' "$*"
}

fail() {
  printf '[ERROR] %s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || fail "Missing required command: $1"
}

ensure_external_networks() {
  for network in "${EXTERNAL_NETWORKS[@]}"; do
    if ! docker network inspect "$network" >/dev/null 2>&1; then
      log "Creating external network ${network}"
      docker network create "$network" >/dev/null
    else
      log "External network ${network} already exists"
    fi
  done
}

load_images() {
  if (( SKIP_IMAGES == 0 )); then
    if [[ -f "$IMAGES_ARCHIVE" ]]; then
      log "Loading Docker images"
      docker load -i "$IMAGES_ARCHIVE"
    else
      log "Image archive not found, building from source"
      docker build -f "${ROOT_DIR}/Dockerfile" -t "gisagent-docs:latest" "${ROOT_DIR}"
    fi
  fi
}

start_stack() {
  if (( SKIP_UP == 0 )); then
    log "Starting gisagent-doc-site container"
    docker compose -f "$COMPOSE_FILE" up -d
    log "Container status"
    docker compose -f "$COMPOSE_FILE" ps
  fi
}

verify_deployment() {
  log "Verifying deployment"
  local container_name="gisagent-doc-site"

  if docker ps --filter name="$container_name" --filter status=running -q | grep -q .; then
    log "✅ Container $container_name is running"
  else
    fail "❌ Container $container_name is not running"
  fi

  # 健康检查
  sleep 5
  if curl -s -o /dev/null -w "%{http_code}" http://localhost:17077/ | grep -q "200"; then
    log "✅ Health check passed: http://localhost:17077/ → 200 OK"
  else
    warn "⚠️  Health check failed, please verify manually: curl http://localhost:17077/"
  fi
}

main() {
  parse_args "$@"

  require_command docker
  require_command curl
  [[ -f "$COMPOSE_FILE" ]] || fail "Compose file not found: $COMPOSE_FILE"

  cd "$ROOT_DIR"

  ensure_external_networks
  load_images
  start_stack
  verify_deployment

  echo
  log "=========================================="
  log "gisagent-docs 部署完成"
  log "=========================================="
  echo
  log "访问地址:"
  log "  - 直接访问: http://localhost:17077/"
  log "  - nginx 代理: http://localhost/doc/ (需配置 nginx)"
  echo
  log "nginx 配置 (添加到 gisagent.conf):"
  log "  upstream docs_backend {"
  log "      server gisagent-doc-site:3000;"
  log "      keepalive 16;"
  log "  }"
  echo
  log "  location ^~ /doc/ {"
  log "      proxy_pass http://docs_backend/;"
  log "      # ... 其他代理配置"
  log "  }"
}

main "$@"
EOF

  chmod +x "${STAGE_DIR}/deploy.sh"
}

generate_readme() {
  log "Writing README.md"

  cat > "${STAGE_DIR}/README.md" <<'EOF'
# gisagent-docs 文档站离线部署包

## 概述

本部署包包含 GIS Agent 文档站的离线部署所需文件。

## 内容

```
.
├── docker-compose.yml    # Docker Compose 配置
├── Dockerfile            # 镜像构建文件
├── deploy.sh             # 部署脚本
├── images/
│   └── docker-images.tar # Docker 镜像归档
├── export-site/          # 静态网站文件
├── scripts/
│   └── nginx-doc.conf    # Nginx 配置模板
├── docs.json             # Mintlify 配置
├── favicon.svg           # 网站图标
├── logo/                 # Logo 文件
└── manifest.txt          # 部署清单
```

## 部署步骤

### 1. 前置条件

确保主服务栈已部署并创建了 `gisagent-network` 网络：

```bash
# 检查网络是否存在
docker network inspect gisagent-network
```

### 2. 部署

```bash
# 解压部署包
tar -xzf gisagent-docs-bundle-*.tar.gz
cd gisagent-docs-bundle-*

# 执行部署
./deploy.sh
```

### 3. 验证

```bash
# 检查容器状态
docker ps --filter name=gisagent-doc-site

# 测试访问
curl http://localhost:17077/
```

### 4. nginx 代理配置

如需通过 nginx 代理 `/doc` 路径，添加以下配置：

```nginx
upstream docs_backend {
    server gisagent-doc-site:3000;
    keepalive 16;
}

location = /doc {
    return 301 /doc/;
}

location ^~ /doc/ {
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_http_version 1.1;
    proxy_buffering off;
    proxy_pass http://docs_backend/;
}
```

## 端口

| 服务 | 容器端口 | 外部端口 |
|------|----------|----------|
| gisagent-doc-site | 3000 | 17077 |

## 相关链接

- 主服务栈部署: xcsmartdatabase/package.sh
- nginx 代理配置: nginx/nginx/gisagent.conf

---

**生成时间**: $(date -Iseconds)
EOF
}

pack_bundle() {
  (( DRY_RUN == 0 )) || return 0

  log "Creating archive ${ARCHIVE_PATH}"
  tar -czpf "$ARCHIVE_PATH" -C "$OUTPUT_DIR" "$PACKAGE_NAME"
}

print_summary() {
  echo
  log "Bundle prepared at: ${STAGE_DIR}"
  if (( DRY_RUN == 0 )); then
    log "Archive created: ${ARCHIVE_PATH}"
    echo
    echo "Usage on target host:"
    echo "  tar -xzf $(basename "$ARCHIVE_PATH")"
    echo "  cd ${PACKAGE_NAME}"
    echo "  ./deploy.sh"
    echo
    echo "Access URLs:"
    echo "  - Direct:    http://localhost:17077/"
    echo "  - Via nginx: http://localhost/doc/"
  else
    echo
    echo "Dry run complete. Bundle directory:"
    echo "  ${STAGE_DIR}"
  fi
}

main() {
  parse_args "$@"
  check_inputs
  prepare_stage
  copy_bundle_files
  generate_manifest
  generate_deploy_script
  generate_readme

  if (( DRY_RUN == 0 )); then
    export_images
    pack_bundle
  fi

  print_summary
}

main "$@"
