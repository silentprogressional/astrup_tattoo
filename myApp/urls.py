from django.contrib import admin
from django.urls import path, include
from myApp import views

urlpatterns = [

    path('user_login', views.user_login, name='login'),

]