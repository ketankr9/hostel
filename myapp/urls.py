from django.conf.urls import url,include
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns=[
 url(r'index2/$',views.index2,name="Home page of each hostel"),
 url(r'contactus/$',views.contactus,name="Contacts of each hostel"),
 url(r'grieverience/$',views.grieve,name="Grieverience page"),
 #url(r'login/(?P<num>[0-4]{0,1})/$',views.login,name="log in page"),
 url(r'^login/$',auth_views.login,{'template_name':'login.html'},name="log in page"),
 url(r'^logout/$',auth_views.logout,{'next_page':'/'},name="logout"),
 url(r'^discussion/(?P<num>[0-4]{1})/$',views.discussion,name="Discussion with group"),
 url(r'registeration/$',views.register,name="Registeration"),
 url(r'studentprofile/(?P<roll>[0-9]{8})/$',views.studprofile,name="Student profile"),
 url(r'messMonthly/$',views.messbill,name='Mess bill'),
 url(r'policy/$',views.policy,name="Hostel policy page"),
 url(r'signupp/$',views.signup,name="Sign up page"),
 url(r'^$',views.index, name='index'),
 ]
