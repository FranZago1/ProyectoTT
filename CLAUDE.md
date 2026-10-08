# Traductor de carruseles · Pulso Económico

Herramienta que traduce carruseles de finanzas (TikTok / Instagram) del inglés al español rioplatense
formal, conserva gráficos y diseño, y pone el logo de Pulso Económico.

## Cómo responder a pedidos habituales

- **El usuario pega un link de TikTok** (con o sin texto): seguí `.claude/commands/traducir.md` con ese
  link. Resultado: `listos/<slug>/` con las fotos traducidas. Si pega varios, procesalos **de a uno**
  (terminá uno completo, incluida la memoria, antes de empezar el siguiente), cada uno en su carpeta.
- **Pide un carrusel nuevo sobre un tema** (sin material de origen): usá `memoria/ESTILO.md`.
- **Pide consolidar el estilo**: `.claude/commands/estilo.md`.

## Entorno

- Las dependencias se instalan solas al abrir la sesión (`.claude/hooks/session-start.sh` →
  `scripts/instalar.sh`). Si algo falla: `bash scripts/instalar.sh`.
- Todo se corre con `.venv/bin/python -m carrusel …` (ver `README.md`). Tests: `.venv/bin/python -m pytest -q tests`.

## Reglas

- Traducción fiel: no corregir el contenido; las afirmaciones dudosas van a `notas_revisar`.
- Español rioplatense formal con voseo; formato numérico argentino (ver `memoria/GLOSARIO.md`).
- No versionar `entrada/`, `trabajo/`, `salida/` ni `listos/`. Sí `memoria/`, `config.yaml`, `fuentes/`, `marca/`.
- El contenido traducido es de terceros: recordar al usuario dar crédito o pedir permiso al autor.
