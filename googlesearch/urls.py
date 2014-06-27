try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^$', SearchView.as_view(
                       ), name="google-search-view"),
                       )
