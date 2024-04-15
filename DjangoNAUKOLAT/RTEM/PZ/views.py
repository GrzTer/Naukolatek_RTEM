import pandas as pd
import numpy as np
from django.http import JsonResponse
from .model_loader import get_model
from sklearn.preprocessing import MinMaxScaler

# Load the model
model = get_model()


def preprocess(data, scaler):
    """ Normalizes data using MinMaxScaler and reshapes it for LSTM model input. """
    data_normalized = scaler.transform(data.reshape(-1, 1))
    time_steps = 1  # Update this based on your model's input shape
    sequences = np.array([data_normalized[i:(i + time_steps)] for i in range(len(data_normalized) - time_steps)])
    return sequences.reshape((sequences.shape[0], sequences.shape[1], 1))


def predict(request):
    """ Endpoint for predicting energy consumption from CSV data. """
    try:
        # Load and preprocess data
        df = pd.read_csv('PZ/data1.csv')
        data = df['energy_consumption'].values
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit(data.reshape(-1, 1))  # Fit scaler to data

        processed_data = preprocess(data, scaler)

        # Make prediction
        predictions = model.predict(processed_data)
        predictions = predictions.flatten().tolist()  # Convert predictions to a list for JSON response

        return JsonResponse({'predictions': predictions}, safe=False)

    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

