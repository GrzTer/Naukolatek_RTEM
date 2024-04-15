from django.shortcuts import render
from keras.models import load_model
import pandas as pd
import numpy as np
import os


def predict(request):
    # Load data
    df = pd.read_csv('PZ/data1.csv', parse_dates=['timestamp'])

    # Preprocess timestamp if needed and select the energy_consumption
    # This assumes the model might need some datetime components like hour of the day
    df['hour'] = df['timestamp'].dt.hour  # Example: Use hour if the model needs it
    features = df[['energy_consumption', 'hour']]  # Adjust this based on your model's trained features

    # Load your model
    model = load_model('PZ/model_checkpoint.keras')  # Ensure the model path is correct

    # Make predictions
    predictions = model.predict(features)

    # Formatting the predictions to return to the template
    predictions = [float(pred) for pred in predictions.flatten()]

    # Rendering the predictions in a template
    return render(request, 'Pz.html', {'predictions': predictions})

