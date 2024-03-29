from django import forms
from django.forms import PasswordInput
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class FormularioRegistro(forms.Form):
    username = forms.CharField(max_length=20, label="Nombre de usuario:")
    name = forms.CharField(max_length=50, label="Nombre:")
    surname = forms.CharField(max_length=50, label="Apellidos:")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=PasswordInput, label="Contraseña", min_length=8)
    password_repeat = forms.CharField(widget=PasswordInput, label="Repita su contraseña")

class FormularioAutenticacion(forms.Form):
    username = forms.CharField(max_length=50, label="Nombre de usuario o Email:")
    password = forms.CharField(widget=PasswordInput, label="Contraseña", min_length=8)

