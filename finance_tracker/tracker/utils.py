# utils.py (new file)
import requests
import os
from django.core.cache import cache
from dotenv import load_dotenv

load_dotenv()

def convert_currency(amount, from_currency, to_currency):
    """
    Converts the given amount from one currency to another using a currency conversion API.
    Caches the exchange rates for efficiency.
    """
    # Check if the exchange rates are already cached
    rates = cache.get('exchange_rates')
    if not rates:
        base_currency = 'USD'
        api_key = os.getenv('EXCHANGE_RATE_API_KEY')  # Fetch API key from .env
        endpoint = f"https://open.er-api.com/v6/latest/{base_currency}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            rates = response.json().get("rates", {})
            # Cache the rates for 1 hour (3600 seconds)
            cache.set('exchange_rates', rates, timeout=3600)
        else:
            raise ValueError("Currency conversion API failed")

    # Get the conversion rates for the requested currencies
    if from_currency == 'USD':
        conversion_rate = rates.get(to_currency)
    else:
        # Assuming the base currency is USD, convert to USD first
        conversion_rate_from_base = rates.get(from_currency)
        conversion_rate_to_target = rates.get(to_currency)
        if conversion_rate_from_base and conversion_rate_to_target:
            conversion_rate = conversion_rate_to_target / conversion_rate_from_base
        else:
            conversion_rate = None

    if conversion_rate:
        return round(amount * conversion_rate, 2)
    else:
        return amount  # Return the original amount if conversion fails
