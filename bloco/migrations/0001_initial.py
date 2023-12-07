# Generated by Django 4.2.5 on 2023-12-07 22:25

import django.core.validators
from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome ou código do bloco', max_length=10, unique=True, verbose_name='Nome')),
                ('andares', models.DecimalField(decimal_places=0, default=1, help_text='Número de andares do bloco', max_digits=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='Andares')),
            ],
            options={
                'verbose_name': 'Bloco',
                'verbose_name_plural': 'Blocos',
                'ordering': [django.db.models.functions.text.Upper('nome')],
            },
        ),
    ]
