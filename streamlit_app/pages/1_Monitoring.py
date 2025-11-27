import streamlit as st
import pandas as pd
import os

st.title("Energy Consumption Monitoring (MZE)")

st.markdown(
    """
    This page displays the energy consumption of different devices over time.
    """
)

# Load the data
@st.cache_data
def load_data():
    data_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "data2.csv"
    )
    data = pd.read_csv(data_path)
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    return data

data = load_data()

# Add a device selector
device_id = st.selectbox(
    "Select a device",
    data["device_id"].unique(),
)

# Filter the data for the selected device
filtered_data = data[data["device_id"] == device_id]

# Display the chart
st.line_chart(
    filtered_data,
    x="timestamp",
    y="energy_consumption",
)
