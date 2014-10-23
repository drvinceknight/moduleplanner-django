from django.conf.urls import patterns, include, url
from django.conf import settings
from planner.views import current_datetime

urlpatterns = patterns('',
        url(r'^$', current_datetime)
)
