
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('landing.urls')),
    path('cookweb/', include('cookweb.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
