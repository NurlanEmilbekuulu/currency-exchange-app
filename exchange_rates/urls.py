from django.urls import path

from .views import ExchangeRateView

urlpatterns = [
    path('', ExchangeRateView.as_view(), name='current_exchange_rates'),
]
