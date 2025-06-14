# model_train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# --- Load dataset ---
df = pd.read_csv("dataset/creditcard.csv")  # Make sure this path is correct
print("✅ Dataset loaded:", df.shape)

# --- Prepare data ---
X = df.drop(columns=["Class"])
y = df["Class"]

# --- Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# --- Train model ---
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
model.fit(X_train, y_train)
print("✅ Model trained")

# --- Evaluate ---
y_pred = model.predict(X_test)
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# --- Save model ---
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/fraud_model.pkl")
print("💾 Model saved to model/fraud_model.pkl")
