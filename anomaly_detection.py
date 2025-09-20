import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest

# Step 1: Load data from DB
conn = sqlite3.connect("logs.db")
df = pd.read_sql("SELECT * FROM logs", conn)
conn.close()

# Step 2: Convert size to numeric
df["size"] = pd.to_numeric(df["size"], errors="coerce")

# Step 3: Simple feature -> request size
X = df[["size"]].fillna(0)

# Step 4: Train Isolation Forest (anomaly detection)
model = IsolationForest(contamination=0.1, random_state=42)
df["anomaly"] = model.fit_predict(X)

# Step 5: Show anomalies
anomalies = df[df["anomaly"] == -1]
print("🚨 Detected anomalies:")
print(anomalies.head())
