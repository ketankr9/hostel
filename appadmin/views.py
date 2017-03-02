from django.shortcuts import render
from django.http import HttpResponse,HttpREsponseRedirect
# Create your views here.


def index(request):
     return  HttpResponse("this is index view of appadmin")
