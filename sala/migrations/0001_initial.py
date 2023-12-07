# Generated by Django 4.2.5 on 2023-12-07 22:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bloco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('andar', models.DecimalField(decimal_places=0, default=1, help_text='Número do andar da Sala ou laboratório', max_digits=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='Andar')),
                ('numero', models.CharField(help_text='Identificação da sala ou laboratório', max_length=6, unique=True, verbose_name='numero')),
                ('uso', models.CharField(choices=[('Exclusivo', 'Exclusivo'), ('Comunitário', 'Comunitário')], help_text='Tipo de uso da Sala ou laboratório', max_length=11, verbose_name='uso')),
                ('bloco', models.ForeignKey(help_text='Bloco da Sala ou laboratório', on_delete=django.db.models.deletion.PROTECT, related_name='sala_bloco', to='bloco.bloco', verbose_name='Bloco')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'ordering': [django.db.models.functions.text.Upper('bloco')],
            },
        ),
    ]
