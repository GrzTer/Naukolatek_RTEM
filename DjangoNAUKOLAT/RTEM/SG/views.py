from django.shortcuts import render
from entsoe import EntsoePandasClient
import pandas as pd


def energy_data_view(request):
    api_key = "d9f78120-2bb1-4182-b3d2-a88195b24ad5"
    client = EntsoePandasClient(api_key=api_key)

    if request.method == "POST":
        country_code = request.POST.get("country_code", "PL")
        start_date = pd.Timestamp(
            request.POST.get("start_date", "2024-03-01"), tz="Europe/Warsaw"
        )
        end_date = pd.Timestamp(
            request.POST.get("end_date", "2024-04-01"), tz="Europe/Warsaw"
        )

        # Example: Query day-ahead prices
        prices = client.query_day_ahead_prices(
            country_code, start=start_date, end=end_date
        )
        prices_chart = prices.to_json()

        return render(request, "SG.html", {"prices_chart": prices_chart})

    return render(request, "SG.html")
