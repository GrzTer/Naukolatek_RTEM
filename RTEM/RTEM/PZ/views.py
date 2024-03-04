from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .utils import load_and_preprocess_data, create_sequences, forecast
from tensorflow.keras.models import load_model

# Assuming your trained model is saved under 'my_app/model/my_model.h5'
MODEL_PATH = 'my_app/model/my_model.h5'
model = load_model(MODEL_PATH)
scaler = None  # This will be set when loading data

                                                                    ###### DO EDYCJI
@csrf_exempt
def upload_and_forecast(request):
    if request.method == 'POST':
        # Example assumes a file is uploaded via POST request with the name 'file'
        file = request.FILES.get('file')
        if not file:
            return JsonResponse({'error': 'No file uploaded.'}, status=400)

        # Convert uploaded file to pandas DataFrame
        df = pd.read_csv(file)
        global scaler
        data_normalized, scaler, _ = load_and_preprocess_data(df)
        X, _ = create_sequences(data_normalized)

        # Using the last sequence from uploaded data for prediction
        recent_data = X[-1].reshape(1, X.shape[1], 1)
        prediction = forecast(model, recent_data, scaler)

        # Returning the forecasted value
        return JsonResponse({'forecasted_energy_consumption': prediction.tolist()})
    else:
        return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)


def load_and_preprocess_data(df):
    data = df['energy_consumption'].values.reshape(-1, 1)
    global scaler
    if scaler is None:
        scaler = MinMaxScaler(feature_range=(0, 1))
        data_normalized = scaler.fit_transform(data)
    else:
        data_normalized = scaler.transform(data)
    return data_normalized, scaler, df
