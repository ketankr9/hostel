from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

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
    dic["value"]="Enter userid and password"
    if request.method=="POST":
        print "DEBUG:RECEIVED POST(LOGIN)"
        data=request.POST
        print data['username'],data['password']
        # check from database here
        #at last
        if data['username']=="hostel" and data['password']=="portal":
            print "DEBUG:username & password matched\nRedirecting to the homepage of stud's profile"
            return HttpResponseRedirect('/index2/')
            # response=render(request,'index2.html',dic)
            # return response
        else:
            dic["value"]="Wrong password or userid"
    print "user & password did't match redirecting to login page again"

    response=render(request,'login.html',dic)
    return response

def discussion(request):
    dic={}
    return render(request,'discussion.html',dic)

def register(request):
    if not request.user.is_authenticated:
        print "Login required",request.user.is_authenticated
    # Do something for anonymous users.
        return render(request,'login.html',{})
    # Do something for authenticated users.
    dic={}
    print "Registeration page"
    if request.method=='POST':
        data=request.POST
        print "DEBUG: data received data['usrname'] etc",data['username'],data['name']
        # put obtained value in the database
        #get his/her hostel from database and redrect to index2/limbdi
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
    dict={'january':'1000',
           'feburary':'2000',
              'march':'3000', 'april':'4000','may':'5000','june':'6000','july':'7000','august':'8000','september':'9000',
                 'october':'10000','november':'11000','december':'12000'}
    return render(request,'messMonthly.html',dict)
def signup(request):
    dic={}

    print request.method
    if request.method=='POST':
        data=request.POST
        print "DEBUG:POST received"
        print data["passwd"]
        user=User.objects.create_user(data['username'],"",data['passwd'])
        user.save()
        return render(request,'login.html',dic)
    response=render(request,'signup2.html',dic)
    return response

def policy(request):
    pass
