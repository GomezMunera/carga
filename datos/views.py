from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
#from django.template import loader
from django.http import Http404

# call the models
from .models import Vehiculo, Registro

# Create your views here.
# index create without shorcut
""" 
def index(request):
    latest_vehiculo_list = Vehiculo.objects.order_by('-fecha')[:5]
    template = loader.get_template('datos/datos.html')
    context = {
        'latest_vehiculo_list': latest_vehiculo_list,
    }
    return HttpResponse(template.render(context,request))
"""

# index create with shortcut, is necessary obtain the context and import render
def index(request):
    latest_vehiculo_list = Vehiculo.objects.order_by('fecha').reverse()[:10] # muestra el último
    context = {'latest_vehiculo_list':latest_vehiculo_list}
    return render(request, 'datos/index.html', context)

# detail without shortcut
"""
def detail(request, vehiculo_id):
    try:
        vehiculo = Vehiculo.objects.get(pk=vehiculo_id)
    except Vehiculo.DoesNotExist:
        raise Http404("El Vehículo no esta registrado")
    return render(request, 'datos/details.html', {'vehiculo':vehiculo})
"""
# detail with shortcut error 404
def detail(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    return render(request,'datos/detail.html',{'vehiculo':vehiculo})
    #lates_register_list = Vehiculo.objects.order_by('fecha').reverse()
    #return render(request,'datos/detail.html',{'lates_register_list':lates_register_list})

def results(request, registro_id):
    #response = "Vista del resultado del vehiculo %s."
    #return HttpResponse(response % vehiculo_id)
    registro = get_object_or_404(Registro, pk=registro_id)
    return render(request,'datos/register.html',{'registro':registro})

def vote(request, vehiculo_id):
    response = "Votación por el vehículo %s."
    return HttpResponse(response % vehiculo_id)
