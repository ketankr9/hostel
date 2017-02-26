from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    dic={}
    return render(request,'index.html',dic)

def index2(request):
    dic={}
    return render(request,'index2.html',dic)

def contactus(request):
    dic={}
    return render(request,'contactus.html',dic)

def grieve(request):
    dic={}
    return render(request,'grieve.html',dic)

def login(request,num):
    dic={}
    print "LOGIN:num:",num
    #redirection here
    # if 'cook' in request.COOKIES:
    #     print "Cookies exists::COOKED"
    #
    if request.method=="POST":
        print "DEBUG:RECEIVED POST(LOGIN)"
        data=request.POST
        print data['username'],data['password']
        # check from database here
        #at last
        response=render(request,'index2.html',dic)
    else:
        response=render(request,'login.html',dic)

    return response

def discussion(request):
    dic={}
    return render(request,'discussion.html',dic)

def register(request):
    dic={}
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
def messbill(request):
    pass
def policy(request):
    pass
