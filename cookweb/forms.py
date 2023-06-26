from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import ConfiguracionCookie, URL


class UserProfileForm(forms.ModelForm):
    password = None  # Excluir el campo de contraseña original

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].required = False
        self.fields['new_password2'].required = False

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2



class CookieConfigurationForm(forms.ModelForm):
    class Meta:
        model = ConfiguracionCookie
        fields = ['nombre', 'categoriasActivas']
        
        
        
#WEBSITES
class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['url']