from django.contrib import admin

from .models import Usuario, DiasUteis, Frequencia
from django.contrib.auth.admin import UserAdmin

# Register your models here.
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Valores Personalizáveis", {'fields': (
        'vr_dia',
        'vt_dia',
        'cor_grafico',
        )})
)

UserAdmin.fieldsets = tuple(campos)

@admin.register(DiasUteis)
class DiasUteisAdmin(admin.ModelAdmin):
    list_display = (
        'ano',
        'mes',
        'qtd_du'
    )


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'mes_referencia',
        'ano_referencia',
        'qtd_home_office',
        'qtd_faltas'
    )

class UsuaropAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email']  # Adicione os campos que deseja exibir na lista de usuários

admin.site.register(Usuario, UsuaropAdmin)
