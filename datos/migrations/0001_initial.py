# Generated by Django 4.0.2 on 2022-03-08 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('peso_ini', models.FloatField(default=0.0)),
                ('dato_inscripcion', models.DateTimeField(verbose_name='Inscripción vehículo')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dato_registro', models.DateTimeField(verbose_name='Fecha')),
                ('peso_neto', models.FloatField(default=0.0)),
                ('peso_carga', models.FloatField(default=0.0)),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.vehiculo')),
            ],
        ),
    ]