from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    username = forms.CharField(required=True, label='Username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].error_messages = {'required': 'Please enter your email address.'}
        self.fields['username'].error_messages = {'required': 'Please enter a username.'}
        self.fields['password1'].error_messages = {'required': 'Please enter a password.'}
        self.fields['password2'].error_messages = {'required': 'Please confirm your password.'}

class FormularioUsuario(AuthenticationForm):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    
