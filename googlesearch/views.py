from django.views.generic import TemplateView
from .conf import settings
import logging
import requests

"""
The main search display view
"""


class SearchView(TemplateView):
    template_name = "googlesearch/google_search.html"

    @property
    def endpoint(self):
        return "https://www.googleapis.com/customsearch/%s/" % (
            settings.GOOGLE_SEARCH_API_VERSION)

    def get_context_data(self, **kwargs):

        context = super(SearchView, self).get_context_data(**kwargs)

        cse_data = self.get_results(self.request.GET)

        if cse_data and 'queries' in cse_data:

            current_page = self.request.GET.get('page', 1)

            if 'nextPage' in cse_data['queries']:
                # Super fragile lets hope it works
                next_page = cse_data['queries']['nextPage'][0]['startIndex']
            else:
                next_page = self.request.GET.get('page', 1)

            if 'previousPage' in cse_data['queries']:
                # Super fragile lets hope it works
                prev_page = cse_data[
                    'queries']['previousPage'][0]['startIndex']
            else:
                prev_page = 0

            items = cse_data.get('items', [])

            context.update({
                'items': items,
                'total_results': int(
                    cse_data['queries']['request'][0]['totalResults']),
                'current_page': int(current_page),
                'prev_page': int(prev_page),
                'next_page': int(next_page),
                'search_terms': cse_data[
                    'queries']['request'][0]['searchTerms']
            })

            return context

        else:

            context.update({
                'items': [],
                'total_results': 0,
                'current_page': 0,
                'prev_page': 0,
                'next_page': 0,
                'search_terms': self.request.GET.get('q'),
                'error': cse_data
            })

            return context

    """
    Makes the request to Google and returns
    matching pages in json
    """
    def get_results(self, GET):

        params = {
            'key': settings.GOOGLE_SEARCH_API_KEY,
            'q': GET.get('q', '').replace(' ', '+'),
            'cx': settings.GOOGLE_SEARCH_ENGINE_ID,
            'start': int(GET.get('page', 1)),
            'alt': 'json',
            'num': settings.GOOGLE_SEARCH_RESULTS_PER_PAGE,
            'sort': GET.get('sort', 'date-sdate:d:s')
        }

        try:
            r = requests.get(self.endpoint, params=params)

        except Exception as e:
            logging.warning("Google Custom Search Error: %s" % (str(e)))
            return False
