from http.client import HTTPException
from django.core.cache import caches
from django.views.decorators.cache import cache_page

from django.shortcuts import render
from parsers.weather_parser import get_temp
from parsers.currency_parser import get_currency


def index(request):
    try:
        temperature = get_temp(city='astana')
        return render(request, 'index.html', {'temperature': temperature})

    except Exception as e:
        raise HTTPException(f'{e}')


def request_currency(request):
    try:
        ram_cache = caches['default']
        cached_currency = ram_cache.get('currency')

        if cached_currency is None:
            currency = get_currency()
            ram_cache.set('currency', currency, 60)
            cached_currency = currency

        return render(request, 'currencies.html', {'currency': cached_currency})

    except Exception as e:
        raise HTTPException(f'{e}')
