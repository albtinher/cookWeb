from django.urls import path
from .views import landing_page, login_view, register, profile, logout_view

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
