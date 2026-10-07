# Traductor de carruseles de Instagram (EN → ES-AR) + memoria de estilo

## MODO DE EJECUCIÓN: AUTÓNOMO DE PRINCIPIO A FIN

La instrucción que vas a recibir es "seguí el .md y hacé todo". Eso significa:

- **Ejecutá todas las fases seguidas, sin frenar y sin hacer preguntas.** No hay checkpoints.
- Cada vez que normalmente consultarías (orden de slides, término dudoso, estrategia de un gráfico, tipografía), **tomá la decisión por defecto que indica este archivo**, seguí adelante y registrala en `DECISIONES.md` con una línea de justificación.
- Si algo falla (una dependencia no instala, un OCR no anda, no hay red), **usá el plan B indicado** y seguí. Solo te detenés si no queda ninguna alternativa viable, y en ese caso dejás todo lo hecho hasta ahí funcionando y documentado.
- Verificá tu propio trabajo mirando las imágenes generadas (sección "Control de calidad") y corregí antes de dar por terminado.
- Terminás cuando se cumple la **Definición de terminado** (al final). Tu último mensaje es el informe final.

## Objetivo

1. Construir una herramienta local (CLI en Python, sin interfaz gráfica, sin estética) que traduzca carruseles de Instagram de 7 slides sobre finanzas cuantitativas y economía, del inglés al español rioplatense formal, **conservando gráficos y diseño**, y deje cada slide lista para subir o retocar en Canva.
2. Procesar con ella los dos carruseles de referencia.
3. Generar la **memoria de estilo** (`memoria/ESTILO.md`), pensada para pegarse en un chat y pedir carruseles nuevos sin material de origen.

## Entrada de referencia

`entrada/referencia/Carrusel_2.pdf` (si no está ahí, buscá cualquier PDF o imágenes en el repo o en el directorio de uploads y copialas ahí): 14 páginas con **dos carruseles de 7 slides** capturados como screenshots de Instagram, **no necesariamente en orden**.

Las capturas incluyen elementos de la interfaz de Instagram que **no son parte de la slide** y hay que eliminar: barra gris superior con la flecha "<", márgenes blancos de la página del PDF, contador "7 / 7" (píldora gris arriba a la derecha), sombras o degradados en los bordes.

La herramienta también tiene que aceptar PNG/JPG sueltos (caso futuro: imágenes originales 1080×1350). Salida siempre en **1080×1350**; si la fuente es de menor resolución, escalar con Lanczos y anotarlo.

## Stack y planes B

- **Python 3.11+**, entorno `.venv` (si no se puede crear, instalar con `pip install --break-system-packages`). CLI: `python -m carrusel <comando> <slug>`. Configuración en `config.yaml`.
- PDF → imágenes: PyMuPDF (`fitz`) a 200–300 dpi. Plan B: `pdftoppm`.
- OCR con cajas (necesario sobre todo para etiquetas de gráficos): si el sistema es macOS, `ocrmac`; si no, EasyOCR. Plan B: Tesseract. Plan C: transcribir el texto vos mismo mirando las imágenes y ubicar regiones de texto con OpenCV (umbral + morfología). Probá el primario sobre 2 páginas; si la calidad es mala, pasá al siguiente. Registrá cuál quedó.
- Imagen: OpenCV + Pillow. Gráficos regenerados: matplotlib. Paleta: k-means con numpy.
- Tipografía: **Inter** (licencia OFL) descargada a `fuentes/` desde Google Fonts o el repo `rsms/inter`. Plan B si no hay red: la sans-serif más parecida disponible en el sistema (DejaVu Sans, Liberation Sans, Helvetica), registrada en `DECISIONES.md`.

## Arquitectura

No hay llamadas a APIs externas desde el código. Los scripts hacen lo mecánico (preparar, extraer, borrar, renderizar, regenerar gráficos, paleta). **Vos hacés lo que requiere criterio** (ordenar, corregir OCR mirando las imágenes, elegir estrategia de cada gráfico, traducir, escribir la memoria) y volcás esas decisiones en `trabajo/<slug>/plan.json`, que los scripts consumen.

```
entrada/<slug>/                     # PDF o PNGs tal como se descargan
trabajo/<slug>/
    slides/01.png … 07.png          # recortadas, sin UI de Instagram, en orden
    plan.json                       # zonas, bloques, traducción, estrategia por gráfico
salida/<slug>/
    01_es.png …                     # slide final traducida
    01_limpia.png …                 # slide sin texto (fondo para Canva)
    graficos/01_grafico_es.png …    # gráficos traducidos o regenerados, sueltos
    textos_es.md                    # textos por slide, listos para copiar
    revisar.md                      # pendientes y alertas
memoria/
    ESTILO.md
    GLOSARIO.md
    historial/AAAA-MM-DD_<slug>.md
fuentes/
carrusel/                           # código
config.yaml
DECISIONES.md                       # registro de decisiones tomadas en modo autónomo
README.md                           # uso en 10 líneas
```

Slugs para la referencia: `fat-tails` y `ergodicity`.

## Modelo de la slide

Fondo claro casi liso (blanco o gris muy claro con degradado suave), **zona de texto** arriba y centrada, y opcionalmente **una zona de gráfico** abajo (a veces dos lado a lado, a veces ninguna), con pie chico en gris.

**No reemplazar texto línea por línea**: la zona de texto completa se borra y se **recompone entera** en español con reflujo libre. Así se absorbe el 20–30 % de largo extra del español.

`plan.json` por slide:
- `zona_texto` (bbox) y `bloques` ordenados: `rol` (titulo | subtitulo | cuerpo | destacado | cita | pie | otro), `texto_en`, `texto_es`, `peso` (regular | semibold | bold), `tam_px`, `color`.
- `zonas_grafico`: bbox, `estrategia` (A/B/C/D), `justificacion`, `etiquetas` (texto_en, texto_es, bbox) y `datos`/`formula` si se regenera.
- `elementos_ui_eliminados`.

## Flujo por carrusel (comando `traducir <slug>` = todos los pasos)

1. **preparar**: rasterizar si es PDF, detectar el rectángulo de la slide, recortar, eliminar UI de Instagram, normalizar a 1080×1350.
2. **agrupar y ordenar** (si hay más de 7 páginas o el orden no es obvio). Pistas: portada con título grande y subtítulo; contador "n / 7"; continuidad del argumento; cierre aforístico, a veces sin gráfico. **Orden por defecto para la referencia** (verificalo mirando las páginas; si la evidencia lo contradice, corregí y registralo):
   - `fat-tails`: páginas 2 → 7 → 6 → 1 → 8 → 4 → 3
   - `ergodicity`: páginas 5 → 9 → 10 → 11 → 12 → 13 → 14
3. **extraer**: OCR + detección de zonas → `plan.json`; corregí el OCR mirando cada imagen.
4. **estrategia por gráfico** (decidila vos, con una línea de justificación):
   - **A. Etiquetas en el lugar**: borrar y reescribir solo los rótulos. Para gráficos con pocos textos sobre fondo liso.
   - **B. Regenerar con matplotlib**: solo si los datos se derivan **exactamente** del contenido (p. ej. moneda +50 % / −40 %; curva de Kelly g(f) = 0,5·ln(1+0,5f) + 0,5·ln(1−0,4f), con óptimo en f = 0,25 y g(1) ≈ −0,053; barras de valores dados; caminos $100 → $150 → $90 y $100 → $60 → $90). Si los datos salen de una simulación aleatoria, regenerar con semilla fija y marcarlo en `revisar.md` como "regenerado, no idéntico". Estilo: minimalista tipo seaborn, ejes finos grises, valores destacados en negrita, verde = ganancia, rojo = pérdida, gris = neutro, fondo igual al de la slide. **Nunca** reconstruir a ojo series de datos reales (p. ej. S&P 500): esas van por A o C.
   - **C. Conservar**: figuras académicas con notación matemática (P(x), E(L), VaR, ES, σ), ilustraciones, capturas. Traducir solo el texto en lenguaje natural si se puede hacer limpio (p. ej. "Loss" → "Pérdida", "5% probability" → "5 % de probabilidad", "Standard Deviations from the Mean" → "Desvíos estándar respecto de la media"); si no, dejarlo y anotarlo.
   - **D. Manual**: gráficos con mucho texto chico (p. ej. la línea de tiempo de LTCM). Conservar la imagen, poner la traducción completa de todos sus textos en `textos_es.md` y marcarlo en `revisar.md` como "rehacer en Canva".
5. **traducir**: completar `texto_es` según reglas y glosario.
6. **renderizar**: reconstruir el fondo de la zona de texto (muestrear el color por fila para respetar el degradado; inpainting solo si hace falta), recomponer el texto, aplicar la estrategia de cada gráfico, generar `salida/<slug>/` completo.
7. **control de calidad** (ver abajo) y corrección.
8. **actualizar memoria**.

## Reglas de traducción

**Registro**: español rioplatense formal y sobrio, con **voseo** porque el original interpela al lector todo el tiempo ("Imaginá", "tenés", "perdés"). Nada de lunfardo ni coloquialismos. Referencia: secciones de economía de la prensa argentina.

**Conservar los recursos retóricos**: oraciones cortas, pregunta-respuesta ("¿Los derrumbes? Prácticamente imposibles."), tríadas ("Misma apuesta. Mismas probabilidades. Misma matemática."), antítesis de cierre, guiones largos (—). Lo que está en negrita en el original sigue en negrita.

**Números (los valores nunca cambian, solo el formato):**
- Coma decimal, punto de miles, espacio antes de %: 99.7% → 99,7 %; 10,000 → 10.000; 0.5 x 1.50 → 0,5 × 1,50.
- Montos reales en dólares, estilo prensa argentina: $3.6 billion → US$ 3.600 millones; $100 billion → US$ 100.000 millones; $553 million → US$ 553 millones; trillion → billones.
- Montos de ejemplos hipotéticos (juego de la moneda): mantener "$".
- Fechas: "17 de agosto de 1998".
- Gráficos regenerados (B): ticks con formato argentino. Gráficos conservados (C): ticks sin tocar.

**No traducir**: notación matemática, VaR, ES, nombres propios, instituciones sin traducción establecida, handles, tickers, "S&P 500".

**Glosario base** (aplicarlo tal cual y copiarlo a `GLOSARIO.md`):

| EN | ES |
|---|---|
| fat tails | colas gruesas |
| quants | quants (primera mención: "analistas cuantitativos (quants)") |
| bell curve | campana de Gauss |
| normal distribution | distribución normal |
| standard deviation | desvío estándar |
| kurtosis | curtosis |
| expected value / EV | valor esperado |
| ergodicity | ergodicidad |
| Kelly Criterion | criterio de Kelly |
| geometric growth rate | tasa de crecimiento geométrica |
| hedge fund | fondo de cobertura |
| Black Swan | cisne negro |
| coin flip / heads / tails | tirada de moneda / cara / ceca |
| flips (eje) | tiradas |
| break even | punto de equilibrio |
| crash | derrumbe (crac si es el nombre de un evento) |
| bearish | bajista |
| bailout / rescue | rescate |
| leverage | apalancamiento |
| defaults on its bonds | entra en default de sus bonos |
| wealth | patrimonio (riqueza si es abstracto) |
| crypto | cripto |
| Loss | Pérdida |
| "Past performance doesn't guarantee future results" | "Rendimientos pasados no garantizan rendimientos futuros" |

Términos nuevos: elegí la forma usual en la prensa económica argentina, agregala al glosario y registrala en `DECISIONES.md`.

## Verificación de contenido

No corrijas el contenido al traducir (es una traducción fiel), pero **anotá en `revisar.md`** toda afirmación dudosa, imprecisa o no verificable. Para la referencia, como mínimo:
- Slide de Kelly: "en 2020 Ole Peters lo probó formalmente" — sus trabajos centrales son de 2011 y 2016 (con Gell-Mann); la nota de Bloomberg con ese titular es de 2017.
- Slide de curtosis: "3x / 5x más eventos extremos" no se deduce de una curtosis de 10 o 15; el valor depende del período y la frecuencia de los retornos.
- Slide "This is what quants call: FAT TAILS": el "95 % en la realidad" no tiene sustento citado.
- Portada de ergodicidad: el gráfico (funciones de onda de Monte Carlo por difusión) no tiene relación con el tema.
- "They go broke. Every single time.": es un resultado con probabilidad 1 en el límite, no en cada caso finito.
- Ed Thorp "survived 1998 without a scratch": verificar.

Estas alertas también pasan a la memoria como "no repetir".

## Render

- Inter: títulos Bold/ExtraBold, cuerpo Regular/Medium, destacados SemiBold/Bold. Medí tamaños, interlineado y márgenes sobre el original y guardalos en `config.yaml`.
- Texto centrado, ancho de columna ≈ 75 % de la slide.
- Si el español no entra: reducir tamaño hasta 90 %; si sigue sin entrar, extender la zona hacia arriba si hay aire; si aún no entra, acortar la redacción sin perder contenido y anotarlo en `revisar.md`. Nunca pisar el gráfico.
- Desarrollá el renderer probando sobre una sola slide y recién después corré todo.

## Control de calidad (obligatorio antes de terminar)

Abrí y mirá **cada** `NN_es.png` y verificá:
- No quedan restos de texto en inglés, ni de la UI de Instagram (flecha, barra, contador).
- El texto no desborda, no se superpone con el gráfico y respeta márgenes.
- La negrita está donde corresponde y no hay caracteres rotos (tildes, ñ, ¿, ¡, —, ×, σ).
- El fondo reconstruido no muestra manchas ni cortes visibles del degradado.
- Las cifras coinciden con el original (comparar `texto_en` con `texto_es`).
- Los gráficos regenerados coinciden con los valores del original.

Corregí lo que falle y repetí. Lo que no puedas resolver bien va a `revisar.md` con la indicación exacta para retocarlo en Canva.

## Semilla de estilo (base para `ESTILO.md`, evidencia 2/2 salvo indicación)

**fat-tails — "Fat Tails: How Quants Profit From the Impossible".** Arco: portada con concepto y promesa → "la matemática te miente" (mito) → el modelo normal y la crisis de 2008 → nombre del concepto (colas gruesas) → cómo medirlo (curtosis) → caso histórico (LTCM, 1998) → figura ejemplar y moraleja (Ed Thorp) + definición de "cisne negro".

**ergodicity — "Ergodicity: The Reason Expected Value Destroys Portfolios".** Arco: portada con concepto y promesa → experimento mental (moneda +50 % / −40 %) → paradoja (promedio de 10.000 personas vs. una persona en el tiempo) → explicación paso a paso con $100 → el orden no importa, siempre se pierde → solución (criterio de Kelly) + historia (Kelly 1956, Ole Peters) → cierre aforístico sin gráfico.

Patrones:
- Tema: conceptos de finanzas cuantitativas y probabilidad para público general, tono de "lo que no te cuentan".
- Portada: concepto en una o dos palabras con título muy grande + subtítulo con promesa o paradoja + a veces un párrafo gancho + gráfico de aspecto académico.
- Cuerpo: 50–90 palabras por slide, oraciones de 3 a 15 palabras, segunda persona, preguntas retóricas, cifras concretas, una oración clave en negrita (frecuente en ergodicity).
- Cierre: aforismo con antítesis.
- Gráficos: uno por slide (salvo el cierre de ergodicity); dos familias: figuras importadas (papers, capturas, notación LaTeX) y gráficos propios minimalistas estilo matplotlib con verde/rojo semántico.
- Diseño: fondo blanco o gris muy claro con degradado suave, texto casi negro, todo centrado, pie de gráfico chico en gris.
- Paleta aproximada (reemplazar por la extraída automáticamente): verde ~#4F8A5B, rojo ~#B85A4E, gris ~#9A9A9A, naranja ~#E8A048, rojo intenso ~#C9433A, texto ~#1A1A1A.

## Memoria de estilo

Al terminar cada carrusel:
1. `memoria/historial/AAAA-MM-DD_<slug>.md`: tema, y por slide: función narrativa, texto final en español, tipo de gráfico y qué muestra, estrategia aplicada, alertas de verificación.
2. `memoria/GLOSARIO.md`: glosario completo y actualizado.
3. `memoria/ESTILO.md`: **reescribir consolidando, no agregar al final**; cada patrón con su evidencia ("2/2 carruseles"); paleta extraída automáticamente.

Estructura obligatoria de `ESTILO.md`:
1. **Instrucciones para el modelo que lo lea** (bloque inicial, textual): "Con esta guía, generá un carrusel de 7 slides sobre el tema indicado, en español rioplatense formal con voseo. Para cada slide entregá: función narrativa, título (si corresponde), texto con la oración destacada en **negrita**, especificación del gráfico (tipo, datos exactos o fórmula, ejes, unidades, período, fuente con fecha) y pie de gráfico. Usá solo datos reales y verificables con fuente; si no podés verificar un dato, marcalo [DATO A VERIFICAR]. Nunca inventes cifras, fechas ni citas. Preferí gráficos que se puedan generar a partir de datos o fórmulas explícitas."
2. Estructura narrativa (función de cada slide 1–7 y variantes).
3. Portadas y títulos (largo, recursos, ejemplos reales en español).
4. Cuerpo (densidad, largo de oraciones, recursos retóricos, negrita).
5. Cierres.
6. Gráficos (tipos, origen, rotulado, pies, colores semánticos).
7. Diseño (paleta en hex, tipografía y jerarquía, márgenes, ubicación de elementos).
8. Tono y registro + "hacer / no hacer" (incluye los errores de contenido detectados, para no repetirlos).
9. Glosario resumido (20–30 términos).
10. Los dos carruseles de referencia resumidos slide por slide, en español.

Límite: **≤ 2.500 palabras**.

## Extras a dejar creados

- `.claude/commands/traducir.md`: ejecuta el flujo completo sobre `entrada/$ARGUMENTS` en modo autónomo y actualiza la memoria.
- `.claude/commands/estilo.md`: consolida `ESTILO.md` y resume qué cambió.
- `README.md`: cómo instalar y cómo usar (descargar imágenes → `entrada/<slug>/` → `/traducir <slug>` → revisar `salida/<slug>/revisar.md` → Canva).
- `.gitignore`: `entrada/`, `trabajo/`, `salida/`, `.venv/`. Sí se versionan `memoria/`, `config.yaml`, `fuentes/`.
- `git init` y un commit final si el entorno lo permite.

## Definición de terminado

- [ ] La CLI corre de punta a punta con `python -m carrusel traducir <slug>` (y cada paso por separado).
- [ ] `salida/fat-tails/` y `salida/ergodicity/` completas: 7 `_es.png`, 7 `_limpia.png`, gráficos sueltos, `textos_es.md`, `revisar.md`.
- [ ] Control de calidad hecho sobre las 14 slides, con los problemas corregidos o documentados.
- [ ] `memoria/ESTILO.md` (≤ 2.500 palabras, con la estructura obligatoria), `memoria/GLOSARIO.md` y dos fichas en `memoria/historial/`.
- [ ] `DECISIONES.md`, `README.md`, comandos en `.claude/commands/` y `.gitignore` creados.

**Informe final** (tu último mensaje, breve): qué se construyó, qué motor de OCR y qué tipografía quedaron, estrategia aplicada a cada gráfico, lista de pendientes de `revisar.md` por slide, y la ruta de `memoria/ESTILO.md`.
