from django.shortcuts import render
from myApp.models import Users
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'myApp/index.html')


@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def aboutus(request):
    return render(request, 'myApp/aboutus.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account is not active')
        else:
            print('Someone tried to login and failed')
            print(f'username: {username}')
            return HttpResponse('invalid login credentials')
        return render(request, 'myApp/user_login.html')






