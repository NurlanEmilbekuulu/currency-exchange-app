from datetime import date
from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from .models import CurrencyRate


class CurrencyRateModelTestCase(TestCase):
    def test_currency_rate_str_representation(self):
        rate = CurrencyRate.objects.create(date='2023-08-05', usd_to_rub=75.0, eur_to_rub=88.5)
        self.assertEqual(str(rate), '2023-08-05 - USD: 75.0, EUR: 88.5')


class ExchangeRateViewTestCase(TestCase):
    def setUp(self):
        CurrencyRate.objects.create(
            date=timezone.now().strftime('%Y-%m-%d'), usd_to_rub=75.0, eur_to_rub=88.5)

    def test_exchange_rate_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def tearDown(self) -> None:
        CurrencyRate.objects.all().delete()


class CurrencyRateUpdateTest(TestCase):

    @patch('requests.get')
    def test_currency_rate_update_command(self, mock_get):
        # Mock the response from the API
        mock_response_data = {
            'conversion_rates': {'RUB': 75.0},
        }
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data

        # Call the management command
        call_command('update_currency_rates')

        # Check if the CurrencyRate object is created with the correct values
        currency_rate = CurrencyRate.objects.get(date=date.today())
        self.assertEqual(currency_rate.usd_to_rub, 75.0)
        self.assertEqual(currency_rate.eur_to_rub, 75.0)
