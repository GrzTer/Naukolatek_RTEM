import pandas as pd
from django.http import JsonResponse
from django.views import View
from django.core.paginator import Paginator
from django.core.cache import cache
from django.shortcuts import render
from entsoe import EntsoePandasClient
import os
from datetime import datetime
from django.conf import settings


class EnergyPricesView(View):
    def post(self, request):
        cache_key = f"energy_prices_{request.POST.get('year', '')}_{request.POST.get('quarter', '')}_{request.POST.get('month', '')}_{request.POST.get('week', '')}_{request.POST.get('country_code', '')}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(cached_data)

        df = pd.read_csv("SG/energy_prices.csv")
        df["date"] = pd.to_datetime(df["date"], utc=True)

        # Pobranie parametrów z formularza
        year = request.POST.get("year")
        quarter = request.POST.get("quarter")
        month = request.POST.get("month")
        week = request.POST.get("week")
        day = request.POST.get("day")
        country_code = request.POST.get("country_code", "PL").upper()

        if year:
            df = df[df["date"].dt.year == int(year)]
        if quarter:
            df = df[df["date"].dt.quarter == int(quarter)]
        if month:
            df = df[df["date"].dt.month == int(month)]
        if week:
            df = df[df["date"].dt.isocalendar().week == int(week)]
        if day:
            df = df[df["date"].dt.isocalendar().day == int(day)]

        df.sort_values(by="date", inplace=True)

        paginator = Paginator(df, 100)
        page_obj = paginator.get_page(request.POST.get("page", 3))

        chart_data = {
            "categories": [
                date.strftime("%Y-%m-%d") for date in page_obj.object_list["date"]
            ],
            "data": [
                {"x": date.strftime("%Y-%m-%d"), "y": price}
                for date, price in zip(
                    page_obj.object_list["date"], page_obj.object_list["price"]
                )
            ],
        }

        cache.set(cache_key, chart_data, timeout=15 * 60)

        return JsonResponse(chart_data)


def fetch_historical_data():
    api_key = settings.ENTSOE_API_KEY
    client = EntsoePandasClient(api_key=api_key)
    end_date = pd.Timestamp(datetime.now(), tz="Europe/Warsaw")
    start_date = end_date - pd.DateOffset(years=1)

    try:
        prices = client.query_day_ahead_prices("PL", start=start_date, end=end_date)
        df = pd.DataFrame(list(prices.items()), columns=["date", "price"])

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


def show_chart(request):
    context = {}
    return render(request, "SG.html", context)
