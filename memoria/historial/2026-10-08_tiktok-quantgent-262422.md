# 2026-10-08 — tiktok-quantgent-262422

**Título original:** Benford's Law: The Equation That Catches Tax Fraud Using Just the First Digit  
**Título en español:** La ley de Benford: la ecuación que detecta fraudes fiscales con solo el primer dígito  
**Motor OCR:** tesseract · **Orden de páginas:** [1, 2, 3, 4, 5, 6, 7, 8]

## Slide 1 — Portada: concepto + promesa + gancho

- *titulo* (bold, 88 px): La ley de Benford
- *subtitulo* (regular, 46 px): La ecuación que detecta fraudes fiscales con solo el primer dígito
- *cuerpo* (regular, 40 px): El IRS (el fisco de EE. UU.), los contadores forenses y hasta el FBI la usan para detectar números falsos al instante. Veamos cómo funciona.
- **Gráfico** (superficie 3D con curvas de nivel, sin relación directa con la ley de Benford) — estrategia C: Superficie 3D decorativa (solo ticks numéricos): se conserva.
- ⚠ Sin fuente: que el IRS y el FBI usen la ley de Benford «para detectar números falsos al instante». Es una herramienta de auditoría conocida (Nigrini), pero sirve para señalar casos a revisar, no para detectar fraudes «al instante».
- ⚠ Gráfico de portada decorativo: no representa la ley de Benford.

## Slide 2 — Planteo: el primer dígito de cada número

- *cuerpo* (regular, 45 px): Todo número empieza con un primer dígito.
- *cuerpo* (regular, 45 px): $142 empieza con 1. $873 empieza con 8. $45 empieza con 4.
- *cuerpo* (regular, 42 px): Hay solo 9 primeros dígitos posibles. Del 1 al 9.
- **Gráfico** (foto: columnas de números) — estrategia C: Foto de números (desenfocada): no tiene texto en lenguaje natural; se conserva.
- ⚠ La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o reemplazarla en Canva.

## Slide 3 — La intuición equivocada: cada dígito, 11 %

- *cuerpo* (regular, 45 px): Entonces, si tomaras miles de números reales… Precios de acciones, declaraciones juradas, poblaciones… Esperarías que cada dígito apareciera más o menos la misma cantidad de veces, ¿no?
- *destacado* (bold, 46 px): ¿Cada uno, alrededor del 11 % de las veces?
- *cuerpo* (regular, 45 px): Es lo que piensa la mayoría.
- *destacado* (bold, 45 px): Se equivocan.
- **Gráfico**: ninguno.
- ⚠ El original no cierra «They're wrong» con punto; en español se agregó.

## Slide 4 — La revelación: el 1 aparece primero el 30 % de las veces (gráfico)

- *destacado* (bold, 45 px): El 1 es el primer dígito el 30 % de las veces. No el 11 %.
- *cuerpo* (regular, 45 px): Y se pone más raro… cada dígito siguiente cae en una curva perfecta. El 9 aparece menos del 5 % de las veces.
- *cuerpo* (regular, 45 px): Este patrón aparece en casi todos los conjuntos de datos naturales del planeta.
- **Gráfico** (barras: frecuencia del primer dígito según la ley de Benford (1-9) y línea del 11,1 %) — estrategia B: Barras que salen exactamente de la fórmula de la slide 5, P(d) = log10(1 + 1/d); coinciden con los valores del original.
  - datos: `{"tipo": "barras_umbral", "categorias": ["1", "2", "3", "4", "5", "6", "7", "8", "9"], "valores": [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6], "formula": "P(d) = log10(1 + 1/d)", "umbral": 11.1, "decimales": 1, "color_ini": "#2A8C5A", "color_fin": "#76B597", "color_bajo": "#4E9C77", "color_alto": "#2E8B57", "color_umbral": "#C0393B", "rotulo_umbral": "Esperado: 11,1 %", "rotulo_umbral_lado": "derecha", "tam_rotulo_umbral": 13.5, "tam_valor": 14.5, "rotulo_x": "Primer dígito", "margen_inferior": 0.17, "tam_ticks": 17, "ticks_negrita": true}`
- ⚠ Exageración: «casi todos los conjuntos de datos naturales». La ley se cumple en datos que abarcan varios órdenes de magnitud y sin topes (precios, poblaciones, montos); no en alturas, edades, números de teléfono o precios fijados (p. ej., $9,99).
- ⚠ Gráfico regenerado (B) con la fórmula: 30,1 / 17,6 / 12,5 / 9,7 / 7,9 / 6,7 / 5,8 / 5,1 / 4,6 %, igual que el original.

## Slide 5 — La fórmula y la intuición + Simon Newcomb

- *titulo* (regular, 46 px): La fórmula
- *otro* (bold, 47 px): P(d) = log₁₀(1 + 1/d)
- *cuerpo* (regular, 42 px): La intuición es esta: pasar de 1 a 2 requiere duplicarse… Un aumento del 100 %. Pasar de 8 a 9 es solo un aumento del 12 %. Los números “pasan más tiempo” empezando con dígitos bajos porque cuesta más superarlos. Por eso domina el 1.
- **Gráfico** (foto: retrato de Simon Newcomb) — estrategia C: Retrato con pie que es un nombre propio (Simon Newcomb): se conserva.
- ⚠ Precisión: de 8 a 9 el aumento es del 12,5 % (el original redondea a 12 %).
- ⚠ Contexto que falta: Simon Newcomb (el del retrato) describió el fenómeno en 1881; Frank Benford lo redescubrió y lo documentó con datos en 1938. El carrusel no lo explica.
- ⚠ La intuición de «pasar más tiempo» vale para cantidades que crecen de forma multiplicativa (exponencial).

## Slide 6 — Aplicación: cómo se detecta a quien inventa números

- *titulo* (bold, 50 px): ¿Y cómo se atrapa a un mentiroso?
- *cuerpo* (regular, 42 px): Cuando la gente inventa números, reparte los dígitos de forma pareja… Alrededor del 11 % cada uno. Su intuición le dice que eso parece “aleatorio”. Pero los datos reales siguen la curva de Benford. Así que una distribución plana es una enorme señal de alerta. Los contadores forenses comparan los datos con la curva de Benford… Y los falsos saltan a la vista al instante.
- **Gráfico** (foto: planilla contable bajo una lupa) — estrategia C: Foto de una planilla con lupa (texto ilegible, de ambientación): se conserva.
- ⚠ La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o reemplazarla en Canva.
- ⚠ Simplificación: quien inventa números no siempre los reparte de forma pareja; la prueba de Benford señala desvíos a investigar, no prueba un fraude.

## Slide 7 — Casos: Enron, elecciones de Irán 2009, tribunales de EE. UU.

- *titulo* (bold, 50 px): Ya se usó en los tribunales
- *cuerpo* (regular, 41 px): La ley de Benford se usó como prueba en el escándalo de Enron. Detectó irregularidades en los resultados de la elección de 2009 en Irán. Fue admitida como prueba en tribunales federales de EE. UU. Y funciona con todo… Desde la magnitud de los terremotos hasta la cantidad de seguidores en Twitter o tu factura de luz.
- **Gráfico** (foto: audiencia en una sala) — estrategia C: Foto (audiencia) sin texto: se conserva.
- ⚠ La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o reemplazarla en Canva.
- ⚠ Verificar: «se usó como prueba en el escándalo de Enron». Lo documentado son análisis posteriores de los estados contables de Enron con la ley de Benford, no su uso como prueba en el juicio.
- ⚠ Matizar: sobre Irán 2009 hubo análisis con Benford (p. ej., Mebane), pero su validez para detectar fraude electoral es discutida.
- ⚠ Imprecisión: «funciona con todo». No funciona con datos acotados o asignados (ver slide 4). La factura de luz y los seguidores de Twitter son ejemplos citados en estudios puntuales.

## Slide 8 — Cierre: lo que revela sobre la naturaleza, sin gráfico

- *titulo* (regular, 49 px): La lección de Benford no es la matemática…
- *destacado* (bold, 46 px): Es lo que revela sobre la naturaleza.
- *cuerpo* (regular, 42 px): El universo no distribuye las cosas de forma pareja. El crecimiento, el deterioro y el azar dejan huellas en los números. La ley de Benford simplemente nos enseñó a leerlas.
- **Gráfico**: ninguno.
