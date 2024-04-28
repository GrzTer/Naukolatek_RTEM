import pandas as pd
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from entsoe import EntsoePandasClient
import os
from datetime import datetime, timedelta
from django.conf import settings
from django.utils.timezone import make_aware, get_default_timezone

class EnergyPricesView(View):
    def post(self, request):
        country_code = request.POST.get("country_code", "PL").upper()
        date_selected = request.POST.get('date')
        week_selected = request.POST.get('week')
        month_selected = request.POST.get('month')

        data_dir = os.path.join(settings.BASE_DIR, 'SG/data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        data_path = os.path.join(data_dir, f"energy_prices_{country_code}.csv")
        # # Attempt to load existing data if available
        # try:
        #     df = pd.read_csv(data_path, parse_dates=['date'])
        # except FileNotFoundError:
        #     df = pd.DataFrame(columns=['date', 'price'])
        #
        # # Fetch data if not available
        # if df.empty or (time_span == 'day' and not df['date'].dt.date.eq(now().date()).any()):
        #     df = fetch_historical_data(country_code, data_path)
        df = pd.read_csv(data_path, parse_dates=['date'])
        df['date'] = pd.to_datetime(df['date'], utc=True).dt.tz_convert(get_default_timezone())

        if date_selected:
            selected_date = datetime.strptime(date_selected, '%Y-%m-%d')
            selected_date = make_aware(selected_date)
            start_of_day = selected_date
            end_of_day = start_of_day + timedelta(days=1, microseconds=-1)
            df = df[(df['date'] >= start_of_day) & (df['date'] <= end_of_day)]
        elif week_selected:
            year, week = map(int, week_selected.split('-W'))
            df['year'] = df['date'].dt.isocalendar().year
            df['week'] = df['date'].dt.isocalendar().week
            df = df[(df['year'] == year) & (df['week'] == week)]
        elif month_selected:
            year, month = map(int, month_selected.split('-'))
            df = df[(df['date'].dt.year == year) & (df['date'].dt.month == month)]

        if not date_selected:
            df = df.resample('D', on='date').agg({'price': 'mean'}).reset_index()

        df.sort_values(by="date", inplace=True)
        chart_data = {
            "categories": df['date'].dt.strftime('%Y-%m-%d %H:%M:%S').tolist(),
            "data": df['price'].tolist()
        }

        return JsonResponse(chart_data)

def fetch_historical_data(country_code='PL', start_date=None, end_date=None):
    api_key = settings.ENTSOE_API_KEY
    client = EntsoePandasClient(api_key=api_key)
    data_dir = os.path.join(settings.BASE_DIR, 'SG/data')

    if not start_date:
        end_date = make_aware(datetime.now())
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
