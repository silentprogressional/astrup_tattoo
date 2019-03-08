from django.shortcuts import render

from myApp import sendEmail, models
from myApp.models import Users, Contacts, Posts ,Comments
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import string
import random
import datetime

# Create your views here.


@login_required()
def adminPage(request):
    return render(request, 'myApp/adminPage.html')


@csrf_exempt
def addComment(request):
    try:
        commenttext = request.POST.get('comment')
        name = request.POST.get('name')
        postid = request.POST.get('postid')
        today = str(datetime.datetime.today()).split()[0].split('-')
        commentedOn = f"{today[2]}/{today[1]}/{today[0]}"
        comment = models.Comments.objects.create(commenter=name, commentDate=commentedOn,
                                                 comment=commenttext, post=models.Posts.objects.get(pk=postid))
        comment.save()
        return HttpResponse('')
    except Exception as a:
        return render(request, 'myApp/errorpage.html', context={'error': a})


def blogPage(request):
    try:
        posts = models.Posts.objects.all()
        return render(request, 'myApp/blogPage.html', context={'posts': posts})
    except Exception as a:
        return render(request, 'myApp/errorPageAdmin.html', context={'error': a})


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class addPost(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myApp/addPost.html')

    def post(self, request, *args, **kwargs):
        try:
            today = str(datetime.datetime.today()).split()[0].split('-')
            publishedOn = f"{today[2]}/{today[1]}/{today[0]}"
            post = models.Posts.objects.create(title=request.POST.get('title'), beginning=request.POST.get('start'),
                                               main=request.POST.get('main'), author=request.user,
                                               pubdate=publishedOn, category=request.POST.get('category'),
                                               postPic="static/myApp/media/postPics/" + request.POST.get('image'))
            post.save()
            return HttpResponse('')
        except Exception as a:
            return render(request, 'myApp/errorPageAdmin.html', context={'error': a})


def postPage(request):
    try:
        postnumber = int(request.GET.get('postid'))
        post = models.Posts.objects.get(pk=postnumber)
        author = models.Users.objects.get(pk=post.author_id)
        comment = models.Comments.objects.filter(post_id=post.id)
        return render(request, 'myApp/postPage.html', context={'post': post, 'author': author, 'comment': comment})
    except Exception as a:
        return render(request, 'myApp/errorpage.html', context={'error': a})


def index(request):
    return render(request, 'myApp/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class forgotPass(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myApp/forgotPass.html')

    def post(self, request, *args, **kwargs):
        try:
            email = request.POST.get('email')
            record = models.Users.objects.get(email=email)
            letters = string.ascii_lowercase
            newpass = ''.join(random.choice(letters) for i in range(10))

            record.set_password(newpass)
            record.save()
            body = f"Your new password is: {newpass}"
            sendEmail.sendmail(body, target=record.email)
            return render(request, 'myApp/passwordChangeSuccess.html', context={'email': record.email})
        except Exception as a:
            return render(request, 'myApp/errorPageAdmin.html', context={'error': a})


class userLogin(TemplateView):

    def post(self, request, *args, **kwargs):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('adminPage'))
                else:
                    return HttpResponse('Account is not active')
            else:
                print('Someone tried to login and failed')
                print(f'username: {username}')
                return HttpResponse('invalid login credentials')
        except Exception as a:
            return render(request, 'myApp/errorPageAdmin.html', context={'error': a})

    def get(self, request, *args, **kwargs):
        return render(request, 'myApp/user_login.html')


@method_decorator(login_required, name='dispatch')
class formView(View):
    form = forms.UserForm

    def post(self, request, *args, **kwargs):
        form = forms.UserForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                cli_addr = request.META.get('REMOTE_ADDR')

                try:
                    record = Users.objects.get(email=form.cleaned_data['email'])
                    record = "This email address already exist"
                    return render(request, 'myApp/errorPageAdmin.html', context={'error': record})
                except Users.DoesNotExist:
                    user = form.save(commit=False)
                    user.set_password(user.password)
                    user.loginIp = cli_addr
                    user.save()
                    return render(request, 'myApp/successpage.html', context={'username': form.cleaned_data['username']})
            except Exception as a:
                return render(request, 'myApp/errorPageAdmin.html', context={'error': a})
        else:
            return render(request, 'myApp/errorPageAdmin.html', context={'error': form.errors})

    def get(self, request, *args, **kwargs):
        form = self.form
        return render(request, 'myApp/register.html', context={'form': form})


#to disable csrf token


@method_decorator(csrf_exempt, name='dispatch')
class contactView(View):

    def post(self, request, *args, **kwargs):
        try:
            contact = Contacts.objects.create(username=request.POST.get('name'), email=request.POST.get('email'),
                                              phoneNumber=request.POST.get('phone'),
                                              message=request.POST.get('message'))
            sendEmail.sendmail(body=contact.message + '\nFrom: ' + contact.email +
                                    f'\nName: {contact.username}'+ f'\nPhone: {contact.phoneNumber}')
            contact.save()
            return render(request, 'myApp/successpage.html')
        except Exception as a:
            return render(request, 'myApp/errorpage.html', context={'error': a})








