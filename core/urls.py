from django.urls import path
from .views import IndexView, CalculadoraView, User
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('calculadora/', CalculadoraView.as_view(), name='calculadora'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('usuario/', User.as_view(), name='user')
]