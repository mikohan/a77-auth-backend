from rest_framework.generics import ListAPIView
from .models import UsdRate
from .serializers import CurrencySerializer

from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 120  # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "currency.my_cron_job"  # a unique code

    def do(self):
        print("Cron runned")


class CurrencyAPIView(ListAPIView):
    queryset = UsdRate.objects.all()
    serializer_class = CurrencySerializer
    paginator = None
