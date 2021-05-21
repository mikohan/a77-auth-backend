import requests
from django.conf import settings

url = settings.CURRENCY_LATEST_URL


def run_api():

    r = requests.get(url)
    return r.json()
