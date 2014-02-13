django-google-search
====================

Django app to show results from a Google Custom Search Engine or Google Site Search

Installation and configuration
------------------------------

1. Create a `Google Custom Search Engine <https://www.google.com/cse/>`_ ("CSE").

2. Install with pip::

    pip install -e git@github.com:hzdg/django-google-search.git

2. Add the app to INSTALLED_APPS along with the following parameters to settings.py::

    INSTALLED_APPS (
        'googlesearch',
        ...,
    )

    GOOGLE_SEARCH_API_KEY = 'YOUR API KEY'
    GOOGLE_SEARCH_ENGINE_ID = 'YOUR GOOGLE SEARCH ENGINE ID'
    GOOGLE_SEARCH_API_VERSION = 'v1' #(optional. defaults to v1)

3. Create the URL for your search page. In urls.py::

    (r'^search/', include('googlesearch.urls'))

How it works
------------

Send a GET request to your search page, with a querystring parameter of 'q'. The app will pass the value of "q" along to your Google CSE, and return the results to your template.

Use the included google_search_results.html template, or create your own template override. The search results template is passed the following template variables

pages
    the total number of pages returned

total_results
    the total number of results found

start_index
    the starting index of the results that are returned

end_index
    the ending index of the results that are returned

prev_page
    the previous page number

next_page:
    the next page number

results
    the actual search results to iterate over

search_terms
    the terms used in the search