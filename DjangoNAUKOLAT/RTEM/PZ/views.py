from django.shortcuts import render
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.src.saving.saving_lib import load_model
from sklearn.preprocessing import MinMaxScaler


def forecast_energy(request):
    # Assuming 'data.csv' is in the same directory as your manage.py
    dataset_path = "PZ/data1.csv"
    data = pd.read_csv(dataset_path)

    # Preprocess your data according to the requirements of your model
    # The preprocessing steps might include normalization, setting the sequence length, etc.
    # For demonstration, let's assume we're scaling the 'energy_consumption' column
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data[["energy_consumption"]].values)

    # Reshape data for LSTM model (assuming this structure based on typical usage)
    # This is highly dependent on how your model was trained
    sequence_length = 50
    x_test = []
    for i in range(sequence_length, len(scaled_data)):
        x_test.append(scaled_data[i - sequence_length : i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    # Load the trained model
    model_path = "PZ/model_checkpoint.h5"
    model = load_model(model_path)

    # Make predictions
    predictions = model.predict(x_test)

    # Inverting the MinMax scale to get actual values
    predictions = scaler.inverse_transform(predictions)

    # Convert predictions to list for rendering in template
    predictions_list = predictions.flatten().tolist()

    # Render a template with the predictions data
    context = {
        "predictions": predictions_list,
    }
    return render(request, "PZ.html", context)
