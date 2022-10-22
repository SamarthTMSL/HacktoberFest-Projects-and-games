from django.contrib import admin
from django.urls import path,include
from registerapp import views
urlpatterns = [
   path('home/',views.home,name='home'), #create online page urls='home' name when use database then it call name=home 
path('index/',views.index),
path('register/',views.register),
path('update/',views.update),
path('search/',views.search),
]