import pandas as pd
import logging
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

# Set up logging
logger = logging.getLogger(__name__)

# Function to serve the main HTML page
@require_http_methods(["GET"])
def index(request):
    return render(request, 'SG.html')

# Function to fetch and process chart data from the CSV
def fetch_chart_data(request):
    try:
        # Read the CSV file
        data = pd.read_csv('energy_prices.csv')
        data['Date'] = pd.to_datetime(data['Date'])

        # Retrieve filtering parameters from the request
        time_span = request.POST.get('time_span', 'month')
        start_date = request.POST.get('start_date', data['Date'].min().strftime('%Y-%m-%d'))
        end_date = request.POST.get('end_date', data['Date'].max().strftime('%Y-%m-%d'))

        # Filter data within the selected date range
        data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

        # Additional filtering based on 'time_span'
        if time_span == 'month':
            month = int(request.POST.get('month'))
            data = data[data['Date'].dt.month == month]
        elif time_span == 'week':
            week = int(request.POST.get('week'))
            data = data[data['Date'].dt.week == week]
        elif time_span == 'year':
            year = int(request.POST.get('year'))
            data = data[data['Date'].dt.year == year]

        # Convert data for chart
        chart_data = [
            {'x': row['Date'].strftime('%Y-%m-%d'), 'y': row['Price']}
            for index, row in data.iterrows()
        ]
        return JsonResponse(chart_data, safe=False)
    except Exception as e:
        logger.error("Failed to fetch or process data: %s", e)
        return JsonResponse({'error': 'Internal server error'}, status=500)

# Function to handle POST requests for data fetching
@require_http_methods(["POST"])
def get_data(request):
    return fetch_chart_data(request)
