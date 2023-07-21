from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import User
import re 

# Create your models here.
class RegisterForm(forms.Form):
    username= forms.CharField(max_length=12, widget=forms.TextInput(attrs = {
        'class':'field',
        'placeholder':'Username',
        'id':'username'
        
        }))
    password1 = forms.CharField(max_length=16, widget=forms.TextInput(attrs = {
        'class':'field',
        'placeholder':'Passwrod',
        'id':'password1'
        }))
    password2 = forms.CharField(max_length=16, widget=forms.TextInput(attrs = {
        'class':'field',
        'placeholder':'Password Confirmation',
        'id':'password2'
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs = {
        'class':'field',
        'placeholder':'Email',
        'id':'email'
        }))
    
    class Meta:
      model = User
      fields = ['username','email','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        if username.find(' ') != -1:
            raise forms.ValidationError("Space is not allowed in username")
            
        return username
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Invalid email format")
        r = User.objects.filter(email=email)
        if r.count():
            raise forms.ValidationError("Email address already registered")
        return email
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("Password must contain at least 8 characters")
        return password1
    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')
        if password2 != password1:
            raise forms.ValidationError('Passwords Not Match')
        return password2
        
    def save(self):
        user =User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('password1'),
            self.cleaned_data.get('email')
        )
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=12, widget=forms.TextInput(attrs = {
        'class':'field',
        'placeholder':'Username',
        'id':'username'
        }))
    password = forms.CharField(max_length=16, widget=forms.TextInput(attrs = {
        'class':'field',
        'placeholder':'Password',
        'id':'password'
        }))
    
    class Meta():
        model = User
        fields = ['username', 'password']