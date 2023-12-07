# Generated by Django 4.2.5 on 2023-12-07 22:25

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo', max_length=50, verbose_name='Nome')),
                ('fone', models.CharField(help_text='Número de telefone - ex: (00)12345-6789', max_length=14, unique=True, verbose_name='Telefone')),
                ('email', models.EmailField(help_text='Endereço de E-mail', max_length=100, unique=True, verbose_name='E-mail')),
                ('funcao', models.CharField(help_text='Função desenvolvida pelo funcionario', max_length=35, verbose_name='Função')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'ordering': [django.db.models.functions.text.Upper('nome')],
            },
        ),
    ]
