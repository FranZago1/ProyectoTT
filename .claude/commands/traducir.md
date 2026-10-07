---
description: Traduce un carrusel de entrada/<slug> (EN → ES-AR) de punta a punta, en modo autónomo, y actualiza la memoria
argument-hint: <slug>
---

Traducí el carrusel `entrada/$ARGUMENTS/` siguiendo el archivo «Traductor carruseles economía
Instagram» del repo, en **modo autónomo**: sin preguntas; cada decisión por defecto va a `DECISIONES.md`
con una línea de justificación.

1. `.venv/bin/python -m carrusel preparar $ARGUMENTS` y `ordenar $ARGUMENTS`. Mirá `trabajo/$ARGUMENTS/paginas/`:
   si el orden no es obvio, fijá `"orden"` en `trabajo/$ARGUMENTS/plan.json` y volvé a `ordenar`.
2. `.venv/bin/python -m carrusel extraer $ARGUMENTS` (borrador con OCR, zonas, tamaños y negritas).
3. Curá `plan.json` mirando cada slide (seguí el modelo de `scripts/curar_referencia.py`): texto exacto en
   inglés, `texto_es` según `memoria/GLOSARIO.md` y las reglas del .md (voseo, coma decimal, US$ … millones,
   negritas como en el original), roles, `funcion`, estrategia A/B/C/D de cada gráfico con `justificacion`,
   `datos` exactos si es B, `notas_revisar` con toda afirmación dudosa, `glosario_nuevo`, y `"curado": true`.
4. `.venv/bin/python -m carrusel traducir $ARGUMENTS --desde graficos`.
5. Control de calidad: abrí y mirá **cada** `salida/$ARGUMENTS/NN_es.png` y `control.png` (restos de inglés
   o de UI, desbordes, superposición con el gráfico, negritas, tildes/ñ/¿/—/×/σ, manchas de fondo, cifras,
   valores de los gráficos regenerados). Corregí y repetí; lo que no se pueda resolver va a `notas_revisar`
   con la indicación exacta para Canva.
6. Memoria: el paso `memoria` ya escribió la ficha y el glosario; después corré `/estilo` para consolidar
   `memoria/ESTILO.md`.
7. Commit de `memoria/`, `DECISIONES.md` y cambios de código. Informe final breve: estrategia por gráfico y
   pendientes de `revisar.md` por slide.
