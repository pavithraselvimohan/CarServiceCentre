from xml.etree.ElementInclude import include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home),
   path('aboutus/',views.aboutus),
   path('offers/',views.offers),
   path('doorstep/',views.doorstep),
   path('contactus/',views.contactus),
   path('login/',views.login),
   path('login/register/',views.register),
   
   
]
urlpatterns += staticfiles_urlpatterns() 
