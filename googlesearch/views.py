from django.conf import settings
from django.views.generic import TemplateView, DetailView, ListView
import math
import pprint
import logging
import urllib2
from lxml import etree

"""
The main search display view
"""
class SearchView(TemplateView):
    template_name = "google_search.html"
    version = getattr(settings, 'GOOGLE_SEARCH_API_VERSION', 'v1')
    api_key = getattr(settings, 'GOOGLE_SEARCH_API_KEY', None)
    cse_id = getattr(settings, 'GOOGLE_SEARCH_ENGINE_ID', None)
    endpoint = "http://www.google.com/?"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        self.search()

        if not self.results:
            return context

        start_index = self.results.xpath(
            "//PARAM[@name='start']")[0].get('value', '1')

        context.update({
            'pages': self.get_pages() if self.results.findall(".//R") else [],
            'total_results': self.results.find(".//M"),
            'start_index': start_index,
            'end_index': int(start_index) + len(self.results.findall(".//R")),
            'prev_page': int(start_index) - 10,
            'next_page': int(start_index) + 10,
            'results': self.results.findall(".//R"),
            'search_terms': self.results.xpath(
                "//PARAM[@name='q']")[0].get('value', '1'),
        })

        return context
    
    """
    Makes the request to Google and returns
    matching pages in XML
    """
    def search(self):

        try:
            params = '&'.join([
                "q=%s" % self.request.GET.get(
                    'search_text', '').replace(' ', '+'),
                "cx=%s" % self.cse_id,
                "start=%s" % self.request.GET.get('start', '0'),
                "num=%s" % self.request.GET.get('num', '10'),
                "output=xml_no_dtd"
            ])

            data = urllib2.urlopen(self.endpoint + params)
            self.results = etree.XML(data.read())
            return True

        except Exception as e:
            logging.warning("Google Custom Search Error: %s" % (str(e)))
            self.results = False
            return False

        else:
            return True

    """
    Makes the request to Google and returns
    matching pages
    """
    def get_pages(self):

        max_pages = int(math.ceil(float(
            self.results.find(".//M").text) / 10))

        current_page = int(math.floor(float(
            self.results.xpath("//PARAM[@name='start']")[0].get('value')) / 10))

        return [(i, (10 * i), (current_page == i)) for i in range(0, max_pages)]
