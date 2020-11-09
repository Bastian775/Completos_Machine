from django.urls import path    
from .views import listado_completo, Completos, Registro , index, login, home



urlpatterns = [
    path('',home, name='home'),
    path('index.html',index, name='index'),
    path('Completos.html/',Completos, name='Completos'),
    path('Registro.html/',Registro, name='Registro'),
    path('Listado_completos.html/',listado_completo, name='listado_completo'),
    path('login.html/',login, name='login'),
]
