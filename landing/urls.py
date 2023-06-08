from django.urls import include, path
from django.conf.urls.static import static
from cookblock import settings
# from .views import landing_page, login_view, register, profile, logout_view
from . import views

app_name = "landing"

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # path('mainpage/', include('cookweb.urls', namespace='cookweb')),

] 
