from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    
    nombre = models.CharField(max_length=60)
    brm = models.CharField(max_length=7)
    telefono = models.CharField(max_length=10)
    sucursal = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    es_gerente = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return f'{self.brm} {self.nombre}'

class Diario(models.Model):

    brm = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    temperatura = models.CharField(max_length=5)
    tos = models.BooleanField(default=False)
    cabeza = models.BooleanField(default=False)
    garganta = models.BooleanField(default=False)
    resfriado = models.BooleanField(default=False)
    malestar_general = models.BooleanField(default=False)
    respirar = models.BooleanField(default=False)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.brm.nombre

class DiarioPorFecha(models.Model):

    fecha = models.DateField(auto_now_add=True)
    diario_persona = models.ManyToManyField(Diario)
    gerente_turno = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Diario por fechas'

    def __str__(self):
        return f'{self.gerente_turno.nombre} : {self.fecha}'