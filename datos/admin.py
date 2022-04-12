from django.contrib import admin

from .models import Vehiculo, Registro, Configuracion

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Registro)
admin.site.register(Configuracion)