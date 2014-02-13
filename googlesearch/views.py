from django.views.generic import TemplateView
from apiclient.discovery import build
from .utils import SearchResults
from  . import *



class SearchView(TemplateView):
    template_name = "googlesearch/search_results.html"


    def get_context_data(self, **kwargs):

        context = super(SearchView, self).get_context_data(**kwargs)

        service = build("customsearch", GOOGLE_SEARCH_API_VERSION,
            developerKey=GOOGLE_SEARCH_API_KEY)

        results = service.cse().list(
                q=self.request.GET.get('q', ''),
                start=self.page_to_index(),
                num=GOOGLE_SEARCH_RESULTS_PER_PAGE,
                cx=GOOGLE_SEARCH_ENGINE_ID,
            ).execute()

        results = SearchResults(results)

        """ Set some defaults """
        context.update({
            'items': [],
            'total_results': 0,
            'current_page': 0,
            'prev_page': 0,
            'next_page': 0,
            'search_terms': self.request.GET.get('q', ''),
            'error': results
        })

        """ Now parse the results and send back some
            useful data """

        pages = self.calculate_pages()

        context.update({
                'items': results.items,
                'total_results': results.total_results,
                'current_page': pages[1],
                'prev_page': pages[0],
                'next_page': pages[2],
                'search_terms': results.search_terms,
            })


        return context


    def calculate_pages(self):
        """ Returns a tuple consisting of
            the previous page, the current page,
            and the next page """

        current_page = int(self.request.GET.get('p', 1))
        return (current_page - 1, current_page, current_page + 1,)



    def page_to_index(self, page=None):

        """ Converts a page to the start index """

        if page is None:
            page = self.request.GET.get('p', 1)

        return int(page) * int(GOOGLE_SEARCH_RESULTS_PER_PAGE) + 1 -  int(GOOGLE_SEARCH_RESULTS_PER_PAGE)

