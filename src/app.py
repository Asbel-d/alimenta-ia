"""Punto de entrada del tablero educativo ALIMENTA-IA (RF-04, RF-05)."""
import os
import pandas as pd
from src.calidad import resumen_tablero
from src.detector_ia import evaluar_anomalias_ia


def ejecutar_tablero() -> None:
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "lotes_ejemplo.csv")
    df = pd.read_csv(csv_path)
    resumen = resumen_tablero(df.to_dict(orient="records"))
    ia = evaluar_anomalias_ia(csv_path)

    print("=== TABLERO ALIMENTA-IA (NutriAlimentos S.A.S.) ===")
    print(f"Total lotes registrados : {resumen['total_lotes']}")
    print(f"Unidades producidas     : {resumen['total_producidas']}")
    print(f"Unidades defectuosas    : {resumen['total_defectuosas']}")
    print(f"Tasa global de defectos : {resumen['tasa_global_pct']}%")
    print(f"Lotes atípicos (IA)     : {ia['alertas_detectadas']} ({ia['proporcion_alertas_pct']}%) -> {ia['lotes_marcados']}")
    print(f"Recall IA (etiquetados) : {ia['recall'] * 100:.1f}%")
    print(f"\n{ia['advertencia']}")


if __name__ == "__main__":
    ejecutar_tablero()
