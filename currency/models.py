from django.db import models


class UsdRate(models.Model):

    rate = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(auto_now_add=True, unique=True)

    class Meta:
        verbose_name = "Dollar Rate"

    def __str__(self):
        return str(self.date)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.name)
