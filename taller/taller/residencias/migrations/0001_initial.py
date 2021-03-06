# Generated by Django 4.0.5 on 2022-06-29 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePropietario', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=100)),
                ('nroCuartos', models.IntegerField(verbose_name='Numero de cuartos')),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='residencias.edificio')),
            ],
        ),
    ]
