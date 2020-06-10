from django.urls import path,include, re_path
from django.conf.urls import url
from .apiviews import *

app_name = 'landingPageTester'

urlpatterns = [
    re_path(r'^page/(?P<url>.+)/?$', PageList.as_view(), name='list'),
    path('pages/', AllPagesList.as_view(), name='all')
]
