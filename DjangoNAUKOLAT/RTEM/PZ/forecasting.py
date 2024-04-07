# energyforecast/forecasting.py
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model


# Load and preprocess data
def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    data = df['energy_consumption'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_normalized = scaler.fit_transform(data)
    return data_normalized, scaler, df


# Create sequences for LSTM
def create_sequences(data, time_steps=1):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:(i + time_steps), 0])
        y.append(data[i + time_steps, 0])
    return np.array(X), np.array(y)


# Forecast future energy consumption
def forecast_energy_consumption(model_path, data_path, time_steps=1):
    data_normalized, scaler, df = load_and_preprocess_data(data_path)

    # Prepare the latest data for forecasting
    recent_data_normalized = data_normalized[-time_steps:]
    X_recent = np.array([recent_data_normalized])
    X_recent = np.reshape(X_recent, (X_recent.shape[0], X_recent.shape[1], 1))

    # Load the pre-trained model
    model = load_model(model_path)

    # Predict using the model
    predicted_normalized = model.predict(X_recent)
    predicted = scaler.inverse_transform(predicted_normalized)

    return predicted.flatten()[0]


# Assuming model and data paths are set relative to the manage.py file
MODEL_PATH = 'energyforecast/model_checkpoint.h5'
DATA_PATH = 'energyforecast/data1.csv'


def run_forecast():
    forecasted_value = forecast_energy_consumption(MODEL_PATH, DATA_PATH)
    return forecasted_value
