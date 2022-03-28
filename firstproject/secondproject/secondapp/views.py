from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def time_info_views(request):
    time=datetime.datetime.now()
    s='<h1> Welcome to second project of Django about time information :'+str(time)+' </h1>'
    return HttpResponse(s)
