#!/bin/bash
# Hook de inicio de sesión (Claude Code local y web): deja instaladas las dependencias del traductor.
set -euo pipefail
cd "${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
bash scripts/instalar.sh
