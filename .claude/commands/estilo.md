---
description: Consolida memoria/ESTILO.md con todos los carruseles del historial y resume qué cambió
---

Reescribí `memoria/ESTILO.md` **consolidando, no agregando al final**:

1. Leé todas las fichas de `memoria/historial/*.md` (y sus `.plan.json` si hace falta detalle),
   `memoria/GLOSARIO.md` y `memoria/paletas.json`.
2. Recalculá la evidencia de cada patrón como «n/N carruseles» (N = cantidad de fichas). Subí a patrón
   lo que se repite, bajá a variante lo que dejó de ser mayoritario y quitá lo que ya no tiene evidencia.
3. Respetá la estructura obligatoria: 1) instrucciones para el modelo (bloque textual, sin cambios),
   2) estructura narrativa 1-7, 3) portadas y títulos, 4) cuerpo, 5) cierres, 6) gráficos, 7) diseño
   (con el bloque de paleta entre `<!-- PALETA:INICIO … -->` y `<!-- PALETA:FIN -->`, que regenera
   `python -m carrusel memoria <slug>`), 8) tono y registro + hacer / no hacer (todas las alertas de
   contenido de las fichas, para no repetirlas), 9) glosario resumido (20-30 términos), 10) carruseles de
   referencia resumidos slide por slide en español (si son muchos, los 2-3 más representativos).
4. Límite: **≤ 2.500 palabras** (verificalo con `wc -w`).
5. Resumí en 5-10 líneas qué cambió respecto de la versión anterior (`git diff memoria/ESTILO.md`) y
   commiteá.
