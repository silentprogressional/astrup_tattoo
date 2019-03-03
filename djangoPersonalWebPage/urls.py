"""djangoPersonalWebPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('logout', views.user_logout, name='logout'),
    path('userLogin', views.userLogin.as_view(), name='login'),
    path('formView', views.formView.as_view(), name='register'),
    path('contactView', views.contactView.as_view(), name='contact'),
    path('forgotPass', views.forgotPass.as_view(), name='forgot'),
    path('blogPage', views.blogPage, name='blogPage'),
    path('postPage', views.postPage, name='postPage'),
    path('adminPage', views.adminPage, name='adminPage'),
    path('addComment', views.addComment, name='addComment'),
    path('addPost', views.addPost.as_view(), name='addPost'),
    path('myApp/', include('myApp.urls')),

]
