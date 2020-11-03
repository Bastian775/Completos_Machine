from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import  Completo
# Create your views here.



def index(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Completos(request):
    template = loader.get_template('main/Completos.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Registro(request):
    template = loader.get_template('main/Registro.html')
    context = {}
    return HttpResponse(template.render(context, request))


def listado_completo(request):
    template = loader.get_template('main/Listado_completos')
    context = {}
    return HttpResponse(template.render(context, request))

