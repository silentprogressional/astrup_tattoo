from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):

    phoneNumber = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='media')
    loginIp = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Contacts(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=14)
    message = models.CharField(max_length=500)
