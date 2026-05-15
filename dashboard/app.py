import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import requests
import time

# config

FASTAPI_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Anomaly Detection Dashboard",layout="wide")

st.title("Real-Time Anomaly Detection Dashboard")

# Auto Refresh

refresh_rate = st.sidebar.slider(
    "Refresh Rate (seconds)",
    1,
    10,
    2
)

# Fetch Metrics

try:
    metrics_response = requests.get(f"{FASTAPI_URL}/metrics")
    metrics = metrics_response.json()

    detector_name = metrics["detector"]
    mean = metrics["mean"]
    std_dev = metrics["std_dev"]
    recent_data = metrics["recent_data"]

except Exception as e:
    st.error(f"Could not connect to FastAPI server.\n{e}")
    st.stop()

# Metrics section

st.subheader("Detector Metrics")
col1,col2,col3 = st.columns(3)
col1.metric("Detector", detector_name)
col2.metric("Mean", f"{mean:.2f}")
col3.metric("Std Dev", f"{std_dev:.2f}")

# Live Data graph
st.subheader("Live Incoming Data")

if recent_data:
    chart_data = pd.DataFrame({
        "values" : recent_data
    })

    st.line_chart(chart_data)

else:
    st.info("No data available yet.")

# Alerts section
st.subheader("Recent Alerts")

try:
    alerts_response = requests.get(f"{FASTAPI_URL}/alerts/db")
    alerts_data = alerts_response.json()

    if alerts_data:
        alerts_df = pd.DataFrame(alerts_data)
        alerts_df = alerts_df.sort_values(
            by="timestamp",
            ascending=False
        )
        st.dataframe(
            alerts_df,
            use_container_width=True
        )
    
    else:
        st.info("No alerts detected yet.")

except Exception as e:
    st.error(f"Could not fetch alerts.\n{e}")

# Auto refresh
st_autorefresh(interval=refresh_rate * 1000, key="refresh")

