from django.contrib import admin

from .models import Equipe, DiasUteis, Frequencia

# Register your models here.
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'vr_dia',
        'vt_dia'
    )

@admin.register(DiasUteis)
class DiasUteisAdmin(admin.ModelAdmin):
    list_display = (
        'ano_mes',
        'qtd_du'
    )


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'mes_referencia',
        'qtd_home_office',
        'qtd_faltas'
    )