from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'admin':
                return redirect('admin_dashboard')
            elif user.user_type == 'lawyer':
                return redirect('lawyer_dashboard')
            elif user.user_type == 'client':
                return redirect('client_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'admin':
                    return redirect('admin_dashboard')
                elif user.user_type == 'lawyer':
                    return redirect('lawyer_dashboard')
                elif user.user_type == 'client':
                    return redirect('client_dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def lawyer_dashboard(request):
    return render(request, 'lawyer_dashboard.html')

@login_required
def client_dashboard(request):
    return render(request, 'client_dashboard.html')
