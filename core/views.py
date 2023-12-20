from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import DiasUteis, Frequencia, Usuario
from .forms import CalculadoraForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class CalculadoraView(FormView):
    template_name = 'calculadora.html'
    form_class = CalculadoraForm
    success_url = reverse_lazy('calculadora')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)


    def form_valid(self, form, *args, **kwargs):
        homeoffice = form.cleaned_data['homeoffice']
        faltas = form.cleaned_data['faltas']
        mes = form.cleaned_data['mes_referencia']

        #


        messages.success(self.request, 'Calculo Realizado')

        return super(CalculadoraView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Favor informar números inteiros nos formulários')

        return super(CalculadoraView, self).form_valid(form, *args, **kwargs)