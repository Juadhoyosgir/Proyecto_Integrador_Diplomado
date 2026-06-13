"""
Script de entrenamiento reproducible del modelo final (Regresión Logística).
Entrena, evalúa sobre el conjunto de prueba y guarda el modelo serializado y sus métricas.
Ejecutar desde la raíz del proyecto:  python src/ml/entrenar_modelo.py
"""
import json
from pathlib import Path
from datetime import date

import joblib
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

# --- Rutas (relativas a la raíz del proyecto) ---
BASE = Path(__file__).resolve().parents[2]        # sube de src/ml/ a la raíz
DATA = BASE / "data" / "processed" / "dataset_limpio.csv"
MODELS = BASE / "models"
MODELS.mkdir(exist_ok=True)

# --- Cargar datos ---
df = pd.read_csv(DATA)
features = ["estu_genero", "fami_estratovivienda", "fami_tieneinternet",
            "fami_educacionmadre", "fami_educacionpadre"]
X = df[features]
y = df["desempeno_global"]

# --- Separar train/test (misma semilla que en el notebook) ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# --- Entrenar el modelo final ---
modelo = Pipeline([
    ("prep", OneHotEncoder(handle_unknown="ignore")),
    ("modelo", LogisticRegression(max_iter=1000, random_state=42))
])
modelo.fit(X_train, y_train)

# --- Evaluar sobre el conjunto de prueba ---
pred = modelo.predict(X_test)
f1 = f1_score(y_test, pred, average="macro", zero_division=0)
acc = accuracy_score(y_test, pred)
prec = precision_score(y_test, pred, average="macro", zero_division=0)
rec = recall_score(y_test, pred, average="macro", zero_division=0)
print(f"F1-macro: {f1:.3f} | Accuracy: {acc:.3f} | Precision: {prec:.3f} | Recall: {rec:.3f}")

# --- Serializar el modelo ---
ruta_modelo = MODELS / "modelo_final.pkl"
joblib.dump(modelo, ruta_modelo)

# --- Verificar que carga correctamente ---
cargado = joblib.load(ruta_modelo)
print("Modelo cargado correctamente:", type(cargado))

# --- Guardar metadatos ---
metadata = {
    "modelo": "LogisticRegression",
    "version": "1.0",
    "fecha_entrenamiento": str(date.today()),
    "metrica_principal": "f1_score_macro",
    "valor_metrica": round(f1, 3),
    "accuracy": round(acc, 3),
    "precision_macro": round(prec, 3),
    "recall_macro": round(rec, 3),
    "variables_entrada": features,
    "variable_objetivo": "desempeno_global",
    "observaciones": f"Entrenado con scikit-learn {sklearn.__version__}, semilla 42."
}
with open(MODELS / "model_metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2, ensure_ascii=False)

print("Modelo guardado en:", ruta_modelo)
print("Metadatos guardados en:", MODELS / "model_metadata.json")