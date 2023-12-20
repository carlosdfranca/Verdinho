from django.urls import path

from .views import IndexView, UsuarioView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('usuario', UsuarioView.as_view(), name='usuario')
]