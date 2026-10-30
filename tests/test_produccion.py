import pytest
from src.produccion import tasa_defectos, validar_lote, filtrar_por_producto


def test_tasa_defectos_caso_normal():
    assert tasa_defectos(200, 6) == 3.0


def test_tasa_defectos_cero_producidas():
    with pytest.raises(ValueError, match="Cantidades inválidas"):
        tasa_defectos(0, 0)


def test_tasa_defectos_valores_negativos():
    with pytest.raises(ValueError, match="Cantidades inválidas"):
        tasa_defectos(100, -5)
    with pytest.raises(ValueError, match="Cantidades inválidas"):
        tasa_defectos(-100, 5)


def test_tasa_defectos_defectuosas_mayores_que_producidas():
    with pytest.raises(ValueError, match="Cantidades inválidas"):
        tasa_defectos(100, 101)


def test_validar_lote_y_filtro_historial():
    lote = validar_lote("LOTE-001", "2026-10-01", "Leche Entera UHT 1L", 1000, 15, 72.4)
    assert lote["tasa_defectos_pct"] == 1.5
    historial = [
        lote,
        validar_lote("LOTE-002", "2026-10-02", "Yogur Griego Natural 500g", 500, 10, 72.0),
    ]
    filtrados = filtrar_por_producto(historial, "Leche Entera UHT 1L")
    assert len(filtrados) == 1
    assert filtrados[0]["codigo_lote"] == "LOTE-001"
