from django.shortcuts import render
from keras.models import load_model
import pandas as pd
import numpy as np
from datetime import timedelta


def predict(request):
    # Define the time range you want to predict: 1 day, 1 week, 1 month
    time_ranges = {
        'next_day': 24,
        'next_week': 24 * 7,
        'next_month': 24 * 30
    }

    # Get the time range from request, default is next_day
    time_range = request.GET.get('time_range', 'next_day')
    hours_to_predict = time_ranges.get(time_range, 24)

    # Generate future timestamps from now
    last_timestamp = pd.Timestamp.now()
    future_timestamps = [last_timestamp + timedelta(hours=i) for i in range(1, hours_to_predict + 1)]

    # Assuming you have a model that can handle such predictions, you might need to
    # create the input features for these future times.
    # Since we don't have real future data, we would need to make assumptions or use
    # historical patterns as input for the future. For simplicity, we'll use an array of zeros.
    features = np.zeros((hours_to_predict, 1))  # This should match the input shape expected by your model

    # Load your model
    model_path = 'PZ/model_checkpoint.keras'  # Update the path to your model
    model = load_model(model_path)

    # Make predictions
    predictions = model.predict(features)

    # Prepare the predictions for display
    forecasted_data = [{'timestamp': ts.strftime('%Y-%m-%d %H:%M:%S'), 'predicted_energy_consumption': float(pred)}
                       for ts, pred in zip(future_timestamps, predictions.flatten())]

    # Render the predictions in a template
    return render(request, 'PZ.html', {
        'forecasted_data': forecasted_data,
        'selected_time_range': time_range
    })
