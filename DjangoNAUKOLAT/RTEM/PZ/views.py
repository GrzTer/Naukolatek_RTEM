from django.shortcuts import render
from keras.models import load_model
import pandas as pd
import numpy as np
import os


def predict(request):
    # Load data
    df = pd.read_csv('PZ/data1.csv', parse_dates=['timestamp'])

    # Preprocess data if needed (example: normalize, reshape, etc.)
    df['energy_consumption_normalized'] = (df['energy_consumption'] - df['energy_consumption'].mean()) / df[
        'energy_consumption'].std()

    # Reshape data if your model expects a different shape (like 3D for LSTM)
    features = df[['energy_consumption_normalized']].values
    features = np.reshape(features, (features.shape[0], features.shape[1], 1))

    # Load your model
    model_path = os.path.join('PZ/model_checkpoint.keras')  # Make sure 'PZ' is the correct directory
    model = load_model(model_path)

    # Make predictions
    predictions = model.predict(features)

    # Convert predictions to a list of dictionaries with the desired structure
    forecasted_data = [{'timestamp': ts, 'predicted_energy_consumption': float(pred)}
                       for ts, pred in zip(df['timestamp'], predictions.flatten())]

    # Render the predictions in a template
    return render(request, 'PZ.html', {
        'forecasted_data': forecasted_data
    })
