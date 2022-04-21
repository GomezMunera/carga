from django.urls import path

from datos import comunicacion
from . import views
from . import comunicacion

#  How does Django differentiate URL names from each other? answer: with app_name

app_name = 'datos'
urlpatterns = [

    path('', views.index, name='index'),

    # path for detail
    path('specifics/<int:vehiculo_id>/', views.detail, name = 'detail'),
    # path for results
    path('<int:registro_id>/results/', views.results, name = 'results'),
    path('lectura_actual', views.lecturaActual, name = 'lectura_actual'),
    # path for registro
    #path('<int:vehiculo_id>/vote/', views.vote, name = 'vote'),
]
comunicacion = comunicacion.Comunicacion()
comunicacion.conectarm()