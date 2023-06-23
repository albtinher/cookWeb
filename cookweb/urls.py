from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from cookweb import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('cookies/', views.cookies, name='cookies'),
    path('about/', views.about, name='about'),
    path('websites/', views.websites, name='websites'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/config/', views.configuraciones, name='configuraciones'),
    path('generar-deshabilitacion-cookies/', views.generar_archivo_deshabilitacion, name='generar_deshabilitacion_cookies'),



]