from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.sessions.models import Session
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.core.paginator import Paginator

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
        records = []
        if request.user.is_authenticated:
            try:
                records_list = Record.objects.all().order_by('id')
                paginator = Paginator(records_list, 10)
                page = request.GET.get('page')
                records = paginator.get_page(page)
            except Exception as _:
                messages.error(request, "Error fetching records")
    
        return render(request, 'home.html', { 'records': records})

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

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Error during registration. Please try again.")
                return redirect('register')
            
            login(request, user)
            messages.success(request, "You have successfully registered! Welcome")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

@require_http_methods(["GET"])
def customer_record(request, pk):
    if request.user.is_authenticated:
        try:
            customer_record = Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record': customer_record})
        except Record.DoesNotExist:
            messages.error(request, "Record not found.")
            return redirect('home')
        
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect('home')    

@require_POST
@login_required
def delete_record(request, pk):
    try:
        delete_it =  Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Customer record deleted successfully")
        return redirect('home')
    except Record.DoesNotExist:
        messages.error(request, "Record not found")
        return redirect('home') 
    except Exception as _:
        messages.error(request, "An error occurred while deleting the record")
        return redirect('home')

@require_http_methods(["GET", "POST"])
@login_required
def add_record(request):
    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Added Successfully")
            return redirect('home')
        messages.error(request, "Please correct the errors below")
    else:
        form = AddRecordForm()
        return render(request, 'add_record.html', {'form': form})
    
    return render(request, 'add_record.html', {'form': form})
