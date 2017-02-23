from django.conf.urls import url,include
from myapp import views

urlpatterns=[
 url(r'index2/$',views.index2,name="Home page of each hostel"),
 url(r'contactus/$',views.contactus,name="Contacts of each hostel"),
 url(r'grieverience/$',views.grieve,name="Grieverience page"),
 url(r'login/(?P<w>[0-4]{0,1})/$',views.loginu,name="log in page"),
 url(r'^discussion/(?P<num>[0-4]{1})/$',views.discussion,name="Discussion with group"),
 url(r'registeration/$',views.register,name="Sign up"),
 url(r'studprofile/(?P<roll>[0-9]{8})/$',views.studprofile,name="student profile"),
 url(r'pastrecruits/$',views.past,name='Past Recruits'),
 url(r'^$',views.index, name='index'),
 ]
