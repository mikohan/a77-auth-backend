from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "date", "description", "amount", "category"]
        extra_kwargs = {
            "date": {"required": False, "allow_null": True},
            "amount": {"required": False, "allow_null": True},
            "category": {"required": False, "allow_null": True},
            "description": {"required": False, "allow_null": True},
        }
