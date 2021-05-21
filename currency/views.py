from rest_framework.generics import ListAPIView
from .models import UsdRate
from .serializers import CurrencySerializer
from .cron import run_api
import json
from rest_framework.exceptions import APIException

from django_cron import CronJobBase, Schedule


class CurrencyAPIView(ListAPIView):
    queryset = UsdRate.objects.all()
    serializer_class = CurrencySerializer
    paginator = None

    def get(self, request, *args, **kwargs):
        try:
            data = run_api()

            obj = UsdRate(rate=str(data["rates"]["RUB"]))
            obj.save()
        except:
            raise APIException("Rate already inserted today")

        return self.list(request, *args, **kwargs)
