import pandas as pd
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from entsoe import EntsoePandasClient
import os
from datetime import datetime
from django.conf import settings
from django.utils.timezone import now

class EnergyPricesView(View):
    def post(self, request):
        country_code = request.POST.get("country_code", "PL").upper()
        time_span = request.POST.get("time_span", "year")

        data_dir = os.path.join(settings.BASE_DIR, 'SG/data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        data_path = os.path.join(data_dir, f"energy_prices_{country_code}.csv")

        # Ensure dates are parsed when reading the DataFrame
        df = pd.read_csv(data_path, parse_dates=['date'])

        # Filter the DataFrame based on the time_span
        if time_span == 'year':
            df = df[df['date'].dt.year == now().year]
        elif time_span == 'quarter':
            current_quarter = (now().month - 1) // 3 + 1
            df = df[df['date'].dt.quarter == current_quarter]
        elif time_span == 'month':
            df = df[df['date'].dt.month == now().month]
        elif time_span == 'week':
            current_week = now().isocalendar().week
            df = df[df['date'].dt.isocalendar().week == current_week]
        elif time_span == 'day':
            df = df[df['date'].dt.date == now().date()]

        df.sort_values(by="date", inplace=True)
        chart_data = {
            "categories": [date.strftime("%Y-%m-%d") for date in df["date"]],
            "data": [{"x": date.strftime("%Y-%m-%d"), "y": price} for date, price in zip(df["date"], df["price"])]
        }

        return JsonResponse(chart_data)

def fetch_historical_data(country_code='PL', start_date=None, end_date=None):
    api_key = settings.ENTSOE_API_KEY
    client = EntsoePandasClient(api_key=api_key)

    if not start_date:
        end_date = pd.Timestamp(datetime.now(), tz="Europe/Warsaw")
        start_date = end_date - pd.DateOffset(years=1)

    try:
        prices = client.query_day_ahead_prices(country_code, start=start_date, end=end_date)
        if prices.empty:
            raise ValueError(f"No data available for {country_code} from {start_date} to {end_date}")

        df = pd.DataFrame(list(prices.items()), columns=["date", "price"])
        data_path = os.path.join(settings.BASE_DIR, 'SG/data', f"energy_prices_{country_code}.csv")
        df.to_csv(data_path, index=False)
        print(f"Data successfully saved to {data_path}")
    except ValueError as e:
        print(f"An error occurred: {str(e)}")
        raise
    except Exception as e:
        print(f"An error occurred while fetching or saving data: {str(e)}")
        raise

    return df

def show_chart(request):
    context = {}
    return render(request, "SG.html", context)
