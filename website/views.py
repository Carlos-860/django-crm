from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.sessions.models import Session

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

@require_POST
@login_required
def logout_user(request): # appended with _user in order to not conflict
     # Invalidate all sessions for the current user
    user_sessions = Session.objects.filter(session_data__contains=request.user.pk)
    user_sessions.delete()
    logout(request)
    messages.success(request, "You have been logged out..." )
    return redirect('home')
