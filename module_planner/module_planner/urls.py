from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from planner.views import current_datetime

urlpatterns = patterns('',
        url(r'^$', current_datetime),
        url(r'^admin/', include(admin.site.urls))

)
