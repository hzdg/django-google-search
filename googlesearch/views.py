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
class ResultsView(TemplateView):
    template_name = "search_results.html"
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
        
            """
            The total number of pages returned in the result set
            """
            'pages': self.get_pages() if self.results.findall(".//R") else [],
            
            
            """
            The total number of results in the result set
            """
            'total_results': self.results.find(".//M"),
            
            
            """
            The number of the first result in the result set
            """
            'start_index': start_index,
            
            """
            The number of the last result in the result set
            """
            'end_index': int(start_index) + len(self.results.findall(".//R")),
            
            
            """
            The number of the first result in the next page
            """
            'prev_page': int(start_index) - 10,
            
            
            """
            The number of the last result in the previous page
            """           
            'next_page': int(start_index) + 10,
            
            """
            The returned search results
            """                
            'results': self.results.findall(".//R"),
            
            """
            The terms the user searched for
            """            
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
                
                """
                The parameters to query
                """
                "q=%s" % self.request.GET.get(
                    'search_text', '').replace(' ', '+'),
                    
                """
                The search engine ID
                """
                "cx=%s" % self.cse_id,
                
                """
                The result number to start with
                """
                "start=%s" % self.request.GET.get('start', '0'),
                
                """
                The result number to end with
                """
                "num=%s" % self.request.GET.get('num', '10'),
                
                """
                The output type
                """
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

"""
Displays a search form
"""
class SearchView(TemplateView):
    template_name = "search_form.html"

