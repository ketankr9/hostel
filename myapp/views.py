from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html',dic)

def index2(request):
    return render(request,'index2.html',dic)

def contactus(request):
    dic={}
    return render(request,'contactus.html',dic)

def grieve(request):
    dic={}
    return render(request,'grieve.html',dic)

def login(request,num):
    dic={}
    print "num received",num
    #redirection here
    # if 'cook' in request.COOKIES:
    #     print "Cookies exists::COOKED"
    #
    response=render(request,'login.html',dic)

    return response

def discussion(request):
    dic={}
    return render(request,'discussion.html',dic)

def register(request):
    print "Registeration page"
    if request.method=='POST':
        data=request.POST
        print "print here the received values eg data['usrname'],data['password'], etc"
    return render(request,'registeration.html',dic)

def studprofile(request,roll):
    print roll
    dic={}
    response=render(request,'index2.html',dic)
    return response

def past(request):
    return HttpResponse("this is a past page of my app")
