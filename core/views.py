from django.shortcuts import render
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


import locale
import calendar
from datetime import datetime


from .models import DiasUteis, Frequencia
from .forms import CalculadoraForm

# Create your views here.

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):

    #     locale.setlocale(locale.LC_TIME, 'pt_BR')

    #     frequencias = Frequencia.objects.filter(usuario=request.user, ano_referencia=2023).order_by('mes_referencia')
    #     dias_uteis = DiasUteis.objects.filter(ano=2023)

    #     beneficios = []
    #     meses = []

    #     for frequencia in frequencias:
    #         dias_trabalhados = dias_uteis.get(mes=frequencia.mes_referencia).qtd_du - frequencia.qtd_faltas
    #         vr_mes = request.user.vr_dia * dias_trabalhados
    #         vt_mes = request.user.vt_dia * (dias_trabalhados - frequencia.qtd_home_office)
    #         beneficio = vr_mes + vt_mes

    #         beneficios.append(float(beneficio))

    #         mes = calendar.month_name[frequencia.mes_referencia]

    #         meses.append(mes)
        

    #     ultimo_beneficio = beneficios[-1]
    #     ultimo_mes = meses[-1]

    #     ultimo_beneficio = "{:.2f}".format(ultimo_beneficio)
        

    #     context = {
    #         'beneficios': beneficios,
    #         'meses': meses,
    #         'ultimo_beneficio': ultimo_beneficio,
    #         'ultimo_mes': ultimo_mes
    #     }

    #     return render(request, self.template_name, context)
    


class CalculadoraView(LoginRequiredMixin, FormView):
    template_name = 'calculadora.html'
    form_class = CalculadoraForm
    success_url = reverse_lazy('calculadora')

    def is_user_in_group(user, group_name):
        return user.is_authenticated and user.groups.filter(name=group_name).exists()

    def form_valid(self, form, *args, **kwargs):
        # Obtenha os valores do formulário
        homeoffice = form.cleaned_data['homeoffice']
        faltas = form.cleaned_data['faltas']
        mes_referencia = form.cleaned_data['mes_referencia']
        ano_referencia = form.cleaned_data['ano_referencia']

        # Obtenha o usuário logado
        usuario = self.request.user

        # Obtenha os valores do modelo Usuario
        vr_dia = usuario.vr_dia
        vt_dia = usuario.vt_dia

        # Obtenha os valores do modelo DiasUteis
        dias_uteis = DiasUteis.objects.filter(mes=mes_referencia, ano=ano_referencia).first()

        if dias_uteis:
            # Calcule os valores
            dias_trabalhados = dias_uteis.qtd_du - faltas
            vr_mes = vr_dia * dias_trabalhados
            vt_mes = vt_dia * (dias_trabalhados - homeoffice)
            beneficio = vr_mes + vt_mes

            # Configurar a formatação de números
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

            # Formatando os valores
            vr_mes_formatado = locale.currency(vr_mes, grouping=True, symbol=None)
            vt_mes_formatado = locale.currency(vt_mes, grouping=True, symbol=None)
            beneficio_formatado = locale.currency(beneficio, grouping=True, symbol=None)

            # Adicione os valores ao contexto do template
            context = self.get_context_data(form=form)
            context['vr_mes'] = vr_mes_formatado
            context['vt_mes'] = vt_mes_formatado
            context['beneficio'] = beneficio_formatado

            messages.success(self.request, 'Cálculo realizado com sucesso! ')

            return self.render_to_response(context)
        
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Favor informar números inteiros nos formulários')

        return super(CalculadoraView, self).form_valid(form, *args, **kwargs)
    

class User(LoginRequiredMixin, TemplateView):
    template_name = 'user.html'
