from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import User
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy  as _
# Create your models here.

class User(AbstractUser):
    username = None
    id = models.CharField(primary_key= True, max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100, null=True)

    token = models.CharField(max_length=255, null= True)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager() 
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email