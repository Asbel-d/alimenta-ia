import os
from src.calidad import resumen_tablero
from src.detector_ia import evaluar_anomalias_ia


def test_resumen_tablero():
    lotes = [
        {"unidades_producidas": 1000, "unidades_defectuosas": 20},
        {"unidades_producidas": 1000, "unidades_defectuosas": 10},
    ]
    res = resumen_tablero(lotes)
    assert res["total_lotes"] == 2
    assert res["tasa_global_pct"] == 1.5
    assert res["tasa_promedio_lote_pct"] == 1.5


def test_detector_ia_y_advertencia():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "lotes_ejemplo.csv")
    resultado = evaluar_anomalias_ia(csv_path)
    assert resultado["total_lotes"] == 36
    assert resultado["recall"] >= 0.80
    assert "NO sustituyen los controles de inocuidad" in resultado["advertencia"]
