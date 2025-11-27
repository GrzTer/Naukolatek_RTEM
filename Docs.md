# RTEM Documentation
---
## (MZE) Energy Consumption Monitoring:
The Energy Consumption Monitoring application is designed to use advanced IoT technology to track and analyze electricity consumption at various levels, from individual devices to entire buildings. Using Django for the backend, the system is built around key models, including `Device`, `TemperatureMeasurement`, and `VoltageMeasurement`, which together facilitate the collection, storage, and analysis of critical parameters such as frequency, resistance, voltage, and temperature.

Each device is uniquely identified by a serial number, which is automatically generated to ensure uniqueness and ease of tracking. The `TemperatureMeasurement` and `VoltageMeasurement` models are linked to specific devices, enabling precise monitoring of environmental conditions and electrical parameters over time. The measurements are time-stamped, providing a historical data trail for analyzing and optimizing energy consumption.

The application supports multiple users and buildings, making it scalable for both residential and commercial properties. It is designed with extensibility in mind, allowing for the future integration of additional types of measurements and IoT devices without significant restructuring.

This documentation is intended to guide developers and system administrators through the configuration, deployment, and daily management of the Energy Consumption Monitoring application, ensuring a robust and user-friendly experience for effective energy monitoring and reduction.
