from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from djangoPersonalWebPage.settings import MEDIA_ROOT


class Users(AbstractUser):

    phoneNumber = models.CharField(max_length=14)
    about = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="adminAvatars")
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
    pubdate = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    postPic = models.ImageField(upload_to="postPics")


class Comments(models.Model):
    commenter = models.CharField(max_length=50)
    commentDate = models.CharField(max_length=50)
    comment = models.CharField(max_length=500, default=None)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

