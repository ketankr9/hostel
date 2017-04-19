from django.conf.urls import url,include
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns=[
 #edited
 #edited
 url(r'about/$',views.about,name="About us page"),
 url(r'index/$',views.index,name="Home page of each hostel"),
 url(r'contactus/$',views.contactus,name="Direct contact by messege"),
 url(r'contact/$',views.contact,name="Contacts in general"),
 url(r'grieverience/$',views.grieve,name="Grieverience page"),
 #url(r'login/(?P<num>[0-4]{0,1})/$',views.login,name="log in page"),
 url(r'^login/$',auth_views.login,{'template_name':'login.html'},name="log in page"),
 url(r'^logout/$',auth_views.logout,{'next_page':'/'},name="logout"),
 # url(r'^discussion/(?P<num>[0-4]{1})/$',views.discussion,name="Discussion with group"),
 # url(r'registration/$',views.register2,name="Registeration"),
 url(r'registration/(?P<num>[0-9]{1,2})/$',views.register3,name="Registeration"),
 url(r'studentprofile/(?P<roll>[0-9]{8})/$',views.studprofile,name="Student profile"),
 url(r'messMonthly/$',views.messbill,name='Mess bill'),
 url(r'policy/$',views.policy,name="Hostel policy page"),
 url(r'signup/$',views.signup,name="Sign up page"),
 # url(r'downloadForm',views.createPDF, name='index'),
 url(r'^$',views.index, name='index'),
url(r'^',views.defaultPage, name='index'),

 ]
