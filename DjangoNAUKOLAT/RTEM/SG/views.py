import pandas as pd
from django.http import JsonResponse
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import render
from entsoe import EntsoePandasClient
import os
from datetime import datetime
from django.conf import settings


class EnergyPricesView(View):
    def post(self, request):
        country_code = request.POST.get("country_code", "PL").upper()
        year = request.POST.get("year")
        month = request.POST.get("month")

        fetch_historical_data(country_code=country_code)

        data_dir = os.path.join(settings.BASE_DIR, 'SG')
        data_path = os.path.join(data_dir, f"energy_prices_{country_code}.csv")

        try:
            df = pd.read_csv(data_path)
            df["date"] = pd.to_datetime(df["date"], utc=True)

            if year:
                df = df[df["date"].dt.year == int(year)]
            if month:
                df = df[df["date"].dt.month == int(month)]

            df.sort_values(by="date", inplace=True)

            paginator = Paginator(df, 100)
            page_obj = paginator.get_page(request.POST.get("page", 1))

            chart_data = {
                "categories": [date.strftime("%Y-%m-%d") for date in page_obj.object_list["date"]],
                "data": [{"x": date.strftime("%Y-%m-%d"), "y": price} for date, price in
                         zip(page_obj.object_list["date"], page_obj.object_list["price"])]
            }

            return JsonResponse(chart_data)
        except FileNotFoundError:
            return JsonResponse({'error': 'Data file not found. Please try fetching data again.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def fetch_historical_data(country_code='PL', start_date=None, end_date=None):
    api_key = settings.ENTSOE_API_KEY
    client = EntsoePandasClient(api_key=api_key)
    data_dir = os.path.join(settings.BASE_DIR, 'SG')

    if not start_date:
        end_date = pd.Timestamp(datetime.now(), tz="Europe/Warsaw")
        start_date = end_date - pd.DateOffset(years=1)

    try:
        prices = client.query_day_ahead_prices(country_code, start=start_date, end=end_date)
        if prices.empty:
            raise ValueError(f"No data available for {country_code} from {start_date} to {end_date}")

        df = pd.DataFrame(list(prices.items()), columns=["date", "price"])

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        data_path = os.path.join(data_dir, f"energy_prices_{country_code}.csv")
        df.to_csv(data_path, index=False)
        print(f"Data successfully saved to {data_path}")
    except ValueError as e:
        print(f"An error occurred: {str(e)}")
        raise
    except Exception as e:
        print(f"An error occurred while fetching or saving data: {str(e)}")
        raise


def show_chart(request):
    context = {}
    return render(request, "SG.html", context)
