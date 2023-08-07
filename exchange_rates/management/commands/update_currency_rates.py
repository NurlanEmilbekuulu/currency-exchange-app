from datetime import date

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from exchange_rates.models import CurrencyRate


class Command(BaseCommand):
    help = 'Update currency rates in the database'

    def handle(self, *args, **kwargs):
        try:
            usd_to_rub, eur_to_rub = self.fetch_currency_rates()
            CurrencyRate.objects.create(
                date=date.today(),
                usd_to_rub=usd_to_rub,
                eur_to_rub=eur_to_rub,
            )
            self.stdout.write(self.style.SUCCESS(
                'Currency rates updated successfully!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f'Failed to fetch currency rates: {str(e)}'))

    def fetch_currency_rates(self):
        usd_to_rub = 0
        eur_to_rub = 0
        currencies = ['USD', 'EUR']
        for currency in currencies:
            response = requests.get(
                f'https://v6.exchangerate-api.com/v6/{settings.EXCHANGE_API_TOKEN}/latest/{currency}')
            self.stdout.write(self.style.SUCCESS(
                f'Fetched currency rate for {response.json()}'))
            response.raise_for_status()
            data = response.json()
            rate_to_rub = data['conversion_rates']['RUB']
            if currency == 'USD':
                usd_to_rub = rate_to_rub
            else:
                eur_to_rub = rate_to_rub
        return usd_to_rub, eur_to_rub
