from currency.models import UsdRate
from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = UsdRate
        fields = ["date", "rate"]
