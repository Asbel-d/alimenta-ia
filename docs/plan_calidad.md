# Plan de Calidad — ALIMENTA-IA

| Objetivo de Calidad | Control Preventivo | Prueba o Evidencia | Responsable | Criterio de Aceptación |
| :--- | :--- | :--- | :--- | :--- |
| **Evitar registros inválidos** | Validación de precondiciones en `tasa_defectos()` y `validar_lote()`. | `tests/test_produccion.py` con `pytest.raises(ValueError)`. | Desarrollador / QA | 100% de entradas inválidas rechazadas. |
| **Asegurar cambios trazables** | Ramas `feature/GH-XX-*`, *Conventional Commits* y Pull Requests revisados. | Historial Git y PRs vinculados a tickets `GH-01`, `GH-02`, `GH-03`. | Configuración / PO | 100% de cambios en `main` con PR y pruebas aprobadas. |
| **Detectar fallas de IA** | Escalado de variables, semilla fija (`random_state=42`) y advertencia orientativa. | `tests/test_calidad.py` y matriz de confusión sobre 36 lotes sintéticos. | Medición / QA | Recall >= 80% (100% obtenido) y aviso ético visible. |
