# ALIMENTA-IA — Sistema Educativo de Calidad y Detección de Anomalías (NutriAlimentos S.A.S.)

Prototipo académico desarrollado para la asignatura **Administración de Proyectos de Software** (Ingeniería de Sistemas, décimo semestre).

## Integrantes
- Asbel Duque
- Carlos Ballesteros
- Juan Fernando Pulgarín

## Propósito y Aviso de Uso Responsable de IA
ALIMENTA-IA registra lotes de alimentos empacados, valida cantidades, calcula tasas de defectos, muestra indicadores de proceso y señala lotes atípicos mediante un modelo de Inteligencia Artificial sobre datos sintéticos (`data/lotes_ejemplo.csv`).

> **ADVERTENCIA DE USO ORIENTATIVO:** Las alertas generadas por este modelo de IA son únicamente apoyo analítico sobre datos operativos y **NO sustituyen** los controles de inocuidad alimentaria, análisis microbiológicos/fisicoquímicos de laboratorio ni las decisiones de los profesionales de aseguramiento de calidad responsables.

## Estructura del Proyecto
- `src/`: Módulos de negocio (`produccion.py`, `calidad.py`, `detector_ia.py`, `app.py`)
- `tests/`: Suite de pruebas automatizadas con `pytest` (`test_produccion.py`, `test_calidad.py`)
- `data/`: Conjunto de datos sintético con 36 lotes (`lotes_ejemplo.csv`)
- `docs/`: Documentación de requisitos, plan de calidad, plan de medición y plan de configuración

## Ejecución de Pruebas y Tablero
```bash
pip install -r requirements.txt
python -m pytest -q
python -m src.app
```
