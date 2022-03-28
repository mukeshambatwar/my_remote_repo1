from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    print(type(request))
    print("Hello... new version")
    print('This is Demo session of git....')
    s='<h1>Welcome to Durgasoft for Django Classes</h1>'
    return HttpResponse(s)
