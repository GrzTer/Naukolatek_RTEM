# Real-Time Energy Manager (RTEM)

A Django-based platform that **monitors, predicts, and optimises electric-power usage in real time**.
The project combines IoT telemetry, time-series storage, and machine-learning forecasts to help data-centre and high-load facilities cut energy costs and react instantly to anomalies.

---

## Key Capabilities

| Code-name | Description |
|-----------|-------------|
| **MZE – Monitoring** | Collect granular voltage, current, temperature, and frequency data from every device or circuit in a building. |
| **PZ – Prediction** | Use TensorFlow/Keras models to forecast future consumption trends from historical time-series. |
| **OZ – Optimisation** | Recommend load-shifting or equipment-schedule changes to flatten peaks and reduce bills. |
| **PA – Alerts** | Real-time notifications when sensors report abnormal patterns or hardware faults. |
| **SG – Smart-Grid Integration** | Optional link to live tariff feeds so decisions factor in dynamic energy prices. |

---

## Tech Stack

* **Django 4** – core web framework.
* **Django REST Framework** – public API.
* **TensorFlow / Keras** – consumption forecasting models.

---

## Data Model (core app)

| Model | Fields (excerpt) | Purpose |
|-------|------------------|---------|
| `EnergyConsumption` | `device_id`, `timestamp`, `energy_consumption` | Uniquely identifies each monitored asset. |

---

## Quick Start

```bash
# 1. Clone the repository and switch to the Django project
git clone https://github.com/GrzTer/Naukolatek_RTEM.git
cd Naukolatek_RTEM/DjangoNAUKOLAT

# 2. Create and activate a virtual environment
python -m venv env
# Windows
env\Scripts\activate
# macOS / Linux
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialise the database
python RTEM/run_migrations.py

# 5. (Optional) create an admin account
python RTEM/create_superuser.py

# 6. Launch the development server
python RTEM/manage.py runserver
```
> Default demo credentials
Username: admin  Password: admin

---

## Usage Highlights

1. **Add Devices** – Log in to `/admin/` and register each rack, UPS, or circuit breaker.
2. **Stream Telemetry** – Connect edge IoT modules to the REST endpoint or WebSocket gateway.
3. **Visualise** – Dashboards update live with power draw and temperature readings.
4. **Receive Alerts** – E-mail, SMS, or in-app pop-ups trigger on thresholds or ML anomaly scores.
5. **Review Insights** – Drill into historical charts or export CSV for further analysis.

---

## Development Workflow

* **Branching** – Start every feature on a separate branch; never commit directly to `main`.
* **Migrations** – After editing `models.py`, run `python manage.py makemigrations` and commit the migration files.
* **Lint & Tests** – A pre-commit hook is recommended (black, flake8, pytest).

---

## Repository Layout
```
DjangoNAUKOLAT/
├── RTEM/
│   ├── manage.py
│   ├── RTEM/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── MZE/
│   │   ├── models.py
│   │   └── views.py
│   ├── PZ/
│   │   ├── models.py
│   │   └── views.py
│   ├── run_migrations.py
│   └── create_superuser.py
├── requirements.txt
└── .gitignore
```
---

## Contributing

Pull requests are welcome!

Please open an issue first to discuss substantial changes and follow the branching and migration guidelines above.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
