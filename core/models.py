from django.db import models

# Create your models here.
class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Criação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
    

class Equipe(Base):
    nome = models.CharField('Nome', max_length=100, null=False)
    vr_dia = models.DecimalField('Vale Refeição',max_digits=5, decimal_places=2, default=45.00, null=False)
    vt_dia = models.DecimalField('Vale Transporte', max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return self.nome
    

class DiasUteis(Base):
    ano_mes = models.CharField('Ano - Mês', max_length=20)
    qtd_du = models.IntegerField('Dias Úteis')

    def __str__(self):
        return self.ano_mes
    

class Frequencia(Base):
    usuario = models.ForeignKey('core.Equipe', verbose_name='Usuário', on_delete=models.CASCADE)
    mes_referencia = models.ForeignKey('core.DiasUteis', verbose_name='Mês de referência', on_delete=models.CASCADE)
    qtd_home_office = models.IntegerField("Quantidade de Home Office")
    qtd_faltas = models.IntegerField("Quantidade de Faltas")

    def __str__(self):
        return f'{self.mes_referencia} - {self.mes_referencia}'