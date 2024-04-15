from django.shortcuts import render
from keras.models import load_model
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os
import json


def predict(request):
    # Load data
    df = pd.read_csv(os.path.join('PZ', 'data1.csv'), parse_dates=['timestamp'])

    # Apply MinMaxScaler
    scaler = MinMaxScaler()
    df['scaled'] = scaler.fit_transform(df[['energy_consumption']])

    # Reshape for model
    features = np.reshape(df['scaled'].values, (-1, 1, 1))  # Example: Reshape for LSTM input

    # Load your model
    model = load_model(os.path.join('PZ', 'model_checkpoint.keras'))

    # Make predictions
    predictions_scaled = model.predict(features)
    predictions_scaled = np.reshape(predictions_scaled, (-1, 1))  # Reshape to 2D for inverse scaling

    # Inverse transform to get actual values
    predictions = scaler.inverse_transform(predictions_scaled)  # Invert scaling

    # Prepare data for chart
    forecast_data = [{'x': time.strftime('%Y-%m-%d %H:%M:%S'), 'y': float(pred[0])} for time, pred in
                     zip(df['timestamp'], predictions)]
    forecast_data_json = json.dumps(forecast_data)

    # Pass to template
    return render(request, 'PZ.html', {'forecast_data': forecast_data_json})
