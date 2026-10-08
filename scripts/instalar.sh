#!/bin/bash
# Instala todo lo necesario para el traductor. Idempotente y no interactivo.
# Lo ejecuta el hook de inicio de sesión de Claude Code; también se puede correr a mano:
#   bash scripts/instalar.sh
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RAIZ"
log() { echo "[instalar] $*" >&2; }

# 1) Python 3.10+ y entorno virtual
PY=""
for c in python3.13 python3.12 python3.11 python3.10 python3; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(sys.version_info < (3, 10))'; then
    PY="$c"; break
  fi
done
if [ -z "$PY" ]; then
  log "ERROR: hace falta Python 3.10 o superior (https://www.python.org/downloads/)"
  exit 1
fi
if [ ! -x .venv/bin/python ]; then
  log "creando .venv con $PY"
  "$PY" -m venv .venv
fi

# 2) Dependencias de Python (solo si cambió requirements.txt)
SELLO=.venv/.requirements.sha
ACTUAL="$(cat requirements.txt | (sha256sum 2>/dev/null || shasum -a 256) | cut -d' ' -f1)"
if [ ! -f "$SELLO" ] || [ "$(cat "$SELLO")" != "$ACTUAL" ]; then
  log "instalando dependencias de Python"
  .venv/bin/python -m pip install -q --upgrade pip
  .venv/bin/python -m pip install -q -r requirements.txt
  echo "$ACTUAL" > "$SELLO"
fi

# 3) Tesseract (OCR)
if ! command -v tesseract >/dev/null 2>&1; then
  if [ "$(uname -s)" = "Darwin" ] && command -v brew >/dev/null 2>&1; then
    log "instalando tesseract con Homebrew"
    brew install tesseract >/dev/null
  elif command -v apt-get >/dev/null 2>&1; then
    SUDO=""
    [ "$(id -u)" -ne 0 ] && SUDO="sudo -n"
    log "instalando tesseract con apt-get"
    if ! { $SUDO apt-get install -y -q tesseract-ocr tesseract-ocr-eng >/dev/null 2>&1 || \
           { $SUDO apt-get update -q >/dev/null 2>&1 && \
             $SUDO apt-get install -y -q tesseract-ocr tesseract-ocr-eng >/dev/null 2>&1; }; }; then
      log "AVISO: no se pudo instalar tesseract sin contraseña. Corré: sudo apt-get install tesseract-ocr"
    fi
  else
    log "AVISO: instalá tesseract a mano (macOS: brew install tesseract; Windows: usar WSL)"
  fi
fi

# 4) Verificación rápida
.venv/bin/python -c "import pymupdf, cv2, PIL, numpy, matplotlib, yaml, pytesseract, fontTools" \
  && log "Python OK" || { log "ERROR: faltan paquetes de Python"; exit 1; }
command -v tesseract >/dev/null 2>&1 && log "tesseract OK ($(tesseract --version 2>&1 | head -1))" \
  || log "AVISO: tesseract no está instalado; el OCR no va a funcionar"
exit 0
