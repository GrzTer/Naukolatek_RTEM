from django.shortcuts import render
from entsoe import EntsoePandasClient
import pandas as pd
import json
from entsoe.exceptions import NoMatchingDataError

def energy_data_view(request):
    api_key = "d9f78120-2bb1-4182-b3d2-a88195b24ad5"
    client = EntsoePandasClient(api_key=api_key)
    country_currency_map = {
        'AL': 'ALL',  # Albania
        'AD': 'EUR',  # Andora
        'AM': 'AMD',  # Armenia
        'AT': 'EUR',  # Austria
        'AZ': 'AZN',  # Azerbejdżan
        'BY': 'BYN',  # Białoruś
        'BE': 'EUR',  # Belgia
        'BA': 'BAM',  # Bośnia i Hercegowina
        'BG': 'BGN',  # Bułgaria
        'HR': 'HRK',  # Chorwacja
        'CY': 'EUR',  # Cypr
        'CZ': 'CZK',  # Czechy
        'DK': 'DKK',  # Dania
        'EE': 'EUR',  # Estonia
        'FI': 'EUR',  # Finlandia
        'FR': 'EUR',  # Francja
        'GE': 'GEL',  # Gruzja
        'DE': 'EUR',  # Niemcy
        'GR': 'EUR',  # Grecja
        'HU': 'HUF',  # Węgry
        'IS': 'ISK',  # Islandia
        'IE': 'EUR',  # Irlandia
        'IT': 'EUR',  # Włochy
        'KZ': 'KZT',  # Kazachstan
        'XK': 'EUR',  # Kosowo
        'LV': 'EUR',  # Łotwa
        'LI': 'CHF',  # Liechtenstein
        'LT': 'EUR',  # Litwa
        'LU': 'EUR',  # Luksemburg
        'MT': 'EUR',  # Malta
        'MD': 'MDL',  # Mołdawia
        'MC': 'EUR',  # Monako
        'ME': 'EUR',  # Czarnogóra
        'NL': 'EUR',  # Holandia
        'MK': 'MKD',  # Macedonia Północna
        'NO': 'NOK',  # Norwegia
        'PL': 'PLN',  # Polska
        'PT': 'EUR',  # Portugalia
        'RO': 'RON',  # Rumunia
        'RU': 'RUB',  # Rosja
        'SM': 'EUR',  # San Marino
        'RS': 'RSD',  # Serbia
        'SK': 'EUR',  # Słowacja
        'SI': 'EUR',  # Słowenia
        'ES': 'EUR',  # Hiszpania
        'SE': 'SEK',  # Szwecja
        'CH': 'CHF',  # Szwajcaria
        'TR': 'TRY',  # Turcja
        'UA': 'UAH',  # Ukraina
        'GB': 'GBP',  # Wielka Brytania
        'VA': 'EUR',  # Watykan
    }
    context = {
        'currency': 'EUR',
        'dates': json.dumps([]),
        'prices_chart': json.dumps([]),
        'error': None
    }

    if request.method == "POST":
        country_code = request.POST.get("country_code", "PL").upper()
        currency = country_currency_map.get(country_code, 'EUR')
        context['currency'] = currency
        start_date = pd.Timestamp(request.POST.get("start_date", "2024-03-01"), tz="Europe/Warsaw")
        end_date = pd.Timestamp(request.POST.get("end_date", "2024-04-01"), tz="Europe/Warsaw")

        try:
            prices = client.query_day_ahead_prices(country_code, start=start_date, end=end_date)
            prices_data = [{'date': str(index.strftime('%Y-%m-%d')), 'price': value} for index, value in prices.items()]
            context['dates'] = json.dumps([item['date'] for item in prices_data])
            context['prices_chart'] = json.dumps(prices_data)
        except NoMatchingDataError:
            context['error'] = "No matching data available for the selected range."
        except Exception as e:
            context['error'] = f"An error occurred: {str(e)}"

        return render(request, "SG.html", context)

    return render(request, "SG.html", context)