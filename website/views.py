from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            messages.error(request, "Please provide both username and password") 
            return redirect('home')

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in. Please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request): # appended with _user in order to not conflict
    pass

def logout_user(request): # appended with _user in order to not conflict
    pass