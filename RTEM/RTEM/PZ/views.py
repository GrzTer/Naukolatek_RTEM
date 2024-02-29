from django.http import JsonResponse
from tensorflow.keras.models import load_model
import numpy as np


def predict_consumption(request):
    model = load_model('forecasting_model.h5')
    # Example of how you might preprocess request data for prediction
    data = np.array([[request.GET.get('data', '')]])
    prediction = model.predict(data)
    return JsonResponse({'prediction': prediction.tolist()})
