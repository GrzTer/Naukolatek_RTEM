# REAL TIME ENERGY MANAGER (RTEM)

## Overview

The Real-Time Energy Manager (RTEM) is a project that optimizes energy consumption in high-demand environments like server rooms. By leveraging IoT and machine learning, RTEM provides real-time monitoring, predictive analysis, and intelligent optimization of energy usage.

## Key Features

- **(MZE) Energy Consumption Monitoring**: Utilizes advanced sensors and IoT technology to track electricity consumption from individual devices to entire buildings.
- **(PZ) Consumption Forecasting**: Employs machine learning algorithms (TensorFlow) to predict future energy consumption based on historical data and current trends.
- **(OZ) Consumption Optimization**: Automatically suggests ways to optimize energy consumption, such as adjusting device operation times and utilizing renewable energy sources.
- **(PA) Notifications and Alerts**: Generates real-time notifications for device failures or abnormal energy consumption patterns.
- **(SG) Smart Grid Integration**: Integrates with smart grids to access real-time energy pricing data.

## Future Enhancements

- **AI Assistant**: A chatbot assistant to improve user experience and application efficiency.
- **Market Price Forecasting**: Expand the Smart Grid integration to predict future energy market prices.
- **Entso-e API Collaboration**: Explore collaboration with Entso-e for more robust API access, especially with a larger user base.
- **Mini-Server Brain**: Develop the system into a mini-server that acts as the central "brain" for a building's electrical network.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Other dependencies (see `requirements.txt`)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Naukolatek_RTEM.git
    ```
2.  **Create and activate a virtual environment:**
    -   **Windows:**
        ```bash
        python -m venv env
        env\Scripts\activate
        ```
    -   **Linux/macOS:**
        ```bash
        python3 -m venv env
        source env/bin/activate
        ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate --run-syncdb
    ```
5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

### Superuser Credentials

-   **Username:** `admin`
-   **Password:** `1234`

## Contribution Guidelines

1.  **Clone/Pull:** Always start with the latest version of the code.
2.  **Create a New Branch:** Create a new branch for each new issue or feature.
3.  **Database Migrations:** If you make changes to `models.py`, run the following command:
    ```bash
    python manage.py makemigrations
    ```

## Useful Links

-   [FIGMA RTEM FLOW](https://www.figma.com/file/Pkl86gwsODaW5lYygA1F1l/RTEM-FLOW?type=whiteboard&node-id=0%3A1&t=FW0Yp6fZ3LtkCLzH-1)
-   [FIGMA MOCK'UP](https://www.figma.com/file/zaxl5wU608z9J7BesLggCP/naukolatek-team-library?type=design&node-id=0%3A1&mode=design&t=PuOzFr1hWV7bI672-1)
-   [Django Cheatsheet](https://docs.google.com/document/d/1z2Mm_dkT3-zRV_uZ3sOxd9jDH--bTU4HZxVyXrb-sHo/edit?pli=1)
