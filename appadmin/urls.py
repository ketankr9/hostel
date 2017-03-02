from django.conf.urls import url,include
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns=[
 url(r'^$',views.index2,name="Home page of each hostel"),
 url(r'contactus/$',views.contactus,name="Contacts of each hostel"),

 ]
