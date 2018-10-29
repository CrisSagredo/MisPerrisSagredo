from django.db import models
from django.utils import timezone

class Postulante(models.Model):
    correo = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    fechaNacimiento = models.DateTimeField(
            default=timezone.now)
    telefono = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    tipoVivienda = models.CharField(max_length=200)
    fechaPostulacion = models.DateTimeField(
            blank=True, null=True)
            
def publish(self):
    self.fechaPostulacion = timezone.now()
    self.save()

def __str__(self):
    return self.nombre
