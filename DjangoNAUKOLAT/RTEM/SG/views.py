from django.shortcuts import render
from entsoe import EntsoePandasClient
import pandas as pd
import json
from entsoe.exceptions import NoMatchingDataError

def energy_data_view(request):
    api_key = "d9f78120-2bb1-4182-b3d2-a88195b24ad5"
    client = EntsoePandasClient(api_key=api_key)

    if request.method == "POST":
        country_code = request.POST.get("country_code", "PL")
        start_date = pd.Timestamp(request.POST.get("start_date", "2024-03-01"), tz="Europe/Warsaw")
        end_date = pd.Timestamp(request.POST.get("end_date", "2024-04-01"), tz="Europe/Warsaw")

        try:
            prices = client.query_day_ahead_prices(country_code, start=start_date, end=end_date)
            prices_data = [{'date': str(index.strftime('%Y-%m-%d')), 'price': value} for index, value in prices.items()]
            dates = [date.strftime('%Y-%m-%d') for date in prices.index]
            prices_chart = json.dumps(prices_data)
            dates_json = json.dumps(dates)
            context = {'prices_chart': prices_chart, 'dates': dates_json}
        except NoMatchingDataError:
            context = {"error": "No matching data available for the selected range."}
            return render(request, "SG.html", context)
        except Exception as e:
            context = {"error": f"An error occurred: {str(e)}"}
            return render(request, "SG.html", context)

        return render(request, "SG.html", context)

    return render(request, "SG.html")
