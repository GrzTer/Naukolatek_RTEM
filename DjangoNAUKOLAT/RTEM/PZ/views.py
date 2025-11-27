from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import json
from django.views.decorators.cache import cache_page
from django.apps import apps
from django.conf import settings


@cache_page(60 * 15)
def predict(request):
    # Load the data
    df = pd.read_csv(settings.DATA_PATH)

    # Normalize features as your model expects for input
    scaler = MinMaxScaler(feature_range=(0, 1))
    df["energy_consumption"] = scaler.fit_transform(df[["energy_consumption"]])

    # Reshape data for LSTM [samples, time steps, features]
    X_test = df["energy_consumption"].values.reshape(-1, 1, 1)

    # Load the Keras model
    model = apps.get_app_config("PZ").model

    # Make predictions
    predictions_scaled = model.predict(X_test)

    # Inverse the predictions to original scale
    predictions = (
        scaler.inverse_transform(predictions_scaled.reshape(-1, 1)).flatten().tolist()
    )

    # Preparing data for chart.js
    forecast_hours = pd.date_range(
        start=df["timestamp"].iloc[-1], periods=len(predictions), freq="h"
    )
    forecast_data = [
        {"timestamp": str(hour), "energy_consumption": f"{pred:.3f}"}
        for hour, pred in zip(forecast_hours, predictions)
    ]

    # Convert data to JSON
    forecast_data_json = json.dumps(list(forecast_data), cls=DjangoJSONEncoder)

    # Pass the forecast data to the template
    return render(request, "PZ.html", {"forecast_data_json": forecast_data_json})
