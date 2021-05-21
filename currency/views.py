from rest_framework.generics import ListAPIView
from .models import UsdRate
from .serializers import CurrencySerializer
from .cron import run_api
import json

from django_cron import CronJobBase, Schedule


class CurrencyAPIView(ListAPIView):
    queryset = UsdRate.objects.all()
    serializer_class = CurrencySerializer
    paginator = None

    def get(self, request, *args, **kwargs):
        # data = run_api()
        with open(
            "/home/manhee/Projects/Sandbox/DjangoProjects/auth_system2/currency/data.json",
            "r",
        ) as file:
            j = json.load(file)
            obj = UsdRate(rate=str(j["rates"]["RUB"]))
            print(j["rates"]["RUB"])

        return self.list(request, *args, **kwargs)
