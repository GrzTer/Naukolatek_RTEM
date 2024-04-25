from entsoe import EntsoePandasClient
import pandas as pd
import os
from datetime import datetime
from django.conf import settings  # This line imports the Django settings


def fetch_historical_data():
    api_key = settings.ENTSOE_API_KEY  # Changed from hardcoded to settings variable
    client = EntsoePandasClient(api_key=api_key)
    end_date = pd.Timestamp(datetime.now(), tz="Europe/Warsaw")
    start_date = end_date - pd.DateOffset(years=1)

    try:
        prices = client.query_day_ahead_prices(
            "PL", start=start_date, end=end_date
        )  # Example with Poland 'PL'
        df = pd.DataFrame(list(prices.items()), columns=["date", "price"])

        # Save to CSV
        data_dir = "../SG"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        data_path = os.path.join(data_dir, "energy_prices.csv")
        df.to_csv(data_path, index=False)
        print(f"Data successfully saved to {data_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    fetch_historical_data()
