from django.urls import path
from . import views

app_name = 'cookweb'

urlpatterns = [
    path('mainpage/', views.index, name='mainpage'),
    # Otras rutas URL de la aplicación 'cookweb'
]
