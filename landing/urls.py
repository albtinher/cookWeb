from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from landing import views

urlpatterns = [
    
    path('', views.landing, name='MainPage'),
    path('auth/', views.auth, name='AuthPage'),
    path('auth/register/', views.register, name='RegisterPage'),
    path('auth/logout/', views.logout, name='LogOutPage'),

]