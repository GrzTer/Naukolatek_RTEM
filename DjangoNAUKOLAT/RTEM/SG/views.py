import os
from datetime import datetime
from datetime import timedelta

import pandas as pd
import pytz
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import make_aware, get_default_timezone
from django.views import View
from entsoe import EntsoePandasClient
from pandas import DateOffset


class EnergyPricesView(View):
    def post(self, request):
        country_code = request.POST.get("country_code", "PL").upper()
        date_selected = request.POST.get('date')
        week_selected = request.POST.get('week')
        month_selected = request.POST.get('month')

        data_path = os.path.join(settings.BASE_DIR, f'SG/data/energy_prices_{country_code}.csv')
        df = self.load_or_fetch_data(data_path, country_code)

        if df.empty:
            return JsonResponse({"error": "No data available"}, status=404)

        if date_selected:
            df = self.filter_by_day(df, date_selected)
        elif week_selected:
            df = self.filter_by_week(df, week_selected)
        elif month_selected:
            df = self.filter_by_month(df, month_selected)
        else:
            df = df.resample('D', on='date').agg({'price': 'mean'}).reset_index()

        df.sort_values(by="date", inplace=True)
        chart_data = {
            "categories": df['date'].dt.strftime('%Y-%m-%d %H:%M:%S').tolist(),
            "data": df['price'].tolist()
        }

        return JsonResponse(chart_data)

    def load_or_fetch_data(self, data_path, country_code):
        if not os.path.exists(data_path) or os.path.getsize(data_path) == 0:
            df = self.fetch_historical_data(country_code)
            if df.empty:
                return df
        try:
            df = pd.read_csv(data_path, parse_dates=['date'])
            df['date'] = pd.to_datetime(df['date'], utc=True).dt.tz_convert(get_default_timezone())
            return df
        except pd.errors.EmptyDataError:
            print(f"The file at {data_path} is empty and cannot be parsed.")
            return pd.DataFrame()

    def filter_by_day(self, df, date_selected):
        selected_date = make_aware(datetime.strptime(date_selected, '%Y-%m-%d'))
        start_of_day = selected_date
        end_of_day = start_of_day + timedelta(days=1, microseconds=-1)
        return df[(df['date'] >= start_of_day) & (df['date'] <= end_of_day)]

    def filter_by_week(self, df, week_selected):
        year, week = map(int, week_selected.split('-W'))
        df['year'] = df['date'].dt.isocalendar().year
        df['week'] = df['date'].dt.isocalendar().week
        return df[(df['year'] == year) & (df['week'] == week)]

    def filter_by_month(self, df, month_selected):
        year, month = map(int, month_selected.split('-'))
        return df[(df['date'].dt.year == year) & (df['date'].dt.month == month)]

    def fetch_historical_data(self, country_code='PL', start_date=None, end_date=None):
        api_key = settings.ENTSOE_API_KEY
        client = EntsoePandasClient(api_key=api_key)
        data_dir = os.path.join(settings.BASE_DIR, 'SG/data')

        if not start_date:
            end_date = pd.Timestamp(datetime.now(), tz="Europe/Warsaw")
            start_date = end_date - pd.DateOffset(years=1)

        data_path = os.path.join(data_dir, f"energy_prices_{country_code}.csv")

        try:
            prices = client.query_day_ahead_prices(country_code, start=start_date, end=end_date)
            if prices.empty:
                raise ValueError(f"No data available for {country_code} from {start_date} to {end_date}")

            df = pd.DataFrame(list(prices.items()), columns=["date", "price"])
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
            df.to_csv(data_path, index=False)
            return df

        except Exception as e:
            print(f"An error occurred while fetching or saving data for {country_code}: {str(e)}")
            if not os.path.exists(data_path):
                pd.DataFrame().to_csv(data_path, index=False)
            return pd.DataFrame()

        return pd.read_csv(data_path, parse_dates=['date'])


def show_chart(request):
    context = {}
    return render(request, "SG.html", context)
