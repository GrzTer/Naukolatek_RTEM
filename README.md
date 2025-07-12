# Real-Time Energy Manager (RTEM)

**Branch to use:** `1_1`

A Django-based platform that **monitors, predicts, and optimises electric-power usage in real time**.  
The project combines IoT telemetry, time-series storage, and machine-learning forecasts to help data-centre and high-load facilities cut energy costs and react instantly to anomalies. 0  

---

## Key Capabilities

| Code-name | Description |
|-----------|-------------|
| **MZE – Monitoring** | Collect granular voltage, current, temperature, and frequency data from every device or circuit in a building. 1 |
| **PZ – Prediction** | Use TensorFlow/Keras models to forecast future consumption trends from historical time-series. 2 |
| **OZ – Optimisation** | Recommend load-shifting or equipment-schedule changes to flatten peaks and reduce bills. 3 |
| **PA – Alerts** | Real-time notifications when sensors report abnormal patterns or hardware faults. 4 |
| **SG – Smart-Grid Integration** | Optional link to live tariff feeds so decisions factor in dynamic energy prices. 5 |

---

## Tech Stack

* **Django 4 + Django Channels** – core web framework & WebSocket streaming 6  
* **PostgreSQL + TimescaleDB** – time-series storage backend 7  
* **Django REST Framework** – public API 8  
* **Celery & Django Background Tasks** – asynchronous data ingestion and ML jobs 9  
* **TensorFlow / Keras** – consumption forecasting models 10  
* **WebSockets** – live dashboards and alerts 11  

---

## Data Model (core app)

| Model | Fields (excerpt) | Purpose |
|-------|------------------|---------|
| `Device` | `serial_number` (auto), `building`, `location` | Uniquely identifies each monitored asset. 12 |
| `TemperatureMeasurement` | `device` (FK), `value`, `timestamp` | Tracks thermal conditions per device. 13 |
| `VoltageMeasurement` | `device` (FK), `voltage`, `current`, `timestamp` | Logs electrical parameters for analytics. 14 |

The schema is designed for easy extension when new IoT sensor types are introduced. 15  

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
pip install -r requirements.txt     # Django, DRF, Celery, etc. 16

# 4. Initialise the database
python manage.py migrate --run-syncdb   17

# 5. (Optional) create an admin account
python manage.py createsuperuser

# 6. Launch the development server
python manage.py runserver            18
```
> Default demo credentials
Username: admin  Password: 1234 




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
* **Task Queue** – Launch workers with `celery -A project_name worker -l info` to process background jobs.  
* **Lint & Tests** – A pre-commit hook is recommended (black, flake8, pytest).  

---

## Project Roadmap

- [ ] **Live tariff API** integration (ENTSO-E) for real-time price signals.  
- [ ] **Chat-bot assistant** to surface optimisation suggestions in natural language.  
- [ ] **Multi-building dashboards** with role-based access controls.  
- [ ] **Containerised deployment** (Docker & Compose).  

---

## Repository Layout
```
DjangoNAUKOLAT/
├── manage.py
├── project_name/          # Django settings, ASGI, Celery config
├── monitoring/            # Device & measurement apps
│   ├── models.py
│   ├── api/               # DRF viewsets & serializers
│   ├── tasks.py           # Celery jobs
│   └── consumers.py       # Django Channels WebSocket handlers
└── templates/ & static/   # Dashboard UI
```
---

## Design Resources

* **User flow** – Figma prototype “RTEM FLOW”  
* **UI mock-ups** – High-fidelity dashboard sketches in Figma.  
* **Cheat-sheet** – Google Doc with common Django commands.  

---

## Contributing

Pull requests are welcome!  
Please open an issue first to discuss substantial changes and follow the branching and migration guidelines above.  

---

## License

No license file is present. Unless one is added, **all rights are reserved by the author**.  
Contact the repository owner before re-using the code.