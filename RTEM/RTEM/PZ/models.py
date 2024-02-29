# pz/models.py
from django.db import models
from ..MZE.models import Device
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM


def create_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model


def train_and_save_model(X_train, y_train, X_val, y_val, model_path='forecasting_model.h5'):
    model = create_model((X_train.shape[1], X_train.shape[2]))
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50, batch_size=72)
    model.save(model_path)


class ForecastData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    predicted_usage = models.FloatField()  # Prognozowane zużycie energii w kWh
    confidence_interval = models.FloatField()  # Interval ufności prognozy

    def __str__(self):
        return f"{self.device.serial_number} - {self.timestamp} - {self.predicted_usage}"
