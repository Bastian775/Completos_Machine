from django.urls import path    
from . import views
from .views import listado_completo


app_name='main'

urlpatterns = [
    path('',views.index, name='index'),
    path('Completos.html/',views.Completos, name='Completos'),
    path('Registro.html/',views.Registro, name='Registro'),
    path('Listado_completos.html/',views.listado_completo, name='listado_completo'),
]
