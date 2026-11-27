#!/usr/bin/env bash
set -euo pipefail

docker compose up --build --detach
echo "DevOpsFlow is starting at http://localhost:${APP_PORT:-5000}"
echo "Check readiness with: curl http://localhost:${APP_PORT:-5000}/health"
