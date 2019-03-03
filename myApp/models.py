from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):

    phoneNumber = models.CharField(max_length=14)
    about = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='static/myApp/media/adminAvatars/')
    loginIp = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Contacts(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=14)
    message = models.CharField(max_length=500)


class Posts(models.Model):
    title = models.CharField(max_length=200, default=None)
    beginning = models.CharField(max_length=500, default=None)
    main = models.CharField(max_length=200000, default=None)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    pubdate = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.CharField(max_length=100)
    postPic = models.ImageField(upload_to="static/myApp/media/postPics/")


class Comments(models.Model):
    commenter = models.CharField(max_length=50)
    commentDate = models.DateTimeField(auto_now_add=True, blank=True)
    comment = models.CharField(max_length=500, default=None)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

