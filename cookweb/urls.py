from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from cookweb import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('cookies/', views.cookies, name='cookies'),
    path('about/', views.about, name='about'),


]