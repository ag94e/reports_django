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

    respuestas = [
        ('SI', 'SI'),
        ('NO', 'NO')
    ]
    brm = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    temperatura = models.CharField(max_length=5)
    tos = models.CharField(max_length=2, choices=respuestas, default=None)
    cabeza = models.CharField(max_length=2, choices=respuestas, default=None)
    garganta = models.CharField(max_length=2, choices=respuestas, default=None)
    restriado = models.CharField(max_length=2, choices=respuestas, default=None)
    malestar_general = models.CharField(max_length=2, choices=respuestas, default=None)
    respirar = models.CharField(max_length=2, choices=respuestas, default=None)

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