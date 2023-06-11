from django.urls import include, path
from django.conf.urls.static import static
from cookblock import settings
from . import views

app_name = "landing"

urlpatterns = [
    path('', views.landing, name='landing_page'),
    path('autenticacion/', views.autenticacion, name='login'),
    path('registro/', views.registro, name='registro'),
    path('profile/', views.profile, name='profile'),
    
] 
