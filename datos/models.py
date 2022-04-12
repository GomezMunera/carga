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
    tara = models.FloatField(default=0.0)
    fecha = models.DateTimeField('Inscripción vehículo')

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha')
    peso_neto = models.FloatField(default = 0.0)
    # peso carga = neto - inicial
    peso_carga = models.FloatField(default = 0.0) 

    def __str__(self):
        return self.fecha.strftime("%Y/%m/%d %H:%M:%S")

@receiver(post_save, sender=Registro)
def calcular_carga(sender, instance, created, **kwargs):
    if created:
        instance.peso_carga = instance.peso_neto - instance.vehiculo.tara
        instance.save()

class Configuracion(models.Model):
    VELOCIDAD_BAUDIOS = (
        ('1200', '1200'),
        ('2400', '2400'),
        ('4800', '4800'),
        ('9600', '9600'),
        ('19200', '19200'),
        ('38400', '38400'),
        ('115200', '115200'),
    )
    lectura = models.FloatField(default=0.0)
    puerto = models.CharField(max_length=255)
    velocidad = models.CharField(max_length=6, choices=VELOCIDAD_BAUDIOS)

    def __str__(self):
        return 'Puerto: '+self.puerto +', Velocidad: ' + self.velocidad

    class Meta:
        verbose_name_plural='Configuraciones'