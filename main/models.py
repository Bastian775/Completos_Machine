from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=80)
    contraseña = models.CharField(max_length=80)

class Completo(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    precio = models.CharField(max_length=20)

# aqui me da problema
