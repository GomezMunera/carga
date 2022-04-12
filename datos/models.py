from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Vehiculo(models.Model):
    placa = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    peso_inicial = models.FloatField(default=0.0)
    dato_inscripcion = models.DateTimeField('Inscripción vehículo')

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    dato_registro = models.DateTimeField('Fecha')
    peso_neto = models.FloatField(default = 0.0)
    # peso carga = neto - inicial
    peso_carga = models.FloatField(default = 0.0) 

    def __str__(self):
        return self.dato_registro.strftime("%Y/%m/%d %H:%M:%S")

@receiver(post_save, sender=Registro)
def calcular_carga(sender, instance, created, **kwargs):
    if created:
        instance.peso_carga = instance.peso_neto - instance.vehiculo.peso_inicial
        instance.save()
