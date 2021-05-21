from django.db import models
from datetime import datetime


class UsdRate(models.Model):

    rate = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(auto_now_add=True, unique=True)

    class Meta:
        verbose_name = "Dollar Rate"

    def __str__(self):
        return str(self.date)


class Product(models.Model):
    name = models.CharField(max_length=50)
    _price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.name)

    @property
    def price(self):
        today = datetime.now().date()
        rate = UsdRate.objects.get(date=today)
        print(float(rate.rate))
        return round(float(self._price) * float(rate.rate))
