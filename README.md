# Traductor de carruseles de Instagram (EN → ES-AR)

Traduce carruseles de 7 slides del inglés al español rioplatense formal, conservando gráficos y diseño,
y deja cada slide lista para Canva. Además mantiene una memoria de estilo (`memoria/ESTILO.md`).

1. Instalar: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt` y el binario
   `tesseract` (`apt install tesseract-ocr` / `brew install tesseract`). Fuentes ya incluidas en `fuentes/`.
2. Descargar las imágenes o el PDF del carrusel en `entrada/<slug>/` (PNG/JPG 1080×1350 o capturas).
3. En Claude Code: `/traducir <slug>`. Recorre todos los pasos, decide orden, traducción y estrategia
   de cada gráfico, y actualiza la memoria.
4. Solo lo mecánico: `.venv/bin/python -m carrusel traducir <slug>`. Pasos sueltos: `preparar`,
   `ordenar`, `extraer`, `graficos`, `renderizar`, `calidad`, `paleta`, `memoria` (más `--desde <paso>`).
5. Leer `salida/<slug>/revisar.md`: pendientes, alertas de contenido y qué retocar.
6. Subir a Canva `NN_es.png` (final) o `NN_limpia.png` + `graficos/` + `textos_es.md` para editar.
7. Criterio editable en `trabajo/<slug>/plan.json` (textos, roles, estrategias); configuración en
   `config.yaml`; decisiones tomadas en `DECISIONES.md`.
8. Carrusel nuevo sin material de origen: pegar `memoria/ESTILO.md` en un chat y pedir el tema.
