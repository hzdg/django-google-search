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

        if len(self.request.GET) == 0:
            return context

        json = self.get_results(self.request.GET)

        if json is False:
            return context

        current_page = self.request.GET.get('page', 1)

        try:
            prev_page = json.queries.previousPage[0].startIndex
        except:
            prev_page = 1

        try:
            next_page = json.queries.nextPage[0].startIndex
        except:
            next_page = self.request.GET.get('page', 1)

        try:
            items = json.items
        except:
            items = []

        context.update({
            'items': items,
            'total_results': int(json.queries.request[0].totalResults),
            'current_page': int(current_page),
            'prev_page': int(prev_page),
            'next_page': int(next_page),
            'search_terms': json.queries.request[0].searchTerms,
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
            return simplejson.loads(r.text, object_hook=decode_hook)

        except Exception as e:
            logging.warning("Google Custom Search Error: %s" % (str(e)))
            return False
