# Generated by Django 4.2 on 2025-03-09 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cars', '0004_alter_rentedcars_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterRentCarUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('day_use', models.IntegerField(blank=None, verbose_name='Quantidade de dias')),
                ('rent_date', models.DateTimeField(auto_now_add=True, verbose_name='Data do aluguel')),
                ('return_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de devolução')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cars.car', verbose_name='Carro Alugado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Registro de Locação',
                'verbose_name_plural': 'Registro de Locações',
            },
        ),
    ]
