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
        if data['username']=="hostel" and data['password']=="portal":
            print "DEBUG:username & password matched\nRedirecting to the homepage of stud's profile"
            response=render(request,'index2.html',dic)
            return response
    print "user & password did't match redirecting to login page again"
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
        print "DEBUG: data received data['usrname'] etc",data['username'],data['name']
        # put obtained value in the database
        #get his/her hosel from database and redrect to index2/limbdi
        response=render(request,'index2.html',dic)
        return response
    response=render(request,'registeration.html',dic)
    return response

def studprofile(request,roll):
    #find details related to the `roll` number
    dic={"name":"Shubham","roll":"15074014","hostel":"Limbdi","room":"B235","year":"2","branch":"xyz","course":"IMD"}
    print roll
    response=render(request,'profile.html',dic)
    return response
def messbill(request):
    pass
def policy(request):
    pass
