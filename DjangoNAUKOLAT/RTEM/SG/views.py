from django.shortcuts import render
import pandas as pd
import os
from django.conf import settings
import json

def energy_data_view(request):
    context = {
        'currency': 'EUR',
        'dates': json.dumps([]),
        'prices_chart': json.dumps([]),
        'error': None
    }

    if request.method == "POST":
        data_path = os.path.join(settings.BASE_DIR, 'data', 'energy_prices.csv')
        if not os.path.exists(data_path):
            context['error'] = "Data file does not exist. Please ensure data fetching is set up correctly."
            return render(request, "SG.html", context)

        # Read the whole dataset from CSV
        df = pd.read_csv(data_path)
        df['date'] = pd.to_datetime(df['date'])

        # Read user input for time span
        time_span = request.POST.get('time_span', 'year')

        if time_span == 'year':
            start_date = pd.Timestamp.now(tz="Europe/Warsaw") - pd.DateOffset(years=1)
        elif time_span == 'quarter':
            quarter = int(request.POST.get('quarter', 1))
            current_year = pd.Timestamp.now().year
            start_month = (quarter - 1) * 3 + 1
            start_date = pd.Timestamp(year=current_year, month=start_month, day=1)
            end_date = start_date + pd.DateOffset(months=3)
        elif time_span == 'month':
            month = int(request.POST.get('month', 1))
            current_year = pd.Timestamp.now().year
            start_date = pd.Timestamp(year=current_year, month=month, day=1)
            end_date = start_date + pd.DateOffset(months=1)
        elif time_span == 'week':
            week = int(request.POST.get('week', 1))
            year_start = pd.Timestamp(year=pd.Timestamp.now().year, month=1, day=1)
            start_date = year_start + pd.DateOffset(weeks=week - 1)
            end_date = start_date + pd.DateOffset(weeks=1)
        else:
            start_date = pd.Timestamp.now(tz="Europe/Warsaw") - pd.DateOffset(years=1)

        filtered_data = df[df['date'] >= start_date]
        if 'end_date' in locals():
            filtered_data = filtered_data[filtered_data['date'] < end_date]

        prices_data = [{
            'date': date.strftime('%Y-%m-%d'),
            'price': price
        } for date, price in zip(filtered_data['date'], filtered_data['price'])]

        context['dates'] = json.dumps([d['date'] for d in prices_data])
        context['prices_chart'] = json.dumps(prices_data)

    return render(request, "SG.html", context)
