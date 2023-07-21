from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class UserRegister(UserCreationForm):
    list_clasa = [(1,'دهم'),(2,'یازدهم'),(3,'دوازدهم')]
    Email = forms.EmailField(required=False)
    Class = forms.ChoiceField(choices=list_clasa)
    class Meta():
        
        model = User
        fields = ['username','Email','password1','password2','Class']

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(default = 'default.jpg',upload_to='profiles_pics')
    bio = models.CharField(max_length= 250)
    
    def __str__(self) :
        return f'{self.user.username}\'s profile'
