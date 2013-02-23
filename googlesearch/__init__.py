from django.conf import settings

api_version = getattr(settings, 'GOOGLE_SEARCH_API_VERSION', 'v1')
api_key = getattr(settings, 'GOOGLE_SEARCH_API_KEY', None)
cse_id = getattr(settings, 'GOOGLE_SEARCH_ENGINE_ID', None)
results_per_page = getattr(settings, 'GOOGLE_SEARCH_PAGE_SIZE', 10)
