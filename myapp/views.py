from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import connection
from .forms import *
#from reportlab.pdfgen import canvas #dynamic pdf generation

from io import BytesIO
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
        #print "DEBUG: data received data['usrname'] etc",data['username'],data['name']
        # put obtained value in the database
        # cursor=connection.cursor()
        # cursor.execute('''INSERT INTO limbdi2016(room) VALUES(%s)''',[data['ifsc']])
        # cursor.close()
        #get his/her hostel from database and redrect to index2/limbdi
        des=open("/home/uk/django/hostel/pic.png",'wb+')
        for chunk in (request.FILES['file']).chunk():
            des.write(chunk)
        des.close()
        print request.FILES['file'].name
        response=render(request,'index2.html',dic)
        return response
    response=render(request,'registeration.html',dic)
    return response
def register2(request):
    if not request.user.is_authenticated:
        return HttpResponse('''LOGIN REQUIRED, come here when you had already logged in<br/> <a href="/signup/">Signup</a> <a href="/login/">Login</a>''')

    if request.method=='POST':
        form=ProfileForm(request.POST)
        print "post received"
        if form.is_valid():
            if request.user.username != form.cleaned_data['roll_no']:
                print "Caught you"
                return HttpResponse("Caught you!!!<br/>You can't register on behalf of your friend :(")
            print "yes is valid"
            post=form.save(commit=False)
            post.save()
            return redirect('/')
        else:
            print "Not valid"
            return HttpResponse("Your registeration is already done<br/>Please contact your administrator")
    else:
        print "not post"
        form=ProfileForm()

    return render(request,'registeration2.html',{'form':form})


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

# def createPDF(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition']='attachment; filename="registerationForm.pdf"'
#     buff=BytesIO()
#     p=canvas.Canvas(buff)
#     p.drawString(100,100,"100:100 Hello World.")
#     p.showPage()
#     p.save()
#     pdf=buff.getvalue()
#     buff.close()
#     response.write(pdf)
#     return response
