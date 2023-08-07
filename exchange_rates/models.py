from django.db import models


class CurrencyRate(models.Model):
    date = models.DateField(unique=True)
    usd_to_rub = models.DecimalField(max_digits=10, decimal_places=4)
    eur_to_rub = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.date} - USD: {self.usd_to_rub}, EUR: {self.eur_to_rub}"
