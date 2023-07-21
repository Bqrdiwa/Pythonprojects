from django.shortcuts import render, redirect
from .models import RegisterForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from main.models import User
# Create your views here.
def Register(request):
    context = {'title':'Register'}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            context['errors'] = 'None'
            user = form.save()
            login(request, user)
            
        else:
            errs = form.errors.as_data()
            errors = {}
            for error in errs.keys():
                errors[error] = list(errs[error][0])[0]
            context['errors'] = errors
        return JsonResponse(context)
    else:
        form = RegisterForm()
        context['form'] = form
        return render(request, 'authenticate/register.html', context)  

def Login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = username=request.POST['username']
        password = password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user != None:
            login(request,user)
            context['errors'] = 'None'
        else:
            context['errors'] = {'username':'Make sure that you enter the username and password currectly!'}

        return JsonResponse(context)
    else:
        form = LoginForm()
        context['form']= form
        return render(request, 'authenticate/login.html', context = context)
def Logout(request):
    logout(request)
    return redirect('auth-login')