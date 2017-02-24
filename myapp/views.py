from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return  HttpResponse("index page of my app")

def index2(request):
    return HttpResponse("index2 page of myapp")

def contactus(request):
    return HttpResponse("contact us page of myapp")

def grieve(request):
    return HttpResponse("grieverience page of myapp")

def loginu(request ):
    return HttpResponse("this is login page of myapp")

def discussion(request):
    return HttpResponse("this is discussion page of my app")

def register(request):
    return HttpResponse("this is discussion page of my app")

def studprofile(request):
    return HttpResponse("this is student profile page of my app")

def past(request):
    return HttpResponse("this is a past page of my app")
