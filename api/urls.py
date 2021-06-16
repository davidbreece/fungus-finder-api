from django.conf.urls import url, include
from django.http import Http404
from api.views import FungusCreateView, FungusDetailView
from rest_framework.response import Response

urlpatterns = [
    url(r'^fungi/$', FungusCreateView.as_view(), name='fungi'),
    url(r'^fungi/(?P<pk>[0-9]+)/$', FungusDetailView.as_view(), name='detail'),
]
