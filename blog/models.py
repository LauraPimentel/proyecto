from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)
    edad = models.IntegerField()
    domicilio = models.CharField(max_length=50)
    tutor = models.CharField(max_length=30)
    tel_emergencia = models.CharField(max_length=30)
