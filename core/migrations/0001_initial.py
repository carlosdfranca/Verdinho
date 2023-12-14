# Generated by Django 5.0 on 2023-12-13 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DiasUteis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("criado", models.DateField(auto_now_add=True, verbose_name="Criação")),
                ("modificado", models.DateField(auto_now=True, verbose_name="Criação")),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                ("ano_mes", models.CharField(max_length=20, verbose_name="Ano - Mês")),
                ("qtd_du", models.IntegerField(verbose_name="Dias Úteis")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Equipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("criado", models.DateField(auto_now_add=True, verbose_name="Criação")),
                ("modificado", models.DateField(auto_now=True, verbose_name="Criação")),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "vr_dia",
                    models.DecimalField(
                        decimal_places=2,
                        default=45.0,
                        max_digits=2,
                        verbose_name="Vale Refeição",
                    ),
                ),
                (
                    "vt_dia",
                    models.DecimalField(
                        decimal_places=2, max_digits=2, verbose_name="Vale Transporte"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Frequencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("criado", models.DateField(auto_now_add=True, verbose_name="Criação")),
                ("modificado", models.DateField(auto_now=True, verbose_name="Criação")),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                (
                    "qtd_home_office",
                    models.IntegerField(verbose_name="Quantidade de Home Office"),
                ),
                (
                    "qtd_faltas",
                    models.IntegerField(verbose_name="Quantidade de Faltas"),
                ),
                (
                    "mes_referencia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.diasuteis",
                        verbose_name="Mês de referência",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.equipe",
                        verbose_name="Usuário",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]