from django.http import JsonResponse
import pandas as pd
import tensorflow as tf
from tensorflow.keras.initializers import Orthogonal
from tensorflow.python import saved_model
# Load the model

model = saved_model.load(
    "PZ/model_checkpoint.h5")


def predict(request):
    # Load data from CSV
    data = pd.read_csv("PZ/data1.csv")

    # Assuming your model expects the same columns and no preprocessing is needed:
    predictions = model.predict(data)

    # Return predictions as JSON
    return JsonResponse({"predictions": predictions.tolist()})
