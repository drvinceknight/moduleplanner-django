from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It's now %s.</body></html>" % now
    return HttpResponse(html)
