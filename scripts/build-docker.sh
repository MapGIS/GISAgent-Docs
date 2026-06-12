#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOC_DIR="$(dirname "$SCRIPT_DIR")"

IMAGE_NAME="${IMAGE_NAME:-gisagent-docs}"
IMAGE_TAG="${IMAGE_TAG:-latest}"
FULL_IMAGE="${IMAGE_NAME}:${IMAGE_TAG}"

echo "[INFO] validating Mintlify docs"
(
  cd "${DOC_DIR}"
  npx -y mint@latest validate
)

echo "[INFO] exporting static site"
rm -rf "${DOC_DIR}/export-site" "${DOC_DIR}/export.zip"
(
  cd "${DOC_DIR}"
  npx -y mint@latest export --output export.zip
)
python3 -m zipfile -e "${DOC_DIR}/export.zip" "${DOC_DIR}/export-site"

echo "[INFO] building ${FULL_IMAGE}"
docker build -f "${DOC_DIR}/Dockerfile" -t "${FULL_IMAGE}" "${DOC_DIR}"

echo "[INFO] built ${FULL_IMAGE}"
echo "[INFO] test run:"
echo "docker run --rm -p 3000:3000 ${FULL_IMAGE}"
