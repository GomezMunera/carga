"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registro

@receiver(post_save, sender=Registro)
def calcular_carga(sender, instance, created, **kwargs):
    if created:
        instance.peso_carga = instance.peso_neto - instance.vehiculo.peso_inicial
        #instance.Registro.save()

post_save.connect(calcular_carga, sender=Registro)


@receiver(post_save, sender=Registro)
def save_carga(sender, instance, **kwargs):
    instance.Registro.save()
"""