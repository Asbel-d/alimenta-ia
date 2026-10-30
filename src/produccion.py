"""Módulo de registro y validación de lotes de producción (RF-01, RF-02, RF-03, RNF-01)."""
from typing import List, Dict, Any


def tasa_defectos(producidas: int, defectuosas: int) -> float:
    """Calcula el porcentaje de unidades defectuosas sobre las producidas (RF-02, RNF-01)."""
    if producidas <= 0 or defectuosas < 0 or defectuosas > producidas:
        raise ValueError("Cantidades inválidas")
    return round(100.0 * defectuosas / producidas, 2)


def validar_lote(codigo_lote: str, fecha: str, producto: str, producidas: int, defectuosas: int, temperatura_c: float) -> Dict[str, Any]:
    """Valida y estructura el registro de un lote de producción (RF-01, RNF-01)."""
    if not codigo_lote or not codigo_lote.strip():
        raise ValueError("El código de lote es obligatorio")
    if not producto or not producto.strip():
        raise ValueError("El nombre del producto es obligatorio")
    porcentaje = tasa_defectos(producidas, defectuosas)
    return {
        "codigo_lote": codigo_lote.strip(),
        "fecha": fecha.strip(),
        "producto": producto.strip(),
        "unidades_producidas": int(producidas),
        "unidades_defectuosas": int(defectuosas),
        "temperatura_c": float(temperatura_c),
        "tasa_defectos_pct": porcentaje,
    }


def filtrar_por_producto(historial: List[Dict[str, Any]], producto: str) -> List[Dict[str, Any]]:
    """Filtra el historial de lotes por nombre de producto (RF-03)."""
    return [lote for lote in historial if lote.get("producto") == producto]
