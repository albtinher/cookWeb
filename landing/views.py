from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def landing_page(request):
    return render(request, 'landing/landingPage.html')


def login_view(request):
    error_message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cookweb:mainpage')
        else:
            error_message = 'Credenciales inválidas'
    else:
        form = AuthenticationForm()
    return render(request, 'landing/login.html', {'form': form, 'error_message': error_message})



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)
            return redirect('landing:login')  # Redirecciona a la página de inicio de sesión
    else:
        form = CustomUserCreationForm()
    return render(request, 'landing/register.html', {'form': form})





@login_required
def profile(request):
    return render(request, 'landing/profile.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('landing/landingPage.html')

