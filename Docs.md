# RTEM Documentation
---
## (MZE) Energy Consumption Monitoring:
The Energy Consumption Monitoring application is designed to use advanced IoT technology to track and analyze electricity consumption at various levels, from individual devices to entire buildings. Using Django for the backend, the system is built around key models, including `Device`, `TemperatureMeasurement`, and `VoltageMeasurement`, which together facilitate the collection, storage, and analysis of critical parameters such as frequency, resistance, voltage, and temperature.

Each device is uniquely identified by a serial number, which is automatically generated to ensure uniqueness and ease of tracking. The `TemperatureMeasurement` and `VoltageMeasurement` models are linked to specific devices, allowing for precise monitoring of environmental conditions and electrical parameters over time. The measurements are time-stamped, providing a historical data trail for analyzing and optimizing energy consumption.

The application supports multiple users and buildings, making it scalable for both residential and commercial properties. It has been designed with extensibility in mind, allowing for the future integration of additional measurement types and IoT devices without significant restructuring.

This documentation is intended to guide developers and system administrators through the configuration, deployment, and daily management of the 'Energy Consumption Monitoring' application, ensuring a robust and user-friendly experience for effective energy monitoring and reduction.

## (PZ) Energy Consumption Prediction:
The Energy Consumption Prediction application uses a machine learning model to forecast future energy consumption. It uses a pre-trained Keras model to predict the energy consumption for the next 24 hours. The model is loaded and used to make predictions, which are then displayed on a chart.

## (SG) Smart Grid Integration:
The Smart Grid Integration application is designed to connect to the ENTSO-E API to fetch real-time energy data. This data can be used to make more informed decisions about energy consumption and to optimize energy usage based on real-time market data.
