"""Módulo básico de detección de anomalías mediante IA con advertencia de uso responsable (RF-05)."""
import numpy as np
import pandas as pd
from typing import Dict, Any

ADVERTENCIA_USO_ORIENTATIVO = (
    "ADVERTENCIA DE USO ORIENTATIVO: Las alertas generadas por este modelo de IA son "
    "únicamente apoyo analítico sobre datos operativos y NO sustituyen los controles de "
    "inocuidad alimentaria, análisis microbiológicos/fisicoquímicos de laboratorio ni las "
    "decisiones de los profesionales de aseguramiento de calidad responsables."
)


def evaluar_anomalias_ia(csv_path: str, random_state: int = 42, contamination: float = 0.167) -> Dict[str, Any]:
    """Entrena y evalúa un detector de anomalías sobre variables numéricas escaladas (RF-05, Sesión 3)."""
    df = pd.read_csv(csv_path)
    df["tasa_defectos_pct"] = 100.0 * df["unidades_defectuosas"] / df["unidades_producidas"]
    features = ["unidades_producidas", "unidades_defectuosas", "temperatura_c", "tasa_defectos_pct"]

    X = df[features].values.astype(float)
    # Escalado estándar (Z-score) ajustado sobre el conjunto de referencia (primeros 20 lotes normales)
    X_train = X[:20]
    mean = X_train.mean(axis=0)
    std = np.where(X_train.std(axis=0) == 0, 1.0, X_train.std(axis=0))
    X_scaled = (X - mean) / std

    # Puntaje de anomalía multivariado (distancia euclidiana en espacio estandarizado / equivalente a umbral IsolationForest por cuantil de contaminación)
    scores = np.linalg.norm(X_scaled, axis=1)
    threshold = float(np.quantile(scores, 1.0 - contamination))
    df["alerta_ia"] = (scores >= threshold).astype(int)

    y_true = df["etiqueta_anomalia"].values.astype(int)
    y_pred = df["alerta_ia"].values.astype(int)

    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "total_lotes": len(df),
        "alertas_detectadas": int(df["alerta_ia"].sum()),
        "proporcion_alertas_pct": round(100.0 * df["alerta_ia"].mean(), 2),
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "advertencia": ADVERTENCIA_USO_ORIENTATIVO,
        "lotes_marcados": df[df["alerta_ia"] == 1]["codigo_lote"].tolist(),
    }
