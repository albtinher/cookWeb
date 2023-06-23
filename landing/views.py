from django.shortcuts import render, redirect
from .forms import FormularioRegistro, FormularioAutenticacion
from django.contrib.auth.models import User
from cookweb.views import home
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required


def landing(request):
    return render(request, 'mainPage.html')

def register(request):
    
    formulario = FormularioRegistro
    
    if request.method == 'POST':
        formulario = FormularioRegistro(data = request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get("username").upper()
            name = formulario.cleaned_data.get("name")
            surname = formulario.cleaned_data.get("surname")
            email = formulario.cleaned_data.get("email")
            password = formulario.cleaned_data.get("password")
            password_repeat = formulario.cleaned_data.get("password_repeat")

                
            if(password != password_repeat):
                messages.error(request,'La contraseña y su confirmación no coinciden ')
                return render(request,'register.html',{'formulario':formulario})
           
            if ' ' in username:
                messages.error(request,'El nombre de usuario no puede contener espacios')
                return render(request,'register.html',{'formulario':formulario})

            if User.objects.filter(email = email).exists():
                messages.error(request,'Este email ya esta registrado en nuestra base de datos, si ha olvidado su contraseña puede recuperarla.')
                return render(request,'register.html',{'formulario':formulario})
            
            if User.objects.filter(username = username).exists():
                messages.error(request,'El nombre de usuario' + username + 'ya esta en uso')
                return render(request,'register.html',{'formulario':formulario})
           
            user = User.objects.create_user(username, email, password)
            user.first_name = name
            user.last_name = surname
            user.save()
            
            login(request, user)
            return redirect(home)
        
        return render(request,'register.html',{'formulario':formulario})
    return render(request,'register.html',{'formulario':FormularioRegistro})


def auth(request):
    
    formulario = FormularioAutenticacion()
    
    if request.method == 'POST':
        formulario = FormularioAutenticacion(data = request.POST)
        if formulario.is_valid:
            username = request.POST.get("username")
            contra = request.POST.get("password")
            if("@" in username):
                if User.objects.filter(email = username).exists():
                    user = User.objects.get(email = username)
                    user_object = authenticate(username = user.username, password = contra)
                else:
                    user_object = None
            else:
                if User.objects.filter(username = username.upper()).exists():
                    user_object = authenticate(username = username.upper(), password = contra)
                else:
                    user_object = None
            
            if user_object is not None:
                login(request,user_object)
  
                return redirect(home)
            else:
                messages.error(request,'Vaya, las credenciales no son correctas. Si ha olvidado su contraseña puede restaurarla.')
                return render(request,'login.html',{'formulario':FormularioAutenticacion})
    return render(request,'login.html',{'formulario':FormularioAutenticacion})




def authOut(request):
    logout(request)
    return redirect(home)