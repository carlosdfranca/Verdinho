from django import forms


class CalculadoraForm(forms.Form):
    homeoffice = forms.IntegerField(label='Dias de home office')
    faltas = forms.IntegerField(label='Número de faltas')
    mes_referencia = forms.IntegerField(label='Mês de Referência')