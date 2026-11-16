#!/usr/bin/env bash
# Vercel build step (see vercel.json): build the static results site into _site.
# The site builder compiles cmd/utopia, so fetch the Go version named in go.mod
# when the build image has no Go.
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v go >/dev/null 2>&1; then
  version="$(awk '$1 == "go" { print $2 }' go.mod)"
  curl -fsSL "https://go.dev/dl/go${version}.linux-amd64.tar.gz" | tar -xz -C /tmp
  export PATH="/tmp/go/bin:$PATH"
fi

python3 harness/build_site.py --out _site
