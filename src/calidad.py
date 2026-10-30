"""Módulo de cálculo de indicadores y resumen de tablero (RF-02, RF-04)."""
from typing import List, Dict, Any
from src.produccion import tasa_defectos


def resumen_tablero(lotes: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Genera indicadores consolidados del tablero de lotes (RF-04)."""
    if not lotes:
        return {"total_lotes": 0, "total_producidas": 0, "total_defectuosas": 0, "tasa_global_pct": 0.0, "tasa_promedio_lote_pct": 0.0}
    total_lotes = len(lotes)
    total_prod = sum(int(l["unidades_producidas"]) for l in lotes)
    total_def = sum(int(l["unidades_defectuosas"]) for l in lotes)
    tasas = [tasa_defectos(int(l["unidades_producidas"]), int(l["unidades_defectuosas"])) for l in lotes]
    return {
        "total_lotes": total_lotes,
        "total_producidas": total_prod,
        "total_defectuosas": total_def,
        "tasa_global_pct": tasa_defectos(total_prod, total_def),
        "tasa_promedio_lote_pct": round(sum(tasas) / total_lotes, 2),
    }
