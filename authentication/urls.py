from django.contrib import admin
from django.urls import path, include
from .views import registro, cerrar_sesion,autenticacion

urlpatterns = [
    path('registro/',registro, name="Registro"),
    path('cerrar_sesion/',cerrar_sesion, name="Cerrar_sesion" ),
    path('',autenticacion, name="Autenticacion"),


]
