from django.urls import path
from . import views

app_name = 'cookweb'

urlpatterns = [
    path('', views.index, name='index'),
    # Otras rutas URL de la aplicación 'cookweb'
]
