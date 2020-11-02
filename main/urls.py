from django.urls import path    

from . import views


app_name='main'

urlpatterns = [
    path('',views.index, name='index'),
    path('Completos.html/',views.Completos, name='Completos'),
    path('Registro.html/',views.Registro, name='Registro'),
]
