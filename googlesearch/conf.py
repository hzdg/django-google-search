from django.conf import settings # Dont delete
from appconf import AppConf


class GoogleSearchAppConf(AppConf):
    API_VERSION = 'v1'
    API_KEY = None
    ENGINE_ID = None
    RESULTS_PER_PAGE = 10

    class Meta:
        prefix = 'google_search'
