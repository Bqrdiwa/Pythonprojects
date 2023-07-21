from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import  login_required
from .models import UserRegister

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            usernam = form.cleaned_data.get('username')
            form.save()
            Us = User.objects.all().filter(username=usernam).first()
            messages.success(request,f'Account created for {usernam}! and your id is {Us.id}')
            return redirect('login')
    else:
        print(1)
        form = UserRegister()
    return render(request,'authenticate/register.html',{'form':form,'title':'Register'})

@login_required
def profile(request):
    return render(request,'authenticate/profile.html')