import streamlit as st

st.set_page_config(
    page_title="Real-Time Energy Manager",
    layout="wide",
)

st.title("Real-Time Energy Manager (RTEM)")

st.markdown(
    """
    A Streamlit-based platform that **monitors, predicts, and optimises electric-power usage in real time**.
    The project combines IoT telemetry, time-series storage, and machine-learning forecasts to help data-centre and high-load facilities cut energy costs and react instantly to anomalies.
    """
)
