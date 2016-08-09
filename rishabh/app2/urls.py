from django.conf.urls import patterns, url

#from app2.views import HomePageView
from django.conf.urls import patterns, include, url
from app1.views import *


urlpatterns = patterns(
    '',

    #url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^$', home),
)