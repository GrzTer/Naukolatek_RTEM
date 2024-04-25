import pandas as pd
from django.http import JsonResponse
from django.views import View
from django.core.paginator import Paginator
from django.core.cache import cache
from django.shortcuts import render

class EnergyPricesView(View):
    def post(self, request):
        # Utwórz klucz cache'u na podstawie parametrów żądania
        cache_key = f"energy_prices_{request.POST.get('year', '')}_{request.POST.get('quarter', '')}_{request.POST.get('month', '')}_{request.POST.get('week', '')}_{request.POST.get('country_code', '')}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(cached_data)

        df = pd.read_csv('SG/energy_prices.csv')
        df['date'] = pd.to_datetime(df['date'], utc=True)  # Dodano 'utc=True' do uniknięcia ostrzeżenia

        # Pobranie parametrów z formularza
        year = request.POST.get('year')
        quarter = request.POST.get('quarter')
        month = request.POST.get('month')
        week = request.POST.get('week')
        country_code = request.POST.get('country_code', '').upper()

        if year:
            df = df[df['date'].dt.year == int(year)]
        if quarter:
            df = df[df['date'].dt.quarter == int(quarter)]
        if month:
            df = df[df['date'].dt.month == int(month)]
        if week:
            df = df[df['date'].dt.isocalendar().week == int(week)]

        df.sort_values(by='date', inplace=True)

        paginator = Paginator(df, 100)
        page_obj = paginator.get_page(request.POST.get('page', 3))

        chart_data = {
            'categories': [date.strftime('%Y-%m-%d') for date in page_obj.object_list['date']],
            'data': [{'x': date.strftime('%Y-%m-%d'), 'y': price} for date, price in zip(page_obj.object_list['date'], page_obj.object_list['price'])]
        }

        cache.set(cache_key, chart_data, timeout=15 * 60)

        return JsonResponse(chart_data)

def show_chart(request):
    context = {}
    return render(request, 'SG.html', context)
