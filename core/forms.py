from django import forms



class CalculadoraForm(forms.Form):
    homeoffice = forms.IntegerField(label='Dias de home office')
    faltas = forms.IntegerField(label='Número de faltas')
    mes_referencia = forms.IntegerField(label="Mês de referência")
    ano_referencia = forms.IntegerField(label="Ano")


# class LoginForm(AuthenticationForm):
#     # Adicione campos adicionais, se necessário