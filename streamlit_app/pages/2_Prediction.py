import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os

st.title("Energy Consumption Prediction (PZ)")

st.markdown(
    """
    This page displays the historical energy consumption and the model's future predictions.
    """
)

# Load the data
@st.cache_data
def load_data():
    data_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "data1.csv"
    )
    data = pd.read_csv(data_path)
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    return data

data = load_data()

# Load the model
@st.cache_resource
def load_keras_model():
    model_path = os.path.join(
        os.path.dirname(__file__), "..", "model", "model_checkpoint.keras"
    )
    model = load_model(model_path)
    return model

model = load_keras_model()

# Prepare the data for prediction
scaler = MinMaxScaler(feature_range=(0, 1))
data["energy_consumption_scaled"] = scaler.fit_transform(
    data[["energy_consumption"]]
)
X = data["energy_consumption_scaled"].values.reshape(-1, 1, 1)

# Make predictions
predictions_scaled = model.predict(X)
predictions = scaler.inverse_transform(predictions_scaled.reshape(-1, 1)).flatten()

# Create a dataframe with the predictions
last_timestamp = data["timestamp"].iloc[-1]
prediction_timestamps = pd.to_datetime(
    [last_timestamp + pd.DateOffset(hours=i) for i in range(1, len(predictions) + 1)]
)
prediction_df = pd.DataFrame(
    {"timestamp": prediction_timestamps, "energy_consumption": predictions}
)

# Display the chart
st.line_chart(
    pd.concat([data, prediction_df]),
    x="timestamp",
    y="energy_consumption",
)
