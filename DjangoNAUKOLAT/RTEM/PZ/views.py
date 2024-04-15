import pandas as pd
from .model_loader import get_model
from django.shortcuts import render

import numpy as np
from sklearn.preprocessing import MinMaxScaler


def preprocess(data, sequence_length=720):
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data.reshape(-1, 1))  # Reshape data if it's a single series

    # Create sequences
    sequences = []
    for i in range(len(data_scaled) - sequence_length + 1):
        sequence = data_scaled[i:i + sequence_length]
        sequences.append(sequence)

    # Convert to numpy array and reshape to fit LSTM input (samples, time steps, features)
    sequences = np.array(sequences)
    return sequences, scaler


def predict(request):
    model = get_model()
    data = pd.read_csv('path/to/data1.csv')['energy_consumption']

    # Preprocess the data
    if len(data) < 720:
        return render(request, 'error.html',
                      {'error': 'Not enough data for prediction. At least 720 data points required.'})

    processed_data, scaler = preprocess(data.values, sequence_length=720)

    # Make predictions
    predictions = model.predict(processed_data)
    predictions = [float(pred) for pred in predictions.flatten()]

    return render(request, 'PZ.html', {'predictions': predictions})

