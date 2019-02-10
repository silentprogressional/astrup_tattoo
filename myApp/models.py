from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):

    phoneNumber = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='media')
    loginIp = models.CharField(max_length=30)

    def __str__(self):
        return self.username
