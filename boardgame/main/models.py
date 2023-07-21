from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils import timezone




class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    date_created  = models.TimeField(default=timezone.now)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ('email','password')
    objects = CustomUserManager()
    def __str__(self):
        return self.username


class Profile(models.Model):
    userRelated = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=320,default='')
    image = models.ImageField(upload_to='profile_pics', default='default.png')
    age = models.CharField(max_length=3,default='None')
    sex = models.CharField(max_length=5,default='None')

    def __str__(self):
        return self.userRelated.username+"'s profile"
