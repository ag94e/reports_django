from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    
    nombre = models.CharField(max_length=60)
    brm = models.CharField(max_length=7)
    telefono = models.CharField(max_length=10)
    sucursal = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    es_gerente = models.BooleanField(default=False)


class Diario(models.Model):

    brm = models.ForeignKey(Perfil, on_delete=mdoels.CASCADE)
    temperatura = models.CharField(max_length=5)
    tos = models.BooleanField(default=False)
    cabeza = models.BooleanField(default=False)
    garganta = models.BooleanField(default=False)
    restriado = models.BooleanField(default=False)
    malestar_general = models.BooleanField(default=False)
    respirar = models.BooleanField(default=False)