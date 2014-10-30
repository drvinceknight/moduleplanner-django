from django.conf.urls import patterns, include, url
from django.conf import settings
from planner.views import ModuleInfoView

urlpatterns = patterns('',
        url(r'^$', ModuleInfoView.as_view()),

)
