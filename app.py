import sqlite3
import pandas as pd
import streamlit as st

st.title("🌐 Cloud Network Log Analyzer with Anomaly Detection")

# Step 1: Load data from DB
conn = sqlite3.connect("logs.db")
df = pd.read_sql("SELECT * FROM logs", conn)
conn.close()

# Step 2: Show raw data
st.subheader("📊 Raw Logs")
st.dataframe(df.head(20))

# Step 3: Simple anomaly detection (size threshold)
df["size"] = pd.to_numeric(df["size"], errors="coerce")
threshold = df["size"].mean() + 2 * df["size"].std()
df["anomaly"] = df["size"] > threshold

st.subheader("🚨 Detected Anomalies")
st.dataframe(df[df["anomaly"] == True])

# Step 4: Charts
st.subheader("📈 Log Size Distribution")
st.bar_chart(df["size"])
