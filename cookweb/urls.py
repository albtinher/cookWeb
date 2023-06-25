from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from cookweb import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('cookies/', views.getCategorias, name='cookies'),
    path('about/', views.about, name='about'),
    path('configCreada/', views.post_configuraciones, name='configuracion_cookie_create'),
    path('websites/', views.websites, name='websites'),
    path('delete_website/<int:id>/', views.delete_website, name='delete_website'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/config/', views.configuraciones, name='configuraciones'),
    path('aprofile/config/activo/<int:configuracion_id>/', views.post_activo, name='activar_desactivar'),
    path('generar-deshabilitacion-cookies/', views.generar_archivo_deshabilitacion, name='generar_deshabilitacion_cookies'),



]