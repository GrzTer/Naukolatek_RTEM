from django.shortcuts import render
from django.http import HttpResponse
from keras.models import load_model
import pandas as pd
import numpy as np
import os

def predict(request):
    df = pd.read_csv('PZ/data1.csv', parse_dates=['timestamp'])  # Update to match your CSV structure

    # Extract features from datetime
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    df['day'] = df['timestamp'].dt.day
    df['hour'] = df['timestamp'].dt.hour
    df.drop('timestamp', axis=1, inplace=True)  # Optionally drop if no longer needed

    # Load model and make predictions
    model = load_model('PZ/model_checkpoint.keras')  # Correct path
    predictions = model.predict(df.values)

    # Process predictions for display
    processed_predictions = [round(float(pred), 2) for pred in predictions.flatten()]

    return render(request, 'Pz.html', {
        'predictions': processed_predictions
    })

# Assume no form and file upload
