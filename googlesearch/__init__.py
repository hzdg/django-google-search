from django.conf import settings


GOOGLE_SEARCH_API_KEY = getattr(settings, 'GOOGLE_SEARCH_API_KEY', None)
GOOGLE_SEARCH_ENGINE_ID = getattr(settings, 'GOOGLE_SEARCH_ENGINE_ID', None)
GOOGLE_SEARCH_API_VERSION = getattr(settings, 'GOOGLE_SEARCH_API_VERSION', 'v1')
GOOGLE_SEARCH_RESULTS_PER_PAGE = getattr(settings, 'GOOGLE_SEARCH_RESULTS_PER_PAGE', 10)