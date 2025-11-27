import streamlit as st
import pandas as pd
from entsoe import EntsoePandasClient

st.title("Smart Grid Integration (SG)")

st.markdown(
    """
    This page displays the real-time energy prices from the ENTSO-E API.
    """
)

# Add a country selector
country_code = st.selectbox(
    "Select a country",
    ["DE", "FR", "ES", "IT", "GB"],
)

# Add a date range selector
start_date = st.date_input("Start date", pd.Timestamp.now(tz="Europe/Brussels").date())
end_date = st.date_input("End date", pd.Timestamp.now(tz="Europe/Brussels").date())

# Fetch the data from the ENTSO-E API
@st.cache_data
def get_energy_prices(country_code, start_date, end_date):
    client = EntsoePandasClient(api_key=st.secrets["ENTSOE_API_KEY"])
    start = pd.Timestamp(start_date, tz="Europe/Brussels")
    end = pd.Timestamp(end_date, tz="Europe/Brussels")
    prices = client.query_day_ahead_prices(country_code, start=start, end=end)
    return prices

if start_date and end_date:
    prices = get_energy_prices(country_code, start_date, end_date)
    st.line_chart(prices)
