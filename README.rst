django-google-search
====================

Django app to show results from a Google Custom Search Engine or Google Site Search

1. Create a Google Custom Search Engine
2. Enable API Access

`https://code.google.com/apis/console`

3. Add the following to settings.py:

.. code-block:: python

	GOOGLE_SEARCH_API_KEY = 'YOUR API KEY'
	GOOGLE_SEARCH_ENGINE_ID = 'YOUR GOOGLE SEARCH ENGINE ID'
	GOOGLE_SEARCH_API_VERSION = 'v1' #(optional. defaults to v1)

3. Create your search results template.
Use the included google_search_results.html template, or create your own template override. 
The template gets passed the following template variables:
 ::

	pages: the total number of pages returned
	total_results:
	start_index:
	end_index:
	prev_page:
	next_page:
	results:
	search_terms:
