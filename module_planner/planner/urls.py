from django.conf.urls import patterns, url
from django.views.generic import View

urlpatterns = patterns('', 
        url(r'^(?P<pk>[\w\d]+)/module/$', View.as_view(), name='module')
)
