from django.conf.urls import url, include
from django.urls import path
from django.http import Http404
from api.views import FungusCreateView, FungusDetailView
from rest_framework.response import Response

from scraper.views import DashboardView

urlpatterns = [
    #url(r'^scraper/$', FungusCreateView.as_view(), name='fungi')
    url(r'', DashboardView.as_view(), name="scraper")
]
