from django.conf.urls.defaults import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^\?=(.*)?$', ResultsView.as_view(), name="search-results-view"),
    url(r'^$', SearchView.as_view(), name="search-view"),
)