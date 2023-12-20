from django.urls import path

from .views import IndexView, CalculadoraView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('calculadora', CalculadoraView.as_view(), name='calculadora')
]