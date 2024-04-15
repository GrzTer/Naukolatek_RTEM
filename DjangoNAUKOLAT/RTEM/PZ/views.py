from django.shortcuts import render
from keras.models import load_model
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import json
import os

def predict(request):
    # Load the data
    data_path = os.path.join('PZ', 'data1.csv')
    df = pd.read_csv(data_path)

    # Normalize features as your model expects for input
    scaler = MinMaxScaler(feature_range=(0, 1))
    df['energy_consumption'] = scaler.fit_transform(df[['energy_consumption']])

    # Reshape data for LSTM [samples, time steps, features]
    X_test = df['energy_consumption'].values.reshape(-1, 1, 1)

    # Load the Keras model
    model_path = os.path.join('PZ', 'model_checkpoint.keras')
    model = load_model(model_path)

    # Make predictions
    predictions_scaled = model.predict(X_test)

    # Inverse the predictions to original scale
    predictions = scaler.inverse_transform(predictions_scaled.reshape(-1, 1)).flatten().tolist()

    # Preparing data for chart.js
    # Assume you have a datetime column corresponding to each prediction.
    # Here, I'm just creating a list of the next N hours as an example.
    forecast_hours = pd.date_range(start=df['timestamp'].iloc[-1], periods=len(predictions), freq='H')
    forecast_data = [{'timestamp': str(hour), 'energy_consumption': pred} for hour, pred in zip(forecast_hours,
                                                                                                predictions)]

    # Convert data to JSON
    forecast_data_json = json.dumps(forecast_data)

    # Pass the forecast data to the template
    return render(request, 'PZ.html', {'forecast_data_json': forecast_data_json})
