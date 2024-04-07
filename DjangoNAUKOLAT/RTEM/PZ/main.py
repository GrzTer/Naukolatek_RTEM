import os
import numpy as np
import pandas as pd
import tensorflow as tf
import json
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import Callback, ReduceLROnPlateau, EarlyStopping, ModelCheckpoint

# Set seed for reproducibility
tf.random.set_seed(84)
np.random.seed(84)

time_steps = 1

# Define callbacks
class PlotLosses(Callback):
    def on_train_begin(self, logs=None):
        self.history = {'loss': [], 'val_loss': []}

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        self.history['loss'].append(logs.get('loss'))
        self.history['val_loss'].append(logs.get('val_loss'))

        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        plt.plot(self.history['loss'], label='Training loss')
        plt.plot(self.history['val_loss'], label='Validation loss')
        plt.title('Training and Validation Loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show(block=False)

# Load and preprocess data
def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    data = df['energy_consumption'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_normalized = scaler.fit_transform(data)
    return data_normalized, scaler, df

# Create sequences for LSTM
def create_sequences(data, time_steps):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:(i + time_steps)])
        y.append(data[i + time_steps])
    return np.array(X), np.array(y)

# Forecast function
def forecast(model, recent_data, scaler, time_steps):
    recent_data_scaled = scaler.transform(recent_data.reshape(-1, 1))
    X_recent = recent_data_scaled.reshape(1, time_steps, 1)
    prediction_scaled = model.predict(X_recent)
    prediction = scaler.inverse_transform(prediction_scaled)
    return prediction

# Load and preprocess historical data
data_normalized, scaler, df = load_and_preprocess_data('data.csv')
X, y = create_sequences(data_normalized, time_steps)
X = X.reshape((X.shape[0], X.shape[1], 1))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=84)

# Define LSTM model
model = Sequential([
    LSTM(100, activation='relu', return_sequences=True, input_shape=(X_train.shape[1], 1)),
    Dropout(0.3),
    LSTM(50, activation='relu'),
    Dropout(0.3),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Callbacks
reduce_lr = ReduceLROnPlateau(factor=0.1, patience=10, min_lr=0.00001, monitor='val_loss')
# early_stopping = EarlyStopping(monitor='val_loss', patience=100)
plot_losses = PlotLosses()
checkpoint_path = "model_checkpoint.h5"
checkpoint = ModelCheckpoint(checkpoint_path, monitor='val_loss', save_best_only=True, mode='min')

# Load weights if they exist
if os.path.exists(checkpoint_path):
    try:
        model.load_weights(checkpoint_path)
        print(f"Loaded weights from {checkpoint_path}")
    except Exception as e:
        print(f"Error loading weights: {e}")

# Train the model
history = model.fit(
    X_train, y_train,
    epochs=1000,
    batch_size=78336,
    validation_split=0.2,
    callbacks=[checkpoint, reduce_lr, plot_losses], # early stopping
    verbose=1
)

# # Save training history to JSON
# with open('training_history.json', 'w') as f:
#     json.dump(history.history, f, indent=4)

# Evaluate the model
test_loss = model.evaluate(X_test, y_test, verbose=1)
print(f"Test loss: {test_loss}")

# Forecast future energy consumption
recent_data = df['energy_consumption'].values[-time_steps:].reshape(-1, 1)
forecasted_consumption = forecast(model, recent_data, scaler, time_steps)

# Save forecast to JSON
forecast_result = {'Forecasted Energy Consumption': float(forecasted_consumption[0][0])}  # Convert to Python float
with open('../../../../PZ-0_1/forecast_results.json', 'w') as f:
    json.dump(forecast_result, f, indent=4)

print(f"Forecasted Energy Consumption: {forecasted_consumption[0][0]}")