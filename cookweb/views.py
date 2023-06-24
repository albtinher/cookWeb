from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ChangePasswordForm, CookieConfigurationForm, URLForm
from django.http import HttpResponse
from .models import ConfiguracionCookie, URL


def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('MainPage')


def about(request):
    return render(request, 'about.html')


def cookies(request):
    return render(request, 'cookies.html')

def websites(request):
    return render(request, 'websites.html')


def my_profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username


def profile(request):
    return render(request, 'profile.html')


@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        password_form = ChangePasswordForm(user=user, data=request.POST)

        if form.is_valid():
            form.save()  # Guardar los cambios en el perfil del usuario
            messages.success(request, 'Los cambios en el perfil se han guardado correctamente.')

            if password_form.has_changed() and password_form.is_valid():
                user.set_password(password_form.cleaned_data['new_password1'])
                update_session_auth_hash(request, user)  # Actualizar la sesión con la nueva contraseña
                user.save()
                messages.success(request, 'La contraseña se ha actualizado correctamente.')

            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
        password_form = ChangePasswordForm(user=user)

    return render(request, 'edit_profile.html', {'form': form, 'password_form': password_form})


def configuraciones(request):
    configuraciones = ConfiguracionCookie.objects.all()
    return render(request, 'configuraciones.html', {'configuraciones': configuraciones})



def cookie_configuration_view(request):
    if request.method == 'POST':
        form = CookieConfigurationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CookieConfigurationForm()

    configuraciones = ConfiguracionCookie.objects.all()

    return render(request, 'configuracioncookies/cookie_configuration.html', {'form': form, 'configuraciones': configuraciones})


def generar_archivo_deshabilitacion(request):
    preferencias = request.session.get('preferenciasCookies')

    contenido_archivo = f"disableCookies({preferencias})"  # Ejemplo de contenido de archivo

    nombre_archivo = 'deshabilitar_cookies.js'

    response = HttpResponse(content_type='application/javascript')
    response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
    response.write(contenido_archivo)

    return response



#WEBSITES

@login_required
def websites(request):
    form = URLForm(request.POST or None)
    urls = URL.objects.filter(user=request.user)
    
    if request.method == 'POST':
        if form.is_valid():
            url = form.save(commit=False)
            url.user = request.user
            url.save()
            return redirect('websites')
    
    context = {
        'form': form,
        'urls': urls
    }
    return render(request, 'websites.html', context)

@login_required
def delete_website(request, id):
    
    if(request.method == 'POST'):
        user = request.user
        url = get_object_or_404(URL, id=id)
        url.delete()
        return redirect('websites')
    
    return render(request, 'websites.html')




