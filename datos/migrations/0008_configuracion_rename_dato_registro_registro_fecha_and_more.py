# Generated by Django 4.0.3 on 2022-04-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0007_alter_registro_peso_carga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lectura', models.CharField(max_length=255)),
                ('puerto', models.CharField(max_length=255)),
                ('velocidad', models.CharField(choices=[('1200', '1200'), ('2400', '2400'), ('4800', '4800'), ('9600', '9600'), ('19200', '19200'), ('38400', '38400'), ('115200', '115200')], max_length=6)),
            ],
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='dato_registro',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='vehiculo',
            old_name='dato_inscripcion',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='vehiculo',
            old_name='peso_inicial',
            new_name='tara',
        ),
    ]