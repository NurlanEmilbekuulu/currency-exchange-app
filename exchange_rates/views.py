from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView

from .models import CurrencyRate


class ExchangeRateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        date_mapping = {
            'yesterday': -1,
            'day_before_yesterday': -2,
        }
        query = self.request.GET.get('q')
        offset = date_mapping.get(query, 0)
        currency_rate_date = (
            timezone.now() + timezone.timedelta(days=offset)).strftime('%Y-%m-%d')
        try:
            context = super().get_context_data(**kwargs)
            context['rate'] = CurrencyRate.objects.get(date=currency_rate_date)
            return context
        except CurrencyRate.DoesNotExist:
            raise Http404("Currency rate not found for the given date.")


def custom_not_found_view(request, exception):
    return render(request, '404.html', status=404)
