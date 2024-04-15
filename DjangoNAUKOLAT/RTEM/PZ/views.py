import numpy as np
from django.shortcuts import render
from keras.models import load_model
import pandas as pd
import json


def predict(request):
    # Load and preprocess data
    df = pd.read_csv('PZ/data1.csv', parse_dates=['timestamp'])
    df['energy_consumption'] = (df['energy_consumption'] - df['energy_consumption'].min()) / (
                df['energy_consumption'].max() - df['energy_consumption'].min())

    # Assuming you reshape data if your model needs it
    features = df['energy_consumption'].values.reshape(-1, 1)

    # Load your model
    model = load_model('PZ/model_checkpoint.keras')

    # Predict
    predictions = model.predict(features)

    # Convert predictions to native Python types for JSON serialization
    predictions = predictions.flatten().tolist()

    # Prepare data for charting
    forecast_data = [{'x': time.strftime('%Y-%m-%d %H:%M:%S'), 'y': pred} for time, pred in
                     zip(df['timestamp'], predictions)]

    # Convert to JSON
    forecast_data_json = json.dumps(forecast_data)

    # Pass data to template
    return render(request, 'PZ.html', {'forecast_data': forecast_data_json})

