from rest_framework.generics import GenericAPIView
from .models import UsdRate
from .serializers import CurrencySerializer


class CurrencyAPIView(GenericAPIView):
    queryset = UsdRate.objects.all()
    serializr_class = CurrencySerializer
    paginator = None
