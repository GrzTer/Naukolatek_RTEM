# Real-Time Energy Manager (RTEM) - Streamlit Edition

A Streamlit-based platform that **monitors, predicts, and optimises electric-power usage in real time**.
The project combines IoT telemetry, time-series storage, and machine-learning forecasts to help data-centre and high-load facilities cut energy costs and react instantly to anomalies.

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repository.git
cd your-repository

# 2. Create and activate a virtual environment
python -m venv env
# Windows
env\Scripts\activate
# macOS / Linux
source env/bin/activate

# 3. Install dependencies
pip install -r streamlit_app/requirements.txt

# 4. Run the Streamlit application
streamlit run streamlit_app/app.py
```

---

## Features

*   **Monitoring (MZE):** View the energy consumption of different devices over time.
*   **Prediction (PZ):** View the historical energy consumption and the model's future predictions.
*   **Smart Grid (SG):** View the real-time energy prices from the ENTSO-E API.

---

## Repository Layout
```
├── streamlit_app/
│   ├── app.py
│   ├── requirements.txt
│   ├── data/
│   │   ├── data1.csv
│   │   └── data2.csv
│   ├── model/
│   │   └── model_checkpoint.keras
│   └── pages/
│       ├── 1_Monitoring.py
│       ├── 2_Prediction.py
│       └── 3_Smart_Grid.py
└── README.md
```
