# Traductor de carruseles (EN → ES-AR) · Pulso Económico

Traduce carruseles de Instagram o TikTok del inglés al español rioplatense formal, conservando gráficos y
diseño, pone el logo de Pulso Económico y deja cada slide lista para Canva. Mantiene una memoria de
estilo (`memoria/ESTILO.md`).

1. Instalar: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt` y el binario
   `tesseract` (`apt install tesseract-ocr` / `brew install tesseract`). Fuentes incluidas en `fuentes/`.
2. Entrada, una de dos:
   - **link de TikTok** (carrusel de fotos): `/traducir https://vt.tiktok.com/…` — baja las imágenes
     originales sola;
   - **imágenes o PDF** en `entrada/<slug>/` (PNG/JPG originales o capturas) → `/traducir <slug>`.
3. `/traducir` (Claude Code) recorre todo: decide orden, traducción y estrategia de cada gráfico.
4. Solo lo mecánico: `.venv/bin/python -m carrusel traducir <slug|link> [slug]`. Pasos sueltos:
   `descargar`, `preparar`, `ordenar`, `extraer`, `graficos`, `renderizar`, `calidad`, `paleta`, `memoria`
   (con `--desde <paso>`).
5. Leer `salida/<slug>/revisar.md`: pendientes, alertas de contenido y qué retocar.
6. Subir `NN_es.png`, o armar en Canva con `NN_limpia.png` + `graficos/` + `textos_es.md`.
7. Logo: `python -m carrusel marca` genera `marca/` (SVG, PNG negro/blanco, fotos de perfil 1080 × 1080).
8. Carrusel nuevo sin material de origen: pegar `memoria/ESTILO.md` en un chat y pedir el tema.
