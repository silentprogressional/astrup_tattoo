from django.urls import path
from myApp import views


urlpatterns = [

    path('userLogin', views.userLogin.as_view(), name='login'),
    path('formView', views.formView.as_view()),

]