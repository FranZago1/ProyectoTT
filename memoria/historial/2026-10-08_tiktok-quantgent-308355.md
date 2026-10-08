# 2026-10-08 — tiktok-quantgent-308355

**Título original:** The Birthday Paradox: The Interview Question That Breaks Quant Candidates  
**Título en español:** La paradoja del cumpleaños: la pregunta de entrevista que desarma a los aspirantes a quants  
**Motor OCR:** tesseract · **Orden de páginas:** [1, 2, 3, 4, 5, 6]

## Slide 1 — Portada: concepto + promesa + gancho

- *titulo* (bold, 92 px): La paradoja del cumpleaños
- *subtitulo* (bold, 40 px): La pregunta de entrevista que desarma a los aspirantes a analistas cuantitativos (quants)
- *cuerpo* (regular, 34 px): Las mesas de trading de Wall Street la usan para evaluar la intuición probabilística. La mayoría se equivoca al instante. Veamos por qué.
- **Gráfico** (superficie 3D: probabilidad de coincidencia según personas en la sala (0-80) y días del año (100-500)) — estrategia C: Superficie 3D (matplotlib) sin datos explícitos en el texto: se conserva; se traducen los dos rótulos de ejes (rotados) y los ticks quedan sin tocar.
- ⚠ Afirmación sin fuente: «Las mesas de trading de Wall Street la usan para evaluar la intuición probabilística» y «la mayoría se equivoca al instante». Es una pregunta conocida de entrevistas, pero no hay evidencia citada.
- ⚠ Gráfico 3D: los rótulos de ejes son chicos y rotados; si en Canva se ven borrosos, reescribirlos a mano. Los ticks (0.0-1.0 con punto decimal) se conservaron (estrategia C).

## Slide 2 — Planteo: la pregunta y las respuestas intuitivas

- *cuerpo* (regular, 34 px): ¿Cuántas personas tiene que haber en una sala para que dos de ellas cumplan años el mismo día?
- *cuerpo* (regular, 34 px): Hay 365 cumpleaños posibles. Entonces necesitarías una multitud, ¿no?
- *cuerpo* (regular, 34 px): La mayoría arriesga alrededor de 180. Algunos dicen 100. Unos pocos, 50.
- *destacado* (bold, 34 px): Todos están muy lejos.
- **Gráfico** (foto: grupo de personas en una fiesta) — estrategia C: Fotografía (gente en una fiesta) sin texto: se conserva.
- ⚠ La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o reemplazarla en Canva.
- ⚠ Sin fuente: «La mayoría arriesga alrededor de 180. Algunos dicen 100. Unos pocos, 50.» No se cita encuesta ni estudio.

## Slide 3 — Respuesta y evidencia: 23 personas (gráfico de probabilidades)

- *titulo* (bold, 39 px): La respuesta es 23.
- *cuerpo* (regular, 34 px): Con solo 23 personas, la probabilidad de que dos cumplan años el mismo día ya es mayor al 50 %. Con 70 personas, es del 99,9 %.
- *cuerpo* (regular, 34 px): No es un truco. No es una adivinanza. Es probabilidad pura. Y destruye la intuición de casi todo el mundo.
- **Gráfico** (barras: probabilidad de al menos una coincidencia para 5-70 personas, línea del 50 %) — estrategia B: Barras con valores que salen exactamente de la fórmula de la slide 5 (P(n) = 1 − 365! / ((365 − n)! · 365ⁿ)); coinciden con las del original a un decimal.
  - datos: `{"tipo": "barras_umbral", "categorias": ["5", "10", "15", "23", "30", "40", "50", "60", "70"], "valores": [2.7, 11.7, 25.3, 50.7, 70.6, 89.1, 97.0, 99.4, 99.9], "formula": "P(n) = 1 − 365! / ((365 − n)! · 365^n)", "umbral": 50, "decimales": 1, "color_ini": "#2E6B4A", "color_fin": "#22A03C", "color_bajo": "#2E7D46", "color_alto": "#B83A32", "color_umbral": "#C9433A", "rotulo_umbral": "Esperado: 50 %", "rotulo_x": "Personas en la sala"}`
- ⚠ Cifras verificadas con la fórmula (365 días equiprobables, sin 29 de febrero ni mellizos): 23 → 50,7 %; 70 → 99,9 % (99,916 %). Con la distribución real de nacimientos, la probabilidad es apenas mayor.
- ⚠ Gráfico regenerado (B): mismos valores que el original. El rótulo «Expected 50%» (que en el original pisaba la barra de 70) se reubicó arriba de la línea, a la izquierda, como «Esperado: 50 %».

## Slide 4 — Mecanismo: no es tu cumpleaños, son todos los pares

- *titulo* (bold, 40 px): Por qué tu cerebro falla.
- *cuerpo* (regular, 34 px): Escuchás “coincidencia de cumpleaños” y pensás… en alguien que cumpla años el mismo día que YO. Eso es 1 en 365. Ínfimo.
- *destacado* (bold, 34 px): Pero la pregunta no es sobre vos. Es sobre cualquier par.
- *cuerpo* (regular, 34 px): Con 23 personas hay 253 pares distintos. Cada uno es una oportunidad de coincidencia. No tirás el dado una vez. Lo tirás 253 veces.
- **Gráfico** (diagrama: 23 personas en círculo; se resaltan los 22 pares que te incluyen y, tenues, los 253) — estrategia A: Diagrama con dos rótulos sobre fondo casi liso: se borran y se reescriben.
- ⚠ Precisión: «1 en 365» es la probabilidad de coincidir con una persona puntual; con 22 personas más, la de que alguien comparta tu cumpleaños es ≈ 5,9 %.
- ⚠ Precisión: los 253 pares no son tiradas independientes; 1 − (364/365)^253 ≈ 50,0 % es una aproximación (el valor exacto es 50,7 %). La traducción es fiel a la metáfora del dado.

## Slide 5 — Fórmula y método (complemento) + qué buscan los entrevistadores

- *titulo* (regular, 34 px): La fórmula
- *otro* (bold, 37 px): P(coincidencia) = 1 − (365! / ((365 − n)! × 365ⁿ))
- *cuerpo* (regular, 34 px): En lugar de contar coincidencias, calculá la probabilidad de que todos cumplan años en días distintos. Después, restala de 1. Cada persona nueva tiene que esquivar todos los cumpleaños ya ocupados. Para la persona 23, el esquive falla más de la mitad de las veces.
- *destacado* (bold, 34 px): Quienes entrevistan a quants no quieren que memorices el número. Quieren ver que recurras a esto.
- **Gráfico** (foto: sala de trading) — estrategia C: Fotografía (sala de trading) sin texto legible: se conserva.
- ⚠ La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o reemplazarla en Canva.
- ⚠ Fórmula correcta (supone 365 días equiprobables). Se tradujo «match» (coincidencia) y se usaron × y superíndice ⁿ en lugar de «x» y «^n».
- ⚠ Imprecisión: «para la persona 23, el esquive falla más de la mitad de las veces» describe la probabilidad acumulada; la persona 23 por sí sola falla solo 22/365 ≈ 6 % de las veces.
- ⚠ Sin fuente: qué buscan «quienes entrevistan a quants».

## Slide 6 — Cierre aforístico sin gráfico

- *cuerpo* (regular, 34 px): La lección de la paradoja del cumpleaños no es el número 23…
- *destacado* (bold, 34 px): Es que los humanos razonan de forma lineal ante problemas combinatorios.
- *cuerpo* (regular, 34 px): Los pares crecen con el cuadrado del grupo. Tu intuición cuenta personas. La matemática cuenta conexiones. Los mejores quants aprenden a detectar ese instinto y a imponerse a él.
- **Gráfico**: ninguno.
- ⚠ Precisión: los pares son n(n − 1)/2, que crece aproximadamente con el cuadrado del grupo (fiel al original).
