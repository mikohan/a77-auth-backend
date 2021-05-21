from django.urls import path
from .views import CurrencyAPIView

urlpatterns = [path("", CurrencyAPIView.as_view(), name="currency")]
