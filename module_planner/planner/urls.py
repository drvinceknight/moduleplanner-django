from django.conf.urls import patterns, url
from views import PostDetailView

urlpatterns = patterns('', 
        url(r'^(?P<pk>[\w\d]+)/module/$', PostDetailView.as_view()), name='module')

