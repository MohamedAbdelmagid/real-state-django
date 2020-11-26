from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        messages.error(request, 'TEST ERROR MESSAGE')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')
