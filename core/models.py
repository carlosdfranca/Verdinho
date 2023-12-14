from django.db import models


MESES = (
    (1, 'Janeiro'),
    (2, 'Fevereiro'),
    (3, 'Março'),
    (4, 'Abril'),
    (5, 'Maio'),
    (6, 'Junho'),
    (7, 'Julho'),
    (8, 'Agosto'),
    (9, 'Setembro'),
    (10, 'Outubro'),
    (11, 'Novembro'),
    (12, 'Dezembro')
)


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
    cor_grafico = models.CharField('Cor no Gráfico', max_length=7, default='#000000')

    def __str__(self):
        return self.nome
    

class DiasUteis(Base):
    mes = models.IntegerField('Mes', choices=MESES, default= 1)
    ano = models.IntegerField('Ano', default=2024)
    qtd_du = models.IntegerField('Dias Úteis')

    def __str__(self):
        return f'{self.mes}/`{self.ano}'
    

class Frequencia(Base):
    usuario = models.ForeignKey('core.Equipe', verbose_name='Usuário', on_delete=models.CASCADE)
    mes_referencia = models.IntegerField('Mes', choices=MESES, default=1)
    ano_referencia = models.IntegerField('Ano', default=2024)
    qtd_home_office = models.IntegerField("Quantidade de Home Office")
    qtd_faltas = models.IntegerField("Quantidade de Faltas")

    def __str__(self):
        return f'{self.usuario} - {self.mes_referencia}/{self.ano_referencia}'