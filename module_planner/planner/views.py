from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'planner/front_page.html')
