from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('MainPage')

def about(request):
    return render(request, 'about.html')

def cookies(request):
    return render(request, 'cookies.html')

def my_profile(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        
def profile(request):
    return render(request, 'profile.html')