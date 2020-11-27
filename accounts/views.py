from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken !')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This is an account with this email !')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=password,
                    )
                    user.save()
                    messages.success(request, 'You are now registered and can log in !')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match !')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(
        user_id=request.user.id
    )

    context = { 'contacts': user_contacts }
    return render(request, 'accounts/dashboard.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in! find your dream property.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out!!')
        return redirect('index')
