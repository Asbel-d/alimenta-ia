# Plan de Medición y Análisis — ALIMENTA-IA

| Indicador | Valor Obtenido | Meta | Interpretación | Acción Correctiva |
| :--- | :--- | :--- | :--- | :--- |
| **Aprobación de pruebas** | 100% (7/7) | 100% | Cumple reglas de validación y negocio. | Mantener ejecución obligatoria de `pytest` en cada PR. |
| **Cobertura de requisitos** | 100% (5/5 RF) | >= 90% | Todos los RF cuentan con prueba automatizada. | Actualizar matriz ante nuevos RF. |
| **PR revisados** | 100% (3/3) | 100% | Trazabilidad completa sin commits directos a `main`. | Mantener rama `main` protegida. |
| **Tasa defectos por lote** | Global: 2.93% (Normales: 1.69%, Atípicos: 9.27%) | Analizar tendencia | Lotes 031–036 elevan el promedio por desvíos térmicos. | Inspeccionar lotes marcados en planta simulada. |
| **Evaluación de IA (Recall)** | Recall: 100% (TP=6, FN=0, FP=0), Alertas: 16.67% | Reportar valor y límites | Detecta los 6 lotes atípicos sintéticos; muestra pequeña (n=36). | Recalibrar umbral al ampliar el dataset. |
