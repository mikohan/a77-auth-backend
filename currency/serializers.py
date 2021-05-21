from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["date", "rate"]
