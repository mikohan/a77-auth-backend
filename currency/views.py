from rest_framework.generics import ListAPIView
from .models import UsdRate
from .serializers import CurrencySerializer


class CurrencyAPIView(ListAPIView):
    queryset = UsdRate.objects.all()
    serializer_class = CurrencySerializer
    paginator = None
