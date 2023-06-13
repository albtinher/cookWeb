from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cookies(request):
    return render(request, 'cookies.html')